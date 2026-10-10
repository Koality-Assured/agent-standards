---
doc_kind: requirement
canonical_id: logging-monitoring-and-detection
purpose: [requirement, security]
rank: high
topics: [security-operations]
rag_keywords: [siem, central-logging, detection, retention, telemetry-pipeline, process-monitoring, pipeline-integrity]
---

# Logging, monitoring, and detection (generalized)

## Purpose

Requirements governing security telemetry ingestion, normalization, log retention, detection alerting, and pipeline integrity monitoring. This standard establishes the baseline through incident declaration; response procedures following declaration are in [`incident-response.md`](./incident-response.md).

## Scope

All production and corporate systems, identity providers, cloud organizations, endpoints, network appliances, databases, and administrative interfaces. General application product metrics are out of scope unless they represent the sole record of security-relevant transactions.

## Telemetry pipeline maturity model

Security logging programs must advance through structured maturity stages:

1. **Collection Stage:** Capture core security events and machine data across identity, network, cloud, and host tiers into centralized storage.
2. **Normalization Stage:** Transform and parse heterogeneous log formats into a standardized security taxonomy (e.g., Open Cybersecurity Schema Framework [OCSF], Common Event Format [CEF], or Elastic Common Schema [ECS]) with unified timestamp formatting and asset attribution.
3. **Expansion Stage:** Expand ingestion to include high-fidelity telemetry: endpoint process trees, command-line arguments, DNS query logs, and network flow records.
4. **Enrichment Stage:** Augment event streams with contextual metadata, including threat intelligence feeds, asset criticality tiers, geographic IP data, and organizational identity roles.
5. **Automation & Orchestration Stage:** Implement automated security orchestration (SOAR) playbooks to execute standardized triage, correlation, and initial containment actions.
6. **Advanced Detection Stage:** Apply behavioral analytics, User and Entity Behavior Analytics (UEBA), and statistical anomaly detection to detect low-and-slow persistence and lateral movement.

## High-risk telemetry sources and events

Telemetry collection must prioritize high-fidelity audit trails across critical attack vectors:

- **Identity and Privileged Activity:** Authentication successes and failures, MFA challenges, privilege elevation, role assignment changes, API token creations, and service account usage.
- **Process and Execution Logging:** Detailed endpoint process creation events capturing full command-line strings, parent-child process relationships, process hashes, and acting user accounts.
- **Script and Command Interpreters:** Script-block logging for PowerShell, shell interpreters (bash, sh, zsh), Windows Command Prompt, and scripting engines (Python, Perl) to detect obfuscated commands and living-off-the-land binaries (LotL).
- **Persistence Mechanisms:** Scheduled task creation, service installations, cron modifications, startup folder alterations, and system configuration modifications.
- **Perimeter and Network Events:** Firewall deny events, proxy connection logs, Web Application Firewall blocks, VPN/ZTNA sessions, and DNS resolution failures/anomalies.
- **Data Plane and Storage:** Mass file modifications, volume snapshots, datastore exports, and access policy changes on databases and object stores.

## Centralization, time sync, and retention

Logs must be resilient against local tampering and readily queryable.

- Central SIEM aggregation: Security-relevant logs must be forwarded off-host to a centralized SIEM or immutable data lake in real time. Local-only log storage is prohibited for production, cloud, or privileged systems.
- Clock synchronization: Synchronize all system clocks using Network Time Protocol (NTP) from at least two independent, authenticated time sources (e.g., internal stratum-2 servers) to ensure forensic event correlation.
- Retention standards: Retain security event logs for a minimum of 90 days in hot, immediately queryable storage, and retain privileged, authentication, and compliance logs for a minimum of 12 months in cold, tamper-evident archive storage.
- Log immutability: Protect central log storage with write-once-read-many (WORM) policies or strict access control lists to prevent attackers from truncating or altering historical audit logs.

## Detection, alerting, and incident declaration

Continuous monitoring must produce actionable outcomes.

- Automated detection rules: Maintain scheduled and real-time detection rules mapped to the MITRE ATT&CK framework covering credential access, execution, lateral movement, and data exfiltration.
- Explicit declaration criteria: Maintain clear, written criteria for when alerts escalate into declared security incidents (e.g., confirmed privilege escalation, ransomware indicators, unauthorized root access, or lateral movement across network zones).
- Declaration workflow: Escalate confirmed incidents immediately through the formal incident response process in [`incident-response.md`](./incident-response.md).

## Telemetry pipeline integrity monitoring

Degradation of logging pipelines must be treated as an operational security incident.

- Pipeline health monitoring: Continuously monitor log ingestion volume and heartbeat signals from all reporting endpoints, cloud connectors, and network devices.
- Forwarding failure alerts: A cessation of log forwarding or an abrupt drop in telemetry volume (e.g., >50% drop over baseline) from any tier-0 asset, cloud organization root, domain controller, or internet-facing service must generate an immediate high-priority alert to the security operations team—not wait for scheduled audits.

## Verification and non-compliance

Security may audit log ingestion rates, test SIEM detection rules using simulated adversary telemetry, verify NTP synchronization, and validate forwarding failure alarms at any time.

Unmonitored production or tier-0 systems, disabled process command-line logging, missing NTP synchronization, or silent log forwarding failures constitute critical control failures; suspected evasion or tampering follows [`incident-response.md`](./incident-response.md).

## Related standards

Post-detection response: [`incident-response.md`](./incident-response.md). Privileged identity logging: [`privileged-access.md`](./privileged-access.md). Public perimeter telemetry: [`internet-facing-services.md`](./internet-facing-services.md). Cloud audit logs: [`cloud-essentials.md`](./cloud-essentials.md). WAF logging: [`web-application-firewall.md`](./web-application-firewall.md).

## Sources

- [NIST SP 800-92 Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final)
- [NIST Cybersecurity Framework (CSF 2.0) — Detect Function](https://www.nist.gov/cyberframework)
- [CIS Controls — Audit Log Management](https://www.cisecurity.org/controls)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
