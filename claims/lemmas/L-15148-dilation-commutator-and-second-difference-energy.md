# L-15148 — Dilation commutator and second-difference energy

Claim ID: `L-15148`  
Title: The scale-subtracted Selberg operator has an exact creation-operator commutator, and one boundary-safe second difference retains the full rightmost-zero exponent  
Status: **PROPOSED PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: `L-15147`; the Hardy/Paley–Wiener transfer used in `T-15119`  
Scope: exact operator algebra and a new finite arithmetic energy; no coercivity claim

## 1. The causal Selberg operator

Extend every function on `[1,infinity)` by zero below `1`. Retain the operator
from `L-15147`,

\[
\boxed{
(\mathcal L f)(x)
 = (\log x)f(x)
 +\sum_{n\le x}{\Lambda(n)\over n}f(x/n)
 -{1\over x}\int_1^x f(t)\,dt.}
\tag{L-15148.1}
\]

For `a>1`, put

\[
\ell=\log a
\]

and define the normalized dilation

\[
\boxed{
(U_af)(x)=a^{-1/2}f(x/a).}
\tag{L-15148.2}
\]

On `L^2([1,infinity),dx)`, `U_a` is an isometry whose range is supported in
`[a,infinity)`.

## 2. Exact commutator

The dilation commutes with both causal averaging terms in (L-15148.1).
Indeed,

\[
\begin{aligned}
\sum_{n\le x}{\Lambda(n)\over n}(U_af)(x/n)
&=a^{-1/2}
  \sum_{n\le x/a}{\Lambda(n)\over n}f(x/(an))\\
&=U_a\left(
  \sum_{n\le \cdot}{\Lambda(n)\over n}f(\cdot/n)
  \right)(x),
\end{aligned}
\tag{L-15148.3}
\]

because the terms with `n>x/a` evaluate `f` below `1` and vanish. Also,

\[
{1\over x}\int_1^x (U_af)(t)\,dt
=U_a\left({1\over \cdot}\int_1^{\cdot}f(t)\,dt\right)(x).
\tag{L-15148.4}
\]

Only multiplication by `log x` fails to commute:

\[
(\log x)U_af
=U_a((\log x)f)+\ell U_af.
\tag{L-15148.5}
\]

Consequently,

\[
\boxed{
\mathcal L U_a=U_a\mathcal L+\ell U_a,}
\tag{L-15148.6}
\]

or equivalently

\[
\boxed{
(\mathcal L-\ell)U_a=U_a\mathcal L.}
\tag{L-15148.7}
\]

This is an exact creation-operator commutation law. It is not an asymptotic
prime-number-theorem statement.

## 3. Scale-subtracted Chebyshev solution

Put

\[
P(x)={\psi(x)\over x},
\qquad
f_a(x)=P(x)-P(x/a).
\tag{L-15148.8}
\]

`L-15147` proves

\[
\boxed{
\mathcal L f_a=H_a,}
\tag{L-15148.9}
\]

where the explicit Selberg forcing `H_a` is bounded.

Define the boundary-safe second difference

\[
\boxed{
r_a=(I-U_a)f_a.}
\tag{L-15148.10}
\]

The commutator eliminates the unknown `f_a` after one further application of
`mathcal L`. Directly from (L-15148.6)--(L-15148.9),

\[
\boxed{
\mathcal L(\mathcal L-\ell)r_a
=(I-U_a)\mathcal L H_a
-\ell(I+U_a)H_a.}
\tag{L-15148.11}
\]

### Proof

First,

\[
(\mathcal L-\ell)r_a
=H_a-\ell f_a-U_aH_a.
\]

Apply `mathcal L`, use `mathcal Lf_a=H_a`, and use
`mathcal LU_a=U_a(\mathcal L+\ell)`. This gives exactly
(L-15148.11). QED.

Thus the twice-filtered RH variable solves a written-down second-order causal
operator equation whose right side contains only the explicit Selberg forcing.

## 4. Safe Mellin transform

Use

\[
\mathcal Mf(z)=\int_1^\infty f(x)x^{-z-1}\,dx.
\]

For `Re z>0`,

\[
\mathcal M f_a(z)
=(1-a^{-z})
{ -\zeta'/\zeta(1+z)\over1+z}.
\tag{L-15148.12}
\]

The dilation has Mellin multiplier

\[
\mathcal M(U_af)(z)=a^{-z-1/2}\mathcal Mf(z).
\tag{L-15148.13}
\]

Therefore

\[
\boxed{
\mathcal M r_a(z)
=(1-a^{-z})(1-a^{-z-1/2})
{ -\zeta'/\zeta(1+z)\over1+z}.}
\tag{L-15148.14}
\]

The first factor cancels the zeta pole at `z=0`. The second has all its zeros
on the boundary line `Re z=-1/2`. Neither factor vanishes in

\[
-\frac12<\operatorname{Re}z<0.
\]

Hence the weighted-`L2` abscissa of `r_a` is still the rightmost zeta-zero
displacement.

Writing

\[
\mathcal R_a(Y)=\int_2^Y|r_a(x)|^2\,dx,
\]

the same half-plane transfer as in `T-15119` gives the proposed identity

\[
\boxed{
\Theta_\zeta
=\limsup_{Y\to\infty}
 {\log(1+\mathcal R_a(Y))\over2\log Y}.}
\tag{L-15148.15}
\]

In particular,

\[
\boxed{
\mathrm{RH}
\iff
\mathcal R_a(Y)=Y^{o(1)}.}
\tag{L-15148.16}
\]

The transfer statement is proposed under the same analytic hypotheses and
review boundary as `T-15119`.

## 5. Exact integer producer

Let `a=c^2` with integer `c>=2`, and let `N` be an integer. On the open cell
`m<x<m+1`,

\[
f_a(x)
={\psi(m)-a\psi(\lfloor m/a\rfloor)\over x}.
\]

Consequently

\[
r_a(x)={B_{a,c}(m)\over x},
\]

where

\[
\boxed{
B_{a,c}(m)
=\psi(m)-(a+c)\psi(\lfloor m/a\rfloor)
+ac\,\psi(\lfloor m/a^2\rfloor).}
\tag{L-15148.17}
\]

Thus

\[
\boxed{
\mathcal R_a(N)
=\sum_{m=2}^{N-1}
 {B_{a,c}(m)^2\over m(m+1)}.}
\tag{L-15148.18}
\]

At scale four,

\[
\boxed{
B_{4,2}(m)
=\psi(m)-6\psi(\lfloor m/4\rfloor)
+8\psi(\lfloor m/16\rfloor),}
\tag{L-15148.19}
\]

and

\[
\boxed{
\mathcal R_4(N)
=\sum_{m=2}^{N-1}
 {\left[
 \psi(m)-6\psi(\lfloor m/4\rfloor)
 +8\psi(\lfloor m/16\rfloor)
 \right]^2\over m(m+1)}.}
\tag{L-15148.20}
\]

Every finite level is an exact positive arithmetic object.

## 6. Annular shift model

Define the unitary annular coordinates

\[
(\mathscr Uf)_j(u)=a^{j/2}f(a^ju),
\qquad1\le u<a.
\tag{L-15148.21}
\]

Then

\[
\|f\|_{L^2([1,a^J])}^2
=\sum_{j=0}^{J-1}
 \|(\mathscr Uf)_j\|_{L^2([1,a])}^2,
\tag{L-15148.22}
\]

and `U_a` becomes the unilateral backward shift:

\[
(\mathscr U U_af)_j=(\mathscr Uf)_{j-1}.
\tag{L-15148.23}
\]

If

\[
d_j=(\mathscr U f_a)_j,
\]

then

\[
\boxed{
\mathcal R_a(a^J)
=\sum_{j=0}^{J-1}
 \|d_j-d_{j-1}\|_{L^2([1,a])}^2,}
\tag{L-15148.24}
\]

with the zero-extension boundary convention. The full RH problem is therefore
an exact scale-square-function problem for one causal arithmetic sequence.

## 7. Proof boundary

Closed exactly:

- the dilation isometry;
- the commutator (L-15148.6);
- the second-order equation (L-15148.11);
- the Mellin multiplier and open-strip zero-free geometry;
- the finite rational energy formula;
- the annular unilateral-shift representation.

Not closed:

- a polynomial or subpolynomial upper bound for (L-15148.18);
- a coercive estimate for `mathcal L(mathcal L-ell)` on the range of `I-U_a`.

Those are the load-bearing steps of the full proposal recorded separately.