# L-90210 — The broad quarter-balanced hinge occupation has an explicit reciprocal-zeta Mellin symbol with no deterministic cancellation

Claim ID: `L-90210`  
Status: **PROPOSED COMPLETE CONTINUUM ANALYTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: continuum child law and characteristic of `L-90212`; elementary Möbius/Mellin calculus  
Scope: the scale-invariant continuum model associated to the ordered balanced policy; finite-policy convergence is not asserted here and RH is not proved

## 1. Continuum square-root hinge source

For `x>=1`, define

\[
 u(x)=\sum_{k\le x}\mu(k)
 \left(\sqrt{\frac{x}{k}}-1\right).
\tag{L-90210.1}
\]

This is the scale profile of the multiples-Möbius primitive for the hinge
`h_T(q)=q^{-1/2}-T^{-1/2}` under `x=T/n`. On every open integer cell,

\[
 u'(x)=\frac1{2\sqrt x}\sum_{k\le x}\frac{\mu(k)}{\sqrt k}.
\]

Put

\[
 \boxed{
 g(x)=xu'(x)
 =\frac{\sqrt x}{2}\sum_{k\le x}\frac{\mu(k)}{\sqrt k}.
 }
\tag{L-90210.2}
\]

## 2. Broad-policy Green operator

The continuum child law of `L-90212` is

\[
 p(v)=4v\mathbf1_{1/4\le v\le3/4}.
\]

The transpose occupation operator is

\[
 \boxed{
 (\mathcal Km)(x)
 =4\int_{4/3}^{4}m(x/t)t^{-2}\,dt
 =\frac4x\int_{x/4}^{3x/4}m(y)\,dy,
 }
\tag{L-90210.3}
\]

with `m(y)=0` below one. The scale-invariant continuum occupation solves

\[
 \boxed{m=g+\mathcal Km.}
\tag{L-90210.4}
\]

This is a continuum model only; no finite-to-continuum error estimate is hidden
in the statement.

## 3. Mellin transform of the arithmetic source

For `Re s>1`, finite switching gives

\[
 \boxed{
 \widehat g(s)
 =\int_1^\infty g(x)x^{-s-1}dx
 =\frac1{2(s-1/2)\zeta(s)}.
 }
\tag{L-90210.5}
\]

## 4. Green multiplier and complete symbol

Scaling `x=ty` gives

\[
 \widehat{\mathcal Km}(s)=\kappa(s)\widehat m(s),
\]

where

\[
 \boxed{
 \kappa(s)
 =4\int_{4/3}^{4}t^{-s-2}dt
 =\frac4{s+1}
 \left[\left(\frac34\right)^{s+1}
       -\left(\frac14\right)^{s+1}\right].
 }
\tag{L-90210.6}
\]

This is `phi(s-1)` for the selected-child moment of `L-90212`. Put

\[
 \Delta_{\rm bal}(s)=1-\kappa(s).
\tag{L-90210.7}
\]

Then

\[
 \boxed{
 \widehat m(s)
 =\frac1{2(s-1/2)\zeta(s)\Delta_{\rm bal}(s)}.
 }
\tag{L-90210.8}
\]

initially for `Re s>1`, then meromorphically.

## 5. Real-axis geometry and the positive main pole

Because `0<V<1`,

\[
 \kappa(s)=\mathbb E[V^{s-1}]
\]

is strictly decreasing on the real axis, so

\[
 \Delta_{\rm bal}(s)<0\ (s<1),\qquad
 \Delta_{\rm bal}(1)=0,\qquad
 \Delta_{\rm bal}(s)>0\ (s>1).
\tag{L-90210.9}
\]

At `s=1`, the simple zero of `1/zeta(s)` cancels the simple conservation zero.
At the critical point,

\[
 \kappa(1/2)=\sqrt3-\frac13,
 \qquad
 \boxed{\Delta_{\rm bal}(1/2)=\frac43-\sqrt3<0.}
\tag{L-90210.10}
\]

Also `zeta(1/2)<0`, e.g. directly from the alternating eta continuation.
Hence the pole at `s=1/2` has positive residue

\[
 \boxed{
 C_{\rm bal}
 =\frac1{2\zeta(1/2)(4/3-\sqrt3)}>0.
 }
\tag{L-90210.11}
\]

## 6. Every hypothetical off-line zeta zero survives

If `zeta(rho)=0` with `Re rho>1/2`, then `Delta_bal` is analytic at `rho` and
occurs in the denominator, not the numerator. It cannot cancel the reciprocal
zeta pole; if it also vanishes, the singularity is only stronger. Thus

\[
 \boxed{
 \zeta(\rho)=0,\ \Re\rho>1/2
 \Longrightarrow \widehat m(s)\text{ is singular at }s=\rho.
 }
\tag{L-90210.12}
\]

This differs fundamentally from the frozen factorization, where a
boundary-dependent deterministic numerator could cancel arithmetic poles.

## 7. Continuum one-sign criterion implies RH

By `L-90212`, `Delta_bal` has no zeros on `Re s>=1` except the removable
conservation root and has a strict deterministic gap. On `(1/2,1)` its real
sign in (L-90210.9) makes it nonzero, and zeta has no real zero there.

If `m(x)>=0` eventually and an off-line zero `rho` existed, the nonreal
singularity (L-90210.12) would force the abscissa of convergence to lie to the
right of the explicit real critical pole. Landau's one-sign theorem would then
force a singularity at that positive real abscissa, but none exists. Therefore

\[
 \boxed{m(x)\ge0\text{ eventually}\Longrightarrow\mathrm{RH}.}
\tag{L-90210.13}
\]

This is a criterion, not a positivity proof.

## 8. Critical logarithmic target

The corresponding critical-log continuum occupation has formal symbol

\[
 \boxed{
 \widehat m_{\log}(s)
 =\frac{s}
 {(s-1/2)^2\zeta(s)\Delta_{\rm bal}(s)}.
 }
\tag{L-90210.14}
\]

The double critical pole produces a positive `sqrt(x) log x` main mode, while
nontrivial zeros retain an additional Riesz smoothing relative to the hinge.
No sign theorem is asserted.

## 9. Proof boundary

Proved for the continuum model:

- the exact square-root Möbius source;
- the broad transpose Green operator and Mellin multiplier;
- the reciprocal-zeta occupation symbol;
- positivity of the critical main residue;
- automatic survival of every hypothetical off-line zeta zero;
- eventual continuum occupation positivity implies RH;
- the logarithmic-target symbol.

Still open:

- positivity of the continuum hinge or logarithmic occupation;
- a sharp finite-to-continuum theorem for `L-90212.5`;
- finite OBH;
- RH.
