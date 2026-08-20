# T-99720 — First-owner square-function integrator and exact OCE67 contract

Claim ID: `T-99720`  
Status: **UNCONDITIONAL INTEGRATOR; ONE ARITHMETIC EMBEDDING OPEN**  
Created: 2026-08-20  
Frozen base: PR #658 at `3dd7eacdadc76822e25ee630a474580259dd64fb`  
RH status: **unproved**

## Native source

The sequential first-owner identity reproduces the literal Möbius Euler source:

\[
\prod_i(I-r_iU_i)
=s_kI+\sum_i\lambda_i(I-U_i)\prod_{h>i}(I-r_hU_h).
\tag{T-99720.1}
\]

## Native energy

`L-99720` gives

\[
\left\|\prod_i(I-r_iU_i)f\right\|^2
=s_k^2\|f\|^2+
\sum_i r_is_{i-1}^2\|\Delta_i^{\rm fut}f\|^2.
\tag{T-99720.2}
\]

`L-99721` gives a polylogarithmic free labelled-source energy bound.

## Scalar consumer

For the factor-67 SHARP defect `h`, PRs #653 and #658 give a fixed zero-free Mellin consumer. Subpower logarithmic negative mass of the zero-free box implies RH.

## Exact OCE67 contract

Let `d\mathfrak m_X(i,\omega)` be the actual first-owner labelled source measure at endpoint `X`, with future completion `\omega`, and let `\mathcal P_X` be the fixed zero-free SHARP-box observation. Define

\[
\mathcal S_X^2=
\sum_i r_is_{i-1}^2
\int|\Delta_i^{\rm fut}(\omega)|^2\,d\mathfrak m_X(i,\omega).
\]

`OCE67` is the source-prescribed estimate

\[
\boxed{
\int_2^Y[(\mathcal P_Xh)(X)]_-\frac{dX}{X}
\ll_\varepsilon
Y^\varepsilon
\left(1+\int_2^Y\mathcal S_X^2\frac{dX}{X}\right)^{1/2}
}
\tag{T-99720.3}
\]

for every `epsilon>0`, with all labels, capacities, endpoint kernels and owner maps fixed before the unknown sign is observed.

Combined with the polylogarithmic energy budget, OCE67 implies subpower negative mass and hence RH.

## Boundary

```text
native first-owner coefficients           PROVED
native Littlewood--Paley identity          PROVED
polylog labelled-source energy             PROVED
source-blind collapse contraction          REFUTED
OCE67 physical owner-Carleson embedding    OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVEN
```
