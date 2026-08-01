# L-15628 — A zero-avoiding Fourier–Mellin source inverse has sub-square-root size

Claim ID: `L-15628`  
Title: Cofinal support selection and Mellin-cardinal sources give an exact finite Fourier right inverse of size `R^(1/4+o(1))`  
Status: `PROPOSED — COMPLETE MODULO THE DECLARED LOCAL ZETA-PRODUCT AND PERIODIZED MELLIN NORMALIZATIONS`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-16205`; `L-16211`; Riemann–von Mangoldt; the standard local product/partial-fraction lemma for zeta in a fixed strip  
Scope: the exact complete-source-frame gate of `L-15627`  
Related counterexample candidates: none

## 1. Purpose

`L-16211` proves finite projected source surjectivity away from zeta-cycle
lengths, but gives no norm for a right inverse. `L-20301` gives an exact
pointwise Möbius inverse, but its forced prefix is unnecessarily large for a
finite Fourier target.

This lemma constructs an exact right inverse directly on the finite circle
space. The support is chosen so that every required zeta multiplier is only
subexponentially small in the logarithmic support. The source interpolation is
explicit and uses one guard mode to impose the exact source integral condition.

The resulting source/profile size is

\[
 R^{1/4+o(1)},
\]

where `R=exp(L)` is the radial scale and `L` is the logarithmic circle length.
This is strictly below the support-large-sieve threshold

\[
 \sqrt{R/\log R}.
\]

The theorem controls the **unwhitened** exact inverse. A tail-Gram floor is a
separate condition and is handled by the core-plus-correction theorem
`L-15629`.

## 2. Finite Fourier target

Let

\[
 L\to\infty,
 \qquad
 N_L\le C_0L^2,
\tag{L-15628.1}
\]

and put

\[
 \omega_k(L)=\frac{2\pi k}{L},
 \qquad |k|\le N_L.
\tag{L-15628.2}
\]

Let

\[
 E_{N_L}(L)
 =\operatorname{span}\{e^{i\omega_k(L)x}:|k|\le N_L\}
\tag{L-15628.3}
\]

on the circle of length `L`. In the periodized Mellin normalization inherited
from `L-16205/L-16211`, the `k`th Fourier coefficient of the arithmetic image
of a source `f` is

\[
 \boxed{
 \widehat{\Sigma E(f)}(k)
 =
 \zeta\!\left(\frac12+i\omega_k(L)\right)
 M_f\!\left(\omega_k(L)\right),
 }
\tag{L-15628.4}
\]

where `M_f` is the normalized positive-half Mellin transform. Any harmless
fixed factor from even extension must be inserted consistently on both sides.

## 3. A cofinal zero-avoiding length

Fix a large parameter `A`. We select a length

\[
 \ell_A\in[A,A+1].
\tag{L-15628.5}
\]

Let

\[
 \delta_A=A^{-4}.
\tag{L-15628.6}
\]

For every nontrivial zero ordinate `gamma` with

\[
 |\gamma|\le C_1A
\tag{L-15628.7}
\]

and every integer `k` for which

\[
 |k|\le C_2A^2,
\tag{L-15628.8}
\]

remove the lengths satisfying

\[
 \left|\frac{2\pi k}{\ell}-\gamma\right|<\delta_A.
\tag{L-15628.9}
\]

### Measure estimate

For one fixed nonzero ordinate `gamma`, the number of resonant integers whose
resonance lies in `[A,A+1]` is `O(1+|gamma|)`. At such a resonance,

\[
 \left|\frac{d}{d\ell}\frac{2\pi k}{\ell}\right|
 \asymp\frac{|\gamma|}{A},
\]

so the total removed length for that ordinate is `O(delta_A A)`. The
Riemann–von Mangoldt bound gives `O(A log A)` ordinates through height `C_1 A`.
Therefore the complete removed measure is

\[
 O(\delta_AA^2\log A)=O(A^{-2}\log A)<1
\tag{L-15628.10}
\]

for large `A`. Thus one may choose `ell_A` for which

\[
 \boxed{
 \operatorname{dist}\!\left(
  \frac{2\pi k}{\ell_A},
  \{\operatorname{Im}\rho\}
 \right)
 \ge A^{-4}
 }
\tag{L-15628.11}
\]

simultaneously for every required grid point. The selected lengths may also
avoid any prescribed countable exceptional set.

## 4. Local zeta-product bound

Use the standard local factorization, uniformly for `-1<=sigma<=2` and
`2<=|t|<=C_1A`,

\[
 \log|\zeta(\sigma+it)|
 =
 \sum_{|\gamma-t|\le1}
 \log|\sigma+it-\rho|
 +O(\log(|t|+2)),
\tag{L-15628.12}
\]

with the pole, trivial factors and completed-gamma term treated in the fixed
normalization. The corresponding partial-fraction estimate is

\[
 \frac{\zeta'}{\zeta}(\sigma+it)
 =
 \sum_{|\gamma-t|\le1}
 \frac1{\sigma+it-\rho}
 +O(\log(|t|+2)).
\tag{L-15628.13}
\]

There are `O(log A)` zeros in every unit-height window. Combining
(L-15628.11)--(L-15628.13) gives

\[
 \boxed{
 \max_{|k|\le C_2A^2}
 \left|
 \zeta\!\left(\frac12+i\frac{2\pi k}{\ell_A}\right)
 \right|^{-1}
 \le
 \exp\!\bigl(C(\log A)^2\bigr).
 }
\tag{L-15628.14}
\]

It also gives the logarithmic support-derivative bound

\[
 \boxed{
 \max_k
 \left|
 \frac{d}{d\ell}
 \zeta\!\left(\frac12+i\frac{2\pi k}{\ell}\right)^{-1}
 \right|_{\ell=\ell_A}
 \le
 \exp\!\bigl(C(\log A)^2\bigr).
 }
\tag{L-15628.15}
\]

Polynomial factors from (L-15628.13) are absorbed in the exponential. The
bounded low-height interval is handled by the same finite avoidance and
compactness argument.

Since

\[
 R_A=e^{\ell_A},
\tag{L-15628.16}
\]

both bounds are

\[
 R_A^{o(1)}.
\tag{L-15628.17}
\]

## 5. Mellin-cardinal source columns

Put

\[
 \chi_L(x)=\frac1L\mathbf 1_{[-L/2,L/2]}(x),
\tag{L-15628.18}
\]

and

\[
 q_{k,L}(x)=\chi_L(x)e^{-i\omega_k(L)x}.
\tag{L-15628.19}
\]

Then

\[
 \int_{\mathbb R}q_{k,L}(x)e^{i\omega_j(L)x}\,dx
 =\delta_{jk}.
\tag{L-15628.20}
\]

Translate `q_(k,L)` to the positive multiplicative source by the exact
logarithmic Mellin isometry of `L-16205`; denote the resulting compact BV source
by `b_(k,L)`. It is supported in

\[
 [e^{-L/2},e^{L/2}],
\tag{L-15628.21}
\]

and therefore vanishes in a neighborhood of zero.

## 6. Exact integral correction by one guard mode

The only remaining source condition is the ordinary integral. Let

\[
 k_*=N_L+1.
\tag{L-15628.22}
\]

The guard column has zero Mellin samples on every target grid point by
(L-15628.20). Put

\[
 a_k=\int_{\mathbb R}b_{k,L}(x)\,dx.
\tag{L-15628.23}
\]

For the box cardinal column, direct integration gives `a_(k_*)!=0` and

\[
 \left|\frac{a_k}{a_{k_*}}\right|
 \le C(1+N_L)
\tag{L-15628.24}
\]

uniformly for `|k|<=N_L`. Define

\[
 \boxed{
 \widetilde b_{k,L}
 =b_{k,L}-\frac{a_k}{a_{k_*}}b_{k_*,L}.
 }
\tag{L-15628.25}
\]

Then

\[
 \widetilde b_{k,L}(0)=0,
 \qquad
 \int\widetilde b_{k,L}=0,
\tag{L-15628.26}
\]

and its target Mellin samples are still exactly the Kronecker delta.

## 7. Exact projected source inverse

For

\[
 y(x)=\sum_{|k|\le N_L}y_ke^{i\omega_k(L)x},
\tag{L-15628.27}
\]

define

\[
 \boxed{
 \mathcal C_Ly
 =
 \sum_{|k|\le N_L}
 \frac{y_k}
 {\zeta(1/2+i\omega_k(L))}
 \widetilde b_{k,L}.
 }
\tag{L-15628.28}
\]

Equations (L-15628.4), (L-15628.20), and (L-15628.25) imply

\[
 \boxed{
 P_{N_L}\Sigma E(\mathcal C_Ly)=y.
 }
\tag{L-15628.29}
\]

Thus `C_L` is an exact source right inverse on the complete finite Fourier
space, not merely on a preselected packet.

## 8. Quantitative envelope

The cardinal columns are orthogonal before the rank-one guard correction. In
any fixed logarithmic BV/Sobolev graph norm of order `p`, their synthesis norm
is bounded by a fixed power of `L+N_L`. Equation (L-15628.24) adds only another
polynomial factor. Combining with (L-15628.14)--(L-15628.15),

\[
 \|\mathcal C_L\|_{\mathrm{Fourier}\to\mathrm{graph}}
 +
 \left\|\frac{d}{dL}\mathcal C_L\right\|
 \le
 \exp\!\bigl(C_p(\log L)^2\bigr).
\tag{L-15628.30}
\]

Returning from logarithmic source coordinates to the symmetric multiplicative
interval costs at most the endpoint weight

\[
 e^{L/4}=R^{1/4}.
\tag{L-15628.31}
\]

Consequently every fixed-order endpoint/alias profile seminorm generated by the
ledger of `L-16221` satisfies

\[
 \boxed{
 \mathfrak M_R
 \le
 R^{1/4}\exp\!\bigl(C(\log\log R)^2\bigr)
 =R^{1/4+o(1)}.
 }
\tag{L-15628.32}
\]

The same bound holds for the logarithmic support derivative after the common
geometric phase is extracted.

Since

\[
 R^{1/4+o(1)}
 =o\!\left(\sqrt{R/\log R}\right),
\tag{L-15628.33}
\]

the exact projected source inverse itself lies strictly below the support
large-sieve conditioning barrier.

## 9. Metric transport

If the production metric `G_L` on a target subspace `W_L subset E_(N_L)(L)`
satisfies

\[
 \|y\|_{\ell^2}\le\kappa_L\|y\|_{G_L},
\qquad
 \kappa_L=R^{o(1)},
\tag{L-15628.34}
\]

then restriction of `C_L` to `W_L` retains the bound

\[
 \mathfrak M_R
 \le R^{1/4+o(1)}.
\tag{L-15628.35}
\]

The harmonic lift metrics in the current finite packets contain the ordinary
finite coefficient norm as a positive block; the exact normalization must be
checked in production.

## 10. What this closes and what it does not

This theorem closes the former **algebraic and unwhitened conditioning** problem
for the complete finite Fourier range. It is stronger than generic finite
surjectivity and substantially smaller than the pointwise Möbius-prefix bound.

It does not prove a uniform lower bound for the omitted-tail Gram of this
cardinal frame. An exact source frame can be unwhitened-well-conditioned while
its tail Gram degenerates in a zero-invisible direction. The safe use of
`C_L` is therefore as an exact correction of a prolate/global-anchor core whose
tail Gram is already uniformly positive; this is `L-15629`.

## 11. Proof boundary

- The support-avoidance measure estimate is elementary from Riemann–von
  Mangoldt.
- The zeta lower bound imports the standard local product lemma with its exact
  strip normalization; an independent review should check the pole/gamma
  bookkeeping.
- The Mellin-cardinal and guard-mode interpolation are exact finite algebra.
- The final endpoint/profile exponent uses the declared logarithmic-to-
  multiplicative norm transport and the fixed-order ledger of `L-16221`.
- No tail-Gram floor and no RH conclusion are asserted by this lemma alone.
