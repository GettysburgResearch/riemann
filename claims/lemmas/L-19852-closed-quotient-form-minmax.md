# L-19852 — Closed quotient forms preserve a one-dimensional low index on a dense source range

Claim ID: `L-19852`  
Status: **PROVED ABSTRACT CLOSED-FORM THEOREM UNDER THE DECLARED MINIMAL-LIFT HYPOTHESIS**  
Authoring agent: `gpt56-pro-09-q`  
Created: 2026-08-07  
Dependencies: closed quadratic forms; Courant--Fischer min--max; quotient Hilbert spaces  
Scope: functional-analytic engine for the projection-free localized-Weil route

## 1. Setup

Let `(U,G)` and `(H,\langle\cdot,\cdot\rangle_H)` be Hilbert spaces. Let `D` be a densely defined, closed, nonnegative quadratic form on `U`. Let

\[
 S:\operatorname{Dom}D\to H
\]

be linear with dense range and suppose

\[
 \|Su\|_H^2\le K\|u\|_G^2
\tag{L-19852.1}
\]

on `Dom D`.

Define the lower-semicontinuous quotient form

\[
 \boxed{
 \overline D(v)
 =\inf\left\{
 \liminf_{j\to\infty}D(u_j):
 Su_j\to v\text{ in }H
 \right\}.}
\tag{L-19852.2}
\]

Assume:

1. `overline D` is proper and closed;
2. after quotienting the zero-energy kernel, every `v in Dom overline D` has a unique `D`-minimal lift `Jv`;
3. the lift map
   \[
   J:\operatorname{Dom}\overline D\to\operatorname{Dom}D
   \]
   is linear and satisfies
   \[
   SJv=v,\qquad D(Jv)=\overline D(v).
   \tag{L-19852.3}
   \]

These properties hold, for example, when the completion of `Dom D/ker S` in the `D`-norm is a Hilbert space and the induced map into `H` is closed. They are stated explicitly because minimization in the `D+G` norm would not in general minimize `D` itself.

## 2. Low-index transfer

Suppose for some `b>0` and scale `d>0`,

\[
 \dim\mathbf1_{[0,bd)}
 \bigl(G^{-1/2}DG^{-1/2}\bigr)\le1.
\tag{L-19852.4}
\]

Let `W` be any two-dimensional subspace of `Dom overline D`. Since `J` is linear and injective, `JW` is two-dimensional. Let `E_<` be the source spectral subspace below `bd`; by (L-19852.4), `dim E_<=1`. Hence there exists nonzero

\[
 u\in JW\cap E_<^{\perp_G}.
\]

Put `v=Su`. Then

\[
 D(u)\ge bd\|u\|_G^2,
\]

while (L-19852.1) gives

\[
 \|v\|_H^2\le K\|u\|_G^2.
\]

Using (L-19852.3),

\[
 \frac{\overline D(v)}{\|v\|_H^2}
 =\frac{D(u)}{\|Su\|_H^2}
 \ge\frac bK d.
\]

Every two-dimensional subspace contains such a vector. Therefore

\[
 \boxed{
 \theta_2(\overline D,H)
 \ge\frac bK d.}
\tag{L-19852.5}
\]

Here `theta_2` is the second min--max value of the selfadjoint operator associated to the closed form `overline D`.

## 3. Target upper bound

Let `u_* in Dom D` satisfy

\[
 D(u_*)\le a d_*\|u_*\|_G^2
\tag{L-19852.6}
\]

and

\[
 \|Su_*\|_H^2\ge k\|u_*\|_G^2.
\tag{L-19852.7}
\]

Put `v_*=Su_*`. The defining infimum gives

\[
 \overline D(v_*)\le D(u_*),
\]

and hence

\[
 \boxed{
 \frac{\overline D(v_*)}{\|v_*\|_H^2}
 \le\frac ak d_*.}
\tag{L-19852.8}
\]

Combining with (L-19852.5),

\[
 \boxed{
 \frac{R_{\overline D}(v_*)}{\theta_2(\overline D,H)}
 \le\frac{aK}{bk}\frac{d_*}{d}.}
\tag{L-19852.9}
\]

## 4. Relative form transfer

Let `Q` be a closed lower-bounded form on `H` with the same domain as `overline D`. If

\[
 \boxed{
 (1-\eta)c\,\overline D
 \preceq Q-\sigma H
 \preceq(1+\eta)c\,\overline D,}
\tag{L-19852.10}
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
\tag{L-19852.11}
\]

When this tends to zero, the ground line is simple and converges projectively to the target line.

## 5. Application interface

For the localized Weil programme:

```text
U                 exact arithmetic-radical source reservoir;
S                 localization to [lambda^-1,lambda];
D                 ordinary omitted-support tail energy;
H                 localized L2 metric;
overline D         minimum tail energy among radical extensions;
Q                 closed localized Weil form.
```

At a non-zeta-cycle support the source range is dense. If the quotient form has the minimal-lift realization above, and if the signed source-tail hierarchy and relative local-Weyl inequality hold, the complete localized operator—not merely a finite Fourier compression—has a simple prolate ground state.

## 6. Proof boundary

- The min--max theorem is exact under the explicitly declared minimal-lift hypothesis.
- Establishing that hypothesis for the Connes--Consani source relation is a separate closability theorem; it is not silently inferred from dense range.
- The theorem does not prove the signed tail hierarchy or the relative localized-Weil comparison.
- It eliminates finite Fourier projection from the composition once those analytic inputs are supplied.
- No RH conclusion is claimed by this lemma alone.
