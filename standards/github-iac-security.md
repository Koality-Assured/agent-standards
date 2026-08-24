---
doc_kind: requirement
canonical_id: github-iac-security
purpose: [requirement]
rank: high
topics: [github, infrastructure-as-code, identity-and-access]
rag_keywords: [actions, oidc, branch-protection, secrets, runners]
---

# GitHub for infrastructure-as-code (generalized)

## Purpose

Security baseline when GitHub is the control plane for infrastructure-as-code.

## Requirements

### AuthZ

- Enforce SSO/MFA for administrators.
- OAuth apps and GitHub Apps get least scopes.
- Prefer fine-grained, short-lived credentials; avoid plaintext secrets in YAML.

### Repository posture

- IaC for a platform lives in dedicated repos (separate from unrelated app code when blast radius differs).
- Default private/internal — not public — for production IaC.
- Branch protection on default branches; required reviews for production-impacting paths.
- Keep production and non-production definitions separable (repos, directories, or stacks) enough to prevent accidental prod apply.

### Actions / CI

- Prefer OIDC federated cloud roles over static cloud keys.
- Self-hosted runners: minimal network access; do not bridge distinct security zones on one runner pool.
- Audit create/update/delete of workflows and secrets.

### Secrets

- Store secrets in GitHub Secrets / OIDC — never in structured config committed to git.
- Rotate on staff change and suspected exposure.

## Related standards

Secrets and rotation: [`passwords-and-credentials.md`](./passwords-and-credentials.md). Workforce IAM: [`identity-and-access.md`](./identity-and-access.md). Branch protection and secret scanning: [`source-code-repository.md`](./source-code-repository.md). Privileged cloud/IdP elevation: [`privileged-access.md`](./privileged-access.md). Cloud landing zone: [`cloud-essentials.md`](./cloud-essentials.md).
