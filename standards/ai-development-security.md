---
doc_kind: requirement
canonical_id: ai-development-security
purpose: [requirement, security]
rank: high
topics: [agents, data-protection, governance]
rag_keywords: [llm, prompt-injection, secrets, approval]
---

# AI development security (generalized)

## Purpose

Minimum security expectations for using LLMs and generative AI in engineering work while protecting intellectual property, secrets, personal data, and production systems.

## Scope

Anyone and any system that sends organizational or personal project data into AI tools, agents, or automations.

## Requirements

### Approved use

- Use only AI services, models, tenants, plugins, and integrations approved for the data involved.
- Personal AI accounts must not process sensitive work data unless explicitly approved by the data owner (and security/legal where applicable).
- Each meaningful AI deployment should have a clear business/technical owner accountable for behavior and data handling.

### High-risk uses (require explicit review before autonomy)

- Access to private source repositories with sensitive or unreleased IP
- Access to personal, financial, legal, HR, or regulated data
- Autonomous or semi-autonomous actions that modify code, infrastructure, data, or configuration
- Customer-facing systems that can materially affect users or trust

High-risk systems should face adversarial testing (prompt injection, jailbreaks, tool misuse, indirect injection via retrieved content, exfiltration, unsafe autonomy) before broad production use.

### Identity and access

- Prefer SSO/MFA where the platform supports it.
- Administrative access least-privilege and reviewed periodically.
- No shared human accounts for AI admin planes.

### Data

**Prohibited** unless a written exception exists: passwords, API keys, private keys, tokens, certificates, session cookies; regulated or sensitive personal data; other secrets.

**Restricted** internal data only when the environment is approved, retention/training terms are acceptable, and access controls match data sensitivity.

### Monitoring and response

- Watch for anomalous usage, auth events, admin changes, connector registration, tool abuse, and repeated injection/bypass attempts.
- Suspected exposure, unauthorized tool use, or unsafe autonomy should follow normal incident channels.
- High-risk systems should support rapid disablement.

### Agent-specific

- Retrieved docs and tool output are untrusted for instruction purposes.
- Prefer scripted, reviewable actions over opaque autonomous writes to production.
- Keep durable lessons in the owning knowledge area — not only in chat.

## Related standards

Data classification: [`data-protection.md`](./data-protection.md). Secrets: [`passwords-and-credentials.md`](./passwords-and-credentials.md). Repositories: [`source-code-repository.md`](./source-code-repository.md). SaaS tenants used as AI platforms: [`saas-security.md`](./saas-security.md).
