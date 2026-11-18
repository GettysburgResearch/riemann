# Round 15 — test-function boundaries, spectral signs and moving prime phases

Literature search cutoff: 18 November 2026 UTC. The archive now contains **1,009 selected works, 964 accessed full texts, 13 additional excerpt-only sources, 129 complete substantive readings, eight whole-work Level 3 audits, and 117 scoped adjudicated claim groups**. Its 473 theorem, conjecture and exercise records and 93 connections are separate from those paper counts. The catalogue has 1,010 works including one deferred supporting record. The 5,203 provider metadata matches are an overlapping discovery pool, not 5,203 reviewed works.

This round establishes a sharp boundary for one family of absolute zero-sampling estimates, supplies a smooth counterexample to an overly broad auxiliary explicit formula in a precisely pinned manuscript, and corrects a misleading inference in our own long-prime investigation. It also completes the whole-work audit of Gonek's 1984 derivative-moment paper and verifies two local spectral formula problems by exact witnesses. These are reusable mathematical deductions and version-specific repairs. Publication novelty has not been established. No proof or disproof of RH or new zero-free or zero-density exponent is claimed.

## A smooth test can defeat the stated raw height limit

The twelve-page author manuscript of Bombieri–Lagarias, *Complements to Li's Criterion*, pp.5–6, permits a piecewise continuously differentiable test with finite one-sided limits for both f and f′ at its finitely many exceptional interior points, and midpoint values for f. Its endpoint value decay is f(x)=O(x^delta) at zero and O(x^(-1-delta)) at infinity. It does not impose corresponding derivative decay at the endpoints. Its zero side is the raw symmetric height limit of the Mellin values h(rho), counted with multiplicity.

A fixed real smooth witness satisfies every printed local and value condition while that height limit fails. In logarithmic coordinates use disjoint bumps at integers j, amplitudes exp(-(1/2+delta)j), and suitably separated cosine carriers Gamma_j. Unconditional Riemann–von Mangoldt counting supplies arbitrarily high cells containing enough zeros. Choose each carrier so that its matching bump is positive on its cell, past bumps are negligible there, and its own transform is small on every earlier cell. Future constraints are summable. The final real part is greater than exp(-(1+delta)j)/5 on at least j exp((1+delta)j) zeros in the j-th cell. The symmetric height increments exceed 2j/5 and fail the Cauchy criterion.

This is an actual existence construction on the zeta zero multiset, without RH or any assumption about critical-line proportions. Its right-hand arithmetic and archimedean terms all converge absolutely. The obstruction is exactly the manuscript's stipulated raw summation mode. It does not transfer to the fixed compact jump tests used in the main arithmetic theorem, and it does not invalidate the generalized multiset criterion.

The same manuscript's finite equality (3.5), p.8, needs the positive term -(n/2)log(1-epsilon²). At n=1 and epsilon=2/3 the missing term is (1/2)log(9/5); the cutoff 3/2 is not a prime power. The correction is O_n(epsilon²) and disappears in the limiting theorem. A separate classical midpoint argument justifies the compact tests. An uninspected publisher PDF receives neither finding: both are pinned specifically to author-manuscript SHA-256 `cd13c8560f961c68e21256e5ba107bdd08fa7f34ce1e2cffbd4b63a16e8d48e0`.

[Complete construction, source scope and finite repair](../audits/adversarial_reviews/director_mellin_explicit_formula_round15.md) · `OBS-BL-RAW-HEIGHT-SMOOTH-COUNTEREXAMPLE` · `LEM-BL-FINITE-CUTOFF-COMPENSATOR`.

## Sufficient repairs and a sharp logarithmic boundary

Let h(s) be the Mellin transform of a continuous test with the preceding value decay. Integrate its weighted squared modulus over beta in [-epsilon,1+epsilon], where 0<epsilon<delta, and all real heights t. The following strip weights give absolute zero sampling and the ordinary compensated explicit formula:

| Strip weight | Condition | Absolute zero-tail bound, apart from fixed constants |
|---|---|---|
| (1+t²)^s | s>1/2 | N_s T^(1/2-s) log(2+T) |
| sqrt(1+t²) log^p(e+abs(t)) | p>3 | N_p log^((3-p)/2)(2+T) |

Holomorphic disk mean value controls the values on each height cell, including off-line zeros. Local zero counting and Cauchy–Schwarz then give the trace and tail. The director note records explicit constants in terms of any certified local zero-count constant. The norm also controls the interior Fourier trace. The first class gives a Hölder modulus at x=1; the second gives the Dini modulus O(N_p log^((1-p)/2)(e/abs(u))) in logarithmic coordinates. Cutoff, mollification and dominated convergence therefore justify the entire formula, including its archimedean singularity. No separate central-line trace assumption is silently added.

The logarithmic class is strictly larger than all the fixed s>1/2 polynomial classes, even among smooth source-admissible functions. A lacunary disjoint-packet example has finite logarithmic norm and infinite norm for every heavier polynomial weight. This example has a valid absolutely convergent explicit formula; it is different from the raw-height counterexample above.

The endpoint investigation goes further. **At p=3 there is a real smooth source-admissible function with finite strip norm but divergent absolute sum over the actual zeros.** Insert finite integer-carrier blocks in each disjoint spatial bump. In an enormous union of dyadic shells, use amplitudes lambda_j/[n(log n)²]. If S_j is the harmonic sum of the shell indices, choose S_j>=exp(4j) and lambda_j=exp(j/2)/S_j. Almost orthogonality of weighted integer translates makes the packet norm at most C exp(5j/4)/sqrt(S_j), which is summable for every choice of carrier signs. The function is O(x^(-4)) and vanishes near one.

Give the carriers independent symmetric signs. Every actual zero in each shell has a nearby integer carrier with a uniform Mellin-modulus lower bound. Dyadic zero counting forces a positive expected absolute contribution per block. Complex Rademacher moment inequalities and a second Paley–Zygmund argument convert this divergent expectation into a positive probability of an infinite absolute sum. Changing finitely many signs adds compact smooth tests with summable zero traces, so a tail zero–one argument even gives divergence for almost every sign choice.

This proves the threshold p>3 sharp **for a universal absolute-sampling guarantee in this norm scale**; the same witness applies to p<=3. It does not establish failure of signed symmetric height convergence at p=3. That weaker convergence question remains an explicit research problem. The construction is rigorous but uses impractically large carrier blocks; it is not a numerical test generator.

[Endpoint proof and three independent reviews](../audits/adversarial_reviews/director_critical_endpoint_round15.md) · `OBS-MELLIN-CRITICAL-LOG-ENDPOINT-ABSOLUTE-DIVERGENCE`.

A bounded primary-source comparison identifies a direct general predecessor: Luecking's 1986 Bergman embedding criterion, Theorem p.126, yields the same ambient analytic-strip thresholds after a conformal change and insertion of local zero counts. The archive's elementary proof supplies its displayed constants and explicit-formula bridge; the smooth real inverse-Mellin witness has additional physical constraints. A transcription of Weil's 1952 original text also retains decay of both the function and its derivative, clarifying the source of the missing endpoint control. Neither observation establishes priority for the specialized witness. [Exact predecessor, derivation, classical test spaces and search limits](../audits/adversarial_reviews/prime146_mellin_trace_prior_art.md) · [Luecking primary publication](https://doi.org/10.1017/S001309150001748X).

## Enlarging the factorability level repairs our earlier inference

The remaining genuine long primes in the signed C_* fourth-moment reduction still require cancellation in a moving additive Fourier mode. Two advances identify precisely which shortcuts remain available.

First, phase-blind progression norms alone do not imply the required projection estimate. On actual supported squarefree four-prime moduli k≈K, put P=KT and choose S≈K/log^4T rows. A centered cosine residue array with amplitude sqrt(P/S) has nonnegative row masses, arbitrarily strong fixed logarithmic savings in the sum of maximum errors, and total squared error of order PK. Nevertheless its required real projection is (12+o(1))sqrt(PS), too large for T log^4T when K≈T^(4b), b>1/8.

The rows have incompatible common-divisor CRT marginals. They therefore cannot come from one common prime sequence. This counterexample rules out an inference from the specified norm budgets and row conditions alone; it does not rule out estimates that exploit genuine cross-modulus arithmetic compatibility.

Second, our earlier unadmitted inference from a failure at the minimal support level to an obstruction to Pascadi's theorem was too broad. There is an exact positive theorem. For a nonempty finite prime band with largest prime p_*, the normalized coefficients of D(s)^m/m! are r-way 1-bounded well-factorable at level Q **if and only if**

```text
Q >= p_*^(m+r-1),     integers m,r >= 1.
```

For every real split Q=product Q_i, allocate the m prime slots among the factors using the capacities floor(log_(p_*)Q_i). The normalized prime-polynomial coefficients are bounded by one. A suitably chosen split below the threshold cannot represent the nonzero coefficient at p_*^m. This also proves exact necessity; complex cancellation cannot create a missing supported product. Completely multiplicative bounded twists preserve the upper bound, and preserve the lower bound when nonzero at p_*.

For m=4,r=3, padding to Y^(6b) fits the fixed-residue 5/8 range at the longest prime scale Y^(1+4b) whenever b<5/28, including every b<1/6 used here. A sharp dyadic restriction is not automatically factorable, and smaller modulus blocks need a separate exponent check. Most importantly, a fixed-residue theorem with a residue-dependent constant does not supply the simultaneous moving Fourier mode. That is the remaining mismatch, rather than failure of the full coefficient's factorability.

A concrete sufficient open estimate is

```text
sum_(k≈K,h≈D) abs(sum_(p≈P,(p,k)=1)
 (log p)^3 p^(-it) [e(-hp/k)-mu(q)/phi(q)])^2
 <= C T^(2-eta) K/D,       q=k/gcd(k,h), DP≈KT,
```

uniformly for abs(t)<=T^epsilon and some fixed eta>0. Cauchy–Schwarz costs T^epsilon sqrt(D/K), and Mellin separation of the taper costs T^(1-kappa). The strict inequality 1-kappa+epsilon<eta/2 would complete this sufficient step. It remains unproved for the genuine primes. All previous partial prime regions and the separate square threshold theta<9/17 retain their strict hypotheses.

[Full derivation, corrected failed inference and primary theorem comparison](../audits/adversarial_reviews/director_long_prime_round15.md) · `THM-PRIME-PRODUCT-EXACT-PADDED-FACTORABILITY` · `OPEN-CSTAR-LONG-PRIME-MOVING-PHASE-SQUARE`.

## Gonek's whole-work audit and an explicit input constant

Gonek's nineteen-page 1984 journal paper is the eighth whole-work Level 3 audit. The independently reconstructed shifted derivative theorem is unconditional in its actual fixed derivative orders and real shift window. Its conversion to derivative-square averages on the zeros uses RH. Multiplicities are retained; simplicity is not assumed. The leading derivative-square coefficient is T log^4T/(24pi), giving the corresponding strict weighted-tail leading coefficient.

Three local printed displays need repairs: the odd-order sign in an introductory continuous comparison; the extracted constant in an auxiliary stationary phase; and the reciprocal gap normalization in the final gap proof. The main discrete theorem already has the proper sign. A bulk-interval covering argument repairs the gap proof's use of shrinking initial arcs. An independently replayed exact rational certificate encloses its gap integral at 1.9 strictly below one. The main theorem and three corollaries survive; the findings do not label the entire argument invalid.

A modern unconditional PNT input makes one substitution explicit. Targeted reading of Fiori–Jaskari v2 gives, for r(u)=abs(psi(u)-u)/u,

```text
r(u) <= 4,
integral_1^infinity r(u) du/u <= 386015/19602 < 20.
```

Abel summation consequently bounds the difference between the von Mangoldt log convolution and its integral by 31(log x)^m+20m(log x)^(m-1), for real abs(delta)<=1/2. The second term is omitted when m=0. A displayed complex-shift variant keeps the finite-interval factor exp(abs(Im delta)log x) before extending the remaining integral. These constants apply to one step of Lemma 8, not to the whole contour argument or a practical derivative-tail onset.

[Gonek whole audit](../audits/adversarial_reviews/director_gonek_whole_round15.md) · [Exact gap certificate](../experiments/code/director_gonek_gap_round15.py) · [Explicit Abel transfer and source limits](../audits/adversarial_reviews/director_explicit_abel_round15.md).

## Two spectral formulas fail exact local tests

The complete v6 reading of Lagarias's Morse paper remains Level 1. Scoped independent reconstructions and actual publisher-page comparisons establish two narrow auxiliary findings in both the inspected v6 and journal versions.

The printed nonzero-shift family is equal to its Schwarz reflection. It therefore has equal moduli where the strict Hermite–Biehler inequality is asserted, already at h=1/2,z=i. Replacing its coefficient -i by +1 gives a compatible reconstruction with the separately defined zero-shift limit. That is our reconstruction, not an author-issued correction.

The explicit quotient called Herglotz in (6.2) has value **-i/(2e)** at u=0,z=i, contradicting its stated positive-imaginary convention. This invariant witness survives any relabeling of the real components. With the stated E=A-iB convention, the positive quotient is +B/A. A Green-identity reconstruction verifies the corrected sign. The main fixed-boundary Morse spectrum, Whittaker zeros and Appendix B energy-variable Weyl function are unaffected by these tests.

[Exact witnesses, both source hashes, independent reviews and theorem impact](../audits/adversarial_reviews/director_morse_scoped_round15.md). No whole-work Level 3 promotion or arithmetic operator construction is implied.

## What the new 2026 dependencies do and do not supply

Two source-backed dependencies were selected. Fiori–Jaskari, arXiv:2609.23222v2, has targeted Level 0 coverage of the unconditional absolute PNT bound used above; the entire fifty-page argument and its numerical optimization have not been audited. Conditional half-plane examples remain conditional.

Inumaru–Sugiyama, arXiv:2610.41394v1, received two complete independent thirty-page readings and remains Level 1. Its fixed-character continuous weighted second-moment density theorem uses compact Fourier support abs(u)<sigma/(sigma+1), fixed sigma in [1/2,1], and entire tests at complex ordinates. Its unconditional support-limited theorem is separate from the GRH appendix result. It is neither the discrete derivative-weighted zero law studied here nor a supply of the long-prime estimate. Small proof-level qualifications remain in its reading reports rather than being elevated to public author-error findings.

The third work added to the complete-reading count is the Bombieri–Lagarias author manuscript. Whole-work source reading, scoped proof checking and full adversarial audit continue to be counted separately.

## What a research team should work on first

The strongest new cross-paper interaction is the PNT-to-Abel transfer, whose output exactly matches one Gonek hypothesis. The new trace theorems and endpoint counterexample give a reusable analytic interface for positivity tests. The exact padded factorability result removes a false obstruction while leaving a sharply stated phase-sensitive arithmetic target. These lower the cost of deciding the next mathematical step; none supplies the last missing implication to RH.

The recurring barriers are control uniform in a growing parameter, summability before exchanging limits, positivity on a complete test space rather than finitely many examples, spectral sign and domain conventions, and arithmetic compatibility lost by abstract norm bounds. Historical transitions in the archive run from Riemann's analytic continuation and explicit formula through quantitative zero estimates, equivalent positivity and approximation criteria, finite-field purity, and statistical/spectral models. The current deductions reinforce the need to retain the exact bridge between those frameworks. A shared vocabulary or similar formula is insufficient.

The most useful immediate tasks are: decide signed symmetric convergence in the critical p=3 class; instantiate an explicit local zero-count constant and evaluate a usable trace tail for a positivity test; exploit genuine common-sequence compatibility in the moving prime phase; and complete numerical constants through the remaining Gonek contour steps. The [ranked twenty-five problems](top_25_research_opportunities.md) place these alongside the continuing approximation, geometry, spectral and random-matrix programs.

Known failed tests are retained: raw explicit-formula convergence under value decay alone; the implication from two phase-blind norm budgets to the required projection; and our minimal-level factorability exclusion. The endpoint absolute counterexample closes one research question while preserving its distinct signed counterpart. No new finding is called a historical discovery without a completed prior-art comparison.

The thousand-work mission remains unfinished: 880 selected works still have Level 0 coverage, and only eight have whole-work Level 3 audits. The original-language Riemann reconstruction and further analytic campaigns continue beyond this checkpoint. The persistent continuation guide and source manifests identify exact remaining work rather than replacing unread papers with summaries.
