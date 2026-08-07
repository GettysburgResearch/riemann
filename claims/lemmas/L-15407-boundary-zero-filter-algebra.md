# L-15407 — Boundary-zero filter algebra for safe terminal-prime witness design

Claim ID: `L-15407`  
Title: Products of line-notch and pole-annihilation factors remain zero-free throughout the counterexample strip  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15405`, `L-15406`, `T-15404`; elementary Laplace-transform algebra  
Scope: complete safe design class for one-window prime criteria  
Related counterexample candidates: none

## Counterexample strip

Write

\[
 z=s-\frac12.
 \tag{L-15407.1}
\]

A nontrivial zeta zero with real part to the right of the critical line lies in

\[
\boxed{0<\operatorname{Re}z<\frac12.}
 \tag{L-15407.2}
\]

A terminal-prime filter is **safe** if its Laplace transform has no zero in this
open strip. Such a filter cannot accidentally cancel a hypothetical
right-half-plane zero.

## Line-notch factors

For `r>0`, put

\[
 B_r(z)={1-e^{-rz}\over rz},
 \tag{L-15407.3}
\]

with the removable value at zero. Its zeros are

\[
 z={2\pi i k\over r},
 \qquad k\in\mathbb Z\setminus\{0\},
 \tag{L-15407.4}
\]

and therefore lie on

\[
 \operatorname{Re}z=0.
\]

In the physical variable, multiplication by `B_r` is convolution with the
normalized interval density `r^-1 1_[0,r]`. It preserves nonnegative profiles.

## Pole-annihilation factors

For an integer `q>=2`, define

\[
 P_q(z)=1-q^{1-2z}.
 \tag{L-15407.5}
\]

Its zeros are

\[
 z={1\over2}-{\pi i k\over\log q},
 \qquad k\in\mathbb Z,
 \tag{L-15407.6}
\]

and therefore lie on

\[
 \operatorname{Re}z=\frac12.
\]

In the physical variable, multiplication by `P_q` is the finite signed shift

\[
 F(u)\longmapsto
 F(u)-qF(u-2\log q).
 \tag{L-15407.7}
\]

The zero at `z=1/2` cancels the zeta pole in the raw von Mangoldt transform.

## Safe product theorem

Let

\[
 H(z)=e^{-cz}
 \prod_{j=1}^m B_{r_j}(z)
 \prod_{\ell=1}^L P_{q_\ell}(z)
 \tag{L-15407.8}
\]

with `c>=0`, `r_j>0`, integers `q_l>=2`, and `L>=1`. More generally, one may
append an infinite smoothness tail of box factors with summable lengths, as in
`L-15405`.

Then

\[
\boxed{
 H(z)\ne0
 \qquad
 (0<\operatorname{Re}z<1/2).}
 \tag{L-15407.9}
\]

### Proof

The exponential has no zeros. Every `B_r` zero lies on the left boundary of the
strip, and every `P_q` zero lies on the right boundary. A locally uniformly
convergent infinite box product is nonzero wherever none of its factors vanish.
Thus the product is zero-free in the open strip. QED.

## Physical window

Start from any nonzero smooth compact profile whose transform is zero-free in
the open strip, for example the dyadic density of `L-15405`. Apply:

1. finitely many interval convolutions for certified line-zero notches;
2. at least one pole-annihilating difference;
3. arbitrary positive translation.

The resulting real signed function `G_H` remains smooth and compactly supported,
with Laplace transform equal to the base transform times `H`.

The raw prime statistic

\[
 Q_H(x)=
 \sum_{n\ge2}{\Lambda(n)\over\sqrt n}
 G_H(x-\log n)
 \tag{L-15407.10}
\]

has no zeta-pole term and is bounded for all right translations exactly when RH
holds, by the argument of `T-15404`.

## Exact spectral roles

The factor classes have distinct meanings.

```text
B_r:
  suppresses selected critical-line frequencies;
  never cancels an off-line displacement.

P_q:
  cancels the zeta pole;
  converts the criterion to a raw finite prime sum.

e^{-cz}:
  translates the window;
  changes no magnitude or zero set.
```

This separation lets discovery optimize numerical conditioning without changing
the analytic implication.

## Transform-bound objective

Under RH, a filter has the zero-sum moat

\[
 B_H\le B_{triv,H}
 +\sum_{k\ge0}M_k
  \sup_{k\le|t|\le k+1}
  |\widehat G_H(it)|.
 \tag{L-15407.11}
\]

The safe design problem is therefore:

\[
\boxed{
 \text{minimize }B_H
 \quad\text{subject to support, coefficient, and evaluation-cost budgets}.}
 \tag{L-15407.12}
\]

All candidate filters in the declared algebra retain exact RH equivalence.

## Rational and directed implementation

- Choose rational box lengths when exact notch placement is unnecessary.
- For zero-ball notches, use directed `r` intervals and certify the complete
  sine attenuation.
- Choose integer `q` so the pole-shift coefficient is exact.
- Store each physical shift symbolically as `2 log q`.
- Build the final profile through exact spline convolution and signed shift
  operations.
- Bound the infinite smoothness tail separately.

## Connection to direct-xi and localized Weil filters

The algebra is the prime-side analogue of the repository's response-polynomial
and zero-deflation cones. It differs in one crucial way: its analytic safety is
encoded by the location of transform zeros on the two boundary lines of the
counterexample strip.

The endpoint convolution-square subclass embeds in `L-15404`. General signed
filters need not be a single quadratic endpoint packet, but may be realized by
finite polarization or used directly as scalar von Mangoldt criteria.

## Gap audit

- A sum of safe filters need not be safe; the theorem concerns products and the
  corresponding convolution/shift construction.
- Additional polynomial differential factors require their own zero-location
  audit.
- Boundary zeros are safe for detecting strict off-line displacement but can
  suppress known on-line contributions strongly.
- Filter optimization does not prove its prime statistic bounded.
- A finite numerical search remains only a search until a strict directed moat
  comparison or a uniform analytic bound is produced.
