# Remaining work and review order

## What would actually finish one of these routes

There are several sufficient targets, not several completed estimates:

1. Prove E_N->0 by constructing coefficients and controlling all three terms
   in the actual head/ramp/tail decomposition. In the exact Schur version,
   derive a nonsummable lower gain under L>0 on a weighted-divergent set of
   scales. A generic norm-to-correlation argument cannot see the persistent part.
2. For the prescribed logarithmic Mobius coefficients, prove Q_N=N^{o(1)} at
   all sufficiently large lengths. By the N^2 cutoff, it suffices to bound the
   explicitly stated cumulative divisor-discrepancy sum. An even more focused
   alternative is subpolynomial best-linear-fit psi variance; its consumer is
   classical-strength and its upper bound is still unproved.
3. Construct a bounded defect-space reflection with the required reciprocal
   dilation eigenvalue consequence. The formal functional equation and its
   unbounded reflected evaluation do not supply that operator.

The exact prime-power Schur formulation is useful for the first two only with
its composite correction retained. Periodic diagonalization alone fails, as
proved by the norm-separation example. The full spectral-synthesis question is
a worthwhile structural task but is not a necessary prerequisite for the
individual-zero obstruction or the length-averaging consumer.

## Review before extending

Begin with Chapter 03's pole-canceling Mellin/Poisson--Jensen argument: check
normalization, the half-plane, the nonzero derivative at 1, and the direction
of the inequality. Then check Chapter 05's real-length interpolation and
meromorphic continuation, including all-length control and multiplicities.
These are the two central consumers of arithmetic estimates.

Next review the bound used to certify optima, then the large-sieve tail in
Chapter 04 with duplicate Fourier frequencies combined. Distinguish its use of
periodic means for a tail bound from the invalid whole-metric substitution.

Review Chapter 06's change of basis, exact source Lambda, the negative-distance
control, and the all-cutoff separation theorem. Check that a Schur complement,
not a principal submatrix, is used to eliminate composites.

For the last packet, review the signs in <b_n,d_r>=-delta_nr, the squarefree
support qualification, the adjacent-divisor term, and the three orthogonal
subspaces. Check the trace estimate and inverse inequality direction separately.
The psi-variance consumer should be read with its upper-bound hypothesis visible.

The dynamics chapter is a motivation and a set of equivalent or conditional
formulations. Verify which assertions concern the continuous flow, the adapted
discrete map, and literal zeta composition. A numerical picture cannot decide
monodromy or all zeros.

## Useful bounded tasks that do not masquerade as completion

A rigorous continued-fraction Gram evaluator would improve arithmetic access,
but it must be paired with an actual solver/storage plan; no 10^5 certified
claim should appear until executed. A proof-assistant formalization of the
finite dual identities could eliminate sign and indexing uncertainty, but
would not formalize the open source estimate. Independent interval replay of
N=512 and 1024 would validate finite receipts, not unbounded decay.

The original question also motivates visualization of inverse branches, prepole
sets, flow centers and synthetic off-line quartets. Such software should label
literal versus adapted dynamics and avoid using only on-line zeros as though
that were a complete zero census. The separate Observatory PRs are related
software context, not dependencies of the proofs in this packet.

## No hidden promotion

No theorem here converts finite agreement, the bound D<0.00327777, dual
completeness, trace<11, or a favorable source-free spectrum into RH. The
substantive remaining step is arithmetic cancellation or the proposed bounded
operator compatibility. The packet exists so the next researcher can start
from the strongest correctly qualified statement rather than repeat a refuted
shortcut or mistake a more precise formulation for an established estimate.
