# Director adjudication: further scoped reconstructions

2026-11-17. These verdicts apply only to the explicit claims below. The director read both independent reconstructions, checked the mathematical transitions described here and reran the finite certificates noted. None promotes an entire paper to Level3, asserts novelty, certifies the complete AF theorem, or resolves RH.

## Uniform shrinking-epsilon Möbius input

Accepted at scoped technical-reconstruction level: THM-E-D202–D204. Source and independent review are `audits/baez_uniform_dependency_round2.md` and `audits/adversarial_reviews/baez_uniform_skeptic_round2.md`.

The director checked that the finite-height bound requires two regimes: the actual-height Titchmarsh region applies above exp(sqrt(log V)); below that height, Borel–Carathéodory applied to the pole-removed (s−1)ζ(s) supplies the missing uniform bound. Simply replacing the actual height by V would be unjustified. Titchmarsh14.14.4 is an equality-line statement and is not quoted as a half-plane theorem by itself.

For the Perron rectangle, height N^4 and left shift−epsilon/2 leave a N^(−epsilon/2) factor. The reciprocal growth and log N integration loss are absorbed by c=6(8K+1) when epsilon>=c/loglog N, leaving N^(−epsilon/3). Integer endpoint half-weights are bounded explicitly. The small-epsilon J estimate splits zero neighborhoods of width delta=epsilon^(2/3); it is not asserted through the pole-reaching endpoint epsilon=1/2. These facts yield the original O((loglog N)^(−1/3)) norm conclusion conditionally on the named classical RH inputs. Their historical ancestry has not been completely audited. Degraded source typography, the unexamined journal-version comparison and unevaluated thresholds remain limitations.

## Explicit rational-inner boundary realization

Accepted: THM-RI303–RI308 under their stated finite-dimensional/positive-length assumptions. Independent third proof: `audits/adversarial_reviews/inner_realization_third_round2.md`; full construction: `proposals/independent_campaigns/factored_inner_round2.md`.

The director checked the adjoint-domain argument rather than symmetry alone, compactness of the graph-domain embedding, maximal invariant dark-state decomposition, and the real-resolvent transfer identity. A real visible eigenvalue of Omega−iG*G/2 would force an Omega-eigenvector in ker G and hence be dark, which is impossible on the visible complement. The determinant phase budget is2pi times visible dimension over the whole line; its positive-axis increment is at most that dimension. Dark counts add monotonically. Positive phase crossing follows from strictly positive interval lengths. Thus −3E−2M<Delta N<3E+M for E>=1, and matching the positive Riemann–von Mangoldt curvature with o(K) errors forces 3E+M>=K log2/pi−o(K). This is a cost restriction on these models, not a spectral construction for zeta.

The common-domain intersection with the uncoupled reference can be nondense, so the earlier finite-defect theorem cannot remove M. Allowing E=0 requires weak finite-dimensional inequalities. Real-axis unitarity alone is insufficient; the inverse Blaschke example has negative crossing velocity.

## Global Lagarias comparison-profile concavity

Accepted upgrade of the existing concavity review group: g(t)=log[(H(e^t)+exp(H(e^t))log H(e^t))/e^t] has g''<0 for all t>=0, with H(x)=psi(x+1)+gamma. The analytic tail and exact finite proof are in `proposals/independent_campaigns/lagarias_global_concavity_round2.md` and its independent audits.

The director checked the derivative integral bounds, the sign-sensitive sufficient inequality N[x/(x+1)]^2+BB'/(2x)<0, the harmonic-sum integral enclosures, and the exp/log remainder directions in the independent integer backend. All170 rational cells covering[1,2048] were replayed successfully using only standard-library integer arithmetic. The tail for x>=2048 is analytic. This is a computer-assisted ordinary proof, not a floating-point observation or Lean theorem.

Shared-supporting-parameter endpoint interpolation follows. Arbitrary abundant endpoints do not supply that hypothesis, and this does not certify the infinite arithmetic endpoint sequence. No priority claim is made.

## Pressure-aware finite-chain transfer

Accepted: THM-F006, conditional on the exact local seven-point inequality and frozen source hypotheses. Proposer and skeptic independently derived the endpoint pressure identity; root checked it algebraically and reran all390 rational knot inequalities and30 endpoint checks.

For m=n+6, the exact unused pressure is Delta=6spread−sum_w span_w=Sum_(r=0..4)(5−r)g_r+Sum_(r=0..4)(r+1)g_(n+r). The prefix-potential bounds give P<=alpha Delta−30alpha theta, including overlapping end blocks. The frozen positionwise rewards satisfy0<=h_(i,1)<=h_(i,2), and summing over positions gives y=69433/10^6. Each fixed position omits exactly six chain sites, so reward loss is at most6y. Consequently the finite loss becomes C*=6y−30alpha theta=516027/2000000, replacing0.432480 by0.2580135.

For chains of length<=6, y>=6alpha theta is essential and holds in the frozen data. The explicit singleton counterexample to dropping this guard is retained. Directed/signed energies require the exact symmetrized defect and cannot reuse nonnegative-energy assertions. The Std-only Lean replay checks finite integer conditions, not the complete real interpolation/chain theorem. This O(1) improvement changes no asymptotic proportion. Sharpness of bookkeeping does not imply sharpness of the full energy inequality.

## Trace localization and zero-buffer transfer

Accepted scoped replacements: THM-F007 and F008. The director inspected the original AF proof of Theorem A in section6, the source trace passage, the two independent localization proofs and the separate Vinogradov–Korobov refinement.

For the fixed even C2 window and critical grid, the bilinear Poisson identity is constant even at complex zeros, by normal convergence and analytic continuation. Absolute-square Parseval gives normalized total mass O(sqrt X/L) per zero. Unit endpoint strips contain O(L) zeros. For interior zeros at distance D>=1, use omitted-grid tails with D−h>=D/2; for exterior zeros, use retained-grid tails. Both are O(sqrt X/(L D^3)), so summing local zero counts gives O(sqrt T). The first omitted grid point can lie inside I; the printed unrestricted distance step is not used.

The omitted-zero matrix is an absolutely nuclear-convergent sum because ||vv^T||_1=||v||^2, even though vv^T need not be positive. At zero buffer its norm is O(sqrt T)=o(sqrt N), N asymptotic to T log T. That is enough to transfer the Hilbert–Schmidt square with O(N/sqrt(log T)) loss. The exact finite block rank–trace deduction in section6 has no dependency on Weyl or an operator error tending to zero. All prime-side moment and identification inputs remain separate.

The classical Vinogradov–Korobov strip, reflected by the functional equation, gives |Im gamma|<=1/2−delta(3T) on comparable heights. The local mass and Fourier tails acquire exp(−delta L), while remote heights contribute O(T^(−3/2)). Hence the nuclear bound is O_A(sqrt T L^(−A)) for each fixed A and preserves the separately assumed prime-side rate. The original zero-free proof has not been audited; its source statement and exact uniform role are explicit. No new limiting zero proportion is asserted.

## Exact kernel tables and actual formal build

The already adjudicated first-table method also checked the second and third tables:733298 total whole-cell inequalities, each with exact rational lower bounds. Only the FIRST full continuum search was rerun; the other two full searches remain unreplayed. The pinned RankTrace Lean source module actually compiled and its queried theorem dependencies were exactly propext, Classical.choice, Quot.sound. This is a module-level replay; the main Multiplicity target is still a separately tracked process. Neither table checking nor that module build certifies all analytic or numerical dependencies of a headline theorem.

## Still pending

The positive-kernel/Bessel quartet, strict-log-concavity certificate and beta extension have since completed independent review; the additional verdict below supersedes the earlier pending status. The Pólya1926 baseline zero/count theorem is recovered prior art. New source typographical observations, including Montgomery's missing absolute value in one local display, require their own precise source-locator review and must not be described as false main theorems.

## Positive Bessel kernels and the beta-normalized arithmetic deletion test

Accepted scoped results: THM-LB301–LB312, with the exact model-class and source boundaries in their records. Proposer proof, independent skeptic and independent third reconstruction are saved in the Bessel campaign, positive_kernel_beta_smoothing_round3.md, bessel_third_round3.md, beta_smoothing_third_round3.md and the two first-negative reviews. No publication novelty is established.

The director independently checked the all-complex-order-zero self-adjoint argument (not merely the existence of real spectral zeros), the differentiated Lagrange identity for analytic simplicity, the exact I-series phase derivative, the global kernel lower bound, min–max Li margin and quartet binomial sum. Both exact log-concavity programs were replayed: one reconstructs in cosh coordinates and the other independently uses Laurent/Chebyshev coordinates and inverse Bernstein expansion. Their199 rational monomials,30 coefficient groups and positive Bernstein coefficients prove the global sign on v>=1,T>=32,6<=c<=7. No sampled sign or external symbolic package is trusted.

The beta extension uses the normalized entire MGF of (delta²−u²)^(3/4) on a compact interval. The director checked its moment normalization, all-complex-zero energy proof, Fourier endpoint exponent7/4, count retuning c=2pi exp(2delta), and the one-dimensional integration-by-parts variance inequality. The latter retains the singular beta endpoints: p is comparable to d^(3/4), F=O(d^(7/4)), u=F/p=O(d), so every required boundary term vanishes. It proves a strictly negative second logarithmic derivative after convolution.

Normalization is essential: F(0)=F(1)=1 and Z=pi^(s/2)F/[s(s−1)Gamma(s/2)] WITHOUT a factor1/2. Thus the residue is1 and Z(0)=−1/2. The independently noticed factor2 disagreement was resolved as a change of completion convention, not an algebraic error.

For eachN>=1 the explicit quartet height T_N=10N(8N²+50) admits a tuning delta in(0,.01), by a rigorous IVT endpoint bound. Its firstN Li coefficients exceed1/[12(8N²+50)²]. The same model has exactly four off-line zeros, the RVM smooth count+O(1), positive even smooth strictly log-concave kernel, standard functional equation/gamma factor/pole/trivial zeros, and bounded right vertical strips. Tuning enforces the right limit1, but Z(sigma)=1−b/sigma+O(sigma^−2), b=c²/2+21/(32delta)−3/16>0. An ordinary Dirichlet series would instead have an exponentially small right tail. The missing arithmetic property is therefore exhibited by an explicit asymptotic witness, not merely named.

Fixed-T tuning can have double critical-line zeros. A separate generic-delta refinement legitimately restores all-simple zeros by excluding the countable analytic collision set, with adjustableT tending to infinity. It does not certify noncollision at a named rational/algebraic delta. All-positive Taylor coefficients of the auxiliary transformed function also follow from the positive even kernel; this does not establish all Li coefficients positive.

The first-negative asymptotic is accepted for this model family and every tuned branch:

n_-(T)=8T²logT+8T²loglogT+8(log2)T²+o(T²).

The director independently checked the exact quartet expression4[1−cosh(n eta)cos(n theta)], eta~1/(4T²), the uniform Bessel coefficient asymptotic .5nlogn+O(n), the beta bound0<=lambda_n(beta)<=n²delta²/9, the two lower-index regimes, and an O(T) phase-aligned upper index. Centering y=n eta at2logT+2loglogT−loga, a=1/4, gives ratio4e^y/(nlogn)→1, including the stated constant. The result provides an asymptotic masking scale, not an effective numerical first-negative index. The mechanism is established prior Bombieri–Lagarias/Lagarias mathematics; the quantified assembly has unassessed priority. It implies the model-only inverse scale T~(1/2)sqrt(N/logN), with no effective startingN claimed.

Neither model is an arithmetic L-function or an RH counterexample. In particular its bounded critical-line values give mean square O(X), which does not reproduce zeta's classical mean-square asymptotic. The positive kernel also gives an exact maximal-modulus identity, but matching that leading growth scale still does not provide integer Dirichlet support.

## Growing multiplicity from the exact finite optimum

The proposed transition and its independent refinements are accepted conditional on the previously checked exact optimum formula. Root, corpus and semantic_skeptic reconstructed the artanh bounds and all scaling regimes. Independent reviews have unique paths; the original source formula is a separate audited dependency.

ForC=N+m+1/2, A=m²/C and the explicit B in growing_multiplicity_transition_round3.md, one has1−e^(−A)<=E<=1−e^(−A−B). In particular E~m²/N holds exactly in the regime m=o(sqrtN); ifm²/N→lambda thenE→1−e^(−lambda), and ifm²/N→infinity thenE→1. A stronger direct upper bracket in the third review simplifies necessity. This is a finite polynomial statement; the degreeN is not automatically a logarithmic arithmetic cutoff.

## Universal scalar reciprocal window

The new fixed-degree scalar-window theorem in unit_circle_scalar_window_round3.md and its independent polynomial_window_third_round3.md review is accepted at the stated fixed-m scope. Root independently derived a separate Euler-operator majorant and checked the sharper twisted finite-difference identity supplied by the equivalences agent. Negative indices, n=M and the final m−1 coefficients are all included.

For Q=product(1−q_j z), |q_j|=1, reciprocal coefficientsb_n, and A=Sum_(n=0..M−1)b_n(1−n/M)^m z^n, the squared error is at mostK_m/M with the explicit degree-only constant in the proof. No separation is needed. For completely coincident roots the leading error ism²/M, matching the optimum. Lower nonnegative integer taper powers fail uniformly through the terminal coefficient. The finite construction may have error greater than1 for smallM, and is not a finite-M optimizer. Further exact quadratic worst-case and fractional-power refinements retain their separate review statuses.

## Fixed synthetic multiset: operator-o(1) does not follow

Accepted THM-F010. The director independently checked the fixed inverse-RVM background plus sparse off-line quartets and the exact smooth-endpoint Fourier identity in AF_no_buffer_operator_countermodel.md. The excluded near pair produces a positive diagonal asymptotic of size exp(L/4)/L²; other sparse pairs cannot cancel it, while real background diagonals are nonnegative. The multiset has both symmetries, local countO(logT), RVM count+O(logT), and an eventual VK strip. Its operator tail diverges along a fixed sequence even while its relative Hilbert–Schmidt error tends0.

This refutes only an attempted inference from those abstract count/window/strip assumptions to operator-o(1). The synthetic multiset is not claimed to satisfy the zeta explicit formula or the full prime-side moment. The source proportion theorem and our relative-HS transfer are unaffected.

## Converse-theorem normalization and a narrow background attribution

The director read the actual Knopp2000 introduction, Nakamura v4p4 and Burnol v2pp2–3, independently reconstructed the variable/frequency change, and checked the independent source review. The original Knopp1994 pp361–363 were subsequently obtained and agree with the author's2000 restatement.

Knopp's R(u)=pi^(−u)Gamma(u)phi(u), reflection1/2−u, becomes the standard zeta completion only aftert=2u. An ordinary series forphi(u) then has frequencies sqrt(n) in thet variable; ordinary integer frequencies return only with square-supported coefficients. The literal standard-variable conjunction H2,H3,ordinaryK in Nakamura v4p4 instead implies a scalar zeta multiple by an exact hypothesis match to Burnol Corollary2. Thus the background abundance attribution needs a variable/frequency qualification. This is not an objection to Nakamura's explicit main examples, which relax the frequency or finite-pole hypothesis. The published journal wording has not been compared and no correction history is claimed complete.

The integer-comb lemma in hamburger_dictionary_round3.md is also checked directly: integer support makes the Fourier transform periodic; a quasi-homogeneous discrepancy analytically extends to an entire polynomial periodic function and is constant; comparison at0 and1 excludes Dirac derivatives and forces constant masses. The deeper Mellin/distribution dictionary retains its declared classical inputs and partial-audit scope. This identifies integer support, rather than an Euler product, as the exact rigidity used in this converse route.

## Christoffel function versus one-sided inertia

The director inspected AF v2p13's informal remark and independently checked two different rational finite Hermitian witnesses from two agents. The unrestricted ordinary-Christoffel reading is false: that function bounds mass at the evaluation point and gives a rank bound; an inertia bound additionally needs a valid polynomial minorant of the positive-halfline indicator. A negative root of the minimizing polynomial can invalidate it.

The source's specific conditional sine moments survive. For moments(1,1,4/3,2,13/4), p=1−7x/4+2x²/3 satisfies p>=1 onx<=0 and E p²=5/36. Thus1−p²<=1_(x>0), giving positive inertia at least31/36 and, under the source's separate block/count assumptions, the conditional13/18 simple-critical conclusion. This is a qualification of the informal general remark, not a refutation of the main source theorem or its specific conditional polynomial calculation. Full prime/block hypotheses are not modeled by the finite counterexamples. Record the finding as missing/insufficiently stated one-sided hypothesis, with no unsupported main-author-error label.
