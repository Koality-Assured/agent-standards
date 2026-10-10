---
doc_kind: requirement
canonical_id: kubernetes-security
purpose: [requirement, security]
rank: high
topics: [infrastructure-as-code, cloud, security-operations]
rag_keywords: [kubernetes, k8s, eks, gke, aks, rbac, network-policy, pod-identity, admission-controller]
---

# Kubernetes security (generalized)

## Purpose

Baseline security controls for provisioning, configuring, operating, and deploying workloads onto managed and self-hosted Kubernetes clusters across multi-cloud and on-premises environments.

## Scope

All production, staging, and development Kubernetes clusters (including Amazon EKS, Google GKE, Microsoft AKS, and self-hosted distributions), along with the containerized workloads, CI/CD pipelines, and engineers interacting with them.

## Cluster provisioning and control plane

Clusters must be provisioned immutably via code and minimize exposure of the Kubernetes control plane.

- Provision all clusters using version-controlled Infrastructure as Code (IaC) subject to peer review and automated linting.
- Disable public API server endpoints by default. When public access is strictly required, restrict endpoint access to explicit, documented CIDR allowlists.
- Maintain cluster versions within supported release windows: no more than three minor versions behind the current stable Kubernetes release.
- Prohibit direct SSH access to cluster worker nodes. Use cloud-native session managers (e.g., AWS Systems Manager Session Manager, GCP OS Login) or ephemeral debug sessions when node-level troubleshooting is necessary.
- Deploy worker nodes exclusively across private subnets without public IPv4 addresses.

## Identity and access control

Authentication and authorization must enforce least privilege and avoid static credentials.

- Enforce Role-Based Access Control (RBAC) with minimal privileges for human operators and automated controllers. Regularly audit and eliminate cluster-admin role bindings.
- Applications and internal workloads must authenticate to cloud resources using cloud-native workload identity mechanisms (e.g., AWS EKS Pod Identity / IAM Roles for Service Accounts, GCP Workload Identity, Azure Workload Identity). Do not mount static cloud credentials into pods.
- Human access via `kubectl` must authenticate through the organizational Identity Provider (IdP) and cloud IAM. Deprecate legacy authentication bridges (such as the EKS `aws-auth` ConfigMap) in favor of direct cloud IAM access entries.
- Use distinct ServiceAccounts per workload. Prohibit using the default ServiceAccount for application workloads.

## Network security and ingress

Network traffic inside and across cluster boundaries must enforce default-deny isolation.

- Enable a container network interface (CNI) plugin that supports `NetworkPolicy` enforcement.
- Apply default-deny `NetworkPolicy` rules for ingress and egress across non-system namespaces, explicitly allowlisting only necessary service-to-service communication.
- Terminate external traffic at an approved Ingress controller or service mesh gateway with TLS 1.2+ encryption and strict cipher suites.
- Segment cluster networks from general corporate networks, allowing communication only through authenticated, stateful gateways.

## Secrets and configuration management

Sensitive data must be encrypted at rest and dynamic at runtime.

- Enable KMS envelope encryption for all Kubernetes Secrets at rest within `etcd`.
- Prohibit hardcoded secrets, API tokens, and private keys in container images, pod manifests, Helm values files, or environment variables.
- Retrieve runtime secrets dynamically using an external secrets operator (such as External Secrets Operator or the Kubernetes Secrets Store CSI Driver) backed by the organizational secret vault.

## Container image and workload hardening

Only vetted, minimal, and verified container images may execute in the cluster.

- Build workloads from minimal, approved base images obtained from authenticated, private container registries.
- Apply immutable image tags (digest or unique build ID); prohibit mutable tags such as `:latest` in production manifests.
- Enable automatic vulnerability scanning on all container registries; gate deployments on the absence of unmitigated Critical and High vulnerabilities.
- Cryptographically sign container images during CI/CD (e.g. via Sigstore/Cosign or Notary) and verify signatures upon deployment.
- Enforce non-root execution (`runAsNonRoot: true`), read-only root filesystems (`readOnlyRootFilesystem: true`), and drop all unnecessary Linux capabilities (`capabilities: drop: ["ALL"]`).
- Define explicit CPU and memory resource requests and limits on every workload to protect against resource exhaustion and denial-of-service.

## Admission control and deployment pipelines

Workload deployments must pass automated policy enforcement before entering the cluster.

- Deploy workloads through automated GitOps workflows (e.g., ArgoCD, Flux) to ensure cluster state matches version-controlled manifests and to minimize human access to production clusters.
- Enforce admission controllers (e.g., Kyverno, Open Policy Agent / Gatekeeper) to validate manifests against security policies prior to scheduling.
- Validate Helm charts and manifests in CI/CD using static linters and security scanners before deployment.

## Observability and monitoring

Cluster control planes and workload behaviors must produce searchable audit telemetry.

- Enable Kubernetes API server audit logging and stream logs directly to the central SIEM.
- Capture pod stdout/stderr logs and forward them to centralized logging with appropriate retention.
- Monitor node and pod CPU, memory, and network usage with alerting on anomalous spikes, crash loops, or resource starvation.
- Deploy runtime security agents (e.g., eBPF-based behavioral monitoring) to detect unexpected process execution, privilege escalation, or outbound connections.

## Verification and non-compliance

Security may audit cluster configurations, inspect API audit logs, scan running images for CVEs, and verify admission policy compliance at any time.

Publicly exposed API endpoints without CIDR restriction, workloads running as root on read-write filesystems, unencrypted secrets in etcd, or untracked cluster-admin bindings constitute control failures; suspected compromised pods follow [`incident-response.md`](./incident-response.md).

## Related standards

Cloud tenancy: [`cloud-essentials.md`](./cloud-essentials.md). IaC pipeline controls: [`github-iac-security.md`](./github-iac-security.md). Secret storage: [`passwords-and-credentials.md`](./passwords-and-credentials.md). Incident response: [`incident-response.md`](./incident-response.md). Central logging: [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md).

## Sources

- [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes)
- [NIST SP 800-190 Application Container Security Guide](https://csrc.nist.gov/pubs/sp/800/190/final)
- [Kubernetes Hardening Guidance (NSA/CISA)](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)
