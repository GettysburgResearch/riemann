# L-19852 — Closed quotient forms preserve a one-dimensional low index on a dense source range

Claim ID: `L-19852`  
Status: **PROVED ABSTRACT CLOSED-FORM THEOREM**  
Authoring agent: `gpt56-pro-09-q`  
Created: 2026-08-07  
Dependencies: closed quadratic forms; Courant--Fischer min--max; quotient Hilbert spaces  
Scope: functional-analytic engine for the projection-free localized-Weil route

## 1. Setup

Let `(U,G)` and `(H,\langle\cdot,\cdot\rangle_H)` be Hilbert spaces. Let `D` be a densely defined, closed, nonnegative quadratic form on `U`. Let

\[
 S:U\to H
\]

be linear with dense range and suppose

\[
 \|Su\|_H^2\le K\|u\|_G^2
\tag{L-19852.1}
\]

on `Dom D`.

Let

\[
 \mathcal N=\{u\in\operatorname{Dom}D:Su=0\}.
\]

Complete `Dom D/\mathcal N` in the norm

\[
 \|[u]\|_{D+G}^2
 :=\inf_{n\in\mathcal N}
 \bigl(D(u+n)+\|u+n\|_G^2\bigr).
\tag{L-19852.2}
\]

Assume the induced map into `H` is closable. Its closed graph defines a lower-semicontinuous quotient form `\overline D` on `H` by

\[
 \boxed{
 \overline D(v)
 =\inf\left\{
 \liminf_{j\to\infty}D(u_j):
 Su_j\to v\text{ in }H
 \right\}.}
\tag{L-19852.3}
\]

This definition is independent of a source basis and remains meaningful when the source range is dense but not closed.

## 2. Minimal-lift realization

Let `\mathscr U` be the quotient completion in (L-19852.2). After dividing out the zero-energy kernel, the closed map

\[
 \widetilde S:\mathscr U\to H
\]

has dense range. Every `v` in the form domain of `\overline D` has a unique lift of minimal `D+G` norm in

\[
 (\ker\widetilde S)^{\perp_{D+G}}.
\]

For that lift `u_v`,

\[
 \overline D(v)=D(u_v).
\tag{L-19852.4}
\]

The lift depends linearly on `v`. Thus every finite-dimensional subspace of `Dom \overline D` has a finite-dimensional space of minimal lifts of the same dimension.

## 3. Low-index transfer

Suppose for some `b>0` and scale `d>0`,

\[
 \dim\mathbf1_{[0,bd)}
 \bigl(G^{-1/2}DG^{-1/2}\bigr)\le1.
\tag{L-19852.5}
\]

Let `W` be any two-dimensional subspace of `Dom \overline D`. Its minimal-lift space `\widetilde W` is two-dimensional. Let `E_<` be the source spectral subspace below `bd`; by (L-19852.5), `dim E_<=1`. Hence there exists nonzero

\[
 u\in\widetilde W\cap E_<^{\perp_G}.
\]

For `v=Su`,

\[
 D(u)\ge bd\|u\|_G^2,
\]

while (L-19852.1) gives

\[
 \|v\|_H^2\le K\|u\|_G^2.
\]

Therefore

\[
 \frac{\overline D(v)}{\|v\|_H^2}
 \ge\frac bK d.
\]

Every two-dimensional subspace contains such a vector, so

\[
 \boxed{
 \theta_2(\overline D,H)
 \ge\frac bK d.}
\tag{L-19852.6}
\]

Here `theta_2` is the second min--max value of the selfadjoint operator associated to the closed form `\overline D`; the statement remains valid if the value lies below the essential spectrum.

## 4. Target upper bound

Let `u_*\in\operatorname{Dom}D` satisfy

\[
 D(u_*)\le a d_*\|u_*\|_G^2
\tag{L-19852.7}
\]

and

\[
 \|Su_*\|_H^2\ge k\|u_*\|_G^2.
\tag{L-19852.8}
\]

Put `v_*=Su_*`. By the defining infimum,

\[
 \boxed{
 \frac{\overline D(v_*)}{\|v_*\|_H^2}
 \le\frac ak d_*.}
\tag{L-19852.9}
\]

Combining with (L-19852.6),

\[
 \boxed{
 \frac{R_{\overline D}(v_*)}{\theta_2(\overline D,H)}
 \le\frac{aK}{bk}\frac{d_*}{d}.}
\tag{L-19852.10}
\]

## 5. Relative form transfer

Let `Q` be a closed lower-bounded form on `H` with the same domain as `\overline D`. If

\[
 \boxed{
 (1-\eta)c\,\overline D
 \preceq Q-\sigma H
 \preceq(1+\eta)c\,\overline D,}
\tag{L-19852.11}
\]

with `c>0` and `0<=eta<1`, then:

1. `Q\succeq\sigma H`;
2. the target Rayleigh excess over `sigma` is at most
   \[
   (1+\eta)c\,(a/k)d_*;
   \]
3. the second spectral value above `sigma` is at least
   \[
   (1-\eta)c\,(b/K)d.
   \]

Thus the target-to-gap ratio is bounded by

\[
 \boxed{
 \frac{1+\eta}{1-\eta}
 \frac{aK}{bk}\frac{d_*}{d}.}
\tag{L-19852.12}
\]

When this tends to zero, the ground line is simple and converges projectively to the target line.

## 6. Application interface

For the localized Weil programme:

```text
U                 exact arithmetic-radical source reservoir;
S                 localization to [lambda^-1,lambda];
D                 ordinary omitted-support tail energy;
H                 localized L2 metric;
overline D         minimum tail energy among radical extensions;
Q                 closed localized Weil form.
```

At a non-zeta-cycle support the source range is dense. If the signed source-tail hierarchy and the relative local-Weyl inequality are proved on the closed quotient, the complete localized operator—not merely a finite Fourier compression—has a simple even prolate ground state.

## 7. Proof boundary

- The quotient construction and min--max statements are abstract functional analysis.
- The theorem does not prove closability for a particular source realization; that must be checked in the declared source graph norm.
- It does not prove the signed tail hierarchy or the relative localized-Weil comparison.
- It eliminates finite Fourier projection from the logical composition once those two analytic inputs are supplied.
- No RH conclusion is claimed by this lemma alone.
