# Bounded downstream audit of the fixed-core owner-range import

Read-only audit on 2026-08-31. Scope: named claims at `86cac1d64364015ec2cc0f8fbb6fc75dc041c12b`, their full-core parent at `ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, the current PR765 source at `5b25f2dace65dd4d46e16d566f2dc7a34b98f41d`, and the continuation's reviewed packet files. This is not a repository-wide dependency validation or a fresh validation of every inherited RH implication. No computation, source mutation, fetch or merge was performed.

## Finding and exact scope

L-102958 uses full physical cores `a=gc,b=gd` and proves `Q<=2a,P<=2b`. L-106124 explicitly uses reduced cores c,d but imports `Q<<c,P<<d`. The factor g cannot be absorbed into an implied constant uniform in g. Its residue-cell lemma is valid on the stipulated smaller owner intervals. Its claim that the complete physical source occupies those intervals is not justified, and the resulting uniform native application of equation .5 with an additional `1/g^2` is false on the declared canonical coefficient class.

The corrected full-range Hilbert estimate has factor `(ell+2gc)(rho+2gd) <= 9g^2 cd`. Inserting the physical coefficient and source-dual weight gives a local upper bound of scale `X^o(1) ell rho/(cd)`, rather than `X^o(1) ell rho/(g^2 cd)`. Frozen dense owners have `P,Q` of order U squared and `c,d,g` of order U, satisfy the actual full-core and physical-shell constraints, and produce a fixed-class observed energy bounded below by a constant times `log(U)^(-8)`. A direct quadratic-Gauss Cauchy comparison retains a conservative factor at least 9/16. This contradicts the proposed uniform extension of the old bound, not its correctly restricted abstract lemma.

## Direct later references and their impact

I searched the named archival claim tree for L-106124, its numbered equations and aliases, then read the matching consumers and the conclusion-facing identity/diagonal proofs.

| Statement read | Impact of the range correction |
|---|---|
| L-106124.1--.5 | The full-source range import and advertised uniform extra common-core saving require correction. The interval estimate remains correct when its shorter ranges are actual hypotheses. |
| Corrected L-106123, retained-local section and correct-use list | Its assertion that the complete owner packet has the L-106124 estimate must specify the true ranges or use the corrected weaker bound. The already-retracted global positive conductor closure is not revived. |
| R-106123, section 1 | The abstract formula explicitly assumes the short ranges and remains true there. Its assignment of that range to the entire literal source needs the same qualification. Its conductor-family counting warning and retraction remain valid; they do not rely on the lost common-core saving. |
| R-106122, section 5 and status table | The elementary fixed-core fact that a sufficiently large modulus forces equality of owner products remains true for a specified owner interval. Calling the full local application of L-106124 retained needs qualification. The physical-squareclass identities and varying-core counterexample are unaffected. |
| R-106124, retained-results list | Its separate atomic phase-cardinality correction is unaffected. Its blanket listing of L-106124 as retained should distinguish the true interval lemma from the false full-source range import. |
| L-106120, section 5 | The actual least-prime inequalities and full-core owner comparability remain true. The prose that no local owner/core obstruction survives must not be interpreted as the reduced-core, uniform `1/g^2` phase-energy estimate. The source partition, two Ramanujan phases and tensor identity use no such quantitative bound. |
| T-106121 | Its broad dependency list includes the local sequence, but the inspected conclusion follows from exact channel geometry, conditional principal domination and the independently derived principal diagonal. No use of L-106124.5 occurs in that argument. |

The older L-106125 still carries a misleading historical status in its own text, but its varying-core closure was already explicitly retracted by R-106122. That separate defect must not be presented as a newly discovered consequence of this range correction.

## What does not change merely because of this finding

L-106121 derives the principal atomic entry bound directly from `ell<=c,rho<=d` and the literal coefficient, producing `X^o(1)/(g^2 cd P Q)`. This is an entrywise diagonal calculation, not the coherent local phase-energy bound of L-106124. The new range issue does not invalidate that calculation. Its assumptions about complete source measures remain a separate inherited obligation; this audit does not newly certify them.

L-106131's finite sign-pair operator decomposition and literal Wick subtraction, L-106190's connected inclusion-exclusion, and L-106191's exact source-dual rescaling do not use a short owner interval. L-106191's references to L/R-106123 are warnings that a global conductor estimate remains necessary, not imports of a proved `1/g^2` coherent-energy estimate.

I read T-106130 and T-106140 in full for this question. Their exact connected/Wick identities, direct principal atomic calculation, and conditional conclusion chains do not quantitatively use L-106124.1 or .5. Their remaining signed global estimates are still open. The finding therefore does not turn those open frontiers into completed results or refute their conditional algebraic implications. It removes a claimed uniformly stronger local estimate that a future proof might otherwise mistakenly use.

The function-field complete prime-shell theorem L-106130 uses a polynomial Dirichlet L-function and its explicit formula. It contains no common-core range import and is unaffected by this finding. Transport through incomplete incidence masks was already explicitly left open there.

## Current predecessor and continuation packets

The current PR765 canonical Boolean diagonal and decoder diagnostic contain no L-106124 citation in the inspected files. Their diagonal proof is an arithmetic coefficient square-sum, and the decoder remains explicitly open. The new complete-positive-candidate lower bound concerns its subsequent readout and does not rely on the faulty local estimate.

Searches of the continuation's native packet files and tests found no L-106124 import outside the new correction itself; the reviewed GLO scientific paths also contained no such reference. More substantially, the earlier reviewed arguments use explicit full-core support, actual coefficients, direct kernel/phase identities, or directly proved operator bounds. FCM/NMO already allow owner products much larger than the reduced phase cores. Source-first completion uses the direct ratio `ell rho c_ell c_rho/(cd)`, not a surviving common-core saving. PQR, OAC, dense-owner and complete-fibre results derive their energies or bounds from the literal source coefficients and original measure. The gauge, marked-owner and arithmetic-geometric packets likewise do not appeal to L-106124.5.

This is a source-level dependency check of the named reviewed arguments, not an exhaustive automated transitive theorem graph. No previously frozen scientific file needs silent alteration to accommodate the finding. Publish the precise range correction and qualify future uses of the affected local claims; retain the existing identity/conditional-frontier boundaries.
