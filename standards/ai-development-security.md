---
doc_kind: requirement
canonical_id: ai-development-security
purpose: [requirement, security]
rank: high
topics: [agents, data-protection, governance, code-and-repositories]
rag_keywords: [llm, prompt-injection, mcp, rag, agentic-tooling, ide-assistants, hallucinated-packages, loop-controls]
---

# AI development security (generalized)

## Purpose

Minimum security requirements for deploying and utilizing Large Language Models (LLMs), generative AI tools, Model Context Protocol (MCP) servers, autonomous coding agents, and AI developer assistants while protecting intellectual property, secrets, personal data, and production infrastructure.

## Scope

All software engineers, contractors, automated workflows, and internal applications that integrate or send organizational data into AI platforms, models, agents, retrieval systems, or IDE extensions.

## Approved use and governance

AI platform adoption must align with data sensitivity and accountability.

- Approved platforms and models: Use only AI services, model tiers, and enterprise tenants that provide documented zero data retention (ZDR) or explicit contractual guarantees that organizational prompts and code are not used for public model training.
- Account accountability: Each automated agent, assistant, or deployed AI workflow must have a designated human or technical owner accountable for its actions, resource consumption, and data handling.
- Personal AI accounts: Prohibit sending internal source code, proprietary algorithms, customer personal data, or operational configurations to personal consumer AI subscriptions or unvetted web chat interfaces.

## High-risk systems and review gates

High-risk AI use cases require explicit architectural and security review prior to granting autonomous permissions:

- Systems with access to private source repositories containing core intellectual property.
- Workflows processing regulated personal data, financial transactions, legal documents, or sensitive corporate records.
- Autonomous or semi-autonomous agents equipped with tools to modify production infrastructure, databases, cloud resources, or source code default branches.
- Customer-facing automated interfaces that execute transactions or generate legal commitments.
- Adversarial pre-deployment testing: High-risk systems must undergo testing against direct prompt injection, indirect prompt injection (via external data feeds or search), tool misuse, data exfiltration, and unsafe autonomy before production release.

## Data protection and secret hygiene

Prompts, system instructions, and tool payloads must enforce strict data minimization.

- Prohibited data: Passwords, API keys, private certificates, session cookies, database credentials, and cryptographic secrets must never be passed into AI models or system prompts.
- Output filtering: Filter and scan AI responses for accidental echoing of credentials or sensitive data before persisting outputs to logs or external systems.
- Non-production data: Prohibit uploading unmasked Confidential or Restricted production databases to AI retrieval indexes or model prompts.

## Model Context Protocol (MCP) and agentic tool security

Agent tools with programmatic execution capabilities must enforce defense-in-depth isolation.

- Principle of least functionality: Equip agents only with the minimal set of tools strictly required for their task. Prohibit broad, unrestricted administrative or shell tools when narrowly scoped domain tools suffice.
- Tool execution sandboxing: Tool execution environments (e.g., containerized runners, isolated workspaces, ephemeral VMs) must restrict network egress to allowlisted endpoints and operate under least privilege.
- Human confirmation for state mutations: Any agent tool call that mutates persistent state (e.g., executing code, modifying databases, deleting resources, pushing git commits, deploying infrastructure) must require explicit human approval or operate within bounded, pre-authorized guardrails.
- Tool input and output validation: All parameters supplied to tools must undergo schema validation and sanitization prior to execution. Tool outputs must be treated as untrusted data and checked for indirect prompt injection prior to feeding back into model context.
- Tool invocation auditability: Log all tool calls, input arguments, execution timestamps, calling agent identities, and output statuses to the centralized SIEM.

## Retrieval-Augmented Generation (RAG) and knowledge base governance

Vector databases, knowledge bases, and document retrieval pipelines must preserve access boundaries.

- Approved ingestion sources: Ingest documents into RAG stores only from verified, authoritative repositories. Validate document integrity before embedding.
- Boundary enforcement: RAG retrieval mechanisms must enforce access control lists matching the underlying document classification. A user or agent querying a RAG pipeline must not receive excerpts from documents they lack permission to read in the primary system of record.
- Corpus drift and revocation: Stale, deprecated, or revoked documents must be purged from retrieval indices on a defined schedule to prevent models from generating hallucinations or enforcing outdated policies.
- Citation and provenance: Generative responses derived from RAG pipelines must provide verifiable source citations, enabling operators to audit factual grounding.

## IDE assistants and developer hygiene

Developer-facing AI coding assistants must adhere to secure development practices.

- Context scoping: Restrict IDE assistant context windows to the relevant project files. Avoid broad repository indexing that sweeps in local `.env` files, credentials, or private configuration.
- Hallucinated package defense: Developers must manually verify the existence, provenance, and reputation of any newly suggested third-party library or package before adding it to package manifests (`package.json`, `requirements.txt`, etc.) to defend against package hallucination and dependency confusion attacks.
- Secret scanning on generated code: Run automated secret scanning and SAST linters on AI-generated code prior to committing. AI coding assistants must not introduce hardcoded secrets or bypass standard linter rules.
- Public code filtering: Enable public code and license matching filters in IDE assistants to prevent accidental copying of GPL-licensed or copyrighted snippets into proprietary codebases.

## CI/CD gates and autonomous development

Autonomous coding agents operating within CI/CD pipelines must remain bounded.

- Mandatory security gates: Pull requests containing AI-generated code must pass standard automated branch protection checks (static analysis, dependency vulnerability scanning, unit tests, secret scanning) before merge.
- Human code review: AI-generated pull requests must require at least one human peer review prior to merging into protected default branches.
- Agent segregation: Maintain clear boundaries between coordinator agents that plan tasks and specialist agents that execute bounded mutations within isolated task worktrees.

## Cost, pacing, and abuse controls

Autonomous loops must incorporate circuit breakers against runaway execution.

- Pacing and quotas: Configure token quotas, rate limits, and maximum multi-turn thresholds across all agent deployments.
- Loop detection: Autonomous agents must incorporate circuit breakers that detect cyclic tool failures or repetitive generation loops and automatically abort execution after a bounded limit (default: maximum 8 exchanges or 15 tool retries).

## Verification and non-compliance

Security may audit AI tool configurations, inspect MCP server logs, audit RAG data permissions, and scan repositories for unverified AI dependencies at any time.

Hardcoded secrets in system prompts, uncontained autonomous mutating tools without human gates, unverified hallucinated packages introduced into production manifests, or bypassed branch protection constitute control failures; suspected prompt-injection compromises follow [`incident-response.md`](./incident-response.md).

## Related standards

Secrets hygiene: [`passwords-and-credentials.md`](./passwords-and-credentials.md). Source code security: [`source-code-repository.md`](./source-code-repository.md). Supply chain: [`open-source-software-security.md`](./open-source-software-security.md). Incident response: [`incident-response.md`](./incident-response.md). SaaS security: [`saas-security.md`](./saas-security.md).

## Sources

- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework)
- [MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/)
- [CISA / UK NCSC Guidelines for Secure AI System Development](https://www.cisa.gov/resources-tools/resources/guidelines-secure-ai-system-development)
