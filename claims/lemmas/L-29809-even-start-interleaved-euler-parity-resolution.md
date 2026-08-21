# L-29809 — Even-start interleaved Euler parity resolution

Claim ID: `L-29809`  
Title: The true shifted-even/unshifted-odd alternating tail has an exact two-mode Laplace decomposition; from an even start every finite Euler jet and the exact remainder are positive Hausdorff sources  
Status: **PROPOSED COMPLETE EXACT SCALAR SOURCE LEMMA — VECTOR/PASCAL BINDING NOT CLAIMED**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: elementary Laplace transform and Euler transformation  
Scope: corrected scalar compression replacing the invalid pair-first step refuted in `R-29803`

## 1. The true interleaved source

Fix integers

\[
 q\ge1,
 \qquad K\ge1,
\]

and a real exponent `s>0`. Define the interleaved sequence

\[
 a_{2k}=(2kq-1)^{-s},
 \qquad
 a_{2k+1}=((2k+1)q)^{-s}.
\tag{L-29809.1}
\]

The common cutoff tail beginning on the shifted-even leg is exactly

\[
 \boxed{
 \mathscr T_K
 =\sum_{r\ge0}(-1)^r a_{2K+r}
 =\sum_{k\ge K}
 \left[(2kq-1)^{-s}-((2k+1)q)^{-s}\right].}
\tag{L-29809.2}
\]

Unlike the invalid pair-first use in `R-29803`, Euler transformation below is
applied to this actual interleaved alternating sequence.

## 2. Exact two-mode Laplace decomposition

For `t>0` put

\[
 z=e^{-qt},
 \qquad
 \alpha(t)={e^t+1\over2},
 \qquad
 \beta(t)={e^t-1\over2}.
\tag{L-29809.3}
\]

Then, for every integer `n>=2`,

\[
 \boxed{
 e^{-x_nt}
 =\alpha(t)z^n+\beta(t)(-z)^n,}
\tag{L-29809.4}
\]

where

\[
 x_{2k}=2kq-1,
 \qquad
 x_{2k+1}=(2k+1)q.
\]

Indeed the right side is `e^t z^(2k)` at even `n=2k` and `z^(2k+1)` at odd
`n=2k+1`.

Using

\[
 x^{-s}={1\over\Gamma(s)}\int_0^\infty t^{s-1}e^{-xt}dt,
\]

we obtain

\[
 \boxed{
 a_n={1\over\Gamma(s)}\int_0^\infty
 t^{s-1}\left[\alpha z^n+\beta(-z)^n\right]dt.}
\tag{L-29809.5}
\]

The two terms are the smooth mode `z^n` and the parity mode `(-z)^n`.

## 3. Exact finite differences

Use the forward-decrease difference

\[
 \Delta a_n=a_n-a_{n+1}.
\]

Since `Delta(lambda^n)=(1-lambda)lambda^n`, equation (L-29809.5) gives for
every `m>=0`

\[
\boxed{
\Delta^m a_n={1\over\Gamma(s)}\int_0^\infty t^{s-1}
 \left[
  \alpha z^n(1-z)^m
  +\beta(-z)^n(1+z)^m
 \right]dt.}
\tag{L-29809.6}
\]

At an even starting index `n=2K`, every factor is nonnegative. Therefore

\[
 \boxed{\Delta^m a_{2K}>0\qquad(m\ge0).}
\tag{L-29809.7}
\]

As a function of `K`, every jet is a Hausdorff moment sequence in the variable
`y=z^2` and is decreasing.

At an odd starting index the parity term changes sign. The exact control

\[
 {1\over6}-{2\over7}+{1\over10}=-{2\over105}
\]

from `R-29803` is therefore consistent with (L-29809.6). Odd-start jets are not
claimed positive; the only odd-start cutoff mismatch remains in the explicit
collar.

## 4. Exact Euler remainder from an even start

Define

\[
 \mathcal R_{K,m}
 =\sum_{r\ge0}(-1)^r\Delta^m a_{2K+r}.
\tag{L-29809.8}
\]

Substitution of (L-29809.6) and summation of the two geometric series yield

\[
\boxed{
\begin{aligned}
\mathcal R_{K,m}
={1\over\Gamma(s)}\int_0^\infty t^{s-1}z^{2K}
\Bigg[
 &{\alpha(1-z)^m\over1+z}\\
 &+{\beta(1+z)^m\over1-z}
\Bigg]dt.
\end{aligned}}
\tag{L-29809.9}
\]

Both summands are nonnegative. Hence

\[
 \boxed{\mathcal R_{K,m}>0.}
\tag{L-29809.10}
\]

It is again a decreasing Hausdorff moment sequence in `K`.

The second term in (L-29809.9) is the parity mode. It explains exactly why the
pair-first ordinary tail has a `1/(1-y)` singularity and why the apparent
`2^-m` damping is not uniform on that mode.

## 5. Correct finite Euler identity

For every integer `M>=1`, the ordinary Euler identity applied to the true
interleaved sequence gives

\[
\boxed{
\mathscr T_K
 =\sum_{m=0}^{M-1}2^{-m-1}\Delta^m a_{2K}
 +2^{-M}\mathcal R_{K,M}.}
\tag{L-29809.11}
\]

Every scalar source coefficient on the right is nonnegative and decreases with
`K`. Equation (L-29809.11), not the pair-first alternating formula refuted in
`R-29803`, is the correct positive scalar Euler compression of the common tail.

If the first omitted term is odd, remove that single signed term into the
collar. The remaining common tail starts at the next shifted-even index and is
covered by (L-29809.11).

## 6. Stability under positive superposition

Equations (L-29809.6)--(L-29809.11) are preserved under nonnegative
superposition over:

- stopped endpoints;
- exponents;
- Taylor orders;
- Peano parameters;
- common arithmetic destinations.

Thus the scalar coefficient bank emitted after exact common-destination
recombination is positive and decreasing, provided the common interleaved tail
starts on its shifted-even leg and the zero-or-one odd mismatch is retained in
the collar.

## 7. Scope firewall

This lemma is an equality of scalar source coefficients for each declared
common arithmetic destination. It does **not** prove that the vector-valued
source

\[
 \sum_r(-1)^r a_{2K+r}e_{2K+r}
\]

may be replaced by a single scalar atom without changing carry columns.

A completed DCD proof must still emit the actual node/source labels of every
finite jet and remainder and prove that their balanced Pascal realization:

1. reproduces the PR #272 odd-commutator channel exactly;
2. has polylogarithmic negative capacity debt;
3. retains the unmatched odd collar and bottom charge.

Scalar positivity alone is not that source-to-flow congruence.

## 8. Exact disposition

```text
pair-first Euler formula of L-29808.6-.7          REFUTED by R-29803
true even-start interleaved Euler identity         PROVED HERE
scalar positivity of common-tail jets/remainder    PROVED HERE
odd-start scalar positivity                        FALSE / collar required
vector-valued Pascal/source binding                 OPEN
DCD and RH                                          UNPROVED
```
