# Primary-source continuation: the sharper horizontal-ratio estimate

Date:2026-11-17. Reader:equivalences. Canonical work PAPER-C103, not a new paper-count entry. Actual primary source `sources/selberg_round2/balazard_roton.pdf`, with arXiv0812.1689v1 header9December2008 and body date8November2018; the version/date discrepancy remains recorded. The published2010 text was not compared. After the earlier track readpp1–5, I substantively read **all20pages** of this private primary manuscript, including§§3–7 and references. This supports whole-work Level1, not whole-paper Level2: the Soundararajan/Maier–Montgomery external technical dependencies are not fully reconstructed from their original proofs.

This note gives a scoped technical reconstruction ofProposition2 and its dependenciesPropositions4–5, printedpp5–8. It is distinct from any audit ofProposition3's sharper Möbius partial-sum estimate.

## Exact source statement and normalization

For0<epsilon<=1/2, on s=1/2+it,

J_epsilon=(2pi)^−1 integral_R |zeta(s)/zeta(s+epsilon)−1|² dt/|s|².

Proposition2, marked(HR), asserts **J_epsilon≪epsilon under RH**. This is the exact horizontal ratio in the growing logarithmic-Riesz campaign. It is not a symmetric functional-equation quotient, a truncated-height norm, or a derivative-moment hypothesis.

The source's main theorem concerns the different shifted Möbius array and yields optimizedd_N²≪_delta (loglogN)^(5/2+delta)(logN)^−1/2 for fixeddelta>0. Hence applying its ratio estimate to our array does not improve the best source upper bound for the optimized distance.

## Completed reconstruction ofPropositions4–5 and2

Write F_epsilon(s)=zeta(s)/zeta(s+epsilon) and completedxi(s)=s(s−1)pi^(−s/2)Gamma(s/2)zeta(s)/2. UnderRH the paired Hadamard product gives|xi(s)/xi(s+epsilon)|<=1 forRe(s)>=1/2. Each paired comparison or symmetric zero-height cutoff preserves this inequality; normal convergence follows from the usual zero count. Completion factors and uniform Stirling giveProposition4(i), |F|²≪|s|^epsilon on the critical line, and the more useful(ii),

|F_epsilon(s)|²<=1+C epsilon |s|^(1/2), Re(s)=1/2.             (BR1)

The completion ratio has logarithm at most epsilon log(|s|/2)/2+O(epsilon/|s|). To keep uniformity through epsilon=1/2, use the convexity chord x^epsilon−1<=2epsilon(sqrt(x)−1), x>=1, rather than losing an unnecessary logx factor; compact values1/2<=|s|<=2 are bounded directly. Together with the O(epsilon/|s|) factor this bounds the squared modulus by1+Cepsilon |s|^(1/2), uniformly forepsilon<=1/2. No pointwise comparison through a denominator zero is used: underRH the shifted line has no zero.

DefineK_epsilon=integral|F|²dt/(2pi|s|²) andL_epsilon=integralFdt/(2pi|s|²). The real coefficients ofzeta makeL real by t↔−t. ThusJ=K−2L+1. Integrating(BR1) givesK<=1+O(epsilon), since integral_R |s|^(−3/2)dt is finite and integral_R dt/(2pi|s|²)=1.

ForL useQ(s)=F_epsilon(s)/[s(1−s)]. It is meromorphic onRe(s)>=1/2 with one pole at1, of order2. Shifted zeta's pole at1−epsilon gives a zero ofF, not a new pole. The sourceProposition4(iii) bounds|Q(s)|≪|s|^(epsilon/2)/|s−1|² in this half-plane. For0<epsilon<=1/2 this makes the large closing arc vanish and the boundary integral absolutely convergent. There is no unsourced interchange of an infinite zero sum with the contour integral.

The residue computation yields the exact sourceProposition5,

L_epsilon=(gamma−1)/zeta(1+epsilon)−zeta'(1+epsilon)/zeta(1+epsilon)²
 =1−(gamma+1)epsilon+O(epsilon²).                            (BR2)

This checks the orientation sign: closing to the right gives minus the residue ofQ at1. WithR=1/zeta, R(1+epsilon)=epsilon−gamma epsilon²+O(epsilon³), so(BR2) is(gamma−1)R+R', yielding the stated first coefficient. CombiningK<=1+O(epsilon), L=1+O(epsilon), andJ>=0 provesJ≪epsilon.

The source also remarks that a neighborhood of a known simple zero givesJ_epsilon≫epsilon. I have not independently audited the computational/simple-zero input behind that remark here. It is not needed for the upper estimate.

## Exact transfer to the growing-order array

For every fixedintegerq>=1, |s|>=1/2 implies

||F_epsilon−1||_q²<=2^(2q−2)J_epsilon≪_q epsilon.

The independently reconstructed convolution estimate inTHM-E-W313 gives||zeta V_N−F_epsilon||_q=O_(q,c)(alpha_N^−1/2), apart from a smaller exponential tail. Therefore, underRH, for each fixedc>0 andalpha_N=c logN/loglogN,

d_q(V_N)=O_(q,c)((loglogN)^−1/2),

d_q(V_N)²=O_(q,c)((loglogN)^−1).                            (BR3)

This transfer has compatible norm measures, the same horizontal shift, and the same RH premise. The new array and the source's optimized-distance bound must remain distinct. Independent review of this scoped source reconstruction and transfer is requested before elevating(BR3).

## Reading limits and next tasks

All20manuscript pages have now been read substantively. The main proof'sV-typical ordinates, adaptive Perron contour, height split and tail estimates were followed as a dependency architecture, while its originalSoundararajan and zero-count-majorant inputs remain accepted cited dependencies. This is not a complete Level2 audit or a claim about the2010version's correction history. The source's several missing-inverse symbols in late displayedI_N estimates are interpreted from the consistent definition and proofs; no new source-error finding is asserted here.

For a materially better prescribed-array rate, trace parameter dependence as the auxiliary near-line constanta shrinks and compare with the source's much stronger Proposition3 rather than optimizing a weaker historical bound in isolation. The fixed-c result alone makes no claim of best possible smoothing order or practical computational usefulness.
