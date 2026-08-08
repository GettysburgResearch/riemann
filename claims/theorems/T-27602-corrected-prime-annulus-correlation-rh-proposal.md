# T-27602 — Corrected prime-annulus correlation proposal for RH

Claim ID: `T-27602`  
Title: Exact dyadic factorization and diagonal closure reduce the prime-annulus criterion to one complete signed ratio correlation  
Status: **FULL CONDITIONAL PROPOSAL — SIGNED CORRELATION ESTIMATE OPEN; RH NOT CLAIMED PROVED**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `T-27601`; `L-27605`; `L-27606`; `R-27601`; PR #269 source/factor-five package  
Scope: corrected review spine after the failed Hardy/complete-monotonicity shortcut

## 1. Direct verdict

This branch does not contain an unconditional proof of RH.

The exact finite prime-annulus statistic remains

\[
\mathfrak P(X)
=\frac1{\sqrt X}
\left[
\sum_{X/2<q\le X}\Lambda(q)(2q/X-1)
+
\sum_{X/4<q\le X/2}\Lambda(q)(1/2-4q/X)
\right].
\tag{T-27602.1}
\]

`T-27601` proves the conditional equivalence

\[
\boxed{
\mathrm{RH}
\iff
\mathfrak P(X)=O_\varepsilon(X^\varepsilon)
\iff
\mathfrak E(J)=e^{o(J)},
}
\tag{T-27602.2}
\]

where

\[
\mathfrak E(J)=\int_J^{J+1}|\mathfrak P(e^t)|^2dt.
\]

The final upper bound in (T-27602.2) remains unproved.

## 2. Correct exact factorization

`L-27605` proves

\[
\int_{1/4}^{1}W(u)u^{s-1}du
=
\frac{(s-1)(1-2^{-s})(1-2^{-s-1})}{s(s+1)}.
\tag{T-27602.3}
\]

It also proves the physical identity

\[
W=(I-D_2)(I-\tfrac12D_2)
[(2u-1)\mathbf1_{(0,1]}(u)].
\tag{T-27602.4}
\]

Thus the annulus is a stable two-step dyadic difference of one parabolic prime statistic. The finite filter preserves the rightmost-zero exponent but supplies no upper bound by itself.

## 3. Positivity shortcut withdrawn

`R-27601` records three required corrections:

1. no admissible Hardy square was constructed;
2. the proposed rational factor `3(s-1)/((s+1)(s+2))` is negative on `0<s<1` and is not completely monotone;
3. positivity of an autocorrelation or Weil form gives a lower bound, not the required subexponential upper bound.

No reviewer is being asked to complete one of those missing steps. They are not dependencies of this proposal.

## 4. Diagonal and ratio sign closed

Let

\[
z(u)=e^{-u/2}W(e^{-u}).
\]

`L-27606` proves

\[
\|z\|_2^2=\frac7{16}
\tag{T-27602.5}
\]

and decomposes

\[
\mathfrak E(J)=\mathfrak D(J)+\mathfrak O(J).
\tag{T-27602.6}
\]

The diagonal satisfies

\[
\boxed{
\mathfrak D(J)\ll(1+J)^2.
}
\tag{T-27602.7}
\]

For `q<r`, the block kernel satisfies

\[
\boxed{
K_J(q,r)\le0
\qquad\text{whenever }r\ge2q,
}
\tag{T-27602.8}
\]

and vanishes for `r>=4q`.

Therefore every positive off-diagonal term lies in the near-ratio sector, while the adjacent ratio-two-to-four sector contributes with the opposite sign and must remain in the same ledger.

## 5. Sole corrected arithmetic theorem

Define the complete signed off-diagonal correlation

\[
\boxed{
\mathfrak O(J)
=2\sum_{q<r}
\frac{\Lambda(q)\Lambda(r)}{\sqrt{qr}}
K_J(q,r).
}
\tag{T-27602.9}
\]

The exact remaining theorem is

> **DACB — Dyadic Annulus Correlation Balance.**
> \[
> \boxed{
> |\mathfrak O(J)|=e^{o(J)}.
> }
> \tag{T-27602.10}
> \]

Because the diagonal is polylogarithmic,

\[
\boxed{
\mathrm{DACB}
\iff
\mathfrak E(J)=e^{o(J)}
\iff
\mathrm{RH}.
}
\tag{T-27602.11}

This equivalence does not establish DACB. It identifies the exact signed arithmetic statement that a completed proof must supply.

## 6. Required producer, not reviewer exercise

A future claim of proof must itself emit a complete identity or inequality establishing (T-27602.10). A sufficient source-specific producer would contain:

1. the independent-frequency reflected Selberg matrix for the fixed annulus window;
2. both annulus bands before absolute values;
3. the exact second-commutator term
   \[
   C_\omega=\Lambda_\omega\log+\Lambda_\omega*\Lambda_\omega;
   \]
4. every factor-five carry row and every synthesis cross term;
5. the explicit continuum/discrete boundary of `L-27604`;
6. a strict lower-scale recurrence whose total charge does not exceed the retained reserve;
7. the dyadic and `2/3` fixed-ratio mutations.

Merely stating that such a producer should exist is not a proof. This branch does not claim that it exists yet.

## 7. Conditional conclusion

If DACB is proved, then (T-27602.7) and (T-27602.9) give

\[
\mathfrak E(J)=e^{o(J)}.
\]

The exact Laplace transform from `T-27601` is

\[
-E(s)R(s)\frac{\zeta'}\zeta(s),
\]

and has a nonzero residue at every nontrivial zeta zero. Normal convergence in the half-plane to the right of the critical line excludes every zero there; functional-equation symmetry gives RH.

The implication after DACB is complete. DACB is open.

## 8. Exact status

```text
annulus Mellin/dyadic factorization     PROPOSED COMPLETE
pole-preserving commutator              PROPOSED COMPLETE
diagonal local energy                   PROPOSED COMPLETE
ratio-at-least-two kernel sign          PROPOSED COMPLETE
Hardy/complete-monotonicity shortcut    WITHDRAWN / REFUTED
DACB signed correlation balance         OPEN / RH-BEARING
DACB -> PAE -> RH                       COMPLETE CONDITIONAL
Riemann Hypothesis                      UNPROVED
```
