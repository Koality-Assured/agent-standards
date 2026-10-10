---
doc_kind: requirement
canonical_id: web-application-firewall
purpose: [requirement, security]
rank: high
topics: [web-and-edge, cloud, security-operations]
rag_keywords: [waf, owasp-crs, virtual-patching, edge-security, modsecurity, cloudflare, aws-waf]
---

# Web application firewall (generalized)

## Purpose

Baseline security controls for Web Application Firewalls (WAF) deployed to defend HTTP and HTTPS applications, web APIs, and edge gateways from application-layer threats, bot traffic, and common exploitation techniques.

## Scope

All internet-facing and high-risk internal web applications, microservices, and HTTP/REST/GraphQL APIs deployed in cloud, containerized, or on-premises environments across the organization. Edge exposure rules are in [`internet-facing-services.md`](./internet-facing-services.md).

## General architecture and deployment

Publicly exposed services must terminate through a managed Layer 7 application firewall.

- External and high-risk internal HTTP/HTTPS applications must be fronted by an approved cloud-native (e.g., AWS WAF, Cloudflare WAF, Google Cloud Armor) or host-based (e.g., ModSecurity) Web Application Firewall.
- Origin lock: Configure origin web servers and application load balancers to deny traffic that does not originate from the authorized WAF or CDN edge IP ranges.
- Cloud WAF instances must be provisioned and managed via Infrastructure as Code (IaC) within centralized infrastructure and security management repos.

## Core rulesets and attack prevention

WAF policies must enforce baseline coverage against standardized web attack categories.

- Deploy an approved industry-standard ruleset (such as the OWASP ModSecurity Core Rule Set or cloud provider managed rule groups).
- Mandatory blocking coverage: Rules detecting SQL Injection (SQLi), Cross-Site Scripting (XSS), Local File Inclusion (LFI), Remote File Inclusion (RFI), and Remote Code Execution (RCE) must be enforced in active block mode.
- Rate limiting and denial-of-service: Enable rate-based rules on sensitive endpoints (e.g., login, password reset, token issue, high-cost search APIs) to defend against brute-force and application-layer DoS.
- Bot and credential stuffing defense: Implement managed bot mitigation and IP reputation feeds on user authentication endpoints.

## Staging lifecycle and preview mode

New WAF configurations must undergo structured tuning to prevent application disruptions.

- Audit and preview mode: When onboarding a new web application to a WAF, the policy must operate in non-blocking preview/audit mode for a minimum of seven (7) days.
- Traffic validation: Application teams must execute realistic synthetic tests and monitor production traffic during the audit period to identify false positives.
- Omission and exclusion rules: Any documented false positives must be addressed with targeted, path-specific exclusion rules before transitioning the policy to active blocking mode. Global rule disables are prohibited without written security approval.

## Rule priority architecture and governance

Rule evaluation orders must maintain centralized security oversight.

- Enforce a standardized rule priority numbering hierarchy. A dedicated priority range (e.g., all rule numbers below 2000) must be reserved exclusively for organization-wide security and compliance rules.
- Application-specific exception rules or custom routing must evaluate at lower priority numbers than centralized threat rules and must never supersede mandatory security blocks.
- Administrator access to WAF management consoles must require SSO with phishing-resistant MFA, enforce least-privilege RBAC, and forbid shared local administrator credentials.

## Virtual patching

WAF rules must serve as rapid compensating controls during security incidents.

- When an exploitable web vulnerability is identified in an active application and cannot be immediately remediated via software patch or code fix, security engineering must deploy a targeted WAF virtual patch rule.
- Virtual patches remain active until the application team deploys, verifies, and promotes the underlying code remediation to production.

## Protocol and HTTP surface hardening

WAFs must sanitize inbound HTTP request structures before they reach upstream application servers.

- Enforce HTTPS: Redirect all plain HTTP requests to HTTPS, or enforce immediate denial. Terminate TLS using version 1.2 or higher, disabling legacy protocols per [`cryptography-and-key-management.md`](./cryptography-and-key-management.md).
- HTTP Method Filtering: Restrict HTTP methods to those explicitly supported by the application (e.g., allow GET, POST, HEAD; block or monitor TRACE, TRACK, DELETE, PUT where inapplicable).
- Geographic Fencing: Applications intended strictly for specific jurisdictions should apply ISO 3166-2 geographic IP allowlists with default-deny rules at the WAF layer.

## Logging and observability

Every action taken by the WAF must be recorded for incident detection and threat analysis.

- Log all blocked and challenged requests, capturing client IP, timestamp, requested URI, request headers, matched rule ID, and action taken.
- Stream WAF access and block telemetry to the central SIEM in real time, with log retention adhering to [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md).
- Configure automated alerting on sudden spikes in blocked transactions, persistent high-volume scans, or virtual patch triggers.

## Verification and non-compliance

Security may test WAF policies via automated perimeter scanners, penetration testing, or rule configuration audits at any time.

Unprotected public web endpoints, WAF policies left in monitoring mode indefinitely without justification, or bypassed security rule priority bands are control failures; active attacks circumventing WAF policies follow [`incident-response.md`](./incident-response.md).

## Related standards

Public edges: [`internet-facing-services.md`](./internet-facing-services.md). Transport and TLS ciphers: [`cryptography-and-key-management.md`](./cryptography-and-key-management.md). Patching and CVEs: [`vulnerability-and-patch-management.md`](./vulnerability-and-patch-management.md). Incident response: [`incident-response.md`](./incident-response.md). Central logging: [`logging-monitoring-and-detection.md`](./logging-monitoring-and-detection.md).

## Sources

- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [OWASP ModSecurity Core Rule Set (CRS)](https://coreruleset.org/)
- [NIST SP 800-44 Rev. 2 Guidelines on Securing Public Web Servers](https://csrc.nist.gov/pubs/sp/800/44/r2/final)
- [CISA Web Application Security Guide](https://www.cisa.gov/resources-tools/resources/capacity-enhancement-guide-securing-web-applications)
