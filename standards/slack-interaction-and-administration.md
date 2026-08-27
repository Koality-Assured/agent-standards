---
doc_kind: requirement
canonical_id: slack-interaction-and-administration
purpose: [requirement]
rank: high
topics: [slack, communication, admin, security, governance, standards]
rag_keywords: [slack-admin, enterprise-grid, dlp, retention, sso, scim, zdr, broadcast-gate]
---

# Slack interaction and administration standard

## Purpose

Define operational rules, security perimeters, messaging governance, and administrative standards for interacting with Slack workspaces (including `koality-assured` and Enterprise Grid organizations). Protects confidential organizational conversations, enforces Zero Data Retention (ZDR) boundaries, mandates role-based access control (RBAC), prevents unauthorized mass broadcasts, and secures token credentials.

## Scope

All autonomous agents, automated workflows, scripts, and personnel interacting with Slack APIs, incoming webhooks, slash commands, bot installations, and workspace administration. Complements [`saas-security.md`](./saas-security.md), [`identity-and-access.md`](./identity-and-access.md), and [`data-protection.md`](./data-protection.md).

## Workspace administration and governance

1. **Identity & Single Sign-On (SSO):**
   - All production Slack workspaces must enforce SAML 2.0 Single Sign-On via a centralized Identity Provider (IdP) with mandatory phishing-resistant Multi-Factor Authentication (FIDO2 / hardware keys).
   - SCIM (System for Cross-domain Identity Management) provisioning must be enabled to automate user onboarding, role assignments, and immediate deprovisioning upon employee offboarding.
2. **Role Separation and Least Privilege:**
   - Separate Primary Owner and Workspace Admin roles from daily engineering accounts.
   - Limit the assignment of Workspace Owner and Admin permissions to the minimum necessary personnel.
3. **App Installation Allowlisting & Approval:**
   - App Approval Mode must be enabled on all workspaces. Non-admin users cannot install arbitrary Slack Marketplace applications without formal security review and administrator sign-off.
   - Restrict OAuth scopes requested by third-party integrations to the minimum required functionality.
4. **Data Retention and Compliance:**
   - Define message and file retention policies per organizational compliance requirements (e.g. 90-day or 1-year retention with automated purging of transient channels).
   - Ingest Slack Audit Logs API streams into the centralized SIEM pipeline per [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md).

## Messaging etiquette and broadcast gates

1. **Broadcast Mentions Gate:**
   - Automated bots and agents MUST NOT issue broadcast mentions (`@channel`, `@everyone`, `@here`) without explicit human confirmation in the immediate turn.
   - Broadcast notifications cause severe cognitive load and distraction across organizational teams.
2. **Block Kit UI Standard:**
   - Production alerts, deployment notices, and interactive messages must use Block Kit for structured layout, clear visual hierarchy, and scannable context.
   - Always supply fallback plain text (`text` field) for accessibility readers and notification previews.
3. **Channel Organization:**
   - Direct automated status alerts to dedicated broadcast/alert channels (e.g., `#alerts-ci`, `#alerts-security`) rather than general discussion channels.
   - Private channel creation must be justified and tracked to prevent channel sprawl.

## Secret management and token security

1. **Prohibition of Committed Credentials:**
   - Slack bot tokens (`xoxb-`), user tokens (`xoxp-`), app-level tokens (`xapp-`), signing secrets, and incoming webhook URLs MUST NEVER be hardcoded, logged, or committed to version control.
   - All tokens must be loaded strictly from environment variables or trusted secret vaults.
2. **Incoming Webhook URL Protection:**
   - Webhook URLs are bearer credentials. Anyone with access to the URL can post to the target channel. Treat webhook URLs with the same sensitivity as API tokens.
3. **Token Rotation:**
   - Regularly rotate Slack App tokens and OAuth client secrets. Enable token rotation with refresh tokens for OAuth apps where applicable.

## Verification and compliance

- Audit workspace security posture: `python scripts/slack/slack_admin.py audit-workspace --workspace koality-assured --json`.
- Validate message formatting and dry-run dispatch: `python scripts/slack/slack_ops.py post-message --workspace koality-assured --dry-run`.
- Fast markdown structure validation: `python scripts/docs/validate_structure_fast.py --path docs/standards/slack-interaction-and-administration.md`.

## Related standards

- SaaS Security: [`saas-security.md`](./saas-security.md)
- Identity & Access Management: [`identity-and-access.md`](./identity-and-access.md)
- Privileged Access: [`privileged-access.md`](./privileged-access.md)
- Logging & Monitoring: [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md)
- Agent Session Security: [`../agent-session-security.md`](../agent-session-security.md)

## Sources

- [Slack Security Whitepaper](https://slack.com/security)
- [CIS Slack Benchmark v1.0.0](https://www.cisecurity.org/benchmark/slack)
- [NIST SP 800-63-4 Digital Identity Guidelines](https://csrc.nist.gov/pubs/sp/800/63/4/final)
