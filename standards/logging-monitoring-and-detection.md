---
doc_kind: requirement
canonical_id: logging-monitoring-and-detection
purpose: [requirement]
rank: high
topics: [security-operations]
rag_keywords: [siem, central-logging, detection, retention, time-sync]
---

# Logging, monitoring, and detection (generalized)

## Purpose

What must be logged, how long it stays searchable, and when an event becomes an incident. This page ends at detection and declaration; response after declaration is [`incident-response.md`](./incident-response.md).

## Scope

Security-relevant telemetry from identity, endpoints, cloud control planes, internet-facing services, and administrative interfaces. Application product analytics are out of scope unless they are the only source of security events.

## Logging program

The organization must have a written logging and detection process with owners, sources, and a declaration path.

- Enable logging on in-scope systems and centralize it (SIEM or equivalent). Local-only logs are not sufficient for privileged and internet-facing systems.
- Retain security logs at least 90 days in hot / immediately queryable storage.
- Synchronize time from at least two reliable time sources so event order is reconstructable.
- Identity and privileged activity (authentication success/failure, elevation, admin configuration changes) must be logged with the acting identity.
- Review detections at least weekly, or continuously via automated alerting.
- Protect logs from tampering (restricted write path, integrity controls, or equivalent) and alert if logging or forwarding fails.

The organization should retain privileged and authentication logs for 12 months total, with at least 3 months immediately available.

## Detection and declaration

Monitoring must produce a decision: ignore, ticket, or declare an incident.

- Maintain criteria for when a detection becomes an incident (for example confirmed unauthorized access, ransomware indicators, mass data export, or failed logging on a tier-0 system).
- Declare through the incident-response process in [`incident-response.md`](./incident-response.md); do not leave confirmed incidents only in a chat thread.
- Cover at least: identity provider and privileged elevation, internet-facing services, cloud organization changes, endpoint malware/EDR alerts, and backup-integrity failures.
- Failed or paused log forwarding on a privileged, internet-facing, or backup system is itself a detection that must page an owner — not a silent gap until the next weekly review.

## Verification and non-compliance

Security may sample whether required sources are present, timestamps agree, and alerts fire when forwarding is stopped.

Missing coverage on a tier-0 or internet-facing system is a control failure and may be declared under [`incident-response.md`](./incident-response.md).

## Related standards

What happens after declaration: [`incident-response.md`](./incident-response.md). Privileged elevation events: [`privileged-access.md`](./privileged-access.md). Public services: [`internet-facing-services.md`](./internet-facing-services.md). Cloud inventory: [`cloud-essentials.md`](./cloud-essentials.md).

## Sources

- [NIST SP 800-92 Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) (Detect function)
- [CIS Controls — Audit Log Management](https://www.cisecurity.org/controls)
