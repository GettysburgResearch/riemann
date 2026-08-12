# L-91313 — Brownian reflection positivity holds unconditionally on the positive Laplace cone

Claim ID: `L-91313`  
Status: **PROVED EXACT POSITIVE-CONE SECTOR; FULL POLARIZED COEFFICIENT SPACE OPEN**  
Created: 2026-08-12  
Depends on: `L-91106`, `L-91310`  
RH status: **unproved**

## 1. The positive Laplace cone

Fix

\[
 0<a<\frac12.
\]

Let `mu` be a finite positive measure with compact support in `(0,infinity)` and
assume

\[
 a+\sup\operatorname{supp}\mu<\frac12.
\tag{L-91313.1}
\]

Define

\[
 \boxed{
 F(x)=e^{i\vartheta}
  \int_0^\infty e^{rx}d\mu(r).
 }
\tag{L-91313.2}
\]

The global phase cancels from every quadratic reflection observable.  Thus it
is enough to take `vartheta=0`.  Finite exponential polynomials with all
coefficients of one common phase and nonnegative magnitudes are the discrete
subcone of (L-91313.2).

## 2. Reflection observable in the two original copies

Let `Z_1,Z_2` be the two BPY log-range copies and put

\[
 S=Z_1+Z_2,
 \qquad
 \Delta=Z_1-Z_2.
\]

Retain

\[
 \mathcal A_F(S,\Delta)
 =\int_{-S/2}^{S/2}
  \overline{F(x+\Delta/2)}F(x-\Delta/2)dx.
\tag{L-91313.3}
\]

For two atoms `r,s>0`, direct integration gives

\[
\begin{aligned}
 &e^{(r-s)\Delta/2}
  \frac{2\sinh((r+s)S/2)}{r+s}\\
 &\qquad=
 \frac{
  e^{rZ_1+sZ_2}
  -e^{-sZ_1-rZ_2}
 }{r+s}.
\end{aligned}
\tag{L-91313.4}
\]

Therefore Tonelli's theorem yields the exact positive-mixture formula

\[
 \boxed{
 \mathcal A_F(Z_1,Z_2)
 =\iint
  \frac{
   e^{rZ_1+sZ_2}
   -e^{-sZ_1-rZ_2}
  }{r+s}
  d\mu(r)d\mu(s).
 }
\tag{L-91313.5}
\]

The displayed quantity is real.

## 3. Coordinatewise monotonicity

Differentiation under the finite positive measure gives

\[
\boxed{
 \partial_{Z_1}\mathcal A_F
 =\iint
  \frac{
   r e^{rZ_1+sZ_2}
   +s e^{-sZ_1-rZ_2}
  }{r+s}
  d\mu(r)d\mu(s)
 \ge0,
}
\tag{L-91313.6}
\]

and

\[
\boxed{
 \partial_{Z_2}\mathcal A_F
 =\iint
  \frac{
   s e^{rZ_1+sZ_2}
   +r e^{-sZ_1-rZ_2}
  }{r+s}
  d\mu(r)d\mu(s)
 \ge0.
}
\tag{L-91313.7}
\]

The inequalities are strict for nonzero `mu`.  Thus the complete reflection
observable is increasing in each BPY copy separately.  This is stronger than
monotonicity in the sum coordinate at fixed imbalance.

## 4. A self-contained product-association argument

Let `P_u` be the completed-zeta exponential tilt of `L-91310`, with

\[
 0\le u\le a.
\]

Under `P_u^(2)=P_u tensor P_u`, the variables `Z_1,Z_2` are independent.

For any increasing integrable one-variable function `g`, an independent copy
`Z'` gives

\[
 \boxed{
 2\operatorname{Cov}(g(Z),Z)
 =\mathbb E[(g(Z)-g(Z'))(Z-Z')]\ge0.
 }
\tag{L-91313.8}
\]

Conditioning on `Z_2` and using (L-91313.6),

\[
\begin{aligned}
 \operatorname{Cov}_u^{(2)}(\mathcal A_F,Z_1)
 &=\mathbb E_{Z_2}
   \operatorname{Cov}_{Z_1}
   (\mathcal A_F(\cdot,Z_2),Z_1)
 \ge0.
\end{aligned}
\tag{L-91313.9}
\]

The same argument with the coordinates exchanged gives

\[
 \operatorname{Cov}_u^{(2)}(\mathcal A_F,Z_2)\ge0.
\tag{L-91313.10}
\]

Consequently

\[
 \boxed{
 \operatorname{Cov}_u^{(2)}
 (\mathcal A_F,S)
 \ge0
 \qquad(0\le u\le a).
 }
\tag{L-91313.11}
\]

No log-concavity, total positivity, RH input or special property of the BPY
density beyond the required moments is used.  Independence and the positive
Laplace coefficients are sufficient.

## 5. Brownian reflection positivity on the cone

`L-91310` proves

\[
 \mathcal R_a(F)
 =M(a)^2\int_0^a
  \operatorname{Re}
  \operatorname{Cov}_u^{(2)}
  (\mathcal A_F,S)du.
\]

The covariance in (L-91313.11) is real and nonnegative.  Hence

\[
 \boxed{
 \mathcal R_a(F)\ge0
 }
\tag{L-91313.12}
\]

for every positive Laplace mixture satisfying (L-91313.1).

Equivalently, the Xi positive-real/Pick quadratic is unconditionally positive
for every finite exponential polynomial

\[
 F(x)=e^{i\vartheta}\sum_{j=1}^Nc_je^{r_jx},
 \qquad
 c_j\ge0,
 \qquad
 r_j>0,
 \qquad
 a+\max_jr_j<1/2.
\tag{L-91313.13}
\]

## 6. What remains outside the cone

The full Pick condition allows arbitrary complex coefficient vectors.  In
(L-91313.5), arbitrary polarization replaces the positive product measure
`dmu(r)dmu(s)` by the Hermitian coefficient kernel

\[
 d\overline\nu(r)d\nu(s),
\]

whose off-diagonal real parts may have either sign.  Coordinatewise monotonicity
then fails term by term.

Thus the remaining obstruction is now sharply identified as **phase and sign
interference between distinct Laplace atoms**, not the diagonal Brownian
response and not the positive-mixture sector.

Positivity on the union of positive cones does not imply positivity on their
linear span; cross terms must still be controlled.

## 7. Relation to the Gamma--Beta direction

For positive Laplace data, the score covariance is already nonnegative before
solving a Poisson equation.  In the Gamma--Beta realization, any solution
`h_u=(-L_u)^(-1)(S-2m_u)` therefore satisfies

\[
 \operatorname{Re}\mathcal E_u(\mathcal A_F,h_u)
 =\operatorname{Cov}_u^{(2)}(\mathcal A_F,S)
 \ge0
\]

on this cone.

The open score-Poisson theorem of `L-91310` is needed only to control the
interference sectors created by arbitrary coefficient phases.

## 8. Proof boundary

```text
positive Laplace-mixture representation          EXACT
coordinatewise monotonicity in both BPY copies    EXACT
product-association covariance sign               EXACT
instantaneous Fisher covariance positivity        EXACT ON CONE
Brownian reflection/Pick positivity               EXACT ON CONE
arbitrary complex coefficient interference        OPEN / RH-BEARING
full Pick kernel                                   OPEN
Riemann Hypothesis                                UNPROVED
```
