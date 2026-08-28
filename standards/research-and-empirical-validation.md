---
doc_kind: requirement
canonical_id: research-and-empirical-validation
purpose: [requirement, governance, research]
rank: critical
topics: [research, validation, empirical-grounding, sources, proof-of-concept]
rag_keywords: [empirical-evidence, feelings-based, primary-sources, source-hierarchy, proof-of-concept, subagents]
---

# Research and empirical validation standard

## Purpose

Establishes the non-negotiable requirements for empirical grounding, authoritative source verification, proof-of-work validation, and structured research escalation across the harness and agent operations.

## Scope

All agents, tools, harness components, proposals, reviews, architecture designs, and operational responses generated within this repository.

## Requirements

### 1. Empirical grounding vs. feelings-based operations

- All ideas, responses, decisions, proposals, recommendations, and architecture plans MUST be **research-backed** and **empirically proven**.
- The harness and agents MUST NOT make speculative, feelings-based, or ungrounded assertions.
- Subjective impressions (e.g., "I feel this is better", "it is generally believed", or "this seems standard") are strictly prohibited as justification for technical decisions.
- Every architectural choice, security rule, and configuration change must cite verifiable evidence: reproducible test results, benchmarks, or authoritative primary documentation.

### 2. Corpus-first knowledge resolution

- Before initiating external searches or assuming missing information, agents MUST evaluate the in-repo corpus first via precision retrieval (`qmd search` / `qmd get`) and structured code inspection (`ast-grep outline`).
- If the internal corpus provides sufficient, validated information to make an informed decision, agents MUST resolve the inquiry using in-repo assets without incurring external latency or token bloat.
- External research is triggered strictly when the in-repo corpus lacks necessary depth, is demonstrably outdated, or when a novel domain is introduced.

### 3. Proof-of-work and validation gate

- The agent/harness MUST NOT encourage or advise a human or orchestrator to adopt a tool, pattern, script, or configuration without performing the work to prove it as a valid idea.
- Validation methods:
  - **Code and configuration**: Execute local automated tests, dry-run simulations (e.g. `--dry-run`), or linters.
  - **Tooling and scripts**: Perform verification against mock fixtures or isolated test runs.
  - **Process and guidance**: Ground steps against official, versioned product documentation.
- If an idea cannot be validated locally due to platform or permission constraints, the agent MUST explicitly label the idea as unverified hypothesis and outline the exact verification steps required.
- **Root-cause problem solving (no workarounds)**: When fixing errors or defects in tools, scripts, or systems, agents MUST identify and resolve the genuine underlying root cause. Agents MUST NOT conceal, bypass, mask, or work around the problem (e.g. silencing linters without fixing violations, disabling assertions, skipping failing tests, or routing around broken tooling).
- **Ambiguity clarification**: When requirements, prompts, or constraints are ambiguous, contradictory, or underspecified, agents MUST stop and seek clarity from the human rather than proceeding on speculative interpretations.

### 4. Novel scope escalation and subagent research protocol

- When a requested task or concept extends beyond the existing in-repo corpus and documentation, agents MUST dive into the topic in detail rather than hallucinating or skimming.
- For material investigations, the parent dispatcher MUST spawn specialized research subagents (`detailed-activity` with `deep-research`) to conduct structured investigations.
- Subagents must collect primary evidence, document reproduction steps or source citations, and deliver structured findings under `results/research/`.

### 5. Authoritative source credibility hierarchy

When performing external or internet-based research, agents MUST adhere to a strict source credibility hierarchy:

| Tier | Source Category | Description & Examples | Permitted Use |
| --- | --- | --- | --- |
| **Tier 1 (Authoritative Primary)** | Official Vendor & Platform Documentation | Microsoft Learn, AWS Docs, Google Cloud Docs, Anthropic Docs, OpenAI Docs, official GitHub docs. | Primary authority for configurations, APIs, and product behavior. |
| **Tier 1 (Standards Bodies)** | Recognized Standards & RFCs | NIST, MITRE (ATT&CK/ATLAS/CWE), OWASP, CIS, IETF RFCs, ISO/IEC. | Primary authority for security controls, cryptography, and protocols. |
| **Tier 2 (Official Ecosystem)** | Official Repositories & Release Notes | Official GitHub/GitLab org repositories, tagged releases, official vendor issue trackers. | Authority for version compatibility, bug tracking, and implementation details. |
| **Tier 3 (Verified Benchmarks)** | Peer-Reviewed & Published Empirical Benchmarks | Papers with code, LMSYS, official vendor benchmarks with published methodology. | Supporting evidence for performance and model tiering. |
| **Disallowed (Speculative/Secondary)** | Unverified Blogs, SEO Spam & Social Media | Medium articles, unvetted blog posts, Reddit threads, speculative forum commentary. | **Prohibited** for normative standards or architecture decisions. |

Validated source registries and domain lists are maintained in [`references/valid-sources/`](../../references/valid-sources/).

### 6. Durable retention and learning loop

- All verified external findings, benchmark results, newly discovered primary source URLs, and architectural decisions MUST be written back to the owning source area:
  - Authoritative reference captures: `references/<family>/` or `references/valid-sources/`
  - Deep investigations: `results/research/<topic>/` promoted to `research/`
  - Reusable standards and security baselines: `docs/standards/`
  - Operational playbooks: `docs/guidance/`
- Ephemeral chat context or scratch directories MUST NOT serve as the final repository of validated knowledge.

## Related standards

- Session security: [`../agent-session-security.md`](../agent-session-security.md)
- Context management: [`context-management.md`](./context-management.md)
- AI development security: [`ai-development-security.md`](./ai-development-security.md)
- Guidance philosophy: [`../guidance/guidance-philosophy.md`](../guidance/guidance-philosophy.md)
- Valid source catalogs: [`../../references/valid-sources/README.md`](../../references/valid-sources/README.md)
