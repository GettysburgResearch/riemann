# L-91314 — Brownian reflection positivity holds for every nonnegative nondecreasing real test

Claim ID: `L-91314`  
Status: **PROVED EXACT MONOTONE-CONE THEOREM; ARBITRARY SIGN/PHASE INTERFERENCE OPEN**  
Created: 2026-08-12  
Depends on: `L-91310`, `L-91313`  
RH status: **unproved**

## 1. Test class

Fix

\[
 0<a<\frac12.
\]

Let `F:R->R` be locally absolutely continuous and satisfy

\[
 \boxed{
 F(x)\ge0,
 \qquad
 F'(x)\ge0
 \quad\text{for almost every }x.
 }
\tag{L-91314.1}

Assume the moments needed below are finite under every two-copy completed-zeta
tilt `P_u tensor P_u`, `|u|<=a`.  For example it is enough that `F` and `F'`
have exponential growth strictly inside the BPY moment strip.

A common complex phase `e^(i theta)F` gives the same quadratic observable, so
the theorem also covers that class.

## 2. Reflection observable in the original coordinates

Let `Z_1,Z_2` be the two BPY log-range copies and put

\[
 S=Z_1+Z_2,
 \qquad
 \Delta=Z_1-Z_2.
\]

The reflection observable is

\[
 \mathcal A_F(S,\Delta)
 =\int_{-S/2}^{S/2}
 F(x+\Delta/2)F(x-\Delta/2)dx,
\tag{L-91314.2}
\]

with oriented integration when `S<0`.

Set

\[
 y=x+\Delta/2.
\]

Then

\[
 \boxed{
 \mathcal A_F(Z_1,Z_2)
 =\int_{-Z_2}^{Z_1}
 F(y)F(y-Z_1+Z_2)dy.
 }
\tag{L-91314.3}
\]

This formula remains valid with the oriented convention.

## 3. Exact coordinate derivatives

Differentiation of (L-91314.3), followed by one integration by parts, gives

\[
\boxed{
\begin{aligned}
 \partial_{Z_1}\mathcal A_F
 ={}&F(-Z_1)F(-Z_2)\\
 &+\int_{-Z_2}^{Z_1}
 F'(y)F(y-Z_1+Z_2)dy,
\end{aligned}}
\tag{L-91314.4}
\]

and directly

\[
\boxed{
\begin{aligned}
 \partial_{Z_2}\mathcal A_F
 ={}&F(-Z_1)F(-Z_2)\\
 &+\int_{-Z_2}^{Z_1}
 F(y)F'(y-Z_1+Z_2)dy.
\end{aligned}}
\tag{L-91314.5}
\]

When `S>=0`, both integrals are nonnegative, so both derivatives are
nonnegative.

## 4. The reversed-orientation case

Assume `S<0`, so `Z_1<-Z_2`.  Put

\[
 G(y)=F(y)F(y-Z_1+Z_2).
\]

Since `F,F'>=0`,

\[
 G'(y)
 =F'(y)F(y-Z_1+Z_2)
  +F(y)F'(y-Z_1+Z_2)
 \ge0.
\tag{L-91314.6}
\]

Therefore

\[
\begin{aligned}
 &\int_{Z_1}^{-Z_2}
 F'(y)F(y-Z_1+Z_2)dy\\
 &\qquad\le
 G(-Z_2)-G(Z_1)\\
 &\qquad=
 F(-Z_2)F(-Z_1)-F(Z_1)F(Z_2).
\end{aligned}
\tag{L-91314.7}
\]

Using the reversed orientation in (L-91314.4),

\[
 \boxed{
 \partial_{Z_1}\mathcal A_F
 \ge F(Z_1)F(Z_2)\ge0.
 }
\tag{L-91314.8}
\]

The complementary term in `G'` gives in the same way

\[
 \boxed{
 \partial_{Z_2}\mathcal A_F
 \ge F(Z_1)F(Z_2)\ge0.
 }
\tag{L-91314.9}
\]

Consequently, without any restriction on the sign of `S`,

\[
 \boxed{
 (Z_1,Z_2)\longmapsto\mathcal A_F(Z_1,Z_2)
 \text{ is nondecreasing in each coordinate.}
 }
\tag{L-91314.10}
\]

## 5. Product association and the Fisher covariance

For `0<=u<=a`, the tilted copies are independent under

\[
 P_u^{(2)}=P_u\otimes P_u.
\]

If `g` is increasing and integrable and `Z'` is an independent copy of `Z`,
then

\[
 2\operatorname{Cov}(g(Z),Z)
 =\mathbb E[(g(Z)-g(Z'))(Z-Z')]\ge0.
\tag{L-91314.11}
\]

Conditioning on the other coordinate and using (L-91314.10) gives

\[
 \operatorname{Cov}_u^{(2)}(\mathcal A_F,Z_1)\ge0,
 \qquad
 \operatorname{Cov}_u^{(2)}(\mathcal A_F,Z_2)\ge0.
\tag{L-91314.12}
\]

Hence

\[
 \boxed{
 \operatorname{Cov}_u^{(2)}(\mathcal A_F,S)\ge0
 \qquad(0\le u\le a).
 }
\tag{L-91314.13}
\]

This is the instantaneous completed Fisher-response inequality.

## 6. Brownian reflection positivity

`L-91310` proves the exact identity

\[
 \mathcal R_a(F)
 =M(a)^2\int_0^a
  \operatorname{Re}
  \operatorname{Cov}_u^{(2)}(\mathcal A_F,S)du.
\]

The covariance in (L-91314.13) is real and nonnegative. Therefore

\[
 \boxed{
 \mathcal R_a(F)\ge0.
 }
\tag{L-91314.14}
\]

Thus the Brownian/Xi Pick quadratic is unconditionally positive on the full
cone of nonnegative nondecreasing real tests, subject only to moment
integrability.

## 7. Relation to the positive Laplace cone

Every positive Laplace mixture

\[
 F(x)=\int_0^\infty e^{rx}d\mu(r),
 \qquad \mu\ge0,
\]

belongs to the class (L-91314.1).  Hence `L-91313` is a source-resolved
subtheorem of the present monotone-cone result.  Its atomwise formula remains
useful because it identifies precisely how arbitrary coefficient phases break
coordinate monotonicity.

## 8. Exact surviving obstruction

The full Pick criterion permits arbitrary complex exponential polynomials.
Their real and imaginary parts need not be nonnegative or monotone, and the
Hermitian cross terms need not have a fixed coordinate sign.

Therefore the remaining problem is not the diagonal Brownian response.  It is
exactly the extension from the monotone cone to its complex linear span while
retaining all interference terms.

A decomposition `F=F_+-F_-` does not close the problem: the cross reflection
form between `F_+` and `F_-` has no sign supplied by (L-91314.14).

## 9. Proof boundary

```text
coordinate representation of the reflection observable  EXACT
monotonicity for S>=0                                  EXACT
reversed-orientation monotonicity                      EXACT
product-association Fisher covariance sign             EXACT
Brownian reflection positivity                         EXACT ON MONOTONE CONE
arbitrary complex sign/phase interference               OPEN / RH-BEARING
full Pick kernel                                        OPEN
Riemann Hypothesis                                      UNPROVED
```
