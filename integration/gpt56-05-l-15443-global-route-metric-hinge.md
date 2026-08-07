# Integration handoff — L-15443 global metric hinge

Date: 2026-08-07  
Agent: `gpt56-05-l`  
Status: `PROPOSED`; RH is not claimed proved

## New claim

`claims/lemmas/L-15443-selberg-volterra-mellin-gauge.md`

The Selberg–Volterra operator of PR #158 satisfies exactly

```text
M L M^-1 = -m^-1 d/dz m,
m(z)=(1+z) zeta(1+z).
```

For `G=mR`,

```text
m M[L(L-log a)r]=G''+log(a)G'.
```

Mellin–Plancherel turns the gauged quadratic form into

```text
integral y(y-log a)|g(y)|^2 dy,
```

which is positive outside the first logarithmic annulus. The physical/source norm conversion remains open and is the exact noncircular review hinge for the proposed Selberg–Mourre completion.

For the actual Chebyshev second difference,

```text
G_a(z)
=(1-a^-z)(1-a^(-z-1/2))[-zeta'(1+z)].
```

The dilation factors vanish only on the boundary lines `Re z=0` and `Re z=-1/2`; every shifted off-critical zero remains an uncanceled simple quotient pole.

## Route connections

- PR #158: use this identity to reconstruct or reject `M-15110.17`; do not count positivity in the gauged metric twice.
- PRs #216/#222/#224: their signed semiprime estimate is a candidate physical metric conversion.
- PR #217: line-zero notches remove known boundary divisors; the variance defect is a scalar trace of the remaining quotient obstruction.
- PR #219 / `L-15439`: polygon/queue transport avoids inverse-zeta division and attacks the physical source directly.
- PR #218: the safe dilation factors are the same boundary-zero geometry in FIR coordinates.

## New report

`reports/gpt56-05-l/2026-08-07-global-route-reconciliation-and-metric-hinge.md`

It freezes and compares current heads #158, #165, #208, #216, #217, #218, #219, #222, and #224, records what has and has not crossed, and names the exact missing steps.

## Merge order

This handoff and `L-15443` are additive to PR #165. They should be independently reviewed before any cross-branch claim is promoted. No source PR should be merged merely because its endpoint is equivalent to the metric hinge.