# Release readiness

**Scientific record:** the September 6 integration is a scoped, corrected research record. RH remains unproved. **Public-launch clearance:** not asserted.

This page is the current operational checklist. The [original release holds](integration/2026-09-06/RELEASE_HOLDS.md) and reviewer omission ledgers remain authoritative detail; they are not erased by this post-merge pass.

| Area | Current disposition | Required evidence for completion |
|---|---|---|
| Review preservation | A, B, C and all four D directories are frozen; original reports and failed checks remain available. | The authenticated checkout command verifies every consumed working file and all seven tree IDs. |
| Current navigation and validation | Hardened runner and 29 normal/optimized synthetic regression tests are supplied. | A real-checkout `PASS_AUTHENTICATED_SCOPED_RELEASE` receipt at the intended commit; not merely a workflow definition or a payload-only PASS. |
| Scientific coverage | Scope, corrections, conditional inputs and omissions are explicit. Unreviewed material is not newly accepted. | Targeted proof/source reviews for the named omissions and adapters; not a blanket rereview or a required proof of every open problem. |
| Actual-Xi formal source | The empty-input defect is disclosed; the conditional paper repair is retained outside trusted imports. | An inhabited source-faithful Lean repair, synchronized definitions/consumers/locks, exact-tree build, comparator and axiom audit. |
| Other formal and external imports | Historical pins and conditional inputs are preserved. | The separately requested import-closure, physical-integral, primitive-certificate and toolchain checks. |
| Automation and access | This pass changes only the bounded integration workflow, not permissions or visibility. | Owner verification of Actions availability, enforced main-branch review rules, bypass/access settings and the contributor workflow. |
| Public distribution | No all-history privacy/credential or comprehensive imported-rights audit is claimed. No license was selected by this pass. | Owner review of history, credentials/personal data, licenses, notices and paper redistribution rights before changing visibility. |

## One verification entry point

Use [canonical/CURRENT.json](canonical/CURRENT.json), whose resolver is the [authenticated scoped verifier](integration/2026-09-06/hardening/verify.py). Commands, exact scope and the distinction between synthetic and real-checkout success are in its [README](integration/2026-09-06/hardening/README.md).

Open mathematics is expected in a research project. It may be published as clearly labeled research; it must not be silently promoted into accepted mathematics. Likewise, the source-specific formal hold is not a claim that Lean's kernel or all finite algebra is invalid.

This checklist does not authorize a visibility change, invent a CI success, or declare the omitted audits complete.
