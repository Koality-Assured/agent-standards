# Standards

Generalized reusable requirements (no org-specific naming). Each file is Markdown with `purpose` / `rank` frontmatter.

## Harness template

Operating rules for this wiki as a fed instance of a generic template.

| Doc | Intent |
| --- | --- |
| [`context-management.md`](./context-management.md) | 5-tier context hierarchy and prompt caching |
| [`research-and-empirical-validation.md`](./research-and-empirical-validation.md) | Empirical grounding, authoritative source hierarchy, and proof-of-work validation |
| [`harness-template.md`](./harness-template.md) | Generic template vs fed instance; what syncs into `ai-harness-core` |
| [`us-law-reference-use.md`](./us-law-reference-use.md) | How operators use the US primary-law corpus in the legal router |

## Foundations

Identity, data, crypto, configuration, virtualization, and cloud tenancy.

| Doc | Intent |
| --- | --- |
| [`zero-trust-architecture.md`](./zero-trust-architecture.md) | Core NIST SP 800-207 tenets, PDP/PEP, continuous verification |
| [`cloud-essentials.md`](./cloud-essentials.md) | Landing zone, org hierarchy, public-access guardrails |
| [`identity-and-access.md`](./identity-and-access.md) | Unique IDs, SSO/MFA, joiner–mover–leaver |
| [`passwords-and-credentials.md`](./passwords-and-credentials.md) | Human passwords and non-human secrets |
| [`privileged-access.md`](./privileged-access.md) | JIT, PAW, IdP/cloud break-glass |
| [`data-protection.md`](./data-protection.md) | Classification, retention, when to encrypt |
| [`cryptography-and-key-management.md`](./cryptography-and-key-management.md) | Algorithms, TLS versions, key custody |
| [`secure-configuration.md`](./secure-configuration.md) | Baselines, gold images, drift, exceptions |
| [`hypervisor-security.md`](./hypervisor-security.md) | Bare-metal hypervisors, TPM/Secure Boot, host lockdown |

## Surfaces

How people and systems are reached, runtime environments, and engineering control planes.

| Doc | Intent |
| --- | --- |
| [`internet-facing-services.md`](./internet-facing-services.md) | Public / internet-exposed services |
| [`web-application-firewall.md`](./web-application-firewall.md) | WAF baseline, OWASP CRS, virtual patching, preview mode |
| [`administrative-interfaces.md`](./administrative-interfaces.md) | Admin planes: network, TLS, protocols, local break-glass |
| [`network-and-remote-access.md`](./network-and-remote-access.md) | 4-zone segmentation, ZTNA/VPN, protective DNS, wireless |
| [`endpoint-and-workstation.md`](./endpoint-and-workstation.md) | Disk encryption, lock, EDR baseline, MDM, Clean Source tiers |
| [`kubernetes-security.md`](./kubernetes-security.md) | Managed K8s clusters, workload identity, network policies, GitOps |
| [`saas-security.md`](./saas-security.md) | SaaS the business consumes (tenant config) |
| [`source-code-repository.md`](./source-code-repository.md) | Source repository baseline |
| [`github-iac-security.md`](./github-iac-security.md) | GitHub as IaC control plane |
| [`open-source-software-security.md`](./open-source-software-security.md) | OSS ingestion, immutable lockfiles, OpenSSF Scorecards, SCA |
| [`code-signing.md`](./code-signing.md) | Code signing certificates, HSM key custody, RFC 3161 timestamps |
| [`ai-development-security.md`](./ai-development-security.md) | LLM / agent use, MCP tool sandboxing, RAG boundaries, loop controls |

## Operations

Detect, patch, respond, recover, and manage suppliers.

| Doc | Intent |
| --- | --- |
| [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md) | 6-stage telemetry model, high-risk events, pipeline health |
| [`vulnerability-and-patch-management.md`](./vulnerability-and-patch-management.md) | Scanning, KEV, patch floor |
| [`incident-response.md`](./incident-response.md) | After declaration: contain, notify, close |
| [`backup-and-recovery.md`](./backup-and-recovery.md) | Copies, isolation, restore tests |
| [`third-party-and-supply-chain.md`](./third-party-and-supply-chain.md) | Buy, assess, contract, exit vendors |

## Platform and tool integrations

Enterprise collaboration and operational suite integration standards.

| Doc | Intent |
| --- | --- |
| [`confluence-app-development-and-webhooks.md`](./confluence-app-development-and-webhooks.md) | Forge/Connect app manifests and webhook security |
| [`confluence-interaction-and-administration.md`](./confluence-interaction-and-administration.md) | Space permissions, page restrictions, and REST API |
| [`google-suite-interaction-and-administration.md`](./google-suite-interaction-and-administration.md) | Google Workspace domain administration and sharing rules |
| [`slack-app-development-and-webhooks.md`](./slack-app-development-and-webhooks.md) | Slack app manifests, request verification, and scopes |
| [`slack-interaction-and-administration.md`](./slack-interaction-and-administration.md) | Workspace administration, channel governance, retention |
