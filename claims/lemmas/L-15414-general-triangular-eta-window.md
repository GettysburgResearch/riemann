# L-15414 — General triangular pole filters and the Dirichlet-eta specialization

Claim ID: `L-15414`  
Title: Every fixed relative annulus has an RH-complete triangular contrast; the ratio-eight case is the exact parity/eta filter  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: elementary Laplace transforms; `T-15406` for the explicit-formula implication  
Scope: finite pole-free prime windows and positive-route scheduling  
Related counterexample candidates: none

## One-parameter triangular family

Fix any `h>0`, put

\[
 c_h=e^{h/2},
 \qquad
 b_h(u)=h^{-1}\mathbf1_{[0,h]}(u),
 \qquad
 F_h=b_h*b_h,
 \tag{L-15414.1}
\]

and define

\[
 \boxed{
 G_h^{\rm pf}(u)=F_h(u)-c_hF_h(u-h).}
 \tag{L-15414.2}
\]

The window is continuous, piecewise linear, and supported in `[0,3h]`. Its
Laplace transform is

\[
 \boxed{
 \widehat G_{h,L}^{\rm pf}(z)
 =\left({1-e^{-hz}\over hz}\right)^2
  \left(1-e^{-h(z-1/2)}\right).}
 \tag{L-15414.3}
\]

The final factor vanishes at `z=1/2`; hence it cancels the zeta pole after the
shift `s=z+1/2`. Its other zeros lie on `Re z=1/2`, while the box-factor zeros
lie on `Re z=0`. Therefore

\[
 \boxed{
 \widehat G_{h,L}^{\rm pf}(z)\ne0
 \qquad(0<\operatorname{Re}z<1/2).}
 \tag{L-15414.4}
\]

For

\[
 Q_h^{\rm pf}(x)=
 \sum_{n\ge2}{\Lambda(n)\over\sqrt n}
 G_h^{\rm pf}(x-\log n),
 \tag{L-15414.5}
\]

only the exact annulus

\[
 e^{x-3h}\le n\le e^x
 \tag{L-15414.6}
\]

contributes. Thus the support ratio is `e^(3h)`. Subject to the same
explicit-formula/Laplace audit as `T-15406`, **every fixed `h>0`** gives

\[
 \boxed{
 \mathrm{RH}
 \iff Q_h^{\rm pf}\text{ is bounded on a right half-line}
 \iff Q_h^{\rm pf}\text{ has bounded Cesaro mean square}.}
 \tag{L-15414.7}
\]

This means the relative annulus can be chosen arbitrarily thin in advance. The
constant in the required cancellation worsens as `h` shrinks; no uniform
`h->0` conclusion is asserted.

## Exact four-hinge formula

Let

\[
 K(x)=\sum_{\log n\le x}{\Lambda(n)\over\sqrt n}(x-\log n).
 \tag{L-15414.8}
\]

The exact coefficient vector is

\[
 d_h=(1,-2-c_h,1+2c_h,-c_h),
 \tag{L-15414.9}
\]

and

\[
 \boxed{
 Q_h^{\rm pf}(x)
 ={1\over h^2}
 \sum_{j=0}^3d_{h,j}K(x-jh).}
 \tag{L-15414.10}
\]

Its polynomial factors as

\[
 \sum_{j=0}^3d_{h,j}r^j
 =(1-r)^2(1-c_hr).
 \tag{L-15414.11}
\]

Consequently constants and linear functions are annihilated, and the pole mode
`e^(x/2)` is annihilated because its shift ratio is

\[
 r=e^{-h/2}=c_h^{-1}.
\]

## Exact diagonal energy and optimal finite width

The triangular overlap is

\[
 \|F_h\|_2^2={2\over3h},
 \qquad
 \langle F_h,F_h(\cdot-h)\rangle={1\over6h}.
 \tag{L-15414.12}
\]

Therefore

\[
 \boxed{
 \|G_h^{\rm pf}\|_2^2
 ={2+2e^h-e^{h/2}\over3h}.}
 \tag{L-15414.13}
\]

The diagonal term in a logarithmic mean square has leading coefficient

\[
 D(h)={2+2e^h-e^{h/2}\over6h}.
 \tag{L-15414.14}
\]

It tends to infinity both as `h->0+` and as `h->infinity`. Its derivative has
the sign of

\[
 g(h)=h\left(2e^h-\tfrac12e^{h/2}\right)
      -\left(2+2e^h-e^{h/2}\right).
 \tag{L-15414.15}
\]

Since

\[
 g'(h)=h\left(2e^h-\tfrac14e^{h/2}\right)>0,
\]

there is a unique minimizer. Ordinary high-precision reconnaissance places it
at

```text
h approximately 1.19227846713369,
exp(3h) approximately 35.7602,
D(h) approximately 0.946934951916897.
```

These decimals are scheduling data, not proof inputs. The integer-coefficient
choice `h=log 4` has ratio `64`; the eta choice below has ratio `8`.

## Dirichlet-eta specialization

Take

\[
 h=\log2,
 \qquad c_h=\sqrt2,
 \qquad s=z+\frac12.
 \tag{L-15414.16}
\]

Then

\[
 \boxed{
 1-c_he^{-hz}=1-2^{1-s},}
 \tag{L-15414.17}
\]

which is exactly the factor in

\[
 \eta(s)=(1-2^{1-s})\zeta(s).
 \tag{L-15414.18}
\]

The active prime-power annulus has ratio

\[
 e^{3h}=8.
\]

In the half-plane `Re s>1`, multiplication of the von Mangoldt Dirichlet
series by the eta factor gives

\[
\boxed{
 (1-2^{1-s})\left(-{\zeta'\over\zeta}(s)\right)
 =\sum_{N\ge1}{b_2(N)\over N^s},}
 \tag{L-15414.19}
\]

where

\[
 \boxed{
 b_2(N)=\Lambda(N)-2\mathbf1_{2\mid N}\Lambda(N/2),}
 \tag{L-15414.20}
\]

with `Lambda(1)=0`. Thus the pole-free signal may be generated either by a
shifted triangular window or by a triangular smoothing of one explicit signed
parity-von-Mangoldt stream.

## Exact zeta-distribution covariance

For real `s>1`, let

\[
 \mathbb P_s(N=n)={n^{-s}\over\zeta(s)},
 \qquad
 \epsilon_2(n)=(-1)^{n-1}.
 \tag{L-15414.21}
\]

Then

\[
 \mathbb E_s\epsilon_2(N)=1-2^{1-s},
 \qquad
 \mathbb E_s\log N=-{\zeta'\over\zeta}(s),
 \tag{L-15414.22}
\]

and

\[
 \mathbb E_s[\epsilon_2(N)\log N]
 =-{\eta'(s)\over\zeta(s)}.
 \tag{L-15414.23}
\]

Differentiating an expectation in this exponential family gives

\[
 {d\over ds}\mathbb E_s\epsilon_2(N)
 =-\operatorname{Cov}_s(\epsilon_2(N),\log N).
\]

Hence the covariance is exactly

\[
 \boxed{
 \operatorname{Cov}_s(\epsilon_2(N),\log N)
 =-(\log2)2^{1-s}.}
 \tag{L-15414.24}
\]

Equivalently,

\[
 (1-2^{1-s})\left(-{\zeta'\over\zeta}(s)\right)
 =-{\eta'(s)\over\zeta(s)}
  +(\log2)2^{1-s}.
 \tag{L-15414.25}
\]

This gives a genuine finite-state parity interpretation in the probability
region.

## What the eta alignment does and does not prove

The eta specialization gives:

- the smallest especially simple annulus found so far: ratio `8`;
- an exact parity covariance and signed coefficient stream;
- an independent direct/shifted/eta replay;
- the same zero-free open-strip transform gate as the ratio-64 window.

It does **not** make the critical estimate automatic. Equation (L-15414.25)
still contains `1/zeta(s)` through `eta'(s)/zeta(s)`, so every off-critical zero
remains an uncancelled resonance. The elementary bound `|epsilon_2|<=1` is
available only for the real probability law `s>1`; analytically continuing that
contraction to the critical boundary is already RH-strength.

## Gap audit

- The RH equivalence inherits the explicit-formula and half-line Laplace audit
  of `T-15406`.
- The coefficient `sqrt(2)` is algebraic, not rational; an exact producer may
  use the quadratic field or keep the two shifted sums separate.
- An annulus ratio of `8` reduces work but does not reduce the logical strength
  of the cofinal bound.
- Probability and independence statements for the zeta distribution are not
  valid after analytic continuation to `Re s<=1`.
- Optimizing the diagonal coefficient is only a scheduler because the signed
  off-diagonal term remains load-bearing.
