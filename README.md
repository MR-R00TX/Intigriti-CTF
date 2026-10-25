<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:620012,100:D90429&height=210&section=header&text=INTIGRITI%20CTF&fontSize=66&fontColor=FFFFFF&fontAlignY=37&desc=Web%20Security%20Research%20%7C%20Write-ups%20%7C%20Proofs%20of%20Concept&descSize=17&descAlignY=59&descColor=FFC2CB" alt="Intigriti CTF — Web Security Research" width="100%" />

# 🛡️ Intigriti CTF — Challenge Write-ups

**Monthly web security challenges · Reproducible research · Technical remediation**

[![Platform](https://img.shields.io/badge/Platform-Intigriti-D90429?style=for-the-badge)](https://www.intigriti.com/)
[![Category](https://img.shields.io/badge/Focus-Web%20Security-161B22?style=for-the-badge)](https://owasp.org/www-project-web-security-testing-guide/)
![Write-ups](https://img.shields.io/badge/Documented%20Challenges-02-BC1C32?style=for-the-badge)
![Language](https://img.shields.io/badge/PoC-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![Author](https://img.shields.io/badge/Author-MR--R00TX-0D1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MR-R00TX)

*Analyze the behavior. Validate the weakness. Demonstrate the impact. Document the fix.*

</div>

---

## 📜 [ 0x01 ] About This Repository

> **Research log:** `[+] Authorized CTF environment detected — documentation initialized`

Welcome to **Intigriti-CTF**, my collection of technical write-ups for Intigriti's web security challenges.

Each case study documents the path from **initial observations** to **vulnerability discovery**, **proof-of-concept validation**, **impact analysis**, and **remediation**. The goal is not just to capture a flag, but to explain *why* the vulnerability exists and how a developer can prevent it.

**Research focus:** Web application security, SQL injection, HTTP/API testing, concurrency vulnerabilities, and business logic abuse.

## 🗂️ [ 0x02 ] Challenge Archive

| Month | Challenge | Vulnerability | Technical Highlight | Write-up |
|:---|:---|:---|:---|:---|
| **September 2026** | **Critter Gallery** | SQL Injection · `CWE-89` | Base64-decoded `pic` parameter → UNION-based SQL injection → database enumeration | [Read published Gist](https://gist.github.com/MR-R00TX/76d7802c6ad63295c5ec8b3a02f97f7d) |
| **October 2026** | **Halloween Store** | Race Condition · `CWE-362` | Concurrent coupon redemption → unauthorized discount stacking → zero-cost checkout | [Read case study](./October-2026-Halloween-Store/README.md) |

> **Publication note:** Challenge solutions and flags should be made public only when permitted by the organizer's disclosure rules. The October case-study link becomes active after its `README.md` is uploaded to the folder shown below.

## 🔎 [ 0x03 ] Featured Research

### `0x01` — Critter Gallery | September 2026

**Category:** UNION-based SQL Injection (`CWE-89`)

- Identified a Base64-encoded `pic` GET parameter (`Zm94` → `fox`).
- Tested the decoded input and confirmed SQL injection with `ORDER BY` and `UNION SELECT`.
- Fingerprinted **MySQL 8.0.46** and explored `information_schema`.
- Demonstrated unauthorized access to the challenge's `secret_vault` table.

**Key lesson:** Encoding an input does not make it safe for SQL queries. Use parameterized queries and least-privilege database accounts.

**Full write-up:** [Critter Gallery — Intigriti September 2026](https://gist.github.com/MR-R00TX/76d7802c6ad63295c5ec8b3a02f97f7d)

### `0x02` — Halloween Store | October 2026

**Category:** Race Condition / Business Logic (`CWE-362`)

**Target workflow:** `POST /api/cart/coupon` → `GET /api/cart` → `POST /api/checkout`

- Normal duplicate coupon submissions returned **HTTP 409 Conflict**.
- A synchronized set of **13 concurrent HTTP/2 requests** resulted in **9 accepted redemptions**.
- The cart recorded `NEWS30` **5 times** and `NIGHT20` **4 times**.
- The **nominal** promotional discount reached **230%**, while the effective discount was capped at the order subtotal.
- The payable amount fell from **€666.00** to **€0.00**; checkout was successfully completed in the challenge environment.

**Key lesson:** A validation check that works for sequential requests may fail under concurrency. Enforce usage limits atomically and revalidate promotions at checkout.

**Technical case study:** [Halloween Store — Intigriti October 2026](./October-2026-Halloween-Store/README.md)

## ⚔️ [ 0x04 ] Tools & Techniques

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![httpx](https://img.shields.io/badge/httpx-HTTP%2F2-1F6FEB?style=flat-square)
![asyncio](https://img.shields.io/badge/asyncio-Concurrency-C2185B?style=flat-square)
![Burp Suite](https://img.shields.io/badge/Burp%20Suite-FF6633?style=flat-square&logo=burpsuite&logoColor=white)
![DevTools](https://img.shields.io/badge/Browser-DevTools-3B82F6?style=flat-square)
![MySQL](https://img.shields.io/badge/MySQL-SQLi%20Analysis-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-Documentation-000000?style=flat-square&logo=markdown&logoColor=white)

</div>

| Area | Approach |
|:---|:---|
| **Attack-surface analysis** | Identify routes, parameters, state transitions, and security controls |
| **Web/API testing** | Examine HTTP requests, responses, cookies, and server-side behavior |
| **Injection analysis** | Compare SQL behavior, identify reflection points, and validate impact |
| **Concurrency testing** | Use Python `asyncio`, `httpx`, and synchronized requests |
| **Business logic** | Test pricing rules, coupon restrictions, checkout state, and authorization |
| **Documentation** | Reproducible steps, redacted evidence, root cause, and recommended fixes |

## 🧭 [ 0x05 ] Research Methodology

```text
┌─────────────────────── INTIGRITI CTF WORKFLOW ───────────────────────┐
│                                                                     │
│  01  INITIAL RECON     →  Understand the challenge and attack surface│
│  02  BEHAVIOR MAPPING  →  Study requests, parameters, and state      │
│  03  HYPOTHESIS       →  Identify a possible security weakness      │
│  04  VALIDATION       →  Test safely in the authorized environment  │
│  05  IMPACT PROOF     →  Capture reproducible evidence              │
│  06  ROOT CAUSE       →  Explain the technical failure              │
│  07  REMEDIATION      →  Recommend practical defensive controls     │
│  08  WRITE-UP         →  Share findings when disclosure is allowed  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## 📂 [ 0x06 ] Repository Structure

This is the **recommended layout** as the archive grows:

```text
Intigriti-CTF/
│
├── README.md                           # Main repository overview
│
├── September-2026-Critter-Gallery/
│   ├── README.md                       # SQL injection write-up
│   └── assets/                         # Screenshots (optional)
│
└── October-2026-Halloween-Store/
    ├── README.md                       # Race condition write-up
    ├── mixed_coupon_race.py            # Authorized challenge PoC
    └── assets/
        ├── halloween-store-homepage.png # Challenge screenshot
        └── POC.png                     # Race condition exploitation evidence

```

The **September write-up** is already accessible via the Gist linked above. Local archive folders are added as their files are committed. Avoid uploading active session cookies, credentials, or unredacted personal information.

## 📝 [ 0x07 ] Write-up Standards

Every published write-up aims to include:

1. **Challenge Overview** — context, objective, and relevant application behavior.
2. **Discovery Process** — initial observations and test hypotheses.
3. **Proof of Concept** — precise steps, HTTP requests, and scripts when relevant.
4. **Observed Results** — response data, screenshots, and measurable outcomes.
5. **Root Cause** — an evidence-based explanation, with unverified assumptions clearly identified.
6. **Security Impact** — demonstrated effect versus potential real-world impact.
7. **Remediation** — specific server-side and persistence-layer controls.
8. **Key Takeaways** — transferable security lessons.

## 🔐 [ 0x08 ] Responsible Disclosure

> [!IMPORTANT]
> This repository documents **authorized Intigriti CTF exercises**. It is not permission to test unrelated infrastructure.

- Respect each challenge's scope, terms, and publication rules.
- Keep solutions and flags private until public disclosure is allowed.
- Redact session identifiers, credentials, tokens, and personal data.
- Distinguish confirmed observations from inferred implementation details.
- Reuse the techniques only in environments where you have explicit authorization.

## 👤 [ 0x09 ] About the Author

**MD Monirul Islam** — **MR.R00TX**  
*Web Application Security · Offensive Security Research · CTF Write-ups*

This archive complements my other hands-on security research and documentation projects:

| Portfolio | Focus |
|:---|:---|
| [PortSwigger Web Security Academy](https://github.com/MR-R00TX/PortSwigger-Web-Security-Academy) | Web vulnerability labs and analysis |
| [HackTheBox](https://github.com/MR-R00TX/HackTheBox) | Machine walkthroughs and exploitation methodology |
| [TryHackMe](https://github.com/MR-R00TX/TryHackMe) | Practical security challenges |
| [Advanced Penetration Testing](https://github.com/MR-R00TX/Advanced-Penetration-Testing) | Lab assessments, techniques, and reporting |

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-MR--R00TX-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MR-R00TX)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-mdmunna--sec-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mdmunna-sec/)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:munna@seccrown.com)

---

**Research. Validate. Document. Secure.**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:620012,100:D90429&height=110&section=footer" alt="Footer wave" width="100%"/>

</div>
