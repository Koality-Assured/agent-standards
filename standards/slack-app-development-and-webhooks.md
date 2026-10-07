---
doc_kind: requirement
canonical_id: slack-app-development-and-webhooks
purpose: [requirement]
rank: high
topics: [slack, apps, webhooks, security, oauth, block-kit, hmac]
rag_keywords: [slack-apps, incoming-webhooks, hmac-signature, oauth-scopes, manifest, events-api]
---

# Slack app development and webhooks standard

## Purpose

Define security requirements, architecture patterns, cryptographic verification controls, and lifecycle practices for developing, configuring, and operating custom Slack applications, Incoming Webhooks, Slash Commands, and Events API integrations.

## Scope

All custom Slack apps, bots, webhook integrations, and API clients deployed within organizational workspaces. Complements [`ai-development-security.md`](./ai-development-security.md), [`internet-facing-services.md`](./internet-facing-services.md), and [`cryptography-and-key-management.md`](./cryptography-and-key-management.md).

## App architecture and authorization

1. **Declarative App Manifests:**
   - All custom Slack applications must be managed and provisioned using declarative App Manifests (`manifest.yaml` or `manifest.json`).
   - App Manifests must be stored under version control, enabling peer review, automated linting, and reproducible environment deployments.
2. **Principle of Least Privilege for OAuth Scopes:**
   - Apps must request only the minimum granular bot and user scopes required for operation.
   - Avoid legacy scopes (`bot`, `read`, `client`). Use modern granular scopes (e.g. `chat:write` instead of broad workspace read permissions).
   - Public channel write permissions (`chat:write.public`) should only be granted when channel membership is not feasible or desirable.
3. **Transport Security & Socket Mode:**
   - All HTTP callback endpoints (Events API, Interactivity, Slash Commands) must use TLS 1.3 (or TLS 1.2 minimum) with valid CA-signed certificates.
   - For internal tools, daemons, or development environments operating behind firewalls, use **Socket Mode** with an app-level token (`xapp-...`) rather than opening inbound public firewall ports.

## Webhook and event security (HMAC-SHA256)

1. **Mandatory Signature Verification:**
   - Every public webhook endpoint receiving payloads from Slack MUST verify the `X-Slack-Signature` header against the application's `SLACK_SIGNING_SECRET`.
   - Verification must compute `v0=HMAC_SHA256(secret, "v0:" + timestamp + ":" + raw_body)` and validate using constant-time string comparison (`hmac.compare_digest`).
2. **Replay Attack Mitigation:**
   - Endpoints MUST verify the `X-Slack-Request-Timestamp` header. Requests with timestamps older than 300 seconds (5 minutes) from the server's current time MUST be rejected immediately.
3. **Events API Challenge Handling:**
   - Endpoints responding to the Events API URL verification handshake must echo back the `challenge` parameter only after verifying the request payload format.
4. **Execution Timeout & Asynchronous Processing:**
   - Slack requires HTTP responses to interactive payloads, slash commands, and events within **3 seconds**.
   - Long-running tasks, heavy database queries, or subagent executions MUST be offloaded to asynchronous background workers, immediately returning an HTTP 200 acknowledgment with an optional ephemeral status message.

## Rate limiting and retry resilience

1. **Backoff and Jitter:**
   - API clients and webhook senders must inspect HTTP 429 status codes and `Retry-After` response headers.
   - Implement exponential backoff with full jitter to prevent retry storms against the Slack Web API.
2. **Channel Burst Protection:**
   - Limit message posting frequency to at most 1 message per second per channel.

## Verification and compliance

Validate the app manifest using Slack CLI’s `slack manifest validate` command, then run the application tests configured in this repository. Webhook tests must cover a valid HMAC-SHA256 signature, altered and missing signatures, a stale timestamp outside the accepted window, replayed event identifiers, and URL-verification challenges. Reject invalid requests before acknowledging or acting on them. Use local fixtures or a test workspace; if these tests or an isolated test environment are unavailable, state that capability gap. Run this repository’s Markdown and relative-link checks.

## Related standards

- Slack Interaction & Administration: [`slack-interaction-and-administration.md`](./slack-interaction-and-administration.md)
- Internet-Facing Services: [`internet-facing-services.md`](./internet-facing-services.md)
- Cryptography & Key Management: [`cryptography-and-key-management.md`](./cryptography-and-key-management.md)
- AI Development Security: [`ai-development-security.md`](./ai-development-security.md)

## Sources

- [Slack App Manifest Specification](https://api.slack.com/reference/manifests)
- [Slack Verifying Requests from Slack](https://api.slack.com/authentication/verifying-requests-from-slack)
- [Slack CLI manifest validation](https://docs.slack.dev/tools/slack-cli/reference/commands/slack_manifest_validate/)
- [RFC 6749: The OAuth 2.0 Authorization Framework](https://www.rfc-editor.org/rfc/rfc6749)
