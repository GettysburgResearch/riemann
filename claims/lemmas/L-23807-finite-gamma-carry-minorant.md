# L-23807 — Finite Gamma–carry minorants suffice

Claim ID: `L-23807`  
Title: A cofinal finite-horizon positive convolution minorant gives the sharp carry packing without a global factorization  
Status: **PROPOSED EXACT CONDITIONAL THEOREM — DEFINES THE WEAKEST LOAD-BEARING HINGE**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `L-23801`, `L-23804`  
Scope: finite positive-minorant route suggested by the repository review

## 1. Finite-horizon certificate

Let

\[
 \kappa(t)=e^{-t/2}K(e^t),
 \qquad t\ge0.
 \tag{L-23807.1}
\]

For an integer `X>=3`, put

\[
 T_X=\log(X/2).
 \tag{L-23807.2}
\]

A **finite Gamma–carry minorant** at level `X` is a nonnegative integrable
function

\[
 b_X:[0,T_X]\to[0,\infty)
\]

such that, with

\[
 c_X(t)=8e^{t/2}b_X(t),
 \tag{L-23807.3}
\]

one has the complete convolution inequality

\[
 \boxed{
 (c_X*\kappa)(t)\le t
 \qquad(0\le t\le T_X),}
 \tag{L-23807.4}
\]

and the two sharp mass budgets

\[
 \boxed{
 1-\int_0^{T_X}b_X(t)dt
 \le X^{-1/2+\varepsilon_X},}
 \tag{L-23807.5}
\]

\[
 \boxed{
 {1\over X}\int_0^{T_X}e^tb_X(t)dt
 \le X^{-1/2+\varepsilon_X},}
 \tag{L-23807.6}
\]

where

\[
 \varepsilon_X\longrightarrow0.
 \tag{L-23807.7}
\]

Call the assertion that such certificates exist for every sufficiently large
`X` the **finite Gamma–carry minorant theorem**, abbreviated `FGCM`.

Unlike global GCF, `FGCM` makes no assertion outside the finite horizon relevant
to the endpoint `X` and does not require one positive convolution factor on the
whole half-line.

## 2. Exact finite packing

Assume a certificate `b_X`. Define

\[
 \boxed{
 d_X(n)=8\sqrt X\int_n^{n+1}
 y^{-2}b_X(\log(X/y))dy,}
 \tag{L-23807.8}
\]

for `2<=n<X`, with `d_X(X)=0`.

The same endpoint argument as in `L-23806` gives

\[
 \boxed{
 d_X(n)\ge0,
 \qquad
 \sum_{n=q}^Xd_X(n)\beta_{nq}
 \le q^{-1/2}\log(X/q).}
 \tag{L-23807.9}
\]

Indeed, `q>=2` implies `log(X/q)<=T_X`, so the complete column is covered by
(L-23807.4).

## 3. Sharp entropy mass

The row main term satisfies

\[
 \begin{aligned}
 {1\over2}\sum_{n=2}^{X-1}n d_X(n)
 \ge4\sqrt X\left[
 \int_0^{T_X}b_X(t)dt
 -{1\over X}\int_0^{T_X}e^tb_X(t)dt
 \right].
 \end{aligned}
 \tag{L-23807.10}
\]

Equations (L-23807.5)--(L-23807.7) therefore give

\[
 \boxed{
 {1\over2}\sum_n n d_X(n)
 \ge4\sqrt X-X^{o(1)}.}
 \tag{L-23807.11}
\]

Moreover

\[
 \sum_nd_X(n)
 \le {8\over\sqrt X}
 \int_0^{T_X}e^tb_X(t)dt
 =X^{o(1)}.
 \tag{L-23807.12}
\]

Using

\[
 G_n\ge n/2-C\log(n+1)
\]

from `L-23801`,

\[
 \boxed{
 \sum_nd_X(n)G_n
 \ge4\sqrt X-X^{o(1)}.}
 \tag{L-23807.13}
\]

Thus `FGCM` gives exactly the prime-ramp estimate required by `T-23801`.

## 4. Global GCF is a canonical sufficient certificate

If the global density `a` of `L-23805` is nonnegative and has the subcritical
exponential moments needed in `L-23806`, then

\[
 b_X(t)=a(t)\mathbf 1_{[0,T_X]}(t)
 \tag{L-23807.14}
\]

satisfies `FGCM`.

However, the converse is not required. A finite certificate may:

- depend on `X`;
- leave the exact deconvolution slack;
- combine neighboring quotient layers before taking a sign;
- be piecewise polynomial or atomic after a directed smoothing;
- arise from a finite reflected-Selberg or BTP proof object.

This is the precise positive-minorant weakening requested by the repository
review.

## 5. Finite LP interpretation

Discretize `[0,T_X]` into rational cells and represent `b_X` by nonnegative cell
masses. Since `K` is piecewise rational in `e^t`, (L-23807.4) becomes a finite
family of directed linear inequalities after retaining every carry-reset knot.
The objectives in (L-23807.5)--(L-23807.6) are linear.

Thus `FGCM` admits fail-closed finite proof objects:

```text
nonnegative rational cell masses
complete reset-knot manifest
outward convolution intervals
mass deficit
exponential first moment
strict X^o(1) rate ledger.
```

Finite successful levels remain finite evidence. A proof requires a symbolic
cofinal construction or recurrence.

## 6. Relationship to balanced Type II

The exact global deconvolution contains `1/zeta(s+1)`. A finite minorant may be
proved instead by grouping the quotient layers in the same signed packets used
by BTP. The difference is that `FGCM` asks only for one scalar positive packing
and permits slack; it does not require pointwise positivity of the exact Möbius
inverse or a norm bound for every packet coordinate.

## 7. Proof boundary

Closed exactly:

- `FGCM` implies a finite nonnegative carry packing;
- its two mass budgets imply the sharp entropy and prime-ramp lower bound;
- global GCF is a sufficient but not necessary route to `FGCM`.

Open and load bearing:

- construction of cofinal `FGCM` certificates.
