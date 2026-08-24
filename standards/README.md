# Standards

Generalized reusable requirements (no org-specific naming). Each file is Markdown with `purpose` / `rank` frontmatter.

## Foundations

Identity, data, crypto, configuration, and cloud tenancy.

| Doc | Intent |
| --- | --- |
| [`cloud-essentials.md`](./cloud-essentials.md) | Landing zone, org hierarchy, public-access guardrails |
| [`identity-and-access.md`](./identity-and-access.md) | Unique IDs, SSO/MFA, joiner–mover–leaver |
| [`passwords-and-credentials.md`](./passwords-and-credentials.md) | Human passwords and non-human secrets |
| [`privileged-access.md`](./privileged-access.md) | JIT, PAW, IdP/cloud break-glass |
| [`data-protection.md`](./data-protection.md) | Classification, retention, when to encrypt |
| [`cryptography-and-key-management.md`](./cryptography-and-key-management.md) | Algorithms, TLS versions, key custody |
| [`secure-configuration.md`](./secure-configuration.md) | Baselines, gold images, drift, exceptions |

## Surfaces

How people and systems are reached, and engineering control planes.

| Doc | Intent |
| --- | --- |
| [`internet-facing-services.md`](./internet-facing-services.md) | Public / internet-exposed services |
| [`administrative-interfaces.md`](./administrative-interfaces.md) | Admin planes: network, TLS, protocols, local break-glass |
| [`network-and-remote-access.md`](./network-and-remote-access.md) | Segmentation, VPN/ZTNA, DNS, wireless |
| [`endpoint-and-workstation.md`](./endpoint-and-workstation.md) | Disk encryption, lock, EDR/MDM, BYOD |
| [`saas-security.md`](./saas-security.md) | SaaS the business consumes (tenant config) |
| [`source-code-repository.md`](./source-code-repository.md) | Source repository baseline |
| [`github-iac-security.md`](./github-iac-security.md) | GitHub as IaC control plane |
| [`ai-development-security.md`](./ai-development-security.md) | LLM / agent use in engineering work |

## Operations

Detect, patch, respond, recover, and manage suppliers.

| Doc | Intent |
| --- | --- |
| [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md) | Central logs, detection, incident declaration |
| [`vulnerability-and-patch-management.md`](./vulnerability-and-patch-management.md) | Scanning, KEV, patch floor |
| [`incident-response.md`](./incident-response.md) | After declaration: contain, notify, close |
| [`backup-and-recovery.md`](./backup-and-recovery.md) | Copies, isolation, restore tests |
| [`third-party-and-supply-chain.md`](./third-party-and-supply-chain.md) | Buy, assess, contract, exit vendors |
