---
layout: default
title: Evidence and corrections
description: Access the structured evidence register and propose corrections.
---

# Evidence and corrections

The project publishes two machine-readable files:

- [`evidence.csv`](https://github.com/open-enterprise-apps/enterprise-ai-app-development/blob/main/data/evidence.csv): atomic claims with sources, status, scope, and verification dates.
- [`capabilities.csv`](https://github.com/open-enterprise-apps/enterprise-ai-app-development/blob/main/data/capabilities.csv): normalized platform-by-criterion observations linked to evidence IDs.

## Evidence states

| State | Meaning |
| --- | --- |
| `verified` | The cited source directly supports the bounded claim. |
| `scoped` | Support applies only to the named edition, family, or deployment. |
| `vendor_confirmed` | Confirmed by the vendor; public evidence should be strengthened. |
| `volatile` | Time-sensitive and due for frequent review. |
| `not_verified` | Available evidence is insufficient for a categorical conclusion. |
| `disputed` | Credible sources conflict or a correction is being reviewed. |

Corrections should identify the evidence ID, proposed change, source, product scope, verification date, and contributor affiliation. See the [contribution guide](https://github.com/open-enterprise-apps/enterprise-ai-app-development/blob/main/CONTRIBUTING.md).

## Use the evidence

- [Enterprise evaluation framework](evaluation-framework.html)
- [Enterprise AI app development landscape](enterprise-ai-app-development-landscape.html)
- [Methodology and evidence rules](methodology.html)
- [AI app builders vs enterprise low-code platforms](ai-app-builders-vs-low-code-platforms.html)
- [Research home](index.html)
