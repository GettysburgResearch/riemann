# Post-merge verification and reading-path hardening

This pass starts from main `4f461e5ad46e452b1eafa69eddff3b76cd0c12be`, the merge of PR #800. It changes verification and current navigation, not the mathematics, historical releases, review verdicts or trusted Lean sources.

## What changed

The original release validator checked the committed review-tree IDs, but read several working-tree tables without checking their bytes against those IDs. A clean-looking `git status` is also insufficient: the test suite demonstrates a changed table hidden by Git's `assume-unchanged` flag.

The current [verification command](verify.py) first authenticates every tracked file in its declared release/review scope against the committed blob. It rejects missing files, changed bytes, symlink components, untracked files even when ignored, changed frozen review trees, altered published payloads, and an incorrect current pointer. It checks those inputs again after the original resolver completes. Output must be outside the repository and new or empty.

The seven review trees, six older dated integration trees and nine original payload/checker files have fixed identities. Older publication trees are checked as committed trees, not replayed as working-file campaigns. The original `validate.py` and its mathematics fixtures remain byte-identical; they execute only after authentication. No archived reviewer/research program is executed by the wrapper.

The explicit current navigation scope includes 24 entry pages. Local link targets and Markdown heading/explicit-ID anchors are checked there. External URLs and internal links in archived proof/report bodies are not a claimed validation scope. Original-context proof links are the default reading path; the ten byte-identical extracts remain archival copies.

## Reproduce

From a complete, clean repository checkout on Linux with Python 3.10 or newer and Git:

```sh
python3 -I -S -B integration/2026-09-06/hardening/test_verify.py
python3 -I -S -B -O integration/2026-09-06/hardening/test_verify.py
work="$(mktemp -d)"
python3 -I -S -B integration/2026-09-06/hardening/verify.py --output "$work/normal"
python3 -I -S -B -O integration/2026-09-06/hardening/verify.py --output "$work/optimized"
diff -r "$work/normal" "$work/optimized"
```

A successful real-checkout run ends with `PASS_AUTHENTICATED_SCOPED_RELEASE` and produces the existing current claim/edge tables plus `hardening.json`. A test-suite success is instead `PASS_SYNTHETIC_HARDENING_CONTRACTS`. These are deliberately different assurances.

## Executed boundary

The 29 synthetic Git, JSON, path and Markdown tests passed normally and under `-O`, with identical JSON summaries. They include one real invocation of the new CLI's output-path rejection. See [the execution receipt](EXECUTION.json) and retained [test result](test-result.json).

The complete Riemann checkout was not available to the authoring runtime: direct network Git access failed. The connected GitHub API supported source inspection and publication, not a local clone. Thus the new full-checkout command and complete 24-page navigation scan are supplied but are **not reported as executed on Riemann**. Neither a workflow file nor a synthetic fixture is a remote CI run.

The workflow now covers relevant main pushes and PRs, and supports manual dispatch. It uses read-only permissions, immutable action pins, no persistent checkout credentials, and bounded integration tests only. Repository-level Actions availability, branch enforcement, access, publication rights and the formal-source repair remain separate [readiness items](../../../RELEASE_READINESS.md).

Changing the validator or its pins still requires review. This is not a security attestation against a contributor who is also allowed to replace the verifier, and it is not a mathematical proof checker.
