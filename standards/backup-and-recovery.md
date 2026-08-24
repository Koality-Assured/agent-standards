---
doc_kind: requirement
canonical_id: backup-and-recovery
purpose: [requirement]
rank: high
topics: [data-protection, security-operations]
rag_keywords: [rto, rpo, immutable-backup, restore-test, 3-2-1]
---

# Backup and recovery (generalized)

## Purpose

How copies are made, isolated, and proven restorable. Classification and retention of primary data are in [`data-protection.md`](./data-protection.md); backups inherit that classification.

## Scope

Data stores, system images, infrastructure-as-code that would be required to rebuild, and identity-configuration exports needed after a destructive incident. SaaS tenant export knobs are also in [`saas-security.md`](./saas-security.md).

## Recovery objectives and coverage

The organization must document what to restore and how fast, then back up everything in that inventory — not only databases.

- Publish recovery time objective (RTO) and recovery point objective (RPO) per critical system or service tier.
- Inventory in-scope data, machine images, IaC, and identity-configuration sources with owners.
- Automate backups. Weekly is the floor for in-scope systems; critical systems must run more often as RPO requires.
- Protect backup copies to the same classification as the source (access control, encryption in transit/rest per [`data-protection.md`](./data-protection.md) and [`cryptography-and-key-management.md`](./cryptography-and-key-management.md)).

## Isolation and integrity

Backup architecture must survive ransomware that reaches production admin identities.

- Keep at least one copy isolated: immutable, air-gapped, or offline (or a cloud equivalent that production admins cannot mass-delete).
- Follow 3-2-1 as the minimum copy pattern (three copies, two media types, one off-site) plus isolation plus tested restore — copies without a restore test are not a recovery capability.
- Verify backup integrity in an isolated environment; do not treat a successful job log as proof the data can be read.

## Restore testing

Restores must be rehearsed on a calendar, not only after a real outage.

- Test restores at least quarterly for critical systems, including a documented result (success, gaps, time taken versus RTO).
- Include identity and IaC rebuild paths in the exercise set when those would be required after a control-plane incident.
- Document who can delete or alter isolated copies; that ability is privileged ([`privileged-access.md`](./privileged-access.md)) and must not sit on the same standing identity that administers production data.

## Verification and non-compliance

Security may review job success, isolation configuration, restore-test records, and whether RTO/RPO are written for critical systems.

A critical system with no tested restore, or backups that production ransomware admins can mass-delete, is a control failure.

## Related standards

Primary data handling: [`data-protection.md`](./data-protection.md). Incidents that trigger restore: [`incident-response.md`](./incident-response.md). Cloud account isolation: [`cloud-essentials.md`](./cloud-essentials.md). Privileged ability to delete backups: [`privileged-access.md`](./privileged-access.md).

## Sources

- [CISA #StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide) (backup isolation themes)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) (Recover)
- [NIST SP 800-34 Rev. 1 Contingency Planning Guide](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final)
