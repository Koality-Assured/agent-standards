---
doc_kind: requirement
canonical_id: privileged-access
purpose: [requirement]
rank: high
topics: [identity-and-access, security-operations, governance]
rag_keywords: [jit, paw, break-glass, privileged, elevation]
---

# Privileged access (generalized)

## Purpose

How privileged identities are issued, elevated, and recovered. This page is identity, just-in-time (JIT) access, privileged workstations, and IdP/cloud emergency accounts — not the network, TLS, or protocol list for reaching admin planes.

## Scope

Any role that can change identity, cloud organization, production infrastructure, security controls, or large sets of sensitive data. How those planes are reached on the network is [`administrative-interfaces.md`](./administrative-interfaces.md). Local device break-glass accounts stay on that page.

## What counts as privilege

The organization must define privilege in writing so standing access is not left to tribal knowledge.

- Treat as privileged at least: IdP administrator, cloud root / organization owner, security-tool admin, production infrastructure admin, and ability to read or export Restricted data at scale.
- Cloud root, organization owner, and IdP administrator are tier-0. Non-human identities with the same abilities are still privileged.
- Recertify privileged membership at least quarterly.

## Dedicated identities and elevation

Privileged work must not use a person’s daily-driver identity as the standing path.

- Issue dedicated admin identities (or equivalent role elevation) separate from the mailbox / productivity account used for email and office work.
- Prefer JIT elevation with time-bound roles; do not grant standing privileged directory or cloud-owner roles for daily operations.
- Require phishing-resistant MFA on every privileged authentication and elevation.
- Reach privileged planes only on a protected path that meets [`administrative-interfaces.md`](./administrative-interfaces.md).
- Use a privileged access workstation (PAW) or equivalent tier-0 device for identity-provider and cloud control-plane administration.
- Monitor elevation events (grant, use, expiry) and alert on standing privilege that bypasses JIT.

## Designed break-glass (IdP and cloud)

Emergency access to the identity provider and cloud organization must be designed, dual-controlled, and tested — not a sticky-note password on a daily admin.

- Maintain two emergency accounts for the IdP and two for each cloud-organization root (or equivalent), stored offline or in a dual-control vault, unused for daily work.
- Dual control: no single person should be able to retrieve and use cloud/IdP break-glass without a second person or equivalent control.
- Alert on any use of break-glass identities.
- Test break-glass at least every 90 days and record the result.
- Local OS or device break-glass remains on [`administrative-interfaces.md`](./administrative-interfaces.md); do not collapse those accounts into IdP emergency identities.

## Verification and non-compliance

Security may review standing privileged directory roles, JIT logs, PAW enrollment for tier-0 admins, and break-glass test records.

Standing global-admin used as a daily driver, unused break-glass that cannot be retrieved, or break-glass used without an alert are control failures; suspected abuse follows [`incident-response.md`](./incident-response.md).

## Related standards

IAM policy: [`identity-and-access.md`](./identity-and-access.md). Credentials: [`passwords-and-credentials.md`](./passwords-and-credentials.md). Admin network/TLS/protocols: [`administrative-interfaces.md`](./administrative-interfaces.md). Endpoints used as PAWs: [`endpoint-and-workstation.md`](./endpoint-and-workstation.md). Cloud org root: [`cloud-essentials.md`](./cloud-essentials.md).

## Sources

- [NIST SP 800-63-4 Digital Identity Guidelines](https://csrc.nist.gov/pubs/sp/800/63/4/final)
- [CISA phishing-resistant MFA](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf)
- [Microsoft privileged access strategy](https://learn.microsoft.com/security/privileged-access-workstations/privileged-access-strategy)
- [CIS Controls — Access Control Management](https://www.cisecurity.org/controls)
