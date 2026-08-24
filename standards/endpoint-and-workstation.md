---
doc_kind: requirement
canonical_id: endpoint-and-workstation
purpose: [requirement]
rank: high
topics: [identity-and-access, data-protection, security-operations]
rag_keywords: [disk-encryption, screen-lock, edr, mdm, byod]
---

# Endpoint and workstation (generalized)

## Purpose

Security baseline for laptops, desktops, and mobile devices that access organizational systems or data. Idle-lock and disk encryption for developers with repo credentials live here; repository rules point at this page.

## Scope

Organization-managed endpoints and any BYOD that is allowed to access Internal or higher data. Privileged access workstations (PAW) also meet [`privileged-access.md`](./privileged-access.md). Server hardening is [`secure-configuration.md`](./secure-configuration.md).

## Device protection

Every in-scope endpoint must encrypt storage, lock when idle, and run managed malware defense.

- Enable full-disk encryption with organizational key escrow (or equivalent recovery) so a lost device is not a standing data incident and so a forgotten password is recoverable by IT.
- Screen lock: at most 15 minutes idle on workstations; at most 2 minutes on mobile devices.
- Deploy malware defense with automatic signature/engine updates and central management.
- Patch OS and standard applications automatically ([`vulnerability-and-patch-management.md`](./vulnerability-and-patch-management.md)).
- Daily work must not use a standing local administrator account; elevation is JIT or helpdesk-mediated.
- Browse with a managed browser (or equivalent managed profile) for organizational work.

The organization should deploy endpoint detection and response (EDR) by default. Privileged users and developers who hold production credentials must have EDR (or equivalent) — treat that as a must-equivalent even if EDR is still rolling out to the general workforce.

## Management and BYOD

Endpoints that touch organizational data must be manageable; BYOD is an explicit decision, not an accident.

- Enroll organization-owned devices in MDM (or equivalent unified endpoint management).
- BYOD: either enforce managed posture (MDM/container, encryption, lock, patch floor) or block access to Internal-or-higher systems. “Personal laptop with a password” is not a posture.
- Developers and others who clone sensitive repositories must meet this standard; repo policy must not re-specify idle-lock here in duplicate ([`source-code-repository.md`](./source-code-repository.md)).
- Lost, stolen, or unreturned devices must trigger credential revoke and, where escrow exists, cryptographic recovery or wipe through MDM.

## Verification and non-compliance

Security may verify encryption state, lock policy, patch level, EDR/MDM enrollment, and local-admin membership at any time via the management plane or spot checks.

Suspected missing encryption, unmanaged BYOD with Internal-or-higher access, or standing local admin on a daily-driver must follow [`incident-response.md`](./incident-response.md) when data exposure is possible.

## Related standards

Privileged workstations: [`privileged-access.md`](./privileged-access.md). Classification on the device: [`data-protection.md`](./data-protection.md). Patching: [`vulnerability-and-patch-management.md`](./vulnerability-and-patch-management.md). Remote access: [`network-and-remote-access.md`](./network-and-remote-access.md). Baselines: [`secure-configuration.md`](./secure-configuration.md).

## Sources

- [CIS Controls — End-of-Life Assets / Malware Defenses / Data Protection](https://www.cisecurity.org/controls)
- [NIST SP 800-124 Rev. 2 Guidelines for Managing the Security of Mobile Devices](https://csrc.nist.gov/pubs/sp/800/124/r2/final)
- [CISA Mobile Device Security](https://www.cisa.gov/mobile-device-security)
