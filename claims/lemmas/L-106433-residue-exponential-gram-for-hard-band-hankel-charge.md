# L-106433 — Residue–exponential Gram for hard-band Hankel charge

Claim ID: `L-106433`  
Status: **PROVED EXACT FOR FINITE RATIONAL SYMBOLS; CONFLUENT EXTENSION INCLUDED**  
Created: 2026-08-25  
Depends on: `L-106432`  
RH status: **not assumed**

This lemma turns the corrected visible and complement terms into explicit
finite Cauchy/exponential matrices at the actual poles of the all-pass
quotient.

## 1. Simple upper-half-plane poles

Let `U` be a rational boundary symbol with no real pole and a finite limit at
infinity.  Suppose its upper-half-plane poles are

\[
b_j=a_j+i y_j,
\qquad y_j>0,
\qquad 1\le j\le m,
\]

and are simple.  With the Fourier normalization fixed in `L-106432`, write the
negative-frequency transform as

\[
\boxed{
\widehat U(-\xi)=\sum_{j=1}^m c_j e^{i b_j\xi},
\qquad \xi>0,
}
\tag{L-106433.1}
\]

where each `c_j` is the corresponding normalized residue coefficient.  Put

\[
\alpha_{jk}
 =y_j+y_k-i(a_j-a_k),
\qquad
\Re\alpha_{jk}>0.
\]

Then `L-106432.4` and elementary integration give

\[
\boxed{
V_H^-(U)
 =\sum_{j,k=1}^m
 c_j\overline{c_k}
 {1-e^{-H\alpha_{jk}}\over\alpha_{jk}^2}.
}
\tag{L-106433.2}
\]

Indeed,

\[
\int_0^\infty\min(H,\xi)e^{-\alpha\xi}d\xi
 ={1-e^{-H\alpha}\over\alpha^2}.
\]

The unobserved negative charge is

\[
\boxed{
C_H^-(U)
 =\sum_{j,k=1}^m
 c_j\overline{c_k}
 {e^{-H\alpha_{jk}}\over\alpha_{jk}^2}.
}
\tag{L-106433.3}
\]

The two matrices in (L-106433.2)--(L-106433.3) are positive semidefinite,
as is immediate from their integral representations, and their sum is the
full negative Hankel Gram

\[
\sum_{j,k}{c_j\overline{c_k}\over\alpha_{jk}^2}.
\]

## 2. Favorable lower-half-plane channel and signed tail

Applying the same construction to `bar U` gives coefficients `d_l` and lower
pole parameters `gamma_{lq}` for the positive-frequency energy.  Hence

\[
\boxed{
\Delta_H(U)
 =c^*E_H^-c-d^*E_H^+d,
}
\tag{L-106433.4}
\]

where

\[
(E_H^-)_{jk}={e^{-H\alpha_{jk}}\over\alpha_{jk}^2},
\qquad
(E_H^+)_{lq}={e^{-H\gamma_{lq}}\over\gamma_{lq}^2}.
\]

Thus the corrected ninety-percent tail is a difference of two explicit
positive exponential Cauchy Grams.  Pole and zero deficits are not estimated
separately unless a proof deliberately discards their cancellation.

## 3. Confluent poles

If `b_j` has order `r_j`, its negative-frequency contribution is

\[
e^{i b_j\xi}
\sum_{q=0}^{r_j-1}c_{j,q}\xi^q.
\]

Every visible or complement entry is obtained by differentiating the simple
kernel with respect to `alpha`:

\[
\boxed{
\int_0^\infty
 \min(H,\xi)\xi^n e^{-\alpha\xi}d\xi
 =(-\partial_\alpha)^n
 {1-e^{-H\alpha}\over\alpha^2},
}
\tag{L-106433.5}
\]

\[
\boxed{
\int_H^\infty
 (\xi-H)\xi^n e^{-\alpha\xi}d\xi
 =(-\partial_\alpha)^n
 {e^{-H\alpha}\over\alpha^2}.
}
\tag{L-106433.6}
\]

This is the exact confluent ledger; no separation denominator is hidden.

## 4. Consequence for the Xi endpoint programme

For each regular finite Xi window, the endpoint quotient of `L-106400` is
rational after canonical-product truncation.  Its visible negative charge and
signed complement are therefore finite matrices of the form above, with poles
at the reduced upper companion zeros and coefficients given by their literal
residues.

The formerly asserted source cost `<1/600` can be recovered only by proving a
bound for (L-106433.2) for those actual Xi pole/residue data, or by proving an
equivalent physical-transfer theorem.  The remaining problem is now an
explicit shallow-pole residue Gram estimate rather than an unspecified source
normalization.
