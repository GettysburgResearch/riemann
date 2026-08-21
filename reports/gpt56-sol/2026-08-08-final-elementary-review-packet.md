# Final elementary review packet — 2026-08-08

## Executive conclusion

The elementary programme is consolidated to one canonical theorem, Weighted Shell-Tail Stability (`WSTS`). The current repository does **not** prove WSTS unconditionally. Instead, frozen PR #276 proves the equivalence

\[
\mathrm{WSTS}\Longleftrightarrow\mathrm{RH}.
\]

This is a substantial completion of the reduction programme but is not an unconditional proof of RH.

## Canonical review target

Freeze PR #276 at

```text
a65a02b9463c1cc3a10d0af03ab359a637e357cd
```

and review its dependency chain. `T-28001` in this branch is the compact repository-wide map explaining which older mechanisms are retained, superseded, or refuted.

## Why this is the right consolidation

The positive parabolic seed, endpoint-scale frame, continuum defect ordering, finite shell geometry, prime-tail transport, and square-screw consumer are all useful and substantially reduce the problem. But attempts to turn those ingredients into an automatic last estimate repeatedly encounter the same logarithmic/von-Mangoldt mode.

PR #276 isolates that mode as the finite weighted shell charge `B_X` and proves that controlling it by `X^epsilon` for every epsilon is exactly equivalent to RH. This prevents the project from accidentally relabeling an RH-equivalent sampling statement as a routine transfer lemma.

## Important negative results retained

- generic boundary B-spline positivity does not survive truncation;
- direct prime-parent capacity transport overloads the root;
- sharp finite Gamma minorants cannot evade the global reciprocal-zeta equality state by boundary escape;
- monotone positive-part covers lose square-root mass;
- unweighted prime-tail queues have a deterministic positive density drift;
- pure carry windows cancel the reciprocal-zeta pole and therefore cannot by themselves supply RH-sensitive physical coercivity.

These corrections are part of the proof architecture: they tell reviewers what not to accept as a hidden closure.

## Recommended reviewer verdict vocabulary

For each imported claim use only:

```text
VERIFIED
VERIFIED WITH FIXES
UNPROVEN
FALSE
```

Reserve `FALSE` for an exact contradiction. Missing cofinal estimates are `UNPROVEN`.

## Final state

```text
review-ready reduction to one scalar       YES
finite/exact elementary geometry           STRONG / REQUIRES REVIEW
WSTS <=> RH                                PROPOSED COMPLETE
unconditional WSTS                         NO
unconditional RH proof                     NO
```

A genuine final proof must now prove WSTS or map another independently proved theorem to it without importing an RH-equivalent estimate under a new name.