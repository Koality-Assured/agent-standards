---
doc_kind: requirement
canonical_id: administrative-interfaces
purpose: [requirement]
rank: high
topics: [identity-and-access, transport-and-crypto, web-and-edge, data-protection, security-operations]
rag_keywords: [admin-interface, tls, ssh, rdp, sso, break-glass, oob, snmp]
---

# Administrative interfaces (generalized)

## Purpose

Security baseline for administrative interfaces: any web portal, service, or protocol that allows direct management of an application, system, device, or data.

## Scope

Anyone and any partner who manages or operates servers, applications, network devices, or data platforms. Applies to dedicated admin planes and to dual-use services when they are used for administration.

## Baseline requirements

Every administrative interface must meet these controls, then any type-specific requirements below.

- Limit access to specific IP addresses and CIDR ranges appropriate for the interface’s purpose.
- Prefer an approved tunneled remote-access path (VPN, zero-trust access gateway, or equivalent). Interfaces used only for administration must not be exposed to the public internet or placed at a DMZ/edge.
- Do not use insecure, legacy, or end-of-life protocols.
- Encrypt all traffic with TLS or another approved secure transport. TLS must be 1.2 or higher; disable lower versions.
- Use local accounts only for break-glass or emergency management. Those accounts must meet current identity and credential standards.
- Keep a single break-glass account on the device or system for use when the primary authentication source is unreachable.
- Implement logging and monitoring appropriate to the interface’s purpose and sensitivity.
- Protect data stored or processed through the interface to the same standard as the underlying system.
- Service accounts must be unique to a device or device group and must not be reused across unrelated purposes.
- Service-account credentials and keys must be rotatable without service interruption.

## Network device interfaces

Out-of-band (OOB) and other network-device management planes must meet the baseline plus:

- Authenticate against a centralized identity source.
- Prefer SSH as the management protocol.
- Keep remotely accessible protocol packages current and free of known exploitable defects.
- Use the highest available SNMP version when SNMP is required.

## Remote desktop interfaces

Graphical remote-control services (for example RDP and similar interactive desktop protocols) must meet the baseline plus:

- Do not store plaintext credentials in connection files or configuration strings.
- Reach these services only through a VPN or remote-service gateway; enforce MFA at that gateway.
- Grant access least-privilege, limited to groups that need the system.
- Disable clipboard, printer, and storage redirection on critical systems (for example domain controllers and equivalent identity/control-plane hosts).
- Require a secure pre-session authentication method (for example Network Level Authentication for RDP) so the host does not start a full session before the user is authenticated.

## Web administration interfaces

Browser-based admin planes (content-management consoles, restricted programmatic UIs, dashboards) must meet the baseline plus:

- Do not expose sensitive data without pre-authentication.
- Authenticate through the organization’s identity provider. Prefer claims-based SSO (SAML, OAuth, OIDC) when the product supports it.
- When claims-based SSO is not possible, use an approved identity-provider brokered integration (password vault / form-fill) rather than local admin passwords as the primary path.
- Exceptions require security approval through the organization’s established request channel and must document the technical limitation.
- Disable directory browsing and verbose error output.
- Do not place admin interfaces on the same network segment as databases or unrelated resources.

## Data access interfaces

Services used to manage stored data (databases, code repositories, secrets platforms, directory services, and similar) must meet the baseline plus:

- Do not expose these services to the internet.
- Place them on isolated networks, separate from the hosts that consume them.
- Do not enable unrelated services on the same hosts.
- Restrict network allow-lists to what operation requires.
- Authenticate both query and write paths.

## Verification and non-compliance

The security function may verify compliance at any time, with or without notice, including by querying programmatic interfaces, reviewing SIEM or equivalent telemetry for changes and anomalies, accessing web admin planes, and penetration testing where applicable.

Suspected non-compliance is handled through [`incident-response.md`](./incident-response.md) and may require the owners to repeat security review. Non-compliance may result in remediation work assigned to the owning team.

## Related standards

Privileged identity, JIT, PAW, and IdP/cloud emergency accounts: [`privileged-access.md`](./privileged-access.md). Workforce IAM and MFA: [`identity-and-access.md`](./identity-and-access.md). Passwords and secrets: [`passwords-and-credentials.md`](./passwords-and-credentials.md). Segmentation and VPN/ZTNA: [`network-and-remote-access.md`](./network-and-remote-access.md). TLS versions and ciphers: [`cryptography-and-key-management.md`](./cryptography-and-key-management.md). Public services: [`internet-facing-services.md`](./internet-facing-services.md).
