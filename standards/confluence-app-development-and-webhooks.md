---
doc_kind: requirement
canonical_id: confluence-app-development-and-webhooks
purpose: [requirement]
rank: high
topics: [confluence, apps, forge, webhooks, security, oauth, adf]
rag_keywords: [forge-manifest, confluence-webhooks, hmac-signature, oauth-scopes, forge-remote, adf-security]
---

# Confluence app development and webhooks standard

## Purpose

Define security requirements, architecture patterns, cryptographic verification controls, and lifecycle practices for developing, configuring, and operating custom Atlassian Forge apps, Connect integrations, and Confluence Cloud webhooks.

## Scope

All custom Confluence applications, UI extensions, macros, webhook consumers, and API clients deployed within organizational workspaces (including `koality-assured`). Complements [`ai-development-security.md`](./ai-development-security.md), [`internet-facing-services.md`](./internet-facing-services.md), and [`cryptography-and-key-management.md`](./cryptography-and-key-management.md).

## App architecture and authorization

1. **Atlassian Forge as Default Architecture:**
   - All new custom applications extending Confluence Cloud must be developed using the Atlassian Forge platform. Forge enforces serverless compute isolation, managed authentication, and data privacy controls natively.
   - Declarative App Manifests (`manifest.yml`) must be version-controlled, linted, and reviewed before deployment.
2. **Principle of Least Privilege for OAuth Scopes:**
   - Apps must declare and request only the minimal granular OAuth 2.0 scopes necessary for functionality.
   - Avoid broad administrative scopes (`manage:confluence-configuration`, `admin:confluence`) unless strictly required. Prefer granular read/write scopes (`read:confluence-content.all`, `write:confluence-content`, `read:confluence-space.summary`).
3. **Data Residency and Egress Controls:**
   - Forge apps must declare external network domains in `permissions.external.fetch.backend` in `manifest.yml`.
   - Arbitrary outbound data egress to unvetted third-party endpoints is strictly prohibited.

## Webhook and event security (HMAC-SHA256 & JWT)

1. **Mandatory Signature and Origin Verification:**
   - Every public webhook endpoint receiving payloads from Confluence MUST verify the incoming signature against the configured signing secret.
   - Inbound HTTP webhooks must validate using constant-time string comparison (`hmac.compare_digest`) to prevent timing attack vulnerabilities.
2. **Replay Attack Mitigation:**
   - Endpoints MUST inspect request timestamp headers (`X-Atlassian-Request-Timestamp` or `timestamp` in body). Requests older than 300 seconds (5 minutes) from current server time MUST be rejected immediately.
3. **Idempotency via Webhook Identifiers:**
   - Webhook processing pipelines must record and deduplicate deliveries using the `X-Atlassian-Webhook-Identifier` header to prevent duplicate side effects caused by network retries.
4. **Execution Timeout & Asynchronous Offloading:**
   - Webhook receivers and Forge event handlers must acknowledge incoming events with HTTP 200 within **3 seconds**.
   - Long-running tasks, documentation index rebuilds, or LLM summarizations MUST be offloaded to asynchronous background queue workers.

## Rate limiting and retry resilience

1. **Backoff and Jitter:**
   - All Confluence REST API clients must inspect HTTP 429 status codes and parse `Retry-After` headers.
   - Implement exponential backoff with full jitter to avoid retry stampedes against Confluence Cloud.

## Verification and compliance

- Validate Forge App Manifest schema: `python scripts/confluence/confluence_app_manifest.py validate --file manifest.yaml --json`.
- Verify webhook signature verification logic: `python -m unittest scripts/tests/test_confluence_webhook.py`.
- Fast markdown structure validation: `python scripts/docs/validate_structure_fast.py --path docs/standards/confluence-app-development-and-webhooks.md`.

## Related standards

- Confluence Interaction & Administration: [`confluence-interaction-and-administration.md`](./confluence-interaction-and-administration.md)
- Internet-Facing Services: [`internet-facing-services.md`](./internet-facing-services.md)
- Cryptography & Key Management: [`cryptography-and-key-management.md`](./cryptography-and-key-management.md)
- AI Development Security: [`ai-development-security.md`](./ai-development-security.md)

## Sources

- [Atlassian Forge Documentation](https://developer.atlassian.com/platform/forge/)
- [Atlassian Confluence REST API v2](https://developer.atlassian.com/cloud/confluence/rest/v2/intro/)
- [RFC 6749: The OAuth 2.0 Authorization Framework](https://www.rfc-editor.org/rfc/rfc6749)
