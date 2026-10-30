# A fixed-profile Möbius/Gauss overlap

**Status:** Source-qualified deduction from OpenAI's [quasi-RH draft, Lemma 4.4 and Proposition 5.1](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf). It applies to an ordinary smooth squarefree Möbius coefficient vector, not its prime-only restriction or a moving row-dependent mask. The cited completed reflection and its standard analytic inputs are not independently proved here. It gives no selected operator or zero-free theorem by itself.

Let S contain the fixed primes above 6 and all fixed finite twist conductors. Use the source's primary Eisenstein convention. Fix smooth annular W,V and a fixed S-supported finite-ray character ν. For squarefree good s of norm ≍P define

    m_s=P^(−1/2) μ(s)ν(s)W(Ns/P)(Ns/P)^(−ih),
    g_s=P^(−1/2) γ₁(s)V(Ns/P)(Ns/P)^(−1/2) · ζ(s),

where ζ is any fixed bounded function of the source's finite ray class, accounting for a chosen class and fixed phases. Here γ₁ is the **normalized sextic** Gauss sum in source §4.2, and h is real. The norms of these two coefficient vectors are O(1). For every η>0,

    |⟨m,g⟩| ≪_{S,ν,W,V,ζ,η} P^(−1/2+η)(1+|h|)^A,              (1)

for a fixed height order A. The scalar product convention may conjugate the whole expression; either orientation has the same bound. For h≤P^τ, choose τ after A and η to absorb its cost into a prescribed small power.

## Proof

For squarefree s, source (4.7) gives

    γ₁(s)γ₂(s)=μ(s)α(s)G_finite(s),    |γ₁(s)|=|G_finite(s)|=1.

Consequently

    μ(s) overline(γ₁(s)) = overline(α(s)) overline(G_finite(s)) γ₂(s). (2)

The conjugate on the finite function G is essential. Lemma 4.4 states that G_finite depends only on a fixed S-supported ray class. Expand `ν(s) overline(ζ(s)) overline(G_finite(s))` in the finite character basis of a common S-supported ray group. It is enough to bound each sum

    Σ_(s sf, good) γ₂(s) overline(α(s)) Ψ(s)
          U(Ns/P)(Ns/P)^(−ih),                                     (3)

for a fixed finite-ray Ψ and fixed smooth annular U, with the exact zero masks from the source.

Proposition 5.1 defines the Dirichlet series D(z,Ψ) of these coefficients and asserts that

    T(z,Ψ)=L₀(z,Ψ) D(z,Ψ)

has an entire continuation and polynomial growth on each fixed vertical strip, for each fixed arithmetic choice. Here

    L₀(z,Ψ)=L_K^S(3z−1/2, overline(α)^3 Ψ^3).

For `Re z>1/2`, the L-argument has real part >1. Its Euler product and reciprocal converge absolutely, so both L₀ and 1/L₀ are bounded on every `Re z≥1/2+η`. Thus D continues holomorphically to that half-plane with fixed polynomial vertical growth. Mellin inversion of U shifts from `Re z>1` to `Re z=1/2+η`; its transform decays rapidly, yielding (3) `≪P^(1/2+η)(1+|h|)^A`. Divide by P from the two coefficient normalizations to obtain (1). □

For fixed independent Gauss profiles U₁,…,U_k, their coefficient Gram matrix has a uniformly bounded inverse as explained in the [profile-space note](README.md). Applying (1) to each basis vector therefore gives

    ||Proj_(V_P)m||₂² ≪ P^(−1+η)(1+|h|)^A.                       (4)

At balanced row/source scales P=Y, the source sextic upper bound gives `||T_Y||²≪Y^(7/6+η)`, so the contribution of this finite-dimensional projection is at most `Y^(1/6+η)` after height losses. This is well below Y. More generally for P≤Y with `P≥Y^(1/2)`, the source upper scale is `Y^(5/6)P^(1/3)`, giving projected contribution `≪Y^(5/6)P^(−2/3+η)`. These are bounds on the **projection onto the chosen fixed profile space**; they do not control `T_Y(1−Proj_(V_P))m`, and cancellation between those two components cannot be discarded to infer a full bound. The row restriction may be any subset after the full-row upper estimate, provided the same fixed profile vectors are used.

## Prime-only and fixed-ray caveats

The argument above uses all squarefree source indices. It cannot be transferred to `m_s` restricted to prime s merely by removing Euler factors: the normalized cubic Gauss coefficients are not multiplicative in the ordinary sense. The September-25 [first-moment draft, Theorem A.1](https://github.com/openai/math/blob/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf), states `o(P^(5/6)/log P)` for all primary primes with a fixed nonzero angular twist. The quasi-RH identities and its additive-character comparison convert the prime overlap to that cubic sum times a **fixed finite-ray factor**, but that theorem does not state the needed fixed-ray-twisted version. A cancellation estimate for the unweighted union of classes does not imply one for each class. Even a prime-specific overlap saving would address only the finite-profile component: a hypothetical `Y^(13/12+ε)` full-space complement would still exceed the desired Y scale by `Y^(1/12)`.

## Fixed Gauss twists and fixed punctures

The same argument permits replacing g_s by `g_s χ_s(h)` for any **fixed** nonzero primary h with good prime factors, retaining the zero when (s,h)≠1. Source sextic reciprocity gives, including these zeros,

    overline(χ_s(h)) = R(s,h) overline(χ_h(s)),

where R(s,h) is a bounded function of the fixed ray class. Factor h into good primes. The right side is a fixed finite product of powers of `χ_p(s)` times a fixed ray function, with the source's convention that even the zeroth power keeps the local zero mask. Proposition 5.1 explicitly permits such a finite prime set and exponents in {0,…,5}. Multiplying the source vector by a fixed unit or S-supported local part contributes only another fixed finite ray function on good s. Therefore (1) holds for each fixed h and each fixed puncture set, with implied constants and height order allowed to depend on them. A fixed finite collection of such h can be handled simultaneously by taking maxima of the constants.

This does **not** make (1) uniform for a family h=h(P) whose norm or support grows with P: Proposition 5.1's entire continuation and polynomial-growth statement allows its constants to depend on the moving prime set and exponents. The explicit local and conductor factors have since been audited in [the moving-twist note](moving-twist-overlap.md), which proves a polynomial-conductor overlap and conditioning for a restricted growing family, conditional on the reflection. It does not cover arbitrary physical-row masks.

**Independent review:** A second researcher checked the additive-character normalization, conjugations in (2), fixed-ray expansion, absolute convergence and reciprocal bound for L₀, Mellin-height dependence, finite-profile conditioning and the P≤Y source-scale calculation. The review remains conditional on the cited completed-reflection assertion; it does not establish uniformity in moving h or a full-space spectral decomposition.
