# L-91310 — The Brownian reflection form is the integrated Fisher covariance of the exponential-tilt path

Claim ID: `L-91310`  
Status: **PROVED EXACT TWO-COPY/FISHER IDENTITY; COVARIANCE SIGN OPEN**  
Created: 2026-08-12  
Depends on: `L-91106`, `L-91309`  
RH status: **unproved**

## 1. Exponential-tilt family

Let `Z` be the symmetric half-size-biased BPY log-range variable, normalized by

\[
 M(u)=\mathbb E[e^{uZ}]
 =\frac{\xi(1/2+u)}{\xi(1/2)}.
\]

For real `u` with `|u|<1/2`, define the tilted one-copy law

\[
 dP_u(z)=\frac{e^{uz}}{M(u)}dP_0(z).
\tag{L-91310.1}
\]

Let `P_u^(2)=P_u tensor P_u`.  Since `Z` is symmetric,

\[
 M(-u)=M(u).
\tag{L-91310.2}
\]

For two copies put

\[
 S=Z_1+Z_2,
 \qquad
 \Delta=Z_1-Z_2.
\]

Then

\[
 \frac{dP_u^{(2)}}{dP_0^{(2)}}
 =\frac{e^{uS}}{M(u)^2}.
\tag{L-91310.3}
\]

## 2. Reflection observable

For an exponential polynomial

\[
 F(x)=\sum_jc_je^{r_jx},
 \qquad r_j>0,
\]

define

\[
 \boxed{
 \mathcal A_F(S,\Delta)
 =\int_{-S/2}^{S/2}
  \overline{F(x+\Delta/2)}F(x-\Delta/2)dx,
 }
\tag{L-91310.4}

with the oriented convention for `S<0`.

`L-91106` gives the Brownian reflection quadratic

\[
 \mathcal R_a(F)
 =\mathbb E_0^{(2)}
  [\sinh(aS)\mathcal A_F(S,\Delta)].
\tag{L-91310.5}

## 3. Difference of two completed tilts

Using (L-91310.3),

\[
\begin{aligned}
 2\mathcal R_a(F)
 &\!=\mathbb E_0^{(2)}
   [(e^{aS}-e^{-aS})\mathcal A_F]\\
 &\!=M(a)^2
   \left(
    \mathbb E_a^{(2)}\mathcal A_F
    -\mathbb E_{-a}^{(2)}\mathcal A_F
   \right).
\end{aligned}
\tag{L-91310.6}

Hence

\[
 \boxed{
 \mathcal R_a(F)
 =\frac{M(a)^2}{2}
  \left(
   \mathbb E_a^{(2)}\mathcal A_F
   -\mathbb E_{-a}^{(2)}\mathcal A_F
  \right).
 }
\tag{L-91310.7}

The Pick quadratic is the difference of one observable under two opposite
completed-zeta tilts.

## 4. Fisher covariance formula

For any integrable observable `H` independent of the tilt parameter,

\[
 \frac d{du}\mathbb E_u^{(2)}H
 =\operatorname{Cov}_u^{(2)}(H,S).
\tag{L-91310.8}

Indeed the score of `P_u^(2)` is

\[
 S-2m_u,
 \qquad
 m_u=\mathbb E_u Z.
\]

Integrating (L-91310.8) from `-a` to `a` and using
(L-91310.7) gives

\[
 \boxed{
 \mathcal R_a(F)
 =\frac{M(a)^2}{2}
  \int_{-a}^{a}
  \operatorname{Cov}_u^{(2)}
  (\mathcal A_F,S)\,du.
 }
\tag{L-91310.9}

This is the exact Fisher-path representation of the Brownian reflection form.

## 5. Symmetry reduction

Under simultaneous reflection

\[
 (S,\Delta,u)\longmapsto(-S,-\Delta,-u),
\]

the tilted two-copy law is invariant after changing `u` to `-u`, and

\[
 \mathcal A_F(-S,-\Delta)
 =-\overline{\mathcal A_F(S,\Delta)}
\]

for real coefficient data, with the corresponding polarized identity in the
complex case.  Consequently the real quadratic may be written as twice the
real part of the positive-half tilt integral:

\[
 \boxed{
 \mathcal R_a(F)
 =M(a)^2\int_0^a
  \operatorname{Re}\operatorname{Cov}_u^{(2)}
  (\mathcal A_F,S)du.
 }
\tag{L-91310.10}

The remaining sign is therefore a monotone-response statement along the
positive exponential family.

## 6. Dirichlet-form target

Let `L_u` be any reversible generator for `P_u^(2)` with carré du champ
`Gamma_u`.  On centered observables,

\[
 \operatorname{Cov}_u(H,S)
 =\mathcal E_u
  \left(H,(-L_u)^{-1}(S-2m_u)\right),
\tag{L-91310.11}

where `mathcal E_u(f,g)=E_u Gamma_u(f,g)`.

For the BPY Gamma--Beta realization, `L-91107/L-91302` provide an explicit
positive beta component whose local direction is

\[
 \partial_\Delta-	anh\Delta\partial_S.
\]

Thus a constructive closing theorem can now be stated without an abstract DtN
map:

> Find an explicit solution `h_u` of the score Poisson equation
> \[
> -L_uh_u=S-2m_u
> \]
> in the Gamma--Beta/theta reservoir and prove
> \[
> \operatorname{Re}\mathcal E_u(\mathcal A_F,h_u)\ge0
> \]
> for every exponential polynomial `F` and `0<u<1/2`.

Integrated in `u`, this is exactly the desired Brownian reflection positivity.

## 7. Relation to the fixed-density Fisher source

The one-copy tilt `P_u` is the probability family of `L-91309`.  Its tangent
vector is

\[
 -\frac12(Z-m_u)q_u.
\]

Equation (L-91310.9) therefore identifies the Brownian Pick form as the
integrated response of the reflection observable to that exact fixed-space
Fisher tangent.  The Brownian and Suzuki/Fisher fronts are two observations of
the same completed source path.

## 8. Proof boundary

```text
two-copy opposite-tilt difference                 EXACT
Fisher covariance representation                  EXACT
positive-half symmetry reduction                  EXACT
Gamma--Beta local positive direction              EXACT
score Poisson solution with favorable cross energy OPEN / RH-BEARING
Brownian reflection positivity                    OPEN
Riemann Hypothesis                                UNPROVED
```
