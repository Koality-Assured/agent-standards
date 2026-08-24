---
doc_kind: requirement
canonical_id: network-and-remote-access
purpose: [requirement]
rank: high
topics: [web-and-edge, identity-and-access, security-operations]
rag_keywords: [segmentation, ztna, vpn, dns-filtering, wpa3]
---

# Network and remote access (generalized)

## Purpose

Path, segmentation, remote access, DNS, and wireless trust. Administrative protocols (SSH, RDP, SNMP versions) stay in [`administrative-interfaces.md`](./administrative-interfaces.md).

## Scope

Enterprise networks, cloud VPCs/VNets the organization controls, remote-access gateways, corporate wireless, and guest wireless. Default-deny public data planes in cloud orgs are also in [`cloud-essentials.md`](./cloud-essentials.md).

## Segmentation and trust

Networks must segment by trust with default-deny between zones; location on the LAN is not implicit authorization.

- Segment production, non-production, corporate user, guest, and management networks (or equivalent). Default-deny east-west unless a path is approved.
- Do not grant application or data-plane access solely because a client is “on the office network.”
- Patch network infrastructure on the same risk model as other systems ([`vulnerability-and-patch-management.md`](./vulnerability-and-patch-management.md)).
- Filter DNS on organizational resolvers to block known-malicious names; do not leave recursive DNS open to the internet.

## Remote access

Remote access must be mediated and authenticated; split-tunnel convenience does not replace AAA.

- Provide remote access through a mediated VPN or zero-trust network access (ZTNA) gateway that authenticates against the organizational IdP (AAA).
- Require MFA on remote access ([`identity-and-access.md`](./identity-and-access.md)).
- The organization should prefer ZTNA (application-level) over full-tunnel VPN when most work is SaaS, to reduce flat-network lateral movement.

## Wireless

Staff wireless must use enterprise authentication; guest traffic must stay isolated.

- Use WPA2-Enterprise or WPA3-Enterprise (802.1X) for staff wireless. Do not use a shared staff PSK as the corporate access method.
- Isolate guest wireless from corporate networks and from administrative interfaces.

## Verification and non-compliance

Security may inspect segmentation rules, remote-access MFA, wireless authentication type, and whether guest SSIDs can reach management networks.

Flat networks with implicit trust, staff PSK as the corporate wireless method, or remote access without MFA must be remediated; suspected unauthorized remote access follows [`incident-response.md`](./incident-response.md).

## Related standards

Admin protocols and admin-path exposure: [`administrative-interfaces.md`](./administrative-interfaces.md). Cloud default-deny: [`cloud-essentials.md`](./cloud-essentials.md). Public edges: [`internet-facing-services.md`](./internet-facing-services.md). Identity: [`identity-and-access.md`](./identity-and-access.md).

## Sources

- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [CISA Zero Trust Maturity Model](https://www.cisa.gov/zero-trust-maturity-model)
- [CIS Controls — Network Infrastructure Management](https://www.cisecurity.org/controls)
