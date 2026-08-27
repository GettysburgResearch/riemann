# L-105432 — Complete critical sign forces Xi-derivative real-rootedness by a finite-strip Lindelof principle

Claim ID: `L-105432`  
Status: **PROVED XI-SPECIFIC CONDITIONAL ANALYTIC THEOREM — ASSUMES THE COMPLETE CRITICAL SIGN; INDEPENDENT HOSTILE REVIEW REQUIRED**  
Created: 2026-08-24  
Depends on: `L-105430--L-105431`; the real-entire parity of the Xi derivative ladder  
RH status: **not assumed**

## 1. Statement

Fix `r>=0` and put

\[
F(z)=\Xi^{(r)}(z),
\qquad
G(z)=F'(z)=\Xi^{(r+1)}(z),
\qquad
m(z)={F(z)\over G(z)}.
\]

Assume:

1. every zero of `G` is real;
2. every nonremovable zero of `G` is simple; and
3. at every such critical point,

   \[
   \boxed{
   \rho_c={F(c)\over F''(c)}\le0.
   }
   \tag{L-105432.1}
   \]

Common zeros are removable and may be treated by the confluent ledger. Then

\[
\boxed{
\operatorname{Im}{F(z)\over F'(z)}>0
\qquad(\operatorname{Im}z>0).
}
\tag{L-105432.2}

Consequently `F/F'` is a meromorphic Pick function, every zero of `F` is real,
and the complete boundary Loewner/Stieltjes/capacity hierarchy of
`L-105350--L-105417` is automatically positive.

In particular, for the Xi derivative ladder,

\[
\boxed{
\text{all critical points real and }
F(c)/F''(c)\le0
\Longrightarrow
F\text{ is real-rooted}.}
\tag{L-105432.3}

The theorem is a source-specific converse to Rolle at the exact sign level.

## 2. The upper safe boundary

Choose `H>H_r`, where `H_r` is supplied by `L-105430`. Then

\[
\boxed{
\operatorname{Im}m(x+iH)>0
\qquad(x\in\mathbb R).
}
\tag{L-105432.4}

Since every zero of `G` is real, `m` is holomorphic in the open strip

\[
\mathcal S_H=\{z:0<\operatorname{Im}z<H\}.
\]

Put

\[
u(z)=\operatorname{Im}m(z).
\]

This is harmonic in `S_H`.

## 3. The lower boundary is nonnegative in the limiting sense

Away from the real zeros of `G`, the quotient is real on the real axis, so

\[
\lim_{y\downarrow0}u(x+iy)=0.
\]

At a simple nonremovable critical point,

\[
m(z)={\rho_c\over z-c}+h_c(z),
\]

where `h_c` is holomorphic and real on the real axis. Hence

\[
\operatorname{Im}m(x+iy)
={-\rho_c\,y\over(x-c)^2+y^2}+O_c(y).
\tag{L-105432.5}
\]

The leading term is nonnegative by (L-105432.1). Therefore, on every fixed
compact real interval,

\[
\boxed{
\inf_x u(x+i\varepsilon)
\ge-\delta(\varepsilon),
\qquad
\delta(\varepsilon)\longrightarrow0
}
\tag{L-105432.6}
\]

as `epsilon downarrow 0`. Removable common zeros contribute only the `O(y)`
term. This formulation avoids deleting pole semicircles.

## 4. Cofinal vertical sides

By `L-105431`, there is a cofinal sequence `X_n->infinity` such that

\[
\boxed{
M_n:=
\sup_{0\le y\le H}
\max\{|m(X_n+iy)|,|m(-X_n+iy)|\}
\le
\exp\!\left(C\log X_n\log\log(3+X_n)\right).
}
\tag{L-105432.7}

Thus

\[
\boxed{
\log M_n=o(X_n).}
\tag{L-105432.8}

This is the only growth information required at infinity.

## 5. Exponentially small harmonic measure of the sides

Fix one point `z_0=x_0+iy_0` in `S_H`. For `epsilon<y_0`, let

\[
R_{n,\varepsilon}
=\{z:|\operatorname{Re}z|<X_n,
       \varepsilon<\operatorname{Im}z<H\}.
\]

Let `omega_(n,epsilon)` be the harmonic measure at `z_0` of the union of the
two vertical sides of this rectangle. Separation of variables for a rectangle
gives

\[
\boxed{
\omega_{n,\varepsilon}(z_0)
\le
C_{z_0,H}
\exp\!\left[
-{\pi(X_n-|x_0|)\over H-\varepsilon}
\right].
}
\tag{L-105432.9}

For example, the right-side harmonic measure has the sine-series expansion

\[
\sum_{j\ \mathrm{odd}}
{4\over j\pi}
{\sinh(j\pi(x+X_n)/(H-\varepsilon))
 \over
 \sinh(2j\pi X_n/(H-\varepsilon))}
\sin {j\pi(y-\varepsilon)\over H-\varepsilon},
\]

and the left side is its reflection. Bounding the first geometric tail gives
(L-105432.9).

## 6. Lindelof rectangle argument

On the top edge of `R_(n,epsilon)`, `u>=0` by (L-105432.4). On the bottom edge,
`u>=-delta_(n)(epsilon)` by (L-105432.6), where for fixed `n`,

\[
\delta_n(\varepsilon)\longrightarrow0.
\]

On the vertical sides,

\[
u\ge-M_n.
\]

Let `omega` denote the side harmonic measure inside the rectangle. The harmonic
function

\[
u+\delta_n(\varepsilon)+M_n\omega
\]

has nonnegative boundary values. The minimum principle therefore gives

\[
\boxed{
u(z_0)
\ge
-\delta_n(\varepsilon)
-M_n\omega_{n,\varepsilon}(z_0).
}
\tag{L-105432.10}

First let `epsilon downarrow 0`. Then use (L-105432.8)--(L-105432.9) and let
`n->infinity`. The exponential harmonic-measure decay beats the subexponential
side growth, so

\[
u(z_0)\ge0.
\]

Since `z_0` was arbitrary,

\[
\operatorname{Im}m(z)\ge0
\qquad(0<\operatorname{Im}z<H).
\]

Together with `L-105430`, the same holds in the complete upper half-plane.
The quotient is nonconstant, so the strong minimum principle gives the strict
inequality (L-105432.2).

## 7. Real-rootedness and the capacity hierarchy

If `F(z_*)=0` for one point in the open upper half-plane, then `G(z_*)` is
nonzero because every zero of `G` is real. Hence

\[
m(z_*)=0,
\]

contradicting the strict Pick inequality. Schwarz reflection excludes zeros in
the lower half-plane. Thus every zero of `F` is real.

The Herglotz representation from `L-105417` now applies:

\[
\widehat m_F(z)
=az+
\sum_{c>0}
\left(-{2\rho_c\over c^2}\right)
{z\over1-z^2/c^2},
\qquad a\ge0.
\tag{L-105432.11}

Every finite-window boundary remainder is the positive affine atom plus the
positive critical atoms omitted by that window. Therefore all ordinary and
shifted Stieltjes matrices and all real-packet Loewner matrices are positive.

## 8. Why this does not contradict the finite-window Schur split

At a finite packet, the residue pivots and boundary remainder are independent
inertia blocks. The present theorem does not derive one block from the other
by finite linear algebra. It uses four global Xi-specific facts:

```text
positive safe half-plane from completed-zeta asymptotics;
fixed-strip gamma decay;
real-zero paired Hadamard product for the derivative;
subexponential good-side growth.
```

These facts force the boundary block through a Lindelof exhaustion. Abstract
entire functions without this infinity control remain subject to the two-gate
firewall.

## 9. Scope

The complete critical-point reality and sign hypothesis remains open at the
low Xi level. Multiple nonremovable critical points require a confluent version
whose local lower-bound statement replaces (L-105432.5). The theorem does not
verify the proposed moving-saddle terminal endpoint and does not by itself
prove RH.
