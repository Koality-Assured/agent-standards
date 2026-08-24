---
doc_kind: requirement
canonical_id: passwords-and-credentials
purpose: [requirement]
rank: high
topics: [identity-and-access, data-protection, code-and-repositories]
rag_keywords: [password, secrets, vault, rotation, oidc]
---

# Passwords and credentials (generalized)

## Purpose

How human passwords and non-human secrets are created, stored, and rotated. This page is credential hygiene, not who gets an account (IAM) or how privilege is elevated.

## Scope

Human passwords, API keys, tokens, certificates used as credentials, and other secrets that authenticate a person or workload. Algorithm and key-custody rules for encryption keys are in [`cryptography-and-key-management.md`](./cryptography-and-key-management.md).

## Human passwords

Password policy must favor length, blocklists, and password-manager use over composition rules and calendar rotation.

- If a password is the only authenticator, require at least 15 characters; if MFA is in use, require at least 8. Permit lengths of 64 characters (or the platform maximum if lower).
- Do not impose composition rules (mixed case, digits, symbols) as a substitute for length.
- Do not require periodic rotation of human passwords. Rotate only on suspected compromise, authenticator change, or known exposure.
- Block common, breached, and context-specific passwords (organization name, username).
- Allow paste and password-manager autofill; do not disable paste on password fields.
- Store passwords with a salted, slow hash (or the platform’s equivalent managed IdP store). Do not store reversible password databases for authentication.
- Initial and reset passwords must be single-use and expire quickly.

Where password-only accounts remain, the organization should raise the floor to 14 characters (CIS / Microsoft guidance) until those accounts are moved to MFA.

## Non-human secrets

Machine credentials must be unique, inventoried, and rotated; NIST’s “no periodic human password rotation” rule does not apply to API keys and similar secrets.

- Do not commit secrets to git or other source history. Prefer OIDC (or equivalent workload identity) and short-lived tokens over long-lived static keys.
- Store remaining static secrets in an approved vault or platform secret store with least-privilege access.
- Rotate machine secrets on a defined cryptoperiod, on owner change, and on suspected exposure.
- Issue unique credentials per workload and environment; do not share a key across production and non-production.
- Inventory secrets with a named owner; revoke unused credentials.
- Build and deploy identities must not use a human’s personal access token as the standing production credential.

## Verification and non-compliance

Security may scan repositories for secrets, sample password-policy settings, and inventory vault credentials for owners and last rotation.

Secrets in git, calendar-based human password expiry used as a substitute for length and MFA, or unrotated shared API keys are control failures; suspected exposure follows [`incident-response.md`](./incident-response.md).

## Related standards

Who authenticates: [`identity-and-access.md`](./identity-and-access.md). Repo secret scanning: [`source-code-repository.md`](./source-code-repository.md). Encryption keys: [`cryptography-and-key-management.md`](./cryptography-and-key-management.md). Privileged elevation: [`privileged-access.md`](./privileged-access.md).

## Sources

- [NIST SP 800-63B-4 Authentication and Authenticator Management](https://csrc.nist.gov/pubs/sp/800/63b/4/final)
- [Microsoft password policy recommendations](https://learn.microsoft.com/microsoft-365/admin/misc/password-policy-recommendations)
- [CIS Password Policy Guide](https://www.cisecurity.org/insights/white-papers/cis-password-policy-guide)
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
