<div align="center">
  <img src="assets/agent-standards-banner.svg" alt="Agent Standards Banner" width="100%" />

  <br /><br />

  <img src="assets/agent-standards-logo.svg" alt="Agent Standards Logo" width="130" />

  # Agent Standards (`agent-standards`)

  **Normative specifications for 5-tier context management, A2A interaction protocols, and autonomous agent safety.**

  <p align="center">
    <a href="https://github.com/Koality-Assured/agent-standards/actions/workflows/ci.yml"><img src="https://github.com/Koality-Assured/agent-standards/actions/workflows/ci.yml/badge.svg" alt="Standards CI" /></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT" /></a>
    <a href="standards/"><img src="https://img.shields.io/badge/context-5--Tier%20Hierarchy-blueviolet.svg" alt="Context: 5-Tier Hierarchy" /></a>
    <a href="standards/"><img src="https://img.shields.io/badge/Status-Active_Standards-brightgreen.svg" alt="Status: Active Standards" /></a>
    <a href="rfcs/"><img src="https://img.shields.io/badge/RFCs-Open-orange.svg" alt="RFC Status: Open" /></a>
  </p>
</div>

---

## Mission Statement

`agent-standards` establishes formal, interoperable, and vendor-neutral architectural specifications for autonomous software engineering agents, multi-agent coordination protocols, hierarchical context budget management, and runtime security MUSTs.

As autonomous engineering agents assume operational responsibility over critical production software, ad-hoc prompts and unstructured tool loops create severe failure modes: context saturation, cross-agent state corruption, prompt injection, and hallucinated interfaces. `agent-standards` replaces ad-hoc conventions with mathematically bounded context tiers, RFC 2119 normative constraints, schema-validated messaging envelopes, and empirical safety invariants.

---

## Core Standards Breakdown

### 1. 5-Tier Context Management ([`standards/context/5-tier-context-management.md`](standards/context/5-tier-context-management.md))

The 5-Tier Context Hierarchy enforces progressive disclosure across agent memory layers, eliminating token waste and preserving LLM reasoning headroom:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ Tier 1: Fast Routing           │ <100 tokens   │ Tag lookup & sub-ms dispatch│
├────────────────────────────────┼───────────────┼─────────────────────────────┤
│ Tier 2: Metadata Index         │ ~500 tokens   │ Manifests & catalog filters │
├────────────────────────────────┼───────────────┼─────────────────────────────┤
│ Tier 3: Summary Cards & Guides │ ~2,000 tokens │ Area rules & AGENTS.md      │
├────────────────────────────────┼───────────────┼─────────────────────────────┤
│ Tier 4: Extracted AST Facts    │ ~5,000 tokens │ Symbol graphs & signatures  │
├────────────────────────────────┼───────────────┼─────────────────────────────┤
│ Tier 5: Raw Full Text          │ On-demand     │ Targeted file edits only    │
└────────────────────────────────┴───────────────┴─────────────────────────────┘
```

#### Runtime Layering Mapping
- **System Prompt:** Static, platform-native baseline rules and tool definitions.
- **Project AGENTS (`AGENTS.md`):** Global project constraints, normative directive hierarchy (`critical` > `must` > `should`), and routing contracts.
- **Area AGENTS (Nested `AGENTS.md`):** Just-in-Time (JIT) deltas for specific directories; never preloaded globally.
- **JIT Skills (`SKILL.md`):** Specialist domain capabilities loaded exclusively on demand.
- **Ephemeral Working Memory:** Isolated turn context and AST structural facts discarded upon task completion.

---

### 2. Agent-to-Agent (A2A) Interaction Protocol ([`standards/protocols/a2a-protocol-v1.md`](standards/protocols/a2a-protocol-v1.md))

The A2A specification defines structured asynchronous message envelopes, communication semantics, and lifecycle state machines governing orchestrators and specialized subagents:

- **Interaction Cards & Envelopes:** All inter-agent traffic MUST adhere to [`specs/a2a-message.schema.json`](specs/a2a-message.schema.json), enforcing explicit `message_id`, `correlation_id`, `sender`, `recipient`, and `message_type`.
- **Exchange Budgets:** Strict conversation turn budgets (default: 8 exchanges) prevent runaway delegation loops and excessive operational costs.
- **Untrusted Boundary Defense:** Subagent and peer outputs are treated as untrusted data inputs. Instructions within data payloads MUST NOT be executed as system-level directives.
- **Lifecycle Invariants:** Clean state progression through `Spawned` → `Dispatched` → `Executing` → `Completed`, monitored by periodic `heartbeat` signals.

---

### 3. Cost Layers: Hybrid Retrieval & Compression

High-efficiency token preservation layers ensure agents operate sustainably across massive codebases:

- **Markdown via `qmd` Hybrid Retrieval:** Leverages BM25 keyword matching and vector embeddings against detached search indexes, preventing massive full-file doc dumps.
- **Structured Files via `ast-grep` Facts:** Extracts symbol definitions, public interfaces, and call graphs with outline-first inspection, delivering **85%+ token reduction** compared to raw code ingestion.
- **Headroom Compression:** Synthesizes structural facts and strips boilerplate while retaining invariants, ensuring critical context fits within reasoning budgets.

---

### 4. Agent Security MUSTs ([`standards/security/security-musts.md`](standards/security/security-musts.md))

Normative RFC 2119 invariants enforced across agent runtimes:

| Rule ID | Standard Title | Normative Invariant |
| :--- | :--- | :--- |
| **SEC-01** | **Sandboxing & Tool Isolation** | Runtimes **MUST** isolate shell execution in restricted subshells and enforce repository boundary containment. |
| **SEC-02** | **AST Verification** | Changes **MUST** pass AST syntax validation before committing; broken code **MUST NOT** reach main branches. |
| **SEC-03** | **Secret Scrubbing** | Telemetry and logs **MUST** scrub credentials, API tokens, and private keys prior to persistence or context injection. |
| **SEC-04** | **Prompt Injection Defenses** | Instructions **MUST** be structurally segregated from untrusted input; executable schemes in markdown are neutralized. |
| **SEC-05** | **Worktree & Concurrency Isolation**| Orchestrators **MUST** provision isolated git worktrees for concurrent agents to prevent cross-agent write races. |

---

## Architectural Workflow & Communication Flow

### Context Loading & Progressive Disclosure Flow

```mermaid
flowchart TD
    Start([User / Agent Query]) --> T1[Tier 1: Fast Routing<br/>Sub-ms lookup, &lt;100 tokens]
    T1 --> Matched{Area or Skill<br/>Identified?}
    
    Matched -->|No| T2[Tier 2: Metadata Index & Manifests<br/>qmd search & catalog filter, ~500 tokens]
    T2 --> T3[Tier 3: Summary Cards & Area AGENTS<br/>Targeted JIT area constraints, ~2k tokens]
    Matched -->|Yes| T3
    
    T3 --> NeedsCode{Inspection or<br/>Mutation Needed?}
    NeedsCode -->|Structural Comprehension| T4[Tier 4: AST Fact Extraction<br/>ast-grep outlines & signatures, 85%+ savings]
    T4 --> Complete[Context Budget Preserved<br/>LLM Headroom Intact]
    
    NeedsCode -->|Direct Mutation / Edit| T5[Tier 5: Raw Full Text<br/>Line-bounded view_file & replace_file_content]
    T5 --> Complete
```

### A2A Orchestration & Boundary Defense Flow

```mermaid
sequenceDiagram
    autonumber
    participant Parent as Orchestrator (Parent)
    participant Bus as A2A Message Bus & Schema Validator
    participant Sub as Specialist Subagent
    participant Target as Isolated Worktree / Tool Sandbox

    Parent->>Bus: task_dispatch (Schema-validated Envelope, 8-exchange budget)
    Bus->>Sub: Ingest with Clean Slate (No parent transcript leakage)
    Sub-->>Bus: task_acknowledge
    Bus-->>Parent: Ack confirmation

    loop Execution & Liveness
        Sub->>Target: Execute scoped operations in isolated worktree
        Sub->>Bus: heartbeat (Progress & telemetry metrics)
        Bus->>Parent: Relay heartbeat
    end

    Sub->>Bus: task_result (Status, modified files, execution metrics)
    Bus->>Parent: Deliver task_result envelope
    Note over Parent: Untrusted Boundary Defense:<br/>Audit results against user goals<br/>AST validation & syntax verification
    Parent->>Target: Verify AST syntax & test suite
    Parent->>Parent: Commit & session-end gates
```

---

## Repository Structure

```
agent-standards/
├── .github/workflows/ci.yml    # Continuous Integration & schema validation
├── assets/                     # Vector branding and architectural visual assets
│   ├── agent-standards-banner.svg   # Widescreen hero identity banner
│   └── agent-standards-logo.svg     # 5-tier context & normative compass logo
├── standards/                  # Normative specifications (RFC 2119)
│   ├── context/
│   │   └── 5-tier-context-management.md  # 5-Tier Context Architecture specification
│   ├── protocols/
│   │   └── a2a-protocol-v1.md            # Agent-to-Agent Messaging Protocol v1
│   └── security/
│       └── security-musts.md             # Normative Security MUSTs for Agent Runtimes
├── specs/                      # Machine-readable JSON schemas
│   ├── a2a-message.schema.json           # A2A Message Envelope JSON Schema
│   └── context-manifest.schema.json      # Context Manifest JSON Schema
├── rfcs/                       # Request for Comments (RFC) process & proposals
│   ├── 0001-rfc-process.md               # RFC Governance & Lifecycle Process
│   └── template.md                       # RFC Submission Template
├── tools/                      # Validation CLI tooling
│   ├── __init__.py
│   └── validate_specs.py                 # Standards & RFC validation CLI
├── tests/                      # Automated validation test suites
│   ├── __init__.py
│   └── test_standards_validation.py
├── .editorconfig               # Repository formatting rules
├── .gitignore                  # Git ignore rules
├── LICENSE                     # MIT License
└── README.md                   # Repository documentation
```

---

## RFC Governance & Lifecycle

We welcome contributions, amendments, and new RFC proposals from the autonomous agent research community.

1. **Governance Process:** Review [`rfcs/0001-rfc-process.md`](rfcs/0001-rfc-process.md) for standard lifecycle states:
   $$\text{Proposed} \longrightarrow \text{Draft} \longrightarrow \text{In-Review} \longrightarrow \text{Accepted} \longrightarrow \text{Final}$$
2. **Drafting Proposals:** Copy [`rfcs/template.md`](rfcs/template.md) to `rfcs/YYYY-your-rfc-title.md`.
3. **Submission:** Open a Pull Request following [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `refactor:`) for community review and architecture committee evaluation.

---

## Testing & Specification Validation

Validate all JSON schemas, RFC frontmatter, and normative standards locally:

```bash
# Validate all schemas, RFCs, and markdown structure
python tools/validate_specs.py --all

# Run automated unit test suite
python -m unittest discover -s tests -v

# Run pytest (if installed)
pytest tests/ -v
```

All Pull Requests trigger the [Standards CI](https://github.com/Koality-Assured/agent-standards/actions/workflows/ci.yml) workflow running on Python 3.10, 3.11, and 3.12.

---

## Security Invariants

Standards published in this repository are actively tested against known prompt-injection vectors, context poisoning attacks, and tool privilege-escalation exploits. To report potential vulnerabilities in specifications or reference schemas, contact `security@koality-assured.org`.

---

## License

Distributed under the [MIT License](LICENSE). Copyright &copy; 2026 Koality-Assured.
