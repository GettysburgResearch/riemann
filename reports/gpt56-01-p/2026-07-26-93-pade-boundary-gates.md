# Report — support-aware Padé boundary gates and candidate reranking

Agent: `gpt56-01-p`  
Issue: #93  
Date: 2026-07-26

## Result

This continuation reviewed the newest direct-ξ, selected-factor, saturated
sign-chain, support-gap, and screw-function branches before extending the
current moment attack.

The main theorem, L-9312, proves that adjoining any one exact horizontal node to
a frozen direct-ξ moment table introduces one scalar Stieltjes value.  Every
new moment is determined by

```text
a_k = b_(k+1) + w b_k.
```

The full degree-extended RH test is the intersection of two affine rank-one PSD
pencils.  A violation produces an explicit response polynomial `q(y)^2` or,
when a certified residual support gap `y>=A` is available,
`(y-A)q(y)^2`.

## Empirical correction

The previous absolute-gap ranking favored `x=5/4`, with lower gap about
`6.92e-8`.  The new invariant Padé coordinate shows that the full admissible
interval collapses at the same rate.  Its normalized lower coordinate is about
`0.2486`, versus `0.2173` at `x=1`.

Near the old horizontal-grid edge, normalized coordinates below `0.002` were
found, but absolute lower gaps remain near `12` and barycentric conditioning is
extreme.  Two apparent boundary crossings at ordinary 50-digit precision were
refuted by 120-digit replays.  They are preserved as precision regressions.

## Strongest finite next computation

PR #105 already contains four directed twenty-node tables through `x=1/2`.
Those data define nineteen response moments and the complete degree-at-most-18
half-line polynomial cone.  Existing order-two Loewner positivity does not
close that cone.

The highest-priority centers are:

```text
distinct-gap edge             20225875608339631745427 / 2^32
maximum local line-zero mass  20225875608339765963155 / 2^32
PR71 baseline                 20225875608341108140435 / 2^32
upper PR71-gap mirror         20225875608345134672275 / 2^32
```

A complete Hankel/localizing replay on those retained primitive tables is the
next proposed calculation.  Complete slab support from PR #108/#110 can tighten
the localizer without another completed-ξ evaluation.

## Exact implementation

X-9310 is a standard-library exact checker for one-node Padé/support-gap
certificates.  It reconstructs the moments with `Fraction`, contracts rational
witnesses, and performs exact LDL plus exact interval row-radius closure.

Seven adversarial tests pass.  Synthetic controls certify one positive table,
one lower square violation, and one upper support-localizer violation.

## Counterexample status

No strict directed Riemann-ξ negative was produced.  No candidate ID is
allocated.  The empirical points and cross-thread target list are preserved as
work items, not counterexamples.
