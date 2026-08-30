# Independent review of the quadratic signed source boundary

Scientific freeze: `c0b197918936d8ad360f462702855020fb26ac67`.

I independently read the five-file packet in `koszul-analytic-parent/`: `QUADRATIC_SIGNED_SOURCE_BOUNDARY.md`, `QUADRATIC_SOURCE_REPLAY.md`, `quadratic_source_boundary_replay.py`, its verification fixture and 25-test source. I reconstructed the general signed-boundary argument, checked the S4 geometry against the separately reviewed `c67d858f` source, and inspected the final authentication prefix. No test or producer was independently executed by this reviewer. Root reports focused Ruff, ordinary/optimized producer checks after final binding, and 25 tests in each Python mode passed.

## Mathematical assessment

No remaining blocker was found under the stated hypotheses.

The general theorem requires both a nonzero quadratic anti-invariant H1 rank and identity as the only group element acting scalarly on both inputs. These conditions matter. The final note includes separate genuine-source counterexamples: a genus-zero quadratic cover with zero anti-cohomology, and trivial inputs on the actual S4/chi_u pair with anti-rank sixty but every selected L-function equal to one. The latter cancels the omitted signed scalar resonances and prevents an overbroad claim from regular anti-rank alone.

The source Hilbert sum uses actual finite cohomology and dual multiplicity spaces. Its polynomial grade growth gives every Schatten class exactly for grading modulus below one, and an ordinary determinant entire in the arithmetic variable. This is distinct from the exponential-growth Koszul Lie parent. The full joint inertia, not a product of separately selected invariant spaces, defines the ramified local trace.

For the signed boundary, the identity coefficient is the integer source count difference `Delta_m=#Ztilde-#Z=-tr(F^m)` divided by the group order. The actual invertible anti-Frobenius gives infinitely many nonzero Delta_m. Its weight bound controls the later multiples of each such order by a quantity tending to zero; integrality prevents cancellation of the first nonzero term. Primitive roots of those unbounded orders are dense. Positive radial constants grow faster than a pole, and negative constants decay faster than a finite-order zero, so either obstructs meromorphic continuation. The proof does not need positivity, a nonzero constant at every root, prime orders, or an assertion for arbitrary complex arithmetic parameter.

The S4 specialization retains diagonal infinity inertia and the two-dimensional standard/sign-standard twisted stalks even when their first traces vanish. The ranks 6,6,4,10, anti-rank60, genus49, conductor identity, finite-grade duality exponents and source curve factors match the geometric packet. The resulting stacked zero radii and reciprocal accumulation at zero obstruct a fixed-grading reciprocal equation with a finite rational prefactor; alternative infinite completions are not excluded.

## Replay and source precision

All frozen producer/proof/artifact/source pins are authenticated by commit, Git blob and normalized hash before either runtime import or artifact read. Their helpers recursively authenticate the earlier source chain. This adapter recounts only extension degrees one and two, over fields of order at most49; higher polynomial data are explicitly inherited from the frozen geometric source.

The code checks full graded local traces against the actual constituent data with the correct weight `z^m`, includes infinity's second Frobenius power, and keeps the twist applied once after forming the grade. The p5 degree-ten determinant and sixth-trace held-out status are retained. The p7 prefix is allowed only through four traces and is refused for full determinant or higher-power operations.

The independent grade-log and cohomological power-log calculations use separate proved tails, including the actual grade-zero vanishing for chi_u. The rank-sixty signed tail has the correct conservative coefficient25. Exact finite functional equations are checked in a bounded range; the infinite boundary and purity are proved, not inferred from that range. Input types, cache entry, source forgery, partial-source promotion and the zero-first-trace counterfeit have explicit controls.

## Scope

This is a function-field arithmetic adapter and a signed noncancellation theorem for a specified graded completion. Finite-cover cohomology, duality and weights are imported classical theorems. The scalar products belong to the classical multiple-q-factorial genre; source-specific regular-count coefficients and their cancellation controls are the substantive boundary content. There is no number-field/archimedean transfer, new RH/GRH theorem, universal fixed-grading functional equation, or external priority claim.
