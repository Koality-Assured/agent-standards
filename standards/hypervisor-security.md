---
doc_kind: requirement
canonical_id: hypervisor-security
purpose: [requirement, security]
rank: high
topics: [infrastructure-as-code, on-premises, secure-configuration]
rag_keywords: [hypervisor, virtualization, esxi, kvm, tpm, secure-boot, lockdown-mode, host-hardening]
---

# Hypervisor and virtualization security (generalized)

## Purpose

Security baseline requirements for bare-metal (Type 1) and hosted (Type 2) virtualization hypervisors, host operating systems, and guest virtual machine boundaries deployed in enterprise datacenters, co-location facilities, and private cloud infrastructure.

## Scope

All physical virtualization hosts, hypervisor operating systems (e.g., VMware ESXi, KVM, Proxmox VE, Microsoft Hyper-V), virtualization management appliances (e.g., vCenter), and the virtual machines and networks hosted on them. Cloud provider hypervisor infrastructure (where the provider manages the virtualization layer) is governed under [`cloud-essentials.md`](./cloud-essentials.md).

## Hardware root-of-trust and firmware configuration

Hypervisor hardware must establish cryptographic trust prior to operating system execution.

- Hardware Security Modules: A physical Trusted Platform Module (TPM 2.0) must be enabled and activated on all host server hardware to establish pre-boot measurements and a hardware root of trust.
- Secure Boot: Enforce UEFI Secure Boot across all hypervisor physical hosts to prevent execution of unauthorized bootloaders or malicious kernels.
- Cryptographic Acceleration: Enable CPU AES-NI (or equivalent hardware cryptographic extensions) to maximize performance of full-disk and in-flight encryption.
- Out-of-Band (OOB) Management: Change default administrative passwords on all baseboard management controllers (e.g., IPMI, iDRAC, iLO). Isolate OOB management interfaces onto a dedicated, non-routable management network with access restricted to authorized administrators via MFA.

## Hypervisor host hardening

The hypervisor management plane must maintain minimal attack surface and strict operational controls.

- Shell and remote access restrictions: Disable interactive host shells (e.g., ESXi Shell, direct SSH) during normal operations. Enable shell access only for break-glass troubleshooting, and enforce automated session timeouts (maximum 15 minutes idle).
- Enforce lockdown mode: Enable strict hypervisor lockdown mode where available, ensuring host configuration occurs exclusively through centralized management planes (e.g., vCenter, centralized orchestrators).
- Minimal software footprint: Prohibit the installation of third-party, non-essential binaries, drivers, or software packages on hypervisor host operating systems. Only vendor-certified, digitally signed drivers (VIBs/packages) may be loaded.
- Administrative authentication: Centralize hypervisor administrative access through the organizational Identity Provider (IdP) supporting least-privilege RBAC. Host-local `root` or administrator accounts must be reserved strictly for break-glass emergency recovery with unique, vaulted credentials.

## Network isolation and management boundaries

Hypervisor management networks must be physically or cryptographically separated from guest virtual machine traffic.

- Segment management and workload traffic: Management interfaces, storage networks (iSCSI, NFS), and VM migration networks (vMotion) must not share logical or physical adapters with tenant or guest virtual machine networks.
- Dedicated management VLANs: Place hypervisor management interfaces in an isolated, secure routing zone reachable only through an approved administrative jump host or ZTNA gateway per [`administrative-interfaces.md`](./administrative-interfaces.md).
- Transport encryption: Encrypt all hypervisor management traffic, remote consoles, API interactions, and live VM migrations using TLS 1.2 or higher.

## Guest virtual machine security

Virtual machines must be protected against inter-tenant escape and data exposure.

- Virtual TPM and Secure Boot: Enable virtual TPM (vTPM) and UEFI Secure Boot for guest operating systems that support them.
- Storage encryption: Enable full storage encryption at the datastore, storage array, or virtual machine level for any guest hosting Confidential or Restricted data.
- Resource isolation and limits: Configure memory and CPU reservations/limits on virtual machines to prevent denial-of-service or noisy-neighbor conditions on shared hypervisor compute.
- Hypervisor updates and patch floors: Keep hypervisors, firmware, and management controllers up-to-date and within published vendor support periods, prioritizing patches that remediate speculative execution or hypervisor breakout vulnerabilities.

## Observability and event logging

Host-level activity and management operations must produce auditable telemetry.

- Forward hypervisor system logs, authentication events, console access, configuration changes, and VM lifecycle events directly to the centralized SIEM.
- Retain local logs for a minimum of 90 days, or ensure immediate forwarding to immutable central storage per [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md).
- Alert on unusual host behavior: Configure automated alerts on failed host logins, enabling of interactive shells, exiting of lockdown mode, or unexpected modification of network virtual switches.

## Verification and non-compliance

Security engineering may audit hypervisor configurations, scan firmware versions, inspect management network access lists, and verify lockdown status at any time.

Hypervisor management planes exposed to guest networks or public subnets, default BMC/IPMI passwords, active host shells without an approved change window, or unencrypted datastores are control failures; suspected hypervisor escapes or compromised hosts follow [`incident-response.md`](./incident-response.md).

## Related standards

Admin planes: [`administrative-interfaces.md`](./administrative-interfaces.md). Server baselines: [`secure-configuration.md`](./secure-configuration.md). Network zones: [`network-and-remote-access.md`](./network-and-remote-access.md). Incident response: [`incident-response.md`](./incident-response.md). Central logging: [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md).

## Sources

- [CIS VMware ESXi Benchmark](https://www.cisecurity.org/benchmark/vmware)
- [NIST SP 800-125B Secure Virtual Network Configuration for Virtual Machine (VM) Applications](https://csrc.nist.gov/pubs/sp/800/125/b/final)
- [NIST SP 800-125A Rev. 1 Security Recommendations for Server-based Hypervisor Platforms](https://csrc.nist.gov/pubs/sp/800/125/a/r1/final)
