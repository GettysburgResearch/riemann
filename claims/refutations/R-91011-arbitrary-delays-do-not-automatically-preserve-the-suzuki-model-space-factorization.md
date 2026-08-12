# R-91011 — Arbitrary boundary delays do not automatically preserve the Suzuki model-space Fisher factorization

Claim ID: `R-91011`  
Status: **EXACT SCOPE CORRECTION / METHOD FIREWALL**  
Created: 2026-08-12  
Corrects: the unqualified delay statement in `L-91316.18` and its proof-boundary summary  
RH status: **unproved**

## 1. Exact theorem retained

`L-91316` proves, for every

\[
 g\in K_{\Theta_a},
\]

the exact completed Fisher--Hankel factorization

\[
 \boxed{
 \mathcal J_a
 =a\sqrt{2\operatorname{Var}_a(Y)}\,
  \mathcal C_a\mathcal A_a,
 }
\tag{R-91011.1}
\]

where

\[
 (\mathcal A_ag)(Y)
 =P_+\left[
  h_{a,\cdot}(Y)\overline{\Theta_a}g
 \right].
\tag{R-91011.2}
\]

The proof uses the load-bearing model-space fact

\[
 \overline{\Theta_a}g\in H^2_-.
\tag{R-91011.3}
\]

Consequently the one-scale model-space domination

\[
 \mathcal J_a^*\mathcal J_a
 \preceq
 2a^2\operatorname{Var}_a(Y)
 \mathcal A_a^*\mathcal A_a
\tag{R-91011.4}
\]

is retained exactly.

## 2. The overreach

The first version of `L-91316.18` stated that one may replace `g` by

\[
 D_\tau g
\]

for an arbitrary boundary delay or modulation `D_tau` and retain the same
factorization automatically.

This is not justified.  In general,

\[
 \boxed{
 D_\tau K_{\Theta_a}
 \not\subseteq K_{\Theta_a}.
 }
\tag{R-91011.5}
\]

Equivalently,

\[
 \overline{\Theta_a}D_\tau g
\]

need not belong to `H^2_-`.  Therefore the step using (R-91011.3) cannot be
repeated after an arbitrary modulation.

No property of the scalar Fisher feature `h_(a,t)` repairs this missing
invariance.

## 3. What polarization is automatic

For any finite packet

\[
 g_1,\ldots,g_N\in K_{\Theta_a},
\]

linearity of (R-91011.1) retains every cross term:

\[
 \left\|
  \mathcal J_a\sum_jc_jg_j
 \right\|^2
 \le
 2a^2\operatorname{Var}_a(Y)
 \left\|
  \mathcal A_a\sum_jc_jg_j
 \right\|^2.
\tag{R-91011.6}
\]

Thus full polarization **inside the model space** is closed.

A delayed physical test may first be mapped or projected into a vector
`g_(x,tau)` in `K_Theta`; once that membership is proved, all cross-delay terms
between such resident vectors are retained by (R-91011.6).  What is not closed
is the claim that raw delay is a symmetry of the model space.

## 4. Correct delayed target

The repaired delayed theorem must construct an explicit family

\[
 \boxed{
 \mathcal D_{a,\tau}:
 \mathcal H_{\rm physical}
 \longrightarrow K_{\Theta_a}
 }
\tag{R-91011.7}
\]

such that:

```text
physical delay/orientation is represented exactly;
the image lies in the Suzuki model space;
all carrier, delay and orientation cross terms agree;
the Fisher-Hankel source norm dominates the joint image;
the finite bridge coordinate is included.
```

Alternatively one may prove an intertwining relation between delay and the
model-space compression.  Either construction is additional mathematics.

## 5. Correct proof boundary

```text
one-scale model-space Fisher-Hankel factorization     EXACT
full polarization among resident model-space vectors  EXACT
arbitrary modulation preserves K_Theta                FALSE IN GENERAL
automatic raw cross-delay factorization                WITHDRAWN
delayed physical-to-model-space intertwiner            OPEN
bridge and two-sided source comparison                 OPEN / RH-BEARING
Riemann Hypothesis                                     UNPROVED
```
