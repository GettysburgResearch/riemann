# R-32301 — Eta zero modes block generic strict boundary contraction

Claim ID: `R-32301`  
Title: The propagated unshifted eta state has exact multiplier one at every zeta zero, so no transform-faithful generic strict contraction can close the RH-sensitive boundary channel  
Status: **PROPOSED COMPLETE STRUCTURAL FIREWALL — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: PR #317 `L-30501/L-30502`; elementary Dirichlet-series algebra  
Scope: rules out a class of generic contraction completions; does not refute source-specific signed recombination and does not prove RH

## 1. Exact propagated symbol

PR #317 isolates the only propagated state after exact terminalization of the discrete `-1` shift. In logarithmic coordinates it is convolution by

\[
\beta
=\sum_{k\ge1}
\left[(2k)^{-1/2}\delta_{\log(2k)}
-(2k+1)^{-1/2}\delta_{\log(2k+1)}\right].
\]

For a complex Laplace frequency `z` with `Re(z)>-1/2`, Dirichlet convergence gives

\[
\widehat\beta(z)
=\sum_{k\ge1}\left[(2k)^{-z-1/2}-(2k+1)^{-z-1/2}\right].
\]

Writing `s=z+1/2` and

\[
\eta(s)=\sum_{n\ge1}(-1)^{n-1}n^{-s}
       =(1-2^{1-s})\zeta(s),
\]

one obtains exactly

\[
\boxed{\widehat\beta(z)=1-\eta(z+1/2).}
\tag{R-32301.1}
\]

No asymptotic or zero hypothesis enters this identity.

## 2. Every nontrivial zeta zero is a unit multiplier

Let `rho` be any nontrivial zero of zeta. Then

\[
\eta(\rho)=(1-2^{1-\rho})\zeta(\rho)=0.
\]

Therefore at the corresponding logarithmic frequency

\[
z_\rho=\rho-\frac12
\]

one has

\[
\boxed{\widehat\beta(z_\rho)=1.}
\tag{R-32301.2}
\]

Thus the exact propagated eta operator has no spectral reserve whatsoever on the RH-sensitive exponential mode.

This is true for zeros on the critical line and for a hypothetical off-line zero.

## 3. Consequence for contraction-based closures

Consider any translation-compatible Banach or Hilbert function space in which compactly truncated exponentials

\[
F_L(t)=\chi_L(t)e^{z_\rho t}
\]

with a plateau of length tending to infinity are admissible and in which boundary layers have lower-order norm than the plateau. On the plateau, convolution by `beta` acts as multiplication by `\widehat\beta(z_\rho)=1`; only the two cutoff collars differ.

Consequently

\[
\frac{\|\beta*F_L\|}{\|F_L\|}\longrightarrow1.
\tag{R-32301.3}
\]

Hence no estimate of the form

\[
\|\beta*F\|\le\theta\|F\|,
\qquad \theta<1,
\tag{R-32301.4}
\]

can hold uniformly on any transform-faithful state space containing arbitrarily long localized representatives of the zeta-zero modes.

In particular, a finite-jet or boundary-renewal argument may have a strict reserve on analytic or source-restricted sectors, but it cannot close the complete RH-sensitive propagated state by a source-blind homogeneous contraction.

## 4. Relation to the live proof graph

This explains a recurring pattern in the post-#300 carry branches:

- PR #324 proves strict `6/7` contraction for the analytic power/faster-power interior;
- PR #316 proves every fresh cap injection has only polylogarithmic native central-flow debt;
- PR #317 proves a strict weighted-jet estimate for smooth eta inputs;
- nevertheless the complete propagated boundary channel repeatedly resists a uniform all-generation contraction.

Equation (R-32301.2) shows that this resistance is structural rather than a poor choice of constants.

A successful completion must exploit additional source-specific information before taking a norm, for example:

1. signed recombination of the exact arithmetic boundary state;
2. first-entrance/first-exit fragmentation before the sign;
3. Pascal-cycle optimization coupled to the actual Möbius source;
4. a reflected physical square retaining the zero mode before carry cancellation;
5. another mechanism which is not a uniform contraction of the bare eta propagation operator.

## 5. What this does not say

This result does **not** contradict the finite weighted-jet estimate of PR #317. That theorem applies to a restricted smooth jet class and includes a derivative export. It also does not contradict the analytic `6/7` contraction of PR #324, whose power-series sector does not contain arbitrary localized zeta-zero exponential modes.

Nor does (R-32301.2) prove that every source-specific recurrence is impossible. It rules out only the generic source-blind contraction strategy.

## 6. Proof boundary

Closed here, subject to review:

1. the exact eta propagation multiplier;
2. unit multiplier at every zeta zero;
3. the resulting approximate-eigenmode obstruction to a generic uniform strict contraction.

Still open:

1. a source-specific signed recombination theorem for the propagated cap-interface state;
2. a complete transition-band or cycle certificate;
3. RH.
