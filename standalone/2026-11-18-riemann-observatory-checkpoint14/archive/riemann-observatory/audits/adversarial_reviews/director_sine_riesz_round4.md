# Director adjudication: expected sine-Gram law, clipped transfer, and growing Riesz construction

2026-11-17. These are scoped ordinary mathematical proofs with named external classical inputs and multiple independent reconstructions. No whole-paper Level3 promotion, publication novelty, unconditional zeta higher-moment estimate or RH proof is asserted.

## Expected sine-Gram law: scope and verdict

Accepted THM-SG301–310, with their exact model and conditional distinctions. Sources/reviews: sine_gram_all_moments_round3.md; sine_gram_moment_existence_round4.md; sine_gram_skeptic_round4.md; sine_gram_moment_existence_third_round3.md; the separately preserved advocate, analytic and semantic fourth-moment reviews. The shared generic review filename was found to collide; the advocate's exact original was recovered from the uploaded checkpoint and both independent versions now have unique filenames. They are not counted as extra results.

The director independently reconstructed the following mechanisms.

1. The sampling comparison uses phi=2sinc(2x)sinc(x), Fourier transform equal1 on[-1/2,1/2], L1 norm<2 and supremum<=2. Scalar Jensen on an eigenbasis, not an invalid operator power inequality, gives TrS^k<=2^k integralW^k. Correlation determinants satisfy0<=rho_j<=1. A set-partition expansion plus Bell_k<=k! gives every expected per-length moment<=4^k k!.
2. In a trace word, identifying repeated point labels gives a connected Eulerian multigraph. Loops contribute1 and the remaining graph is bridgeless. All labelled parallel edges remain distinct. Averaging all spanning trees gives edge probabilities0<theta_e<1. Generalized Hölder applied to the weighted product of rooted tree integrands yields an absolute integral bounded by products of sinc L^(1/theta_e) norms. Every such norm is finite. The single-vertex case is separate. The exact anchored window factor is(1−span(0,u)/R)_+, so dominated convergence proves every fixed expected moment limit. No determinant sign expansion is needed for this existence argument.
3. Tightness, uniform higher-moment integrability and the factorial bounds give a unique full EXPECTED per-length spectral law, exponential moments and Hamburger determinacy. No almost-sure empirical-law theorem, rate or growing-m uniformity is proved.
4. No atom at0 follows from one global close-pair deletion and fixed-block capping, the exact Paley–Wiener interpolation theorem at subcritical uniform density, and principal-minor interlacing. The Riesz lower constant may depend on the configuration. Taking a deterministic lower quantile of its measurable positive value handles this dependence; no uniform constant is assumed. Cauchy–Schwarz controls the bad event without independence, and OPEN-set Portmanteau has the required direction. The exact PW2 theorem was inspected through primary research restatements; the original Beurling/Seip proofs remain declared external. A separate Bernstein-to-PW2 strict-margin argument was independently reconstructed.
5. Positive-root canonical quadratures, moment tightness and determinacy show the Christoffel values at0 tend to zero. This supplies the precise law hypotheses needed for the conditional all-fixed-moment route, not the arithmetic matching itself.

The first four model moments are independently checked as1,4/3,2,13/4. For the fourth, all15 trace partitions and24 determinant permutations are included. The all-distinct four-cycle integral is zero. In particular the crossed doubled-edge integral is11/30; the director independently derived it by Fourier autocorrelation, obtaining2 integral_0^1 ell^3(1−ell/3)dell. This is independent of the other reviewers' flow-polytope calculation. The pure random model's valueD=116 is NOT an estimate for the prime-side zeta matrix.

## Clipped Hilbert–Schmidt transfer

Accepted finite lemma and conditional application THM-SG306–308. Root independently derived Hoffman–Wielandt from Hermitian trace rearrangement and checked all clipping directions. The relevant finite squared-displacement and Lipschitz empirical-test lemmas were actually compiled in Lean, using only propext, Classical.choice and Quot.sound. Global polynomial clipping, asymptotic spectral laws and the zeta application were not silently called formalized.

For fixed realq<=1_(0,infinity), h=max(q,−1) is bounded and globally Lipschitz. For HermitianF,G in the SAMEd-dimensional space,

n_+(G)/d>=Trq(F)/d−Lip(h)||F−G||HS/sqrt(d).

This is a trace stability statement and does not assert scalar Lipschitz functions are operator-Lipschitz. At0 the indicator inequality is preserved. For the specified quarticq=1−(1−7x/4+2x²/3)^2, the director checked the exact identity(pprime)^2=(8/3)(p+19/128), giving the global clipped Lipschitz bound6 from211/6<36.

Keep the dimension factorr=d/N in the finite block consequence:

s1/N>=2r Trq(F)/d−1−12r||F−G||HS/sqrt(d).

Withr→1, relativeHSerror→0, low moments→1,4/3 andD=84m3−16m4, a finite lower limitD0 gives simple-critical fraction at least(D0−103)/18. A boundD>115 would beat2/3;D=116 gives13/18; exceeding the statedA005 fraction requiresD>31699883/275355. No such arithmetic bound is proved. A model computation cannot supply it.

This bridge only needs relativeHS control. It avoids falsely transferring higher polynomial moments through rare large outliers, and avoids requiring operator-o(1). It therefore combines legitimately with the independently proved zero-buffer localization. The single mixed-moment target is a precise missing inequality, not evidence that the inequality is easier than its separate third/fourth moment counterparts.

## Growing logarithmic Riesz array: accepted conditional theorem

Accepted THM-E-W312 and W313. The director read the complete proof and its rate addendum AFTER independently deriving the contour/kernel construction and free auxiliary scale. Independent skeptic review checked actual Titchmarsh source passages, all noncompact tails, kernel moments and quantifier dependencies. Historical priority is unassessed; actual Lee1996 and modern Riesz-source comparisons are ongoing.

For EVERY FIXEDc>0, sufficiently large integerN, define

epsilon_N=c/loglogN, alpha_N=epsilon_N logN,

V_(N,c)(s)=Sum_(n<=N)mu(n)(1−logn/logN)^(alpha_N)n^(−s),

with the n=N term0. For each fixed integerq>=1 let

d_q(V)^2=(2pi)^−1 integral_R |1−zeta(1/2+it)V(1/2+it)|²/|1/2+it|^(2q)dt.

Then RH implies

d_q(V_(N,c))=O_(q,c)((loglogN)^(-1/3)).

Conversely d_q(V_(N,c))→0 implies RH by the previously reconstructed Hardy evaluation witness for arbitrary finite coefficient arrays. Thus this is an equivalent criterion for each fixedc. It does not prove RH or improve a bound for actual zeta zeros. It uses a different prescribed array from the fixed logarithmic Selberg family; its growing order cannot be substituted silently into that unresolved fixed-array question.

The exact inverse-Laplace contour starts where the Mobius series is absolutely convergent and shifts only withinRew>0. Under RH there are no reciprocal-zeta poles there; the zeta pole is a reciprocal zero. The fractional power uses principalLogw throughout that half-plane. For eachN, horizontal integrals vanish from subpower inverse growth and the actual kernel decay; there is no hidden finite Perron truncation.

Writingalpha=epsilon logN, the complex kernel is

K(v)=Gamma(alpha+1)exp(alpha+i v logN)/[2pi(logN)^alpha(epsilon+iv)^(alpha+1)].

Its exact mass is1. Its absolute density in y=v/epsilon isB_alpha(1+y²)^(-(alpha+1)/2), B_alpha=O(sqrtalpha), with uniformly bounded mass, exponentially small full tail outside|y|<=eta and exact first absolute moment2B_alpha/(alpha−1)=O(alpha^-1/2).

On the center, the RH paired xi product gives a uniform horizontal completion ratio; the source logarithmic-derivative formula controls the short vertical shift. Choosing fixedeta small yields an integrable height majorant. Critical zero ordinates are a null set; no pointwise limit1 there is asserted. For the quantitative comparison to zeta(s)/zeta(s+epsilon), the first absolute kernel moment gives O(alpha^-1/2).

The decisive tail estimate retains its N-dependent loss. For every FIXEDa>0, the source RH bounds and the low-height Borel–Carathéodory patch give

sup_(|u|<=V, sigma>=1/2+a/loglogV, sigma<=2)|1/zeta(sigma+iu)|
<=exp(K_a logV/loglogV).

Takea=c/2 and a freely chosen small FIXEDr>0, V=|t+v|+N^r+3. For sufficiently largeN depending onc,r, epsilon_N>=a/loglogV and the inverse loss is exp[(4K_a r/c)alpha+2K_a ell(t+v)]. Choose r<kappa_eta c/(8K_a). The global subpower height factor is absorbed in a fixed small power of|v| and an integrable height weight, while the kernel contributes exp(−kappa_eta alpha). Minkowski therefore gives a decaying full noncompact tail. The oldN^4 auxiliary scale was not a requirement of this infinite contour; freeing it is what permits every fixedc>0.

Finally the separately reconstructed horizontal ratio zero-excision estimate has squared normO(epsilon^(2/3)). Its bad-zero-neighborhood measure and off-neighborhood logarithmic derivative bounds preserve multiplicities and require no spacing. Combining gives the stated norm rate, distinct from its square. The samec works for every fixedq; constants may depend onq,c. Nothing is uniform asc tends to0, c=c_N moves, q grows, or finiteN is chosen practically. Constants/start thresholds remain unevaluated.

The fixed-alpha multiplicity obstruction and the new varying-alpha construction are compatible: the former applies to one fixed Mellin/Riesz exponent. The present alpha_N diverges, so it does not impose a fixed finite multiplicity ceiling. No simplicity, reciprocal-derivative moment or zero-spacing assumption has entered the proof.

## Stronger published input: accepted W314 update

The preceding1/3 rate is preserved as the historically reconstructed first proof, not the best rate now available for this array. Accepted THM-E-W314: for every fixed c>0 and integer q>=1 the same array has, under RH,

d_q(V_(N,c))=O_(q,c)((loglogN)^(-1/2)), with squared norm O_(q,c)(1/loglogN).

PAPER-C103, Balazard–de Roton Proposition2, gives the exact horizontal-ratio quantity J_epsilon=O(epsilon), not the weaker zero-excision bound used above. The owner read the entire20-page manuscript; the skeptic independently reconstructed a contractive-xi/Poisson proof before comparing the primary residue proof on pp4–8. The director read both completed reconstructions, checked the paired-product derivative, harmonic measure normalization, completion logarithmic derivative, clockwise contour sign and reciprocal-zeta expansion at1. No issue was found in this inspected source argument or its transfer. The comparison error O(alpha^(-1/2)) is o(sqrt(epsilon_N)), giving the displayed rate.

Evidence: audits/balazard_roton_ratio_round3.md and audits/adversarial_reviews/balazard_roton_poisson_skeptic_round4.md. The stronger ratio estimate is established prior mathematics, not a discovery of this program. The source also obtains a substantially stronger optimized Nyman–Beurling distance bound by a different array; the present transfer is not advertised as a record distance bound. Priority of the particular moving-order construction is still unassessed.
