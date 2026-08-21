# T-23811 — Weighted shell-tail carry proposal for RH

Claim ID: `T-23811`  
Title: A subpolynomial weighted upper-tail remainder for one fixed-ratio parabolic shell implies the Riemann hypothesis  
Status: **FULL PROPOSED PROOF — `WSTS` IS THE SINGLE NEW RH-BEARING HINGE**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23823`--`L-23826`; PR #248 parabolic seed, signed carry consumer, and proper-prime-power reduction; PR #202 square-screw/Landau transfer  
Supersedes as preferred review target: the abstract source identity `SGQB(K)` of `L-23822`  
Scope: ordinary-prime signed carry transport; RH is not claimed independently verified

## 1. Exact shell residual

For every integer `X>=4`, put

\[
Y=\lfloor X/2\rfloor.
\tag{T-23811.1}
\]

Let

\[
r_X(p)
=v_p(b_X^{(0)})
-p^{-1/2}\log(X/p)
\tag{T-23811.2}
\]

be the ordinary-prime residual of the explicit parabolic seed, and define the
dyadic shell residual

\[
\boxed{
s_X(p)
=r_X(p)-\mathbf1_{p\le Y}r_Y(p).}
\tag{T-23811.3}
\]

Define its weighted upper-tail charge

\[
\boxed{
\mathcal B_X
=
\max_{z}
\left(
\sum_{z\le p\le X}(\log p)s_X(p)
\right)_+,}
\tag{T-23811.4}
\]

where `z` ranges over the finite prime set and the empty tail.

The new arithmetic theorem is:

> **Weighted Shell-Tail Stability (`WSTS`).** For every `epsilon>0`,
> \[
> \boxed{
> \mathcal B_X\le C_\varepsilon X^\varepsilon
> \qquad(X\ge4).}
> \tag{T-23811.5}
> \]

This is one explicit finite maximum. It contains no packet dimension, source
rank, Schur reserve, Green norm, contact count, or optimization over arbitrary
vectors.

## 2. Exact continuum theorem beneath `WSTS`

Let `E_(1/2)` be the dyadic parabolic shell defect and

\[
H_{1/2}(\theta)=\int_\theta^1E_{1/2}(u)du.
\]

`L-23823` proves unconditionally

\[
\boxed{H_{1/2}(\theta)\le0,}
\tag{T-23811.6}
\]

with the quantitative moat

\[
\boxed{
H_{1/2}(\theta)
\le-\frac{\log2}{5}\sqrt\theta
\qquad(0<\theta\le1/4).}
\tag{T-23811.7}
\]

Thus the complete continuum shell already transports positive defect into
larger-scale slack. `WSTS` is only the finite prime-sampling stability of this
proved order.

`L-23825` makes this exact:

\[
\sum_{z\le p\le X}(\log p)s_X(p)
=
\sqrt X H_{1/2}(z/X)
+\mathcal E_X(z)
+O((1+\log X)^2),
\tag{T-23811.8}
\]

where

\[
\mathcal E_X(z)
=X^{-1/2}\int_{[z,X]}
E_{1/2}(t/X)d[\vartheta(t)-t]
\tag{T-23811.9}
\]

is one source-specific Chebyshev sampling remainder. The carry-floor error has
already been bounded absolutely.

Consequently a proof may establish `WSTS` by proving only

\[
\boxed{
\sup_z(\mathcal E_X(z))_+=X^{o(1)}.}
\tag{T-23811.10}
\]

The negative continuum main term must remain present; replacing it by absolute
values is invalid.

## 3. Exact finite correction of one shell

`L-23824` proves that if all logarithmically weighted upper tails of a prime
residual are nonpositive, then the positive residual can be transported into
larger-prime slack at exactly zero objective cost.

For a general shell, `L-23826` first pays the single charge `mathcal B_X` at the
largest existing prime and then applies this zero-cost weighted transport. It
produces a signed shell carry vector `c_X^[shell]` satisfying every ordinary-
prime shell constraint and

\[
\boxed{
J_{\mathbb P}(c_X^{[\mathrm{shell}]})
\ge
J_{\mathbb P}(b_X^{(0)}-b_Y^{(0)})
-\mathcal B_X.}
\tag{T-23811.11}
\]

The correction stays inside the original endpoint and alters no third prime or
proper prime-power row.

## 4. Dyadic shell assembly

Iterate

\[
X_0=X,
\qquad
X_{j+1}=\max(2,\lfloor X_j/2\rfloor).
\tag{T-23811.12}
\]

The seed and target shell differences telescope. Summing the exact shell
certificates gives one signed ordinary-prime carry certificate at endpoint `X`
with objective

\[
\begin{aligned}
J_{\mathbb P}(c_X)
&\ge
J_{\mathbb P,X}(b_X^{(0)})
-\sum_j\mathcal B_{X_j}
-O(1).
\end{aligned}
\tag{T-23811.13}
\]

Under `WSTS`, for every `epsilon>0`,

\[
\sum_j\mathcal B_{X_j}
\ll_\varepsilon X^\varepsilon.
\tag{T-23811.14}
\]

The parabolic seed satisfies

\[
J_{\mathbb P,X}(b_X^{(0)})
\ge4\sqrt X-O(\log^2X).
\tag{T-23811.15}
\]

Since signed carry coordinates suffice by PR #248 `L-24508`, the ordinary-prime
ramp obeys

\[
\boxed{
P_X
\ge4\sqrt X-O_\varepsilon(X^\varepsilon).}
\tag{T-23811.16}
\]

Proper prime powers cost `O(log^2X)`, so the same estimate holds for the complete
von-Mangoldt ramp.

## 5. Zero exclusion

At square endpoints `X=N^2`, the exact zeta screw identity gives

\[
\Psi(2\log N)
=4(N+N^{-1}-2)-\mathcal P(N^2)+O(\log N).
\tag{T-23811.17}
\]

Equation (T-23811.16) implies

\[
\Psi(2\log N)\le N^{o(1)}.
\tag{T-23811.18}
\]

The reviewed square-sampling/Landau theorem then excludes every zeta zero with
real part greater than `1/2`; functional-equation symmetry yields

\[
\boxed{\mathrm{RH}.}
\tag{T-23811.19}
\]

## 6. Why this is stronger than the former proposals

The old two-contact route asserted that the arithmetic source itself had only
two free coordinates. That assertion did not survive the same-sign Möbius cube.
The present route instead proves:

```text
the continuum shell has an exact upper-tail order;
finite weighted tail order has an exact zero-cost carry implementation;
all shell geometry composes by literal telescoping;
only one finite prime-sampling remainder is unproved.
```

There is:

- no source-rank bound;
- no endpoint/face count;
- no reflected positive reserve;
- no nonnegative monotone cover;
- no complete Green-energy theorem;
- no arbitrary-vector BTP estimate;
- no limit in packet order.

The same-sign cube is included automatically because the complete scalar shell
residual is formed before the weighted tail is taken.

## 7. Mandatory review mutations

A proof of `WSTS` must fail closed under:

1. deletion of one prime or prime-square source row;
2. replacement of the weighted tail by an unweighted tail;
3. absolute values before the continuum moat and prime remainder are combined;
4. loss of the first `2/3` Mertens/Farey shell;
5. a changed finite-floor endpoint convention;
6. a boundary charge placed outside the assembled endpoint;
7. promotion of the classical PNT error, by itself, to (T-23811.10).

## 8. Exact status

```text
normalized continuum shell order          PROPOSED COMPLETE
finite floor approximation                 PROPOSED COMPLETE
zero-cost weighted prime transport         PROPOSED COMPLETE
in-support shell assembly                  PROPOSED COMPLETE
WSTS / one-sided Chebyshev remainder       OPEN / RH-BEARING
WSTS -> prime ramp -> RH                   COMPLETE CONDITIONAL CHAIN
Riemann Hypothesis                         NOT CLAIMED PROVED
```
