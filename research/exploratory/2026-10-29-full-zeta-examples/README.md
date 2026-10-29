# Three source-qualified full Dedekind-zeta rectangles at 0.874

**Status.** These are conditional density-one family consequences, not individual zero-free half-planes. They combine the locally compiled and fresh-Lean-replayed Dirichlet candidate at `θ=4369347/5000000`, interpreted conventionally, with the cited rectangular-sieve, buffered-detector, common-profile and height replays. Tracker admission, independent external-kernel verification and an independent mathematical audit of those analytic replays remain separate. The named prior comparisons are not an exhaustive novelty search.

Let `σ=437/500=0.874`, so `σ>θ` but `σ<7/8`. In each row below, K is the stated cyclotomic field, L/K is the indicated cyclic extension, and L ranges over one fixed box of coprime squarefree ideals at conductor scale `X`. The exponent a means that the two squarefree ideals A,B have norms `≈X^a` and `≈X^(1−a)`; a=0 means A=1 and B is squarefree. For each fixed ε>0 the cited calculations give a sufficiently small τ>0 for the zero rectangle `Re s≥σ`, `|Im s|≤X^τ`. Exclude the simple pole at 1. In a corresponding top-scale discriminant box the results are:

| K | [L:K] | a | Exceptional fields | Fields in the box |
|---|---:|---:|---:|---:|
| Q(i) | 4 | 31/375 | O(Y^(163/900+ε)) | ≫Y^(1/3) |
| Q(ζ₅) | 5 | 29/300 | O(Y^(51/400+ε)) | ≫Y^(1/4) |
| Q(ζ₁₁) | 11 | 0 | O(Y^(1328/31735+ε)) | ≫Y^(1/10) |

Here `Y` bounds the absolute discriminant, and the height in the discriminant formulation is `Y^τ′` for a sufficiently small τ′>0 depending on the fixed family and ε. The quoted cardinalities refer to a single top-scale box, not all number fields below Y. The exponent gaps imply density one inside each stated box. The number of fixed ray sectors and class-field character-to-field fibers is bounded in each fixed family. The lower counts use the [squarefree-box counting argument](../2026-10-29-squarefree-box-count/README.md); in the quartic case a quadratic core can have a subpower number of factor assignments, which is absorbed in ε.

For the **full** ζ_L, the base factor ζ_K is controlled by the candidate's Dirichlet statement: `ζ_Q(i)=ζ L(χ₋₄)` and `ζ_Q(ζ_p)=ζ∏_(χ mod p, χ≠1)L(s,χ)`, with primitive factors. The remaining factors of `ζ_L/ζ_K` are controlled by the source-qualified family density estimates. Thus a relative-quotient zero-free rectangle becomes a full ζ_L rectangle for these bases at this σ. This use of the Dirichlet candidate does not require the separate Eisenstein-Hecke interpretation.

The source arguments, conductor–discriminant identities, local character powers and field counts are documented in [the quartic continuum](../2026-10-29-quartic-relative-continuum/README.md), [the quintic example](../2026-10-29-fourth-moment-prime-fields/README.md), and [the degree-11 example](../2026-10-29-all-prime-relative-fields/README.md). Those notes also specify the imported analytic conditions and internal reviews. At fixed height, the cited de Faveri natural-index exponents for the same boxes in X are respectively `179303/305700`, `6181293/9915500`, and `2100479/4803751`, above the new exponents `163/300`, `51/100`, and `2656/6347`; the broad Khale et al. comparator is `252/437` for each. A sufficiently small power-height loss preserves each strict comparison. These comparisons do not establish priority over every possible theorem.

Hu's preprint claims a broader all-height unitary-Weil half-plane `Re s>7/8`; that claim is not independently verified here and does not itself cover σ=0.874. The cited Liu preprint's claimed all-field finite-order threshold is also to the right of 0.874. The candidate and density replays retain their explicit qualifications.

[check_exact.py](check_exact.py) checks the displayed rational exponents, relevant affine endpoints, β margin and named-source comparator arithmetic with exact fractions. It does not prove the analytic sieve, detector, class-field identities, or a formal admission.
