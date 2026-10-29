# Quadratic ideal sieve and fourth- and fifth-order density comparisons

**Status:** Source matching and exponent comparisons, not a proof of the candidate conductor sieve, its detector transfer, or novelty. Fixed fields, original zero extensions, height losses and label multiplicity must be kept in each application. Comparisons with the emerging bounds are conditional on those bounds being established.

## Quadratic large sieve, including squares of quartic characters

Goldmakher–Louvel, [*A quadratic large sieve inequality over number fields*](https://arxiv.org/html/1112.1642), Theorem 1.1 and Corollary 1.2, give for a fixed number field k, fixed bad modulus c, squarefree ideals a,b prime to c, and arbitrary λ_b,

    Σ_(Na≤A)^* |Σ_(Nb≤B)^* λ_b χ_b(a)|²
        ≪_(k,c,ε) (AB)^ε (A+B) Σ_b |λ_b|².

Their Definition 1 spells out the quadratic Hecke-family hypotheses, including a finite-group reciprocity phase and primitive conductors for same-sector products. Corollary 1.2 explicitly permits the quadratic family `χ_b^(n/2)` obtained from an even-order Hecke family; in particular n=4 supplies the square of a quartic family over Q(i). This is a genuinely ideal-indexed, squarefree-row and squarefree-column statement, not the rational quadratic sieve or the quartic large sieve. The source uses primitive characters. For de Faveri's FHL family, squarefree b have good conductor b even after squaring; original b-masks and fixed S deletions must still be matched to the chosen primitive presentations. Finite ray phases can be separated only after fixing the appropriate sector. The theorem does not by itself bound a mixed quartic character sum before the algebra and masking are checked.

The introduction attributes an earlier Q(i) special case to Onodera. The more general [Kuan–Lesesvre, Lemma 6.4](https://academic.oup.com/qjmath/article/73/3/991/6551976) also records the squarefree-ideal inequality, attributing it to Goldmakher–Louvel.

## Full conductor families versus squarefree labels

Fix K=Q(i), and define fourth-power-free labels `g=a b² c³` with a,b,c squarefree and pairwise coprime, all outside S. A good prime occurs in the primitive conductor precisely when it occurs in abc. Its quartic local exponent distinguishes 1,2,3, so fixed-conductor presentations have bounded multiplicity in the primitive family; this assertion uses the FHL good-prime conductor identity and fixed S choices. A fixed finite-order background twist may be included if its conductor is supported in S; a general fixed unitary twist also requires matching its archimedean type to the counting source. The following direct comparison uses no extra twist.

The unconditional [Khale–O'Kuhn–Panidapu–Sun–Zhang, Lemma 3.3](https://arxiv.org/html/2008.09677v3), for a fixed Galois number field K, bounds zeros summed over **all** primitive finite-order ray characters of conductor norm at most X, and over a bounded set of angular modes, by

    (X² T^[K:Q])^[min{3/(2−σ),2/σ}(1−σ)] (log XT)^B.

For Q(i), choose the zero angular mode, enlarge T by an absolute constant if necessary, and use bounded label multiplicity. At `σ=4/5` this yields `X T` up to logarithms; at fixed or polylogarithmic T its X exponent is 1. The paper sketches the corresponding family large-sieve and zero-detection extension; it is a published general-family comparator, not an independently verified input here.

The emerging source-conditional fourth-order sieve `X+X^(2/3)Q` with the proposed saturated detector gives the asserted exponent `R₄(σ)=5/3−σ` for `2/3<σ≤5/6`, and `1−(2σ−1)/[3(3−2σ)]` above 5/6. At `σ=4/5` this is `13/15`; it is smaller than the general conductor comparator for sufficiently small power height, provided all source and detector hypotheses hold. For `4/5≤σ≤5/6`, the fixed-height comparator is `4(1−σ)/σ`: it is weaker than the candidate below `(17−sqrt(145))/6≈0.8264009`, and stronger above. It remains stronger throughout `5/6≤σ<1`. At polynomial heights the source's T factor must be included; the stated crossover is fixed/polylog height.

Blomer–Goldmakher–Louvel, [Corollary 1.6](https://arxiv.org/html/1112.1650), give a stronger exponent `8(1−σ)/(7−6σ)=8/11` at σ=4/5, but only for squarefree labels, a proper subfamily of fourth-power-free `a b² c³` labels. Gao–Zhao's [one-level density of quadratic and quartic Hecke L-functions](https://arxiv.org/abs/1708.01701) concerns scaled low-lying zeros and central nonvanishing, not this off-critical rectangular zero count. Quartic **Dirichlet** character results over Q concern a different family and do not automatically control all Gaussian Hecke characters.

De Faveri, [Corollary 1.5](https://arxiv.org/abs/2610.04045v1), treats the full n-th-power-free family ordered by **index norm**. At n=4 and σ=4/5 its exponent is `1−δ₄=15/22`, with T exponent `1+2(1−σ)/(3−2σ)` for Q(i). This improves the BGL comparator to `15/22` on the squarefree-label subfamily. Conjugation maps the label `(a,b,c)` to `(c,b,a)` and preserves zeros in symmetric height; the smaller of the conjugate label norms is at most `(Nabc)²`. Thus conductor X can be reordered to natural index X² with at most two-to-one multiplicity, yielding exponent `15/11`, a valid but non-saving conductor comparison. This uses conjugation with ν=1; for complex ν it changes ν to barν, requiring both background families.

## Fifth-order check

Take K=Q(ζ₅), a Galois field of degree four, and fifth-power-free labels `g=∏_(j=1)^4 a_j^j` with disjoint squarefree a_j. At every good prime the conductor determines its presence, and the local fifth-order exponent determines j, giving the same bounded-presentation argument. The general Khale et al. bound has X exponent 1 and T exponent 2 at σ=4/5, i.e. `X T²(log XT)^B`.

In De Faveri Corollary 1.5, at n=5, σ=4/5 the middle formula gives `δ₅=12/35`, hence natural-index exponent `23/35`. Conjugation replaces j by 5−j, and the smaller natural index of the two orientations is at most `(N∏a_j)^(5/2)≤X^(5/2)`. Reordering the whole family as above therefore yields exponent `23/14` and height factor `T^(11/7)` (up to ε), again non-saving at conductor scale. For ν=1 and symmetric heights, each conjugate pair costs at most 2; other fixed backgrounds require their conjugates.

Consequently, the emerging conditional fifth-order candidate `R₅=3/4+1−σ=19/20` at σ=4/5 would improve the cited general-character conductor bound for sufficiently small power height. It is not established by the sources in this note. De Faveri's `23/35` natural-index exponent is stronger on the squarefree-label subfamily, as is BGL's `8/11`. A finite targeted search did not locate a sharper theorem directly covering all fifth-power-free conductor labels; that is not a priority claim.

More generally, for `σ>3/4`, the candidate is `7/4−σ`. The Khale et al. fixed-height exponent is

    H(σ) = 6(1−σ)/(2−σ)  for σ≤4/5,
         = 4(1−σ)/σ      for σ≥4/5.

Exact comparison shows the candidate wins for `3/4<σ<(23−sqrt(273))/8=0.8096610447...`, and H wins above that crossover. For `T=X^τ` over Q(ζ₅), the source exponent is `H(σ)(1+2τ)` plus logarithms; choose τ and losses strictly small enough before comparing. De Faveri's conjugate-reordered full-family index bound is larger than the candidate throughout this potential improvement window (for example, it is approximately 1.8478 at σ=3/4 and 1.5963 at the crossover). It becomes smaller than the candidate only near `σ=0.9248458`, where H is already substantially stronger. These statements are comparisons of sourced sufficient bounds and the proposed candidate, not optimality or novelty theorems.

## Further checks: cyclic extensions and newer sources

Lemke Oliver–Thorner–Zaman, [*An approximate form of Artin’s holomorphy conjecture and non-vanishing of Artin L-functions*](https://arxiv.org/html/2012.14422v3), Theorems 3.1 and 6.1, directly address relative zeta functions in families of Galois extensions over an arbitrary fixed number field. For G=C₅, N=G, the intersection multiplicity is 1, and Theorem 6.1 gives

    Σ_(L/k cyclic C₅, D_L≤Y) N_(L/k)(σ,T)
       ≪ (Y T^[5[k:Q]])^[(40+ε)(1−σ)] (log YT)^C.

If k=Q(ζ₅) and the common faithful-character conductor is at most X, the conductor–discriminant formula gives `D_L≪X⁴`. At σ=4/5 this leads to the coarse bound `X^(32+ε) T^(160+ε)`, far larger than the candidate. Their Theorem 3.1 is important earlier work on almost-all zero-free **relative** zeta regions, but its strip width depends on the exceptional-set exponent and is close to 1 in the small-exception regime; it does not state the candidate's σ=4/5 bound.

Chen An, [*Log-free zero density estimates for automorphic L-functions*](https://arxiv.org/html/2004.14410v2), JNT 261 (2024), Theorem 1.1, also treats a fixed arbitrary base number field. Applied to GL(1), fixed infinity type, conductor at most X, and a label family of size `≪X^(1+η)`, it yields X exponent `(15/2+O(η))(1−σ)` and height exponent `([k:Q]/2+3)(1−σ)`. At σ=4/5 and k=Q(ζ₅), these are 3/2 and 1, respectively, again weaker in X. Theorem 1.2 and §6 study almost-all effective Chebotarev for cyclic extensions, including prime degree, over arbitrary k. Its displayed Chebotarev theorem should not be treated as an explicit off-critical σ=4/5 zero-density bound. The cited preprint also states an auxiliary `c_n Y^(1/(n−1))` field-count asymptotic without discussing cyclotomic base-field logarithms; its use in k containing μ₅ needs a separate source check.

Cho–Kim, [*On the residues and Euler–Kronecker constants of cyclic number fields*](https://doi.org/10.1007/s11139-026-01331-7), §4, derive near-1 almost-all relative-zeta rectangles for cyclic prime-degree extensions of **Q**, ordered by their rational conductor. Their printed character-count exponent from Kowalski–Michel is `(7/2)(1−σ)/(2σ−1)`, with a polynomial height factor; the underlying theorem allows constants strictly greater than 7/2, so retain a small loss when invoking it. At σ=4/5 the displayed exponent is 7/6. This is significant prior work on cyclic quintic relative zeta functions over Q, but its rational base and family do not cover all cyclic quintic extensions of Q(ζ₅).

Corrigan, [Theorem 2.4](https://arxiv.org/html/2310.16518), gives a conductor-ordered density bound for primitive Dirichlet characters of **any fixed order** over Q. For order 5 and σ=4/5 one branch is `(Q⁸T⁵)^(1/9)(QT)^ε`, stronger than the candidate's Q exponent on that rational family. A base change from rational Dirichlet characters supplies only a restricted subfamily of the Hecke characters over Q(ζ₅), and the two conductor scales must not be identified.

The targeted search also inspected recent [rStation paper 52](https://rstation.ai/problems/riemann_hypothesis/papers/52/v5), which is about cubic Hecke characters, and related papers 58 and 65, which concern cubic or sextic sums; none inspected states the proposed full quartic or fifth-order conductor-family estimate. An [rStation discussion](https://rstation.ai/r/riemann_hypothesis/posts/29) calls the n=6 exponent in De Faveri Corollary 1.5 a “conductor exponent”; the primary source orders this sum by index norm. That sentence is not a conductor-ordered theorem without an additional argument. This remains an incomplete targeted search, and provides no priority claim.

Finally, [Liu, Theorem 17.1 and Corollary 19.2](https://arxiv.org/html/2610.26835v1), claims zero-freeness in `Re s>0.874886647…` for every finite-order Hecke character over every number field and for every relative zeta quotient, based on the cited OpenAI theta machinery. If that claimed source and its dependencies hold, a zero count in that narrower half-plane is zero for every individual member, so a nonzero density upper bound there is weaker. At σ=4/5 it gives no such conclusion. The analytic development has not been independently verified in this note.

## Central-value preprints and the scope of their large-sieve inputs

Castillo–de Faveri–Dunn, [arXiv:2604.01316v2](https://arxiv.org/abs/2604.01316v2), Theorem 1.2, use squarefree Gaussian labels `q≡1 mod (1+i)^7` ordered by `Nq≤X`, and prove a positive proportion of nonvanishing **at the central point** for each fixed angular mode ω. Their Corollary 1.8 gives a central second-moment asymptotic for this same squarefree sector. The statement does not cover the full quartic conductor-ordered labels `a b² c³`, nor does it count zeros in `Re s≥4/5`. Their quartic twists of the CM elliptic curve have a different fixed infinity type from the finite-order inducing characters in the Artin comparison. Thus their theorem supplies strong central information on a smaller family, not a direct competitor for the stated off-critical full-family exponents.

Diaconu–Ion–Paşol–Popa, [arXiv:2607.27131v1](https://arxiv.org/abs/2607.27131v1), Theorem F, prove positive-proportion central nonvanishing for the **full r-th-power-free** family, but explicitly order it by the label norm rather than conductor. Their Theorems D and E give central second and first moment formulas; Theorem D's second moment contains the explicit additional label weight `Q_a`. Their standing hypothesis requires the base field to contain μ_{2r}. It applies with r=5 to Q(ζ₅), which contains μ₁₀, but its printed form does not cover r=4 over Q(i), which lacks μ₈. The introduction's comparison to the earlier Gaussian result should not be read as removing that standing hypothesis. These central statements do not give the required off-critical zero-density count.

The same paper offers possible analytic inputs but does not state the conductor-box inverse norm needed by the proposed argument. Proposition 7.2.4 bounds a weighted central second moment with a fixed r-free twist f by `N(rad f)^(1/2+ε)`; it is not a zero detector or arbitrary-length inverse-polynomial estimate. In Appendix A.3.2, write `q=q_sf q_full`, with q_sf squarefree and q_full squarefull, and put `Q₁≈Nq_sf`, `Q₂≈N rad(q_full)`. Equation (47) bounds a centrally normalized character polynomial of length R over that family by

    (Q₁Q₂R)^ε Q₂ [Q₁+R+(Q₁R)^(2/3)].

The proof freezes q_full and applies the Blomer–Goldmakher–Louvel squarefree sieve to q_sf; Q₂ counts its allowable local exponents. In a conductor box `Q₁Q₂≲X`, the term `Q₂R` can be as large as `XR`, so this printed estimate alone does not supply the proposed quartic `X+X^(2/3)R` moment. The multiple-Dirichlet-series functional equations and twisted moment formulas may nevertheless be useful for developing a new joint-exponent estimate; no such transfer or improvement is established here.

At σ=4/5, the source-conditional candidates for full conductor-ordered families are `X^(13/15+ε)` for n=4 and `X^(19/20+ε)` for n=5, each only at a sufficiently small power height. For comparison, Khale et al.'s full finite-order conductor family gives `X T` over Q(i) and `X T²` over Q(ζ₅), up to logarithmic factors; de Faveri's norm-ordered source gives `X^(15/22+ε)T^(9/7+ε)` on squarefree quartic labels and `X^(23/35+ε)T^(11/7+ε)` on squarefree quintic labels, with the full-family conjugate-reordering losses above. These are statements about different scopes and height dependencies, not a claim that the conditional candidates are novel or established.

For induced monomial Artin representations, Artin induction transfers an L-function and its conductor from the Hecke source up to the fixed field discriminant, as in the [monomial note](2026-10-29-monomial-artin-density/README.md). Therefore the above Hecke comparisons also give direct benchmarks for its induced subfamilies. The squarefree quartic central result does not automatically yield a positive proportion within the full conductor-ordered induced family, and a result on a restricted rational Dirichlet or class-group-character family does not automatically cover all its inducing characters. The search has not established an exhaustive priority result or ruled out a stronger specialized monomial theorem.
