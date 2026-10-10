---
doc_kind: requirement
canonical_id: network-and-remote-access
purpose: [requirement, security]
rank: high
topics: [web-and-edge, identity-and-access, security-operations]
rag_keywords: [segmentation, ztna, vpn, dns-filtering, wpa3, network-zones, inspection-transit]
---

# Network and remote access (generalized)

## Purpose

Network architecture, zone segmentation, remote access, DNS filtering, and wireless security requirements across enterprise, datacenter, and cloud environments. Administrative protocols (SSH, RDP, SNMP versions) are governed in [`administrative-interfaces.md`](./administrative-interfaces.md).

## Scope

All enterprise physical networks, cloud virtual networks (VPCs/VNets), remote-access gateways, software-defined perimeters, corporate wireless infrastructure, and guest networks operated or accessed by the organization.

## Architectural network zones and segmentation

Networks must enforce trust boundaries with default-deny routing between logical zones; presence on a physical or logical LAN never confers authorization.

The enterprise network architecture must be partitioned into distinct security zones:

### 1. Production network zone

- Hosts live customer-facing applications, data stores, and production microservices.
- Enforce default-deny east-west routing between subnets; all allowed paths must be explicitly defined and protocol-restricted.
- All intra-zone and inter-zone connections must be authenticated and encrypted using TLS 1.2+ or mutual TLS (mTLS).
- Direct inbound connections from development, staging, or corporate user subnets are strictly prohibited; connections must pass through an intermediary transit zone.
- Host-based firewalls must be enabled, tuned, and managed via Infrastructure as Code (IaC) across all production nodes.

### 2. Enterprise and pre-production network zone

- Hosts corporate user workstations, internal productivity services, and pre-production staging/development environments.
- Staging and development environments must be segmented from corporate end-user subnets.
- Pre-production workloads must not access production data stores directly.

### 3. Secure routing and transit inspection zone

- Dedicated transit network (e.g., cloud transit gateway, firewall hub, DMZ) hosting network security controls, stateful inspection firewalls, load balancers, and ZTNA ingress proxies.
- All inter-zone traffic traversing boundaries between separate security zones (e.g., enterprise to production, on-premises to cloud) must be routed through this zone for Layer 7 stateful inspection and security policy evaluation.
- All appliances and gateways within this zone must be centrally managed with audit logging enabled.

### 4. Legacy and quarantine network zone

- Isolated containment zone reserved for legacy systems, unpatchable appliances, or specialized vendor devices unable to meet baseline security standards.
- Inbound and outbound communications must be strictly constrained via restrictive Layer 3/4 Access Control Lists (ACLs) to only pre-approved, monitored destinations.
- Legacy zones must never have direct, unmediated access to production or enterprise subnets.

## Remote access and zero trust network access (ZTNA)

Remote access must be mediated, least-privileged, and authenticated against organizational identity.

- Prefer application-level Zero Trust Network Access (ZTNA) or software-defined perimeters over full-tunnel layer-3 VPNs to eliminate flat network exposure and prevent lateral movement.
- When VPNs are maintained, enforce split tunneling rules that mandate traffic to internal resources traverses the secure tunnel while public internet traffic routes independently, unless regulatory requirements dictate full-tunnel inspection.
- Enforce phishing-resistant Multi-Factor Authentication (MFA) on all remote access gateways prior to establishing connectivity per [`identity-and-access.md`](./identity-and-access.md).
- Integrate endpoint posture checks: Remote access gateways must verify client health (e.g., compliant EDR, disk encryption, patch level) before granting network access per [`endpoint-and-workstation.md`](./endpoint-and-workstation.md).

## DNS security and name resolution

Domain Name System (DNS) services must be protected against tampering and abuse.

- Protective DNS (PDNS): All internal endpoints and cloud VPCs must resolve external queries through managed protective DNS resolvers that actively block known malicious, phishing, and command-and-control (C2) domains.
- Prohibit open recursion: Internal recursive DNS resolvers must not be exposed to the public internet or untrusted guest networks.
- Enforce DNSSEC validation where supported to ensure the integrity of external DNS responses.

## Wireless infrastructure

Wireless networks must enforce strong cryptographic authentication and client isolation.

- Corporate wireless: Staff wireless networks must use WPA2-Enterprise or WPA3-Enterprise (IEEE 802.1X) authenticated against the organizational Identity Provider or RADIUS directory. Prohibit shared pre-shared keys (PSKs) for corporate network access.
- Guest wireless: Guest wireless networks must be completely isolated from corporate subnets, internal servers, and administrative interfaces. Enable client isolation on guest SSIDs to prevent peer-to-peer lateral communication.

## Verification and non-compliance

Security engineering may perform network segmentation audits, attempt cross-zone traversal, test remote-access MFA enforcement, and evaluate DNS filtering policies at any time.

Flat networks without inter-zone firewalls, shared corporate wireless PSKs, unauthenticated remote access paths, or unmonitored legacy systems outside of quarantine constitute critical control failures; suspected unauthorized lateral movement follows [`incident-response.md`](./incident-response.md).

## Related standards

Administrative interfaces: [`administrative-interfaces.md`](./administrative-interfaces.md). Zero Trust architecture: [`zero-trust-architecture.md`](./zero-trust-architecture.md). Cloud tenancy: [`cloud-essentials.md`](./cloud-essentials.md). Identity and MFA: [`identity-and-access.md`](./identity-and-access.md). Endpoint health: [`endpoint-and-workstation.md`](./endpoint-and-workstation.md).

## Sources

- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [CISA Zero Trust Maturity Model](https://www.cisa.gov/zero-trust-maturity-model)
- [CIS Controls — Network Infrastructure Management](https://www.cisecurity.org/controls)
- [NSA Protective DNS Guidance](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/2523274/nsa-and-cisa-release-guidance-on-protective-dns/)
