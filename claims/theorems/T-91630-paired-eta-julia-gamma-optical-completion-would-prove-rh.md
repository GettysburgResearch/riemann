# T-91630 — Paired-eta Julia–gamma optical completion would prove RH

Claim ID: `T-91630`  
Status: **FULL CONDITIONAL RH PROPOSAL / SOURCE-TO-MODEL EXHAUSTION OPEN**  
Created: 2026-08-12  
Depends on: `L-91630/L-91631`; `R-91630`; `T-91405/T-91530`  
RH status: **unproved**

## 1. Explicit arithmetic source

For `0<omega<1/2`, combine:

1. the hard paired-eta carrier space and its exact Julia decomposition into a
   safe returned state plus positive eta detail (`L-91630`);
2. the compact finite-interval dyadic/gamma bridge (`L-91530`);
3. the lossless rational inner factor
   \[
   b_\omega(s)^2=\left(\frac{s-\omega}{s+\omega}\right)^2;
   \]
4. the positive beta/Laplace gamma source of `L-91631`.

Their tensor/direct-sum product is an explicit positive arithmetic source
space

\[
 \mathcal S_\omega^{\rm arith}
\]

with full carrier polarization and coefficient-one factor bookkeeping.

No same-space unbounded inverse, free non-Hilbert pole tail, or unspecified
prime product limit remains in the source construction.

## 2. Paired-Eta Julia–Gamma Optical Completion (`PEJGOC_omega`)

Construct a source-ordered isometry or conservative colligation

\[
 \boxed{
 \mathfrak U_\omega:
 \mathcal S_\omega^{\rm arith}
 \longrightarrow
 \mathcal H_\omega^{\rm crit}
 \oplus
 \mathcal H_\omega^{\rm st}
 \oplus
 \mathcal H_\omega^{\rm hyp}
 \oplus
 \mathcal E_\omega
 }
\]

on the pole/Green-aligned model core such that:

1. the visible transfer is exactly
   \[
   \xi(s-\omega)/\xi(s+\omega);
   \]
2. the eta returned state and eta Julia detail are carried by the explicit
   weighted spaces of `L-91630`;
3. the compact bridge, rational inner factor and gamma Laplace source are
   inserted with the exact factors of `L-91631`;
4. the critical and deterministic stable outputs are the canonical model
   outputs of the horizontal Xi quotient;
5. the arithmetic norm is exhausted by those two outputs:
   \[
   \boxed{
   \|\Phi_\omega^{\rm arith}\|^2
   =\|k_\omega^{\rm crit}\|^2
    +\|k_\omega^{\rm st}\|^2;
   }
   \]
6. no same-node hyperbolic or auxiliary norm remains.

## 3. Consequence

The model-space ledger then forces

\[
 k_\omega^{\rm hyp}=0,
 \qquad
 \mathcal E_\omega=0.
\]

By the one-node crossed-zero detector,

\[
 \xi(s)\ne0
 \qquad
 \left(\Re s>\frac12+\omega\right).
\]

Hence

\[
 \boxed{
 PEJGOC_{\omega_j}\text{ for one sequence }\omega_j\downarrow0
 \Longrightarrow RH.
 }
\]

## 4. Reduction relative to the parent route

The parent `EPDOB/EBOC` formulation treated the paired-eta tail as the last
unbounded source operation.  `L-91630` removes that obstruction by orienting
the map as a weighted sector-changing Julia dilation.

The remaining theorem is now purely a **source-to-model exhaustion theorem**.
Every arithmetic source factor is explicit and positive; the burden is to
identify their canonical critical/stable outputs without leaving a hyperbolic
remainder.

## 5. Firewall

`R-91630` blocks the shortcut from positive source kernels to a Schur quotient
or to model exhaustion.  The colligation must preserve the exact analytic
factors and cannot be replaced by an arbitrary unitary between source vectors
of equal norm.

## 6. Exact boundary

```text
paired eta weighted Julia source                  EXACT
compact dyadic/gamma bridge                       EXACT
rational inner factor                             EXACT
positive gamma Laplace source                     EXACT
all source-side unboundedness                      REMOVED
PEJGOC canonical source-to-model exhaustion        OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```
