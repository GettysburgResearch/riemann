# Live release-enforcement observations and uncompleted owner gates

Repository: GettysburgResearch/riemann. Observation scope: this retry's connected GitHub reads, not an atomic snapshot or all-history security audit.

- `get_repo` returned private visibility, not archived, and default branch main. The connection reported broad permissions; this does not enumerate other contributors' effective access.
- Direct main ref and `GET /branches/main` returned `8d16f8d9c475db290bc85e53d775b93b9bcdb336`. The branch response reports `protected:false`, protection disabled, status-check enforcement off and empty required contexts/checks.
- `GET /rulesets?includes_parents=true&per_page=100` returned HTTP 403 with the feature-tier message asking for an upgrade or public visibility. No ruleset list was returned. This is not a successful full organization-rules audit.

The owner must establish enforceable main-branch controls before relying on the written contributor policy at public launch: required PR/review conditions, appropriate code-owner review, and force-push/deletion restrictions should be checked against the effective configuration and bypass actors. A README or CODEOWNERS file is not enforcement.

Private visibility is not itself an error. This review does not authorize changing it. All-history credential/PII examination, third-party licenses/NOTICE requirements and paper redistribution rights, complete ACL/bypass review, and an end-to-end contributor onboarding check remain uncompleted. No secret leak, licensing violation or compromise is asserted merely because these gates are open.

No visibility, collaborator, team, permission, branch rule, workflow or repository setting was changed. This document records owner-only work, not a request to execute it automatically.
