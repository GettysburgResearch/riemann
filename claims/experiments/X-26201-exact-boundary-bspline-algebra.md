# X-26201 — Exact boundary B-spline algebra

Claim ID: `X-26201`  
Title: Standard-library replay of the aligned dyadic source, digital forcing, inverse positivity, and finite Euler transform  
Status: **EXACT FINITE ALGEBRA; NO RH VERDICT**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08

The verifier in `experiments/X-26201-boundary-bspline/` uses only Python
integers, `fractions.Fraction`, and an exact quadratic-field implementation for
`Q(sqrt(2))`.

Retained result:

```text
verdict                              EXACT_BOUNDARY_BSPLINE_ALGEBRA_VERIFIED
Dirichlet convolution rows          256
positive inverse coefficients       33
finite Euler identities             158
unit/adversarial tests               5/5 PASS
proof-object SHA-256
cde8ac0d20702856c6fc0339d33861ec63aa819b237a1facbf4e49ff7353db69
```

The exact rational enclosure proves

\[
\eta(1/2)>1/2
\]

and hence the paired transport mass in `L-26202` is strictly below one.

The experiment does not verify the convolution-analytic source theorem, the
source-specific reflected LMI `L-26203.9`, a cofinal energy recurrence, or RH.
