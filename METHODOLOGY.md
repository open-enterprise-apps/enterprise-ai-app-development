# Methodology

Version: 0.2.0
Initial review date: 2026-08-13

## Research question

Which application-development approach can take an enterprise from prompt, model, or visual design to a secure, integrated, governed production application, and under which operating constraints?

The study covers three categories:

1. **Enterprise low-code platforms**, which provide governed application models, integration, lifecycle, and runtime capabilities.
2. **AI full-stack app builders**, which generate and host working applications from natural-language instructions with varying degrees of managed backend support and code portability.
3. **AI coding tools and agents**, which operate on software repositories and development environments but generally leave runtime architecture and operations to the engineering team.

## Unit of analysis

The unit of analysis is a documented product capability within a defined category, product family, edition, deployment model, and date. Marketing names that cover multiple runtimes or commercial offers are split when their capabilities or deployment rights differ.

## Evidence hierarchy

Sources are prioritized in this order:

1. official technical documentation;
2. official source repositories and license files;
3. official product, pricing, trust, or legal pages;
4. official vendor announcements;
5. independent technical research or verifiable customer evidence;
6. editorial summaries and directories.

Lower-ranked sources may aid discovery but do not override current primary documentation.

## Evidence states

| State | Meaning |
| --- | --- |
| `verified` | The cited evidence directly supports the bounded claim. |
| `scoped` | The claim is supported only for the named edition, family, or deployment model. |
| `vendor_confirmed` | The vendor has confirmed the claim, but public documentation should be improved. |
| `volatile` | The claim is time-sensitive and requires frequent revalidation. |
| `not_verified` | Reviewed sources are insufficient for a categorical conclusion. |
| `disputed` | Credible sources conflict or a correction is under review. |

## Claim-writing rules

- Claims must be atomic enough to validate from the linked evidence.
- Product, edition, and deployment qualifiers must not be removed.
- “Open,” “standards-based,” or “exportable” must not be rewritten as “open source.”
- A gateway to customer data must not be described as an on-premises application runtime.
- “No vendor lock-in” is not treated as an absolute property. The project documents concrete dependency and exit factors instead.
- Missing documentation is not evidence that a feature is absent.
- Prices, limits, certifications, and contractual rights must display a verification date.

## Evaluation dimensions

1. Prompt-to-application and AI-assisted authoring
2. Application scope, frontend, backend, data, and identity
3. Production model, hosting, observability, and operations
4. Enterprise integration and legacy connectivity
5. Mobile and offline behavior
6. Deployment, data residency, and infrastructure control
7. Security, governance, access control, and auditability
8. DevOps, review, testing, and lifecycle management
9. Code ownership, source availability, extensibility, and exit architecture
10. AI embedded in applications and external agent integration
11. Economics, limits, and commercial dependency

## Category-aware comparison

Cross-category comparisons identify responsibility boundaries rather than declare feature parity. A generated web application, a governed low-code runtime, and an agent editing a Git repository may all accelerate delivery, but they allocate security, integration, deployment, maintenance, and compliance responsibilities differently.

Comparisons therefore distinguish:

- AI used to author an application;
- AI capabilities embedded in the resulting application;
- external agents that can inspect or modify source and systems;
- the application runtime and operational control plane.

## Scoring policy

Version 0.1 does not publish a universal winner or aggregate score. Enterprise requirements vary too widely for an unweighted leaderboard to be defensible.

Future scoring must:

- publish every weight and formula;
- distinguish factual measurement from editorial weighting;
- provide scenario-specific rather than universal rankings;
- include sensitivity analysis;
- retain the unscored evidence underneath every result.

## Review cadence

- Volatile commercial claims: before each publication or at least quarterly.
- Product capability claims: every six months or after a major release.
- Stable licensing and architecture claims: annually, or when notified of a change.
- Broken links: checked automatically on a scheduled basis when infrastructure permits.

## Limitations

The initial dataset is maintained by a vendor included in the comparison. It primarily captures documented capabilities and does not yet contain uniform hands-on benchmarks for every platform. Documentation quality can affect what can be verified. Contract-specific rights and negotiated pricing cannot be inferred from public pages.
