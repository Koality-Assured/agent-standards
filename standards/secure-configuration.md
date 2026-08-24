---
doc_kind: requirement
canonical_id: secure-configuration
purpose: [requirement]
rank: high
topics: [infrastructure-as-code, security-operations, governance]
rag_keywords: [baseline, cis-level-1, gold-image, drift, exception]
---

# Secure configuration (generalized)

## Purpose

How baselines are chosen, applied, excepted, and kept from drifting. This page cites CIS Level 1 and vendor hardening guides as *sources*, not as pasted benchmark items.

## Scope

Servers, cloud images, containers, network devices, and standard end-user builds the organization operates. Cloud org-level public-access guardrails are in [`cloud-essentials.md`](./cloud-essentials.md). Endpoint-specific encryption and MDM are in [`endpoint-and-workstation.md`](./endpoint-and-workstation.md).

## Baseline source and apply

Each asset class must have an approved baseline with a cited source, then a gold image or desired-state definition that implements it.

- Maintain a written configuration-management process (owners, apply path, exception path, drift response).
- Approve a baseline per asset class. Cite CIS Benchmarks Level 1, vendor security guides, or an equivalent published profile as the source. Do not paste CIS item text into this standard or into tickets as a substitute for the organization’s baseline document.
- Deploy via gold image, desired-state configuration (for example policy-as-code), or both. Unmanaged “click-built” production images are not a baseline.
- Disable default vendor accounts and default passwords after commissioning ([`identity-and-access.md`](./identity-and-access.md), [`passwords-and-credentials.md`](./passwords-and-credentials.md)).
- Disable unnecessary services and features for the asset’s role.
- Use secure management channels; protocol details for admin planes are in [`administrative-interfaces.md`](./administrative-interfaces.md).

## Change, exceptions, and drift

Hardening must survive change control and must not be undone by the application stack.

- Configuration changes to in-scope production assets follow change control (review, approval, record).
- Exceptions to the baseline require an owner, a risk rationale, and an expiry; they are reviewed, not infinite.
- Monitor for drift from the approved baseline (desired-state tooling, CSPM, or equivalent) and remediate or re-except.
- Applications and installers must not weaken platform hardening (for example re-enabling SMBv1, opening admin ports, or turning off disk encryption) without an approved exception.

## Verification and non-compliance

Security may compare running configuration to the approved baseline via desired-state tooling, CSPM, authenticated scans, or sampling.

Unmanaged production images, expired exceptions, and drift that re-opens administrative ports or public data planes must be remediated; suspected exposure follows [`incident-response.md`](./incident-response.md).

## Related standards

Cloud org guardrails: [`cloud-essentials.md`](./cloud-essentials.md). Patching: [`vulnerability-and-patch-management.md`](./vulnerability-and-patch-management.md). Endpoints: [`endpoint-and-workstation.md`](./endpoint-and-workstation.md). IaC review: [`github-iac-security.md`](./github-iac-security.md). Public hardening: [`internet-facing-services.md`](./internet-facing-services.md).

## Sources

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) (Level 1 as source, not pasted)
- [CIS Controls — Secure Configuration](https://www.cisecurity.org/controls)
- [NIST SP 800-128 Guide for Security-Focused Configuration Management](https://csrc.nist.gov/pubs/sp/800/128/final)
