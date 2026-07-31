# T-15110 — Central logarithmic Stieltjes--Hankel criterion for RH

Claim ID: `T-15110`  
Status: **PROVED EQUIVALENCE THEOREM; ALL-ORDER HANKEL POSITIVITY OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: the Stieltjes moment theorem; the genus-zero Hadamard product for an entire function of order `1/2`  
Scope: eliminate the noncanonical operator realization and state its exact coefficient content directly on `xi`  
Related counterexample candidates: none

## 1. Centered square variable

Normalize

\[
 E(w)=\frac{\xi(1/2+w)}{\xi(1/2)}.
 \tag{T-15110.1}
\]

The functional equation makes `E` even, real entire, and `E(0)=1`. Therefore
there is a unique real entire function `mathcal E` such that

\[
 \boxed{E(w)=\mathcal E(w^2).}
 \tag{T-15110.2}
\]

Since `E` has order one, `mathcal E` has order `1/2`.

Define the meromorphic logarithmic derivative

\[
 \boxed{G(z)=\frac{\mathcal E'(z)}{\mathcal E(z)}.}
 \tag{T-15110.3}
\]

At the origin write

\[
 \boxed{
 G(z)=\sum_{n=0}^{\infty}(-1)^n s_nz^n.}
 \tag{T-15110.4}
\]

Equivalently, if

\[
 \log E(w)=\sum_{m\ge1}c_mw^{2m},
\]

then

\[
 \boxed{s_{m-1}=(-1)^{m-1}m c_m.}
 \tag{T-15110.5}
\]

Thus every `s_n` is an explicit central logarithmic derivative of `xi`.

## 2. RH gives a Stieltjes moment sequence

Assume RH.  The zeros of `E` are `w=+/- i gamma`, with positive ordinates
`gamma` repeated according to multiplicity.  Since `mathcal E` has order below
one and

\[
 \sum_{\gamma>0}\gamma^{-2}<\infty,
\]

its genus-zero product is

\[
 \boxed{
 \mathcal E(z)=
 \prod_{\gamma>0}
 \left(1+\frac z{\gamma^2}\right)^{m_\gamma}.}
 \tag{T-15110.6}
\]

Therefore

\[
 G(z)=
 \sum_{\gamma>0}\frac{m_\gamma}{z+\gamma^2}
 =\int_{[0,R]}\frac{d\nu(x)}{1+xz},
 \tag{T-15110.7}
\]

where

\[
 R=\gamma_1^{-2},
 \qquad
 \nu=\sum_{\gamma>0}
 m_\gamma\gamma^{-2}\delta_{\gamma^{-2}}.
 \tag{T-15110.8}
\]

The measure is finite.  Expanding at zero gives

\[
 \boxed{
 s_n=\int x^n\,d\nu(x)
 =\sum_{\gamma>0}m_\gamma\gamma^{-2n-2}.}
 \tag{T-15110.9}
\]

Hence, for every `r>=1`, the ordinary and shifted Hankel matrices

\[
 H_r=(s_{i+j})_{0\le i,j<r},
 \qquad
 H_r^+=(s_{i+j+1})_{0\le i,j<r}
 \tag{T-15110.10}
\]

are positive semidefinite.  In fact they are positive definite because the
measure has infinite support.

## 3. All Hankel gates imply RH

Assume conversely that

\[
 \boxed{H_r\succeq0,\qquad H_r^+\succeq0
 \quad\text{for every }r.}
 \tag{T-15110.11}
\]

The Stieltjes moment theorem gives a positive measure `nu` on `[0,infinity)`
with moments `s_n`.

The power series (T-15110.4) has positive radius because `G` is meromorphic and
regular at zero.  Hence

\[
 \limsup_{n\to\infty}s_n^{1/n}<\infty.
\]

For a positive representing measure this forces compact support: if positive
mass lay above every finite bound, its moments would have unbounded root
growth. Thus `supp nu subset [0,R]` for some finite `R`.

For `|z|<1/R`, moment expansion gives

\[
 \boxed{
 G(z)=\int_{[0,R]}\frac{d\nu(x)}{1+xz}.}
 \tag{T-15110.12}
\]

The right side is a Stieltjes function and is analytic away from the negative
real half-line.  Equality near zero and analytic continuation imply that the
meromorphic function `G` has no pole off the negative real axis.

Every zero of `mathcal E` produces a pole of `mathcal E'/mathcal E`, with its
positive integer multiplicity as residue. Therefore every zero of `mathcal E`
is negative real.  By (T-15110.2), every zero of `E` is purely imaginary, so
every nontrivial zero of `zeta` lies on the critical line.

Thus RH holds.

## 4. Exact equivalence

Combining the two directions,

\[
 \boxed{
 \mathrm{RH}
 \iff
 H_r\succeq0\text{ and }H_r^+\succeq0
 \text{ for every }r.}
 \tag{T-15110.13}
\]

Equivalently,

\[
 \boxed{
 G(z)=\frac{d}{dz}
 \log\!\left(
  \frac{\xi(1/2+\sqrt z)}{\xi(1/2)}
 \right)
 \text{ is a Stieltjes function}.}
 \tag{T-15110.14}
\]

The square-root notation in (T-15110.14) is single-valued because the centered
function is even.

## 5. Recovery of the determinant model

The meromorphicity of `G` forces the Stieltjes measure in (T-15110.12) to be
purely atomic.  If an atom is at `x` and the corresponding pole has residue
`m`, Stieltjes inversion gives atom weight `mx`.  Therefore the recovered
self-adjoint Hilbert--Schmidt spectrum is

\[
 \lambda=+/-\sqrt x
\]

with multiplicity `m`.  This reconstructs exactly the paired determinant model
of `L-15128` without a Sobolev chart.

Hence the all-order moment match required in `T-15109` is neither an auxiliary
regularity fact nor a finite-window bookkeeping identity. It is precisely the
Hankel hierarchy (T-15110.11), which is equivalent to RH.

## 6. Finite proof interface

At order `r`, a directed certificate needs:

1. balls for the central Taylor coefficients of `log xi` through order `4r`;
2. directed intervals for `s_0,...,s_(2r-1)`;
3. positive-definite interval `LDL^T` certificates for `H_r` and `H_r^+`.

Passing every finite `r` is not a completed proof unless one also supplies a
symbolic theorem covering all orders.  A single failed Hankel gate would
unconditionally disprove RH.

## 7. Relation to known kernel positivity

Strict log-concavity of the Riemann kernel is only a second-order total-
positivity statement.  The complete Hankel hierarchy above is the all-order
condition.  Thus a `TP_2` kernel theorem, however rigorous, does not establish
(T-15110.11).
