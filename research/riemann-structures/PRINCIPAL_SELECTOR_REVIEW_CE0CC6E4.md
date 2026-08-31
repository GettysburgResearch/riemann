# Independent review of the principal-selector gauge obstruction

Scientific checkpoint: `ce0cc6e48e3cdaedd9d5f52fb087b03e8f86c257`.

Reviewed packet: `PRINCIPAL_SELECTOR_GAUGE_OBSTRUCTION.md`, `principal_selector_gauge_obstruction.py`, its JSON certificate, and `tests/test_principal_selector_gauge_obstruction.py`.

## Finding

No unresolved blocker was found for the stated uniform source-operator obstruction. The packet identifies an actual prime-square gauge entry for which canonical conductor reselection produces a power-size weighted norm loss. It does not give a counterexample to the full principal moment, or place both input and output in one unchanged physical shell.

## Independent mathematical and source checks

I read the complete proof, implementation and nine tests, and inspected the principal weight in frozen T-106140. The weight is `g^2*ell*rho*c_ell*c_rho`. If a prime `p` in the opposite residual core is inserted on the left, the new common core is `p*g`, the right residual core loses `p`, and its least prime must be recomputed. The physical gauge coefficient is `-tau*(1-tau)/(4p)`, up to the explicitly retained unit phase. Combining it with the weight gives the exact cocycle in the proof.

When `p` was not the old least residual prime, there is no conductor jump. The example instead removes the least prime three, revealing a prime `C` of size `T`. Its weights are `45` and `(135/2)*C*c_C`; at parameter one half, the squared weighted entry is `C*c_C/1536`. Since the physical horizon is `40000*T^4`, this supplies the stated norm lower bound of order `H^(1/8)` for the declared operator.

The prime-window inequalities are strict and imply the asserted before/after ratio bounds. I raised the shell issue during review: a width-eight window cannot contain both `N` and `9N`, regardless of whether each separately compares to `M` within a factor eight. The frozen proof explicitly uses the finite-horizon direct sum of the two shell blocks and retains their tags. It does not promote this example to a single fixed-shell assertion.

The Boolean coefficients are live: the two original three-prime cores have balanced coefficient minus two, and the new left four-prime core has coefficient plus two, for every cutoff between fifteen and the four large primes. The operator image retains its gauge-history provenance. It is not identified with a fresh owner reallocation at a different depth; the latter would need its own coefficient adapter. The gamma normalization, stripped unit phase, and Mellin phase are separated explicitly.

I checked the two integrated controls. A constant parameter path gives squared ratio `C*c_C/2880`. The literal projected bilateral Euler path is `tau^4*(1-tau)^6`, and the beta-integral ratio is `B(11,15)/B(9,13)=273/5060`, giving `91*C*c_C/161920`. Mellin integration preserves each one-entry norm ratio because the added phase has modulus one. This does not equate the old and new off-atomic Gram entries or assert a positive full signed moment.

## Independent code review

The producer authenticates all named historical blobs, and rehashes the frozen Boolean algebra before executable compilation. It uses exact integer/fraction arithmetic for common-core extraction, least-prime selection, quadratic classes, physical products, the canonical weights, and the gauge cocycle. The four fixed large primes are checked by bounded trial division; there is no new prime search. Complete Boolean allocations establish the declared nonzero support rather than relying on a formal core value alone.

The fixture uses the integer floor of the sixth root of its horizon. The proof's support argument only requires the displayed strict small/large split, so a comparable dyadic cutoff has the same Boolean rows; the fixture is not falsely described here as itself a power of two. The tests include nonleast-prime insertion, physical-shell separation, gamma denominator transport, exact root endpoints, illegal source records, type/resource limits, and refusal of unauthenticated executable or malformed certificate data.

## Execution evidence and remaining boundary

I did not execute the producer or tests. The coordinating agent reports Ruff, complete write/check, optimized check, nine ordinary tests and nine optimized tests all passing. The reported proof-object hash is `f360d9aaf7f87832faa8cf9eae1d8b4fe2cb5e416da4468f6644be9ae3323a7a`.

The result rules out a uniform subpower bound for the stated canonically reselected weighted gauge operator. Other source columns can interfere at an output, differentiated transport also requires the connection term, and the complete carrier/renewal assembly may have additional structure. The open T-106140 estimate and RH remain untouched. The constructive value is locating the precise least-prime-removal transition that an admissible weighted transport must address.
