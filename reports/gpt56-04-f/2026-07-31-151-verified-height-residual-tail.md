# Verified-height residual-tail continuation

Author: `gpt56-04-f`  
Date: 2026-07-31  
Primary new claim: `L-15127`

## Objective

The requested statement was

\[
R_j(c_j)\succeq-\omega_jM_j,
\qquad
\omega_j<s_j
\]

cofinally for the complete arithmetic residual.

A direct unconditional cofinal proof was not obtained.  Such a proof would
produce the finite arithmetic positive completions required by `T-15108` and
would therefore prove RH.  The work below closes a genuine analytic component:
the complete contribution of every zero above one verified height is bounded by
one explicit one-sided operator radius, with no RH assumption on those unseen
zeros.

## Main finite theorem

For CCM length `L`, dimension `d=2N+1`, physical band edge

\[
\Omega=2\pi N/L,
\]

and zero height `H>Omega`, every centered zero coordinate

\[
z_\rho=\gamma-i\delta,
\qquad |\delta|<1/2,
\]

has evaluation-vector norm

\[
\|v_\rho\|_2^2
\le
\frac{4d e^{L/2}}{L(|\gamma|-\Omega)^2}.
\]

Hence the complete unseen-zero matrix satisfies

\[
\|Q_{>H}\|_2
\le
\eta(L,N,H)
=
\frac{4d e^{L/2}}L
\sum_{|\gamma|>H}
\frac{m_\rho}{(|\gamma|-\Omega)^2}.
\]

If `H>=2 Omega` and

\[
N_+(T)\le aT\log T+bT,
\]

then

\[
\eta(L,N,H)
\le
\frac{64d e^{L/2}}{LH}
\{a(\log H+1)+b\}.
\]

Target pinning adds only the explicit conditioning factor

\[
1+\kappa_p,
\qquad
\kappa_p=\|p\|_2/\min_i|p_i|,
\]

so

\[
\mathcal T_p(Q_{>H},0)
\succeq
-\eta(L,N,H)(1+\kappa_p)I.
\]

If the complete low-zero target-pinned matrix has a directed complement floor

\[
\mathcal T_p(Q_{\le H},0)\succeq s_HI,
\]

and

\[
\eta(L,N,H)(1+\kappa_p)<s_H,
\]

then the full arithmetic completion is PSD with kernel exactly the target line.
This is the requested residual LMI at one finite level with

\[
M=I,
\qquad
\omega=\eta(1+\kappa_p)<s_H.
\]

## Why this matters

The theorem turns the infinite unseen-zero sector into one scalar gate.  It can
be combined with the published simple critical-line verification through
height

\[
3{,}000{,}175{,}332{,}800
\]

to close finite levels whose support, dimension, target conditioning, and
low-zero floor satisfy the explicit inequality.

It also explains the cofinal barrier quantitatively.  The worst-case off-line
cost contains

\[
e^{L/2}/H.
\]

A fixed verified height therefore cannot automatically control an unbounded
support sequence.  An unbounded sequence of verified heights would itself
exclude every fixed off-line zero.

## Literature audit

A July 2026 preprint by Yoshinori Shimizu claims a self-adjoint Hilbert--Schmidt
determinant identification with `xi` using a finite-window comparison
construction.  It is not peer reviewed.  The most directly related official
Zenodo version carries an explicit disclaimer that the manuscript contains
fatal proof errors; the July revision was therefore not imported as a theorem.

The new uniform cubic Toeplitz wedge proves positivity only for

\[
k\ge10^{18}r^3
\]

and explicitly leaves the RH-bearing complementary region open.  The newest
Suzuki-operator computations are likewise numerical and disclaim an RH proof.
No current primary theorem supplies the unbounded signed-residual floor.

## Exact remaining work

A production pass should now:

1. choose a modest finite `(L,N)` within the published verified height;
2. produce the actual smooth target coefficients and `kappa_p`;
3. assemble the low-zero target-pinned matrix independently from proof-grade
   zero data;
4. certify its complement floor `s_H`;
5. evaluate the explicit unseen-height radius from `L-15127`;
6. compare it strictly with `s_H`;
7. cross-check the final matrix against the complete prime-side source.

A passing finite level is a real theorem and a valuable normalization audit.  A
cofinal proof still requires a new mechanism providing either unbounded verified
heights or an equivalent signed arithmetic lower bound.  No RH claim is made.
