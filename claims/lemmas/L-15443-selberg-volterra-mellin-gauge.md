# L-15443 — Exact Mellin gauge for the Selberg–Volterra operator

Claim ID: `L-15443`  
Title: The scale-subtracted Selberg operator is a gauge-conjugated derivative, and its proposed Mourre bulk diagonalizes outside one boundary annulus  
Status: `PROPOSED — EXACT OPERATOR ALGEBRA; PHYSICAL-NORM COERCIVITY OPEN`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: PR #158 `L-15147/L-15148`; the classical Euler product in `Re z>0`; Mellin–Plancherel on a causal smooth core  
Cross-route connections: PRs #165, #208, #216, #217, #219, #222, #224  
Scope: identifies the exact positive metric behind the Selberg–Mourre proposal and the remaining metric/division hinge; it does not prove RH

## 1. Selberg–Volterra operator

For a smooth compactly supported function on `(1,infinity)`, use

\[
 \mathcal Mf(z)=\int_1^\infty f(x)x^{-z-1}\,dx.
 \tag{L-15443.1}
\]

Retain the operator of `L-15147`,

\[
\boxed{
(\mathcal Lf)(x)
=(\log x)f(x)
+\sum_{n\le x}{\Lambda(n)\over n}f(x/n)
-{1\over x}\int_1^x f(t)\,dt.}
\tag{L-15443.2}
\]

Put

\[
\boxed{m(z)=(1+z)\zeta(1+z).}
\tag{L-15443.3}
\]

All identities below first hold in `Re z>0`, where the Euler series converges absolutely, and then wherever both sides continue.

## 2. Eureka: exact gauge conjugation

Let `F=mathcal Mf`. The three terms in (L-15443.2) have transforms

\[
\mathcal M[(\log x)f](z)=-F'(z),
\tag{L-15443.4}
\]

\[
\mathcal M\left[
 \sum_{n\le x}{\Lambda(n)\over n}f(x/n)
\right](z)
=-{\zeta'\over\zeta}(1+z)F(z),
\tag{L-15443.5}
\]

and

\[
\mathcal M\left[
 {1\over x}\int_1^x f(t)dt
\right](z)
={F(z)\over1+z}.
\tag{L-15443.6}
\]

Since

\[
{m'(z)\over m(z)}
={1\over1+z}+{\zeta'\over\zeta}(1+z),
\tag{L-15443.7}
\]

one obtains the exact identity

\[
\boxed{
\mathcal M(\mathcal Lf)(z)
=-{1\over m(z)}{d\over dz}\bigl(m(z)F(z)\bigr).}
\tag{L-15443.8}
\]

Thus the complete number, prime-convolution, and continuous-average operator is not merely analogous to a first-order canonical operator: it is exactly a derivative after the arithmetic gauge `m`.

## 3. Dilation commutator and second-order diagonalization

For `a>1`, put

\[
\ell=\log a,
\qquad
(U_af)(x)=a^{-1/2}f(x/a).
\tag{L-15443.9}
\]

Then

\[
\mathcal M(U_af)(z)=e^{-\ell(z+1/2)}F(z),
\tag{L-15443.10}
\]

and (L-15443.8) immediately recovers

\[
\mathcal LU_a=U_a\mathcal L+\ell U_a.
\tag{L-15443.11}
\]

Let `r` be in the common smooth causal core, write

\[
R=\mathcal Mr,
\qquad
G=mR.
\tag{L-15443.12}
\]

Applying (L-15443.8) twice gives

\[
\boxed{
\mathcal M\bigl[\mathcal L(\mathcal L-\ell)r\bigr](z)
={G''(z)+\ell G'(z)\over m(z)}.}
\tag{L-15443.13}
\]

This is the exact source-coordinate content behind the proposed Selberg–Mourre square completion.

## 4. Exact physical logarithmic energy

Assume on the chosen vertical line that

\[
G(z)=\int_0^\infty g(y)e^{-zy}\,dy
\tag{L-15443.14}
\]

with `e^{-cy}g(y)` in `L2`, where `z=c+it`. Then

\[
G''(z)+\ell G'(z)
=\int_0^\infty y(y-\ell)g(y)e^{-zy}\,dy.
\tag{L-15443.15}
\]

Mellin/Fourier Plancherel therefore gives

\[
\boxed{
\begin{aligned}
&{1\over2\pi}\operatorname{Re}
 \int_{\mathbb R}
 \overline{G(c+it)}
 \bigl[G''+\ell G'\bigr](c+it)\,dt\\
&\qquad=
 \int_0^\infty
 y(y-\ell)e^{-2cy}|g(y)|^2\,dy.
\end{aligned}}
\tag{L-15443.16}
\]

Consequently the gauged second-order form is:

```text
strictly positive on y>ell,
zero at y=0 and y=ell,
negative only on the first logarithmic boundary band 0<y<ell.
```

This proves, in the exact arithmetic gauge, the number-operator/boundary geometry sought in `M-15110`: the bulk does not require a conjectural semiprime sign. All possible negative mass is confined to one explicit initial annulus.

The identity is metric-sensitive. It controls `G=mR`, not the original Mellin vector `R`.

## 5. The actual Chebyshev dilation ray

Put

\[
P(x)={\psi(x)\over x},
\qquad
f_a(x)=P(x)-P(x/a),
\qquad
r_a=(I-U_a)f_a.
\tag{L-15443.17}
\]

`L-15148` gives

\[
\mathcal Mf_a(z)
=(1-a^{-z})
 { -\zeta'/\zeta(1+z)\over1+z}.
\tag{L-15443.18}
\]

Therefore

\[
\boxed{
R_a(z)
=(1-a^{-z})(1-a^{-z-1/2})
 { -\zeta'/\zeta(1+z)\over1+z},}
\tag{L-15443.19}
\]

while the gauged numerator is

\[
\boxed{
G_a(z)=m(z)R_a(z)
=(1-a^{-z})(1-a^{-z-1/2})[-\zeta'(1+z)].}
\tag{L-15443.20}
\]

The nontrivial-zero denominator has disappeared from the numerator. Only the elementary zeta-pole channel and an explicit all-integer logarithmic source remain.

If `rho` is a zeta zero of multiplicity `m`, then `z=rho-1` is a zero of `m` of order `m`, whereas `G_a` has order exactly `m-1` unless a dilation factor vanishes there. The two dilation factors have zeros only on

\[
\Re z=0
\quad\text{and}\quad
\Re z=-1/2.
\tag{L-15443.21}
\]

Thus no zero with

\[
-1/2<\Re z<0
\tag{L-15443.22}
\]

is canceled. Division by `m` recreates one simple pole at every shifted off-critical zero, independently of its multiplicity.

## 6. Exact review hinge for the proposed full Selberg–Mourre proof

Equations (L-15443.13)--(L-15443.16) show that a positive bulk identity is available without guessing the factor maps of `M-15110.17`, but only in the gauged metric.

A completed proof still has to justify a physical/source estimate of the form

\[
\boxed{
\|R\|_{\rm physical}
\ \lesssim_{\rm poly}\ 
\|mR\|_{\rm gauge}
+\|\text{explicit first-annulus trace}\|,}
\tag{L-15443.23}
\]

on the actual causal range and uniformly along the cofinal critical approach.

It is not valid to obtain (L-15443.23) by simply declaring `1/m` holomorphic and bounded in the target half-plane. For the source ray (L-15443.20), holomorphic division by `m` across every shifted zero in the open strip is exactly the zero-exclusion statement being sought.

Accordingly:

```text
M-15110 bulk square:
    exact in the arithmetic gauge;

conversion back to the original Chebyshev/Hardy norm:
    still RH-bearing;

finite semiprime factorization:
    useful only if it supplies this physical metric conversion rather than
    reproducing the already-positive gauged bulk.
```

This is the smallest audit target for PR #158's proposed completion.

## 7. Cross-route synthesis

### Prime Hardy and semiprime routes — PRs #216/#222/#224

These routes estimate the physical signal `R` directly. Their signed Type-II or critical `H1` theorem is precisely a noncircular way to establish the metric conversion in (L-15443.23). The gauge identity explains why entrywise absolute values fail: they destroy the division-compatible cancellation before the physical norm is formed.

### Line-zero annihilator — PR #217

The centered notch product supplies boundary factors at the actual critical-line zeros. In gauge language it removes the known boundary divisors while leaving every open-strip divisor in (L-15443.22) visible. The positive variance defect of `T-21702` is a scalar trace of the same uncanceled quotient obstruction.

### Prime polygon and critical-load queue — PR #219 and `L-15439`

The polygon margin and the queue reserve work before Mellin division, directly on the physical prime-power measure. They are convex-dual and transport coordinates for controlling the same source ray without an inverse-zeta metric step.

### Haar and r-adic screw filters — PR #218

The factors in (L-15443.19) are the Mellin analogue of the boundary-safe dilation filters. The sharp half-knot debt found on PR #218 is the finite-filter manifestation of the fact that only boundary-line zeros can be canceled safely.

## 8. Proof boundary

Closed exactly:

- the Mellin transforms (L-15443.4)--(L-15443.6);
- the gauge identity (L-15443.8);
- the second-order identity (L-15443.13);
- the positive-outside-one-band Plancherel formula (L-15443.16);
- the explicit actual-source numerator (L-15443.20);
- the open-strip noncancellation and multiplicity statement.

Open:

- the physical metric conversion (L-15443.23);
- the finite-section boundary estimate in the original source norm;
- any signed semiprime/Carleson theorem strong enough to supply that conversion.

This lemma does not prove RH. It turns the newest Selberg–Mourre proposal into an exact gauged theorem and isolates the remaining noncircular step.