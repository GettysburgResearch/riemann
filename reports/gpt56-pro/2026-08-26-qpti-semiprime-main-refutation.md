# QPTI continuation: semiprime-main refutation

Date: 2026-08-26  
PR: #719  
Starting head: `25857c1704948bffa85234e2a386cfc98dd6a5e5`  
Cross-checks: current main `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f`; PR #730 `b3114562acbeb8c5890ef7a5fc59eed8db71d29a`; PR #756 `6e4609dfe1b073f1eb58445fdd1d7164dbc450d6`  
RH status: **unproved**

## Executive disposition

The request to prove `QPTI103112` cannot be completed as stated because the
literal gate is false.  The previous Euler–Beta pass had already exposed a
nonzero fixed-core owner polynomial.  Summing the core layers does not cancel
that mode: the complete live-core coefficient is strictly positive, while the
bounded detector has a strictly negative semiprime moment.

Consequently

\[
 H_{\rm EB}(X)
 =-C_0\sqrt X\frac{\log\log X}{\log X}(1+o(1)),
 \qquad C_0>0.
\]

The dyadic negative mass is `Y^(1/2+o(1))`.  `EBD103120` and the literal
completed-source `QPTI103112` are refuted.

## The missed mode

The live source of `L-103120` is

\[
 \sum_{\omega(c)\ge2}
 \frac{\mu(c)}{\binom{\omega(c)+2}{2}c}
 \sum_{p<q,(pq,c)=1}
 \frac1{\sqrt{pq}}K_L(X/(pqc^2)).
\]

Its core coefficient after semiprime scaling is

\[
 D_{\ge2}
 =\sum_{\omega(c)\ge2}
 \frac{\mu(c)}{\binom{\omega(c)+2}{2}c^2}>0.
\]

The positivity is exact:

\[
 D_{\ge2}
 =2\int_0^1(1-\theta)
 \left[
  \prod_p(1-\theta/p^2)-1+\theta\sum_p p^{-2}
 \right]d\theta,
\]

and the bracket is nonnegative by
`prod(1-a_p)>=1-sum a_p`, strictly positive away from `theta=0`.

The corrected bounded detector gives

\[
 \widehat K_L(1/2)=-(2-\sqrt2)^2\log2<0.
\]

Landau's squarefree-semiprime asymptotic and compact partial summation then
supply the displayed negative main.

## Why the previous replay passed

`X-103120` checked finite Boolean algebra, canonical Beta shares, and one
nonzero two-prime-core owner mode.  Those checks were correct.  They did not
measure the global semiprime density.  In fact, the new finite regression at
`X=1,000,000` gives

```text
literal current:              -0.459523240793834
normalized by
sqrt(X) loglog(X)/log(X):     -0.002417765151083594
predicted limiting constant:  about -0.0024415
```

The close agreement is a hostile regression check, not the proof of the
asymptotic.

## Structural correction

The completed two-owner/squared-core field is stronger than the native
Möbius wavelet and carries a deterministic semiprime main.  Relative
polylogarithmic squared-core operator bounds cannot turn that field into an
absolute subpower error unless the unsquared owner base has already been
controlled.

Therefore the completed-source equivalence

```text
QPTI103112 <=> BCI102990 <=> HMO102940
```

is withdrawn.  `BCI102990` and `HMO102940` are not declared false; their
source-faithful status must be reconstructed without this promotion.

The non-refuted front door returns to the integrated ordinary-Möbius ratio-eight
wavelet and its same-`K1` largest-prime/Vaughan translation.  Its critical
signed cross-core estimate remains open.  RH remains unproved.
