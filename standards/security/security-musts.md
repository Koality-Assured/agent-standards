# Specification: Autonomous Agent Security MUSTs (SEC-01)

- **Status:** Normative Standard
- **Version:** 1.0.0
- **Author:** Koality-Assured Security Working Group
- **RFC 2119 Keywords:** MUST, MUST NOT, SHOULD, RECOMMENDED, MAY

## 1. Abstract

This specification establishes normative, mandatory security requirements for autonomous software development agents, harness runtimes, tool execution engines, and multi-agent systems.

## 2. Normative Requirements

### SEC-01: Sandboxing & Tool Boundary Isolation
- Agent execution engines **MUST** execute shell commands and untrusted scripts in restricted subshells or isolated containers.
- Agent runtimes **MUST** constrain file modification operations to designated working tree paths and reject path traversal outside the root repository directory.

### SEC-02: AST & Code Modification Verification
- Agent runtimes **MUST** validate code changes using language-specific AST parsers to ensure syntactic validity prior to staging or committing changes.
- Automated tooling **MUST NOT** commit syntactically broken code to main or release branches.

### SEC-03: Secret Boundary & Credential Redaction
- Telemetry collectors and log aggregators **MUST** scrub sensitive tokens, API keys, private certificates, and environment secrets prior to persisting or transmitting prompt context.
- Agents **MUST NOT** write plain-text credentials into committed source repositories.

### SEC-04: Context Poisoning & Prompt Injection Defense
- System instructions **MUST** be structurally segregated from untrusted external data (such as web search results or external repository issues).
- Runtimes **MUST** treat external markdown and HTML links as untrusted and neutralize executable schemes (`javascript:`, `data:`, `vbscript:`).

### SEC-05: Worktree & Concurrency Isolation
- Multi-agent orchestrators **MUST** provision separate git worktrees or isolated workspaces for concurrent agents to prevent race conditions and cross-agent file corruption.
