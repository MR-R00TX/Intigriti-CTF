<div align="center">
🛡️ Intigriti CTF — Write-ups & Security Research
Web Exploitation · Vulnerability Analysis · Proof of Concepts
A structured collection of my solutions to Intigriti's monthly web security challenges.
![Platform](https://img.shields.io/badge/Platform-Intigriti-ED1C24?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Web%20Security-111827?style=for-the-badge&logo=owasp&logoColor=white)
![Writeups](https://img.shields.io/badge/Write--ups-2%20Solved-159957?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-English-007ACC?style=for-the-badge)
Maintained by MD Monirul Islam · `MR.R00TX`
GitHub Profile · LinkedIn · Intigriti
</div>
---
📖 About This Repository
Welcome to Intigriti-CTF, my hands-on web application security research notebook.
This repository documents how I approach authorized CTF challenges—from analyzing application behavior and identifying input vectors to reproducing vulnerabilities, understanding their impact, and recommending secure fixes.
Each write-up focuses on the reasoning behind the exploit, not just the final payload or flag.
What you'll find here:
Reconnaissance and application behavior analysis
Manual testing methodology and failed hypotheses
Reproducible, challenge-specific proof-of-concept scripts
HTTP requests, responses, and supporting evidence
Root cause discussion, impact assessment, and remediation
> [!IMPORTANT]
> **Authorized testing only.** The techniques and PoCs in this repository are documented for designated Intigriti CTF environments and other systems where explicit permission has been granted. Challenge flags and full solutions should be shared publicly only when the applicable disclosure rules allow it.
---
🏆 Challenge Archive
Challenge	Vulnerability	Key Technique	Result	Write-up
September 2026 — Critter Gallery	UNION-based SQL Injection	Base64 input analysis, MySQL enumeration	✅ Solved	Read Gist
October 2026 — Halloween Store	Race Condition · CWE-362	Concurrent HTTP/2 coupon redemption, business logic	✅ Solved	Read write-up
🔎 September 2026 — Critter Gallery
Vulnerability: UNION-based SQL Injection  
Attack surface: `GET /challenge.php?pic=...`
The application accepted Base64-encoded critter names. By decoding the parameter and testing the underlying query behavior, I identified a single-column SQL injection, confirmed a reflected `UNION SELECT`, and enumerated database metadata in the challenge environment.
Takeaway: Encoding is not sanitization; SQL queries need parameterization and appropriate database permissions.
📄 Full September write-up on GitHub Gist
⚡ October 2026 — Halloween Store
Vulnerability: Race Condition / TOCTOU · CWE-362  
Attack surface: `POST /api/cart/coupon`
The store rejected sequential duplicate coupon redemptions, but concurrent HTTP/2 requests exposed inconsistent enforcement. During a successful test, 9 of 13 requests were accepted, repeatedly applying `NEWS30` and `NIGHT20` and reducing a €666.00 cart to €0.00. The challenge was completed through a confirmed zero-cost checkout.
Takeaway: Coupon validation, redemption state changes, and checkout revalidation must withstand concurrent requests.
📄 October write-up · 🧪 Python race-condition PoC
---
🧠 My Testing Methodology
```text
Recon & First Look
        ↓
Map Inputs, Requests & State
        ↓
Build Hypotheses
        ↓
Test Manually & Capture Evidence
        ↓
Reproduce the Vulnerability
        ↓
Assess Impact & Root Cause
        ↓
Document Findings & Remediation
```
My write-ups distinguish directly observed results from inferred implementation details, and redact session cookies, credentials, and other sensitive values.
---
🛠️ Tools & Topics
Area	Tools / Concepts
HTTP & Web Testing	Burp Suite, browser developer tools, request/response analysis
Scripting	Python, `asyncio`, `httpx`
Injection Testing	SQL Injection, `UNION SELECT`, MySQL `information_schema`
Application Logic	Race Conditions, TOCTOU, coupon and checkout validation
Reporting	Reproduction steps, evidence, CWE classification, remediation
---
📂 Repository Structure
```text
Intigriti-CTF/
│
├── README.md                        # Repository overview (this file)
│
├── September-2026-Critter-Gallery/
│   └── README.md                    # Optional local copy of the Gist
│
└── October-2026-Halloween-Store/
    ├── README.md                    # Full October challenge write-up
    ├── assets/
    │   └── halloween-store-homepage.png
    └── poc/
        └── mixed_coupon_race.py
```
The September write-up is already available as a Gist; its local folder can be added later. The October folder structure matches the provided GitHub write-up package.
---
🔗 Explore My Other Security Work
🧪 PortSwigger Web Security Academy — Web vulnerability labs and learning notes
🖥️ HackTheBox — Offensive security lab write-ups
🚩 TryHackMe — CTF practice and technical notes
🛡️ Advanced Penetration Testing — Assessment methodologies and research notes
---
<div align="center">
Learn → Test → Understand → Document → Improve
Built for ethical security research and continuous learning.
![GitHub](https://img.shields.io/badge/GitHub-MR--R00TX-181717?style=flat-square&logo=github)
![LinkedIn](https://img.shields.io/badge/LinkedIn-MD%20Munna-0A66C2?style=flat-square&logo=linkedin)
</div>
