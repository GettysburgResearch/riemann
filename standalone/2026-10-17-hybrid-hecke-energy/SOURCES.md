# Sources, overlap, and dependence

## Live repository inputs

- #953 at a93d382951f8fac7b0c28783061a7ddb99fcf0a4:
  standalone/2026-10-16-divisibility-covariance/THEOREMS.md, read in full
  from the supplied archive and compared with the live PR description.
  Its Sections 4--5 provide the two-pole SQUARE-COEFFICIENT series and the
  diagonal expansion used in Theorem 4 here. These constants are inherited.
  https://github.com/GettysburgResearch/riemann/pull/953
- #952 at 3b7d2948840446c752bbf284f6f90f6592395a29:
  standalone/2026-10-16-critical-gaussian-energy/ENERGY_THEOREM.md, read from
  the supplied archive. Gaussian pair kernel, coefficient counts and the
  crude full-tail estimate are reconstructed in the present argument.
  https://github.com/GettysburgResearch/riemann/pull/952
- #954 at 3241178607671c4dd979cefdad0670fd426194da:
  standalone/2026-10-16-norm-collision-energy/THEOREMS.md, live read covering
  its statements, tensor-square count, critical coefficient comparison and
  Gaussian preliminaries. It already proves full NORM collisions and the
  Mellin-only mean; those are not new here. Its exact higher-degree formal
  comparison strategy is credited in HIGHER_MOMENTS.md. No #954 analytic
  theorem is required as an unproved premise of our spacing proof.
  https://github.com/GettysburgResearch/riemann/pull/954
- #936 primitive arithmetic helper, retained in #952's critical-power packet:
  Git blob 64d21a7f400f5bf5654fd67735743ff1befab067. The Eisenstein/Z[zeta_6]
  distinction and residue algorithms were inspected. check_hybrid.py is a
  fresh self-contained implementation, NOT a byte copy or independent
  mathematical referee. Its exact arithmetic uses the omega basis throughout.

The live AGENTS.md and STATUS.md were read at the #953 source. Recent PRs were
searched for overlap, including angular/hybrid descriptions; this was not an
exhaustive reading of the entire historical repository. No older all-cusp,
theta, quasi-RH, zero-free, or native-moment assertion is imported into the
new upper-bound proofs. Other branches are not merged or promoted.

## Classical primary literature checked for attribution

1. M. N. Huxley, The large sieve inequality for algebraic number fields,
   Mathematika 15 (1968), 178--187, doi:10.1112/S0025579300002540.
   Publisher extract inspected: multidimensional exponential-sum separation
   and number-field large sieves are established classical ideas.
   https://www.cambridge.org/core/journals/mathematika/article/abs/large-sieve-inequality-for-algebraic-number-fields/DF941BA0756AAB8081FCE03F606B907B
2. M. N. Huxley, The Large Sieve Inequality for Algebraic Number Fields. II:
   Means of Moments of Hecke Zeta-Functions, Proc. London Math. Soc. (3) 21
   (1970), 108--128, doi:10.1112/plms/s3-21.1.108. Publisher metadata inspected;
   the complete paywalled theorem text was not obtained or audited.
   https://doi.org/10.1112/plms/s3-21.1.108
3. Daniel White, Extreme values of Hecke L-functions to angular characters,
   arXiv:2208.02309. Abstract inspected as primary evidence for the established
   imaginary-quadratic angular-character family and its geometric diagonals.
   Its resonance theorem is NOT used here; HTML body retrieval failed.
   https://arxiv.org/abs/2208.02309

The written proof supplies its own Gaussian Poisson identity, class-character
extension, lattice Schur bound and coefficient comparison. Standard inputs
are unique ideal factorization, finiteness of the imaginary-quadratic class
group, geometry of its fixed lattices, finite abelian character orthogonality,
and elementary integral/convolution results. The new full-average secondary
term additionally uses #953's explicitly reproduced positive-zeta residue
calculation. No full external analytic theorem or formal library was rebuilt.

## Claim scope

This is new work relative to the inspected recent packets, with classical
methods explicitly identified. It is not a claim to have improved the best
published general hybrid large sieve, nor a certified historical novelty
claim. The additional angular and class averaging change the measured family.
Their parameter-volume cost is stated next to every full moment conclusion.
