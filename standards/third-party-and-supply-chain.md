---
doc_kind: requirement
canonical_id: third-party-and-supply-chain
purpose: [requirement]
rank: high
topics: [governance, code-and-repositories, data-protection]
rag_keywords: [vendor, soc2, sbom, contract, decommission]
---

# Third-party and supply chain (generalized)

## Purpose

How the organization buys, assesses, contracts, monitors, and exits vendors and software suppliers. Tenant knobs after purchase are [`saas-security.md`](./saas-security.md). Our own git hosting rules stay in [`source-code-repository.md`](./source-code-repository.md).

## Scope

SaaS vendors, hosted processors, professional-services firms with system access, and software suppliers whose code or components run in organizational environments. This page does not reprint SOC 2 Trust Services Criteria or ISO control text.

## Inventory, policy, and classification

Every vendor with access to organizational systems or Internal-or-higher data must be inventoried and classified.

- Maintain a vendor inventory (name, owner, data classes touched, systems integrated, last review date).
- Publish a written third-party security policy covering intake, review, monitoring, and exit.
- Classify vendors by impact (for example low / medium / high) so evidence and contract depth scale with risk.

## Contracts and evidence

Contracts must create security, breach-notice, disposal, and flow-down obligations; badges are not a substitute for reading scope.

- Require contractual terms for security obligations, breach notice, data disposal or return on exit, and flow-down to the vendor’s subprocessors where they touch organizational data.
- Request evidence commensurate with risk — typically a SOC 2 Type II report, an ISO 27001 certificate plus statement of applicability, or a Consensus Assessments Initiative Questionnaire (CAIQ). Read the scope, period, and exceptions; a logo or “we are certified” slide is not evidence.
- Least-privilege integrations: vendor connections (API, SCIM, support access) get only the roles required; standing global-admin for a vendor is privileged access ([`privileged-access.md`](./privileged-access.md)).

For software suppliers, the organization should request a software bill of materials (SBOM) and a vulnerability-disclosure path on a risk-tiered basis (required for high-impact components, asked for others).

## Monitor and decommission

Vendors must not outlive their access; identities and tokens are part of exit.

- Monitor high-impact vendors (renewed evidence, material incident news, significant product or ownership change).
- On exit: disable identities, revoke tokens and API keys, remove OAuth grants, confirm data disposal or return, and withdraw any remaining attestations or trust of that vendor’s connections.

Internet-facing purchased applications still need the go-live path in [`internet-facing-services.md`](./internet-facing-services.md).

## Verification and non-compliance

Security may sample the inventory against SSO and finance records, read evidence scope (not cover pages), and confirm exit revoked tokens.

High-impact vendors with no contract security terms, or former vendors whose API keys still work, are control failures; suspected vendor breach follows [`incident-response.md`](./incident-response.md).

## Related standards

SaaS tenant config: [`saas-security.md`](./saas-security.md). Classification in contracts: [`data-protection.md`](./data-protection.md). Public exposure of purchased apps: [`internet-facing-services.md`](./internet-facing-services.md). Our repositories: [`source-code-repository.md`](./source-code-repository.md).

## Sources

- [AICPA SOC 2](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2) (request reports; do not copy TSC into this standard)
- [ISO/IEC 27001](https://www.iso.org/standard/27001)
- [CSA CAIQ / CCM](https://cloudsecurityalliance.org/research/cloud-controls-matrix)
- [CISA Secure Software Development Attestation](https://www.cisa.gov/resources-tools/resources/secure-software-development-attestation-form) (software supplier assurance themes)
- [NTIA / CISA SBOM](https://www.cisa.gov/sbom)
