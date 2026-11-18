# Sine-process Gram moment laws: exponential tails, no zero atom, and the conditional moment ladder

Date: 2026-11-17. Proposer: li_advocate. Independent reconstructions by the parent and li_skeptic are saved and cited below. No novelty or RH claim. These are scoped statements about a random Gram model, not verification of a zeta prime-side higher-moment hypothesis.

## Scope and precise conclusions

Let X be the stationary unit-intensity sine determinantal point process onR, with kernel

    K(x,y)=k(x−y),    k(t)=sin(πt)/(πt),    k(0)=1.

For R>0 let X_R=X∩[0,R], N_R=#X_R, and let G_R=(k(x−y))_{x,y∈X_R}. Define the expected, per-length spectral measure

    μ_R=(1/R) E sum_{j=1}^{N_R} δ_{lambda_j(G_R)}.

This is a probability measure on[0,∞), since E N_R=R. The following proof establishes:

1. For every integer j≥1 and R>0,

       ∫t^j dμ_R(t) ≤4^j j!.

2. The family μ_R is tight as R→∞. Every weak subsequential limit is a probability measure on[0,∞), has no atom at0, has an exponential moment, and is moment determinate.
3. A subsequent independently checked Eulerian-graph/spanning-tree Hölder proof establishes every expected fixed moment limit and hence a unique full weak limit μ_R⇒μ. It is saved as THM-SG309 and in the moment-existence review cited below. No almost-sure integrated density of states, convergence rate, growing-moment limit, or arithmetic moment matching is asserted.
4. For this unique limiting law μ, the ordinary minimum-square Christoffel values λ_m(0;μ) tend to0. Its nondegenerate kernel polynomials have only positive roots, so their squared-polynomial complements are valid one-sided positive-index certificates even for an indefinite Hermitian matrix with the same moments.

Together with the existing zero-side index geometry, matching **every fixed finite moment prefix** to this law would yield simple-on-line proportion1. It does not supply that arithmetic matching.

## Primary sources and source boundary

* Soshnikov, *Determinantal Random Point Fields*, arXiv:math/0002099v4 (28 November2000), published Russian Math. Surveys55(5) (2000), 923–975, DOI10.1070/RM2000v055n05ABEH000321. Actual primary preprint inspected at p3, Definition2/Eq1.5 (factorial moment convention); p8, Definition3/Eq1.20 (determinantal correlations); p13, Theorem3 (existence for0≤K≤I); p28, Eq2.35 (the exact unit-intensity sine kernel). Whole66-page preprint not read/audited.
* Gaunard, *Minimality, (Weighted) Interpolation in Paley-Wiener Spaces & Control Theory*, arXiv:1110.1714v1, printed pp2,5–7 and bibliography. Actual p7 Theorem3 visually inspected: a uniformly separated set in a finite horizontal strip with upper uniform density D^+<τ/π is interpolating for PW_τ^p. This is explicitly a Paley–Wiener L^p theorem, including p=2, not merely a Bernstein sup-norm theorem. It cites Seip1995 Theorem2.2 and Beurling1989. Those original proofs were not accessed. The exact PW² statement is a primary-research restatement accepted as an external classical interpolation theorem in this campaign.

The original Seip1995 publisher PDF and AMS2004 chapter PDF returned403. No source is called read on that basis. Private PDFs, extracted text, and page images are in `sources/sine_gram_round3/` and must not be distributed as archive source copies.

## 1. Elementary sine-process facts used

The correlation functions are ρ_l(x1,...,xl)=det(k(x_i−x_j)). Each kernel matrix is positive semidefinite with diagonal1, so Hadamard's inequality gives0≤ρ_l≤1. In particular

    ρ1=1,    ρ2(x,y)=1−k(x−y)^2≤1,
    E N_R=R,
    Var N_R=R−∫_[0,R]^2 k(x−y)^2 dxdy ≤R.

These follow directly from the inspected factorial-moment convention. The process is simple and locally finite. No mixing or ergodicity theorem is needed below.

## 2. A deterministic sampling-to-multiplication comparison

Use Fourier transform fhat(ξ)=∫ f(t)e^{−2πitξ}dt, and let H=PW_[−1/2,1/2] be the corresponding closed subspace of L²(R). Its orthogonal projection P has kernel k(x−y), with P(t,t)=1. Evaluation has unit-norm reproducing vector k_x(t)=k(t−x).

For any finite point set Y, the sampling operator T_Y:H→C^Y has Gram matrix G_Y=T_YT_Y^*. The finite-rank positive operator S_Y=T_Y^*T_Y has the same nonzero eigenvalues.

Choose a reproducing convolution function φ with φhat=1 on[−1/2,1/2], v=|φ|∈L¹∩L∞, and C=||φ||1. For f∈H, f=φ*f and weighted Cauchy–Schwarz gives

    |f(x)|² ≤ C ∫ |f(t)|² v(x−t)dt.

Thus with W_Y(t)=sum_{x∈Y}v(x−t),

    0≤S_Y≤C P M_{W_Y}P.

The right side is trace class, since W_Y is integrable. For an integer j≥1, min–max eigenvalue monotonicity gives

    Tr S_Y^j ≤ C^j Tr(PM_{W_Y}P)^j.

No general noncommutative power-monotonicity assertion is used. If u_i are normalized eigenvectors of PM_WP in H with eigenvalues b_i, scalar Jensen gives b_i^j≤∫W(t)^j|u_i(t)|²dt. The reproducing-kernel Bessel inequality gives sum_i|u_i(t)|²≤P(t,t)=1. Therefore

    Tr S_Y^j ≤ C^j ∫W_Y(t)^jdt.                         (SG1)

All interchanges are of nonnegative quantities. For finite Y, W is bounded and integrable, so every displayed integral is finite.

## 3. Factorial moment bound and an explicit constant

A smooth Schwartz φ would suffice. Independently, li_skeptic supplied the useful explicit choice, with sinc(t)=sin(πt)/(πt),

    φ(t)=2 sinc(2t)sinc(t).

Its Fourier transform is the convolution of1_[−1,1] and1_[−1/2,1/2], equal to1 on the whole required band. Also ||φ||∞≤2 and

    ||φ||1 ≤2 ||sinc(2·)||2 ||sinc||2 =sqrt2<2.

The1/t² decay makes φ integrable; Schwartz regularity is not needed for(SG1). For this choice0≤v≤2 and ∫v≤2.

Expand E W_{X_R}(t)^j according to set partitions π of{1,...,j}. If π has l blocks B, the factorial-moment formula and ρ_l≤1 give the corresponding term at most

    product_{B∈π} ∫_0^R v(x−t)^{|B|}dx.

Put a_R(t)=∫_0^R v(x−t)dx≤2. Since v≤2, the product is at most2^{j−l}a_R(t)^l≤2^{j−1}a_R(t). Integration over t gives at most2^jR for each partition, because ∫a_R=R∫v≤2R. The number Bell_j of set partitions is at most j!: inject a partition into the permutation whose cycles list each block in increasing order. Hence

    E∫W_{X_R}(t)^jdt ≤2^j R Bell_j ≤2^j R j!.

Combining with(SG1) and C≤2 proves

    (1/R)E TrG_R^j ≤4^j j!.                           (SG2)

An alternative check uses any reproducing φ and the DPP Laplace functional bound obtained by expanding factorial moments:

    E exp(θW_R(t))≤exp(A_R(t)),
    A_R(t)=∫_0^R(e^{θv(x−t)}−1)dx≤A∞=∫(e^{θv}−1).

Since e^a−1≤a(e^{A∞}−1)/A∞ and ∫A_R=RA∞,

    (1/R)E TrG_R^j ≤ C^j j! θ^{−j}(e^{A∞}−1).

This independently reproduces the factorial growth mechanism without assuming independence of the sine points.

## 4. Consequences for subsequential moment laws, without an IDS assumption

Exactly TrG_R=N_R, so μ_R has first moment1. Markov's inequality makes the family tight. Every weak limit μ is supported on[0,∞) and retains the moment bounds by truncation/Portmanteau. In fact the uniform(j+1)-moment bound gives uniform integrability of t^j, so along any weakly convergent subsequence its moments converge to those of μ.

For0<z<1/4, monotone convergence and(SG2) give

    ∫e^{zt}dμ(t) ≤sum_{j≥0}(4z)^j=1/(1−4z).

Thus μ is Hamburger-moment determinate, meaning unique among positive measures on all ofR, not only among Stieltjes measures; alternatively Carleman's series diverges because m_{2j}^{1/(2j)}≤4[(2j)!]^{1/(2j)}=O(j). The fixed-moment limits were subsequently proved independently by the Eulerian-graph argument documented below. Thus all subsequences have the same moments, determinacy makes their laws identical, and full expected-law convergence follows. This does not supply an almost-sure spectral-law statement.

The conventional expected spectral measure normalized by N_R rather than R has the same weak subsequential limits: for bounded test functions the discrepancy is at most E|N_R/R−1|≤R^{−1/2}, after any fixed probability convention on the event N_R=0.

## 5. Thinning, Beurling interpolation, and no zero atom

Fix δ>0, a block length L>1 and0<η<1, with M=floor((1−η)L)≥1. Construct a **single global subset** Λ of the infinite process X, independently of the later window R:

1. Remove every point having another process point within distanceδ.
2. In each half-open block[nL,(n+1)L), retain at most M surviving points, using a fixed measurable ordering rule.

Λ is δ-separated. Every interval of length r meets at most r/L+2 blocks, so

    D^+(Λ)≤M/L<1.

Apply the inspected PW² interpolation theorem with τ=π. For each configuration, the reproducing vectors {k_x:x∈Λ} form a Riesz sequence with a strictly positive lower bound a(ω). The bound need not be uniform over configurations.

For clarity, interpolation-to-Riesz uses only Hilbert-space duality. Evaluation T:H→ℓ²(Λ) is bounded on a separated set (the same convolution comparison, with the1/t²-decaying v, gives a uniform bound on sum_{x∈Λ}v(x−t)). Interpolation says T is onto. The open mapping theorem gives a bounded right inverse, hence T^* is bounded below. Its finite synthesis Gram forms are exactly the sinc matrices. This gives a(ω)>0 for **every** finite subset of Λ.

One can choose a measurable lower constant: take the infimum of the smallest Gram eigenvalues for Λ∩[−n,n], n∈N, assigning value1 to an empty set, and cap the result at1. These finite eigenvalues are measurable functions of the finite ordered point configurations. Beurling's theorem says the infimum is positive. Therefore for every ε>0 there exists a deterministic a_ε>0 with P(a(ω)<a_ε) arbitrarily small.

Let D_R=#(X_R\Λ) be the deleted count. The expected loss from the close-point deletion is at most2δR, by the ordered two-point count and ρ2≤1. For a complete block, the subsequent capping loss is bounded by(N_L−M)_+, so

    E(N_L−M)_+ ≤E|N_L−L|+(L−M)≤sqrtL+ηL+1.

The last incomplete block costs at most L in expectation. Consequently

    E D_R/R ≤2δ+η+1/L+1/sqrtL+L/R.                    (SG3)

On the good event a(ω)≥a_ε, Cauchy interlacing of the retained principal Gram minor shows

    #{j:lambda_j(G_R)<a_ε}≤D_R.

On the bad event it is at most N_R. No independence between the event and N_R is assumed: Cauchy–Schwarz and VarN_R≤R give

    E[(N_R/R)1_bad]≤sqrt((1+1/R)P(bad)).

Given ε>0, first choose δ,η small and L large so the constant part of(SG3) is small; then choose a deterministic quantile a_ε with P(bad) small; finally take R large. This yields

    limsup_{R→∞} μ_R([0,a_ε)) ≤ε.                    (SG4)

For any weak subsequential limit μ, apply Portmanteau to the **open** interval(−1,a_ε), since all measures are supported on[0,∞). It gives μ({0})≤ε. As ε was arbitrary, μ({0})=0.

This quantile argument avoids the unproved stronger demand for one Riesz lower bound uniform over every capped configuration. It also avoids stationarity/ergodicity assertions about the thinned process and avoids assuming an almost-sure IDS exists.

## 6. Why Christoffel values now tend to zero

Let μ be any law obtained above. It is a Stieltjes measure that is determinate in the stronger Hamburger sense, and μ({0})=0. Define λ_m(0)=min_{deg p≤m,p(0)=1}∫p²dμ.

If μ has finite positive support, a polynomial vanishing on that support makes λ_m(0)=0 for all sufficiently large m. Otherwise its moment Hankel matrices are positive definite. Stationarity of the minimum says ∫x p_m h dμ=0 for all h of degree≤m−1. The minimizer has full degree m: if its degree were smaller, taking h=p_m would give∫x p_m²dμ=0, impossible. The elementary sign-change argument for orthogonal polynomials applied to the positive measure x dμ gives m distinct positive roots.

The node0-plus-roots quadrature from the independent CMS review is a positive probability measure ν_m matching moments through2m, with ν_m({0})=λ_m(0). Its fixed second moment makes ν_m tight. Along any weak subsequence, higher fixed moments ensure uniform integrability, so the limit matches all moments of μ. Determinacy identifies that limit with μ. Portmanteau for the closed set{0} yields

    limsup λ_m(0)≤μ({0})=0.

Therefore λ_m(0)→0. This proof states explicitly the law properties required by an all-moments-to100% argument; they do not follow from the first four moment values alone.

## 7. Conditional transfer to the AF moment ladder

Suppose a Hermitian family H_T of dimensions d_T~N_T has every fixed normalized moment prefix converging to the moments of one such law μ. For each fixed m, use p_m above and q_m=1−p_m². Its positive roots imply q_m≤1_{(0,∞)} onR and q_m(0)=0. Then

    liminf n_+(H_T)/d_T ≥1−λ_m(0).

If H_T=A_T+E_T, ||E_T||→0, the threshold minorant q_m(x)≤1_{x>δ}+C_mδ and Weyl's inequality transfer the same lower limit to n_+(A_T). If the already established zero-side geometry gives s1_T≥2n_+(A_T)−N_T+o(N_T), then

    liminf s1_T/N_T ≥1−2λ_m(0).

Take m→∞ **after** the T→∞ lower limit to obtain1. No moment estimates uniform in m(T) are needed. What remains arithmetic is precisely the convergence of every fixed higher-moment prefix to this particular sine-Gram law, plus matching normalization/window definitions. This campaign establishes none of those prime-side estimates, makes no unconditional100% assertion for zeta, and makes no RH claim.

The later independent connection `audits/adversarial_reviews/hilbert_schmidt_moment_transfer_round3.md` weakens the sufficient perturbation hypothesis to ||E_T||HS=o(sqrtd_T). For each fixed polynomial q_m, replace it by the bounded Lipschitz minorant max(q_m,−1). This increases its expectation and transfers its certificate directly by Hoffman–Wielandt, without transferring higher moments. Alternatively transfer the full weak empirical law and use its absence of mass on(−∞,0]. The operator-norm condition above is sufficient, but no longer necessary for this archive’s conditional bridge.

## Independent review checklist and limits

The operator comparison, scalar Jensen/Bessel trace bound, factorial expansion, thinning losses, quantile treatment, and open-set Portmanteau direction have been independently reconstructed by the parent and/or li_skeptic. Final durable third-review references should be appended after they are saved. The Beurling–Seip PW² interpolation theorem remains an explicit external classical source dependency, accessed through Gaunard's primary research restatement; its original proof is not claimed audited.

No numerical eigenvalue agreement is used as proof. Full expected-law convergence and every fixed expected moment limit are now established by the accepted addendum below. Almost-sure law convergence, rates, sourceAF's arithmetic HL*(k0), and novelty/prior-art completeness remain outside the established scope.

Durable independent review now saved: `audits/adversarial_reviews/sine_gram_skeptic_round4.md`. The reviewer reconstructed the core arguments before reading this draft, then read this complete file and found no issue in the inspected argument. The review also gives a separate direct Laplace-transform proof that λ_m(0)→0 and a Bernstein-to-PW² strict-margin interpolation derivation from an additional actual primary source. The original1995 proof is still not claimed read. That original independent review covered the subsequential-law stage; the accepted addendum below strengthens it to a full expected model law. The arithmetic moment ladder remains conditional.

## Accepted addenda: full expected law and first four exact moments

The moment-existence limitation was closed by li_skeptic’s proposer proof `proposals/independent_campaigns/sine_gram_moment_existence_round4.md`, theoremTHM-SG309 in its separate JSONL, independently reconstructed before reading by `audits/adversarial_reviews/sine_gram_moment_existence_third_round3.md` and checked by the parent. Each trace partition yields a connected Eulerian, hence bridgeless multigraph after loop deletion. Spanning-tree edge probabilitiesθ_e lie strictly between0 and1. Weighted Hölder factors the rooted integral into sinc L^(1/θ_e) norms, all finite. Stationary translation gives overlap factor(1−span/R)_+; dominated convergence establishes every fixed expected moment limit. The factorial bound then gives uniqueness and full expected weak convergence.

The exact first four model moments are now independently derived in `audits/adversarial_reviews/sine_gram_fourth_moment_advocate_archived_round3.md`, with exact code/results `sine_gram_fourth_exact_round3`. They are(1,4/3,2,13/4). In particular the previously unverified all-distinct four-cycle integral is exactly0: the24 determinant terms reduce to projection/graph integrals1,2/3,1/2,9/20,11/30,2/5 and cancel. The parent independently verified the delicate11/30 crossing integral using autocorrelation and triangular Fourier overlap. Thus the model valueD=84m3−16m4=116 is checked. This is not a proof that a zeta prime-side matrix attains that value.
