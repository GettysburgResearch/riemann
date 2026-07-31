# T-14302 — A vanishing cofinal lower envelope implies RH

Claim ID: `T-14302`  
Title: Cofinal approximate lower bounds, not ground-state convergence, suffice for the Riemann hypothesis  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-b`  
Created: 2026-07-30  
Dependencies: monotonicity of the localized Weil lower spectral value (`CCM` equation (3.27), repository `L-14201`); Weil's positivity criterion; `L-14308` for the block certificate  
Scope: positive sufficient criterion for RH  
Related counterexample candidates: none

## Localized lower spectral value

Let `A_lambda` be the self-adjoint operator associated to the Weil quadratic
form localized to

\[
 [\lambda^{-1},\lambda],\qquad \lambda>1,
\]

and let

\[
 \mu_\lambda:=\inf\sigma(A_\lambda).
 \tag{T-14302.1}
\]

Connes–Consani–Moscovici prove

\[
 \lambda>\lambda'\quad\Longrightarrow\quad
 \mu_\lambda\le\mu_{\lambda'}.
 \tag{T-14302.2}
\]

## Main theorem

Suppose there is a cofinal sequence

\[
 \lambda_j\longrightarrow\infty
\]

and rigorous real lower bounds `F_j` such that

\[
 \mu_{\lambda_j}\ge F_j
 \tag{T-14302.3}
\]

and

\[
 \boxed{\liminf_{j\to\infty}F_j\ge0.}
 \tag{T-14302.4}
\]

Then the Riemann hypothesis is true.

Equivalently, it is sufficient to prove

\[
 \mu_{\lambda_j}\ge-\varepsilon_j,
 \qquad
 \varepsilon_j\downarrow0.
 \tag{T-14302.5}
\]

The lower bounds may remain negative at every finite level.

## Proof

Fix any `lambda>1`.  For all sufficiently large `j`,
`lambda_j≥lambda`, so monotonicity gives

\[
 \mu_\lambda\ge\mu_{\lambda_j}\ge F_j.
\]

Taking the limit inferior in `j` yields

\[
 \mu_\lambda\ge0.
\]

Thus the localized Weil form is nonnegative for every compact multiplicative
support.  Every admissible compactly supported Weil test function lies in one of
these localized spaces.  Hence the full Weil quadratic form is nonnegative on
its test class, and Weil's criterion gives RH.  QED.

## Block Temple–Schur certificate corollary

For each `j`, choose a finite-dimensional near-radical subspace `S_j` and write
the exact ambient localized operator as

\[
 A_{\lambda_j}
 =\begin{pmatrix}B_j&R_j^*\\R_j&C_j\end{pmatrix}
 \quad
 \text{on }S_j\oplus S_j^\perp.
 \tag{T-14302.6}
\]

Suppose a positive complement metric `M_j`, numbers `gamma_j∈R`, `h_j>0`, and
an ambient approximation radius `delta_j≥0` satisfy

\[
 C_j-\gamma_jI\succeq h_jM_j.
 \tag{T-14302.7}
\]

Define

\[
 K_j=B_j-h_j^{-1}R_j^*M_j^{-1}R_j
 \tag{T-14302.8}
\]

and

\[
 F_j=\min\{\gamma_j,\lambda_{\min}(K_j)\}-\delta_j.
 \tag{T-14302.9}
\]

If

\[
 \boxed{\liminf_{j\to\infty}F_j\ge0,}
 \tag{T-14302.10}
\]

then RH follows.

This criterion allows `dim(S_j)>1`.  In particular, all numerically tiny prolate
modes may be placed in `S_j`, avoiding a false spectral-gap requirement between
the first and second tiny localized Weil eigenvalues.

## Scalar squared-residual corollary

For normalized trial vectors `p_j`, let

\[
 \rho_j=\langle A_{\lambda_j}p_j,p_j\rangle,
 \qquad
 z_j=(A_{\lambda_j}-\rho_j)p_j.
\]

If the orthogonal complements satisfy

\[
 C_j-\gamma_jI\succeq h_jM_j
\]

and

\[
 \liminf_j
 \min\left\{
 \gamma_j,
 \rho_j-\frac{\|z_j\|_{M_j^{-1}}^2}{h_j}
 \right\}
 \ge0,
 \tag{T-14302.11}
\]

then RH follows.

Unlike `T-14301`, this statement requires neither:

- simplicity of the finite or infinite ground state;
- evenness of an individual ground eigenfunction;
- convergence of a ground eigenvector to `k_lambda`;
- locally uniform convergence of finite regularized determinants;
- a Hurwitz argument.

It proves positivity directly.

## Radical-tail specialization

Assume the domain and normalization gates of `L-14309` have been verified for

\[
 r_j=E(h_{\lambda_j}),
 \qquad
 k_j=P_{\lambda_j}r_j,
 \qquad
 t_j=(I-P_{\lambda_j})r_j.
\]

If a form-continuity estimate yields

\[
 \|QW(k_j,\cdot)\|_{M_j^{-1}}
 \le C_j\|t_j\|_{X_j},
 \tag{T-14302.12}
\]

then the scalar Schur loss is bounded by

\[
 \frac{C_j^2\|t_j\|_{X_j}^2}{h_j\|k_j\|^2}.
 \tag{T-14302.13}
\]

Thus it is sufficient that the complete lower-floor expression

\[
 \min\left\{
 \gamma_j,
 \rho_j-
 \frac{C_j^2\|t_j\|_{X_j}^2}{h_j\|k_j\|^2}
 \right\}
 -\delta_j
 \tag{T-14302.14}
\]

have negative part tending to zero.  The prolate concentration defect may enter
quadratically through the tail norm.

## Why this is materially weaker than the existing positive route

The CCM paper identifies two missing steps: prove the localized ground state is
simple-even, and prove that it approaches the prolate target closely enough for
its Fourier transform to converge to `Xi`.  Repository `T-14301` turns those
steps into a clean finite diagonal criterion.

T-14302 bypasses both.  The only global objective is a cofinal lower spectral
envelope whose error vanishes.  Even if:

- the low eigenspace has growing multiplicity;
- the ground vector rotates among prolate modes;
- the projective target-to-ground distance does not tend to zero;

RH still follows if the full block Schur floor obeys (T-14302.10).

The scaling

\[
 \|z_j\|_{M_j^{-1}}\asymp h_j\asymp\varepsilon_j
\]

illustrates the separation: the target-distance ratio stays of order one, while
the spectral energy loss is `O(epsilon_j)` and is sufficient here.

## Relationship to CCM Corollary 3.8

CCM Corollary 3.8 states that `lim mu_lambda=0` implies RH.  T-14302 is slightly
more direct.  The cofinal lower envelope first proves `mu_lambda≥0` for every
fixed support by monotonicity, so Weil positivity follows without separately
proving an upper bound tending to zero.

If one also has trial Rayleigh quotients `rho_j→0`, then

\[
 F_j\le\mu_{\lambda_j}\le\rho_j
\]

recovers the CCM limit statement by squeezing.

## What would constitute a completed proof

A completed RH proof along this route needs a finite analytic argument proving,
for all sufficiently large `j`, the full ambient certificate (T-14302.6)–
(T-14302.10).  A finite list of positive numerical floors or a fitted decay law
is not enough.

A viable proof packet may split the complement into:

1. a finite middle-frequency block certified by directed rational `LDL*`;
2. a high-frequency tail controlled by an explicit archimedean coercivity
   estimate minus the finite-prime operator norm;
3. a low prolate block containing every near-radical mode and evaluated exactly;
4. a cross-block squared-residual correction;
5. a symbolic error envelope `epsilon(lambda)→0`.

## Gap audit

- The theorem is exact, but no current repository artifact proves the required
  cofinal ambient lower floors.
- A conforming finite-element or Fourier compression gives an upper eigenvalue
  bound, not (T-14302.3).
- Complement coercivity must include all omitted modes.
- Superexponential `L2` prolate leakage does not automatically imply a small
  Weil-form residual.
- The countable criterion still requires one uniform asymptotic proof, not
  infinitely many unaudited computations.
