# Sources, corrections, self-review and exact open targets

## Live repository sources inspected

All repository references below are research proposals, not automatically
accepted mathematics. Reading a proof is not replaying its checker or
reconstructing every upstream theorem. No old result is rebranded as new.

1. **#1000**, `6c4d5309d64978b420c2b897977d6db2ea01ce03`:
   `standalone/2026-10-18-primitive-positive-determinant/POSITIVE_DETERMINANT.md`,
   blob `6af94838b41d4351c804048e026e6e791b09c7c7`, read in full.
   The exact primitive cycle matrix, cyclotomic divisor identity, function B,
   and one-sided Landau consumer are credited. The new all-mass proof redoes
   the full variation argument; the original theorem restricted c to [0,1].
   Its delivered original ZIP was inspected locally; no duplicate recovery
   is included and no full new upstream replay is claimed.
2. **#994**, `c93ca65a510b6acaf167f929b9bf7e67d742b05a`:
   `standalone/2026-10-18-theta20-and-native-cancellation/native/PROOF.md`,
   blob `f8abf7967e8d71dfed4a506827401df96f6cdb34`.
   The complete coefficient factorization, low-denominator bounds, native
   crossing comparison and full core-sector estimate through Section 6
   were read. The new core-budget corollary imports that sector theorem.
   The full #848 sparse-cut growth theorem is NOT imported here; the new
   elementary recurrence theorem explicitly assumes an all-Y recurrence.
   The degree-20 construction was inspected at overview/PR scope, not
   independently recertified or rerun.
3. **#996**, `56ec8747ccf75d7fc19c2395a6523a664938b9f6`:
   `standalone/2026-10-18-quadratic-angular-all-order/PRIMITIVE_CORE_EQUIVALENCE.md`,
   blob `f5eeb80d337120f0bb042251bec0afb0e00ee618`, read in full.
   Its fixed-field split/inert correction and no-loss convolution transfer
   are credited. The present extension retains ramification with coefficient
   -1 and gives uniform kernels and a quantitative varying-field average.
   It does not claim the earlier split-prime primitive idea as new.
4. **#934**, `3092feee25c583ec760c5f14f4aa4c98d9c5df39`:
   `research/exploratory/2026-10-10-quasi-rh-wave/`.
   Its mechanism discussion is background already read in the preceding
   conversation; the live notes directory was checked in this pass.
   No whole earlier audit, exact cubic-theta source reconstruction, or
   physical multiprobe cancellation certificate is claimed here.
5. **#998**, `65a0e7e4016aad5aeb099973c0d079c6059a6c76`, was read at
   current PR-description scope. Its same-field Euler-mask averaging is
   different from the varying-field character average in this packet.
   No #998 critical upper bound is inferred or used.

The add-only parent #1000 and predecessor #993 were already published.
The final verification/push receipt separately records the new commit/tree.
Main, inherited files and integrated scientific status are not modified.

## Fresh primary literature and its precise role

- Baiying Liu, *Improved zero-free half-planes for the quasi-Riemann
  hypothesis*, arXiv:2610.12234v2, primary HTML:
  https://arxiv.org/html/2610.12234v2
  The abstract, main theorem and changed-moment-parameter explanation were
  freshly read. **Correction to the preceding chat:** v2 reports

      B_new=(18x+7)/(18x+9)=0.874957019420098946...,
      1188x^3-2160x^2+171x+190=0, 0.38858<x<0.38859.

  The earlier displayed `(1507-2sqrt(921))/1653` is B_alg, not v2's final
  benchmark. The improvement between them is about 5.04e-8. These are
  reported external results; their deep proofs/formalization were not
  rebuilt here. No new theorem in this packet uses that zero-free claim.
  Hypothetical intermediate targets must beat B_new, not the broader
  all-field 0.90333 proposal.
- Newman--Wu, *Lee--Yang Property and Gaussian Multiplicative Chaos*,
  Communications in Mathematical Physics (2019), DOI
  10.1007/s00220-019-03453-0:
  https://link.springer.com/article/10.1007/s00220-019-03453-0
  Primary text was consulted for the real-zero closure framework. The
  fixed-band counterexample and the one-exponential-budget proof in this
  packet are proved directly, not attributed to a theorem for a larger
  class than the source treats.
- de Faveri--Dunn--Hoffstein, *Non-orthogonality of the cubic and quartic
  large sieves via Rankin--Selberg*, arXiv:2607.07911v1:
  https://arxiv.org/html/2607.07911v1
  Primary abstract/introduction used for the existence of genuine Gauss
  bias and nonorthogonality. No detailed large-sieve inequality is an
  input to the elementary paired-probe theorem.
- de Faveri--Pandey, arXiv:2610.01035v1:
  https://arxiv.org/html/2610.01035v1
  Primary introduction inspected as an exponential-sum lead. No faithful
  square-root-phase adapter for the native rough-core source was proved,
  so this paper is NOT an analytic premise of the Newton argument.

Classical inputs used explicitly in the new proofs are quadratic Gauss-sum
Fourier inversion, squarefree divisor inversion, cyclotomic factorization,
Dirichlet/Dedekind factorization, the elementary real nonvanishing of zeta,
Montel/Hurwitz, ordinary Mellin transforms, and Landau's positive-transform
argument. The detailed bounds are derived in the notes. No novelty of these
classical tools, exhaustive literature search, or world-record claim is made.

## Self-review corrections and failure boundaries

**Common factor:** every individual field product contains the zeta zero,
but arbitrary combinations of residues could cancel. The actual positive
statement is the complete finite coefficient comparison to mu6. A moving
family is transferred to that fixed source BEFORE a Mellin argument.
The r=1 divisor channel remains explicit. Treating it as a cancellable
nonprincipal character term would assume the desired arithmetic conclusion.

**Small fields:** the positive paired series for chi_-3 and chi_-4 justify
removing known real Mellin modes in their PRINCIPAL Dedekind functions. This
is not asserted for every quadratic field or every auxiliary Hecke twist.

**Paired probes:** one notch loses a vertical lattice of possible target
poles. The two irrationally related notches share only the known zero-free
real point. A quantitative polynomial-height lower bound is supplied.
The fact that a Gauss first mean has a real main term does not mean the
entire binding Gram covariance is that main term. That adapter is OPEN.

**Narrow strips:** a rare-jump sequence refutes moment/variance-only normality.
One exponential moment at R>1/2 repairs the zeta transfer, but its budget
must be enforced. No new target moment realization is certified here.

**Native recurrence:** the exact denominator/core source is retained. A root-
norm cost is paid before squaring. The sparse crossing comparison is not
silently treated as an all-Y recurrence. The adaptive core cutoff buys a
smaller complement; it does not estimate that complement.

**Determinant:** the right mass coordinate is N arcosh(1+t/2), not N sqrt(t).
At growing mass the earlier bounded-c approximation is insufficient. The
exact B counterterm is retained. Its bulk is now order N^((5+theta)/2),
larger than N^2; improved conditioning trades against that subtraction.
The long heat tail is paid, but the centered short-time trace remains OPEN.
Matrix positivity in the regularization variable says nothing by itself
about Riemann-zero locations.

## Five next targets, not ongoing background jobs

- OPEN-Q: estimate the complete signed field mean at a power theta< B_new,
  with Q at least X^(5/2-2theta); retain the common channel and exception cost.
- OPEN-PROBE: obtain both exact physical filtered identities and a strict
  signed power improvement for their complete remainders.
- OPEN-S: construct cofinal actual-theta approximants with zeros in a fixed
  narrower band and one uniform exponential-moment budget.
- OPEN-N: bound the energy-adaptive high-core remainder strongly enough for
  a valid full recurrence, or independently certify the requisite sparse-cut
  native-growth theorem and its application.
- OPEN-D: bound the mesoscopically regularized centered height at
  N^(1+theta+epsilon), with its full larger B bulk and short heat window.

These are actionable proof obligations, not claims that agents are still
working. No independent agent/human referee or formal proof assistant was
used. The author performed a separate self-audit and wrote the checker.
