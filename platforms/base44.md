# Base44

Category: AI full-stack app builder
Evidence reviewed: 2026-08-13

## Documented position

Base44 combines AI-assisted application creation with a managed backend covering identity, data entities, connectors, and backend functions. It also documents two-way GitHub synchronization and a CLI that external coding agents can use.

## Enterprise-relevant observations

- The managed backend reduces initial assembly work but creates service dependencies that must be mapped.
- GitHub synchronization and local development are plan-scoped and have documented limitations.
- Enterprise controls include SSO, SCIM, audit logs, and IP allowlists according to current documentation.
- Agent and CLI access should be governed as privileged development access.

## Validate in a proof of concept

Test data export, schema migration, code synchronization, backend replacement, identity integration, authorization, audit coverage, residency, rate limits, recovery, and post-export operations.

Evidence IDs: `BA001`–`BA005` in [the evidence register](../data/evidence.csv).
