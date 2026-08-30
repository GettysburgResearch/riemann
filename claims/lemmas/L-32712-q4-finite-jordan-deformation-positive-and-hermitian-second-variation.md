# L-32712 — The finite Q=4 Jordan deformation is coefficientwise positive and has an exact Hermitian second variation

Claim ID: `L-32712`  
Title: The complete deformation `A_4(s-tau)/A_4(s)` has nonnegative Dirichlet coefficients for every real `tau>=0`; after source convolution its finite reflected difference is a literal Hermitian square, and its imaginary-shift Hessian gives the correctly polarized augmented reserve  
Status: **PROPOSED COMPLETE EXACT DIRICHLET/HERMITIAN THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: PR #325 `L-32404`; PR #337 `L-32710/L-32711`  
Scope: finite deformation, coefficient positivity, exact reflected square, and second-variation polarization; positivity of the complete Hessian matrix and the global block recurrence are not inferred

## 1. Definition

Retain the Q=4 Euler–Blaschke inverse

\[
 A_4(s)=\zeta(s)\frac{1-4^{-s}}{1-4^{1-s}},
 \qquad
 B_4(s)=A_4(s)^{-1}.
\]

For real `tau>=0`, define

\[
 \boxed{
 J_\tau(s)=\frac{A_4(s-\tau)}{A_4(s)}
 =\sum_{n\ge1}\frac{J_\tau(n)}{n^s}.
 }
 \tag{L-32712.1}
\]

Initially the series converges absolutely for `Re(s)>1+tau`. At `tau=0`,

\[
 J_0=\varepsilon.
\]

## 2. Odd-prime local factors

For an odd prime `p`, put `x=p^{-s}` and `a=p^tau>=1`. The local factor is

\[
 \frac{1-x}{1-ax}
 =1+\sum_{r\ge1}(a-1)a^{r-1}x^r.
\]

Hence

\[
 \boxed{
 J_\tau(p^r)=(p^\tau-1)p^{(r-1)\tau}\ge0
 \qquad(r\ge1).
 }
 \tag{L-32712.2}
\]

It is strictly positive when `tau>0`.

## 3. Exact positive two-adic factor

Put

\[
 b=2^\tau\ge1,
 \qquad y=2^{-s}.
\]

The two-adic local factor of `A_4` is

\[
 A_{4,2}(y)=\frac{1+y}{1-4y^2}.
\]

Therefore the local factor of (L-32712.1) is

\[
 \boxed{
 R_b(y)
 =\frac{1+by}{1+y}\frac{1-4y^2}{1-4b^2y^2}
 =\sum_{r\ge0}r_r(b)y^r.
 }
 \tag{L-32712.3}
\]

For `b=1`, `R_b=1`. Assume `b>1`. The exact partial-fraction decomposition is

\[
 \boxed{
 \begin{aligned}
 R_b(y)={}&\frac1b
 -\frac{3(b-1)}{(4b^2-1)(1+y)}\\
 &+\frac{3(b^2-1)}{2b(2b+1)(1-2by)}
 +\frac{b^2-1}{2b(2b-1)(1+2by)}.
 \end{aligned}}
 \tag{L-32712.4}
\]

Consequently, for `m>=0`,

\[
 \boxed{
 \begin{aligned}
 r_{2m+1}(b)
 ={}&\frac{3(b-1)}{4b^2-1}\\
 &+(2b)^{2m+1}
 \frac{2(b-1)^2(b+1)}{b(4b^2-1)}>0,
 \end{aligned}}
 \tag{L-32712.5}
\]

and, for `m>=1`,

\[
 \boxed{
 \begin{aligned}
 r_{2m}(b)
 ={}&-\frac{3(b-1)}{4b^2-1}\\
 &+(2b)^{2m}
 \frac{(b^2-1)(4b-1)}{b(4b^2-1)}>0.
 \end{aligned}}
 \tag{L-32712.6}
\]

The last inequality follows after factoring `b-1`: for `b>=1` and `m>=1`,

\[
 (2b)^{2m}\frac{(b+1)(4b-1)}b
 \ge4b(b+1)(4b-1)>3.
\]

Also `r_0(b)=1`. Thus every two-adic coefficient is nonnegative, and every nonconstant one is strictly positive when `tau>0`.

## 4. Global coefficient positivity

The Euler factors are multiplicative. Combining Sections 2 and 3 gives

\[
 \boxed{
 J_\tau(n)\ge0
 \qquad(n\ge1,\ \tau\ge0),
 }
 \tag{L-32712.7}
\]

with strict positivity for every `n` when `tau>0`.

Thus the complete finite deformation joining the identity source to the Q=4 logarithmic hierarchy is coefficientwise positive. No truncation in the logarithmic order is involved.

## 5. Source-convolved finite reflected square

Let `b_4` be the coefficient sequence of `B_4`. For independent twists `t,u`, put

\[
 J_{\tau,t}(n)=J_\tau(n)n^{-it},
 \qquad
 K_{\tau,t}=b_{4,t}*J_{\tau,t}.
 \tag{L-32712.8}
\]

Since `K_(0,t)=b_(4,t)`, associativity gives exactly

\[
 \boxed{
 \begin{aligned}
 &(K_{\tau,t}-b_{4,t})
 *(K_{\tau,-u}-b_{4,-u})\\
 &\qquad=(b_{4,t}*b_{4,-u})*
 [(J_{\tau,t}-\varepsilon)
 *(J_{\tau,-u}-\varepsilon)].
 \end{aligned}}
 \tag{L-32712.9}
\]

After any of the source-complete physical localizations used in `L-32710`, the diagonal `u=t` is the literal norm square

\[
 \boxed{
 \left\|\mathcal P_{B_4(J_\tau-1)}\right\|^2\ge0.
 }
 \tag{L-32712.10}
\]

Thus the finite Jordan deformation polarizes before any derivative or rowwise estimate is taken.

## 6. Logarithmic derivatives at the origin

Allow the deformation parameter to be complex near zero. Coefficientwise differentiation gives

\[
 J_z
 =\varepsilon+z\Lambda_4+\frac{z^2}{2}C_4+O(z^3),
 \tag{L-32712.11}
\]

where

\[
 C_4=\Lambda_4\log+\Lambda_4*\Lambda_4.
\]

Source convolution gives

\[
 K_z
 =b_4+zq_4+\frac{z^2}{2}t_4+O(z^3),
 \tag{L-32712.12}
\]

with

\[
 q_4=b_4*\Lambda_4,
 \qquad
 t_4=b_4*C_4.
\]

For a carry row `e=(n,j)`, let `L_e` denote its carry functional and put

\[
 P_e=L_e(\Lambda_4),
 \quad S_e=L_e(C_4),
 \quad Y_e=L_e(b_4),
 \quad Q_e=L_e(q_4),
 \quad T_e=L_e(t_4).
 \tag{L-32712.13}
\]

Define the imaginary-shift row path

\[
 Z_e(\tau)=1+L_e(J_{i\tau}),
 \qquad
 W_e(\tau)=L_e(K_{i\tau}).
 \tag{L-32712.14}
\]

Then

\[
 Z_e(0)=1,
 \quad Z_e'(0)=iP_e,
 \quad Z_e''(0)=-S_e,
\]

and

\[
 W_e(0)=Y_e,
 \quad W_e'(0)=iQ_e,
 \quad W_e''(0)=-T_e.
\]

Therefore

\[
 \boxed{
 \frac12\frac{d^2}{d\tau^2}
 \left(|Z_e(\tau)|^2+|W_e(\tau)|^2\right)_{\tau=0}
 =P_e^2-S_e+Q_e^2-Y_eT_e.
 }
 \tag{L-32712.15}
\]

The right side is exactly the augmented reserve `A_e` of `L-32711`.

## 7. Correct independent-row Hermitian polarization

For two possibly twisted rows `e,f`, define

\[
 \mathcal G_{e,f}(\tau)
 =Z_e(\tau)\overline{Z_f(\tau)}
 +W_e(\tau)\overline{W_f(\tau)}.
\]

Its exact second variation is

\[
 \boxed{
 \begin{aligned}
 \mathcal A_{e,f}
 :={}&\frac12\mathcal G_{e,f}''(0)\\
 ={}&P_e\overline{P_f}
 -\frac12(S_e+\overline{S_f})\\
 &+Q_e\overline{Q_f}
 -\frac12(T_e\overline{Y_f}+Y_e\overline{T_f}).
 \end{aligned}}
 \tag{L-32712.16}
\]

On the diagonal this reduces to (L-32712.15). Equation (L-32712.16), not the one-sided replacement `Q_e conjugate(Q_f)-Y_e conjugate(T_f)`, is the Hermitian polarization selected by the finite deformation.

This corrects the normalization ambiguity in a naive scalar-to-matrix lift.

## 8. Exact boundary

Established here:

1. coefficientwise positivity of `J_tau` for every real `tau>=0`;
2. an explicit positive formula for every two-adic coefficient;
3. the complete finite source-convolved reflected square;
4. the full first/second logarithmic derivative tower at zero;
5. the augmented reserve as an imaginary-shift second variation;
6. the unique symmetric Hermitian polarization produced by that variation.

Not inferred here:

1. that the Hessian matrix `(A_(e,f))` is positive semidefinite for arbitrary row families;
2. that scalar diagonal positivity alone yields the independent-frequency block theorem;
3. the coefficient-one delayed recurrence;
4. RH.
