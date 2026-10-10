# Independent review of the correlation, theta and low-kappa adapters

Review date: 2026-10-10. Status: the displayed arithmetic and elementary analytic implications below pass independent inspection at their stated scope. This review does not rebuild an external quasi-RH proof or establish an estimate for the actual arithmetic source.

## Correlation transfer C1–C11

Reviewed `../correlations/CORRELATION_TRANSFER.md` and checked its C6 interface against `../arithmetic/NEGATIVE_MASS.md`.

* C1 counts every zero-extended window with the correct `H-d` multiplicity. The index range `1<=j<=N+H-1` includes both endpoint fragments. Its Cauchy consequence C2 retains the signed energy; C3 and C4 correctly pay half the smaller shift-range and absolute-correlation saving.
* C5 includes all square divisors, including nonsquarefree integers. The positive internal epsilon makes the square-divisor sum convergent at `theta=1/2`; no exact endpoint bound is asserted.
* C6 retains `M_beta(x)=M(x)-M(x/67)`. The needed cancellation of the `sqrt(x)` main term follows from the zero value of `sum beta(n)/n`, justified by the convergent series and its Abel limit. The cited nonnegative-transform argument has the required real-axis holomorphy and noncancellation of off-line poles.
* C7 holds uniformly over every character and real frequency because `Re(alpha conjugate(chi(p)p^(it)))<=alpha`. The prime lower bound for the positive summatory function excludes every power exponent below one.
* C8 is an exact log-weight identity before its Chebyshev upper bound: complete multiplicativity supplies `g(md)=g(m)g(d)`, and `log n=sum_(d|n) Lambda(d)`. C9 is a positive Euler-product majorant, requiring no asymptotic for the summatory function.
* C10 removes the log weight by splitting at `sqrt(X)`. C11 applies Cauchy to a shifted interval contained in `[1,2X]`; its constant is independent of every integer `0<=h<=X`. Thus the proof needs only the explicitly named Chebyshev and prime-harmonic estimates, not Selberg–Delange.

The firewall is correctly scoped to bounded completely multiplicative functions. Its logarithmic correlation saving comes from decaying mean-square mass, and the source is positive; it does not supply signed cancellation or have the unit modulus of Liouville. These distinctions do not invalidate its intended counterexample to an implication from the listed general bounded-source properties.

The complete classical reconstruction in `../arithmetic/ZERO_FREE_MERTENS.md` was also reviewed. Its elementary polynomial zeta bound is sufficient for Borel–Carathéodory on the fixed zero-free disk. The positive harmonic rectangle barrier has the correct edge bounds and exponentially small center-height correction, giving a strictly sublinear power of `log(t)` for `log zeta` and hence subpower reciprocal growth. The half-integer Perron error is `O(x log(x)/T)`; its contour stays away from zero, and the reciprocal's removable zero at one creates no residue. With `T=x^2`, `sigma_0=theta+epsilon/2` and `eta=epsilon/4`, the stated Mertens exponent follows. The resulting exact fixed-SHARP negative-mass growth exponent `Theta-1/2` handles `Theta=1`, `theta=1/2`, and an unattained supremum at their explicitly stated scope. No correction was found.

## Complete positive theta source and modular binding

Reviewed `../xi/POSITIVE_THETA_QUARTET.md`, `../xi/MODULAR_BINDING_AND_TRANSPORT.md`, the Fourier normalization in `reviews/D-pass3/PROOFS_AND_REPAIRS.md#R16`, and the saddle interface in `reviews/A/supplement/REPORT.md#S06`.

P1–P7 pass: the polynomial adds exactly the indicated quartet with multiplicity; integration by parts has `D^2 -> -z^2` and `D^4 -> z^4`; the derivative recurrence and complete atom positivity imply full-source positivity on both half-lines. The R=10 lower margin is 2000, and the unbounded-height polynomial has positive coefficients.

The Fraction checker was replayed from a byte-identical copy in `/tmp`, avoiding mutation of the owner's receipt. It passed all 49 Bernstein coefficients, 36 synthetic quartet locations and both unbounded tails. The compact Bernstein cover and the positive tail are complete domain certificates; the quartet evaluations are finite consistency checks of the independently displayed factorization.

P8 has the stated scope. For each fixed R,d the leading atom has degree six, changing the bounded linear coefficient from `9/2` to `25/2`; the double-exponential curvature and the S06 local/exterior estimates survive. Constants and the first applicable derivative order may depend on R,d. This does not assert uniformity in R, a low-order companion bound, or a descent theorem.

M1–M11 pass: the two normalizations `Q(0)` and `Q(i/2)` are distinguished; even L commutes with Jacobi reflection; `L(1/2)=L(-1/2)` preserves the endpoint and small-v terms. Repeated Mellin integration by parts gives the correct factor `L(s-1/2)/C`. Its real-axis growth excludes an ordinary absolutely convergent Dirichlet series normalization. The compact-error factorization and derivative bounds are correct. The companion ratio estimate retains and protects both original denominators, so it does not silently deduce descent from a small polynomial correction.

## Compiled low-kappa arithmetic

Reviewed `../xi/formal/LowKappaCapacity.lean`, its README and the complete compilation receipt. The variables match `KAPPA_EXTENSION_CONDITIONAL.md`, Section 2.2: `A=n_1+n_2+z`, capacity `A+(6*kappa-1)z`, and M includes the declared moving twist-radical width.

The comparison, strict-width, support-error, terminal and clipped deleted-column theorems match the written adapter. The real positive examples inhabit the new interval `13/18<=kappa<3/4`; the equality and below-threshold examples have the advertised values. The reported axiom sets of all fifteen compiled statements contain only `propext`, `Classical.choice` and `Quot.sound`.

This is a compiled real-arithmetic adapter with explicit analytic hypotheses. It proves neither the extended analytic moment theorem nor the source identities that would instantiate those hypotheses.

## Separate independent induction audit

A second mathematical reviewer read all of the frozen September-30 Section 18 source, lines 12477–14973, together with its logarithmic-control, smooth-calculus and kernel interfaces. Sections 1–3 of `KAPPA_EXTENSION_CONDITIONAL.md` passed that review, conditional on the cited analytic inputs. The exact source findings were:

| Source lines | Audited use |
| --- | --- |
| 12929–12936 | The terminal exponent uses `kappa*z<=M/6`; the auxiliary `z<=2M/9` can be replaced by `z<=3M/13`. |
| 12947–12980 | The intermediate `z<M/21` is weakened to `z<M/20`, which already supplies the source's operative comparison totals `23M/30` and `14M/15`. |
| 12833–12900 and 1531–1607 | The prime estimate retains `beta_*<=(1+kappa)/2`; the compact enlarged range has `s_kappa>=31/36`, and its derivative-independent prime exponent is unchanged. |
| 14218–14301 | Greedy removal has capacity decrement `6*kappa*d` and squared-prime cost `kappa*d`, hence exact ratio `1/6`; deletion monotonicity needs `6*kappa-1>=0`, and overshoot uses `kappa<=1`. |
| 14810–14971 | Finite induction and weighted all-height propagation need `0<=6*kappa-1<=5` and the preserved margins. Full-product Fourier measures, aggregate support thresholds, backward finite internal orders and the later external tail order are retained. |

The actual-capacity crossing and balanced count in Section 3 were also checked, including the inverse `7/37` supply and the plain `c/3` capacity. The former `Delta/4` penalty came from the baseline-capacity replacement and disappears when the actual capacity is retained. The clipped auxiliary hypotheses already imply `M>=0` from `0<=short<=M/4`; no missing hypothesis was found.

This audit validates the written parameter adapter against its frozen source. The shared analytic inputs remain dependencies, and this result alone does not establish the continuation conclusion or independently rebuild the upstream L-function theorem.

## Convex payment and complete source window

`../operators/CONVEX_WINDOW_EXTENSION.md` and its exact checker pass independent review. The moving-integral norm has support of length `L+s`, total integral `s*mu`, and the stated Cauchy lower bound. The `s=L` primitive identity retains both endpoint fragments and works for complex h. The mean coefficient simplifies exactly to `L^-1 integral_0^L w` after two integrations by parts, with the weighted-curvature hypotheses controlling zero. Thus a negative endpoint is genuinely paid from the full positive curvature mixture.

The literal source bounds have the correct directed signs. The full prime constant uses both sides of the convex trapezoid tail, and the gamma integral drops only positive terms in its lower bound. The helper enclosures imply `C_b>-(.578+.6932+1.1448-1)/3=-.472`; the new lower gamma/log enclosures imply `C_b<(1-.57-.693-1.144)/3=-.469`. The curvature lower bound covers the complete interval, and its weighted endpoint integrability survives at `L=3/20`.

Normal and optimized `-B` checker outputs were independently replayed into `/tmp` and are byte-identical. Their source hash is `72ff5c1c4653558f40b737348860a9937ae21be49201329b44c5178673072c2e`. The resulting `3/500` and `1/300` lower coefficients are correct. This certifies all complex L2 tests on the stated window in a primitive norm; it supplies neither a uniform L2 spectral gap nor interval joining.

## Recompleted negative height features and extended anchors

A separate independent reviewer verified N10–N13 of `../heights/NEGATIVE_FEATURES.md`. Symbolic comparison to the native quartet gave zero. Normalized Leibniz produces W2 and W3 as stated; `zeta_o>0` ensures the odd positive-square coefficient, and the negative coefficients give exactly `16A^2(S^4 W2 S8/zeta_c+S^6 W3 S10/zeta_o)`. The j=10 tail and `log H<63/2` give `2845/(81H^9)`. Compact convergence retains all positive quartet squares via `sum m/b^2`.

At the reviewed freezes, `../certificates/certify_hardy_z.py` certifies 16 intervals with 33 endpoint balls, and `../heights/certify_extended_anchors.py` certifies 48 intervals with 96 endpoint balls. Both were replayed at 128 bits with python-flint 0.9.0 into `/tmp`; the extended producer's normal and optimized receipts were byte-identical. The floating-point finder only places proposals. Exact rational endpoints, strict real signs, zero-containing imaginary enclosures, disjointness and the existing continuous Hardy-Z functional-equation argument justify the IVT existence conclusions. They do not prove uniqueness, simplicity or a zero census.

The reviewed hashes are: negative features `4415102019f19efe63f581d4aa5dd8b734faa6af47e146f37c10b96b790ce4f4`; 16-anchor producer `44c83f855447c7acf348da070b9617ca12d5ce270ef949d5a99eb7bf17dc6a6a`; 48-anchor producer `875baffd29b1dde90683503536814e3eb9f7cb9d75745407fc7c4641e2f3a574`. `HARDY_Z_REVIEW.md` separately records the earlier nine-anchor freeze.

## Weighted squarefree stitch

Two independent mathematical reviews pass `../arithmetic/SQUAREFREE_STITCH.md` and `verify_squarefree_stitch.py` for their stated scope: every real x>=1 and every real m>=1.737. The noninteger continuation remainder in S5 has the correct sign and `z^-b` bound. Completing the two absolutely convergent h-sums gives S4's exact error constant while retaining the negative `zeta(b)/zeta(2b)` term. Rescaling the 67 label gives the three displayed factors without losing its separate multiplicity.

The normalized Bernoulli prefix and tail errors produce exactly E0, L and C in S9. Holding the slab coefficients fixed, the derivative lower bound has the stated factor `x^(b0-2)[B0(m0-1)sqrt(x)/2-L0(1-b0)]`, plus a positive omitted error derivative. Thus S12 covers every real tail endpoint, rather than just the stitched horizon. The labelled-prime finite-horizon argument covers the whole bounded endpoint interval; the seven closed slabs and the inherited higher-power theorem cover the entire claimed power range.

The second reviewer replayed the 192-bit Arb checker in normal and optimized `-B` Python into `/tmp`: all seven slabs pass and the receipts are byte-identical. Each constructed whole-power ball was also confirmed to enclose both exact endpoint balls. Directed coefficient endpoints, complete prime enumeration and explicit guards were checked. Finite density and prefix controls corroborate the normalizations but are not substitutes for S1–S12.

Reviewed SHA-256: manuscript `62253844e57e2ad2c4490cb5dd08dc318a90ef058fdf81062dac9112ab32b221`; checker `746be9f6382323a0131e3a7ece95e4448461c2b44c7e0dd33310d02675513550`; horizon dependency `8486059b8468ceb6cb59d34c4c16c61eeb72a8097583596e5253b934571e5104`. No mathematical correction was identified. This remains a sufficient supercritical-power theorem, with no critical-power-one or RH claim.

## All-order outer rays and protected source transport

A separate reviewer checked O1–O21 of `../xi/outer-ray/THEOREM.md` and T1–T22 of its `SOURCE_TRANSPORT.md`. The all-order sector argument, Schwarz–Pick comparison and protected multiplier bounds pass. The checker was independently replayed into `/tmp`, avoiding writes to its owner's receipt. Its 1152 sector, 1152 Schwarz–Pick and 1152 protected-multiplier cases, four polynomial controls and five sharp Fourier controls passed in normal and optimized Python with byte-identical outputs. These finite controls supplement the displayed all-order proof.

One wording correction was reported to the owner: a quartet at imaginary distance d lies inside the original zero strip of width A only if d<A. The weaker hypothesis 0<d<1/2 suffices when explicitly referring to the classical Xi strip A=1/2. The compact-error transport itself does not require preservation of a sharper zero strip. This issue does not change the protected denominator or outer-ray theorems.

Reviewed SHA-256: theorem `2b35a58b119a6f924658a702769c401126e708e592738551e992403004cdfe6d`; transport `43b7f9a5da0ac3a59b6cc70a04606bc1bc100a09b60ff0974cfce61ce616691c`; checker `943ad4d58b328a043f9c4d902d7c035c997c706735bb72db53b4711577b56662`. The owner may subsequently correct the noted wording; these hashes identify the reviewed freeze.

## Two-label all-real power threshold

A separate reviewer checked all of `../arithmetic/TWO_LABEL.md`, `verify_two_label.py` and `test_two_label.py`. The theorem passes for every real x>=1 and every real m>=3/2. The level-pairing argument for R<3, activation endpoints and the separate duplicate-67 contributions are correct. The complete prime-zeta tail uses

    P(ka)/k <= 2^(-ka)[1+2/(ka-1)]/k,

followed by a geometric tail, retaining the correct directed signs. An independent trial-factorization census matched all 23550 entries of the pair multiset, including two entries at 134 and one at 4489.

The reviewer replayed the 192-bit Arb certificate into `/tmp`. All 60 bounded rectangles and four complete tails passed; normal and optimized receipts were byte-identical. All four negative/control test groups remain active under Python optimization and passed. The smallest first-tail margin was greater than 0.00754409984518. The new certificate covers [1.5,1.81], and the previously reviewed higher-power theorem covers the remainder.

Reviewed SHA-256: manuscript `3d8f05192841107bcf9b7904e212ebcb7db3afc8440cc813cc9b513479f5bd5d`; checker `9d58b1b9b2ef69e335ef64ff08a976a2a30051cc5e5cf23812369adf8aaf1212`; controls `ed921cbb565dae7d1fb414b353651c11f90478096a8004ae7dfc7254807b984e`. This improves the sufficient power threshold; it does not establish the power-one theorem or RH.

## Literal continuum convolution and residual error bounds

The analytic argument in `../operators/CONTINUUM_RESIDUAL_DERIVATION.md` and its three accompanying helpers passes a scoped independent review. The complete prime constant and real source, gamma partial fractions and removable values, elementary/dilogarithmic/hypergeometric incomplete transforms, semantic zero-frequency handling and exact double-integral formula are correct. Exact symbolic differentiation with r=exp(-x/2) independently proved the full gamma primitive and its endpoint constant `(7-pi-4log2)/9`. Eighteen real-length incomplete transforms, including both repeated poles and frequency 111*pi, matched 2048 literal gamma terms within the independently proved tail `1/(4*2048^2)`.

The orthogonalization and exact trial coefficients enclose the original trial space rather than rounded replacement tests. The Schur U formula, common analytic extension of F, prime correction integrated from log2, and piecewise cusp branches match their definitions. On the Cauchy disks the complete source bound, partial-path allowance, primitive bounds and uniform trial coefficient sum justify M. The Taylor argument gives `8hB*2^(-2n)` for the positive Gauss rule. The logarithmic modulus controls all omitted neighborhoods, and the anchor guards imply the displayed `24epsilon` and `36epsilon` entrywise radii.

An independent Fraction census confirms 232 contiguous normalized panels per slab, each of width at most 1/100, covering exactly `[2^-60,1-2^-60]`. Thus all 696 physical panels and the six declared omitted neighborhoods cover the full window. The projection Gram entries, directed matrix solve, symmetrization and coefficient 15/8 agree with the inherited coupling and codimension-14 coercivity.

This review validates the written analytic enclosure and its implementation. The complete 696-panel matrix run was in progress at review time and was not duplicated. Positivity remains conditional on a completed directed lower receipt. A positive finite U alone does not establish that conclusion, and neither conclusion proves all-window positivity or the terminal xi/Weil adapter.

Reviewed SHA-256: derivation `e2979233b85be95c8615313d72108e5d766c4b7280cebadb870baaa0940ef53f`; upper producer `b3832a0cddc8bc1e2603c40240b608d1f06a868bda9436d8e88a146393fe007b`; convolution `d53aa6c4e9c0e33d26c2327305bc1aa0ae9adef035ea4437ccd2a19b23bbf014`; residual producer `e03d92bb09c1250b4a93e485aba6cc85bf2a4309b00e6d9217dbfbd39887cc92`.

## Common inverse/plain conditional pricing

A separate reviewer checked all of `JOINT_WITNESS_PRICING.md`, its exact checker and receipt. The source-qualified conditional deduction passes. S's lines 4520–4546 supply the common-character/common-height product spike and padded t=1 rectangle; lines 15282–15314 supply the no-slot edges. The declared logarithmic derivative products suffice for two-variable Sobolev maximalization, matching S's lines 1141–1151 and 1231–1244. Summing over rows before integrating preserves the U exponent with one finite extra height power. Positivity permits bin restriction, and two different dyad selections can still give the minimum of the two cardinality bounds.

The original kappa=3/4 is retained, and no new prime supply or coefficient family enters J1. The original compensated branch retains its required inverse supply above 7/37. The reviewer independently recovered the displayed high exponent from S's stage expression at lines 15827–15833, and checked all twenty retained geometry and transport gates.

Normal and optimized checker outputs are byte-identical to the frozen receipt. An independent oracle reconstructed every tensor Bernstein coefficient using a 3-by-4 interpolation grid and inverse Bernstein evaluation matrices, rather than the checker's power conversion. All 6144 coefficients matched. Its minimum, base reserve and joint reserve are exactly `415930007/63281250000000`, `415930007/316406250000000` and `353513/585937500`.

Section 6's nondegenerate prime-ideal example and its disjoint-slot extension also pass at their stated coefficient-energy scope. They exclude a power saving from the truncated annular mu*1 identity alone, without imposing a lower bound on a character moment or a zero bin. The new arithmetic mixed moment J1 remains unproved. Thus the review validates the conditional boundary B=0.874956 and its exact price, rather than an independently established zero-free theorem.

Reviewed SHA-256: manuscript `58afe2b764e4cc27215f0e71d4e79817f52ab81924891d0ffd8ac3cb019923ee`; checker `be3821e6bd265d45b934dab43f4172c25874ba84bfb1c7dac16d7ab5d7f914f7`; receipt `df33021edf2606752b63a37167ddb8238adf11c99b91a181a4e5bb90be54984c`.

## Global Pick packets through order twelve

The complete argument in `../heights/ANNULAR_GLOBAL_PICK.md` passes independent analytic review, conditional on its explicit classical and published inputs. The even/odd rational moment congruence holds at arbitrary distinct positive nodes, and its determinant is the square Vandermonde factor. Its largest moment index is absolutely summable under the complete zero count. The normalization is a positive scalar/diagonal congruence for both Hankel blocks.

Logarithmic differentiation gives the displayed node-independent second-derivative estimate on every vertical pole segment. Conjugation cancels its first-order term. The six-band Lagrange bound controls the inverse Vandermonde trace for arbitrary points in their projected intervals. Taking a product probability measure over the six bands proves the same reserve for arbitrary multiplicities and within-band distributions. Both the complete pole-weight factor of two and W/W_min<8000 are correct.

The Trudgian error, elementary Stirling remainder and main-count increment imply the strict lower open-band count at every L>=H. The one-sided endpoint convention preserves the strict margin. The exact domination C/H^2<1/3 then holds on every dyadic annulus. Adding all complete annular kernels and the verified lower critical pairs is justified by locally normal convergence. Appending distinct nodes handles smaller packets, and repeated nodes use a coefficient-summing congruence.

Normal and optimized `-B` Fraction replays into `/tmp` are byte-identical, covering the exact frame constants, arbitrary-node congruences for n=1 through 12 and Pfaffian controls. The published zero verification and argument bound were not independently rebuilt. The accepted result is a source-qualified fixed-order global positivity theorem, with no all-order or RH conclusion.

Reviewed SHA-256: manuscript `c04cdf51ad64972137ecd3f4aa2c835e82481d4984115bd7fadf9b8621311724`; checker `150341214b3a6a5fde8ad3b7e53da2d4631970b4c6291c1beab5fe6f422cedb0`.

## Phase-aware eight-dimensional positive sector

`../operators/CODIMENSION_8_PHASE_REFINEMENT.md` and `check_codimension8_phase.py` pass independent source and arithmetic review. The outward phase union covers the entire sqrt(x)*log2 interval in each cell. The truncated gamma floors are monotone lower bounds; the sign-aware P endpoint product covers both signs of the directed V lower endpoint. The rational tail completes the unbounded frequency range. The supporting line implies the stated primitive gap after five sine constraints, and the retained whole-source tail remains a nonnegative sinh moment. The exact residual coefficient is 27/2.

Both normal and optimized `-B` replays passed all 4096 closed cells and the unbounded tail, with byte-identical local receipts under python-flint 0.9.0. The stored owner receipt uses 0.8.0; this version field distinguishes their runtime provenance. This is positive-sector coercivity, rather than the eight-dimensional effective sign, interval joining or all-window positivity. Checker SHA-256 `11f1662311aaa5cbd0f274790069c1cb88b49ff591c4d500c6a63cdbdac6e60f`.

## Uniform positive sectors through log3 and finite upper matrix replay

`../operators/WINDOW_FAMILY_TO_LOG3.md` and its checker pass independent review. The outside-prime cosh identity remains valid through equality at log3, and that endpoint introduces no additional integral mass. The first seven sine moments give the stated L-dependent Poincare bound. Its rational lower gap `259120533/517719200>1/2`, complement dimension ten and residual coefficient 9/2 are correct uniformly for every 0<L<=log3. Normal and optimized phase/scaling replays are byte-identical under python-flint 0.9.0. This establishes positive-sector coercivity only; it does not join effective matrices. Reviewed manuscript SHA-256 `4141b356c805a99d2f9b535da5e808175ca3508d34f0534ff2ab5764cd322b2a`; checker `7bbef766664319616bf3b55ca653e07e925a1e699cdcaa930a127485b3bfd592`.

The current `enclose_analytic_upper.py` was also independently replayed in normal and optimized Python at 256 bits, with 100 trial modes and eleven removed sine modes. All matrix, trial-coefficient, LDL and mathematical receipt fields match after excluding elapsed time. Both certify U>=1e-10 I in dimension fourteen. This supplements the preceding analytic review while preserving its U-only scope: the complete residual lower matrix remained in progress.

## Four-label global power theorem and explicit activation defect

A separate mathematical reviewer checked all of `../arithmetic/FOUR_LABEL.md` and `KERNEL_DEFECT.md`. The four-label theorem passes for every real x>=1 and m>=7/5. The level-four/five pairing and subsequent even/odd pairs use the correct removal factors. Negative odd levels receive upper bounds, positive even levels receive lower bounds, and the final nonnegative coefficient is preserved. Newton's third elementary identity correctly treats the two 67 labels as distinct. The complete prime-zeta tails are the previously reviewed P10 contract.

An independent integer-factor census through one million reproduced all four product multisets exactly, with counts 78499, 211614, 210777 and 95714. Both 192-bit directed replays are byte-identical to the two frozen receipts (SHA-256 `fc976107d9f7c131deaf5412b33227d4358eaec36356f80c11a61e683a194c9b`). All 126 bounded and seven unbounded rectangles pass; the least whole-tail margin exceeds 0.01265529821835. Three separate control groups pass in normal and optimized Python. The previously reviewed two-label theorem supplies the larger powers.

The defect note's exact absolute source identity is correct: the coefficients at n=67^k*l, 67 not dividing l, are mu(l), -2mu(l), mu(l), 0 for k=0,1,2,>=3. Thus `A(t)=(1+67^-t)zeta(t)/zeta(2t)`. Bernoulli and the activation estimate retain only adverse even-parity defects and exclude the empty subset, giving `(A+B)/2-1`. All Euler products converge because a-delta>1. The pole asymptotics prove the displayed diverging horizon as m decreases to one. This is eventual positivity for each fixed m>1, without a critical or all-endpoint conclusion.

Reviewed SHA-256: four-label manuscript `0adf4d69d1fc66e36942e40345c7b83625d758a38dc5a179221e9ffa6f70b818`; checker `e07cd340f82fe61e39c864d2a91a944beb5211cd884a464e20baf2289ff707b6`; controls `46398d948f57ba70dc8efb7e3a04a66a6ed1c60f9b5e487f6dcd5cb1c0a4467e`; defect manuscript `af1f6c919245b684f5e7b7fc6d389a23a2e45b695170b854c0b612ce70424fc3`.

## Critical pointwise sign obstruction

A separate reviewer checked `../correlations/CRITICAL_SIGN_OBSTRUCTION.md`. Eventual H1>=0 implies RH by the cited Landau/negative-mass adapter. The resulting absolute Mellin convergence and Laplace triangle bound make every boundary pole at most simple; the transform numerator does not vanish at any nontrivial zero. Thus the simplicity implication also follows. The finite nonresonance contract and positive Fejer product imply the displayed necessary inequality `a0>=2K/(K+1) sum|a_j|` using finitely many residue limits, with no infinite zero expansion.

The reviewer identified a conjugate-sign typo, which the coordinator corrected: rho=1/2+i*gamma creates a pole at +i*gamma and is tested by omega=-gamma. The corrected manuscript SHA-256 is `1afb76b7acd8dea9ee42efb00a2e093e6099b99c8c9459ad9afa8b77fa67e6e8`. The owner independently replayed 1000 directed intervals and whole-interval residues in both modes, obtaining byte-identical receipts and strict Fejer deficit greater than 1/50; the receipt SHA-256 is `1b69ff03236d94e6e53f11f5c71fb0381564f2d2926cb89ddb85e01f1e6175fa`. This review inspected the interval/derivative/residue checker contract but did not duplicate that full runtime. The finite nonresonance condition and any actual negative point remain unproved.

## Narrow-annulus Markov theorem through global order 320

N1–N14 in `../heights/NARROW_ANNULAR_PICK.md` pass independent analytic review. The scaled iterated Markov inequality and finite complex Taylor sum give the stated polynomial and derivative bounds. The rational weights have the required node-uniform upper/lower bounds. Conjugate grouping and the four product-rule terms produce the complete per-weight error coefficient 32A^2*n^6/L^2.

The adaptive maximum interval stays in the projected J interval; shrinking its squared-height endpoints by A^2/L^2 places an open source band inside [1,r^2]. Its width is sufficient for the uniform Trudgian count at 1/(4n^3), without a zero-spacing assumption. The narrow full-weight upper count is less than 2L*log(L)/n. Comparing it to the peak-band lower reserve gives exactly 204800A^2*n^8/L^2. This proves global order 320 under the classical strip and the named classical/published inputs. Global order 350 additionally assumes the imported uniform depth A<=3/8.

The coordinator identified the A=0 strict-error corner; the author corrected N10 and N14 to non-strict bounds. Both corrected normal and optimized Fraction replays are byte-identical to the corrected owner receipt. Published count/verified-height inputs and Markov's theorem remain explicit dependencies. The complete-source summation, smaller packets and repeated nodes follow the already reviewed arbitrary-node congruence. No all-order limit or RH conclusion follows at fixed H.

The separate hostile reviewer also passed the inherited arbitrary-node congruence, both one-sided endpoint counts and the adaptive interval construction. Its replay-scope observation was corrected by checking every even auxiliary order from 8 through 350 at the worst depth A=1/2; an independent Fraction oracle verified all 172 orders and 1720 inequalities. The A=0 deviation and bound are both exactly zero under the corrected non-strict bounds.

Reviewed corrected SHA-256: manuscript `c7dd156fec0d3982dd1d513697ef6786d9a1cc5f48a051865a8fcd493d404253`; checker `fad4f520ddf0c87e6c404a627e61d405de83cc75e9bd65cb4641ea984fe3eca4`; receipt `ce5466a74c0ef5ee66c69d0497dc6b525e3035d19242ae858c848cac1343e57c`.

## Galerkin orthogonality in the literal source residual

`../operators/GALERKIN_SOURCE_PROJECTION.md` passes independent operator review. Exact Galerkin orthogonality makes the residual functional vanish on the finite trial space H, so its energy dual norm restricts to H's energy-orthogonal complement. Coercivity makes the primitive derivative continuous under completion. The literal source images Pi F_H are independent by positivity of q on H; therefore their Gram inverse is legitimate and `R_H=R-B*G^-1 B` lies between zero and R.

The cheaper shifted-source Gram also yields a valid lower bound with the original U: an arbitrary exact u_i in H changes no residual functional on H's energy-orthogonal complement. No extra trial-energy matrix or ordinary L2 spectral gap is required. Any effective sign still needs the full directed residual integrals; exploratory fits alone do not certify it.

Reviewed manuscript SHA-256 `29738b5f61c49e027858387ac90f2eb5823f8f3487b59949d90a313d368c6c03`.
