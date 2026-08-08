# L-28101 — Fixed-dyadic top dipole and opposite-parity factorization

Claim ID: `L-28101`  
Title: The complete top Möbius source is stably equivalent to a fixed opposite-parity source convolved with one reciprocal-free residual fiber  
Status: **PROPOSED COMPLETE EXACT ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #281  
Dependencies: PR #266 `L-25801`; PR #269 `L-26901`; elementary Dirichlet convolution  
Scope: coefficient range `n<=X<=V^K`; no boundary-commutator estimate

## 1. Top source

Retain

\[
r_V=\varepsilon-\mathbf1*\mu_V,
\qquad
\mu_{>V}=\mu-\mu_V,
\]

and

\[
\boxed{
T_{K,V}=\Lambda*r_V^{*(K-1)}.
}
\tag{L-28101.1}
\]

Since

\[
r_V=\mathbf1*\mu_{>V}
\]

and

\[
\Lambda=\mu*\ell,
\qquad
\ell(n)=\log n,
\]

one has globally

\[
T_{K,V}
=
\mu*\ell*\mathbf1^{*(K-1)}*
\mu_{>V}^{*(K-1)}.
\tag{L-28101.2}
\]

This is the prime-anchored normal form of PR #266.

## 2. Reciprocal-free common fiber

Define

\[
\boxed{
H_{K,V}
=
\ell*\mathbf1^{*(K-1)}*
\mu_{>V}^{*(K-1)}.
}
\tag{L-28101.3}
\]

Then

\[
\boxed{T_{K,V}=\mu*H_{K,V}.}
\tag{L-28101.4}
\]

In Dirichlet-series notation put

\[
M_V(s)=\sum_{n\le V}\frac{\mu(n)}{n^s},
\qquad
R_V(s)=1-\zeta(s)M_V(s).
\]

Since

\[
\sum_{n>V}\frac{\mu(n)}{n^s}
=
\frac{R_V(s)}{\zeta(s)},
\]

the fiber has the exact series

\[
\boxed{
H_{K,V}(s)
=
-\zeta'(s)R_V(s)^{K-1}.
}
\tag{L-28101.5}
\]

It contains no reciprocal-zeta factor. At a zero of multiplicity `m`, it has
the zero order needed to leave the simple logarithmic-derivative pole of
`T_(K,V)` intact.

## 3. Fixed dyadic dipole

Put

\[
b_2=(\varepsilon-\delta_2)*\mu.
\tag{L-28101.6}
\]

Thus

\[
b_2(n)
=\mu(n)-\mathbf1_{2\mid n}\mu(n/2)
\]

and

\[
B_2(s)=\frac{1-2^{-s}}{\zeta(s)}.
\tag{L-28101.7}
\]

Define

\[
\boxed{
D_{2;K,V}
=(\varepsilon-\delta_2)*T_{K,V}.
}
\tag{L-28101.8}
\]

Equations (L-28101.4)--(L-28101.7) give the exact source factorization

\[
\boxed{
D_{2;K,V}=b_2*H_{K,V}.
}
\tag{L-28101.9}
\]

At the series level,

\[
D_{2;K,V}(s)
=
-(1-2^{-s})\frac{\zeta'}{\zeta}(s)
R_V(s)^{K-1}.
\tag{L-28101.10}
\]

The factor `1-2^-s` has zeros only on `Re s=0`, so it does not cancel a zeta
zero in the critical strip.

## 4. Opposite-parity fixed source

Define

\[
\boxed{
\omega_2
=(\varepsilon-\tfrac12\delta_2)*b_2
=
\mu-\frac32\delta_2*\mu+\frac12\delta_4*\mu.
}
\tag{L-28101.11}
\]

Its Dirichlet series is

\[
\boxed{
\Omega_2(s)
=
\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}.
}
\tag{L-28101.12}
\]

Put

\[
\boxed{
S_{K,V}
=(\varepsilon-\tfrac12\delta_2)*D_{2;K,V}.
}
\tag{L-28101.13}
\]

Then

\[
\boxed{
S_{K,V}=\omega_2*H_{K,V}.
}
\tag{L-28101.14}
\]

Thus every packet order has been separated into:

```text
one fixed RH-bearing opposite-parity source omega_2
times
one order-dependent reciprocal-free fiber H_(K,V).
```

The second finite factor `1-2^(-s-1)` has zeros only on `Re s=-1`.

## 5. Stable physical inverses

Let `tau_h` denote right translation by

\[
h=\log2
\]

on the square-root normalized logarithmic source field. Arithmetic convolution
by `delta_2` becomes

\[
2^{-1/2}\tau_h.
\]

Therefore

\[
\boxed{
\mathcal D_2
=(I-2^{-1/2}\tau_h)\mathcal T,
}
\tag{L-28101.15}
\]

and

\[
\boxed{
\mathcal S
=(I-2^{-3/2}\tau_h)\mathcal D_2.
}
\tag{L-28101.16}
\]

Both filters have causal `ell^1` inverses:

\[
\boxed{
\mathcal T
=\sum_{r\ge0}2^{-r/2}\tau_{rh}\mathcal D_2,
}
\tag{L-28101.17}
\]

\[
\boxed{
\mathcal D_2
=\sum_{r\ge0}2^{-3r/2}\tau_{rh}\mathcal S.
}
\tag{L-28101.18}
\]

Every sum is pointwise finite for a finite endpoint source and absolutely
summable on cumulative block energies.

For

\[
\mathcal A_F(J)=\int_{-\infty}^{J}|F(t)|^2dt,
\]

Minkowski gives

\[
\mathcal A_T(J)^{1/2}
\le
\frac1{1-2^{-1/2}}\mathcal A_{D_2}(J)^{1/2},
\tag{L-28101.19}
\]

and

\[
\mathcal A_{D_2}(J)^{1/2}
\le
\frac1{1-2^{-3/2}}\mathcal A_S(J)^{1/2}.
\tag{L-28101.20}
\]

The direct finite filters give the reverse comparisons with fixed constants.
Consequently

\[
\boxed{
\mathcal T,\ \mathcal D_2,\ \mathcal S
\text{ have the same cumulative-energy exponential exponent.}
}
\tag{L-28101.21}
\]

The same conclusion holds for fixed-length local blocks after replacing one
block by a fixed additive past envelope.

## 6. Interpretation

The scale-adapted radix of PR #266 is unnecessary and, by `R-28101`, vacuous.
The fixed dyadic filters are:

- nonvacuous;
- zero-safe;
- stably invertible;
- independent of `K`;
- exactly compatible with the parity-comb and factor-five source package.

They do not prove a contraction. They reduce the top-source problem to a fixed
source with an explicit common fiber.

## 7. Proof boundary

Closed exactly:

- the reciprocal-free fiber (L-28101.3)--(L-28101.5);
- the fixed dyadic factorization (L-28101.9);
- the opposite-parity factorization (L-28101.14);
- both stable causal recoveries;
- equality of exponential block-growth exponents.

Open:

- the physical boundary/commutator theorem for `omega_2*H_(K,V)`;
- the fibered factor-five recurrence;
- RH.
