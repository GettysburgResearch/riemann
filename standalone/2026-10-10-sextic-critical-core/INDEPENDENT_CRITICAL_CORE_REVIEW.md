# Scoped review of the critical-core research

Review date: 2026-10-10. Review signed by research agent `/root/audit_formalization`. This is an AI-agent mathematical audit, not human peer review or proof-assistant verification. The reviewer is distinct from the authors of the coupled completion, negative-branch quotient, anisotropic core and polynomial-horizon notes. Two notes authored by this reviewer are identified separately below; their hash bindings do not constitute independent self-review.

The reviewed results include exact arithmetic identities, source-conditional estimates for specified components, a new controlled incidence portion, a squarefree-row high-value bound, and a native arithmetic rate criterion. They do not prove the full short-row fourth moment, a new zero-free boundary, or RH. No unresolved must-fix was found in the versions bound here, subject to the retained analytic inputs and the review-role distinctions below.

## Bound versions and review roles

File names are relative to this report. A change to any bound file requires review of that change.

| File | Bytes | SHA-256 | Role |
| --- | ---: | --- | --- |
| COUPLED_THETA_COMPLETION.md | 18030 | `f3b57f69338e8736ffe4addd5a6e2ebf6d5f8976ee9d2fda5921c83ff484eb36` | Independently reviewed |
| NEGATIVE_BRANCH_DIRICHLET_SERIES.md | 8685 | `025b1f9507f7aff3794d93e80a10337e61732944ec3ba1cb28107c8a7d59326e` | Independently reviewed |
| ANISOTROPIC_SINGLETON_CORES.md | 8894 | `4854a01c2767a1dc4d7c67c490e5502bcad8935bce3089ba5f37adb1e6d02ea8` | Independently reviewed |
| POLYNOMIAL_CRITICAL_HORIZON.md | 7072 | `664cffb7738fc9cce5d5bd81916e10e5760dff0072fefeb55a2d96317cf0c4a6` | Independently reviewed |
| REFLECTION_SCALAR_AUDIT.md | 5533 | `17bdce731735412cc463c50c944df9240736e5797282f2c5a4eed5a07b2e21e2` | Authored here; independently reviewed by another agent |
| HIGH_VALUE_SCALAR_OBSTRUCTION.md | 7768 | `de996cf077718d2ba9af351eb998337e8c5c63c8f9ed36bfaf0225128c1dc061` | Authored here; independently reviewed by another agent |
| LOG_FREE_REPLICATED_SPIKES.md | 11753 | `b59978c1c5d3b5cb904c7f22d675a67bb71b2af512db9f0577e568a04565a86b` | Independently reviewed |
| REUNITED_RAMANUJAN_EULER_PRODUCT.md | 9791 | `6d1f0e01d8645972de0c38897e37633d8bfc70d193f6e279dcf8f33b0e992433` | Independently reviewed |
| PRIMARY_SOURCE_MATCH.md | 7394 | `c4162dc668980d44c115e67868393fc43230d78a0fdacf73ff05abcc8a200258` | Independently reviewed source scope and divisor identity |
| README.md | 12653 | `aefca7502e38c0f2e912f2689d0bcc1a250536538d3e9ef2136bc6af95879807` | Independently reviewed synthesis, quantifiers and multiplier corollary |
| adjacent-sources/README.md | 1430 | `7ef9c382fa59641f1fef9ab37a1aebbac2f806ad7aa172cd1095fe06428367d1` | Independently reviewed statement scope; snapshot Git verification by parent |

The inherited baseline is PR 913 at `6498d6cc2eded03159c7332b25fd224ad07f89c1`. Source statements from OpenAI's October 5 manuscript were checked at its pinned commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. The adjacent PR 911 and PR 912 statements used by the horizon note were read from the exact local copies identified in its source paragraph and adjacent manifest. Those source identities are retained inputs rather than silently replaced by stronger statements.

## Coupled completion: what was independently checked

The complete note was read against the imported definitions of the completed sum, the full reflection formula, theta support and coefficient bounds, weight-derivative bounds, local Ramanujan factors, and reflection scalar. The source's automorphy and analytic continuation proof were not rebuilt in this pass.

The normalized balanced completion has the asserted cube-free face. The external character supplies its literal coprimality zero, and Gauss CRT restores the coefficient of the squarefree product. The exact scalar audit retains the angular factor from the source's scalar, so cancellation of the cubic Gauss factors leaves an angular weight and a cubic cross-symbol. The additional original character changes the latter to a quadratic cross-symbol. No variable phase is absorbed into a constant.

The three-term local Ramanujan identity and the allocation to e, f and g are exact. In particular, the negative g term is present even at divisibility points; it does not impose coprimality with the dual theta index. Reindexing the squarefree theta part by e and the cube part by f gives the stated normalization and the scale Y = H^2 E G^2 / (B F). The repeated squares leave the compulsory row mask at e and f. The normalized theta coefficient is bounded only after its cube growth and ramified factor have been included.

The product-column quadratic lemma correctly separates the repeated prime gcd before applying the squarefree quadratic sieve. Its coefficient mass is G divided by the squared gcd norm, up to a subpower. Minkowski then costs one logarithmic sum and one convergent sum. It never replaces the square of a character by one on a nonunit.

For the every-cusp component bound, the e and f count contributes the stated square of their number under Minkowski; the cube index has bounded inverse-norm mass on each dyad. The resulting terms are H E / G and H^2 A^2 / (B F^3). The theta ramified valuation is at least -4, so the finitely many negative valuations and the geometric decay at positive valuations are both controlled. Scales below one are handled through the nonzero rapidly decreasing tail, not by applying a sieve at an invalid length.

One substantive scope issue was repaired during review. The source's reflected theta support allows primary n and b to meet the fixed bad set. The final note keeps this support. It freezes only the finitely many squarefree bad-prime patterns of n before using the good-prime sieve; the cube index remains unrestricted and its character stays in the sum. Thus the every-cusp theorem does not discard reflected bad-prime powers. The stronger second-sieve theorem explicitly concerns only the stated good standard-cusp face.

The standard-cusp formula retains its supplementary cubic factor at lambda. That factor splits between e and the remaining squarefree index and therefore does not obstruct separation. The moving row mask in the quadratic–cubic lemma is expanded by its divisor identity, followed by divisor Cauchy on each row. This order avoids an unjustified unrestricted triangle sum. The six resulting divisor weights have exponents 3, 2, 8/3, 2, 1 and 5/3; only the exponent-one sum is logarithmic.

The smooth separation is uniform for both sieve arguments. After fixed ray splits, the smooth dependence is a function of compact dyadic norm ratios through the original compact weight and the transformed weight. The source bounds for each fixed logarithmic derivative of the transformed weight give a common integrable Mellin majorant, including rapid decay in the parameter 3^m U C^3 / Y. The varying row norm contributes a bounded Mellin phase. Angular and Gauss phases remain arithmetic coefficients and are not differentiated as smooth norm functions. Separation precedes the relevant norm inequalities.

The final standard-face bound H E + Y + (E Y)^(2/3) follows with the displayed normalization. In the all-squarefree-divisibility component with A = B = D, it reaches D^(2+epsilon) for H at most D. This is a strictly larger range for that specified component. The all-negative component and the adverse fourth-moment initialization remain outside the resulting full estimate, as the note explicitly states.

## Negative-branch quotient: the exact domain matters

This note was read in full. The surviving negative coefficient has infinity type -3. Its angular part is not a finite-order twist. The complementary Gauss-series character has infinity type +2. The note maintains those distinctions throughout.

The three absolute-convergence series multiply exactly, with no coprimality imposed among their g, n and b indices. The numerator's cube Euler factor has ray character rho cubed and angular type +3. The squarefree Gauss series retains its nonmultiplicative cubic cross-symbol and is not falsely declared an Euler product.

The original standard-face coefficient, including the supplementary lambda factor, gives exactly the two Mellin arguments s = 1/2 + t and w = 1/2 + z - 2t. The initial contours require Re(t) greater than 1/2 and Re(z) greater than 2 Re(t) + 1/2. These are sufficient for absolute convergence of all three series and for the stated interchange. The imported transformed weight has a Mellin transform and sufficient vertical decay there.

The quotient uses the source's defining completed Dirichlet series as a formal absolutely convergent object; it does not invoke the finite-order reflection theorem for an unproved angular generalization. A functional equation for the reciprocal would require the matching conjugate character, all conductor and gamma factors, and a further relation between the two Mellin variables. The displayed relation z + t = -1/2 is a codimension-one condition, not an identity of the double integral. No continuation or gain is inferred from the product representation alone.

## Reunited Ramanujan product and its continuation domain

REUNITED_RAMANUJAN_EULER_PRODUCT.md was independently read in full. Its fixed theta index is the original unreindexed squarefree n. Thus its a and b sums reunite every Ramanujan allocation on the stated standard face, including the squarefree-index divisibility contribution; the argument does not impose an unstated coprimality between a, b and n.

The two local factors, distinguished by whether the prime divides n, are exact. Multiplication of the angular characters of types -3 and +3 cancels their infinity types and leaves the finite-order character eta times rho cubed. The sixth power of the quadratic cross-symbol retains its zero at the moving row primes. Consequently the extracted finite-order L-factor retains those imprimitive Euler factors.

The remainder is defined by an infinite product away from n and separate finite factors at n. It never divides by a potentially vanishing numerator factor. Normal convergence follows from the two prime-summable errors of orders q^(-Re(w+v)) and q^(-2 Re(v)), with the denominator bounded when Re(w) is positive. The domain Re(w) greater than zero, Re(v) greater than one half, and Re(w+v) greater than one is sufficient. The finite n factors have the uniform bound (Nn)^(max(0,1-Re(w))+epsilon). Classical Hecke continuation then gives a fixed-index meromorphic identity, without assuming a zero-free half-plane.

The fixed-index pole example is valid. For n = 1 and trivial eta and rho, on v = 1 and Re(w) greater than one the remainder factors are individually nonzero and form an absolutely convergent nonzero product. The denominator is nonzero by its Euler product. Apart from the discrete zeros of the angular numerator, the finite-order factor therefore gives a genuine simple pole of this fixed-index function. The note correctly does not infer an uncancelled pole after the theta-index or finite-ray sums, or a lower bound for the original smoothed polynomial.

The exact Mellin coordinates are w = v - 3t and s = 1/2 + t, with scale factor A^(v-1) times (Nk^2/(cAB))^t. This exposes rather than removes the adverse independent norm ratio. The stated sufficient absolute-convergence region for the deformed n sum forces Re(v) greater than 5/2, far from the new divisor at v = 1. The equivalent condition on z_M - t is explicitly restricted to the case 0 less than Re(w) less than one. No useful simultaneous contour shift follows from these elementary product bounds alone.

## Anisotropic singleton cores

The combined forward Euler correction and moving mask were checked coefficient by coefficient. Outside the mask, the nonconstant coefficient is one minus the number of active axes; at a masked prime it is one. This gives the exact finite smooth convolution, including rows with a vanishing local character.

The absolute coefficient product converges when every axis weight is positive and each pair has sum greater than one. Its moving-mask cost is a subpower of the mask norm, uniformly in the mask. No small-prime enlargement or inverse correction is needed for this direction. The application legitimately places weight 1/2 on one axis and b greater than 1/2 on every other axis.

The proof keeps the selected axis fixed after each scale dilation. It therefore uses precisely the inherited smaller-rectangle second moment, rather than a changed smooth test or a second moment at an unstated scale. Pointwise estimates on the other axes must be uniform in the moving row. The note distinguishes the elementary b = 1 case from the additional common zero-free input required for b below one.

The resulting core energy H P Q^(2b-1), with Q the product of all axes except the largest, and its aggregate incidence version were independently recomputed. The harmonic pair-overlap cost and summable higher overlaps are the same exact sums as in the inherited incidence identity. The k = 3 configuration with singleton scales comparable to (D, 1, 1) is genuinely outside both previously controlled ranges while lying in the new portion. At k = 2 the balanced configuration receives no new range. No stronger full-moment consequence is claimed.

## Polynomial critical horizon

The new proofs and the interfaces to the inherited negative-mass and zero-free-to-Mertens statements were checked. The full proofs of those inherited adapters were not independently rebuilt in this pass.

The main expansion is uniform in the small power increment. Its error estimate uses the strict positive margin b - (1 + delta_0)/2 and the independent tail denominator 1 - b. The two boundary/integral terms are added; missing plus signs in the initial draft were repaired. The lower bound for the positive leading coefficient and the resulting polynomial horizon follow with constants independent of the increment.

The converse differentiates the finite arithmetic sum with respect to its power, not with respect to its activation variable. The derivative bound is uniform in the required small increment. Choosing the increment at the assumed horizon yields the claimed negative-part bound. The A = 2 endpoint has only logarithmic integrated growth and fits the inherited negative-mass criterion.

The horizon infimum identity keeps all positive buffers and does not assert attainment at the endpoint. Its restriction to exponents at least two is explicit. The conversions from a hypothetical sextic moment or the inherited zero-free line are consequences, not new moment or zero-free estimates. The ordinary native detector alone is not presented as a theorem about every sextic twist.

## Positive-density replicas and log-free spikes

LOG_FREE_REPLICATED_SPIKES.md was independently read in full, with its cited universal-test and exact replica interfaces. The limiting average of the inverse-mask recurrence kernel follows by dominated convergence from conditional rough-base divisibility densities. Its Euler product converges for every positive amplitude exponent. Enlarging the fixed roughness set then leaves a positive proportion of bases with a contractive kernel. The constants depend on the fixed row and roughness set, not on the moving base.

The record-scale argument transfers a fixed-row large value to a positive-density population of sixth-power replicas at the same scale. The proof works for every fixed positive h; it uses elementary ideal counting and does not require prime-ideal density. The improved spike denominator loses no logarithm. The sufficient exceptional-set condition is correspondingly a little-o of D^(h/6), with constants allowed to depend on the fixed row. The continuous-scale induction is valid because every nontrivial recurrence divisor reduces its argument by at least a factor two.

The endpoint moment corollary applies Holder to the same base family and averages its recurrence kernel before induction. It produces the stated fixed-row exponent without an unstated logarithmic or epsilon loss. The finite-order moment profile uses the separately stated, conductor-uniform reciprocal bound and the imported second moment only at scales where that moment is assumed. It is correctly identified as a consolidation rather than a new arithmetic upper bound. The final version explicitly defines log(0) as minus infinity in the limsup.

## Authored notes and separate cross-checks

REFLECTION_SCALAR_AUDIT.md was authored by this reviewer after independently deriving the full active-prime product from the source. Its identity was cross-checked by the completion author and parent research agent, and independently reviewed directly against the source by `/root/map_existing_riemann`, which confirmed the bound final hash. Its publication hash here records the exact dependency used by the independently reviewed completion; it is not represented as independent self-certification. The calculation is restricted to the stated coprime squarefree mixed local branch and retains every fixed-ray factor, the angular weight and the original external character.

HIGH_VALUE_SCALAR_OBSTRUCTION.md was authored by this reviewer and independently reviewed by `/root/map_existing_riemann`, which confirmed its final frozen hash after editorial repair. That review checked the actual m-fold product coefficient mass, the unrestricted physical-index use of the Gram theorem, the high-value inequality, its optimized squarefree-row fourth-moment consequence, and the scalar compatibility example.

The squarefree-row bound is an actual consequence on that subset, conditional on the inherited second moment. It does not purport to include the other rows. Its improvement occurs in the explicitly stated intermediate range, not at the desired near-linear scale. The abstract spike assignment is only a witness that the collected scalar majorants do not imply a stronger bound; no actual sextic/Möbius polynomial or common coefficient vector is claimed to realize it. The assignment needs no exceptional sixth-power rows, which explains why merely removing them would not resolve this particular limitation.

Two carriage-return math delimiters and a doubled comma in the authored note were repaired before its final binding. A binary scan of the bound theorem notes found no remaining control characters other than tabs and newlines. This is editorial validation, not a mathematical certificate.

## Exact local diagnostic: source review and independent replay

The following bindings identify the final local checker and its output. They are finite local checks, not an analytic theorem certificate.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| checks/check_local_identities.py | 10017 | `d4fa6751c832591de4a0759e26ab8923d713f342263741d2ee8f2b7ef8219fc4` |
| results/local_identity_checks.json | 2120 | `a521eb5db925b30606faa7687cd8c94a4f69d5bcc501d93bc9871c00bbae2d7a` |

The code was read in full. Its finite fields use the Eisenstein quadratic relation, and its cyclotomic arithmetic reduces exact integer coefficients using the sixth-root quadratic relation and the p-th cyclotomic relation. The two coefficient components are independent for the seven fixtures, whose rational primes are distinct from 3. The source Fourier normalization is handled by storing q times the local Fourier coefficient; the unnormalized Gauss products and both sides of the local reflection consequently have matching powers of q.

The fixtures are the two split primes over each of 7, 13 and 19, and the inert field of norm 25. Each fixture checks all field residues in Fourier inversion and in the local j = 1 and j = 4 transformations, for the script's explicitly selected nonzero epsilon and sigma parameters. It also checks Gauss products, multiplicativity, inverses, the Ramanujan allocation's repeated-prime zero mask, and moving Euler coefficients for two through six axes with local exponents zero through three. This is precisely finite fixture coverage; it is not an exhaustive test over all fields or all epsilon/sigma parameters.

The initial checker used Python assertions for acceptance. All such gates were replaced by explicit conditional exceptions before this binding. This reviewer reran the final script in ordinary and optimized Python. Each reported 14,224 counted exact predicates; both resulting JSON files matched the saved output byte for byte. A temporary copy with the local q-minus-one Ramanujan factor deliberately changed to q-minus-two was rejected in both modes, without a passing output artifact.

The checker does not establish the global Gauss/alpha normalization, a CRT theorem at arbitrary composite conductor, a large-sieve bound, normal convergence, or any infinite moment assertion. The global normalization and CRT manipulations were reviewed mathematically against the displayed source formulas. Replay of this one script is not a second independently implemented finite-field package. Its local exact arithmetic and the scope of its acceptance output are the claims authenticated here.

## Final synthesis and primary-source comparison

The final README was checked against the bound proofs. It explicitly fixes the finite-order character and bad-prime set, distinguishes the original and dual row lengths, restricts every component table entry to squarefree dual rows, and retains the stronger estimate's standard-face restriction. The native positivity conclusion explicitly uses a positive power increment. The adverse initial dual scale and the unresolved full moment are visible alongside the component gains.

The README's additional outer-multiplier corollary follows from the reviewed proofs. A row-independent subpower coefficient can be absorbed after freezing e,f in the every-cusp argument, and after freezing f,g in the standard-face argument. It only changes an arbitrarily small power allowance; no norm derivative is taken. The corollary is not applied to the separate exact Euler identities, which keep their literal coefficients.

PRIMARY_SOURCE_MATCH.md was read in full. The two pinned family 023 Git blobs were read directly. The cited Dunn–Radziwill periodic/angular theta statements and specialized cubic-twist statement were opened in the primary paper, as were Chinta–Gunnells' coefficient construction, local functional equation and global continuation theorem. The note correctly distinguishes the scope of those results from the unproved coefficient match for this deformed series. This is a bounded source comparison, not a proof that no relevant theorem exists.

The finite-divisor deformation identity was recomputed. Its prime coefficient is (q x - z)/(1 - x + z). The denominators and the base remainder product are nonzero in the stated initial region; the character zero masks persist. Re(s) greater than one and Re(w) greater than one suffice for the full absolutely expanded outer sum. The identity supplies no extension to points where its new denominator vanishes and no unproved summable moving-conductor estimate.

The adjacent-source overview accurately retains the original files' status and source-tree link conventions. This reviewer checked the interfaces named in the new proofs. The separate verification of all twelve snapshots against their pinned Git objects was performed by the parent agent; that provenance is not represented as a second complete replay by this reviewer.

## Retained verification boundaries

The imported theta transformation, its cusp coefficient and smooth-weight estimates, the imported inverse second moment, and the established character large sieves remain explicit analytic inputs. This review does not independently prove the upstream quasi-Riemann result or the completed theta automorphy theorem. The older review and source qualifications must remain attached to those dependencies.

No Lean kernel build, formal proof certificate, zero search or numerical asymptotic inference was performed for this review. Exact rational spot checks supplemented the displayed exponent algebra; they do not replace the proofs and are not advertised as a theorem checker. The central unresolved task remains cancellation sufficient for the full short-row moment, including the difficult coupled branch and every row stratum.
