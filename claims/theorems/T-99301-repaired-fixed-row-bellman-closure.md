# T-99301 — Repaired fixed-row Bellman closure without differential Hall or common-parent ownership

Claim ID: `T-99301`  
Status: **PROPOSED COMPLETE COMPOSITION ON A LOCAL SCALAR LEDGER — INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-20  
Supersedes as conclusion-producing composition: `T-99300`  
RH status: unproved

## 1. Inputs

Fix one component row `j`. For every finite typed quotient state `v`, assume:

1. the frozen **cumulative** compact Hall inequalities hold and the row profile
   is monotone in the Hall orientation;
2. the same-index factor-67 child observation is exact in this component row;
3. after including the finite/continuum, knot, anchor and realization
   calibration, the actual scalar ledger is

   \[
   c_v(j)=J_v(j)+\sum_{w\succ v}a_{vw}c_w(j)+C_v(j),
   \tag{T-99301.1}
   \]

   with

   \[
   J_v(j)\ge0,
   \qquad a_{vw}\ge0,
   \qquad \sum_{w\succ v}a_{vw}<67^{-1/2}<1/8;
   \tag{T-99301.2}
   \]

4. the local calibration family `C_v(j)` is uniformly subpolynomial in the
   root endpoint, hence belongs to the class `S_0` of `L-99303`;
5. the fixed-row Mellin identity of `L-96000` and the noncancellation theorem of
   `L-96001` hold.

These inputs are scalar. They make no assertion that target, score, capacities
or different rows share one physical coupling.

## 2. Positive witness

Define the finite-DAG Bellman witness

\[
D_v(j)=J_v(j)+\sum_{w\succ v}a_{vw}D_w(j)
\tag{T-99301.3}
\]

from the terminal states upward. By `L-99302`,

\[
D_v(j)\ge0.
\tag{T-99301.4}
\]

The error `E_v=c_v-D_v` obeys

\[
E_v=C_v+\sum_{w\succ v}a_{vw}E_w.
\tag{T-99301.5}
\]

By `L-99303`, the complete resolved error remains in `S_0`, and therefore in
the absolute Mellin class `A_+`:

\[
\int_1^\infty |E_X(j)|X^{-\sigma-1}\,dX<\infty
\qquad(\sigma>0).
\tag{T-99301.6}
\]

At the root we have

\[
\boxed{c_X(j)=D_X(j)+E_X(j),\qquad D_X(j)\ge0,\qquad E_X(j)\in\mathcal A_+.}
\tag{T-99301.7}
\]

## 3. Mellin--Landau conclusion

Suppose `rho` is a zeta zero with `Re(rho)>1/2`. By `L-96001`, choose one
sufficiently large fixed row `j` with `P_j(rho)!=0`. Then the Mellin transform
of `D_X(j)` has a nonreal pole at

\[
s=\rho-\frac12,
\]

because the transform of `E_X(j)` is holomorphic in `Re(s)>0`.

The transform is holomorphic at every positive real point by the explicit
fixed-row formula. Since `D_X(j)>=0`, the exact Landau trichotomy of `L-99303`
forbids that nonreal pole. Hence no zero can satisfy `Re(rho)>1/2`; functional
equation symmetry gives RH.

## 4. Interfaces removed by the repair

The conclusion no longer uses:

```text
pointwise endpoint-density Hall
measurable differential Hall selection
endpoint-nested residual source
random-key common-parent partition
native first-owner physical ownership
all-coordinate cone coupling
global score or capacity feasibility
```

The density-level Hall premise is in fact false for the native target family,
as proved in `R-99301`.

## 5. Exact remaining reconstruction target

This theorem is not an assertion that RH has been proved. Its only
repository-specific load-bearing producer is now the **local scalar ledger**
(T-99301.1): reconstruct, in one component row, the cumulative Hall current,
the exact same-index alpha children, and the explicit signed calibration
`C_v(j)`, then verify that `C_v(j)` is uniformly subpolynomial.

This is strictly weaker than reconstructing one common physical parent across
all coordinates, and it cannot be replaced by the false differential Hall
claim.
