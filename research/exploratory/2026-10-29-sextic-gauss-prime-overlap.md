# Sextic Gauss sums over primes and the exceptional source vector

**Scope.** The desired input is a fixed-ray-sector smooth prime estimate of size Y^(11/12+ε) for the normalized sextic Gauss coefficient of the source vector in [the Gauss-profile note](2026-10-29-gauss-profile-low-rank/README.md). Such an estimate controls the overlap with that one profile direction; it does not prove that the full operator has only one exceptional direction or bound its complement. The discussion below isolates a promising cubic reduction and a missing simultaneous angular/ray estimate. No zero-free region follows here.

## Exact primewise reduction

Let O=Z[ω], λ=1+2ω, α(π)=π/|π|, with π a primary good prime. For j=−1,1,2,3 let γ_j(π) be the normalized Gauss sum of the j-th power of the sextic residue symbol, using additive kernel e(Tr(z/λ)). In the notation of the [October 5 quasi-RH draft](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex), its arithmetic lemma and μ(π)=−1 imply

    γ_{−1}(π) = −χ_π(−1) G_ray(π)^(−1) overline(α(π)) γ₂(π),
    G_ray(π) = overline(χ_π(4)) γ₃(π).

The factors χ_π(−1) and G_ray(π) are fixed finite-ray-class functions. G_ray need not be a character as the prime varies, but it is constant on each fixed ray class. The conjugate orientation follows by conjugating the identity, with the angular exponent reversed.

The [September 25 first-moment draft](https://github.com/openai/math/blob/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf), (1.1), uses instead the cubic Gauss sum

    G_cub(π) = (Nπ)^(−1/2) Σ_(x mod π) χ_π(x)^2 e(Tr(x/π)).

The substitution x=λy gives exactly γ₂(π)=χ_π(λ)^2 G_cub(π). The supplementary phase χ_π(λ)^2 also factors through a fixed finite ray group. After enlarging the fixed ray modulus to include the relevant factors, the requested sextic sum is a constant multiple, in each sector, of

    Σ_(π primary prime, [π]=C) W(Nπ/Y) overline(α(π)) G_cub(π),

with possibly a fixed finite-ray multiplier. Sector restrictions can be expanded as finitely many ray-character twists. The additive-convention phase must be retained before making this reduction. The paper versions use different definitions of G_ray; the displayed identity uses the October 5 definition above.

## Source statements and exact limitation

1. Heath-Brown, [*Kummer's conjecture for cubic Gauss sums*](https://ora.ox.ac.uk/objects/uuid:16c3966e-61cb-499d-839c-559b3794fcff), 2000, proves for each integer ℓ and ε>0 the unrestricted primary-element von-Mangoldt sum

       Σ_(Nc≤X, c≡1 mod 3) G_cub(c) Λ(c) α(c)^ℓ
          ≪_ε X^(5/6+ε)+|ℓ| X^(3/4+ε).

   Thus ℓ=−1 supplies a 1/6 saving in that unweighted ray sector. The theorem as stated does not impose the additional congruence class needed by the sextic vector. The source's prime-power convention and finite good-prime deletions should be matched before transfer; removal of finitely many primes is harmless.

2. David and Güloğlu, [*One-level density and non-vanishing for cubic L-functions over the Eisenstein field*](https://arxiv.org/abs/2102.02469), Theorem 4.4, establishes an unconditional twisted cubic prime estimate with a finite-modulus character η and primary r:

       H(Z,r,η) ≪_ε Z^ε [Z^(2/3) N(r)^(1/6+ε)
                         + Z^(1/2) N(r)^(1/4+ε)
                         + Z^(5/6) N(r)^(1/12+ε)
                         + Z^(4/5) N(r)^(1/10+ε)].

   H is the prime sum weighted by log Nπ and normalized g(r,π), with (π,r)=1; constants depend on the modulus of η. For fixed r this is Z^(5/6+ε). Its printed statement includes finite characters, not the required nonzero angular exponent. Section 5 explicitly adapts Heath-Brown's proof to such finite characters, so replaying their adaptation alongside Heath-Brown's angular version is a concrete research route, not an already-stated joint theorem. This Theorem 4.4 is unconditional even though the paper's one-level-density application assumes GRH.

3. The September 25 OpenAI preprint above, Theorem A.1, **claims** for each fixed nonzero integer ℓ that

       Σ_(Nπ≤X, π primary prime) α(π)^ℓ G_cub(π)
           = o_ℓ(X^(5/6)/log X).

   This has no asserted uniformity as ℓ grows and no arbitrary finite-ray restriction or finite-ray twist in its theorem statement. The preprint and its imported dependencies have not been independently verified here. For fixed W∈C_c^1((0,∞)), Abel summation yields the same little-o estimate for Σ W(Nπ/Y)α(π)^ℓ G_cub(π). That conclusion remains unrestricted over the primary prime sectors; cancellation of their total does not prove cancellation within each sector.

4. Dunn and Radziwiłł, [*Bias in cubic Gauss sums: Patterson's conjecture*](https://annals.math.princeton.edu/2024/200-3/p03), prove a smoothed cubic first-moment asymptotic under GRH for Hecke L-functions over Q(ω), with an X^(5/6)/log X bias in their stated rational-prime normalization. Their unconditional level-aspect Voronoi formula is an input to later methods, but the conditional asymptotic in the abstract does not itself state the fixed angular, arbitrary fixed-ray-sector estimate above.

An assertion that combines the unrestricted angular theorem with a separate finite-ray theorem requires a new joint proof. In particular, fixing the Gauss phase in a ray class makes it constant **inside** that class; it does not permit applying the unrestricted angular prime sum separately to that class.

The specific missing source interface is visible in David–Güloğlu §§5–6. Their (27) is the finite-character-twisted Kubota series ψ(r,η,s)=Σ_{b primary}η(b)g(r,b)N(b)^(−s). Lemma 6.5 supplies its meromorphic continuation, convexity and residue bound (the stated pole at s=4/3 can occur only if η³ is principal); Lemma 6.6 supplies the mean square ∫_{−T}^T|ψ(r,η,1+ε+it)|²dt≪T²N(r)^(1/2), with constants depending on the finite modulus. These feed their Proposition 6.2 and then their Type-I estimate. A source-level proof for ηΘ_{−1} needs counterparts of both lemmas at finite ray level **and** fixed nonzero archimedean type, including the correct residual spectrum, conductor and gamma factors. Although (ηΘ_{−1})³ is nonprincipal, Lemma 6.5 as printed does not itself certify the pole condition for this infinity type. The multiplicative phase can be absorbed in the Type-II coefficient sequences, but that observation alone does not supply the Type-I analytic input. A targeted search did not locate the joint theorem in a primary source.
