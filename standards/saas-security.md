---
doc_kind: requirement
canonical_id: saas-security
purpose: [requirement]
rank: high
topics: [identity-and-access, data-protection, web-and-edge, governance]
rag_keywords: [saas-tenant, sso, scim, oauth-consent, sharing-links]
---

# SaaS security (consumption) (generalized)

## Purpose

Tenant configuration after the organization buys and uses a hosted SaaS product. Buy/assess/contract/exit controls are in [`third-party-and-supply-chain.md`](./third-party-and-supply-chain.md). This page does not apply “admin not on the public internet” to inherently hosted SaaS consoles.

## Scope

SaaS the business consumes (collaboration, HR, CRM, ITSM, and similar). SaaS the organization *builds and exposes* follows [`internet-facing-services.md`](./internet-facing-services.md). Git hosting rules for our source remain in [`source-code-repository.md`](./source-code-repository.md).

## Identity and administration

Each in-scope tenant must federate to the organizational IdP and must have named, least-privilege administrators.

- Require IdP SSO for workforce users where the product supports it; do not use a long-lived shared password as the primary login.
- Require MFA on administrator logins; phishing-resistant MFA is the floor for tenant administrators.
- Name tenant administrators explicitly; do not leave a large standing “everyone is admin” group.
- Provision and deprovision via SCIM (or equivalent automated lifecycle). Manual leftover accounts after HR termination are a control failure.
- Name a tenant owner accountable for configuration and data handling.

Do not require SaaS admin consoles to sit off the public internet when the vendor only offers a hosted console; protect them with SSO, MFA, and least privilege instead. Network isolation of *self-hosted* admin planes remains [`administrative-interfaces.md`](./administrative-interfaces.md).

## Sharing, OAuth, logs, and data

Default sharing and third-party app consent must not silently publish Internal or higher data.

- Disable public and “anyone with the link” sharing by default; enable only with a documented business need and classification check ([`data-protection.md`](./data-protection.md)).
- Allowlist OAuth / third-party app consent; do not permit arbitrary marketplace apps to read organizational mail or files by default.
- Export or forward audit logs to the organization’s logging destination where the product allows; retain per [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md).
- Handle tenant data per its classification (encryption-when, retention, no live Confidential/Restricted in unsanctioned tenants).
- Confirm an export or legal-hold path exists before the tenant holds Confidential or Restricted data; exit without export is a third-party failure ([`third-party-and-supply-chain.md`](./third-party-and-supply-chain.md)).

## Verification and non-compliance

Security may review SSO/MFA posture, sharing defaults, OAuth grants, admin lists, and whether SCIM deprovision matches HR leavers.

Public link-sharing left on by default, standing unused admin accounts, or OAuth apps with mailbox-wide consent outside the allowlist must be remediated; suspected data exposure follows [`incident-response.md`](./incident-response.md).

## Related standards

Vendor onboarding: [`third-party-and-supply-chain.md`](./third-party-and-supply-chain.md). IAM: [`identity-and-access.md`](./identity-and-access.md). Classification: [`data-protection.md`](./data-protection.md). Public apps we operate: [`internet-facing-services.md`](./internet-facing-services.md).

## Sources

- [CIS Controls — Secure Configuration of Enterprise Assets and Software](https://www.cisecurity.org/controls) (SaaS tenant hygiene as configuration)
- [NIST SP 800-63-4 Digital Identity Guidelines](https://csrc.nist.gov/pubs/sp/800/63/4/final)
- [CSA Cloud Controls Matrix](https://cloudsecurityalliance.org/research/cloud-controls-matrix)
