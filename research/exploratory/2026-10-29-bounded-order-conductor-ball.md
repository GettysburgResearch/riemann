# Bounded-order characters in a growing conductor ball

**Status.** The character-counting input is classical. The numerical simultaneous zero-density applications below are conditional on the cited moving-common-twist detector, its source inputs and a common height power. They are family statements, not individual zero-free regions; the source comparison is not exhaustive.

## Classical conductor count

For a fixed number field K and integer m≥1, the number of finite-order Hecke characters ν satisfying `ν^m=1` and `Nf_ν≤Q` is

    ≪_{K,m,ε} Q^(1+ε).                                          (1)

One direct proof uses the narrow ray class exact sequence. At p∤m, an m-torsion local character of the unit group factors through the cyclic residue group and has at most m choices; its conductor exponent is 0 or 1. At the finitely many p|m, the local quotient `K_p×/(K_p×)^m` is finite, so there are finitely many local possibilities and uniformly bounded conductor exponents. Real-place signs and fixed class-group m-torsion contribute a bounded factor. Hence a given good conductor support a has at most `O_{K,m}(m^{ω(a)})` global choices, and summing over ideals `Na≤Q` gives (1).

More precise results precede (1). [Melanie Matchett Wood, *On the probabilities of local behaviors in abelian field extensions*, Theorem 3.1](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/62671044291FFD9492C72D1DE76007DB/S0010437X0900431Xa.pdf/on-the-probabilities-of-local-behaviors-in-abelian-field-extensions.pdf), counts G-extensions of an arbitrary number field by conductor for fixed finite abelian G. For `G=C_d`, an exact-order-d character corresponds to a cyclic degree-d extension together with one of φ(d) faithful identifications of its character group, and its conductor agrees locally with the conductor of that cyclic extension. The theorem's conductor specialization has main growth `Q(log Q)^{w−1}`, with

    w=Σ_{e|d,e>1} φ(e)/[K(ζ_e):K].                              (2)

For each d|m there are only finitely many such families. This is a conductor-ordered theorem, not Wright's distinct discriminant-ordered theorem. Equation (1) follows from the stronger source asymptotic; no novelty is claimed for it. For m=1 there is just the principal character.

## Conditional simultaneous bounds

Let ν vary over (1) with `Q=X^κ`, and let χ_u range over the specified n-free FHL natural labels `Nu≤X`. Suppose the [moving-common-twist estimate](2026-10-29-moving-unitary-twist-density/README.md) holds uniformly for one such ν, including the original local masks and one common height exponent, with row exponent `E(κ)<1`. Then union over ν gives at most

    O(X^[E(κ)+κ+ε])                                             (3)

exceptional labels at some common height `X^τ`. All background infinity types are among a finite set because ν has finite order. Possible pure-norm products require the detector's separate treatment; at most one label occurs per ν, and its individual zero count is absorbed after shrinking τ. Formula (3) improves the generic O(Q²) all-finite-order-character union, but is a straightforward consequence of the known count and the assumed density bound.

At cubic order n=3, K=Q(ζ₁₂), `σ=4369347/5000000`, and κ=1/20, the per-background exponent is

    R=6306530/11891959≈0.5303188482;
    R+κ=138022559/237839180≈0.5803188482.                        (4)

At quartic order n=4, `σ=4/5`, and κ=1/10, it is

    R=35/52,      R+κ=201/260≈0.7730769231.                     (5)

These count exceptional natural labels; the field applications require their own Artin-factorization and field-fibre arguments. The analytic inputs, including uniformity when the common background conductor grows, remain unverified here.

## Published broad Hecke comparison

For fixed Galois K, [Khale–O’Kuhn–Panidapu–Sun–Zhang, Lemma 3.3](https://arxiv.org/pdf/2008.09677v3), bounds zeros over **all primitive finite-order Hecke characters** of conductor ≤R, with factor `(R²T^[K:Q])^[min{3/(2−σ),2/σ}(1−σ)]` and logarithmic loss. Its fixed-height conductor exponent is

    B(σ)=2 min{3/(2−σ),2/σ}(1−σ).                              (6)

For every product `ψ=νχ_u`, `Nf_ψ≪X^(1+κ)`. If gcd(m,n)=1, ψ determines ν via an integer inverse of n modulo m applied to `ψ^n=ν^n`, and then χ_u and u through the good local exponents. Summing the broad conductor family therefore bounds **all** such pairs, and hence exceptional labels, with exponent `(1+κ)B(σ)+ε`, after selecting τ small enough to absorb the T factor. At the cubic point, this is `4414571/7282245≈0.60621017`, and at the quartic point it is `11/10=1.1`; both are weaker than (4)–(5).

When gcd(m,n)>1, recovering ν from `ψ^n` is not generally unique; nevertheless the conductor-fibre argument in [the cubic prior-art note](2026-10-29-cubic-cyclotomic-moving-prior-art.md) extends to fixed n. Group possible pairs by `f_ν`: outside f_ν, ψ's local inertia determines each good exponent of u; on primes dividing f_ν there are at most n choices. Thus the number of pairs above ψ is at most `Σ_(Nf≤X^κ)n^{ω(f)}≪X^(κ+ε)`, giving a broad comparator exponent `κ+(1+κ)B(σ)`. It equals approximately 0.65621017 in the cubic example and 1.2 in the quartic example. This is an elementary derived comparison, not a verbatim theorem from Khale et al. Principal products, finite bad factors, and the distinction between primitive and zero-extended presentations must be handled separately as in the cited detector; all height factors must be retained before choosing τ. Other specialized results could be stronger: the search is not exhaustive.
