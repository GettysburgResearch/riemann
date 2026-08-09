# L-34006 — The radix-four reserve increment is an exact relative Jordan log-curvature

Claim ID: `L-34006`  
Title: The critical-scale Q=4 reserve increment is the negative second logarithmic derivative of one explicit positive relative Jordan partition function  
Status: **PROPOSED COMPLETE EXACT CALCULUS IDENTITY — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-09  
Parent: PR #341  
Dependencies: PR #339 `L-33802`; PR #342 `L-34002`  
Scope: deterministic relative Kummer/Jordan curvature; no current domination or RH conclusion

## 1. Positive Jordan partition on one carry row

Let

\[
 J_{4,\tau}(s)=\frac{A_4(s-\tau)}{A_4(s)},
 \qquad \tau\ge0,
\]

be the positive Q=4 Jordan deformation. For an integer carry row

\[
 e=(n,j),
 \qquad 0<j<n,
\]

put

\[
 \boxed{
 F_e(\tau)=1+\mathcal L_e(J_{4,\tau}).
 }
\tag{L-34006.1}

Because the Jordan coefficients and carry indicators are nonnegative for `tau>=0`,

\[
 F_e(\tau)\ge1.
\tag{L-34006.2}

At `tau=0`,

\[
 F_e(0)=1,
 \qquad
 F_e'(0)=P_e,
 \qquad
 F_e''(0)=S_e,
\tag{L-34006.3}

where `P_e=P_4(n,j)` and `S_e=S_4(n,j)`. Therefore

\[
 \boxed{
 \mathcal R_e=P_e^2-S_e
 =-\frac{d^2}{d\tau^2}\log F_e(\tau)\Big|_{\tau=0}.
 }
\tag{L-34006.4}

Thus the deterministic Kummer reserve is literally the log-concavity curvature of the positive Jordan partition function at the undeformed source.

## 2. Exact relative scale-four partition

Let

\[
 4e=(4n,4j).
\]

Define

\[
 \boxed{
 H_e(\tau)
 =\frac{F_{4e}(\tau)}{F_e(4\tau)}.
 }
\tag{L-34006.5}

Both numerator and denominator are strictly positive for `tau>=0`, so `H_e` is a positive real analytic function near zero. Also

\[
 H_e(0)=1.
\tag{L-34006.6]

Taking logarithmic derivatives and using (L-34006.3),

\[
 \boxed{
 \frac{d}{d\tau}\log H_e(\tau)\Big|_0
 =P_{4e}-4P_e
 =:E_e.
 }
\tag{L-34006.7]

The first relative score is exactly the positive radix-four Kummer innovation from PR #342.

For the second logarithmic derivative,

\[
\begin{aligned}
 -\frac{d^2}{d\tau^2}\log H_e(\tau)\Big|_0
 &=\mathcal R_{4e}-16\mathcal R_e.
\end{aligned}
\]

Hence

\[
 \boxed{
 \Delta_4\mathcal R(e)
 :=\mathcal R_4(4n,4j)-16\mathcal R_4(n,j)
 =-\frac{d^2}{d\tau^2}\log H_e(\tau)\Big|_0.
 }
\tag{L-34006.8]

(The closing square brackets in tags `L-34006.6]`--`L-34006.8]` are typographical only.)

This is an exact identity, not an asymptotic analogy.

## 3. Algebraic expansion

Since

\[
 P_{4e}=4P_e+E_e,
\]

one may expand (L-34006.8) as

\[
 \boxed{
 \Delta_4\mathcal R(e)
 =E_e(8P_e+E_e)
  +16S_e-S_{4e}.
 }
\tag{L-34006.9]

PR #325 `L-32414` proves

\[
 E_e\ge0,
 \qquad
 16S_e-S_{4e}\ge0.
\]

Consequently the relative curvature splits into two nonnegative deterministic components:

\[
 \boxed{
 \Delta_4\mathcal R(e)
 \ge E_e(8P_e+E_e)
 \ge8P_eE_e.
 }
\tag{L-34006.10]

This lower bound is useful when seeking a Cauchy/Schur realization of the compact physical-current innovation: the available critical-scale reserve already contains the geometric cross budget `8 P E` before the independent second-moment slack is used.

## 4. Relation to the discovery current inequality

PR #342 observed numerically that the one-step physical innovation

\[
 I_e=Q_4^{\rm phys}(4n,4j)-Q_4^{\rm phys}(n,j)
\]

appears to satisfy

\[
 |I_e|^2\le\Delta_4\mathcal R(e)
\]

outside a tiny finite base. The present theorem does **not** prove that inequality.

It identifies precisely what a proof would have to construct: a source-bound second score whose covariance with the relative Jordan score `E_e` is `I_e`, with covariance matrix dominated by the positive log-curvature (L-34006.8). Equivalently, a legitimate two-parameter positive or reflected family would yield the desired inequality by a `2x2` Schur/Cramér--Rao argument.

The distinction matters: scalar positivity of `H_e` does not imply positivity of an arbitrary two-parameter Hessian.

## 5. Proof boundary

Closed exactly, subject to review:

1. reserve as negative log-curvature of a positive Jordan partition;
2. relative scale-four partition function;
3. first relative score equals the radix-four Kummer innovation;
4. second relative log-curvature equals the complete reserve increment;
5. the exact positive decomposition (L-34006.9)--(L-34006.10).

Still open:

1. construction of the correct second parameter carrying the physical current innovation;
2. the corresponding `2x2` Hessian/Schur positivity;
3. RH.
