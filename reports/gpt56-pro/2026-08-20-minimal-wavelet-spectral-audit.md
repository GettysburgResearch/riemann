# Minimal-wavelet spectral audit after the priority-flux refutation

## Live state

PR #673 proves that the positive priority flux `UPBF67` is power-large and
therefore cannot close the normalized box. PR #674 removes that overpayment and
reduces the canonical scalar route to the ordinary-Mobius compact wavelet
`MWOC99910`.

This audit attacks that minimal gate and the separate positive-floor-kernel
proposal.

## Exact spectral identity

For

\[
F_\gamma(X)=\sum_n\mu(n)n^{1/2-i\gamma}K_0(X/n),
\]

the Poisson square is

\[
Q_X=\int|F_\gamma(X)|^2P_1(\gamma)d\gamma.
\]

The Mellin transform is exactly

\[
\widehat F_\gamma(s)
={\widehat K_0(s)\over\zeta(s-1/2+i\gamma)}.
\]

The compact wavelet has zeros only on the real-carrier boundary lines, so no
off-line zeta zero is cancelled. Weighted Mellin-Plancherel identifies the
L2 convergence abscissa as

\[
\sigma_2=\Theta+1/2.
\]

Consequently the critical cumulative energy

\[
\int_1^YQ_XdX/X^3
\]

is subpower exactly when RH holds. Cauchy--Schwarz then gives the forward RH to
MWOC implication; the one-sided Landau theorem of PR #674 gives the reverse
implication.

This explains all previous physical-collapse failures: an estimate of the
required strength is not a generic compact-support or diagonal theorem. It is
the reciprocal-zeta zero-free statement in a positive L2 coordinate system.

## Positive floor-kernel audit

For

\[
K_Q(x)=\sum_jq_j\lfloor x/j\rfloor,
\qquad q_j\ge0,
\]

Möbius inversion gives exactly

\[
\sum_m\mu(m)K_Q(N/m)=\sum_{j\le N}q_j.
\]

The corresponding zeta factor in the floor kernel cancels the Möbius
`1/zeta` factor. The resulting Mellin transform is `Q(s)/s`, so its automatic
positivity detects no zeta zero. This invalidates the conclusion-facing arrow
of T-100120 while preserving its elementary positive identity.

## Outcome

The attempted pass did not prove RH. It did prove that the current minimal
wavelet gate is exact and quantitatively RH-equivalent, and removed a false
finite-dimensional positive escape. Future work must introduce genuinely
arithmetic signed cross-core cancellation; rearranging the same source into a
source-blind positive kernel cannot suffice.