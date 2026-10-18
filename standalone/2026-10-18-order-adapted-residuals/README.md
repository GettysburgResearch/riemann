# Order-adapted inverse residuals

**Proposed source-qualified deductions. No RH proof or new zero-free boundary.**
The exact residual is E_A=L M_A-1, with the actual ideal-Mobius mollifier and every original family member retained. An actual zero contributes -1 to this residual, so a power-saving family average does not rule out a prescribed bad member.

The parallel #986 published the M6/R2/R4 mechanism and U^(11/15) second residual moment during this pass. This packet credits that overlap, uses its general fixed-order theorem, and supplies new order-adapted corollaries and exact method-threshold proofs. It does not claim the 11/15 result a second time.

## Results

At s=3/4+it, t in a fixed compact interval, for the full sixth-power-free ideal family of norm at most U:

| residual order | mollifier exponent a | auxiliary cutoff x | Holder parameter p | full error exponent |
|---|---|---|---|---|
| 2 | 3/5 | 3/5 | 3 | 11/15 (already #986) |
| 4 | 1/5 | 1/2 | 5 | **4/5** |
| 6 | 19/291 | 293/582 | 11 | **175/194** |

The sum is `sum_all |L(s)M_(U^a)(s)-1|^(order) << U^(error exponent+epsilon)`. There is NO cap and NO zero-selected deletion. The length changes with the order: this is not a stronger estimate for #986's same long A=U^(3/5) mollifier. All cutoffs, moment orders, field/ray data and real parts are fixed before U tends to infinity.

The fourth-order exponent 4/5 is the EXACT minimum of #986's displayed mixed-Holder envelope over all legal a,x and integer p. The proof treats both x<=1/2 and x>=1/2 and needs no numerical optimization. This is a limit of those upper estimates, not a lower bound for the actual arithmetic residual.

For every fixed character order n>=6, at s=3/4+it, a=x=(2n-6)/(3n-8) gives the full second residual exponent `2(n^2-2n-2)/(n(3n-8))`. It equals 11/15 at n=6 and formally tends to 2/3 as the field and character order change. This is not a zero-free fraction or an RH limit for one fixed function.

## The actual all-order boundary is now explicit

The present fixed-order envelope admits a strict power saving in its 2r-th residual moment precisely on

`Re s > 1/2 + [k_n(r/2)-1]/r`.

For n=6 the thresholds are 1/2, 7/12, 25/36, 3/4, 4/5, ... . From r>=4 onward the threshold is 1-1/r. This is proved as a necessary-and-sufficient condition for the ENVELOPE, not asserted necessary for the true moments. It prevents treating the fixed-order formula as a critical all-order theorem.

## Proof and validation

Read [PROOF.md](PROOF.md), especially Sections 4 and 6. The analytic foundation is the stated de Faveri sieve, the complete classical Hecke functional equation, and the fully stated #984/#986 adapters. Actual conductor dyads, both functional-equation sides, all ideal powers and nonunit masks remain. Principal rows are separated from the auxiliary dual estimate and included in the final residual sum.

`python replay.py` verifies the manifest, reruns the exact checker in ordinary and optimized Python, and runs eight deliberately corrupted optimized models. The checks use finite integer convolution and abstract sixth-root fixtures; they are NOT a number-field L-value census, a zero census, or an independent analytic proof. General identities and method-optimality are proved in the manuscript rather than extrapolated from test grids.

There is no independent referee, separately commissioned agent, Lean build or full-repository CI claim. Source and exploration limits are in [SOURCES_AND_VALIDATION.md](SOURCES_AND_VALIDATION.md).
