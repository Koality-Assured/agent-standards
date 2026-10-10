---
doc_kind: requirement
canonical_id: code-signing
purpose: [requirement, security]
rank: high
topics: [code-and-repositories, transport-and-crypto, security-operations]
rag_keywords: [code-signing, certificates, hsm, timestamping, rfc-3161, integrity, provenance]
---

# Code signing (generalized)

## Purpose

Security controls governing code signing certificates, signing pipelines, and cryptographic validation to ensure software packages, binaries, and updates maintain provenance and integrity from build through distribution.

## Scope

All software, executables, scripts, container images, installers, firmwares, and libraries built or distributed by the organization, as well as the cryptographic keys, certificates, and infrastructure used to sign them. Source code repository protections and commit signing are governed separately in [`source-code-repository.md`](./source-code-repository.md).

## Certificate separation and issuance

Signing certificates must be strictly scoped to their intended environment and function.

- Separate in-development signing certificates from certificates used for external or public software distribution. Test and development builds must never carry production distribution signatures.
- Dedicated certificate profiles: Code signing certificates must have specific X.509 `KeyUsage` (`digitalSignature`) and `ExtendedKeyUsage` (`codeSigning`) extensions set. Prohibit combining code signing with `ServerAuthentication` (TLS) or other certificate functions.
- Issue production distribution certificates exclusively through reputable, accredited public Certificate Authorities (CAs). Internal PKI may issue certificates for purely internal tooling and pre-release test builds.
- Immediately revoke compromised or suspect certificates through the issuing PKI Certificate Revocation List (CRL) and OCSP responders.

## Key custody and hardware isolation

Private signing keys must be protected against export, theft, and unauthorized invocation.

- Store private signing keys in a hardware-backed security boundary rated FIPS 140-2 Level 2 or higher (e.g., dedicated Hardware Security Module (HSM), cloud KMS HSM, or hardware authentication tokens).
- Prohibit storing plaintext code-signing private keys on developer workstations, shared network drives, or unencrypted storage media.
- Protect signing operations with multi-factor authentication (MFA) and least-privilege role-based access control. High-assurance release keys must require dual-custody or quorum approval prior to signing.
- Restrict code submission: Maintain an auditable access list defining who and what automated systems may submit artifacts to the signing service.

## Signing system and pipeline architecture

Signing operations must execute within hardened, isolated systems.

- Perform automated signing within dedicated CI/CD build agents or dedicated signing services. Systems performing signing operations must not be used as daily-driver workstations.
- Verify intellectual property and code provenance: Signing pipelines must authenticate the source repository and verify build integrity before invoking signing keys. Never sign unverified third-party binaries under organizational signatures.
- Deploy managed endpoint security (EDR) and configuration baselines on all physical or virtual hosts that interact with signing operations.

## Timestamping and verification

Signed packages must remain valid across certificate lifecycles without runtime failure.

- Mandatory RFC 3161 timestamping: All signed packages and binaries must incorporate a trusted cryptographic timestamp from an approved public or enterprise Timestamping Authority (TSA). Timestamping guarantees software remains valid and verifiable after the signing certificate expires.
- Client validation: Client-side software update mechanisms must cryptographically verify signatures and certificate revocation status before staging or applying updates.

## Cryptographic standards

Ciphers and key lengths must align with industry baseline standards.

- Asymmetric key sizes must meet or exceed current CA/Browser Forum baselines: minimum RSA 3072-bit or Elliptic Curve Cryptography (ECC) with NIST P-256 (or stronger).
- Digest algorithms must use SHA-256 or stronger. The use of deprecated or broken hash algorithms (e.g., MD5, SHA-1) is strictly prohibited.
- Maintain crypto-agility plans to enable migration to post-quantum signatures when standardized by primary bodies.

## Auditability and logging

All certificate lifecycle events and signing transactions must generate immutable audit records.

- Log every signing transaction, capturing the artifact hash, submitter identity, timestamp, certificate identifier, and operation result.
- Log administrative actions, certificate issuance, renewal, export attempts, and permission changes.
- Forward all signing audit logs immediately to the centralized SIEM with standard retention under [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md).

## Verification and non-compliance

Security engineering may inspect signing infrastructure, audit key storage posture, sample signing transaction logs, and verify package signatures at any time.

Unprotected private keys found on workstations, production packages signed with development keys, missing RFC 3161 timestamps, or unauthenticated signing requests constitute critical control failures; suspected key compromise follows [`incident-response.md`](./incident-response.md).

## Related standards

KMS and TLS ciphers: [`cryptography-and-key-management.md`](./cryptography-and-key-management.md). Git commit signing: [`source-code-repository.md`](./source-code-repository.md). Incident response: [`incident-response.md`](./incident-response.md). Endpoint hardening: [`endpoint-and-workstation.md`](./endpoint-and-workstation.md). Central logging: [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md).

## Sources

- [CA/Browser Forum Baseline Requirements for the Issuance and Management of Publicly-Trusted Code Signing Certificates](https://cabforum.org/working-groups/code-signing/)
- [NIST SP 800-57 Part 1 Rev. 5 Recommendation for Key Management](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)
- [RFC 3161 Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)](https://www.rfc-editor.org/rfc/rfc3161)
- [CISA / NSA Securing the Software Supply Chain: Recommended Practices for Developers](https://www.cisa.gov/resources-tools/resources/securing-software-supply-chain-recommended-practices-guide-developers)
