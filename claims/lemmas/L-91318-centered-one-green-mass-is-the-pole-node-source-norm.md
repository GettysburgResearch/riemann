# L-91318 — The centered one-Green total mass is the exact pole-node arithmetic source scalar

Claim ID: `L-91318`  
Status: **EXACT SAFE-SOURCE IDENTIFICATION; MODEL-SPACE TANGENT MAP REMAINS OPEN**  
Created: 2026-08-12  
Depends on: main `L-9506`, `L-91316/L-91317`  
RH status: **unproved**

## 1. Completed one-Green factorization

For `0<s<1`, put

\[
 \mathcal H_s(q)
 =\frac1q\frac{\xi(1+q)}{\xi(1+s+q)}
 =R_s(q)B_s(q)Z_s(q),
 \tag{L-91318.1}
\]

where

\[
 R_s(q)=\frac{q+1}{(q+s)(q+s+1)},
 \tag{L-91318.2}
\]

\[
 B_s(q)=\pi^{s/2}
 \frac{\Gamma((1+q)/2)}
      {\Gamma((1+s+q)/2)},
 \tag{L-91318.3}
\]

and

\[
 Z_s(q)=\frac{\zeta(1+q)}{\zeta(1+s+q)}.
 \tag{L-91318.4}
\]

Let

\[
 c_s=\frac1{\zeta(1+s)}.
 \tag{L-91318.5}
\]

The centered regular channel is

\[
 \mathcal G_s(q)
 =R_s(q)B_s(q)
  \left[Z_s(q)-\frac{c_s}{q}\right]
 =\int_0^\infty e^{-qt}Y_s(t)\,dt.
 \tag{L-91318.6}
\]

## 2. Exact pole expansion

The Laurent expansion at `q=0` is

\[
 \zeta(1+q)=\frac1q+\gamma+O(q),
 \tag{L-91318.7}
\]

and

\[
 \frac1{\zeta(1+s+q)}
 =c_s\left[
 1-q\frac{\zeta'}{\zeta}(1+s)+O_s(q^2)
 \right].
 \tag{L-91318.8}
\]

Therefore

\[
 \boxed{
 Z_s(q)-\frac{c_s}{q}
 =c_s\left[
 \gamma-\frac{\zeta'}{\zeta}(1+s)
 \right]+O_s(q).
 }
 \tag{L-91318.9}
\]

## 3. Completed pole amplitude

At `q=0`,

\[
 R_s(0)B_s(0)c_s
 =\frac{\pi^{s/2}\Gamma(1/2)}
        {s(s+1)\Gamma((1+s)/2)\zeta(1+s)}.
 \tag{L-91318.10}
\]

Using the completed-zeta definition,

\[
 \boxed{
 R_s(0)B_s(0)c_s
 =\frac{\xi(1)}{\xi(1+s)}
 =\frac1{2\xi(1+s)}
 =:A_s^{\rm pole}.
 }
 \tag{L-91318.11}
\]

This is exactly the pole-aligned scattering amplitude of `L-91316` with
`s=2a`.

## 4. Exact centered total mass

Letting `q downarrow0` in (L-91318.6),

\[
 \boxed{
 \mathcal G_s(0)
 =A_s^{\rm pole}
 \left[
 \gamma-\frac{\zeta'}{\zeta}(1+s)
 \right].
 }
 \tag{L-91318.12}
\]

Equivalently, whenever the inverse-Laplace integral is read in the natural
finite-part sense,

\[
 \boxed{
 \int_0^\infty Y_s(t)\,dt
 =A_s^{\rm pole}
 \left[
 \gamma-\frac{\zeta'}{\zeta}(1+s)
 \right]>0.
 }
 \tag{L-91318.13}
\]

For `s=2a`, normalization by the pole amplitude gives

\[
 \boxed{
 \frac{\mathcal G_{2a}(0)}{A_{2a}^{\rm pole}}
 =F(a)
 =\gamma-\frac{\zeta'}{\zeta}(1+2a).
 }
 \tag{L-91318.14}
\]

This is exactly the pole-normalized finite part of `L-91316/L-91317`.

## 5. Exact positive innovation telescope

Combining with `L-91317`,

\[
 \boxed{
 \frac{\mathcal G_{2a}(0)}{A_{2a}^{\rm pole}}
 -
 \frac{\mathcal G_{4a}(0)}{A_{4a}^{\rm pole}}
 =\int_0^\infty t\,d\nu_{a,1+2a}(t)>0.
 }
 \tag{L-91318.15}
\]

Thus the complete source-side scalar at the pole node has:

```text
an explicit completed amplitude;
an explicit finite centered mass;
an exact positive prime-jump innovation;
a coefficient-one dyadic telescope;
a terminal value gamma.
```

## 6. Minimal remaining map

The arithmetic scalar in the pole-aligned one-node theorem is no longer
unspecified. The remaining theorem is to construct the completed tangent map

\[
 \Phi_a^{\rm arith}
 \longmapsto
 k_{\eta_a}^{\rm crit}
 \oplus k_{\eta_a}^{\rm stable}
 \oplus k_{\eta_a}^{\rm hyp}
 \tag{L-91318.16}
\]

with source norm

\[
 \|\Phi_a^{\rm arith}\|^2
 =A_{2a}^{\rm pole}F(a)
 \tag{L-91318.17}
\]

and then prove that the first two output norms already exhaust it. The exact
model ledger would force the hyperbolic component to vanish.

The model-space identification in (L-91318.16), not the source scalar, is the
sole remaining RH-bearing interface.

## 7. Firewall

The positivity of the total centered mass does not imply positivity of the
centered density `Y_s(t)` and does not by itself imply RH. A planted symmetric
factor can preserve safe scalar positivity while leaving a nonzero crossed-zero
port. The completed tangent/isometry is indispensable.
