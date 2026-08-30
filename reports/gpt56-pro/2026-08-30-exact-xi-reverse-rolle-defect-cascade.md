# Exact reverse–Rolle descent for Xi derivatives

Date: 2026-08-30  
Programme: PR #714  
Status: **first programme target completed; RH unproved**

## Main result

For a real analytic function, count real zeros with multiplicity. At each derivative zero not shared with the parent, retain both:

```text
the multiplicity r of the derivative zero;
the topological orientation iota of the logarithmic derivative f'/f.
```

The local defect is `r+iota`. A simple ordinary Rolle extremum costs zero; a simple wrong-sign extremum costs two; every stationary or higher-order degeneracy is charged automatically.

The exact interval identity is

\[
N_I(f)=N_I(f')-\mathfrak R_I(f)+\varepsilon_I(f).
\]

For the Xi derivative ladder,

\[
N_0(I)=N_m(I)-\sum_{k<m}\mathfrak R_k(I)+\sum_{k<m}\varepsilon_k(I).
\]

In the Morse case,

\[
\mathfrak R_k(I)=2E_k(I),
\]

where `E_k` counts the derivative zeros at which the Laguerre defect is negative.

This completes the exact real-variable theorem requested by the programme and corrects the formerly unspecified coefficient on extra extrema.

## Complex source of the defect

The normalized Laguerre curvature is

\[
Q_f=-(f'/f)'=\sum_\rho(x-\rho)^{-2}.
\]

Real zeros contribute positively. One nonreal conjugate pair `a+-ib` contributes

\[
{2((x-a)^2-b^2)\over((x-a)^2+b^2)^2}
\]

and has exact negative mass `2/b`. Thus negative Laguerre curvature is sourced only by nonreal zero pairs.

## What remains

The descent identity is exact but not self-closing. A proof of RH would still need:

1. an Xi-specific theorem turning the nonreal-pair curvature budget into a bound on the discrete defects `R_k`—shallow negative wells are the principal danger;
2. growing-order control of the high derivative, uniform in height;
3. a summable boundary and multiplicity ledger down to `Xi`.

The immediate target is now sharply stated:

```text
XICURV107110:
  lower-bound the depth/separation of every Xi extra-extremum well strongly
  enough that L-107101 converts off-line zero-pair budget into a summable
  reverse-Rolle defect.
```

The verified actual-Xi Pick/Loewner order-three matrices are plausible finite curvature inputs, but no extrapolation to all derivative orders is made here.

## Scientific boundary

```text
exact real reverse-Rolle identity       PROVED
multiplicity and boundary ledger        PROVED
Laguerre/nonreal-pair dictionary         PROVED
Xi complex defect transport             OPEN
uniform growing-order concentration      OPEN
Riemann Hypothesis                        UNPROVEN
```
