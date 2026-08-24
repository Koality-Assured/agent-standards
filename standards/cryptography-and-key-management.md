---
doc_kind: requirement
canonical_id: cryptography-and-key-management
purpose: [requirement]
rank: high
topics: [transport-and-crypto, data-protection]
rag_keywords: [tls, aes, kms, hsm, cryptoperiod, certificates]
---

# Cryptography and key management (generalized)

## Purpose

Which cryptographic algorithms and TLS versions are acceptable, and how keys and certificates are custodied. *When* to encrypt is in [`data-protection.md`](./data-protection.md).

## Scope

TLS for services, data-at-rest ciphers, signing hashes, and encryption-key lifecycle (including cloud KMS/HSM). Human passwords and API-key rotation are in [`passwords-and-credentials.md`](./passwords-and-credentials.md).

## Written policy and approved algorithms

The organization must publish a crypto policy so product teams do not pick deprecated ciphers ad hoc.

- TLS 1.2 is the minimum for production; TLS 1.3 should be preferred where clients support it. Disable SSL and TLS 1.0/1.1.
- Symmetric encryption: AES-128 minimum; AES-256 for Restricted data.
- Hashing for integrity and new signatures: SHA-256 or stronger.
- Asymmetric: RSA 2048-bit minimum or NIST P-256 (or stronger curves). Prefer the stronger option for new Restricted-data protection.
- Do not use DES, 3DES, MD5, RC4, or SHA-1 to protect new data or new authenticators.
- Internet-facing TLS profile (HSTS, origin lock) is in [`internet-facing-services.md`](./internet-facing-services.md).

The organization should use envelope encryption (data keys wrapped by a key-encryption key) and should maintain a crypto-agility plan, including a post-quantum cryptography (PQC) roadmap. PQC-everywhere-now is not required.

## Key custody and lifecycle

Encryption keys must live in an approved KMS or HSM, never in git or application config files.

- Generate, store, and use keys in KMS/HSM (or an equivalent hardware-backed service). Application code holds handles or data keys briefly, not the master key.
- Each customer-managed key (or equivalent) has a named owner.
- Split duties: key administrators must not also be the standing data administrators for the same corpus where the platform allows.
- Define cryptoperiods. Rotating a key-encryption key is not the same as re-encrypting all data; document which rotations require re-wrap versus re-encrypt.
- Inventory certificates (public and private PKI) with owners and expiry; do not allow silent expiry on production endpoints.
- Audit key-management operations (create, rotate, disable, destroy, policy change).
- Destroy or disable keys at end of life so leftover CMKs are not a standing decrypt path for retired data stores.

## Verification and non-compliance

Security may inventory TLS versions on public and admin endpoints, confirm KMS/HSM custody, and sample certificate expiry and key-admin separation.

TLS 1.0/1.1 left enabled, keys in git, or a production certificate allowed to expire are control failures; suspected key compromise follows [`incident-response.md`](./incident-response.md).

## Related standards

When to encrypt: [`data-protection.md`](./data-protection.md). TLS on public services: [`internet-facing-services.md`](./internet-facing-services.md). Admin-plane TLS: [`administrative-interfaces.md`](./administrative-interfaces.md). Secrets that are not encryption keys: [`passwords-and-credentials.md`](./passwords-and-credentials.md).

## Sources

- [NIST SP 800-57 Part 1 Rev. 5 Recommendation for Key Management](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)
- [NIST SP 800-52 Rev. 2 Guidelines for TLS Implementations](https://csrc.nist.gov/pubs/sp/800/52/r2/final)
- [OWASP Transport Layer Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
