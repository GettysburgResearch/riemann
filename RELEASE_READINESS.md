# Publication and verification readiness

The [scientific account](STATUS.md) describes an open research project, not a completed proof release. Open mathematics can remain clearly disclosed work. Publication decisions, source verification and formal-proof completion are separate questions.

## Verification status

The conditional-API graph defect has been repaired. [PR #802](https://github.com/GettysburgResearch/riemann/pull/802) records real-registry regressions and ordinary/optimized authenticated full-checkout PASS at merged commit `051808c1f8367b4320c52f94b40908eb2173d622`, tree `115c71ffd64b5f9ab3568185634c9efd07c89333`. Its Windows symlink-test omissions are explicit. The earlier fixture-only and payload-only narratives remain historical evidence; they no longer mean that no real-checkout validation has ever occurred.

A receipt covers its tested tree, not all later commits. For an intended publication commit, run the [current authenticated verifier](integration/2026-09-06/hardening/README.md) selected by [canonical/CURRENT.json](canonical/CURRENT.json). Record the exact commit, platform and actual checks. No remote CI success or new whole-checkout execution is asserted by this editorial update.

## Remaining publication decisions

| Area | What still needs an explicit decision or evidence |
|---|---|
| Distribution | Appropriate project license, imported licenses/notices and paper redistribution rights; history/privacy/credential review at the intended disclosure scope |
| Main and contributor access | Enforced review rules and bypass permissions where available; verify contributor access and the phone walkthrough rather than assuming the documentation was tested |
| Automation | Deliberately decide whether to enable the bounded workflow; local recorded validation is distinct from Actions success |
| Scientific presentation | Keep integrated component scopes, later corrections and active unreviewed work distinguishable; do not advertise exhaustive review |
| Formal claims | Do not advertise a completed source-faithful formal release while the actual-xi repair remains unimplemented/uncompiled at its full intended interface |

This page does not infer current repository settings from an older observation and does not change visibility, permissions, Actions or licensing. Exact historical holds and omissions remain in [the integration record](integration/2026-09-06/RELEASE_HOLDS.md). Its dated unresolved-execution statements must be read with the later verification receipt above.

The unresolved [research tasks](OPEN_CUTS.md) do not have to be solved before publishing clearly labeled research. They do have to remain visible beside any result that depends on them.
