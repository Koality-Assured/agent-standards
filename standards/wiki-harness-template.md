---
doc_kind: requirement
canonical_id: wiki-harness-template
purpose: [decision, requirement]
rank: high
topics: [wiki, harness, agents]
rag_keywords:
  [
    ai-harness-core,
    fed-instance,
    generic-template,
    wiki-structure,
    downstream-sync,
  ]
---

# Wiki harness template versus fed instance

## Purpose

This page records how this wiki relates to the public generic template `ai-harness-core`. Structure here is the source; domain corpus stays in fed instances.

## Fed instance versus generic template

`ai-router` is a fed instance of the wiki harness. It carries a security and tech corpus under `references/`, many pages under `docs/standards/`, and cloud-provider skills.

`ai-harness-core` is the generic wiki harness template. It uses the same folder layout and operating machinery, with domain areas empty or stubbed so another domain router can start from it.

Start a new domain router from the template, then add that domain's corpus. The template must not receive this instance's framework dumps, organization security-ops pages, or cloud-vendor skills.

## What the template keeps

Machinery belongs in `ai-harness-core`. Copy it, then sync later corrections from this wiki:

- Root and nested `AGENTS.md`
- `routing/` (areas, skill-dispatch, isolation)
- Cost layers: qmd, ast-grep, Headroom
- Generic skills, agents, scripts, and `supporting/` notes that are not a vendor or domain corpus
- Harness operating pages such as this one and [`context-management.md`](./context-management.md)

## What the template must not copy

Fed domain content stays in this instance, or in public slice repos that publish a selected corpus. Leave it out of `ai-harness-core`:

- Framework dumps under `references/` (NIST, OWASP, CWE, ATT&CK, and similar)
- Organization security-ops standards under `docs/standards/` (identity, endpoint, cloud tenancy, and the other control pages in that folder), except the harness operating pages listed above
- Cloud-vendor skills (AWS, Azure, GCP)
- Instance `projects/`, `research/`, and `ai-tooling/memory/`

The template may keep empty or stub folders so the layout is recognizable, without the filled domain pages from this instance.

## Sync source

Structure corrections in this wiki are the source that gets synced into `ai-harness-core` via `scripts/sync`. Domain pages remain in this instance and in other public slice repos; they do not go into the template.

This page states the boundary. The file map and redaction pipeline live with the repo-sync specialist.

## Public export

Public export still redacts credentials, tokens, internal paths, and similar secrets. Redaction applies even when the payload is machinery only.

Session rules: [`../agent-session-security.md`](../agent-session-security.md).

## Related

Phase 4 initiative spec: [`../../projects/harness-v2-evolution/README.md`](../../projects/harness-v2-evolution/README.md).
