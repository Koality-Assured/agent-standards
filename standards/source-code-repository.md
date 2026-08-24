---
doc_kind: requirement
canonical_id: source-code-repository
purpose: [requirement]
rank: high
topics: [code-and-repositories, identity-and-access, data-protection]
rag_keywords: [git, branch-protection, secret-scanning, sso, oidc]
---

# Source code repository security (generalized)

## Purpose

Baseline controls for source repositories that hold intellectual property or production-impacting code. This page is the organization’s git hosting rules; SaaS tenant knobs for other products are in [`saas-security.md`](./saas-security.md).

## Scope

Hosted and self-hosted source repositories, including bots and CI identities that push or merge. Workstation lock and disk encryption for developers are in [`endpoint-and-workstation.md`](./endpoint-and-workstation.md), not duplicated here.

## Authentication and authorization

Repositories must use organizational identity, private-by-default visibility, and least privilege for humans and bots.

- Integrate with organizational SSO where available; prohibit anonymous access.
- Default repositories to private/restricted; visibility changes limited to owners/admins.
- RBAC and least privilege for humans and bots.
- Automation identities are unique, least-privileged, scoped to needed repos, and not used for daily human admin. Prefer OIDC / short-lived tokens over long-lived personal access tokens.
- Unique bot identities should use OIDC (or equivalent workload identity) rather than a standing human PAT.

## Branch protection and review

Default branches must not accept unreviewed, force-pushed, or history-rewritten changes.

- Enable branch protection (or equivalent rulesets) for default branches: required reviews, no direct pushes, status checks when applicable.
- Do not allow force-push or history rewrite on protected branches.
- Require a non-author review before merge to protected branches.
- Dismiss stale reviews when new commits are pushed so an approval cannot outlive the diff it covered.
- The organization should require signed commits for high-assurance repositories; signed commits are not a must for every repo.
- The organization should use path owners (CODEOWNERS or equivalent) for high-impact paths, and two reviewers for production-impacting changes.

## Secrets and data protection

Secrets must not live in git; the hosted copy must scan for them.

- Do not store secrets in code — use a vault or platform secret store ([`passwords-and-credentials.md`](./passwords-and-credentials.md)).
- Enable secret scanning on the hosted repository copy and alert or block on known secret patterns.
- Encrypt data in transit (TLS 1.2+; see [`cryptography-and-key-management.md`](./cryptography-and-key-management.md)).
- Encrypt data at rest for hosted platforms and backup media.
- Report suspected policy breaches through established security channels.

## Logging and endpoints

Access, admin, and protection-rule changes must be attributable; developer devices follow the endpoint standard.

- Retain access and admin activity logs long enough for investigation (commonly ≥ 90 days, or shorter if centrally archived). See [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md).
- Log changes to branch-protection and ruleset configuration.
- Preserve attribution of commits and merges to individual identities.
- Systems that hold clones or repo credentials must meet [`endpoint-and-workstation.md`](./endpoint-and-workstation.md) (disk encryption, idle lock, malware defense).

## Related standards

Credentials: [`passwords-and-credentials.md`](./passwords-and-credentials.md). IAM: [`identity-and-access.md`](./identity-and-access.md). Developer endpoints: [`endpoint-and-workstation.md`](./endpoint-and-workstation.md). GitHub as IaC control plane: [`github-iac-security.md`](./github-iac-security.md). Vendor git SaaS: [`saas-security.md`](./saas-security.md).
