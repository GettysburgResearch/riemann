# Quadratic-character counting and simultaneous fixed twists

**Status.** The character count below uses standard class field theory and the stated quadratic FHL construction. The simultaneous density consequence is conditional on the squarefree-family detector and its uniform fixed-twist matching. It is a family result, not an individual zero-free region. General-field simultaneous zero-free rectangles already follow near 1 from the published sources cited below; no priority claim is made.

## Counting quadratic characters

For a fixed number field K, let `X₂(Q)` be the primitive Hecke characters of exact order two with finite conductor norm at most Q. Then

    #X₂(Q) ≍_K Q.                                                (1)

For the upper bound choose S containing all primes over 2 and the archimedean places. Away from S a quadratic local character is either unramified or tamely ramified with conductor exponent one. At each odd-residue-characteristic prime there is only one nontrivial quadratic character of the residue-field unit group. Thus two global quadratic characters with the same good conductor ideal have identical local restrictions to units away from S, and their quotient is unramified outside S. All quadratic Hecke characters unramified outside S form a finite group: local quadratic characters at each dyadic place have bounded conductor because `K_v×/(K_v×)²` is finite, real-place signs have finitely many choices, and the resulting bounded ray class group is finite. There are `O_K(Q)` good integral ideals of norm at most Q, giving `#X₂(Q)≪_K Q`.

For a lower bound take the Goldmakher–Louvel/Fisher–Friedberg quadratic Hecke family on good squarefree ideals a. Its good conductor is exactly a, while the S-supported conductor is uniformly bounded; the latter follows from finite quadratic local types and fixed K,S. Distinct a therefore give distinct primitive characters and conductors `≪_{K,S} Na`. The standard positive-density count for squarefree ideals coprime to S supplies `≫Q` labels with `Na≤cQ`. Remove the possible unit label or principal character. This proves (1), with the family construction treated as the cited input.

More precisely, fix one such family `χ_a`. Every χ∈X₂(Q) satisfies

    χ = ξ χ_a,    Na≤Q,                                         (2)

where a is the good part of its conductor and ξ lies in the finite group of quadratic characters unramified outside S. The identity is between primitive global Hecke characters, not their possibly imprimitive zero-extended ideal representatives; their missing Euler factors need separate bookkeeping in polynomial witnesses.

## A conditional simultaneous consequence

Let `ν₁,...,ν_J` be fixed unitary Hecke characters, with fixed archimedean types, and fix `1/2<σ<1`. Suppose that for every fixed twist from the finite list `ν_j ξ`, the squarefree FHL detector and its common-height/profile replay supply, for every ε>0 and some τ>0,

    Σ_{Na≤Q, a squarefree good} N(σ,Q^τ;(ν_j ξ χ_a)^*)
       ≪ Q^[R(σ)+ε],
    R(σ)=3(1−σ)/(2−σ).                                         (3)

The moments, finite reciprocal phases, original common zero masks and moving-frequency/Sobolev bounds have to be verified for each fixed twist; a finite list permits one common τ by taking the minimum. The count is for primitive inducing functions.

By (2) and a finite union bound, the number of χ∈X₂(Q) for which at least one primitive `L(s,(ν_jχ)^*)` has a zero in `Re s≥σ, |Im s|≤Q^τ` is

    ≪_{K,ν_1,...,ν_J,σ,ε} Q^[R(σ)+ε].                         (4)

If `ν_jχ` is a pure norm character, it has a shifted Dedekind-zeta pole and is omitted from the entire-function detector. For fixed j, there is at most one such quadratic χ: equality of two such presentations forces their ratio to be both finite-order quadratic and a pure norm character, hence trivial. Treat these finitely many cases separately by the standard individual bound `O(Q^τ log Q)` for zeros in the finite height window, after shrinking τ if necessary. For fixed `1/2<σ<1`, `0<R(σ)<1`, so (1), (4) and small ε show a power-saving exceptional proportion. No assertion is made that an arbitrary continuously varying twist family admits a common τ or uniform constants.

## Prior work and scope

[Corrigan–Zhao, Theorem 1.4](https://arxiv.org/pdf/2211.00260), prove the same Q-exponent for all primitive quadratic Dirichlet characters over Q, with explicit T-dependence. A simultaneous union follows directly when each fixed background is quadratic or trivial, since each twist remains quadratic with conductor O(Q). The printed theorem counts quadratic Dirichlet characters and does not by itself cover a fixed nonquadratic or infinite-type background.

For general number fields, [Lemke Oliver–Wang–Wood, Theorem 4.2 and Lemma 4.3](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/average-size-of-3torsion-in-class-groups-of-2extensions/6AABE169B5BA8192FE036455DE4F806F), use the Lemke Oliver–Thorner general ray-class density theorem to obtain a bound `(D_K Q T)^[c_d(1−σ)+ε]` over **all** primitive ray class characters of conductor at most Q, with c_d depending on the degree. Their Lemma 4.3 already applies it to almost all quadratic extensions, with polynomial height `Q^{1/2}` and σ sufficiently close to 1. A finite collection of fixed finite-order twists is handled by the same broad bound: twist conductor is `≪_ν Q` and each fixed twist map on characters is injective. Thus this published source supplies simultaneous rectangles near 1, although its displayed constant c_d is unspecified and does not permit an unconditional numerical superiority comparison with (3). It does not cover arbitrary infinite-type ν in the displayed ray-class statement. This comparison is nonexhaustive.
