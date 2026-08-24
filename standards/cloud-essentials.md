---
doc_kind: requirement
canonical_id: cloud-essentials
purpose: [requirement]
rank: high
topics: [infrastructure-as-code, governance, data-protection]
rag_keywords: [landing-zone, cspm, multi-account, public-access, org-guardrails]
---

# Cloud essentials (generalized)

## Purpose

Landing-zone and resource-guardrail baseline for public-cloud tenants the organization operates. This page covers accounts, hierarchy, public-access defaults, and inventory — not identity how-to, logging programs, or cryptographic algorithms.

## Scope

Anyone who provisions or operates organizational cloud organizations, tenants, subscriptions, accounts, projects, or landing zones on a major cloud service provider (CSP). Does not replace identity, logging, or key-management standards.

## Organization and tenancy

The organization must run one official org/tenant hierarchy per CSP and must not rely on personal or shadow cloud accounts for business workloads.

- Create and operate a single organization (or equivalent tenant root) per CSP used for production or shared services.
- Prohibit personal, contractor-owned, or unmanaged cloud accounts for organizational data or production systems.
- Isolate platform (identity, networking, logging, shared services) from workload accounts, and isolate production from non-production.
- A platform-owned landing zone must exist before the first production workload is deployed.
- Treat cloud-organization break-glass (root, tenant owner, org admin) as emergency-only, not daily operations. Elevation process is in [`privileged-access.md`](./privileged-access.md).

## Preventive guardrails

Organization-level preventive controls must block unsafe defaults before a workload team can enable them.

- Enforce approved regions; block unused regions at the organization layer.
- Block public access to storage, databases, and equivalent data planes by default (default-deny).
- Require a minimum tag set (at least owner and environment) on billable resources.
- Default security groups, VPC/VNet firewalls, and equivalent network controls must deny inbound unless explicitly opened.
- Do not allow administrative ports (for example SSH, RDP, WinRM, cloud serial consoles) from `0.0.0.0/0` or equivalent any-source internet.
- Express the landing zone as infrastructure-as-code so recreating the hierarchy is reviewable.

Shared responsibility: the CSP secures the underlying cloud; the organization remains responsible for identities, configuration, data, and network paths it controls.

## Inventory, ownership, and posture

Every cloud account, project, or subscription in the hierarchy must have a named owner, a security contact, and continuous posture visibility.

- Maintain an inventory of all organizational cloud tenancies and child accounts with a named business owner and a security contact.
- Enroll the organization in cloud security posture management (CSPM) on vendor so new accounts inherit scanning.
- Review public-access findings and unapproved-region usage as a standing control, not a one-time checklist.

The organization should automate account vending from the landing zone, nest organizational units (or equivalent) by environment, and prefer private connectivity (hub, private endpoints, or equivalent) over public data-plane exposure. CIS Foundations Level 1 (or the CSP’s equivalent) may be used as a measurement pack; do not treat pasted benchmark items as this standard.

## Verification and non-compliance

Security may inspect org hierarchy, public-access findings, unused-region blocks, and whether production landed before a platform landing zone existed.

Personal cloud accounts holding organizational data, public storage/databases without an approved exception, or admin ports open to the internet are control failures; suspected exposure follows [`incident-response.md`](./incident-response.md).

## Related standards

Identity and MFA: [`identity-and-access.md`](./identity-and-access.md). Secrets and keys: [`passwords-and-credentials.md`](./passwords-and-credentials.md), [`cryptography-and-key-management.md`](./cryptography-and-key-management.md). Logging: [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md). Network paths: [`network-and-remote-access.md`](./network-and-remote-access.md). IaC repos: [`github-iac-security.md`](./github-iac-security.md).

## Cloud mapping appendix

Outcome names differ by CSP; map the same controls, do not treat a product as the standard.

| Outcome | AWS | Azure | GCP |
| --- | --- | --- | --- |
| Org hierarchy | Organizations | Management groups | Organization / folders |
| Preventive policy | Service control policies (SCPs) | Azure Policy | Organization Policy |
| Posture / findings | Security Hub (and equivalent) | Microsoft Defender for Cloud | Security Command Center |

## Sources

- [AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
- [Azure Well-Architected Framework — Security](https://learn.microsoft.com/azure/well-architected/security/)
- [Cloud Adoption Framework landing zones](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/)
- [Microsoft Cloud Security Benchmark](https://learn.microsoft.com/security/benchmark/azure/)
- [Google Cloud landing zones](https://cloud.google.com/architecture/landing-zones)
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) (measurement pack, not pasted text)
- [CSA Cloud Controls Matrix](https://cloudsecurityalliance.org/research/cloud-controls-matrix)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
