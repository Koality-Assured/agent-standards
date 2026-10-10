---
doc_kind: requirement
canonical_id: repository-beautification
purpose: [requirement, process]
rank: high
topics: [branding, repositories, documentation, visual-identity, packaging]
rag_keywords: [beautify, branding, vector-logo, vector-banner, badges, pyproject-hardening, audit]
---

# Repository Beautification, Visual Identity & Hardening (Normative Standard)

## Purpose

Normative standard governing the visual presentation, identity assets, documentation heroes, live status badges, and packaging hardening across all repositories within the Koality-Assured ecosystem.

Every repository represents the organization's engineering discipline. Incomplete README files, missing visual assets, dead badge links, and packaging crashes degrade developer trust and operational clarity.

## Scope

Applies to all public and internal repositories maintained by Koality-Assured, including:
- Domain AI agent harnesses (`*-router`)
- Core platform engines and libraries (`ai-harness-core`, `harness-cli`)
- Interactive documentation wikis and web portals (`core-harness-wiki`, `personal-portfolio`)
- Security scanners, bots, and operational utilities (`koality-pii-scanner`, `backdoors-and-breaches-bot`, `cloud-scripts`)
- Reference architectures, examples, and catalogs (`logscale-examples`, `pulumi-examples`, `industry-references`)
- Technical white-paper programs (`koality-whitepapers`)

---

## Normative Requirements

### 1. Vector SVG Branding Assets (`assets/`)

Every repository MUST feature dedicated vector XML branding assets committed directly into an `assets/` directory at the repository root:

- **Vector Logo Mark (`assets/<repo-name>-logo.svg`)**:
  - MUST be a valid XML SVG document with `viewBox="0 0 512 512"`.
  - MUST render cleanly in both dark and light display modes without external asset dependencies.
  - MUST incorporate domain-specific geometric motifs adhering to the Art Router representation registry.
- **Vector Hero Banner (`assets/<repo-name>-banner.svg`)**:
  - MUST be a valid XML SVG document with `viewBox="0 0 1280 400"`.
  - MUST feature the high-contrast technical blueprint grid backdrop, dynamic data stream vectors, and domain emblem.
  - MUST prominently display the repository category capsule, uppercase title, tagline, and capability chips.

### 2. Centered README Hero Block

Every repository `README.md` MUST begin with a structured, centered visual hero block:

```markdown
<div align="center">

![<Project Title> Banner](assets/<repo-name>-banner.svg)

# <Project Title>

<p align="center">
  <img src="assets/<repo-name>-logo.svg" alt="<Project Title> Logo" width="128" height="128" />
</p>

**<Project Tagline>**

<Badge Matrix>

</div>

---
```

### 3. Auto-Updating Live Badges

Every repository MUST display live, auto-updating badges in its README hero:

1. **Continuous Integration (CI)**: Direct GitHub Actions workflow status badge targeting the primary workflow (`ci.yml` or `deploy.yml`).
2. **License**: Shields.io badge referencing the repository's open-source or proprietary license (e.g. `License-MIT-blue.svg`).
3. **Runtime / Language**: Python runtime version (`python-3.11+-blue.svg`), Node.js, or Go version where applicable. Pure documentation/IaC blueprint repos without runtimes omit this badge.
4. **Domain Classification**: Domain badge referencing the functional archetype (`domain-<slug>-blueviolet.svg`).
5. **Conventional Commits**: Commit hygiene badge (`Conventional%20Commits-1.0.0-yellow.svg`).

### 4. Setuptools Flat-Layout Package Hardening

Any Python-enabled repository with an `assets/`, `docs/`, or non-package directory in the repository root MUST configure `pyproject.toml` against setuptools multi-package auto-discovery collisions:

```toml
[tool.setuptools]
packages = []
```

Without this declaration, setuptools >= 61 discovers `assets` as an unintended top-level Python package and fails pip builds with:
`error: Multiple top-level packages discovered in a flat-layout: ['assets', ...]`.

---

## Root-Cause Analysis (RCA): Why Recent Repos Were Missed

Prior to this hardening standard, multiple newly initialized repositories (`core-harness-wiki`, `cloud-scripts`, `koality-pii-scanner`, `backdoors-and-breaches-bot`, `logscale-examples`, `pulumi-examples`) were published without branding assets, live badges, or centered heroes.

The genuine root causes were:

1. **Point-in-Time Initiative Scoping**: The initial repository beautification program (`projects/repo-beautification/README.md`) audited a fixed roster of 20 repositories. Once merged, the project was marked `completed` without establishing continuous enforcement.
2. **Narrow Generator Hook Points**: Automated asset synthesis was wired exclusively into `scaffold_harness.py` (domain spokes) and `scaffold_public_repos.py` (a hardcoded list of 6 repositories). Standalone utilities, bots, and documentation wikis were scaffolded outside these generators and inherited no assets.
3. **Absence of Fleet Linter**: No automated audit script existed to inspect active repositories across the ecosystem and flag compliance drift.
4. **Preset Taxonomic Gaps**: `beautify_repo.py` initially lacked presets and motifs for non-router archetypes (`wiki`, `scanner`, `bot`, `cloud-scripts`, `telemetry`, `layers`, `manuscript`).

---

## Automated Enforcement & Audit Gate

Compliance is permanently enforced through two automated tools:

1. **Audit & Drift Detection**:
   ```bash
   python scripts/repos/audit_repo_beautification.py
   ```
   Scans all repositories in `c:\Code\KA` (or specified via `--repos`), verifies XML SVG validity, README hero presence, live badges, and `pyproject.toml` hardening, returning exit code 0 only when 100% compliant.

2. **Automated Remediation**:
   ```bash
   python scripts/repos/audit_repo_beautification.py --fix
   # Or for an individual repo:
   python scripts/repos/beautify_repo.py --repo-dir <path> --domain <domain>
   ```
   Synthesizes vector SVGs, formats the README hero cleanly without duplicating existing badges, hardens package configuration, and writes the canonical MIT license.
