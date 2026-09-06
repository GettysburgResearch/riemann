# Exact sources and literature boundary

This is an author submission, not an independent review of PR #805.
No external novelty or priority is asserted. Nyman--Beurling criteria,
Vasyunin duals, Mobius damping, Mellin--Plancherel, and Euler-factor algebra
are classical. The source-specific contribution proposed here is the
explicit bounded operator convolution for the preceding parity optimizer,
its full-norm comparison and growth-exponent consequence.

## Resident source

Repository: GettysburgResearch/riemann. PR #805.
Parent commit: `0f8724bbd86c1de8f40eacbf30129321e0ebc8aa`.

1. `standalone/2026-09-06-astra-dilation-observability/PROOF.md`:
   discrete step space, finite-support duals, source-complete finite gain.
   Git blob `7d95febb1b72125c82d53a028f6ae6085781262f`.
2. `standalone/2026-09-06-astra-block-gain/PROOF.md`:
   exact odd-detail optimizer, the full lift and finite coupled obstruction.
   Git blob `0a276d31f68b188b43589fbfdc66c91880de7e43`.

The current PR/head was read through the authenticated connector. The second
proof was fetched by blob and read in full. Both local proof files are
byte-bound in SOURCE_LOCK.json. The mathematics needed by the new proof is
restated, not imported as executable code. No unpublished reviewer result
is a dependency, and no historical scientific status is changed.

## Primary analytic sources consulted

* Luis Baez-Duarte, *A strengthening of the Nyman--Beurling criterion for
  the Riemann hypothesis*, arXiv:math/0202141v2, 18 February 2002.
  https://arxiv.org/abs/math/0202141
  https://arxiv.org/pdf/math/0202141
  Read the full seven-page text, with page images for the analytic lemma
  and norm convergence. Lemma 2.1 quotes Balazard--Saias verbatim: the
  zero-free half-plane hypothesis is essential. Section 2.2 proves the
  RH-conditional damped Mobius norm approximations; Corollary 3.1 records
  their equivalence criterion. In our variables x=1/t, his L2(dx) is our
  L2(dt/t^2). The conditional identification preceding his final limit is
  not dropped when reusing that limit.
* Michel Balazard and Eric Saias, *Notes sur la fonction zeta de Riemann, 1*,
  Advances in Mathematics 139 (1998), 310--321, Lemma 2.
  Used through the precise quoted Lemma 2.1 above. The original proof was
  not separately inspected or reproduced. This remains an external
  analytic input, not a tested finite predicate or a custom formal axiom.
* NIST DLMF 25.9.1--25.9.3, especially 25.9.3, sourced there to Titchmarsh,
  *The Theory of the Riemann Zeta-function*, second edition, p. 88.
  https://dlmf.nist.gov/25.9
  https://dlmf.nist.gov/25.10
  Section 25.10(i) also supplies classical existence of critical-line zeros
  for the nonconvergence proof; no numerical zero location is used.
  At the critical line the two sums have length sqrt(t/(2pi)), and the
  functional-equation factor has modulus one. Absolute summation gives
  the unconditional O(t^(1/4)) bound used in PROOF.md. No Lindelof bound is
  assumed. This is a cited established asymptotic formula, not a new result.
* Michel Balazard, *An arithmetical function related to Baez-Duarte's
  criterion for the Riemann hypothesis*, arXiv:1812.04309.
  https://arxiv.org/abs/1812.04309
  The step-space dictionary and Vasyunin biorthogonal system are classical;
  Proposition 10 gives the target approximation criterion. The duals are
  reconstructed directly in the new proof. The squarefree support statement
  is a consequence of that dual system and Baez-Duarte's damped construction,
  not an assertion of priority for a new approximation criterion.

* Ethan Simpson Lee and Nicol Leong, *New explicit bounds for Mertens
  function and the reciprocal of the Riemann zeta-function*,
  arXiv:2208.06141v4, 26 July 2024.
  https://arxiv.org/html/2208.06141v4
  Only the classical asymptotic shape in introduction (1) is imported for
  PROOF.md section 9. The introduction and statement of Theorem 1.1 were
  inspected. Their explicit constants, numerical zero input, tables and
  certificate computations are not consumed or replayed here. The derived
  full-norm bound likewise has no certified numerical constants.

Standard background used explicitly: completeness of Hilbert space,
Cauchy--Schwarz, Mellin--Plancherel, summation by parts, locally uniform
Dirichlet-series convergence, the analytic identity principle, zeta's
functional equation and nontrivial-zero existence. These do not assume RH.
No zero table, numerical zeta evaluation, or certified zero prefix is used.

## Boundaries

The previous nonzero coefficient at index 9 concerns the exact finite
optimum. It never proves that omitting 9 prevents asymptotic approximation
of chi. Conversely omitting any squarefree index has an explicit
finite-support separating witness. Ambient density, target approximation,
and finite optimality must remain separate in summaries.

The exact growth exponent contains the unknown Theta; it is not an
unconditional proof that Theta=1/2. The uniform full-source gain is a
stronger quantitative goal whose implication from RH is not established
here. The operator transfer removes no original arithmetic correlations.
