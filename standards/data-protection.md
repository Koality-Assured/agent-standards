---
doc_kind: requirement
canonical_id: data-protection
purpose: [requirement]
rank: high
topics: [data-protection, governance]
rag_keywords: [classification, retention, disposal, encryption-when, need-to-know]
---

# Data protection (generalized)

## Purpose

How information is classified, handled, retained, and destroyed, and when encryption is required. Algorithms, TLS versions, and key custody are in [`cryptography-and-key-management.md`](./cryptography-and-key-management.md).

## Scope

Organizational data in systems, endpoints, backups, SaaS tenants, and removable media. Backup copy mechanics and restore tests are in [`backup-and-recovery.md`](./backup-and-recovery.md); this page governs classification and handling of the primary data (and of backups that inherit it).

## Classification scheme

The organization must publish a documented classification scheme and a handling matrix that staff can apply without inventing labels.

Use these four labels unless legal maps a stricter regulated overlay onto Restricted:

| Label | Intent |
| --- | --- |
| Public | Approved for unlimited disclosure |
| Internal | Business-default; not for public posting |
| Confidential | Harmful if disclosed; limited audience |
| Restricted | Highest harm (secrets, regulated personal data, control-plane material) |

- Label Confidential and Restricted data in the system of record or equivalent handling process.
- Inventory systems and stores that hold Confidential or Restricted data, with a named owner.
- Access is need-to-know; default-deny sharing outside the owning group.

## Retention, disposal, and sharing

Retention must have both a minimum (legal/operational) and a maximum (do not keep sensitive data forever by default).

- Publish min and max retention per class or record type; dispose when the maximum is reached unless a legal hold applies.
- Disposal of media and systems that held Confidential or Restricted data must meet NIST SP 800-88-class sanitization. Deleting a file (`rm` or emptying a recycle bin) is not sanitization of the underlying media.
- Sharing Internal or higher outside the organization requires an approved channel and a contract or equivalent agreement.
- Do not place live Restricted or Confidential data unmasked in non-production.
- Backups inherit the classification of the source data and the handling rules that go with it.

## When to encrypt

Sensitive data must be encrypted in transit and at rest; this section states *when*, not *which* ciphers.

- Encrypt Confidential and Restricted data in transit and at rest. Cipher and key-custody rules are in [`cryptography-and-key-management.md`](./cryptography-and-key-management.md).
- Encrypt Internal data in transit on untrusted networks; encrypt Internal at rest when the system is portable, multi-tenant, or otherwise higher risk.
- Full-disk and removable-media encryption for endpoints that may store Internal or higher: [`endpoint-and-workstation.md`](./endpoint-and-workstation.md).

## Verification and non-compliance

Security may sample classification labels, sharing paths, non-production data, and disposal records for decommissioned media.

Unmasked Confidential data in non-prod, or media disposal that is only `rm`, is a control failure; suspected leakage follows [`incident-response.md`](./incident-response.md).

## Related standards

How to encrypt: [`cryptography-and-key-management.md`](./cryptography-and-key-management.md). Backup copies: [`backup-and-recovery.md`](./backup-and-recovery.md). SaaS handling: [`saas-security.md`](./saas-security.md). Endpoints: [`endpoint-and-workstation.md`](./endpoint-and-workstation.md). Vendor contracts: [`third-party-and-supply-chain.md`](./third-party-and-supply-chain.md).

## Sources

- [NIST SP 800-88 Rev. 1 Guidelines for Media Sanitization](https://csrc.nist.gov/pubs/sp/800/88/r1/final)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [ISO/IEC 27001](https://www.iso.org/standard/27001) (management-system rationale, not pasted controls)
