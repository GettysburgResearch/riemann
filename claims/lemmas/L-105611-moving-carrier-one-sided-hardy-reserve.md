# L-105611 — The one-sided Hardy gap survives the exact moving carrier with one scalar drift debt

Claim ID: `L-105611`  
Status: **PROVED EXACT OPERATOR REDUCTION**  
Created: 2026-08-24  
Depends on: `L-105422`, `L-105610`  
RH status: **not assumed**

## 1. One-sided source operators

Use the setup of `L-105610`. Put

\[
\ell=\Re L(s),
\qquad \tau=\Im L(s),
\qquad
\Delta=\ell-A(\sigma)>0.
\tag{L-105611.1}
\]

Let `S_x` be the right translation by `x` in a one-sided frame of length
`R`. For each Laplace parameter `u`, define

\[
\mathscr B_u
=\sum_{n\ge1}c_u(n)n^{-\sigma}S_{\log n},
\tag{L-105611.2}
\]

\[
\mathscr C_u
=\sum_{n\ge1}c_u(n)(1+h\log n)n^{-\sigma}S_{\log n}.
\tag{L-105611.3}
\]

Their source masses are

\[
B_u^\#=\sum_nc_u(n)n^{-\sigma}=e^{uA(\sigma)},
\tag{L-105611.4}
\]

\[
A_u^\#=\sum_nc_u(n)(1+h\log n)n^{-\sigma}.
\tag{L-105611.5}
\]

The actual moving-carrier operator corresponding to `q-hq'` is

\[
\boxed{
\mathscr Q_{s,h,R}
=\int_0^\infty e^{-u\ell}e^{-iu\tau}
\bigl(\mathscr C_u+h uL'(s)\mathscr B_u\bigr)\,du.
}
\tag{L-105611.6}
\]

Put

\[
\mathscr A_{s,h}
=\int_0^\infty e^{-u\ell}A_u^\#\,du.
\tag{L-105611.7}
\]

## 2. Phase-uniform gap before integration

`L-105422` applies to every real global phase. Therefore, at each `u`,

\[
\boxed{
A_u^\# I-
\Re\bigl(e^{-iu\tau}\mathscr C_u\bigr)
\succeq
\Gamma_R(u)I,
}
\tag{L-105611.8}
\]

where

\[
\boxed{
\Gamma_R(u)
\ge {2\over9R^2}
\sum_{n\ge1}c_u(n)(1+h\log n)n^{-\sigma}
\min\{(\log n)^2,R^2\}.
}
\tag{L-105611.9}
\]

The phase `-u tau` need not be frozen or approximated because the theorem is
uniform in that phase.

## 3. Exact integrated reserve

The carrier-drift operator satisfies

\[
\|h uL'(s)\mathscr B_u\|
\le h u|L'(s)|B_u^\#.
\tag{L-105611.10}
\]

Integrating (L-105611.8) and using (L-105611.10) gives

\[
\boxed{
\mathscr A_{s,h}I-\Re\mathscr Q_{s,h,R}
\succeq
\bigl(\Gamma^{\rm mov}_{s,h,R}
      -\mathcal E^{\rm drift}_{s,h}\bigr)I,
}
\tag{L-105611.11}
\]

with

\[
\Gamma^{\rm mov}_{s,h,R}
=\int_0^\infty e^{-u\ell}\Gamma_R(u)\,du,
\tag{L-105611.12}
\]

and the explicit scalar debt

\[
\boxed{
\mathcal E^{\rm drift}_{s,h}
\le
h|L'(s)|
\int_0^\infty u e^{-u\Delta}\,du
={h|L'(s)|\over\Delta^2}.
}
\tag{L-105611.13}
\]

No operator-valued carrier error remains.

## 4. Positive real-carrier resolvent form

Define nonnegative coefficients `r_ell(n)` by

\[
\boxed{
{1\over\ell-A(w)}
=\sum_{n\ge1}r_\ell(n)n^{-w}.
}
\tag{L-105611.14}
\]

Coefficientwise,

\[
r_\ell(n)
=\int_0^\infty e^{-u\ell}c_u(n)\,du.
\tag{L-105611.15}
\]

Fubini in (L-105611.9) yields the explicit lower bound

\[
\boxed{
\Gamma^{\rm mov}_{s,h,R}
\ge {2\over9R^2}
\sum_{n\ge1}r_\ell(n)(1+h\log n)n^{-\sigma}
\min\{(\log n)^2,R^2\}.
}
\tag{L-105611.16}
\]

Thus the moving complex carrier is replaced, without approximation, by:

```text
one positive real-carrier resolvent reserve;
one scalar drift debt h|L'|/Delta^2.
```

## 5. Scope

This theorem is an operator reserve before the final physical trace or
restriction. It does not assert pointwise positivity of `Re(q-hq')`; arbitrary
translation phases remain. It removes the carrier-freezing layer from
`DMPXFER105603` and replaces the archimedean drift ledger by the single scalar
quantity in (L-105611.13).