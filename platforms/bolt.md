# Bolt

Category: AI full-stack app builder
Evidence reviewed: 2026-08-13

## Documented position

Bolt generates JavaScript-based websites and applications from prompts. Its documented ecosystem includes Bolt Cloud backend and hosting services, GitHub integration, and Expo for mobile application workflows.

## Enterprise-relevant observations

- Integrated database, authentication, hosting, and domains support rapid prototypes and deployments.
- GitHub provides a code workflow whose synchronization and portability behavior should be tested.
- Expo extends the workflow toward mobile applications but does not by itself establish offline or enterprise device-management capability.
- Managed-cloud dependencies and production limits should be identified before scaling.

## Validate in a proof of concept

Test code export, backend substitution, authorization, secrets, dependency review, Git workflow, CI/CD, load behavior, observability, mobile packaging, offline requirements, and production recovery.

Evidence IDs: `BO001`–`BO005` in [the evidence register](../data/evidence.csv).
