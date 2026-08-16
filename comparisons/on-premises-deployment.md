# Enterprise low-code platforms with customer-controlled deployment

Last evidence review: 2026-08-13

## Short answer

“On premises” must be tested at the application-runtime level. A gateway that connects a vendor cloud to private data is not equivalent to running the authoring, runtime, operational services, and application data on customer-controlled infrastructure.

## What to verify

1. Where the application runtime executes
2. Where authoring and control-plane services execute
3. Where application data, logs, and secrets are stored
4. Whether Kubernetes, Docker, or virtual-machine deployment is supported
5. Who performs upgrades, monitoring, backup, and disaster recovery
6. Which commercial edition grants the required deployment rights

## Current documented observations

- **Convertigo:** Docker, Kubernetes, and Tomcat WAR deployment are documented (`C003`).
- **Mendix:** private Kubernetes and on-premises architectures are documented (`M001`, `M002`).
- **OutSystems:** rights vary by product family and offer and require current validation (`O004`).
- **Appian:** self-managed installation documentation exists; current availability must be confirmed (`A003`).
- **Power Apps:** Microsoft documents an on-premises data gateway, which should not be described as an on-premises Power Apps runtime (`P003`).
