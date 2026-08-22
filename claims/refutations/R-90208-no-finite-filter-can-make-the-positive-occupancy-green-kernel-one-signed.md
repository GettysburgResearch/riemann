# R-90208 — No nonzero finite scale filter can make the universal positive-occupancy Green kernel one-signed

Claim ID: `R-90208`  
Status: **PROPOSED COMPLETE EXACT REFUTATION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: positive-source Green identity `L-90015/L-90016` on PR #353; elementary Laplace transforms  
Scope: every finite endpoint-scale filter, including the factor-64 family; no statement about source-specific arithmetic cancellation and no RH claim

## 1. Universal positive-source kernel

For every nonnegative arithmetic weight `lambda`, `L-90016` gives

\[
 -F_\lambda(e^t)
 =\int_0^t h(t-u)\,\mathcal Q_\lambda(u)\,du,
 \qquad
 h(a)=1-\frac a2,
 \tag{R-90208.1}
\]

where

\[
 \mathcal Q_\lambda(u)\ge0.
\]

Extend `h` by zero to negative ages:

\[
 h_+(a)=\left(1-\frac a2\right)\mathbf1_{a\ge0}.
 \tag{R-90208.2}
\]

Fix any scale step `L>0` and any nonzero finite polynomial

\[
 P(y)=\sum_{j=0}^{d}c_jy^j.
 \tag{R-90208.3}
\]

Applying the corresponding endpoint filter gives the universal age kernel

\[
 \boxed{
 K_P(a)=\sum_{j=0}^{d}c_jh_+(a-jL).
 }
 \tag{R-90208.4}
\]

Indeed

\[
 -\sum_{j=0}^{d}c_jF_\lambda(e^{t-jL})
 =\int_0^t K_P(t-u)\mathcal Q_\lambda(u)\,du.
 \tag{R-90208.5}
\]

Thus a source-blind proof based only on `mathcal Q_lambda>=0` would require
`K_P` to have one sign.

## 2. Critical exponential neutrality

For every real `z>0`,

\[
 \int_0^\infty h_+(a)e^{-za}\,da
 =\frac1z-\frac1{2z^2}
 =\frac{z-1/2}{z^2}.
 \tag{R-90208.6}
\]

Translation therefore gives the exact filtered transform

\[
 \boxed{
 \int_0^\infty K_P(a)e^{-za}\,da
 =P(e^{-zL})\frac{z-1/2}{z^2}.
 }
 \tag{R-90208.7}
\]

At the critical source exponent,

\[
 \boxed{
 \int_0^\infty K_P(a)e^{-a/2}\,da=0.
 }
 \tag{R-90208.8}
\]

for **every** finite filter `P`, independently of its coefficients, roots,
annulus size, or zero-safety properties.

This is the exact transform form of PR #353's observation that a pure critical
exponential source is neutral.

## 3. Universal one-sign filtering is impossible

A nonzero function which is everywhere nonnegative has strictly positive
integral against the strictly positive weight `e^{-a/2}`. Likewise a nonzero
everywhere nonpositive function has strictly negative integral. Equation
(R-90208.8) therefore implies that `K_P` cannot be one-signed unless it vanishes
identically.

But a nonzero finite filter cannot give `K_P identically 0`: let `j_0` be its
smallest index with `c_(j_0)!=0`. On a sufficiently short interval immediately
to the right of `j_0L`, the first active translated kernel contributes the
nonzero affine term

\[
 c_{j_0}\left(1-\frac{a-j_0L}{2}\right),
\]

so the filtered kernel is not identically zero.

Hence

\[
 \boxed{
 P\ne0
 \quad\Longrightarrow\quad
 K_P\text{ takes both positive and negative values.}
 }
 \tag{R-90208.9}
\]

This theorem is stronger than a no-go for the preferred factor-64 polynomial:
it excludes **every finite scale filter** from converting positivity of the
occupancy source alone into a one-sided endpoint theorem.

## 4. Annular filters and compact support

If

\[
 P(1)=P'(1)=0,
 \tag{R-90208.10}
\]

then the filtered kernel is compactly supported. Indeed, once every delay is
active,

\[
\begin{aligned}
 K_P(a)
 &=\sum_jc_j\left(1-\frac{a-jL}{2}\right)\\
 &=P(1)\left(1-\frac a2\right)+\frac L2P'(1)=0.
\end{aligned}
 \tag{R-90208.11}
\]

This covers the compact annular filters of PR #352. Equation (R-90208.8) then
says even more geometrically: the compact kernel has exactly zero critical
exponential mass, so positive and negative lobes are compulsory.

No optimization of the coefficients can remove this sign change while
retaining a nontrivial finite filter.

## 5. Preferred factor-64 member

Take `L=log 2` and the unscaled preferred polynomial of `L-90023`,

\[
 P_{64}^*(y)
 =(1-y)^2(1-y/\sqrt2)(1+y)(1+\tfrac34y+y^2).
 \tag{R-90208.12}
\]

Its kernel is therefore forced to change sign before any arithmetic source is
inserted. Direct piecewise evaluation gives three age sectors:

```text
positive near age 0,
negative on the middle annulus,
positive again near the oldest dyadic ages,
```

and returns to zero after age `6 log 2` because of (R-90208.10).

The sign changes are not a defect of the chosen `3/4` coefficient. They are a
consequence of the universal zero moment (R-90208.8), so every alternative
finite factor-64 dressing has the same source-blind obstruction.

## 6. What remains possible

The theorem refutes only the strategy

```text
positive occupancy source
+
finite scale filter
+
pointwise sign of the filtered Green kernel
=> RH criterion.
```

It does **not** say the filtered endpoint scalar itself lacks a sign. A proof
may still exploit arithmetic timing inside the positive source, for example:

- the strict between-integer decrease and prime-power jumps of `R_Lambda`;
- a stochastic/convex-order comparison of source ages;
- source-specific cancellation between the positive and negative lobes;
- the exact signed prime-power flux of `L-90021`;
- a nonlocal martingale or ordered-transport argument.

Thus the factor-64 and positive-occupancy routes remain alive, but their final
step must use more than `mathcal Q_lambda>=0`.

## 7. Proof boundary

Proved exactly:

1. the universal filtered Green kernel;
2. its complete Laplace transform;
3. the critical exponential zero moment for every finite filter;
4. compulsory sign change for every nonzero finite filter;
5. compact support under the usual annular double-root conditions.

Not proved:

- a sign or asymptotic for the arithmetic convolution against the true prime or
  prime-power source;
- the preferred factor-64 endpoint inequality;
- RH.
