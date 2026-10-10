# Primary-source identification and scope

Status: source identification and mathematical extraction; imported headlines have not been independently rebuilt in this research wave.
Scope: fixed zero-free half-planes and their proof mechanisms. RH remains open.
Source freeze: OpenAI `math` commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`; Baiying Liu's extension commit `7d10420de90efa2f082a06a342fc7accbd57ab37`.
What was actually run: HTTPS source downloads, SHA-256 calculations, PDF-to-text conversion, exact symbolic exponent calculations. No upstream Lean build is claimed here.
Smallest remaining gap: independent validation of the imported analytic proofs and the proposed extension of the fourth-moment parameter range.

The user's two principal references can be identified confidently. The official release catalogue lists the first two manuscripts together in family 003.

| Author | Manuscript date | Exact title and frozen public source | Claimed range |
| --- | --- | --- | --- |
| OpenAI | September 30, 2026 | [The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s)>7/8](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) | All finite-order Hecke L-functions over Q(sqrt(-3)) and all Dirichlet L-functions: no zeros for Re(s)>7/8. |
| OpenAI, with human assistance | October 5, 2026 | [The Quasi-Riemann Hypothesis](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf) | The same families, Re(s)>11/12, via a simpler different argument. This boundary is numerically weaker than 7/8. |
| OpenAI | October 1, 2026 | [Uniform exclusion of Landau–Siegel zeros](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf) | One c>0 for all primitive nonprincipal real Dirichlet characters of conductor q>=3 and their real zeros beta in (0,1): (1-beta)log(q)>=c. |
| OpenAI | September 25, 2026 | [An unconditional first moment for cubic Gauss sums](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf) | All-primary-prime first moment (6/5)c_* X^(5/6)/log(X)+o(X^(5/6)/log(X)); each fixed nonzero angular Fourier mode has little-oh cancellation at this scale. |
| OpenAI | September 24, 2026 | [Ordinary two-point correlations of multiplicative functions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf) | Every fixed nonproportional affine Liouville correlation has O_forms(X/log^c X), absolute c>0; general uniformly nonpretentious multiplicative factors have qualitative ordinary binary cancellation. |
| Baiying Liu | October 8, 2026 | [Slightly improved zero-free half-planes for the quasi-Riemann hypothesis](https://github.com/liubaiying101/Slightly-improved-zero-free-half-planes-for-the-quasi-Riemann-hypothesis/blob/7d10420de90efa2f082a06a342fc7accbd57ab37/Slightly%20improved%20zero-free%20half-planes%20for%20the%20quasi-Riemann%20hypothesis.pdf) | Same Hecke and Dirichlet families: B_new=(1507-2sqrt(921))/1653 = 0.874957069799..., improving 7/8 by about 4.29302008e-5. |

All half-plane inequalities are strict. Principal poles at s=1 are allowed, rather than counted as zeros. Primitive and imprimitive characters are covered after finite Euler-factor transfer. These assertions do not put zeros on Re(s)=1/2.

The official scope note `lean/docs/003.md` describes formalizations of the 7/8 results and uniform real-zero gap, excluding the principal poles in Dirichlet/Hecke statements. It expressly excludes the papers' later applications from the formalization scope. The October 5 alternate proof is not listed among that note's associated formalized manuscripts.

## Mechanisms and transferable boundaries

The September 30 proof has two stages. Its common continuation principle, Proposition 2.1 (`lem:continuation-criterion`), compares a direct bound on a normalized cubic-theta average with a Mellin signal containing a reciprocal L-function. The positive power margins are uniform over the target family; constants and eventual thresholds may depend on the fixed target. A family-wide supremum of zero real parts is essential because Poisson rows twist the target by additional Hecke characters.

The 11/12 stage uses balanced scales, completed cubic-theta reflection, a quadratic large sieve for reflected rows, a planar additive large sieve for reduced fractions, and one inverse-polynomial zero witness. The 7/8 stage introduces prime compensation, asymmetric scales, and simultaneous inverse/plain witnesses with the same row character and height. Separate moment estimates bound their common exceptional row set. Keeping the two witnesses correlated is an available direction for genuinely new estimates.

The October 5 companion embeds a fixed Möbius sum A_1(D) in sextic-twisted sums A_u(D), proves a family mean square of size D^(1+epsilon)H, and uses the many replicas u=p^6. With Y=H^(1/6), A_(p^6)=A_1+O(D/Y), so

    |A_1|^2 << D^(1+epsilon) H^(5/6) + D^2 H^(-1/3).

Taking H close to D gives the 11/12 exponent. Its completed cubic-theta transform becomes a quadratic twist, avoiding a higher-order large-sieve term. Cube completion must be inverted; discarding cube terms is invalid because they can cancel. The proof controls a short cube prefix directly and the remainder by a recursion at smaller scales.

The September 25 cubic first-moment theorem is expressly unused by the September 30 proof. It improves cancellation for structured prime-convolution coefficients using several-length moments and a Gram estimate; it does not improve the arbitrary-coefficient cubic large sieve. Its angular modes are fixed, with no growing-mode uniformity. In its normalization c_*=(2pi)^(2/3)/(3Gamma(2/3)), both conjugate primary prime ideals are counted. Its rational-prime consequence has coefficient (3/5)c_*, not (6/5)c_*. The manuscript itself records a conflicting historical normalization in Dunn–Radziwill; the two conventions must not be silently identified.

Liu's improvement spends slack in the same estimates. The decisive class is x=1/2 and delta_c=(49-sqrt(921))/48. At that class R=2/3 makes the high exponent independent of the scale difference b. Its endpoint and a tangency condition determine ell and b. Proposition 25.1 is an exact dual certificate for three explicitly assumed affine constraints; the broader optimality of the full estimate system is presented as an expectation, not as a theorem about the true arithmetic energy.

The ordinary two-point theorem is family 007. It expressly permits constants that need not be effective and does not assert growing-coefficient uniformity. Its general Elliott conclusion has no quantitative rate. The strongest literal Liouville saving has c=delta/(6WA), with delta=1/200, A a large absolute finite-law exponent, and W a large absolute graph parameter. The proof uses independent-residue graph traces, exact bounded-independence correction for Boolean circuits, and rough-shift short-interval Fourier cancellation. Its full split source tree and comparator metadata are downloaded under `sources/chowla/`; the quantitative and growth restrictions are extracted in `TWO_POINT_ARCHITECTURE.md`.

The comparator `.lean` files intentionally contain `sorry`: they are theorem statement challenges, not proof files. Their JSON identifies the solution modules `OAI.NumberTheory.TwoPointCorrelations.FinalMain` and `OAI.NumberTheory.OrdinaryCorrelations.Elliott.Main`, with only `propext`, `Quot.sound`, and `Classical.choice` permitted. The scope documentation describes a formalization, but this wave has not built or audited that complete solution closure. A statement challenge must not be presented as an independently verified proof.

An exact-title scan of the official catalogue found no separate release family explicitly about Möbius, Mertens, a large sieve, or cubic theta beyond the directly relevant families 003, 007 and 023. The large-sieve and theta statements needed here are internal lemmas of those manuscripts, with additional classical inputs listed below; this observation is about catalogue titles, not a claim that every one of the 719 manuscripts was read.

## Adjacent classical inputs

These are precise citations supplied by the primary manuscripts; their full sources were not independently downloaded and audited in this wave's initial extraction.

| Source | Transferable input | Scope limit |
| --- | --- | --- |
| A. Dunn and M. Radziwill, *Bias in cubic Gauss sums: Patterson's conjecture*, Annals 200 (2024), 967–1057; [arXiv:2109.07463](https://arxiv.org/abs/2109.07463), DOI 10.4007/annals.2024.200.3.3 | Explicit cubic-theta cusp expansions and level Voronoi formulas. | The cited cusp expansions are unconditional; their GRH-conditional prime asymptotic is not an input to the 7/8 proof. |
| V. Blomer, L. Goldmakher, B. Louvel, *L-functions with n-th-order twists*, IMRN 2014, 1925–1955; [arXiv:1112.1650](https://arxiv.org/abs/1112.1650) | Higher-order character norm recursion and sextic large-sieve framework. | An exceptional-row upper bound does not exclude every zero. |
| L. Goldmakher and B. Louvel, *A quadratic large sieve inequality over number fields*, Math. Proc. Cambridge Philos. Soc. 154 (2013), 193–212; [arXiv:1112.1642](https://arxiv.org/abs/1112.1642) | Quadratic family norm bounded by row length plus column length, up to small powers. | Preserve the quadratic family and coefficient independence when transferring. |
| P. Gao and L. Zhao, *Moments and one level density of sextic Hecke L-functions*, Functiones et Approximatio 70 (2024), 7–28; [arXiv:2201.01885](https://arxiv.org/abs/2201.01885) | Eisenstein-integer sextic estimates. | One-level density concerns averages. |
| C. David, A. de Faveri, A. Dunn, J. Stucky, *Non-vanishing for cubic Hecke L-functions*, [arXiv:2410.03048v2](https://arxiv.org/abs/2410.03048v2), 2026 version | Cubic large sieve and mollified moments at the central point. | Positive-proportion nonvanishing is not pointwise nonvanishing for every family member. |
| L. Guth and J. Maynard, *New large value estimates for Dirichlet polynomials*, Annals 203 (2026), 623–675; [arXiv:2405.20552](https://arxiv.org/abs/2405.20552) | Large-value and zero-density improvements. | Zero-density estimates do not exclude individual zeros. |
| J. Maynard and K. Pratt, *Half-isolated zeros and zero-density estimates*, IMRN 2024, 12978–13014; [arXiv:2206.11729](https://arxiv.org/abs/2206.11729) | Truncated-reciprocal zero detection. | Retain saturation, common character/height, and available witness lengths. |

## Local reproducibility and source hashes

Downloaded sources reside outside the checkout in `/workspace/.riemann-research/sources/`. The SHA-256 of the official September 30 TeX is `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`; its PDF is `8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`. October 5 TeX: `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`; PDF: `f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18`. Cubic first-moment TeX: `8cfe4339113b0f734a728e59f7bc82a17fbd15084c04097ba103ced76f2f10c3`. Liu's frozen repository archive: `c24076c1fae6b66f38361fb5417c5bf427a81c18cca6fb9b8c8a1e126f20c0b7`.

The first-moment root TeX uses external inputs: its complete `sections/{background-type1,dual,dispersion,decomposition,perron,angular}.tex` and `figures/proof-map.tex` are downloaded under `sources/cubic/`, with exact frozen URLs and hashes in `manifest.json`. The two-point split technical sources are under `sources/chowla/build/{qualitative,quantitative}/`, with `manifest.json` and `lean-manifest.json`. Its PDF SHA-256 is `ccb6f339a7505db7ab158dae4b739164ed8dda32be4012b0310198dd32f5c70a`.

Initial direct OpenAI, arXiv, and Google HTTPS requests were denied by the network proxy. Official GitHub and raw-source downloads succeeded through the existing configured route. This source identification required no network-policy bypass.
