# L-91902 — The safe Xi flow has an exact Cauchy-covariant bounded-real identity

Claim ID: `L-91902`  
Status: **PROVED EXACT DIFFERENTIAL IDENTITY; DISSIPATIVE CONNECTION OPEN**  
Created: 2026-08-13  
Depends on: `L-91901`  
RH status: **unproved**

## 1. A moving metric and multiplier

Let `C(u)` be a `C1` path of strictly positive Hermitian matrices and let
`D(u)` be a `C1` matrix path.  Put

\[
 \boxed{
 P=C-D^*CD.
 }
 \tag{L-91902.1}

Thus `P>=0` says that `D` is contractive in the moving `C` metric.

A connection `Gamma(u)` is metric compatible when

\[
 \boxed{
 C'=\Gamma^*C+C\Gamma.
 }
 \tag{L-91902.2}

One canonical choice is

\[
 \boxed{
 \Gamma_0=\frac12C^{-1}C'.
 }
 \tag{L-91902.3}

Every other compatible connection is `Gamma_0+Omega`, where

\[
 \Omega^*C+C\Omega=0.
 \tag{L-91902.4}

The skew term is the gauge freedom of the moving metric.

## 2. Covariant derivative of the multiplier

Define

\[
 \boxed{
 \nabla D
 =D'+\Gamma D-D\Gamma.
 }
 \tag{L-91902.5}

Then the following identity is exact:

\[
 \boxed{
 P'-\Gamma^*P-P\Gamma
 =-\Big[
  (\nabla D)^*CD
  +D^*C(\nabla D)
 \Big].
 }
 \tag{L-91902.6
}

### Proof

Differentiate `P=C-D*CD` and use (L-91902.2):

\[
\begin{aligned}
P'={}&C'
 -D'^*CD-D^*C'D-D^*CD'\\
={}&\Gamma^*C+C\Gamma
 -D'^*CD-D^*(\Gamma^*C+C\Gamma)D-D^*CD'.
\end{aligned}
\]

Subtracting

\[
 \Gamma^*P+P\Gamma
 =\Gamma^*C+C\Gamma
  -\Gamma^*D^*CD-D^*CD\Gamma
\]

and regrouping gives (L-91902.6).

## 3. Covariant bounded-real lemma

Suppose

\[
 \boxed{
 \mathcal R_\Gamma
 :=-\Big[
  (\nabla D)^*CD+D^*C(\nabla D)
 \Big]
 \succeq0
 }
 \tag{L-91902.7
}

for every `u` in an interval, and `P(u_0)>=0`.  Then

\[
 \boxed{P(u)\succeq0\qquad(u\ge u_0).}
 \tag{L-91902.8}

Indeed let `U'=-Gamma U`, `U(u_0)=I`.  Equation (L-91902.6) gives

\[
 \frac d{du}(U^*PU)
 =U^*\mathcal R_\Gamma U\succeq0.
 \tag{L-91902.9}

This is a finite-dimensional moving-metric Kalman--Yakubovich--Popov identity.
It propagates contractivity from a lossless or contractive initial section.

## 4. Safe Xi specialization

For the safe-real packet of `L-91901`, put

\[
 c=1+u,
 \qquad
 (C_u)_{ij}=\frac1{c+q_i+q_j},
 \tag{L-91902.10}

\[
 (S_u)_{ij}=\frac1{(c+q_i+q_j)^2},
 \qquad
 C_u'=-S_u,
 \tag{L-91902.11}

and

\[
 D_u=\operatorname{diag}\left(
  \frac{\xi(1+q_i)}{\xi(1+u+q_i)}
 \right).
 \tag{L-91902.12}

Let

\[
 L_u=\operatorname{diag}\left(
  \frac{\xi'}{\xi}(1+u+q_i)
 \right).
 \tag{L-91902.13}

Then

\[
 \boxed{D_u'=-L_uD_u.}
 \tag{L-91902.14}

With the canonical Cauchy connection

\[
 \boxed{
 \Gamma_u^{\rm C}
 =-\frac12C_u^{-1}S_u,
 }
 \tag{L-91902.15}

one has

\[
 \boxed{
 \nabla^{\rm C}D_u
 =-L_uD_u
  +\Gamma_u^{\rm C}D_u
  -D_u\Gamma_u^{\rm C}.
 }
 \tag{L-91902.16}

Every entry in (L-91902.16) is a finite expression in rational Cauchy data and
safe values of `xi'/xi` to the right of one.

The exact differential Pick identity is also

\[
 \boxed{
 P_u'
 =D_uS_uD_u-S_u
  +L_uD_uC_uD_u
  +D_uC_uD_uL_u.
 }
 \tag{L-91902.17}

## 5. The actual connection problem

The canonical connection (L-91902.15) is only the metric connection.  The
completed arithmetic system has additional skew connection data from:

```text
returned Euler states;
gamma/pole motion;
the compact dyadic bridge;
Hardy reflection and compressed-delay leakage;
the finite completed safe-jet connection.
```

Such data may enter through a `C`-skew gauge `Omega_u`.  The precise
conclusion-producing target is therefore to construct explicitly

\[
 \Gamma_u=\Gamma_u^{\rm C}+\Omega_u,
 \qquad
 \Omega_u^*C_u+C_u\Omega_u=0,
 \tag{L-91902.18}

from the declared source ports and prove

\[
 \boxed{
 \mathcal R_{\Gamma_u}\succeq0.
 }
 \tag{L-91902.19
}

Then `P_0=0` and (L-91902.8) give every safe-real Pick matrix.

## 6. Scope firewall

Positivity of the target path does not force the simple canonical remainder
`R_(Gamma^C)` to be positive pointwise.  `R-91901` supplies an exact rational
control.  Thus (L-91902.19) is a **source-specific completed connection
problem**, not a generic consequence of a moving contraction.

## 7. Exact boundary

```text
moving-metric differential identity                 EXACT
covariant bounded-real propagation                  EXACT
safe Cauchy metric and Xi derivative                EXACT
canonical metric connection                         EXPLICIT
canonical pointwise dissipation                     NOT AUTOMATIC
completed source-ordered skew connection             OPEN
completed covariant dissipation                     OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVED
```
