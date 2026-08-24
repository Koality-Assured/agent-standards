# RFC 0001: The Koality-Assured Standards RFC Process

- **RFC Number:** 0001
- **Title:** The Koality-Assured Standards RFC Process
- **Status:** Active
- **Author:** Koality-Assured Governance Board
- **Created:** 2026-08-24

## 1. Summary

This document establishes the official Request for Comments (RFC) process for creating, modifying, and retiring standards within the `agent-standards` ecosystem.

## 2. RFC Lifecycle States

```
[Proposed] ──> [Draft] ──> [In-Review] ──> [Accepted] ──> [Final / Normative]
                                 │
                                 └──> [Rejected / Superseded]
```

1. **Proposed:** Initial issue or PR introducing the proposal concept.
2. **Draft:** Complete specification written using `rfcs/template.md`.
3. **In-Review:** 14-day public comment and implementation trial period.
4. **Accepted:** Approved by governance vote and slated for incorporation into `standards/`.
5. **Final / Normative:** Merged as an authoritative normative standard.
6. **Superseded:** Replaced by a newer approved standard.

## 3. Submitting an RFC

1. Copy `rfcs/template.md` to `rfcs/YYYY-short-title.md`.
2. Fill out all required sections: Motivation, Specification, Rationale, Backwards Compatibility, Security Considerations.
3. Open a Pull Request with the label `rfc`.
