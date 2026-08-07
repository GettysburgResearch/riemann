# T-15404 — A pole-free single prime-power window is equivalent to RH

Claim ID: `T-15404`  
Title: One fixed two-shift window cancels the zeta pole algebraically and detects every off-critical zero  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15405`, `T-15403`; the smoothed von Mangoldt explicit formula  
Scope: numerically stable one-scalar positive/negative RH criterion  
Related counterexample candidates: none

## Pole-annihilating window

Let `F_*` be the explicit nonnegative smooth window of `L-15405`, supported in
`[2,4]`, and put

\[
 h=\log4.
 \tag{T-15404.1}
\]

Define the real signed window

\[
\boxed{
 G_*(u)=F_*(u)-2F_*(u-h).}
 \tag{T-15404.2}
\]

It is smooth and compactly supported in

\[
 [2,4+h].
 \tag{T-15404.3}
\]

Its Laplace transform is

\[
\boxed{
 \widehat G_{*,L}(z)
 =\widehat F_{*,L}(z)
  \left(1-2e^{-hz}\right)
 =\widehat F_{*,L}(z)
  \left(1-2\,4^{-z}\right).}
 \tag{T-15404.4}
\]

At the shifted zeta pole,

\[
 \widehat G_{*,L}(1/2)=0.
 \tag{T-15404.5}
\]

The extra factor vanishes only at

\[
 z={1\over2}-{\pi i k\over\log2},
 \qquad k\in\mathbb Z.
 \tag{T-15404.6}
\]

Every such zero has real part `1/2`. A shifted nontrivial zeta zero has

\[
 z=\rho-1/2,
 \qquad -1/2<\operatorname{Re}z<1/2,
 \tag{T-15404.7}
\]

so (T-15404.6) cannot cancel it. Since `F_*` is zero-free in the open right
half-plane,

\[
\boxed{
 \widehat G_{*,L}(\rho-1/2)\ne0
 \quad\hbox{whenever}\quad
 \operatorname{Re}\rho>1/2.}
 \tag{T-15404.8}
\]

## Raw prime-power statistic

For real `x` sufficiently large, define

\[
\boxed{
 Q_*(x)=
 \sum_{n\ge2}{\Lambda(n)\over\sqrt n}
 G_*(x-\log n).}
 \tag{T-15404.9}
\]

Only the finite annulus

\[
 e^{x-(4+h)}\le n\le e^{x-2}
 \tag{T-15404.10}
\]

contributes.

No continuous pole main term is subtracted in (T-15404.9).

## Main theorem

The following are equivalent.

1. The Riemann Hypothesis is true.
2. The single raw prime-power statistic is bounded:
   \[
    \boxed{
    \sup_{x\ge4+h}|Q_*(x)|<\infty.}
    \tag{T-15404.11}
   \]

### Proof

Let

\[
 d\mathcal P(t)=
 \sum_{n\ge2}{\Lambda(n)\over\sqrt n}
 \delta_{\log n}(dt).
 \tag{T-15404.12}
\]

Its Laplace transform is

\[
 \mathcal L\mathcal P(z)
 =-{\zeta'\over\zeta}\left(z+{1\over2}\right)
 \qquad(\operatorname{Re}z>1/2).
 \tag{T-15404.13}
\]

The function `Q_*` is the convolution `mathcal P*G_*`. Therefore

\[
\boxed{
 \mathcal LQ_*(z)=
 -\widehat G_{*,L}(z)
 {\zeta'\over\zeta}\left(z+{1\over2}\right).}
 \tag{T-15404.14}
\]

The zero (T-15404.5) cancels the pole of zeta at `s=1`. Equation
(T-15404.8) shows that no pole coming from a nontrivial zero in
`Re rho>1/2` is canceled.

If `Q_*` is bounded on the right, its Laplace transform is holomorphic for
`Re z>0`; hence there are no such poles and RH follows by the functional
equation.

Conversely, under RH all nontrivial poles in (T-15404.14) lie on the imaginary
axis. The smooth compact window gives rapid vertical decay, so the corresponding
zero expansion converges absolutely and uniformly in `x`; the trivial-zero
terms decay. Thus `Q_*` is bounded. QED.

## Relation to the pole-subtracted statistic

Let `D_*(a)` be the statistic of `T-15403`. The exact choice `h=log4` gives

\[
\boxed{
 Q_*(x)=D_*(x/2)-2D_*((x-h)/2).}
 \tag{T-15404.15}
\]

Indeed, the two pole terms cancel because

\[
 e^{x/2}-2e^{(x-h)/2}=0.
 \tag{T-15404.16}
\]

Equation (T-15404.15) is an exact producer cross-check. A direct raw-prime
contraction and the two pole-subtracted contractions must overlap.

## Explicit formula and moat

Under RH,

\[
\boxed{
 Q_*(x)=
 -\sum_\rho e^{ix\gamma}
 \widehat G_{*,L}(i\gamma)
 +E_{triv,G}(x),}
 \tag{T-15404.17}
\]

with the symmetric zero convention. Consequently any certified shell-count
majorants `M_k` give the computable bound

\[
\boxed{
 |Q_*(x)|\le
 B_G:=B_{triv,G}+
 \sum_{k\ge0}M_k
 \sup_{k\le|t|\le k+1}
 |\widehat G_{*,L}(it)|.}
 \tag{T-15404.18}
\]

A strict directed violation of this bound is an unconditional RH-disproof
certificate after independent analytic and numerical review.

Certified notches from `L-15406` may be inserted before taking the two-shift
difference, reducing `B_G` while preserving (T-15404.8).

## Numerical advantage

`T-15403` subtracts two quantities of order `exp(x/2)` to recover an order-one
signal. `Q_*` performs that cancellation symbolically at the window level.
Its producer evaluates only one signed finite prime-power sum.

This sharply reduces interval-width pressure and makes the criterion suitable
for very large terminal windows.

## Empirical control

The `10^7` reconnaissance in `O-15401` gives, by both direct raw-prime
contraction and (T-15404.15),

```text
maximum approximately +0.01012916
minimum approximately -0.01008357
```

over the retained support range. Direct and difference-form evaluations agreed
to about `10^-13` at the extrema. These are ordinary floating controls only.

## General pole-annihilating differences

For any integer `q>=2`, set

\[
 h_q=2\log q,
 \qquad
 G_{q}(u)=F_*(u)-qF_*(u-h_q).
 \tag{T-15404.19}
\]

Then

\[
 \widehat G_{q,L}(z)
 =\widehat F_{*,L}(z)(1-q^{1-2z}),
 \tag{T-15404.20}
\]

which again vanishes at `z=1/2`, while all added zeros have real part `1/2`.
Every `q` therefore supplies an equivalent raw prime-window criterion. The
choice `q=2` has the smallest integer coefficient and support increase.

## Gap audit

- The theorem inherits the bounded-convolution/Laplace-transform review target
  of `T-15403`.
- The classical zero-free line `Re s=1` is used to exclude a nontrivial zero at
  the added-factor real part.
- The explicit RH-valid moat must include all zero multiplicities and trivial
  terms.
- The window is signed; midpoint cancellation or omission of prime powers is
  unsafe.
- Boundedness of finitely many values does not prove RH.
- The theorem provides a numerically stable equivalent criterion, not the
  missing boundedness proof.
