# Cubic density over Q(ζ₁₂) and conductor-ball comparators

**Status.** Source comparison and an elementary conductor-ball deduction; analytic preprints and the proposed moving detector are not independently established here. This search is nonexhaustive. Set `K=Q(ζ₁₂)` and `θ=4369347/5000000`. Natural labels mean the cube-free FHL ideal labels, not character conductors.

The proposed direct all-cube-free-label exponent at θ is

    R₃(θ)=6306530/11891959=0.5303188482… .                       (1)

[De Faveri, Corollary 1.5](https://arxiv.org/html/2610.04045v1#S1.Thmtheorem5), applies to fixed number fields containing μ₃ and full cube-free natural labels. Its upper branch has exponent `2741281467955/5056830380773=0.5420948028…`, with explicit `T^[1+2(1−θ)/(3−2θ)+ε]`; a strict comparison with (1) at power height requires choosing τ sufficiently small. [Khale–O’Kuhn–Panidapu–Sun–Zhang, Lemma 3.3](https://arxiv.org/pdf/2008.09677v3), applies to the full finite-order conductor family over fixed Galois K and gives at fixed height

    B(θ)=4(1−θ)/θ=2522612/4369347=0.5773430217… .             (2)

Its height factor is explicit: `(R² T^[K:Q])^[2(1−θ)/θ]` times logarithms. Thus its all-character result has a weaker base exponent than (1), but importantly can compare *simultaneous* growing backgrounds, as below. Inclusion of original labels requires fixed bounded bad-prime factors and the good-prime injection.

[rStation paper 52 v5, Theorem 1](https://rstation.ai/problems/riemann_hypothesis/papers/52/v5), claims the stronger cube-free fixed-twist exponent `1891959/4564490≈0.4144951572` over the **Eisenstein field Q(ω)**, at sufficiently small polynomial heights, and Theorem 5.7 claims the all-natural-label principal-twist exponent `9414571/16891959≈0.5573403890`. Its prescribed cubic characters and ordinary moments are not a theorem over K=Q(ζ₁₂); extending a field-specific Poisson/Gauss proof, or its constants uniformly to growing backgrounds, is an additional proof task. Likewise [rStation paper 55](https://rstation.ai/problems/riemann_hypothesis/papers/55) claims an ordinary fourth moment over the Eisenstein field, not the full K-family sixth or eighth moment or a growing-ray estimate. This targeted search found no printed full-cube-free K=Q(ζ₁₂) density exponent smaller than (1), and no matching cubic sixth/eighth moment with the required moving common twists; this is not a priority assertion. The above recent preprint results remain unverified here.

## Published all-character source beats the quadratic-background ball

Consider all good cube-free u with `Nu≤X` and every finite-order quadratic or trivial ν of conductor norm at most `X^κ`. Let ψ be the primitive global product `νχ_u`. Pointwise as Hecke characters,

    ψ³=ν,    χ_u=ψ/ν.                                            (3)

The first identity uses ν²=1 and χ_u³=1, so ψ determines ν and χ_u. At each good prime the cubic local exponents 1 and 2 are distinct; hence χ_u determines u. Thus each orientation yields an injection from such pairs `(u,ν)` to primitive ψ. Their conductor is `≪_K X^(1+κ)`; apply (2) to the whole ambient family, including all zeros. For fixed θ and any ε>0 a small enough common τ>0 gives the exceptional-label bound

    O(X^[(1+κ)B(θ)+ε]).                                         (4)

Summing the two cubic orientations costs only 2; principal ψ have no zero counted as a nonprincipal Hecke factor and may be handled separately. The effective T power in the cited source must be absorbed into ε by choosing τ afterward. This deduction requires only FHL local-character and conductor facts, the published Khale bound, and standard character multiplication; no moving cubic detector or field-specific cubic moment is used.

For κ=1/5, (4) has exponent

    5045224/7282245 = 0.6928116261… ,

which is strictly smaller than the source-qualified moving-detector simultaneous quadratic-ball value `34618079/46959795=0.7371854796…` in [the relative-fields note](2026-10-29-growing-ray-relative-cubics.md). In particular it supplies a stronger directly comparable published-input exception bound for the elementary-2-extension conductor ball at θ, after the same Artin-factorization and field-count steps. No individual zero-free theorem follows.

## A possible general-background improvement

For general finite-order ν of conductor norm ≤U and a fixed primitive product ψ, group possible pairs `(ν,u)` by the exact conductor ideal f of ν. At every good prime p not dividing f, ν is unramified, so the restriction of ψ to local inertia uniquely determines the exponent `v_p(u)∈{0,1,2}`. At each good prime p dividing f, there are at most three choices for this exponent. The good support is finite, and the entire exponent vector determines u. Once u is fixed, ν=ψ/χ_u is uniquely determined globally. Hence for a fixed f there are at most `3^{ω(f)}` possible pairs, including all cancellations and without assuming local independence. Summing over `Nf≤U` gives `O_{K,ε}(U^{1+ε})` by standard divisor and ideal-counting estimates. Fixed bad primes do not divide u and need no additional choices. The same argument works for each cubic orientation.

Consequently, subject to the cited source and its FHL local-character input, the same broad density source yields

    O(X^[κ+(1+κ)B(θ)+ε])                                        (5)

for arbitrary simultaneous finite-order ν of conductor at most `X^κ`. At κ=1/10 this is `32118079/43693470=0.7350773239…`, slightly smaller than `0.7371854796…`; at κ=1/20 it is `0.6562101728…`, weaker than the moving detector's `0.63032…`. The conductor bound, fixed small height loss, finite local factors and both orientations remain necessary. For a principal product ψ, the same fibre count contributes at most `X^{κ+τ+ε}` via the standard zero count of the fixed Dedekind zeta function; choose τ small enough to absorb it. Formula (5) is a derived consequence, not a verbatim theorem from the cited source.

[Lemke Oliver–Wang–Wood, Theorem 4.2 and Lemma 4.3](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/average-size-of-3torsion-in-class-groups-of-2extensions/6AABE169B5BA8192FE036455DE4F806F), already deduce zero-free rectangles for most quadratic extensions over arbitrary fixed fields from an all-ray-class zero-density theorem. Their general exponent is an unspecified `c_[K:Q](1−σ)`, so numerical dominance near θ cannot be inferred. Prior simultaneous family statements and the specific conductor-ball deduced above should not be presented as a new individual region.

## One common background of large conductor

For a single finite-order ν per X with `Nf_ν≤X^κ`, the map `u↦νχ_u` is injective under the FHL good-inertia hypothesis, and its primitive product conductor is `≪X^(1+κ)`. Thus (2), without any conductor-ball union, gives the source-comparison exponent `(1+κ)B(θ)` (with a sufficiently small polynomial T loss). At κ=1 this is `5045224/4369347≈1.1546860`, whereas the proposed common-twist fourth-moment/detector exponent is `3783918/6891959≈0.5490337`. At κ=3 it is `10090448/4369347≈2.3093721`, whereas the proposed ordinary-second-moment/detector exponent is `2522612/4391959≈0.5743706`. The broad source is weaker than even the O(X) label count in these instances. Its m=0 specialization covers finite-order backgrounds; a general compact archimedean background requires a separate match to the source’s archimedean basis and common norm shift.

De Faveri's printed Corollary 1.5 is a theorem for the fixed FHL family; its 0.54209 at θ is not literally uniform over a common background whose conductor grows as X or X³. His Theorem 1.1 does permit multiplying a shared coefficient vector by the common ν, but transferring that fact through a zero detector with the conductor `X^(1+κ)`, local cancellation, and one common height is an additional argument. The proposed exponents remain contingent on that proof and source. Recent Eisenstein-only sixth/fourth-moment and paper52 density claims cannot be cited directly as a common-background theorem over Q(ζ₁₂). No stronger directly matching printed result was located by this targeted search; that is not an exhaustive priority determination.
