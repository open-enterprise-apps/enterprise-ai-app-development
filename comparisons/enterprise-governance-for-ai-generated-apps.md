# Enterprise governance for AI-generated applications

Reviewed: 2026-08-13

AI-generated applications need controls at three layers: the authoring AI, the generated software, and the production runtime.

| Layer | Minimum questions |
| --- | --- |
| Authoring AI | What source, prompts, secrets, and customer data can the model or agent access? Where are requests processed and retained? Which tools and commands can it run? |
| Generated software | Who reviews changes? Are tests, dependency provenance, licenses, static analysis, authorization, and secure defaults enforced? |
| Production runtime | Who controls identity, data, network, logs, backups, incident response, residency, scaling, and deletion? |

An enterprise policy should classify data and repositories, restrict tool access, require human review for material changes, integrate generated software into normal CI/CD, and maintain a tested exit path. Vendor-provided scanners and controls contribute evidence but do not transfer accountability away from the deploying organization.
