# Specification: 5-Tier Context Management Architecture

- **Status:** Normative Standard
- **Version:** 1.0.0
- **Author:** Koality-Assured Architecture Committee

## 1. Abstract

Large Language Model (LLM) agents operating on expansive software repositories experience rapid context degradation, hallucination, and excessive token expenditure when ingesting monolithic code dumps. This specification establishes a standardized 5-Tier Context Management model that optimizes token allocation through progressive disclosure and AST fact extraction.

## 2. Context Tiers

```
┌──────────────────────────────────────────────────────────┐
│ Tier 1: Fast Routing (<100 tokens, sub-ms dispatch)      │
├──────────────────────────────────────────────────────────┤
│ Tier 2: Metadata Index & Manifests (~500 tokens)         │
├──────────────────────────────────────────────────────────┤
│ Tier 3: Summary Cards & Area Guides (~2k tokens)         │
├──────────────────────────────────────────────────────────┤
│ Tier 4: Extracted AST Facts & Headroom (~5k tokens)      │
├──────────────────────────────────────────────────────────┤
│ Tier 5: Raw Full Text (Targeted on-demand inspection)    │
└──────────────────────────────────────────────────────────┘
```

### 2.1 Tier 1: Fast Routing
- **Format:** Key-value routing tags, keyword maps, and dispatch tables.
- **Latency Budget:** < 1 ms.
- **Token Budget:** < 100 tokens per query.
- **Purpose:** Immediate agent routing to responsible subagents or documentation domains without retrieval overhead.

### 2.2 Tier 2: Metadata Index & Manifests
- **Format:** JSON/YAML catalog metadata, BM25 keyword indices, and file manifests.
- **Token Budget:** 200 - 1,000 tokens.
- **Purpose:** Broad architectural orientation and file inventory filtering.

### 2.3 Tier 3: Summary Cards & Area Guides
- **Format:** High-level Markdown overview cards, interface contracts, and module summaries (`AGENTS.md`).
- **Token Budget:** 1,000 - 3,000 tokens.
- **Purpose:** Contextual understanding of component responsibilities and interaction rules.

### 2.4 Tier 4: Extracted AST Facts & Headroom Compression
- **Format:** Class hierarchies, method signatures, exported types, and call reference graphs extracted via AST parsers.
- **Compression Target:** >= 85% token reduction relative to raw source files.
- **Purpose:** Deep structural comprehension of dependencies and APIs without loading function implementation bodies.

### 2.5 Tier 5: Raw Full Text
- **Format:** Complete, unmodified source code files.
- **Policy:** Strictly restricted to precise files actively undergoing modification or line-by-line debugging.

## 3. Conformance Requirements

1. Agent runtimes **MUST NOT** load raw files (Tier 5) into context prior to filtering via Tiers 1-3.
2. AST extraction engines **MUST** preserve type annotations and public docstrings in Tier 4 artifacts.
3. Runtimes **SHOULD** enforce context headroom budgets to prevent context window saturation.
