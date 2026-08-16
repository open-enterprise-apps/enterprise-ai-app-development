# Cursor

Category: AI coding tool and agent
Evidence reviewed: 2026-08-13

## Documented position

Cursor is an AI-assisted code editor and agent environment. Its agents can inspect repositories, edit multiple files, run commands, use MCP tools, and perform work asynchronously in remote environments.

## Category boundary

Cursor is not, by itself, an application runtime or managed enterprise application platform. The engineering team remains responsible for architecture, frameworks, databases, identity, deployment, observability, security, and ongoing operations.

## Enterprise-relevant observations

- Repository-native work can fit established review, testing, and CI/CD practices.
- Terminal, internet, and MCP access create a powerful permission surface.
- Cursor documents privacy modes while stating that requests route through its infrastructure.
- Team controls include SSO, SCIM, model controls, repository blocklists, and MCP configuration, subject to plan.

## Validate in a proof of concept

Test data-flow policy, repository access, generated-code review, command approval, MCP allowlists, secret isolation, dependency provenance, test quality, auditability, and incident response.

Evidence IDs: `CU001`–`CU005` in [the evidence register](../data/evidence.csv).
