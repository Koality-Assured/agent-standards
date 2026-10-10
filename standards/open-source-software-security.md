---
doc_kind: requirement
canonical_id: open-source-software-security
purpose: [requirement, security]
rank: high
topics: [code-and-repositories, third-party-and-supply-chain, governance]
rag_keywords: [oss, open-source, sca, lockfiles, ossf-scorecard, supply-chain, dependency-pinning, artifactory]
---

# Open-source software security (generalized)

## Purpose

Mandatory security controls governing the evaluation, adoption, integration, and lifecycle management of open-source software (OSS) components, third-party dependencies, and build-time tooling to mitigate software supply-chain risk.

## Scope

All open-source libraries, packages, frameworks, container base layers, and build-time utilities integrated into software engineered or maintained by the organization. Commercial SaaS vendors and procurement contracts are governed in [`third-party-and-supply-chain.md`](./third-party-and-supply-chain.md). Git hosting controls are in [`source-code-repository.md`](./source-code-repository.md).

## Sourcing and registries

Dependencies must originate from trusted, authenticated distribution channels.

- Ingest open-source packages exclusively from official package ecosystem registries (e.g., npmjs, PyPI, Maven Central, crates.io) or approved internal artifact mirrors (e.g., Artifactory, Nexus). Prohibit retrieving dependencies directly from arbitrary, unvetted internet URLs during build processes.
- Internal mirrors and proxy caches must verify upstream registry TLS certificates, validate package checksums, and enforce organizational blocklists for malicious packages.
- Namespace protection: Configure package manager configurations to prevent dependency confusion attacks (e.g., ensuring internal private packages cannot be shadowed by public registry packages).

## Version pinning and deterministic builds

Build pipelines must produce deterministic, reproducible artifacts using pinned dependency trees.

- Explicit version pinning: Declare exact, unchanging dependency versions in package manifests. Prohibit floating version ranges (e.g., `^`, `~`, `>=`), wildcards (`*`), and moving tags (`latest`).
- Mandatory lockfiles: Dependency resolution records and lockfiles (e.g., `package-lock.json`, `pnpm-lock.yaml`, `poetry.lock`, `go.sum`, `Cargo.lock`, `packages.lock.json`) must be committed to source code repositories alongside manifests.
- Enforce locked-mode CI/CD builds: Continuous integration workflows must use commands that strictly honor committed lockfiles without resolving new upstream versions (e.g., `npm ci`, `bundle install --frozen`, `dotnet restore --locked-mode`). Builds must fail immediately if lockfiles drift from package manifests.

## CI/CD actions and pipeline plugins

Third-party automation components introduced into CI/CD pipelines represent direct supply-chain attack vectors.

- Pin pipeline actions to immutable commit SHAs: All third-party GitHub Actions, pipeline extensions, and build runners must be pinned to full 40-character commit SHAs, not mutable tags or branch names (e.g., `actions/checkout@a81bbbf...` rather than `@v3`).
- Minimize token permissions: Restrict default repository permissions (`GITHUB_TOKEN` or equivalent pipeline tokens) to read-only; grant write permissions only to explicitly necessary pipeline stages.
- Prohibition of unpinned remote scripts: Executing unpinned external scripts fetched dynamically over the network (e.g., `curl -sSL https://... | bash` or `wget -O - ... | sh`) in build or deployment pipelines is strictly prohibited. External scripts must be vendored, version-controlled, or fetched from an internal artifact repository and verified against a cryptographic SHA-256 digest before execution.

## Dependency evaluation and health metrics

Teams must assess new open-source packages for maintainability and security hygiene prior to integration.

- OpenSSF Scorecard evaluation: When evaluating new open-source libraries, teams should assess repository health using OpenSSF Scorecard metrics, targeting acceptable thresholds across code review practices, branch protection, CI automated testing, and maintenance activity.
- Prohibit unmaintained packages: Teams must not introduce packages that have lacked active maintenance or updates for over 24 months, unless accompanied by documented architectural justification and formal security approval.
- High-risk dependency scrutiny: Dependencies that process authentication, cryptography, personal data, or network inputs require explicit security review prior to production adoption.

## Software composition analysis and vulnerability management

All codebase dependencies must undergo automated vulnerability and license tracking.

- Continuous SCA scanning: Enable automated Software Composition Analysis (SCA) tooling across all repositories to continuously identify known Common Vulnerabilities and Exposures (CVEs) in transitive and direct dependencies.
- Build-failing thresholds: Pipelines must block merges or deployments that introduce unmitigated Critical or High severity CVEs unless an approved time-bound exception is logged.
- Dependency inventory: The organization must maintain an up-to-date inventory and Software Bill of Materials (SBOM) for all production software, enabling rapid triage during zero-day disclosure events.

## Verification and non-compliance

Security engineering may run automated supply-chain scanners against repositories and inspect CI build definitions at any time.

Unpinned dependency ranges in production projects, missing lockfiles, mutable pipeline action tags, unpinned `curl | bash` commands, or open Critical CVEs in production dependencies constitute control failures; suspected dependency compromises follow [`incident-response.md`](./incident-response.md).

## Related standards

Vendor procurement: [`third-party-and-supply-chain.md`](./third-party-and-supply-chain.md). Git hosting and secret scanning: [`source-code-repository.md`](./source-code-repository.md). Vulnerability management: [`vulnerability-and-patch-management.md`](./vulnerability-and-patch-management.md). Incident response: [`incident-response.md`](./incident-response.md).

## Sources

- [OpenSSF Scorecard Project](https://securityscorecards.dev/)
- [NIST SP 800-161 Rev. 1 Cybersecurity Supply Chain Risk Management Practices](https://csrc.nist.gov/pubs/sp/800/161/r1/final)
- [CISA / NSA Securing the Software Supply Chain: Recommended Practices for Developers](https://www.cisa.gov/resources-tools/resources/securing-software-supply-chain-recommended-practices-guide-developers)
- [OWASP Software Component Verification Standard (SCVS)](https://owasp.org/www-project-software-component-verification-standard/)
