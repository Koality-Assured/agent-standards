---
doc_kind: requirement
canonical_id: confluence-interaction-and-administration
purpose: [requirement]
rank: high
topics: [confluence, documentation, admin, security, governance, standards]
rag_keywords: [confluence-admin, atlassian-guard, space-permissions, page-restrictions, scim, zdr, export-governance]
---

# Confluence interaction and administration standard

## Purpose

Define operational rules, security perimeters, space governance, and administrative standards for interacting with Atlassian Confluence Cloud workspaces (including `koality-assured` at `https://koality-assured.atlassian.net/`). Enforces Zero Data Retention (ZDR) boundaries, mandates role-based space access control (RBAC), prevents unauthorized mass page purging, protects confidential page hierarchies, and secures API token credentials.

## Scope

All autonomous agents, automated pipelines, scripts, and personnel interacting with Confluence REST API v2, Atlassian Forge apps, webhooks, and space administration. Complements [`saas-security.md`](./saas-security.md), [`identity-and-access.md`](./identity-and-access.md), [`data-protection.md`](./data-protection.md), and [`agent-session-security.md`](../agent-session-security.md).

## Workspace administration and space governance

1. **Identity & Single Sign-On (SSO):**
   - All production Confluence instances must enforce SAML 2.0 Single Sign-On via Atlassian Guard and a centralized Identity Provider (IdP) with mandatory phishing-resistant Multi-Factor Authentication (FIDO2 / WebAuthn).
   - SCIM (System for Cross-domain Identity Management) user provisioning must be enabled to automate account provisioning, group assignments, and immediate deprovisioning upon employee offboarding.
2. **Space RBAC and Least Privilege:**
   - Space permissions must be assigned strictly by IdP group memberships (e.g. `confluence-administrators`, `engineering-team`, `security-auditors`) rather than individual user accounts.
   - Anonymous public view and edit access MUST be disabled across all internal spaces.
   - Limit Space Admin rights to team leads or designated space curators.
3. **Page-Level View and Edit Restrictions:**
   - Confidential documents containing system architecture designs, credentials policy, financial data, or legal reviews must enforce page view/edit restrictions.
   - Parent page restrictions automatically inherit downwards; verify that sensitive child pages are not inadvertently exposed by loose parent permissions.
4. **App Installation & Marketplace Governance:**
   - App Approval Mode must be enabled. Non-admin users cannot install arbitrary Atlassian Marketplace apps or third-party Forge apps without formal security review.
   - All custom internal Forge apps must undergo static analysis and least-privilege OAuth scope audits before installation on `koality-assured`.
5. **Data Retention, Export & Audit Logging:**
   - Configure space export restrictions to prevent unauthorized mass bulk data exfiltration. Space exports must be logged and audited.
   - Ingest Confluence Cloud Audit Logs and Organization Audit API streams into the centralized SIEM per [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md).

## Publishing standards and content integrity

1. **Destructive Mutation Gate:**
   - Automated agents MUST NOT delete spaces or perform mass page purging without explicit human confirmation in the immediate turn.
2. **Structured Formatting Standard:**
   - Technical documentation and operational guides must use structured Atlassian Document Format (ADF) or Confluence Storage Format XHTML with appropriate macros (`info`, `warning`, `code`, `toc`).
   - Page titles must follow clear hierarchical naming conventions without colliding across the space.

## Secret management and token security

1. **Prohibition of Committed Credentials:**
   - Confluence API tokens, email credentials, OAuth client secrets, and webhook signing secrets MUST NEVER be hardcoded, logged, or committed to version control.
   - All credentials must be loaded strictly from `CONFLUENCE_API_TOKEN`, `CONFLUENCE_EMAIL`, and `CONFLUENCE_BASE_URL` environment variables or trusted secret managers.
2. **Token Rotation & Scoping:**
   - Regularly rotate personal API tokens and OAuth client secrets. Where available, use fine-grained OAuth 2.0 service account tokens rather than personal account tokens.

## Verification and compliance

- Audit space permissions: `python scripts/confluence/confluence_admin.py audit-space --workspace koality-assured --space-key ENG --json`.
- Inspect page restrictions: `python scripts/confluence/confluence_admin.py check-restrictions --workspace koality-assured --space-key ENG --json`.
- Fast markdown structure validation: `python scripts/docs/validate_structure_fast.py --path docs/standards/confluence-interaction-and-administration.md`.

## Related standards

- SaaS Security: [`saas-security.md`](./saas-security.md)
- Identity & Access Management: [`identity-and-access.md`](./identity-and-access.md)
- Data Protection: [`data-protection.md`](./data-protection.md)
- Confluence App Development: [`confluence-app-development-and-webhooks.md`](./confluence-app-development-and-webhooks.md)
- Agent Session Security: [`../agent-session-security.md`](../agent-session-security.md)

## Sources

- [Atlassian Confluence Cloud Documentation](https://support.atlassian.com/confluence-cloud/)
- [Atlassian Guard Security and Administration](https://support.atlassian.com/atlassian-access/)
- [CIS Benchmarks for SaaS Applications](https://www.cisecurity.org/benchmark)
- [NIST SP 800-63-4 Digital Identity Guidelines](https://csrc.nist.gov/pubs/sp/800/63/4/final)
