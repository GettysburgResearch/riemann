# L-91673 — Fixed-window score Hall is an explicit simultaneous native-root decomposition

Claim ID: `L-91673`  
Status: **PROPOSED COMPLETE ROOT-DECOMPOSITION THEOREM; FROZEN ENDPOINT-FRAME INPUTS REQUIRE INDEPENDENT RECONSTRUCTION**  
Created: 2026-08-14  
Primary inputs: `L-91340`, `L-91341`, native response identities in `L-91663.1--.8`, formal endpoint-frame theorem `L-91674`, and firewall `R-91673`  
RH status: **unproved**

## 1. Certified domain

Fix

\[
0.01844367547103<c_0<0.01844367547105,
\qquad X_0=c_0^{-1}<54.2192.
\]

All Hall operations in this theorem occur at a normalized root quotient

\[
1\le x\le X_0.
\]

No stopped one-prime leaf `py` is Hallized.

## 2. Native score, target, and component-row atoms

For a squarefree integer `k<=x`, put

\[
S_x(k)=\frac{5\sqrt{x/k}-3}{\sqrt k}
      =\frac{5\sqrt x}{k}-\frac3{\sqrt k},
\]

\[
T_x(k)=\frac{4\sqrt{x/k}-3}{\sqrt k}
      =\frac{4\sqrt x}{k}-\frac3{\sqrt k},
\]

and, for every row index `j>=2`,

\[
A_{x,j}(k)=\frac1{\sqrt k}Q_{x/k}(j).
\]

Let

\[
E_x=\{e\le x:\mu(e)=1\},
\qquad
O_x=\{o\le x:\mu(o)=-1\}.
\]

## 3. Score Hall with a strict fixed-window margin

The directed finite-window theorem supplies, for every active odd threshold `t`,

\[
\sum_{\substack{e\in E_x\\e\le t}}S_x(e)
-
\sum_{\substack{o\in O_x\\o\le t}}S_x(o)
>\frac3{100}.
\]

Therefore the nested-neighborhood Hall theorem gives a nonnegative score-mass transport

\[
t_x(o,e)\ge0,
\qquad t_x(o,e)>0\Longrightarrow e\le o,
\]

such that

\[
\sum_e t_x(o,e)=S_x(o)
\quad(o\in O_x),
\]

\[
\sum_o t_x(o,e)\le S_x(e)
\quad(e\in E_x).
\]

Define the unused even score mass and residual coefficient by

\[
r_x(e)=S_x(e)-\sum_o t_x(o,e)\ge0,
\qquad
\nu_x(e)=\frac{r_x(e)}{S_x(e)}\in[0,1].
\]

The signed score is represented exactly:

\[
\boxed{
\sum_{k\le x}\mu(k)S_x(k)
=
\sum_{e\in E_x}\nu_x(e)S_x(e).
}
\tag{L-91673.1}
\]

## 4. Explicit nonnegative target slack

Write

\[
q_x(k)=\frac{T_x(k)}{S_x(k)}
      =\frac{4z_k-3}{5z_k-3},
\qquad z_k=\sqrt{x/k}.
\]

Since

\[
\frac d{dz}\frac{4z-3}{5z-3}
=rac3{(5z-3)^2}>0,
\]

the support condition `e<=o` gives `q_x(e)>=q_x(o)`. Score-mass conservation therefore yields the exact identity

\[
\boxed{
\sum_{k\le x}\mu(k)T_x(k)
=
\sum_e\nu_x(e)T_x(e)+U_x,
}
\tag{L-91673.2}
\]

where

\[
U_x=\sum_{o,e}t_x(o,e)[q_x(e)-q_x(o)]\ge0.
\]

Thus the positive residual source is target-subordinate, with every unit of unused target displayed explicitly.

## 5. Explicit all-row decomposition

For each `j>=2`, define the score-normalized row profile

\[
\Phi_{x,j}(k)=\frac{A_{x,j}(k)}{S_x(k)}
=rac{Q_{x/k}(j)}{5\sqrt{x/k}-3}.
\]

The directed normalized-row theorem proves that

\[
Y\longmapsto\frac{Q_Y(j)}{5\sqrt Y-3}
\]

is increasing on the entire certified window. Hence `e<=o` implies

\[
\Phi_{x,j}(e)\ge\Phi_{x,j}(o).
\]

Put

\[
B_{x,j}
=
\sum_{o,e}t_x(o,e)
 [\Phi_{x,j}(e)-\Phi_{x,j}(o)]
\ge0.
\]

Then, coefficientwise and simultaneously for every component row,

\[
\boxed{
\sum_{k\le x}\mu(k)A_{x,j}(k)
=
B_{x,j}
+
\sum_e\nu_x(e)A_{x,j}(e).
}
\tag{L-91673.3}
\]

This is an atomwise positive decomposition, not a coordinatewise complement. The same transport coefficients occur in score, target, and every row.

## 6. Native ordinary and radix-four identities

Let `c_X` denote the complete finite equality row obtained after restoring the endpoint scaling and Möbius sum. The exact native response formulas give, for every physical integer column `q>=2`,

\[
\Gamma(c_X;q)=w_X(q),
\qquad
\Xi(c_X;q)=\Omega_X(q).
\]

Apply the linear ordinary response to (L-91673.3), and obtain the detail identity by applying the two ordinary maps at `q` and `4q` before taking their radix-four combination. If `B_X` is the positive current row assembled from the row bonuses and `R_X\widehat Z_X` is the positive residual certificate row, then

\[
\boxed{
\Gamma(B_X;q)+\Gamma(R_X\widehat Z_X;q)=w_X(q),
}
\tag{L-91673.4}
\]

\[
\boxed{
\Xi(B_X;q)+\Xi(R_X\widehat Z_X;q)=\Omega_X(q).
}
\tag{L-91673.5}
\]

These equalities are the simultaneous residual-capacity ledger missing from the coordinatewise-complement proposal. No current piece is tested against an independent copy of the full parent budget.

## 7. Arbitrary positive-certificate replacement

First write a simple realized residual certificate as

\[
R_X\widehat Z_X=\sum_a c_aP_a,
\qquad c_a\ge0.
\]

For any row `d_a>=0` feasible for the complete ordinary and radix-four capacities of `P_a`, set

\[
d_X^{\rm pre}=B_X+\sum_a c_ad_a.
\]

Equations (L-91673.4)--(L-91673.5) give simultaneously

\[
\Gamma(d_X^{\rm pre};q)\le w_X(q),
\qquad
\Xi(d_X^{\rm pre};q)\le\Omega_X(q).
\]

General positive certificate measures follow by monotone convergence. Same-index multiplicative placement supplies the actual arithmetic child coefficient once; root collars, omissions, mismatch packets, and common ports are not child-owned.

## 8. Endpoint-frame and one-use finite correction

`L-91674` proves the formal commutation of this finite decomposition with positive endpoint integration, common-parent pushforward, same-index child transport, and one global positive quantizer. Under the frozen analytic endpoint-frame hypotheses, all current packets are summed first and the following are applied exactly once:

```text
positive martingale B-spline quantization;
finite/continuum mismatch repair;
interior safety factor;
fixed top omission and terminal taper;
finite base correction.
```

Their declared equality-score cost is one absolute `C_fin` per generation. No Schur/color projection, negative butterfly center, or stopped-leaf Hall theorem is used.

## 9. Exact boundary

```text
fixed-window score Hall                         DIRECTED EXACT
score equality                                  EXACT
target subordination and slack                  EXACT
all component-row decomposition                 EXACT
ordinary/detail common normalization            EXACT
arbitrary positive-certificate replacement      EXACT
endpoint-frame formal commutation                EXACT / L-91674
frozen analytic endpoint producer hypotheses    IMPORTED / RECONSTRUCT
one-use finite correction estimates             IMPORTED / RECONSTRUCT
Riemann Hypothesis                              UNPROVEN
```
