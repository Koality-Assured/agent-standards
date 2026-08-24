---
doc_kind: requirement
canonical_id: incident-response
purpose: [requirement]
rank: high
topics: [security-operations, governance]
rag_keywords: [incident, severity, containment, after-action, notification]
---

# Incident response (generalized)

## Purpose

What happens after an incident is declared: ownership, communication, containment, notification, and closure. Detection and the declaration decision are in [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md).

## Scope

Security incidents affecting organizational systems, identities, data, or services, including those originating at a vendor or SaaS tenant. This page does not invent regulatory notification hour-counts; legal owns that matrix.

## Ownership and reporting

Incident response must have a primary owner, a backup, and a path every worker can use without knowing a private chat channel.

- Name a primary incident-response owner and a backup who can run the process if the primary is unavailable.
- Publish contacts (security, legal, communications, executive) and a workforce reporting path (for example a dedicated mailbox, form, or phone) that does not depend on the suspected-compromised system.
- Maintain an out-of-band communications path for when email or chat may be untrusted.
- Define severity levels so triage, paging, and executive notification are consistent.

## Response process

Declared incidents must be triaged, contained, eradicated, and recovered under a written process — not improvised solely in a ticket comment.

- Triage: confirm, classify severity, and identify affected systems and data classes ([`data-protection.md`](./data-protection.md)).
- Contain: stop ongoing access or spread (identity disable, network isolation, key revoke) before forensic curiosity delays the cut.
- Eradicate and recover: remove the cause, restore from known-good backups when needed ([`backup-and-recovery.md`](./backup-and-recovery.md)), and verify before returning to service.
- Legal owns the external notification matrix (regulators, customers, insurers). Do not hard-code hour counts in this standard.
- Record decisions and timeline as the incident proceeds.

## Exercises, after-action, and close

The process must be exercised and must have explicit close criteria so incidents do not linger as “still watching.”

- Run at least one incident-response exercise annually (tabletop is acceptable; include a technical exercise for high-impact scenarios when practical).
- Produce an after-action review with corrective actions and owners.
- Close only when containment is verified, evidence retention is satisfied, notifications required by legal are complete or waived, and monitoring for recurrence is in place.

## Verification and non-compliance

Security leadership may check that primary and backup owners are named, the workforce reporting path works, the last annual exercise is on record, and open incidents have close criteria.

An incident left only in chat, or notification sent without legal’s matrix, is a process failure.

## Related standards

Declaration: [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md). Restore: [`backup-and-recovery.md`](./backup-and-recovery.md). Vendor incidents: [`third-party-and-supply-chain.md`](./third-party-and-supply-chain.md). Evidence in logs: [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md).

## Sources

- [NIST SP 800-61 Rev. 3 Incident Response Recommendations](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [CISA Incident Response](https://www.cisa.gov/topics/cybersecurity-best-practices/incident-response)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) (Respond / Recover)
