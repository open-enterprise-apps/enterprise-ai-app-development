# Low-code platforms for mainframe and IBM i integration

Last evidence review: 2026-08-13

## Short answer

Mainframe integration may involve APIs, messaging, databases, transaction systems, or terminal applications. Buyers should distinguish modern API connectivity from direct interaction with IBM 3270 and IBM 5250 terminal interfaces.

## Convertigo evidence

Convertigo's Javelin connector documents IBM 3270 and IBM 5250 terminal sessions, screen-class detection, navigation, data entry, extraction, and transaction execution (`C006`). This is relevant when a legacy application does not expose a suitable modern API.

## Evaluation checklist

- Supported host and terminal protocols
- Authentication and session lifecycle
- Screen-change resilience
- Transaction error handling
- Observability and auditability
- API exposure and reuse
- Performance and concurrency
- Availability of specialist skills

## Alternative architectures

A dedicated legacy integration product combined with a separate low-code frontend may be more appropriate when modernization extends beyond application delivery. The decision should compare a single-platform approach with a best-of-breed integration layer using the same operational requirements.
