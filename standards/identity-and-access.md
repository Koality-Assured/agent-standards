---
doc_kind: requirement
canonical_id: identity-and-access
purpose: [requirement]
rank: high
topics: [identity-and-access, governance]
rag_keywords: [sso, mfa, joiner-mover-leaver, aal2, least-privilege]
---

# Identity and access (generalized)

## Purpose

Who may access organizational systems, how they authenticate, and how joiner–mover–leaver (JML) changes are applied. This page is identity policy, not password hashing, secret rotation, or privileged-elevation process.

## Scope

Workforce identities, contractor identities, and application identities that authenticate to organizational systems. How secrets are stored is [`passwords-and-credentials.md`](./passwords-and-credentials.md). How privilege is elevated is [`privileged-access.md`](./privileged-access.md).

## Unique identities and federation

Every person and every non-human actor that authenticates must have a unique identity; shared logins are not an acceptable primary path.

- Issue unique identities; do not share human accounts.
- Default authentication to an organizational identity provider (IdP) with single sign-on (SSO) for workforce applications that support it.
- Do not leave default vendor or product accounts enabled after commissioning.
- Run a quarterly inventory of accounts against HR or contractor records and disable identities that no longer have a business need.

## Authentication strength

Workforce authentication must meet authenticator assurance level 2 (AAL2) equivalent: something you have plus something you know or a biometric, not a password alone.

- Require multi-factor authentication (MFA) for workforce access to organizational systems.
- Require phishing-resistant authenticators (for example FIDO2 / passkeys or equivalent) for privileged roles.
- Do not use email as an authentication factor.
- Restrict SMS OTP to legacy exceptions with an expiry; do not adopt it for new privileged paths.
- Account recovery must not bypass MFA (recovery must re-establish equivalent assurance).

The organization should issue passkeys (or equivalent phishing-resistant authenticators) to all workforce users and, where push notifications remain, require number-matching.

## Joiner, mover, leaver and authorization

Access must follow least privilege and must be disabled — not deleted — when someone leaves, so audit history remains attributable.

- Joiners receive only the roles required for the role; movers lose prior access that the new role does not need.
- Leavers: disable the identity promptly; do not delete until retention and investigation needs are met.
- Disable dormant workforce identities after approximately 45 days of inactivity unless a documented exception exists.
- Roles and groups must be least-privilege; standing broad roles (global admin, owner, root-equivalent) are privileged access, not daily IAM.
- Automate JML from the HR system of record when practical.

## Verification and non-compliance

Security may sample SSO coverage, MFA enrollment (including phishing-resistant authenticators on privileged roles), dormant accounts, and leftover default vendor accounts.

Shared human logins, MFA bypass via recovery, or privileged access without phishing-resistant MFA are control failures; suspected account takeover follows [`incident-response.md`](./incident-response.md).

## Related standards

Credentials: [`passwords-and-credentials.md`](./passwords-and-credentials.md). Elevation and break-glass: [`privileged-access.md`](./privileged-access.md). How humans reach admin planes: [`administrative-interfaces.md`](./administrative-interfaces.md). SaaS tenant SSO: [`saas-security.md`](./saas-security.md).

## Sources

- [NIST SP 800-63-4 Digital Identity Guidelines](https://csrc.nist.gov/pubs/sp/800/63/4/final)
- [NIST SP 800-63B-4 Authentication and Authenticator Management](https://csrc.nist.gov/pubs/sp/800/63b/4/final)
- [CISA phishing-resistant MFA](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf)
