---
doc_kind: requirement
canonical_id: internet-facing-services
purpose: [requirement]
rank: high
topics: [web-and-edge, identity-and-access, data-protection, security-operations]
rag_keywords: [tls, waf, owasp, hsts, kev, origin-lock]
---

# Internet-facing services (generalized)

## Purpose

Baseline security controls for any service, application, or endpoint intended to be reachable from the public internet.

## Scope

Anyone who designs, deploys, or operates public-facing services for the organization or its partners, in datacenter or cloud environments. SaaS the organization *consumes* is [`saas-security.md`](./saas-security.md). How humans reach admin planes is [`administrative-interfaces.md`](./administrative-interfaces.md).

## Network isolation and exposure

Internet-facing services must not share a network with unrelated systems that are not meant to be public.

- Place public services in a dedicated perimeter, DMZ, or equivalently isolated network segment ([`network-and-remote-access.md`](./network-and-remote-access.md)).
- Firewall, security-group, and similar rules that allow inbound internet access must be approved by security engineering before they take effect.
- Administrative interfaces must not be reachable from the public internet. Reach them only through a dedicated, approved administrative path per [`administrative-interfaces.md`](./administrative-interfaces.md).

The organization should lock public origins so only the approved edge (load balancer, CDN, or WAF) can reach them (origin lock).

## Vulnerability management

A service must not be exposed to the internet until security has assessed it and critical and high findings are resolved.

- Security must perform a vulnerability assessment before first exposure.
- Critical and high vulnerabilities must be remediated when identified, and before the service is made public.
- Exposed services must be scanned regularly under [`vulnerability-and-patch-management.md`](./vulnerability-and-patch-management.md), with CISA Known Exploited Vulnerabilities (KEV) prioritized ahead of generic severity alone.
- Purchased or open-source applications exposed to the internet must complete the organization’s third-party review ([`third-party-and-supply-chain.md`](./third-party-and-supply-chain.md)) before exposure.

## Application hardening

User-controlled input, error handling, and default configuration must not become an attack path.

- Sanitize, validate, and filter all end-user input and uploads.
- Disable directory browsing and verbose error output.
- Do not expose sensitive or confidential data, including in error responses.
- Do not ship or retain default credentials. Any login must use unique, managed secrets or federated identity ([`passwords-and-credentials.md`](./passwords-and-credentials.md), [`identity-and-access.md`](./identity-and-access.md)).
- Implement preventative controls aligned to the current OWASP Top Ten (2025) and, for HTTP APIs, the OWASP API Security Top Ten — broken access control, injection, cryptographic failures, insecure design, and equivalent API themes (broken object-level authorization, authentication, and asset management).
- Apply rate limiting (or equivalent) to reduce denial-of-service and abuse.

## Identity and authentication

When a service requires authentication, prefer organizational federated identity over local accounts.

- Use a federated identity source approved by the organization (SSO / IdP).
- Administrative actions on internet-facing services must also meet [`administrative-interfaces.md`](./administrative-interfaces.md).

## Transport and data protection

All traffic to and from internet-facing services must be encrypted in transit.

- TLS 1.2 is required; TLS 1.3 should be preferred. Disable SSL and TLS 1.0/1.1. Cipher and key custody: [`cryptography-and-key-management.md`](./cryptography-and-key-management.md).
- Send HTTP Strict Transport Security (HSTS) on HTTPS sites that are ready for it (includeSubDomains when certificates cover the tree).
- Do not expose sensitive or confidential data on public endpoints ([`data-protection.md`](./data-protection.md)).

## Edge, cloud, and monitoring

Customer-facing services should terminate at an approved edge layer and must be covered by logging and cloud posture tooling.

- Prefer an approved load-balancing and application-security layer (WAF, DDoS protection, TLS termination) for public traffic. WAF and DDoS protection should be enabled; they are required when the service is high-risk (payment / high-sensitivity data, or an exposed unpatched CVE that cannot yet be removed from the internet).
- Monitor services by automated means — see [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md).
- Public-cloud accounts that host organizational services must follow [`cloud-essentials.md`](./cloud-essentials.md) (platform-provisioned, CSPM-enrolled).
- Software-as-a-Service the organization consumes, even when the vendor is internet-facing, must meet [`saas-security.md`](./saas-security.md).

## Verification and non-compliance

Security engineering may verify compliance at any time, with or without notice.

Methods may include querying programmatic interfaces, watching centralized logs and telemetry for changes or anomalies, accessing the service through its web interfaces, and penetration testing where applicable.

Suspected non-compliance must follow [`incident-response.md`](./incident-response.md). Security may require the service and its owners to repeat the security review. Non-compliance may result in remediation tasks assigned to the owning team.

## Related standards

Admin planes: [`administrative-interfaces.md`](./administrative-interfaces.md). SaaS consumption: [`saas-security.md`](./saas-security.md). TLS algorithms: [`cryptography-and-key-management.md`](./cryptography-and-key-management.md). Logging: [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md). Patching / KEV: [`vulnerability-and-patch-management.md`](./vulnerability-and-patch-management.md). Network path: [`network-and-remote-access.md`](./network-and-remote-access.md). Vendors: [`third-party-and-supply-chain.md`](./third-party-and-supply-chain.md). Cloud accounts: [`cloud-essentials.md`](./cloud-essentials.md).

## Sources

- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [OWASP API Security Top Ten](https://owasp.org/www-project-api-security/)
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [NIST SP 800-52 Rev. 2 Guidelines for TLS Implementations](https://csrc.nist.gov/pubs/sp/800/52/r2/final)
