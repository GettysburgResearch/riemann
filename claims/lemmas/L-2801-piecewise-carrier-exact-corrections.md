# L-2801 — Exact compact correction formulas for piecewise carriers

Claim ID: L-2801  
Title: Exact cellwise archimedean and pole reductions for D-0801  
Status: PROPOSED  
Authoring agent: `gpt56-04-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801; the archimedean and pole normalization inherited from D-0001/L-0702  
Scope: exact finite-dimensional reduction, independent of X-0701/X-0801 numerical code  
Related counterexample candidates: none

## Statement

Fix `L>0`, put

\[
 \Delta=\frac{L}{2\pi},\qquad h=\frac{\Delta}{K},
\]

and use the D-0801 piecewise carrier with coefficient vector
`v=(v_0,...,v_{K-1})`. Normalize

\[
 \sum_{j=0}^{K-1}|v_j|^2=1,
\]

so that `hat(g)(0)=h`.

Write

\[
 H(r)=\operatorname{Re}\psi\!\left(\frac14+\frac{ir}{2}\right)-\log\pi
\]

and use the source normalization

\[
 \mathcal A(g)=\frac1{2\pi}\int_{\mathbb R}H(r)g(r)\,dr,
 \qquad
 \mathcal R(g)=2g(i/2).
\]

For `0<=d<K`, define the discrete autocorrelations

\[
 a_d=\sum_{j=0}^{K-1-d}v_{j+d}\overline{v_j},
 \qquad a_K=0.
\]

For `0<=t<=2L`, put

\[
 r(t)=\frac{Kt}{2L},\qquad d=\lfloor r(t)\rfloor,
 \qquad f=r(t)-d,
\]

with the endpoint `t=2L` interpreted as zero, and define

\[
 C_v(t)=(1-f)a_d+fa_{d+1},
 \qquad
 B_v(t)=\operatorname{Re}\!\left(e^{-iTt/2}C_v(t)\right).
\]

Then the exact normalized archimedean and pole Rayleigh values are

\[
 \boxed{
 \frac{\mathcal A(g_{T,v})}{h}
 =\frac1{2\pi}\left[
 \int_0^{2L}\left(
 \frac{e^{-t}}t-
 \frac{e^{-t/4}}{1-e^{-t}}B_v(t)
 \right)dt+E_1(2L)-\log\pi
 \right],}
\]

and

\[
 \boxed{
 \frac{\mathcal R(g_{T,v})}{h}
 =\frac1\pi\int_0^{2L}\cosh(t/4)B_v(t)\,dt.}
\]

The first integrand is understood as the combined removable expression at
`t=0`; its two displayed pieces must not be evaluated independently there.

Equivalently, the pole term has the finite cell-transform formula

\[
 \boxed{
 \mathcal R(g_{T,v})
 =2\operatorname{Re}\left[
 W_v(-T+i/2)\overline{W_v(-T-i/2)}
 \right].}
\]

Both compact terms are Hermitian Toeplitz quadratic forms. If

\[
 \tau_d(r)=(1-|r-d|)_+,
\]

let `M(t)` be the Hermitian Toeplitz matrix with

\[
 M_{j,j}(t)=\tau_0(r(t))\cos(Tt/2)
\]

and, for `d>=1`,

\[
 M_{j,j+d}(t)=\frac12\tau_d(r(t))e^{-iTt/2},
 \qquad
 M_{j+d,j}(t)=\overline{M_{j,j+d}(t)}.
\]

Then

\[
 v^*M(t)v=B_v(t),
\]

so the two source matrices are compact integrals of one explicitly known
Toeplitz path plus scalar multiples of the identity.

## Proof

### Cellwise autocorrelation

For positive `xi`, the overlap between a cell and a translate of another cell
has normalized length

\[
 \left(1-\left|j-k-\frac{\xi}{h}\right|\right)_+.
\]

At `xi=t/(4*pi)`, one has `xi/h=Kt/(2L)=r(t)`. Only the two nearest integer
lags can occur. At the integer lag `d` the normalized autocorrelation is
`a_d`, and linear interpolation to the next knot gives

\[
 \frac{R_v(t/(4\pi))}{h}
 =(1-f)a_d+fa_{d+1}=C_v(t).
\]

D-0801 therefore gives

\[
 \frac{\widehat g_{T,v}(t/(4\pi))}{h}=B_v(t).
\]

The Toeplitz representation follows by expanding `a_d` and pairing every
positive-lag term with its conjugate transpose.

### Archimedean term

For `Re(z)>0`, use the regularized digamma identity

\[
 \psi(z)=\int_0^\infty\left(
 \frac{e^{-t}}t-\frac{e^{-zt}}{1-e^{-t}}
 \right)dt,
\]

where the two singular terms are interpreted together. At
`z=1/4+ir/2`, take real parts and integrate against `g(r)`. The Fourier
convention gives

\[
 \int_{\mathbb R}g(r)\cos(rt/2)\,dr
 =\widehat g(t/(4\pi)).
\]

Also

\[
 \int_{\mathbb R}g(r)\,dr=\widehat g(0)=h.
\]

The compact support of `hat(g)` removes the second term when `t>2L`; the
remaining first-term tail is exactly `h E_1(2L)`. Division by `h` gives the
boxed formula.

At the origin, `B_v(0)=a_0=1`. Hence the `1/t` singularities cancel. Since
`C_v(t)` is piecewise linear, the combined integrand has a finite one-sided
limit.

### Pole term

Fourier inversion at `z=i/2` gives

\[
 g(i/2)=\int_{-\Delta}^{\Delta}\widehat g(\xi)e^{-\pi\xi}\,d\xi.
\]

The transform is real and even, so

\[
 2g(i/2)=4\int_0^\Delta\cosh(\pi\xi)\widehat g(\xi)\,d\xi.
\]

Substituting `t=4*pi*xi` and dividing by `h` yields the compact pole formula.

For the finite formula, D-0801 gives

\[
 A_{T,v}(i/2)=W_v(-T+i/2)\overline{W_v(-T-i/2)}.
\]

The corresponding value at `-i/2` is its complex conjugate. Their average is
`g(i/2)`, proving the identity.

## Analytic domain audit

- `W_v`, its Schwarz reflection, and `g_{T,v}` are entire.
- The only special-function identity used is the digamma integral in the half
  plane `Re(z)>0`, applied at real part `1/4`.
- Fourier support is exactly contained in `[-Delta,Delta]`.
- The compact archimedean integrand must be evaluated as one cancellation-safe
  expression at zero.
- `E_1(2L)` is the ordinary positive real exponential integral.
- The formulas are conditional on the inherited project source normalization;
  they do not independently prove the full Guinand--Weil theorem.

## Dependency audit

The cell overlap, pole formula, and Fourier reduction are re-derived here and
share no implementation with X-0701 or X-0801. The factors `1/(2*pi)`,
`1/pi`, and the sign of the prime block remain tied to the explicit-formula
normalization whose wider audit is still open.

## Gap audit

1. A numerical quadrature of these formulas is not automatically rigorous.
2. Huge phases require directed range reduction before a sign can be promoted.
3. The equal-cell envelope may require mollification if the final selected
   Guinand--Weil theorem demands more regularity than D-0801 presently proves.
4. A negative leading prime matrix is not enough; these exact corrections and
   every normalization dependency must be included.

## Adversarial tests

X-2801 independently checks:

- the autocorrelation values at the zero and support endpoints;
- agreement of the compact pole integral with the finite cell-transform formula
  for a complex three-cell vector;
- agreement of the `K=1` compact archimedean formula with a separately arranged
  cancellation-safe triangular expression.

## Remaining uncertainty

No algebraic discrepancy was found. Independent review should reconstruct the
Fourier sign and the project-level source normalization before status promotion.

## Suggested next attack

Use L-2802 to bound the complete correction without oscillatory quadrature, then
replace the ordinary prime-side margin in PR #44 by a directed phase-ball
interval. The exact checker in X-2801 can combine the two pieces.
