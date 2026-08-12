# L-91319 — The Brownian Fisher covariance is a positive Gaussian bulk plus one explicit Stein-kernel variability defect

Claim ID: `L-91319`  
Status: **PROVED EXACT STEIN NORMAL FORM; SOURCE-SPECIFIC DEFECT DOMINATION OPEN**  
Created: 2026-08-12  
Depends on: `L-91310`  
RH status: **unproved**

## 1. Canonical Stein kernel of the completed tilt

Fix a real tilt

\[
 |u|<\frac12
\]

and let `p_u` be the density of the completed BPY/Riemann variable `Z` under
`P_u`.  Put

\[
 m_u=\mathbb E_uZ,
 \qquad
 V_u=\operatorname{Var}_u(Z).
\]

The canonical one-dimensional Stein kernel is

\[
 \boxed{
 \tau_u(z)
 =\frac1{p_u(z)}
  \int_z^\infty(y-m_u)p_u(y)dy.
 }
\tag{L-91319.1}
\]

Under the double-exponential completed density, the boundary terms vanish and

\[
 \boxed{
 \mathbb E_u[(Z-m_u)g(Z)]
 =\mathbb E_u[\tau_u(Z)g'(Z)]
 }
\tag{L-91319.2}
\]

for every smooth test in the natural energy domain.

The numerator in (L-91319.1) is nonnegative, so

\[
 \tau_u(z)\ge0.
\tag{L-91319.3}
\]

Taking `g(z)=z` gives

\[
 \boxed{
 \mathbb E_u\tau_u(Z)=V_u.
 }
\tag{L-91319.4}
\]

## 2. Product Stein identity

Let `Z_1,Z_2` be independent under `P_u tensor P_u` and put

\[
 S=Z_1+Z_2.
\]

For any differentiable two-copy observable `H`, applying (L-91319.2)
conditionally in each coordinate gives

\[
\boxed{
 \operatorname{Cov}_u^{(2)}(H,S)
 =\mathbb E_u^{(2)}[
  \tau_u(Z_1)\partial_1H
  +\tau_u(Z_2)\partial_2H
 ].
}
\tag{L-91319.5}
\]

This is the explicit score-Poisson solution requested abstractly in
`L-91310`: the one-copy potential has derivative `tau_u`.

## 3. Sum derivative of the reflection observable

For an arbitrary complex exponential polynomial or smooth test `F`, retain

\[
 \mathcal A_F
 =\int_{-S/2}^{S/2}
  \overline{F(x+\Delta/2)}F(x-\Delta/2)dx,
 \qquad
 \Delta=Z_1-Z_2.
\]

Differentiation in the common translation direction gives the exact boundary
identity

\[
\boxed{
 (\partial_1+\partial_2)\mathcal A_F
 =\overline{F(Z_1)}F(Z_2)
  +\overline{F(-Z_2)}F(-Z_1).
}
\tag{L-91319.6}
\]

No integral remainder occurs in this direction.

## 4. Positive constant-Stein bulk

Center the Stein kernel:

\[
 \delta\tau_u(z)=\tau_u(z)-V_u.
\tag{L-91319.7}
\]

Substituting `tau_u=V_u+delta tau_u` into (L-91319.5) yields

\[
\begin{aligned}
 \operatorname{Cov}_u^{(2)}(\mathcal A_F,S)
 ={}&V_u\mathbb E_u^{(2)}
 [ (\partial_1+\partial_2)\mathcal A_F ]\\
 &+\mathcal D_u(F),
\end{aligned}
\tag{L-91319.8}
\]

where

\[
 \boxed{
 \mathcal D_u(F)
 =\mathbb E_u^{(2)}[
  \delta\tau_u(Z_1)\partial_1\mathcal A_F
  +\delta\tau_u(Z_2)\partial_2\mathcal A_F
 ].
 }
\tag{L-91319.9}
\]

Independence and (L-91319.6) give

\[
\boxed{
 \mathbb E_u^{(2)}
 [ (\partial_1+\partial_2)\mathcal A_F ]
 =|\mathbb E_uF(Z)|^2
  +|\mathbb E_uF(-Z)|^2.
}
\tag{L-91319.10}
\]

Therefore

\[
\boxed{
\begin{aligned}
 \operatorname{Re}
 \operatorname{Cov}_u^{(2)}(\mathcal A_F,S)
 ={}&V_u\Big(
  |\mathbb E_uF(Z)|^2
  +|\mathbb E_uF(-Z)|^2
 \Big)\\
 &+\operatorname{Re}\mathcal D_u(F).
\end{aligned}}
\tag{L-91319.11}
\]

The first line is an explicit positive rank-two bulk.

For a Gaussian completed source, the Stein kernel is constant, `delta tau=0`,
and the full Fisher covariance is automatically nonnegative for every complex
`F`.  Thus every non-Gaussian difficulty is concentrated in (L-91319.9).

## 5. Quantitative defect bound

Vector-valued Cauchy--Schwarz gives

\[
\begin{aligned}
 |\mathcal D_u(F)|
 &\le
 \left(
  \mathbb E[(\delta\tau_1)^2+(\delta\tau_2)^2]
 \right)^{1/2}\\
 &\quad\times
 \left(
  \mathbb E[|\partial_1\mathcal A_F|^2
            +|\partial_2\mathcal A_F|^2]
 \right)^{1/2}.
\end{aligned}
\]

Hence

\[
 \boxed{
 |\mathcal D_u(F)|
 \le
 \sqrt{2\operatorname{Var}_u(\tau_u(Z))}\,
 \mathfrak E_u(F)^{1/2},
 }
\tag{L-91319.12}
\]

where

\[
 \mathfrak E_u(F)
 =\mathbb E_u^{(2)}[
  |\partial_1\mathcal A_F|^2
  +|\partial_2\mathcal A_F|^2
 ].
\tag{L-91319.13}
\]

A sufficient instantaneous closing inequality is therefore

\[
\boxed{
 V_u\Big(
  |\mathbb E_uF(Z)|^2+|\mathbb E_uF(-Z)|^2
 \Big)
 \ge
 \sqrt{2\operatorname{Var}_u(\tau_u(Z))}\,
 \mathfrak E_u(F)^{1/2}.
}
\tag{L-91319.14}
\]

## 6. Exact relationship with the monotone cone

For nonnegative nondecreasing real `F`, `L-91314` proves the complete covariance
is nonnegative without estimating the defect separately.  In that sector the
coordinate derivative signs force the sum of bulk and defect to be favorable.

For arbitrary complex `F`, equation (L-91319.11) shows precisely what is lost:
there is still a universal positive bulk, but the variable Stein weight may
couple to the antisymmetric/interference derivatives.

Thus the open problem is no longer an unspecified Brownian reflection sign.
It is a source-specific control of the fluctuation

\[
 \tau_u(Z)-\operatorname{Var}_u(Z).
\]

## 7. Gamma--Beta/theta route

`L-91107/L-91302` provide a reversible Gamma--Beta realization and a positive
local direction

\[
 \partial_\Delta-	anh\Delta\partial_S.
\]

The canonical one-dimensional Stein potential above is the marginal score
solution.  A successful theta/Gamma--Beta proof may close (L-91319.14) by:

```text
bounding the Stein-kernel variance from the positive theta curvature;
rewriting the defect as a Gamma--Beta carré-du-champ cross term;
showing the rank-two boundary bulk dominates that cross term;
or proving a sharper source-specific operator inequality than Cauchy--Schwarz.
```

## 8. Integrated Brownian criterion

By `L-91310`,

\[
 \mathcal R_a(F)
 =M(a)^2\int_0^a
  \operatorname{Re}
  \operatorname{Cov}_u^{(2)}(\mathcal A_F,S)du.
\]

Therefore a proof of (L-91319.14), or merely an integrated domination of the
negative part of `D_u`, proves the target Pick quadratic.

## 9. Proof boundary

```text
canonical completed Stein kernel                  EXACT POSITIVE
product score/Stein identity                       EXACT
translation derivative boundary square             EXACT
positive Gaussian rank-two bulk                    EXACT
Stein-variability defect                           EXACT
quantitative defect bound                          EXACT
source-specific defect domination                  OPEN / RH-BEARING
full Brownian reflection/Pick positivity            OPEN
Riemann Hypothesis                                 UNPROVED
```
