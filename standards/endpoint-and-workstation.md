---
doc_kind: requirement
canonical_id: endpoint-and-workstation
purpose: [requirement, security]
rank: high
topics: [identity-and-access, data-protection, security-operations]
rag_keywords: [disk-encryption, screen-lock, edr, mdm, byod, paw, clean-source, tiering]
---

# Endpoint and workstation (generalized)

## Purpose

Baseline security controls for laptops, desktops, workstations, and mobile devices accessing organizational systems, repositories, or data. Idle-lock, disk encryption, EDR baselines, and developer workstation hygiene are established here.

## Scope

All organization-owned endpoints, managed mobile devices, contractor hardware, and any approved Bring Your Own Device (BYOD) systems accessing organizational resources. Dedicated Privileged Access Workstations (PAWs) must also satisfy [`privileged-access.md`](./privileged-access.md). Server configuration baselines are in [`secure-configuration.md`](./secure-configuration.md).

## Device encryption, locking, and hardware trust

Physical endpoints must maintain cryptographic hardware trust and storage protection.

- Full-disk encryption: Enable full-disk encryption (e.g., BitLocker, FileVault) with organizational recovery key escrow managed via MDM. Escrow ensures lost or stolen devices do not result in unencrypted data compromise and that device data remains recoverable upon personnel departure.
- Hardware security module: Endpoints must utilize a Trusted Platform Module (TPM 2.0) or Secure Enclave to protect cryptographic keys, authenticate device identity, and support measured boot integrity.
- Screen idle lock: Enforce automatic screen lock with password/biometric challenge after at most fifteen (15) minutes of inactivity on workstations and at most two (2) minutes on mobile devices.
- Local administrator privileges: Daily productivity and engineering work must execute without standing local administrator or root privileges. Elevation must occur via audited JIT privilege management or helpdesk authorization.

## Endpoint detection and response (EDR)

All managed endpoints must run a centrally controlled, behavioral-based EDR agent.

- Real-time protection and behavioral detection: EDR agents must perform continuous on-access scanning, memory inspection, and behavioral monitoring to detect and block malware, ransomware, living-off-the-land binaries, and unauthorized script execution.
- Anti-tampering protection: Enable agent tamper-protection features to prevent local users or unauthorized processes from disabling, stopping, or uninstalling security software.
- Automated containment: The EDR solution must support remote endpoint network isolation/quarantine to sever network connectivity instantly during active security investigations while maintaining management telemetry.
- Telemetry forwarding: EDR alerts, process execution trees, and system behavioral events must stream directly to the centralized SIEM per [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md).

## Unified Endpoint Management (UEM) and compliance

Devices accessing organizational networks must be managed throughout their lifecycle.

- Mandatory enrollment: Enroll all organization-owned endpoints into an approved Unified Endpoint Management (UEM/MDM) solution prior to provisioning to staff.
- Compliance policies: Devices must satisfy continuous compliance policies (active disk encryption, firewall enabled, EDR running, OS within supported patch window). Non-compliant devices must be blocked from corporate systems via conditional access gateways.
- Operating system and third-party patching: Enforce automated OS update baselines and third-party application patching per [`vulnerability-and-patch-management.md`](./vulnerability-and-patch-management.md).
- Lost or stolen device response: Report lost or stolen devices immediately; security operations must initiate cryptographic wipe or remote device sanitization via MDM.

## Clean source principle and enterprise access tiering

Administrative and high-impact actions must observe access tiering boundaries.

- Enterprise access tiers: Systems and user sessions must adhere to tiered isolation:
  - **Tier 0 (Control Plane):** Identity providers, cloud root organizations, PKI roots, and security monitoring infrastructure.
  - **Tier 1 (Enterprise Infrastructure):** Enterprise applications, database clusters, servers, and cloud workload subscriptions.
  - **Tier 2 (Workstations & Endpoints):** User laptops, mobile devices, and standard office applications.
- Clean Source Principle: An asset's security dependencies can never be of a lower tier than the asset itself. Performing Tier 0 or Tier 1 administration from a standard Tier 2 daily-driver workstation is strictly prohibited.
- Privileged Access Workstations (PAWs): Tier 0 control plane administrators must operate from dedicated, hardened PAWs that prohibit general internet browsing, external email access, and unvetted third-party software per [`privileged-access.md`](./privileged-access.md).

## Bring Your Own Device (BYOD) controls

Personally owned devices accessing organizational data must enforce strict containerization.

- Explicit posture enforcement: Unmanaged personal devices must not access Internal, Confidential, or Restricted systems directly.
- Work profile containerization: Approved mobile BYOD access must be containerized through a managed work profile or application-level mobile application management (MAM) with remote wipe limited to corporate data.
- Developers and engineers cloning source repositories or accessing production environments must use dedicated, organization-managed endpoints; personal unmanaged laptops are prohibited from holding production credentials or source code clones.

## Verification and non-compliance

Security may audit endpoint compliance posture, sample BitLocker/FileVault escrow records, verify EDR agent coverage across asset inventories, and audit local administrator group membership at any time.

Unencrypted endpoints, unmanaged devices accessing sensitive corporate repositories, disabled EDR agents, or Tier 0 administrative tasks conducted from general user laptops constitute critical control failures; suspected lost or compromised endpoints follow [`incident-response.md`](./incident-response.md).

## Related standards

Privileged workstations: [`privileged-access.md`](./privileged-access.md). Data classification: [`data-protection.md`](./data-protection.md). Patching floors: [`vulnerability-and-patch-management.md`](./vulnerability-and-patch-management.md). Remote network access: [`network-and-remote-access.md`](./network-and-remote-access.md). Configuration baselines: [`secure-configuration.md`](./secure-configuration.md). Source code repos: [`source-code-repository.md`](./source-code-repository.md).

## Sources

- [CIS Controls — Safeguards for Endpoint Security](https://www.cisecurity.org/controls)
- [NIST SP 800-124 Rev. 2 Guidelines for Managing the Security of Mobile Devices](https://csrc.nist.gov/pubs/sp/800/124/r2/final)
- [Microsoft Privileged Access Strategy: Clean Source Principle](https://learn.microsoft.com/security/privileged-access-workstations/privileged-access-strategy)
- [CISA Mobile Device Security Guidelines](https://www.cisa.gov/mobile-device-security)
