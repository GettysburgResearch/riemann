# L-105202 — Xi critical residues are monochromatic and coherent on the natural high-derivative scale

Claim ID: `L-105202`  
Status: **PROPOSED UNCONDITIONAL ANALYTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105200--L-105201`; PR #720 `L-104522`  
RH status: **not assumed**

## 1. Residues and exact normalization

Fix `C,H>0` and the common height

\[
T_M=C\sqrt{M/\log M}.
\]

For `m>=M+2` and every real zero `c` of `Xi^(m)` in `[-T_M,T_M]`, define

\[
\rho_{m,c}
={\Xi^{(m-1)}(c)\over\Xi^{(m+1)}(c)}.
\tag{L-105202.1}
\]

`L-105201` makes every such zero simple.  Put

\[
\alpha_m={M_{m-1}\over M_{m+1}}
={1\over\mu_{m-1}\mu_m}>0,
\qquad
\mu_j={M_{j+1}\over M_j}.
\tag{L-105202.2}
\]

Then there is a sequence `eta_M -> 0`, depending only on `C,H`, such that

\[
\boxed{
\sup_{m\ge M+2}
\sup_{\substack{\Xi^{(m)}(c)=0\\|c|\le T_M}}
\left|{\rho_{m,c}\over-\alpha_m}-1\right|
\le\eta_M.
}
\tag{L-105202.3}
\]

In particular every residue in the box is negative for all sufficiently large
`M`.

## 2. Adjacent saddle and moment ratios

The saddle equation in `L-105200` and the mean-value theorem give, uniformly
for `j>=M`,

\[
w_{j+1}-w_j=O(1/j),
\tag{L-105202.4}
\]

and differentiating the curvature formula gives

\[
s_{j+1}^2-s_j^2=O(\log j/j^2).
\tag{L-105202.5}
\]

The Gaussian limit also gives

\[
{\mu_j-w_j\over s_j}
=\int X_j\,d\nu_j=o(1),
\]

hence

\[
\boxed{
\mu_j=w_j(1+o(1)),
\qquad
\alpha_m=w_m^{-2}(1+o(1))
}
\tag{L-105202.6}
\]

uniformly on the complete tail.

Since `|c|<=T_M`, (L-105202.4)--(L-105202.5) imply

\[
(w_{m\pm1}-w_m)c=o(1),
\qquad
(s_{m\pm1}^2-s_m^2)c^2=o(1)
\tag{L-105202.7}
\]

uniformly for `m>=M+2`.

## 3. Evaluation at a critical zero

By `L-105201`, if `m` is even then

\[
w_mc=(j+\tfrac12)\pi+o(1),
\]

while if `m` is odd then

\[
w_mc=j\pi+o(1),
\]

uniformly over all zeros in the box.

Apply the Gaussian model of `L-105200` to the three adjacent orders.  When
`m` is even, the two neighbouring derivatives are sine models and

\[
\Xi^{(m-1)}(c)
=2i^mM_{m-1}e^{-s_{m-1}^2c^2/2}
\sin(w_{m-1}c)(1+o(1)),
\]

\[
\Xi^{(m+1)}(c)
=-2i^mM_{m+1}e^{-s_{m+1}^2c^2/2}
\sin(w_{m+1}c)(1+o(1)).
\]

When `m` is odd, both neighbouring derivatives are cosine models and the same
minus sign occurs because `i^(m+1)=-i^(m-1)`.

Equation (L-105202.7) shows that the two sine values, or the two cosine values,
have the same nonzero sign and ratio `1+o(1)`.  The Gaussian envelope ratio is
also `1+o(1)`.  Division gives (L-105202.3).

## 4. Exact coherence consequence

Let

\[
R_m=\#\{c\in[-T_M,T_M]:\Xi^{(m)}(c)=0\},
\]

\[
A_m=-\sum_c\rho_{m,c},
\qquad
B_m=\sum_c\rho_{m,c}^2,
\]

and define the residue coherence

\[
\mathfrak C_m={A_m^2\over R_mB_m}.
\tag{L-105202.8}
\]

From (L-105202.3),

\[
R_m\alpha_m(1-\eta_M)
\le A_m\le
R_m\alpha_m(1+\eta_M),
\]

and

\[
R_m\alpha_m^2(1-\eta_M)^2
\le B_m\le
R_m\alpha_m^2(1+\eta_M)^2.
\]

Therefore

\[
\boxed{
\mathfrak C_m
\ge
\left({1-\eta_M\over1+\eta_M}\right)^2
=1-o(1)
}
\tag{L-105202.9}
\]

uniformly for every `m>=M+2`.

This proves the Xi-specific residue mean-value condition `RCMV104530` with
arbitrarily strong margin throughout the entire natural-scale derivative tail.
It does not prove that condition for a fixed low derivative.

## 5. First and second residue moment asymptotics

Combining `L-105201.4`, (L-105202.6), and (L-105202.3), whenever
`w_mT_M -> infinity`,

\[
\boxed{
A_m
={2T_M\over\pi w_m}(1+o(1)),
\qquad
B_m
={2T_M\over\pi w_m^3}(1+o(1))
}
\tag{L-105202.10}
\]

uniformly on the derivative tail.

Thus the high derivatives have not merely real zeros but a quantitatively
monochromatic inverse-curvature field.

## 6. Reverse-Rolle consequence and boundary

The exact transfer theorem `L-104522` gives

\[
N_\mathbb R(\Xi^{(m-1)};(-T_M,T_M))
\ge
(1-o(1))
N_\mathbb R(\Xi^{(m)};(-T_M,T_M))-1.
\tag{L-105202.11}
\]

The conclusion is unconditional on the high derivative tail.  It does not
iterate to `Xi` without a coherence theorem covering the intervening fixed and
moderate derivative orders.  No RH claim is made.
