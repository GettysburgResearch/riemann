# T-102870 — Balanced owner phases remove all fixed-quadruple modulus loss

Claim ID: `T-102870`  
Status: **MAJOR UNCONDITIONAL NORMALIZATION ADVANCE; RH UNPROVED**  
Created: 2026-08-24  
Base: PR #719  
RH status: **unproved**

`T-102860` left a coherent two-modulus sum over four-distinct-owner semiprime
squareclasses. `L-102860--L-102864` sharpen that packet by balancing phase
coordinates across the two physical products.

## 1. Owner/core overlaps are not a direct gate

If an owner prime occurs in the opposite square core, a common copy is
extracted from both products. Translation invariance contributes the factor
`1/ell`, and that incidence cannot recur. Iteration gives a distinct-prime
renewal of total mass

\[
\prod_{\ell\le Y}\left(1+{C\over\ell}\right)
=(\log Y)^{O(1)}.
\]

Thus the direct theorem may be restricted to the clean sector in which no
owner prime occurs in the opposite core.

## 2. One phase from each side

For

\[
N=pq\,a^2,
\qquad
M=rs\,b^2,
\]

choose the phase modulo `r` on the `N` field and the phase modulo `p` on the
`M` field. The phase-cardinality factors cancel the literal weights of the two
selected owners. For fixed core octaves `A,B`,

\[
\boxed{
|\mathcal C_{P,Q}|
\ll
{1\over\sqrt{qs}}
\left(1+{r\over A}\right)^{1/2}
\left(1+{p\over B}\right)^{1/2}.
}
\tag{T-102870.1}

No positive power of either greatest owner remains.

## 3. Four owner phases

Use phases modulo `r,s` on the `N` field and modulo `p,q` on the `M` field.
All four zero frequencies are absent. Product-modulus orthogonality and Cauchy
give

\[
\boxed{
|\mathcal C_{P,Q}|
\ll
\left(1+{rs\over A}\right)^{1/2}
\left(1+{pq\over B}\right)^{1/2}.
}
\tag{T-102870.2}

Hence in the doubly long regime

\[
A\ge rs,
\qquad
B\ge pq,
\]

one has the completely modulus-free estimate

\[
\boxed{|\mathcal C_{P,Q}|\ll1.}
\tag{T-102870.3}

This is the first fixed-quadruple estimate in the programme with no explicit
loss in any of the four owner primes.

## 4. Exact remaining theorem

The only operation not controlled by the fixed-pair analysis is coherent
summation over different clean owner quadruples and core octaves. Define

```text
BQSP102870:
  after exact carrier, source-region, gauge, shared-owner and owner/core-overlap
  renewals, the coherent balanced nonzero-phase sum over clean four-owner
  semiprime squareclasses has subpower logarithmic negative mass in the fixed
  ratio-eight outer observation.
```

The theorem includes the explicit long/short factors in (T-102870.1)--
(T-102870.2); they may be optimized dyadically before the coherent sum.

Then

\[
\boxed{
\mathrm{BQSP}_{102870}
\Longrightarrow
\mathrm{2QDSP}_{102860}
\Longrightarrow
\mathrm{DPWNC}_{102749}
\Longrightarrow
\mathrm{OER}_{102780}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-102870.4}

`R-102840` proves that fixed-quadruple normalization alone does not control the
coherent identity-point sum. The remaining theorem is arithmetic, not another
source or matrix interface.

## Exact boundary

```text
common-factor owner/core renewal          PROVED POLYLOG
balanced cross-side phase identity        PROVED EXACT
two-owner phase/weight cancellation       PROVED EXACT
four-owner phase/weight cancellation      PROVED EXACT
fixed-quadruple long-core bound            PROVED MODULUS-FREE
coherent squareclass summation             OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVED
```