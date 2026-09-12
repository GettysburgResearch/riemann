# Review and publication handoff

Suggested new branch (NOT created): `research/astra/20260912-hyperbolic-renormalization`.
Prepared against main: `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
Suggested title: `research: full analytic Brownian spectrum, exact cutoff law, and arithmetic-shift bridge (HBR28)`.

The accompanying patch adds only this new research directory. It contains no deletions or edits to main's existing files, earlier branches, canonical claims, formal files, or workflows. There is no new remote head SHA or PR number to report.

## Load-bearing review

1. Verify the Banach space in Section 3, the full tail resolvent, algebraic simplicity, and the non-claim of a Schauder basis or zeta spectral interpretation.
2. Verify the exact bounded/Pareto law coupling, mean difference, normalization of the survival density, its full tail, and the signed derivative in (26b).
3. Verify the Mellin cancellation range in (25), absolute Fubini in (26e), and every constant in the shifted-xi identity (29). Check removable points, not only generic s.
4. Verify the native TN2 argument and negative TN3 minor; preserve the common-zero and positive-mixture cautions. None is an off-line xi zero.
5. Reproduce the finite checks in normal and optimized Python. Do not confuse their receipt with a formal proof of the infinite arguments or authentication of a Riemann zero computation.

The central complex-zero estimate is NOT supplied. This requests review of the proposed component mathematics, not approval of an RH proof with its final hypothesis left open.

## Applying the patch

From a local checkout of the intended base, after checking the working tree and branch:

```sh
git apply --check /path/to/riemann_HBR28_add_only.patch
git apply /path/to/riemann_HBR28_add_only.patch
```

These commands do not commit, push, or open a PR. An existing destination file causes the add-only patch to fail rather than overwrite it. The packager checked the patch against an empty temporary fixture and compared resulting file bytes. A full repository checkout was not available, so no claim is made that `git apply --check` was run against main itself.
