# Cofinal Finsler–Bézoutian completion criterion

This directory contains a standalone PDF note packaging the conditional finite-to-global theorem developed in `T-15104`, together with the exact Finsler and simple-root Bézoutian formulations from `L-15107` and `L-15109`.

## Status

The note proves the following implication under its stated hypotheses:

```text
local-uniform convergence of exact finite targets to Xi
+ cofinal positive target-pinned special-matrix completions
=> finite real-rooted transforms
=> Xi has no nonreal zero in |Im z|<1/2
=> RH.
```

It also proves that the finite completion condition is equivalent to positivity of the pinned form on the nonzero isotropic cone of the universal slope form, and—when the target polynomial has simple real roots—to strict separation of the Bézoutian root thresholds.

This is a **conditional theorem note**. It does not prove that the required target convergence or cofinal positivity/separation hypotheses hold, and therefore it does not claim a proof of the Riemann Hypothesis.

## Files

- `cofinal-finsler-bezoutian-rh-criterion.pdf` — four-page repository proof note.
- `SHA256SUMS` — content digest for the PDF.

The expanded repository theorem is:

- `claims/theorems/T-15104-finsler-hermite-cofinal-criterion.md`

Related finite reductions are:

- `claims/lemmas/L-15107-finsler-target-completion.md`
- `claims/lemmas/L-15109-bezoutian-root-threshold-completion.md`
- `claims/lemmas/L-15108-special-completion-converse.md`

## Validation

The committed PDF was rendered and visually inspected page by page, parsed successfully as PDF 1.4, and contains four unencrypted pages with no forms or JavaScript.
