# L-91015 — The exact gap between one-Green positivity and target Pick contractivity

Claim ID: `L-91015`  
Status: **EXACT FINITE-MATRIX NORMAL FORM / CORRECTED PROOF INTERFACE**  
Created: 2026-08-11  
Depends on: `L-9506`, `L-91014`  
RH status: **unproved**

## 1. Two different positive kernels

For `u>0`, write

\[
 H_u(q)=\frac1q\frac{\xi(1+q)}{\xi(1+u+q)},
 \qquad
 \vartheta_u(q)=qH_u(q).
\tag{L-91015.1}
\]

The unconditional one-Green theorem gives a positive measure `mu_u` such that

\[
 H_u(q)=\int_0^\infty e^{-qt}\,d\mu_u(t).
\tag{L-91015.2}
\]

Consequently

\[
 \boxed{
 G_{ij}=H_u\left(\frac{q_i+q_j}{2}\right)\succeq0.
 }
\tag{L-91015.3}
\]

This is a Hankel/Laplace Gram matrix.

The kernel required for horizontal Schur continuation is instead

\[
 \boxed{
 P_{ij}=
 \frac{1-\vartheta_u(q_i)\vartheta_u(q_j)}
      {1+u+q_i+q_j}.
 }
\tag{L-91015.4}
\]

There is no identity turning (L-91015.3) into (L-91015.4).

## 2. Exact contraction form

Put

\[
 C_{ij}=\frac1{1+u+q_i+q_j},
 \qquad
 D=\operatorname{diag}(\vartheta_u(q_1),\ldots,\vartheta_u(q_N)).
\tag{L-91015.5}
\]

Then

\[
 \boxed{P=C-DCD.}
\tag{L-91015.6}
\]

Since `C` is positive definite for distinct positive points,

\[
 P\succeq0
 \quad\Longleftrightarrow\quad
 \left\|C^{1/2}DC^{-1/2}\right\|\le1.
\tag{L-91015.7}
\]

Thus the missing theorem is an exact **Cauchy-space multiplier contraction**.
It is a Carleson/de Branges--Rovnyak statement, not positivity of the Laplace
feature measure in (L-91015.2).

In continuous form, `C` is the Gram matrix of

\[
 \phi_q(t)=e^{-(q+(1+u)/2)t}
\]

in `L^2(0,infinity)`.  Equation (L-91015.7) asks for an operator of norm at most
one satisfying

\[
 T^*\phi_q=\vartheta_u(q)\phi_q
\tag{L-91015.8}
\]

on every finite span.  Constructing this contraction for all safe `q` is already
equivalent, by `L-91014`, to the desired global Schur flow.

## 3. Infinitesimal gate

If `vartheta_u` is real on the safe ray, positivity of all two-point Pick matrices
implies the half-plane Schwarz--Pick inequality

\[
 \boxed{
 |\vartheta_u'(q)|
 \le
 \frac{1-\vartheta_u(q)^2}{1+u+2q}.
 }
\tag{L-91015.9}
\]

This is the first nontrivial local compatibility condition between the safe
values.  Complete monotonicity of `H_u=vartheta_u/q` does not imply it.

For the exact control `f_(u,y)` of `R-91005`, the one-Green function `f/q` is
completely monotone, yet

\[
 \frac{1-f(q)^2}{1+u+2q}-f'(q)
 =-\frac{16u(2y-u)(2y+u)}
 {[(1+2q+2u-2y)(1+2q+2u+2y)]^2}<0.
\tag{L-91015.10}
\]

So the failure occurs before any high-order analytic continuation issue.

## 4. Corrected full-proof target

A proof from safe Euler data may now be stated without ambiguity:

> For every positive rational `u`, every finite positive rational set
> `q_1,...,q_N`, prove
> \[
> C_u-D_{\vartheta_u}C_uD_{\vartheta_u}\succeq0.
> \]

Every matrix entry uses only

\[
 \xi(1+q_i),\qquad \xi(1+u+q_i),
\]

so no value is sampled in the critical strip.  `L-91014` then supplies the global
continuation and RH.  Conversely, `R-91005` shows that replacing this contraction
by separate positivity of the Jordan and one-Green feature kernels is invalid.

The most plausible non-circular interfaces are now:

```text
an exact colligation coupling the Jordan and beta/rational feature spaces;
a source-ordered proof of the Cauchy multiplier contraction;
a Loewner differential inequality in u whose initial kernel is zero and whose
  generator is manifestly completely positive;
a direct Schur-complement realization of C-DCD using the Euler--Bessel dilation.
```

No such coupling is proved here.

## 5. Boundary

```text
one-Green Hankel kernel                            UNCONDITIONALLY POSITIVE
safe target Pick kernel                            EXACT C-DCD FORM
Pick positivity                                    EQUIVALENT TO MULTIPLIER CONTRACTION
two-point infinitesimal Schwarz--Pick gate          EXACT
one-Green positivity -> Schwarz--Pick gate          REFUTED
actual-xi Cauchy multiplier contraction             OPEN / RH-EQUIVALENT
Riemann Hypothesis                                  UNPROVED
```
