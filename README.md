# Agent Standards (`agent-standards`)

[![Standards CI](https://github.com/Koality-Assured/agent-standards/actions/workflows/ci.yml/badge.svg)](https://github.com/Koality-Assured/agent-standards/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Active Standards](https://img.shields.io/badge/Status-Active_Standards-brightgreen.svg)](standards/)
[![RFC Status: Open](https://img.shields.io/badge/RFCs-Open-orange.svg)](rfcs/)

## Mission Statement

`agent-standards` defines formal, interoperable, and vendor-neutral specifications for autonomous agentic systems, multi-agent coordination protocols, hierarchical context budget management, and agent security MUSTs.

As autonomous engineering agents assume greater operational responsibility, establishing uniform interfaces and provable safety invariants is essential to enable cross-platform reliability, deterministic orchestration, and robust containment.

## Architecture Overview

```
agent-standards/
├── .github/workflows/ci.yml    # CI test & RFC validation workflow
├── standards/                  # Formal normative specifications
│   ├── context/
│   │   └── 5-tier-context-management.md  # 5-Tier Context Architecture specification
│   ├── protocols/
│   │   └── a2a-protocol-v1.md            # Agent-to-Agent (A2A) Messaging Protocol v1
│   └── security/
│       └── security-musts.md             # Normative Security MUSTs for Agent Runtimes
├── specs/                      # Machine-readable JSON schemas
│   ├── a2a-message.schema.json           # A2A Message Envelope JSON Schema
│   └── context-manifest.schema.json      # Context Manifest JSON Schema
├── rfcs/                       # Request for Comments (RFC) process & proposals
│   ├── 0001-rfc-process.md               # RFC Governance & Lifecycle Process
│   └── template.md                       # RFC Submission Template
├── tools/                      # Validation scripts
│   ├── __init__.py
│   └── validate_specs.py                 # Standards & RFC validation CLI
├── tests/                      # Automated validation tests
│   ├── __init__.py
│   └── test_standards_validation.py
├── .editorconfig               # Editor configuration
├── .gitignore                  # Git ignore rules
└── LICENSE                     # MIT License
```

## Standards Summary

### 1. 5-Tier Context Management ([`standards/context/5-tier-context-management.md`](standards/context/5-tier-context-management.md))
Specifies the hierarchical context budgeting model designed to preserve LLM reasoning headroom:
- **Tier 1: Fast Routing:** Sub-millisecond routing indices and tag lookup tables (<100 tokens).
- **Tier 2: Metadata Index & Manifests:** Structured catalog summaries and semantic search keywords.
- **Tier 3: Summary Cards & Area Guides:** High-level component summaries and operational playbooks.
- **Tier 4: Extracted AST Facts:** Deterministic symbol graphs, call hierarchies, and method signatures (85%+ token reduction).
- **Tier 5: Raw Full Text:** Selective, on-demand full file inspection reserved for direct editing.

### 2. Agent-to-Agent (A2A) Protocol ([`standards/protocols/a2a-protocol-v1.md`](standards/protocols/a2a-protocol-v1.md))
Defines structured asynchronous message envelopes, state machines, task delegation, heartbeat monitoring, and parent-subagent handoffs.

### 3. Agent Security MUSTs ([`standards/security/security-musts.md`](standards/security/security-musts.md))
Authoritative RFC 2119 security requirements for agent runtimes:
- **SEC-01: Sandboxing & Tool Isolation:** Runtimes MUST isolate shell execution and enforce working directory boundaries.
- **SEC-02: AST Validation:** Runtimes MUST validate syntax trees prior to committing edits.
- **SEC-03: Secret Boundary Protection:** Runtimes MUST NOT leak credentials into context or telemetry.
- **SEC-04: Prompt Injection Defenses:** Systems MUST separate instruction channels from untrusted user and web inputs.

## RFC Governance & Proposals

We welcome contributions to existing standards and new RFC proposals:
1. Review [`rfcs/0001-rfc-process.md`](rfcs/0001-rfc-process.md) for lifecycle states (**Proposed** → **Draft** → **In-Review** → **Accepted** → **Final**).
2. Copy [`rfcs/template.md`](rfcs/template.md) to `rfcs/YYYY-your-rfc-title.md`.
3. Submit a Pull Request for community review and voting.

## Validation CLI

Run specification and RFC schema validation locally:

```bash
# Validate all standards, RFCs, and schemas
python tools/validate_specs.py --all

# Run automated tests
python -m unittest discover -s tests -v
```

## Security Notice

Standards defined in this repository are actively tested against known prompt-injection and privilege-escalation vectors. To report potential standard-level security flaws, contact security@koality-assured.org.

## License

Distributed under the [MIT License](LICENSE). Copyright (c) 2026 Koality-Assured.
