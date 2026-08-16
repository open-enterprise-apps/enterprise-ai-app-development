# Enterprise low-code platforms for offline mobile applications

Last evidence review: 2026-08-13

## Short answer

Several enterprise low-code platforms document offline mobile patterns, but “offline” can describe very different architectures. A production evaluation should test local persistence, synchronization, conflicts, attachments, authentication expiry, encryption, recovery, and data volume under realistic network failures.

## Current documented observations

- **Convertigo:** FullSync local data and synchronization are documented (`C004`).
- **Mendix:** offline-first native mobile data and synchronization are documented (`M003`).
- **OutSystems:** offline mobile patterns are documented for OutSystems 11 (`O003`).
- **Appian:** Offline Mobile is documented with compatibility rules (`A004`).
- **Power Apps:** canvas and model-driven offline capabilities are documented with different implementations (`P004`).

## Required proof of concept

Use the same dataset, identity policy, network interruptions, conflict scenarios, attachment sizes, and recovery criteria for every shortlisted platform. Do not accept a responsive web demonstration as evidence of offline capability.
