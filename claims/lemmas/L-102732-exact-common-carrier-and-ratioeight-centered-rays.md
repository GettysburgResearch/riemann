# L-102732 — The exact common ray carrier is `cX`; every centered filtered ray is ratio-eight compact

Claim ID: `L-102732`  
Status: **PROVED EXACT CARRIER CORRECTION AND COMPACT-SUPPORT THEOREM**  
Created: 2026-08-23  
Depends on: `L-102729`; `T-102750`  
RH status: **not assumed**

Let

\[
 K_w=P_2|S_-+w|^2,
 \qquad |w|\le\frac12,
\]

and put

\[
 c=2(2-\sqrt2).
\]

`L-102729` proves

\[
 K_w(y)=cy
 \qquad(y\ge8),
\]

independently of `w`.

## 1. Exact initial integral

Write

\[
 K_w=C+2B\Re w+A|w|^2
\]

on the three finite activation cells. Direct integration of the exact
piecewise formulas gives

\[
 \int_1^8 A(y)\frac{dy}{y}=0,
 \qquad
 \int_1^8 B(y)\frac{dy}{y}=0,
\]

and

\[
 \int_1^8 C(y)\frac{dy}{y}
 =32-16\sqrt2
 =8c.
\]

Therefore, for every `|w|<=1/2`,

\[
 \boxed{
 JK_w(y)=cy
 \qquad(y\ge8).
 }
 \tag{L-102732.1}
\]

The common one-atom carrier is `cy`, not `c(y-1)`.

## 2. Correct source carrier

For the tangent source `Sigma_tau`, the exact common ray carrier is

\[
 \boxed{
 \mathcal C_\tau(X)
 =
 cX
 \sum_n\frac{\Sigma_\tau(n)}{n^{3/2}}.
 }
 \tag{L-102732.2}
\]

The historical `(X-1)` display in `T-102750` is therefore corrected by
(L-102732.2).  This does not change the Lorentz/barycentric identity, because
its ray coefficients sum to zero.

## 3. Ratio-eight compact centering

Define the one-atom centered ray

\[
 \boxed{
 R_w(y)
 =
 JK_w(y)-cy\mathbf1_{y\ge1}.
 }
 \tag{L-102732.3}
\]

Then

\[
 \boxed{
 \operatorname{supp}R_w\subset[1,8]
 \qquad(|w|\le1/2).
 }
 \tag{L-102732.4}
\]

Consequently every carrier-recombined centered ray, every entry of the
centered post-filter disk matrix, and the complete Lorentz barycentric
combination have physical overlap only when two source products have ratio in

\[
 \boxed{[1/8,8].}
 \tag{L-102732.5}
\]

This sharpens the `[1/16,16]` mother-support occupancy window for the centered
filtered current.

## 4. Exact scope

The compact centered rays are signed.  Compactness and the ratio-eight window
do not prove their arithmetic negative-mass estimate.  They remove the affine
mode exactly and reduce the radial-slack/occupancy problem to one fixed finite
multiplicative shell.