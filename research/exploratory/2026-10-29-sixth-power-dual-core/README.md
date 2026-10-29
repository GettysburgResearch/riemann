# Sixth-power dual frequencies in the small-gcd correlation

**Status.** This is a source-qualified partial estimate for a sparse high-dual subrange, not the full small-divisor core or a zero-free theorem. It imports the fixed-sector physical Poisson formula and sextic Gauss calibration from [the low-dual analysis](../2026-10-29-low-dual-theta-bound.md), and the completed-theta mean and cube inversion in [OpenAI October 5, Proposition `prop:R` and equation `eq:cube-inverse`](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex). Their full analytic proofs are not independently verified here. An independent audit is requested.

In the fixed-column-ray sextic physical correlation at `P=Y^(6/5)`, retain the original common column gcd `d=1` and its divisor term `k=1`. Restrict the dual-frequency ideals to **good sixth powers** `v=a⁶`. In a dual dyad `Nv≈H` with `H≲Y^ε P²/Y=Y^(7/5+ε)`, the resulting contribution is

    ≪ Y^ε (Y/P) H^(1/6) P^(1/3)
     ≪ Y^(13/30+ε).                                            (1)

Summing the logarithmically many dual and auxiliary-gcd dyads preserves the bound. This covers only the sixth-power dual ideal subset of the original d=k=1 block; it does not control non-sixth powers, growing original gcd/divisor terms, or the whole signed core.

## A pointwise theta estimate

Let C(n)=`overline(α(n))γ₂(n)` in the source's squarefree good-ideal normalization. Fix a finite ray character ξ and a squarefree good ideal f. For a compact smooth annular W define

    P_f(T)=T^(−1/2) Σ_(n good squarefree)
       C(n) ξ(n) χ_n(f)^4 W(Nn/T).                              (2)

All residue symbols retain their zeros. Proposition `prop:R` at its row index k=1 states, uniformly for fixed polynomial ranges,

    |T_f(X)|² ≪ (X Nf)^ε (1+Nf/X),                             (3)

for the completed theta sum T with the same `χ_n(f)^4` factor, fixed-ray profile and its stated seminorms. Its exact `eq:cube-inverse` expresses P_f(T) as a sum over cube indices c with coefficient of modulus at most `1/Nc` and completed argument `T/(Nc)³`. The source's elementary coefficient bound gives `|T_f(X)|≪X^(1/2+ε)` uniformly in f. Weighted Cauchy for `Nc≤C` and the elementary tail for `Nc>C` therefore give

    |P_f(T)|² ≪ (T Nf)^ε [1+Nf C³/T+T/C³].                    (4)

If `Nf≤T²`, choose `C³=T/sqrt(Nf)`; otherwise use the elementary absolute bound `|P_f(T)|²≪T^(1+ε)`. Hence uniformly in polynomially bounded f,T,

    |P_f(T)|² ≪ (T Nf)^ε min{T, 1+sqrt(Nf)}.                  (5)

Empty annuli and bounded scales are absorbed into the constants. Both the fixed finite ray character ξ and a bounded common norm-frequency phase are allowed with the source's polynomial profile-height loss.

## Exact sixth-power mask and the gcd projector

For a fixed good a, the residue symbol identity is

    χ_n(a⁶)=1_{(n,a)=1}.                                       (6)

In the source-normalized d=k=1 dual expression, use the exact projector for `(r₁,r₂)=1` and write `r_i=g n_i` with good squarefree g. The diagonal `r₁=r₂` is absent because mutually coprime equal r_i would both be the unit, outside the P-annulus. On a dyad `Ng≈G`, the residual n-scale is `D≈P/G`. The exact source multiplicativity is

    C(gn)=C(g) C(n) χ_n(g)^4.                                  (7)

The factor χ_g(a⁶)χ̄_g(a⁶) is the mask `1_{(g,a)=1}`. It is legitimate to discard that outer mask only after expanding the square or applying Cauchy to the two original column profiles. We now fix g coprime to a and retain the remaining mask `1_{(n,a)=1}`.

Expand the latter by Möbius inversion over `d|rad(a)`, then write n=d m. Squarefreeness imposes `(d,m)=1` and the source multiplicativity gives

    C(dm)χ_(dm)(g)^4
      = C(d) C(m) χ_d(g)^4 χ_m(d)^4 χ_m(g)^4.                 (8)

The factor χ_m(d)^4 includes the zero when `(m,d)>1`, so it supplies the squarefree condition even if the m-sum is formally extended. Since `(d,g)=1`, multiplicativity gives the exact identity with zeros

    χ_m(d)^4 χ_m(g)^4 = χ_m(dg)^4.                             (9)

Thus each divisor term is of the form (2) with squarefree label `f=dg`, length `T=D/Nd`, common finite-ray profile, and exterior factor of modulus `1/sqrt(Nd)`; any ray phases from (7)–(8) are separated into finitely many fixed classes. No moving a-dependent puncture is discarded. Terms with empty or bounded T are harmless.

Combining (5), the trivial bound `|P_f(T)|≪T^(1/2+ε)`, and the divisor estimate for fixed K,

    |Σ_(n good sf,(n,a)=1) C(n)χ_n(g)^4 W(Nn/D)/sqrt(Nn)|²
       ≪ (P Na)^ε min{D, 1+sqrt(G)}.                            (10)

Indeed the source bound gives each divisor contribution at most `(Nd)^(−1/2)[1+(G Nd)^(1/4)]`, whose sum is `≪(Na)^ε(1+G^(1/4))`; the trivial bound gives `sqrt(D) Σ_(d|a)1/Nd≪sqrt(D)(Na)^ε`. The `1/sqrt(Nn)` convention differs from (2) only by absorbing the bounded annular factor into W.

## Physical summation

Separate the radial kernel in the original dual expression by the source's fixed-sector logarithmic Fourier method, before taking absolute values. Its two column profiles and one bounded dual phase then have uniform fixed seminorms, and Cauchy reduces their mixed product to two squares covered by (10). For `Ng≈G`, the exterior coefficient from the two `r_i=g n_i` normalizations is `(Y/P)/G`. There are `O(G)` ideals g and `O(H^(1/6))` sixth-power roots a in the dual dyad. Hence the separated absolute contribution is at most

    (Y/P) H^(1/6) min{P/G,1+sqrt(G)} (PH)^ε.                  (11)

The final minimum is `≪1+P^(1/3)` for all G≥1: if `G≤P^(2/3)`, use `1+sqrt(G)`; otherwise use P/G. At the natural Poisson cutoff `H≲Y^ε P²/Y`, (11) is (1). The source transform's rapid tail and the polynomial Fourier-height costs are handled using fixed sufficiently high Schwartz orders before absorbing small powers.

The proof bounds the **restricted** original dual sum absolutely after retaining the source phases and all masks. It does not replace the full signed sum by the sum over sixth powers, infer positivity of other frequencies, or justify removing any global diagonal after separate dyad majorants.

**Independent review.** Other_families checked the source-stated `prop:R`/cube-inversion deduction, the squarefree label f=dg and its zero masks, divisor weights, physical normalization, sixth-power ideal count and exponent 13/30. High_match separately checked the algebra and orientation. The imported analytic theorems, physical Poisson calibration and full profile/Fourier replay are not independently established by these reviews.

## Dual frequencies with small sixth-free core

The same argument extends to good dual ideals `v=b a⁶` with b sixth-free, allowing b and a to share primes. This decomposition is unique by prime valuations. In dual and core dyads `Nv≈H`, `Nb≈B`, the restricted d=k=1 contribution obeys

    ≪ (Y/P) (H/B)^(1/6) min{BP/G, B+B^(3/2) sqrt(G)} (PBH)^ε
    ≪ Y^(13/30+ε) B^(7/6).                                    (12)

uniformly after summing the logarithmic auxiliary g dyads and using `H≲P²/Y`. The core bound `Nb≤B₀` follows by summing logarithmically many B dyads. Thus at the 125/144 moment target `Y^(21/20+ε)`, this subrange is controlled whenever `B₀≤Y^(37/70)`. To beat the staged θ boundary exponent `19949123/18750000`, it is controlled with a strict margin for fixed `B₀≤Y^b` and `b<11824123/21875000≈0.54053134`. This is a restriction on the sixth-free **dual core** b, not a bound for all high dual frequencies.

For the first bound, keep the exact identity

    χ_n(b a⁶)=χ_n(b)1_{(n,a)=1},                               (13)

including all overlapping b,a primes. The outer g factor vanishes unless `(g,a)=1`; after the two-column Cauchy inequality its remaining `|χ_g(b)|²` mask may be dropped. Expand the a-mask over `d|rad(a)` as before. Equation (8) now has one additional factor `χ_d(b)χ_m(b)`: its first component is a bounded multiplier depending on b,d, and the second is exactly the source row character χ_m(b). The f-label remains `gd`, squarefree because `(g,a)=1`; no coprimality between b and a, d or g is assumed. All zeros at these shared primes are retained until the appropriate bounded multiplier is removed.

For every fixed squarefree f and any row bound B, `prop:R` and the same cube inversion give

    Σ_(Nb≤B) |P_b(T;f)|²
       ≪ (TBNf)^ε [B+B^(3/2) sqrt(Nf)],                         (14)

where `P_b(T;f)` is (2) with the additional factor χ_n(b), and the source sum is over all permitted b rows (restricting to sixth-free b only decreases it). To prove (14), the short cube-index part contributes `≪B+B² Nf C³/T` by weighted Cauchy and `prop:R`; the elementary tail contributes `≪B T/C³`. If `BNf≤T²`, choose `C³=T/sqrt(BNf)`. If `BNf>T²`, the trivial bound `B T` is already at most `B^(3/2)sqrt(Nf)`. Bounded and empty scales are harmless.

Apply Minkowski in the b-row ℓ² norm to the d|rad(a) expansion. The coefficient `χ_d(b)` has modulus ≤1, and divisor bounds give

    Σ_(Nb≤B) |S_g(D;a,b)|²
       ≪ (P B Na)^ε min{B D, B+B^(3/2)sqrt(G)}.               (15)

Here the first term is the trivial pointwise bound; the second uses (14) with f=gd, the outer `(Nd)^(−1/2)` factor and `Σ_(d|a)(Nd)^(−1/4)≪(Na)^ε`. Because `Nb≈B` and `Nv≈H`, there are at most `(H/B)^(1/6)` roots a. Sum over that containing ball only after the absolute-value/Cauchy step, and use the complete b≤B mean (14); O(G) auxiliary labels g and the original `(Y/P)/G` coefficient give the first line of (12). Finally

    min{BP/G, B+B^(3/2)sqrt(G)} ≪ P^(1/3)B^(4/3),              (16)

by comparing the two terms at `G≈(P/sqrt(B))^(2/3)` and using B,P≥1. This proves (12) conditional on the same source calibration, Fourier-profile uniformity and completed-theta inputs as (1). It does not estimate the complementary sixth-free core `Nb>B` or license cancellation between unrelated frequency subsets.

**Independent extension review.** Other_families checked the complete b-average, the shared-prime χ_d(b) multiplier, the squarefree label gd and its zeros, and the dyadic root saving `(H/B)^(1/6)` and both exponent thresholds. The cited analytic, Poisson and profile inputs remain unverified externally.

## Original common gcd with k=1

The same source-qualified method extends to the original common-gcd dyad `Nd₀≈D₀`, still with k=1 and sixth-free dual core `Nb≈B`. Assume the nonnegligible dual range `H≲Y^ε P²/(Y D₀²)`; then the residual column scale is `D≈P/(D₀G)`. The original columns require `(g n_i,d₀)=1`, so `(g,d₀)=1`. The dual `a⁶` mask requires `(g,a)=1`. Combine the two residual column masks **before** opening them:

    1_{(n_i,a)=1}1_{(n_i,d₀)=1} = 1_{(n_i,rad(a d₀))=1}.       (17)

Expand (17) once over `e|rad(a d₀)`. Then `(g,e)=1`, so the completed-theta label `f=ge` is squarefree and the exact χ_m(f)^4 zero convention still applies. This single expansion is necessary: expanding two overlapping masks separately and multiplying their symbols could produce a non-squarefree f. The divisor loss is `(Na Nd₀)^ε`, and the bound (15) remains valid at the new scale D, uniformly in d₀ and its finitely many fixed ray sectors.

There are `O(D₀^(1+ε))` choices of the original squarefree gcd, and the original physical coefficient is still `(Y/P)/G`: the two factors μ(d₀) cancel. Therefore

    |B_(D₀,k=1; Nb≈B)|
       ≪ Y^ε (Y/P) D₀ (H/B)^(1/6)
             · min{B P/(D₀G), B+B^(3/2)sqrt(G)}
       ≪ Y^(13/30+ε) D₀^(1/3) B^(7/6).                      (18)

In the last step optimize G as in (16) with P replaced by P/D₀, then insert the H cutoff. Large dual tails are removed by the source transform's rapid decay; when the cutoff makes H<1 there is no nonzero dual ideal, up to that negligible tail. The residual P/D₀-annulus remains ≫Y^(1/2) on the nonnegligible range, so the artificial equal-column principal pair is absent. This proves a source-qualified bound for the **k=1** gcd dyad, not for growing divisors k|d₀.

Writing `D₀=Y^d`, `B=Y^b`, (18) is at most `Y^(21/20+ε)` when

    d/3 + 7b/6 ≤ 37/60.                                         (19)

It lies strictly below the staged θ threshold when `d/3+7b/6<11824123/18750000`, with all fixed source losses chosen inside the margin. As before, b is the sixth-free dual core and this control cannot be extended to the remaining frequencies or to the full signed core without further input.

## Growing k: source-qualified small-core bound

For an original gcd/divisor dyad `Nd₀≈D₀`, `Nk≈K`, write `d₀=k d′`. Assume the exact source physical fixed-sector correlation and its common-profile Fourier separation, as in the earlier sections and [the mask-preserving ledger](../2026-10-29-mask-preserving-second-poisson.md). For good `v=b a⁶` with b sixth-free, `Nb≈B` and `Nv≈H`, the k-dependent sextic factors obey the exact identity including zeros

    χ_n(g)^4 χ_n(k)^5 χ_n(b) = χ_n(gk)^4 χ_n(bk).              (20)

The source's g is coprime to d₀; the a⁶ dual mask also requires `(g,a)=1`. Combine the remaining source puncture d′ and a-mask into `1_{(n,rad(a d′))=1}` and expand once over `e|rad(a d′)`. Since d₀ is squarefree, `(k,d′)=1`; if e meets k, the factor `χ_e(k)^5` makes that entire term zero. On surviving terms `f=gke` is therefore squarefree. The source χ_m(f)^4 factor retains all its zeros. The e-dependent factor is `χ_e(b)χ_e(k)^5=χ_e(bk)χ_e(k)^4`: the first factor is a bounded b-row multiplier and the second is a fixed e,k phase. Shared b,k or a,b primes are allowed. The residual column scale is `D≈P/(D₀G)` and the Poisson dual cutoff is `H≲Y^ε P²K/(Y D₀²)`.

Fix k before applying the b-average. The map `b↦bk` is injective, so positivity allows its source row sum to be enlarged to all row labels of norm `≪BK`. Proposition `prop:R`, cube inversion and the e-divisor Minkowski step give

    Σ_(Nb≈B) |S_{g,k}(D;a,b)|²
       ≪ Y^ε [BK+B^(3/2)K²sqrt(G)].                            (21)

The row label and f may share primes; the source's original zero extension is retained. In a **separate** estimate do not enlarge the b set: direct absolute counting of the D-annular source gives `|S_{g,k}|²≪D`, and there are only `O(B)` actual b labels. Thus the same mean is also `≪Y^ε BD`. This elementary branch is uniform in k and all the masks.

The physical factor is `(Y/P)/(KG)`. There are `O(D₀/K)` choices for d′, `O(K)` for k and `O(G)` for g, up to small powers. The a-root ball has size `≪(H/B)^(1/6)`. After Cauchy/absolute values and these sums, the total is

    ≪ Y^ε (Y/P)(D₀/K)(H/B)^(1/6)
       · min{B P/(D₀G), BK+B^(3/2)K²sqrt(G)}.                 (22)

Since B,K,G≥1, the second summand in the theta branch dominates BK. The elementary minimax inequality

    min{B P/(D₀G), B^(3/2)K²sqrt(G)}
       ≪ (P/D₀)^(1/3) B^(4/3) K^(4/3)                       (23)

holds even if its formal crossing lies outside the nonempty G range. Inserting the dual cutoff gives

    |B_(D₀,K; Nb≈B)|
       ≪ Y^(13/30+ε) D₀^(1/3) K^(1/2) B^(7/6).               (24)

The roots and b-labels are enlarged independently only after Cauchy, so no extra multiplicity of a given dual ideal is assumed. The source's artificial principal restoration and rapid tails must be handled as in the cited ledger; (24) bounds this specified nonzero-frequency, small-core contribution and does not control its complement. It remains conditional on the exact original physical phase, fixed-sector matching and source Fourier/profile uniformity.

**Growing-k arithmetic review.** Other_families checked the zero-preserving identity (20), the vanishing of e meeting k, the squarefree source label gke and the injection b↦bk. The sharper K^(1/2) power uses the actual B-row trivial bound before enlarging the row set; the fixed-sector physical identity, principal restoration and Fourier-profile replay remain source inputs.
