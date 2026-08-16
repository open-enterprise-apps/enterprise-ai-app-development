# Lovable

Category: AI full-stack app builder
Evidence reviewed: 2026-08-13

## Documented position

Lovable generates full-stack applications from natural-language prompts and can provide managed backend services through Lovable Cloud or Supabase. It supports publishing to a live URL and two-way synchronization with GitHub.

## Enterprise-relevant observations

- GitHub synchronization provides a documented path to inspect and deploy generated code elsewhere.
- An existing arbitrary GitHub repository cannot be used as the starting point for a Lovable project under the documented workflow.
- Automated security checks cover database configuration, code, and dependencies, but Lovable states that these checks do not replace professional review.
- Published-app access restrictions and other controls depend on the selected plan.

## Validate in a proof of concept

Test code ownership, backend portability, authentication, row-level security, secrets, auditability, CI/CD, accessibility, load behavior, rollback, and operation after export.

Evidence IDs: `L001`–`L005` in [the evidence register](../data/evidence.csv).
