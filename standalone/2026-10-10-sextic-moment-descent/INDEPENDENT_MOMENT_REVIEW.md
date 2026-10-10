# Independent review of the moment-research components

Review date: 2026-10-10. Reviewer: a second research agent, distinct from the authors of the four initial bound theorem files. The collaborative contribution and additional independent review of the Gram adapter are identified below. This is a mathematical source and proof audit, not human peer review or kernel-checked formalization.

The reviewed components give useful exact reductions and proved partial ranges. They do not prove the near-linear-row fourth moment, the exponent 17/24, the unbounded diagonal moment hierarchy, or RH. No unresolved must-fix was found in the versions bound below, subject to their explicitly retained analytic inputs.

## Bound versions

File names are relative to this report. Copying these files without modification preserves the review binding; any changed byte requires review of that change.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| README.md | 14631 | `940d8a9b096b42457bafead7d59aa1786a023a7c68451a8e72cd979d043ec34c` |
| FOURTH_MOMENT_ATTACK.md | 37899 | `354e8f7f5f81d0f8821ea6e821f55546f9c9641ac0690def1ae373000b4b3d08` |
| GENERAL_MOMENT_ATTACK.md | 27326 | `a4ca15c0d731ef6000b19507b39b64a4786a7f8af9939864b3176221bf02b499` |
| ALL_ROW_SIEVE_AND_GCD_TAIL.md | 9589 | `08c78f5127829e4b02e6dcf058cefc1bd22e5149f9bcca2f287edea7857897bf` |
| REFINED_ALL_ROW_SIEVE.md | 17097 | `6879e094fb63969ddc88c637bf633cf46360d144d2b1615573647e734b4141e8` |
| MOMENT_OBSTRUCTIONS.md | 31027 | `663c6ac878eb0fdd865389ac066ff5a23dbb33016e7061384a83fd186be3fd9b` |
| SEXTIC_GRAM_BOUND.md | 15156 | `c2b6c326f929de85a4f6d50ae2f4bdf4fc089f4f4705961d1c59ea1ad35d4fe1` |
| GRAM_MOMENT_COMPOSITION.md | 6680 | `91194de87b98e0cd0e1197172c248fcdd687e0815ee91b2da41a738789007a80` |

## Structured transfer and the weaker moment

FOURTH_MOMENT_ATTACK.md was read in full, including its final general-factor and general-incidence additions. The audit also checked the pinned October 5 source's exclusion lemma and full two-Poisson arithmetic proof, with particular attention to the signed preimage regrouping. The source's full completed theta proof was not independently rebuilt.

The following load-bearing steps were checked:

- The residual identity Ctgw = rf' makes the inserted coefficient identical across the signed preimages, so regrouping remains valid before absolute values. The condition f' dividing k' is retained.
- For squarefree products, allocation among r, f', and the remaining factor columns is exact. The multiplicity at a fixed f' is a divisor function, not the number of auxiliary labels in its entire dyadic interval.
- The coupled kernel may have either sign. The final proof performs Mellin separation before Cauchy–Schwarz, with an integrable coefficient majorant uniform in the moving factor norms. Thus it does not silently assume positivity or invoke an arbitrary-column-coefficient theorem.
- The bounded one-axis rescaling makes the total child column length and source normalizer exact. Exclusion removal divides the product column length and multiplies the auxiliary scale by the same ideal norm. The source row-range ratio is preserved.
- The extension to every fixed number of factor axes has the required 2j-coordinate decay order and only fixed-order divisor losses.
- The fourth-moment initial conductor ratio is genuinely outside the imported canonical domain. A valid transfer adapter does not supply the missing completed theta estimate or change that initialization.
- The uniform moving-exclusion second-moment adapter keeps the larger row range at every smaller column scale, and its Euler-factor inverse has subpower norm uniformly in the excluded ideal.
- Section 8 proves rather than assumes the conductor uniformity needed for pointwise interpolation. The lattice boundary count gives polynomial L-function growth; Borel–Caratheodory bounds its analytic logarithm; Gaussian-localized three-lines gives conductor-subpower reciprocal bounds inside the assumed common zero-free half-plane. The principal pole-removal factor and the imprimitive Euler factors have the correct direction.
- The resulting moment exponent H D^(1+2(k-1)beta+epsilon) and its extraction saturation beta+(11/6-2beta)/(2k) are correct. They are conditional on the stated zero-free hypothesis and imported second moment. They give no improvement of a beta below 11/12.

Two review issues were resolved before the bound version: the order of smooth separation versus Cauchy, and an explicit uniform majorant for the factor-dependent profiles. The exact child normalizer was also checked against the source; independently chosen factor dyads are reconciled by the displayed bounded rescaling.

## All-row sieve and large-gcd fourth-moment piece

ALL_ROW_SIEVE_AND_GCD_TAIL.md was read in full. The primary squarefree sieve statement was checked against Blomer–Goldmakher–Louvel, Theorem 1.3 (arXiv:1112.1650), and the corresponding pinned September 30 source convention. The proof of that established theorem is an input here.

The unique decomposition of a row into valuation-one primes and a powerful ideal is valid. The latter has counting function O(R^(1/2)), and its weighted ideal sums converge above exponent 1/2. Fixing that powerful part puts its exact zero mask into a row-independent coefficient vector; positivity permits enlargement only of the remaining squarefree row set. This justifies the all-row sieve factor H + H^(1/2)L + (HL)^(2/3).

The balanced coefficient energy is O(X^(2+epsilon)) uniformly in the moving exclusion. The exact inverse-square gcd expansion and Minkowski yield the displayed tail powers C^(-2) and C^(-4/3). Both become acceptable when C is at least D H^(-1/4). This controls an actual part of A(D)^2, not an artificially enlarged coefficient model. The equivalence of the full fourth-moment target with the remaining small-gcd target follows from both norm triangle inequalities once the large-gcd part is bounded.

## General incidence ranges and exact extraction

GENERAL_MOMENT_ATTACK.md was read in full. Its arithmetic decomposition was cross-checked independently against the general-k decomposition in the structured-transfer note.

Every shared prime is assigned to its exact incidence subset. Its exterior character multiplier, including powers divisible by six, remains bounded by one with its zero mask intact. The normalized overlap sum has harmonic weights precisely at two-factor incidences and convergent weights at all larger incidences.

The updated note explicitly depends on the reviewed refined sieve, while retaining its initial weaker proof for provenance. Its Rankin tail now has H^(1/6)P0 in the middle energy term and H^(1/12) in the corresponding norm calculation. The diagonal threshold P0 at most H^(1/2) is unchanged. Its full-common-gcd cutoff is the maximum of 1, (D^k/H^(5/6))^(1/(2k-2)), and (D^(2k)/H)^(1/(5k-6)); neither nonconstant term is discarded for all k. The displayed specializations at k=2,3,4 were independently recomputed, including the eighth-moment exponent (19-5theta)/36. These results apply to specified pieces of the actual k-th polynomial and leave their complement open. The hierarchy link correctly records an equivalence without asserting the unproved moment hierarchy.

The ordinary-character alternative uses primitive nontrivial local powers, Gauss expansion with square-root normalization, and correctly separated residue fractions. The exception for powers divisible by six is explicitly treated by counting.

The rough composite-base extraction is valid. Fixed-prime exclusion gives positive density; the averaged inverse-mask coefficient converges by domination to the displayed convergent Euler product for every positive amplitude exponent. Enlarging the fixed roughness set makes the recursion contractive. This avoids a prime-counting logarithm without introducing moving fixed data or applying the moment at an unstated rectangular range. The weighted-Hölder cardinality argument is a restriction on that extraction method, not a lower bound for the actual Möbius sum.

## Refined all-row sieve and larger higher-moment ranges

REFINED_ALL_ROW_SIEVE.md was independently read in full after the earlier three components. The additional quadratic input was checked directly in Goldmakher–Louvel, arXiv:1112.1642, Theorem 1.1 and Corollary 1.2. Its Section 2 also records the fixed bad-modulus correction and good-prime conductor of the power-free core. These classical theorems are inputs; no new automorphic assertion is inferred from a formal residue-symbol resemblance.

The exact sixth-free valuation decomposition allows the sixth-power base v to overlap the five squarefree layers. The v mask is frozen into the column vector before either sieve is applied. Applying the order-six, order-three or quadratic sieve to the largest layer is legitimate after fixed ray-class splitting; all five nonzero local powers remain nontrivial.

The alternative primitive-character estimate is proved directly, not cited without scope. A primitive Gauss sum has modulus sqrt(Nq); orthogonality over the residue-unit characters contributes phi(q), and phi(q)/Nq is at most one. Reduced fractions with conductor norm at most Q have separation bounded below by a fixed multiple of Q^(-1), so the source planar additive sieve gives L+Q^2. Chosen primary ideal generators form an actual subset of that lattice disk.

The character of a sixth-free core has exact good-prime conductor equal to its squarefree radical: the five local powers are distinct and nontrivial. CRT recovers the local exponent from the character, so only bounded fixed-bad and unit multiplicity remains. Primes appearing solely in v are retained through the coefficient mask, and no primitive-inducing convention deletes their zeros.

The displayed monomial inequalities and the interpolation of the two block bounds are exact. They prove the stronger all-row factor H+(HL)^(2/3)+H^(1/6)L. This sharpens the pure L term but leaves the squarefree-row cross term unchanged. It consequently does not move the fourth-moment diagonal cutoff beyond C at least D H^(-1/4).

For higher common-gcd pieces, the improved middle energy term is H^(1/6) D^(2k) C^(2-2k); the third term remains H^(2/3) D^(5k/3) C^(2-5k/3). The two threshold powers in Theorem 5.1 follow by direct comparison with H D^k. For k=3 and H=D^(1+theta), the third term gives the dominant cutoff D^((5-theta)/9); the difference from the competing exponent is (1+7theta)/72, positive in the stated range. This is a strictly larger proved part of the sixth-moment polynomial, while its small-overlap complement remains open.

## Sextic Gram correlation: collaborative adapter and independent cross-check

SEXTIC_GRAM_BOUND.md was read in full and checked against family 023's pinned cubic Gram proof, dual.tex lines 149–240, and its unrestricted-inner coefficient extension, background.tex lines 234–276. The new note proves its sextic adaptation explicitly. It does not assume that the cubic source's exceptional-moment conclusion transfers to this family.

This reviewer contributed the bounded-coefficient strengthening: freeze all but the valuation-one factor in the complete sextic valuation decomposition, then use the squarefree sextic sieve and Minkowski. The number of frozen labels squared times the free coefficient count is at most the total norm length, because every frozen prime-power exponent is at least two. A different agent independently checked Lemma 2.1 and its use in the final bound, including the final frozen version. Thus the strengthened component has an additional review beyond the agent who suggested it.

The following points were checked in the final proof:

- The bound for unrestricted inner coefficients assumes bounded or specified subpower coefficients. It is not misstated as an arbitrary-vector theorem with the length replaced by coefficient energy. Smooth separation in the Gram application supplies exactly this boundedness.
- Factoring the common gcd of the two squarefree moduli produces a literal physical coprimality mask. Finite inclusion–exclusion removes it before primitive Poisson summation. The only principal child is exactly the omitted diagonal p'=p.
- The primary congruence coset is retained in the Fourier calculation. The sextic value psi(3lambda) need not equal one; it is retained as a row scalar of modulus one. Every nonunit character zero is preserved.
- The common comparison frequency scale J0=B^2/Y is explicitly independent of the varying modulus b. Its actual conductor-dependent scale is comparable to J0, and all remaining norm dependence enters a uniformly controlled smooth kernel.
- Mellin separation precedes the square-sum estimate. Its common integrable majorant retains rapid decay in J/J0, and the proof separately justifies the dyadic summation when J0 is below one. Bounded nonempty physical scales below one are counted directly.
- The substituted terms are PZ/(KM), P^2/K^2 and P^2 Z^(1/3)/(K^2 M^(1/3)). Divisor summation costs only a subpower. This proves G(P,Z)=PZ+P^2 Z^(1/3), including arbitrary subsets of the off-diagonal modulus range.
- The Bombieri–Halasz–Montgomery consequence has coefficient energy A2 multiplying Z+sqrt(R G). Its large-value corollary follows from Young's inequality with the stated powers. No extra factor of Z is inserted or deleted.

The remaining limitation is material: this is a smooth unweighted character correlation with a controlled optional fixed inner mask. It does not establish the target moment with its long balanced Mobius/divisor coefficient, nor authorize masks growing arbitrarily without a separate uniform adapter. At the full fourth-moment product scale P=D^2, Z approximately D, its second term does not improve the trivial squared row correlation P Z^2. A further arithmetic connection or cancellation estimate is needed.

## Direct Gram composition and its limitation

GRAM_MOMENT_COMPOSITION.md was independently read in full. Its adapter from smooth primary rows to every nonzero element row is valid: first freeze the unit and the exact power of the prime above 3 into the coefficients, keeping their nonunit zeros; then sum the primary norm ball by smooth dyadic annuli. All three scale exponents are positive, so the annular and prime-power sums are geometric. The Schur row-sum estimate consequently gives the operator factor H + P H^(1/2) + P^(3/2) H^(1/6) with arbitrary squarefree-column coefficients.

The comparison with the refined sieve is correct in both ranges. For P at least H^(1/2), the Gram expression dominates H + (HP)^(2/3) + P H^(1/6) term by term. For P at most H^(1/2), both expressions are O(H). This compares available upper bounds; it does not forbid a different use of signed correlations or assert a lower bound for the actual inverse polynomial.

The actual inverse-polynomial energy and the balanced-core coefficient energy are correctly substituted. The three common-gcd norm sums have exponents 1, 2 and 5/2, yielding the squared tail H D^2 + H^(1/2) D^4 C^(-2) + H^(1/6) D^5 C^(-3), up to the stated subpower. The sufficient cutoff is max(1, D H^(-1/4), D H^(-5/18)) = max(1, D H^(-1/4)). Thus this composition recovers, and does not enlarge, the already proved fourth-moment gcd range. The final product-length comparison reproduces the exact threshold theta greater than 1/5 for a strict gain of the second Gram term over the trivial correlation bound at P=D^2, Z=D^(1+theta).

The repaired inline-math delimiters were inspected in the final frozen version. The final README changes are a link to this separately proved limitation and removal of one extra blank line at EOF; its mathematical description agrees with the note. The EOF normalization changes no text or mathematical content.

## Authored obstruction note and overview scope

MOMENT_OBSTRUCTIONS.md was authored by this reviewer. Its hash is included for publication identity, not as a claim of independent self-review. The parent and a different agent independently reviewed its identities, core transfer, rectangular converse, exceptional-row obstruction, elementary long-row theorem, and extraction quantifiers. Their scope fixes were incorporated before the bound version.

The additional hierarchy-equivalence theorem was independently checked by the other agent. For fixed nu, unbounded moment orders at one fixed polynomial row scale imply the critical-line statement for each fixed row character already by positivity; Mellin continuation with a test whose transform does not vanish at the candidate zero gives the zero exclusion. The converse uses the separately proved uniform conductor adapter over the entire row-twist family. The fixed-nu, nu=1 and all-nu scopes are explicitly distinguished. Neither direction asserts the unproved hypothesis.

The packet README was reviewed for mathematical scope, matching formulas, the meanings of the overlap cutoffs versus zero-free boundaries, and the distinction between arithmetic row norm and imaginary height. Its computation paragraph summarizes the separately validated diagnostic; the listed panel counts were cross-checked against the diagnostic JSON, but this review does not independently certify the numerical run. The final added Gram section has the correct bound PZ+P^2 Z^(1/3) and correctly identifies Z>P^(3/5) as the threshold for its second term to beat the trivial squared row-correlation bound. The overview preserves the unresolved full moment and the original upstream verification boundary.

## Scoped diagnostic reproduction and artifact identity

The following bindings identify the final producer, identity checker and saved diagnostic outputs. They do not convert the ordinary binary64 moments into certified values.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| checks/sextic_moment_probe.py | 11346 | `5c97cd58bea1067215f98f112bbb19c31ad9d0179575159ecdc3a390f8c0884f` |
| checks/check_sextic_probe.py | 3886 | `62987a152eb65e0e38d2996081289500410cc749325f1025644792208ae43c50` |
| results/sextic_moment_probe.json | 22645 | `7f4a2a0003d75883a439778080ba0df43c356ca3e56125d01cd211791f01d59e` |
| results/sextic_probe_additional_checks.json | 802 | `5805ecd1e6516d3972212af3973573905ef340a5d2692ca423958665100c7962` |

The exact rational cutoff helper was source-reviewed and checked independently on 3,593 exact predicates: bases 1 through 512 at the seven exponents 1/10, 1/2, 1, 11/10, 3/2, 2 and 17/3; the perfect-power case 1024^(11/10); and the eight saved panel cutoffs. Each returned integer h satisfied (h-1)^q < b^p <= h^q for the reduced positive exponent p/q. The saved D=1024 panel now has H=2048 and 7,446 rows. Its floating normalization was corrected without changing the raw row set; no Eisenstein element has norm 2049.

The additional checker initially used Python assertions for acceptance. The final source uses explicit conditional exceptions, including both int64 bounds. This reviewer reran the final checker in ordinary and optimized Python, reproducing its 51,688 exact symbol predicates across 1,022 prime ideals. Both JSON outputs matched the saved additional-check artifact byte for byte. Both modes also rejected a temporary producer wrapper with a deliberately altered value at -1 and wrote no passing artifact.

These are a reproduced identity check on the producer's arithmetic and a separate exact cutoff check. The symbol checker calls the producer's own finite-field implementation; it is not a second independent implementation of the entire residue symbol. This reviewer did not recompute the eight floating moment panels, independently authenticate every primitive numerical operation, or obtain rigorous error bounds for their sums. The main result file is bound for artifact identity and the stated cutoff/metadata checks only. None of these finite diagnostics supports an asymptotic moment bound or a zero-free theorem.

## Retained boundaries of this review

This review does not independently establish the imported quasi-Riemann theorem, the source's completed cubic-theta reflection theorem, or the established higher-order large sieve. The first remains an upstream result relied on only where expressly indicated. The classical all-row sieve consequences and elementary extraction identities do not depend on the imported quasi-Riemann conclusion.

No Lean kernel build, proof-assistant certificate, or zero computation was performed as part of this review. The exact diagnostic checks reproduced here have the limited scope stated above; the floating moment panels were not independently reproduced. No finite sample is used here as evidence for an asymptotic bound.

The seven substantive mathematical notes and the overview are bound by the exact file hashes above for publication identity, with review roles distinguished in the corresponding sections. The authored obstruction note and collaboratively strengthened Gram adapter are not represented as wholly independent work by this reviewer. Their separate cross-checks should remain in the packet provenance.
