# R-99970 — The positive priority-surface flux is power-sized

Claim ID: `R-99970`  
Status: **PROVED ASYMPTOTIC REFUTATION OF `UPBF67`**  
Created: 2026-08-20  
Depends on: `L-99920/L-99921`; the classical prime number theorem and Mertens product theorem  
RH status: **not assumed**

Let `U_X` be the positive upward priority flux in `T-99920`, for any ordering
of the active native labels.  Thus the activities are `a_p=1/p`, with two
labelled copies of `67`, and

\[
 J_{i,A}=\lambda_iw(A),\qquad
 \lambda_i=a_i\prod_{h<i}(1-a_h).
\]

Then there is an absolute constant `c>0` such that

\[
\boxed{
 \mathcal U_X\ge {c\over(\log X)^3}
}
\tag{R-99970.1}
\]

for every sufficiently large real `X`, independently of the label ordering.
Consequently

\[
\boxed{
 \int_2^Y\sqrt X\,\mathcal U_X\,{dX\over X}
 \gg {\sqrt Y\over(\log Y)^3},
}
\tag{R-99970.2}
\]

so `UPBF67`, as stated in `T-99920`, is false.

## Proof

Put

\[
 \mathcal P_X=\{q\text{ prime}:2\sqrt X<q\le3\sqrt X\}.
\]

Every `q in P_X` is an active singleton label.  For distinct `q,r in P_X`,

\[
 qr>4X,
\]

so the pair vertex is inactive and has box potential zero.  Whichever of `q`
and `r` occurs earlier in the chosen priority order, call it `i`; take `A` to
be the singleton containing the later label.  Then `A` is an odd suffix set,
so this edge is one of the terms counted positively by `U_X`.  Its loss is

\[
 \lambda_i{1\over r}\Phi_X(r)
 \ge {s_X\over qr}\Phi_X(r),
\tag{R-99970.3}
\]

where

\[
 s_X=\prod_{\ell\ {m active}}(1-a_\ell)
 =(1-67^{-1})\prod_{p\le X}(1-p^{-1}),
\]

and `s_(i-1)>=s_X` was used.  The normalized box potential is increasing in
its scale argument.  Since

\[
 {X\over r}\ge {\sqrt X\over3}\ge67
\]

for large `X`,

\[
 \Phi_X(r)=\Phi_{67}(X/r)\ge \Phi_{67}(67)=:c_0>0.
\]

Summing (R-99970.3) over unordered pairs gives

\[
 \mathcal U_X
 \ge {c_0s_X\over2}
 \left[
  \left(\sum_{q\in\mathcal P_X}{1\over q}\right)^2
  -\sum_{q\in\mathcal P_X}{1\over q^2}
 \right].
\tag{R-99970.4}
\]

The PNT and partial summation give

\[
 \sum_{2\sqrt X<q\le3\sqrt X}{1\over q}
 \sim {2\log(3/2)\over\log X},
\]

whereas the square sum is `o((log X)^(-2))`.  Mertens' product theorem gives

\[
 s_X\sim {(1-67^{-1})e^{-\gamma}\over\log X}.
\]

This proves (R-99970.1).  Integrating only over `Y/2<=X<=Y` proves
(R-99970.2).

## Interpretation

The lower bound uses pair vertices that are individually harmless for the
signed Euler scalar: their large positive odd-surface loss is cancelled by
unused even surface and survival terms.  Taking absolute upward flux discards
that cancellation.  The failure is therefore structural, not a weak constant
or an improvable prime estimate.
