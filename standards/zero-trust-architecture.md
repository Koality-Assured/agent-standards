---
doc_kind: requirement
canonical_id: zero-trust-architecture
purpose: [requirement, architecture]
rank: high
topics: [cross-cutting-controls, identity-and-access, web-and-edge]
rag_keywords: [zero-trust, nist-800-207, pdp, pep, cisa-ztmm, continuous-verification, least-privilege]
---

# Zero trust architecture (generalized)

## Purpose

Architectural tenets, operational principles, and technical requirements for implementing Zero Trust across organizational identities, devices, networks, applications, and data planes.

## Scope

All enterprise infrastructure, cloud environments, corporate networks, applications, microservices, end-user devices, and non-human identities operated by or connecting to the organization. Network transport mechanics are in [`network-and-remote-access.md`](./network-and-remote-access.md). Identity federation controls are in [`identity-and-access.md`](./identity-and-access.md).

## Core tenets of zero trust

Architecture and engineering teams must design systems adhering to the foundational tenets defined in NIST SP 800-207:

- All data sources and computing services are considered discrete resources.
- Secure communication regardless of network location: Network location alone never implies trust. Access requests originating from internal enterprise networks must meet the exact same authentication, authorization, and encryption requirements as requests originating from public or external networks. Systems must operate under the assumption that an adversary is present on the network.
- Per-session, per-request access: Access to individual enterprise resources is granted on a per-session and per-transaction basis. Authentication to one resource must never grant implicit access to another resource.
- Dynamic policy enforcement: Access to resources is governed by dynamic policy—evaluating the observable state of subject identity, device health, service status, contextual attributes, and environmental variables.
- Asset posture monitoring: The organization continuously monitors, measures, and inventories the security posture of all physical, virtual, and cloud assets accessing enterprise resources.
- Dynamic authentication and authorization: All resource access is strictly authenticated and authorized using least privilege before access is granted.
- Continuous diagnostics and telemetry: Telemetry from assets, network infrastructure, identity events, and application requests is continuously analyzed to detect anomalies and adjust trust decisions.

## Policy decision and enforcement architecture

Zero Trust environments must separate policy evaluation from traffic transport.

- Policy Decision Point (PDP): Access decisions must be made by a centralized, auditable Policy Engine (PE) and Policy Administrator (PA) evaluating current context against established access policies.
- Policy Enforcement Point (PEP): Traffic must be gated by explicit enforcement points (e.g., application proxies, ZTNA gateways, API gateways, service mesh sidecars) that enforce decisions rendered by the PDP. PEPs must terminate connections and prevent direct network-layer access to underlying application origins.
- Plane separation: Control plane signaling (authentication, posture evaluation, policy delivery) must remain logically and cryptographically separated from the underlying data plane traffic.

## Continuous evaluation and adaptive access

Trust decisions must be adaptive and persistent throughout active sessions.

- Trust is not a one-time gate: Authentication at the beginning of a user session does not confer standing trust. The PDP must continuously evaluate signals throughout the session lifecycle.
- Risk-based step-up authentication: Significant contextual changes (such as device compliance degradation, unusual geographic jumps, high-risk IP addresses, or anomalous data export volumes) must trigger automated re-authentication, step-up MFA, or immediate session revocation.

## Subject and device binding

Access decisions must evaluate both the actor and the client device.

- Subject credentials alone are insufficient: Authentication to sensitive or internal enterprise resources requires both a validated subject identity and a verified, compliant device identity.
- Hardware-backed device trust: Managed devices must possess hardware-rooted identity certificates (e.g., stored in a TPM or Secure Enclave) issued and verified by organizational device management systems.
- Posture verification: Devices must pass continuous posture checks (e.g., EDR active and healthy, OS patch floor met, full-disk encryption active, screen lock configured) prior to being granted access to internal or production resources.

## Workload-to-workload and data micro-segmentation

Internal services must enforce Zero Trust across east-west application traffic.

- Micro-segmentation: Applications and microservices must not reside on flat networks. Segment workloads using network policies, service mesh mutual TLS (mTLS), or software-defined perimeters.
- Workload identity: Service-to-service communication must authenticate cryptographically using short-lived workload identity tokens (e.g., SPIFFE/SPIRE, cloud workload identity, mTLS certificates) rather than shared network IP trust.
- Data protection: Protect data at rest and in transit regardless of storage medium or network transit route, enforcing access controls directly at the data and API layers.

## Verification and non-compliance

Security engineering may evaluate trust scoring algorithms, test PEP enforcement by simulating unmanaged devices or compromised networks, and audit session lifetime configurations at any time.

Flat network segments with implicit trust, services granting access based solely on IP origin, unmanaged devices accessing sensitive corporate resources without posture evaluation, or standing cross-resource privileges constitute architectural failures; confirmed unauthorized lateral movement follows [`incident-response.md`](./incident-response.md).

## Related standards

Network segmentation and remote access: [`network-and-remote-access.md`](./network-and-remote-access.md). Identity and MFA: [`identity-and-access.md`](./identity-and-access.md). Endpoint health: [`endpoint-and-workstation.md`](./endpoint-and-workstation.md). Privileged access: [`privileged-access.md`](./privileged-access.md). Data protection: [`data-protection.md`](./data-protection.md).

## Sources

- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [CISA Zero Trust Maturity Model Version 2.0](https://www.cisa.gov/zero-trust-maturity-model)
- [DoD Zero Trust Reference Architecture](https://dodcio.defense.gov/Portals/0/Documents/Library/DoD-ZTReferenceArchitecture-v2.0(Aug2022).pdf)
