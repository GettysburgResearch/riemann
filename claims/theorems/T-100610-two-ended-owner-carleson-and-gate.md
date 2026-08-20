# T-100610 — Two-ended owner Carleson AND-gate

Claim ID: `T-100610`  
Status: **PROVED EXACT CONDITIONAL AND-GATE; BOTH INPUT ENERGIES OPEN**  
Created: 2026-08-20  
Audited: 2026-08-21  
Depends on: `L-100610`; `L-100611`; `L-100612`; `L-100614`  
RH status: **unproved**

Let

\[
F_k(X)=\prod_{i=1}^{k}(I-r_iU_i)\Psi(X),
\qquad r_i=p_i^{-1/2},
\]

where `Psi` is the positive cubic critical kernel and the ordered coordinates
include the second labelled copy of `67`.

The two-ended hazard identity gives

\[
F_k
=s_k\Psi
+
\sum_i r_iL_iR_i\Delta_i\Psi
+
\sum_{i<j}r_ir_jL_iR_jH_{i,j},
\tag{T-100610.1}
\]

where

\[
H_{i,j}=\Delta_i\Delta_jE_{i+1:j-1}\Psi.
\]

By `L-100612`, the root and every singleton are nonnegative. By `L-100614`,
write

\[
H_{i,j}=M_{i,j}+\widetilde H_{i,j},
\qquad M_{i,j}\ge0,
\tag{T-100610.2}
\]

with the complete half-order carrier kept explicitly. Therefore

\[
\boxed{
(F_k(X))_-
\le
\sum_{i<j}r_ir_jL_iR_j
|\widetilde H_{i,j}(X)|.}
\tag{T-100610.3}
\]

Define the row and column energies

\[
\mathfrak R_k(X)
=
\sum_{i<j}r_ir_jL_i^2
|\widetilde H_{i,j}(X)|,
\tag{T-100610.4}
\]

\[
\mathfrak C_k(X)
=
\sum_{i<j}r_ir_jR_j^2
|\widetilde H_{i,j}(X)|.
\tag{T-100610.5}
\]

Pairwise Cauchy--Schwarz gives the exact matrix interpolation

\[
\boxed{
(F_k(X))_-
\le
\sqrt{\mathfrak R_k(X)\mathfrak C_k(X)}.}
\tag{T-100610.6}
\]

The survival-vector estimates

\[
\sum_i r_iL_i^2\le1,
\qquad
\sum_jr_jR_j^2\le1
\]

show that these are probability-normalized owner energies, not source-blind
label counts.

## Conditional closure theorem

Define:

`FOCR100610` — for every `epsilon>0`,

\[
\sup_k\int_1^Y\mathfrak R_k(X)\frac{dX}{X}
\ll_\epsilon Y^\epsilon;
\tag{T-100610.7}
\]

`LOCR100610` — for every `epsilon>0`,

\[
\sup_k\int_1^Y\mathfrak C_k(X)\frac{dX}{X}
\ll_\epsilon Y^\epsilon.
\tag{T-100610.8}
\]

Then Cauchy--Schwarz in `X` and (T-100610.6) give

\[
\sup_k\int_1^Y(F_k(X))_-\frac{dX}{X}
\ll_\epsilon Y^\epsilon.
\tag{T-100610.9}
\]

The complete cubic source is obtained by the absolutely convergent limit of
the finite labelled Euler packets. The frozen critical-negative-mass detector
then gives

\[
\boxed{
FOCR100610+LOCR100610\Longrightarrow RH.}
\tag{T-100610.10}
\]

## Audited relationship to the repository

This AND-gate is a direct consequence of the exact two-ended hazard and does
**not** use the withdrawn claims `L-100603` or `L-100604`.

- `FOCR100610` is the least-owner row-energy problem obtained from the exact
  row marginal of `L-100610`.
- `LOCR100610` is the greatest-owner column-energy problem obtained from the
  exact column marginal.
- Finite squaring, compact interval positivity, and the balanced coboundary
  homotopy may be used only after a source-typed identity has placed them in
  these energies. No generic dilation is treated as a divisor restriction.
- The carrier terms may not be estimated independently of their transition
  partners; the power-sized cancellation firewall on PR #695 remains binding.

The theorem is therefore a valid implication gate, but neither input estimate
is claimed to follow from the superseded renewal arrows.

## Scientific status

```text
two-ended hazard identity                  proved exact
carrier subtraction                        proved exact
row/column interpolation                   proved exact
FOCR100610                                  open / RH-bearing
LOCR100610                                  open / RH-bearing
AND-gate to negative mass and RH            proved conditional
withdrawn renewal shortcuts                 not used
Riemann Hypothesis                          unproved
```