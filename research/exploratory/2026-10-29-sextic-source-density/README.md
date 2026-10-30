# Sextic natural-label density from existing source moments

**Status.** This is a direct consequence of existing preprint moment and detector assertions, not a claim of an independent new source-level bound. The cited preprints' full analytic proofs have not been independently verified here; the source-to-FHL conventions below are retained as inputs. No individual zero-free boundary or exhaustive priority claim is made.

Fix either `K=Q(ω)` or `K=Q(ζ₁₂)` and a sufficiently large fixed admissible bad set S. Let χ_u be the good sextic FHL family, indexed by sixth-power-free good ideals `Nu≤X`. For fixed `1/2<σ<11/12`, put `δ=2σ−1` and

    R(σ)=(15−16δ)/(15−6δ).                                      (1)

Under the source identifications stated below, for every ε>0 there is τ>0 such that

    Σ_{u good, sixth-free; Nu≤X} N(σ,X^τ;χ_u)
       ≪_{K,S,σ,ε} X^(R(σ)+ε).                                 (2)

The zeros of the primitive inducing functions are counted with multiplicity. Fixed principal presentations are handled separately. The implied height power is chosen after all fixed ε and detector losses and is not asserted uniform as σ approaches an endpoint. At σ=4/5, `R=9/19`; at `θ=4369347/5000000`, `R=3795224/13141959≈0.288787`. This is a natural-index bound, not a conductor-ordered bound or an individual zero-free theorem.

## Source inputs and detector

On each shell `U≤Nu≤2U`, the normalized inverse polynomial M_r of length `U^r` obeys

    Σ_u |M_r(u)|² ≪ U^[max{1,(1+5r)/6}+ε](1+H)^A.             (3)

The normalized ordinary polynomial S_m of length `U^m` obeys, on nonprincipal inducing rows and `m≤1/2+small fixed loss`,

    Σ_u |S_m(u)|⁴ ≪ U^(1+ε)(1+H)^A.                            (4)

For `K=Q(ω)`, (3) is OpenAI [Lemma 17.6](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), and (4) is its Lemma 18.1 with no prime slots. For `K=Q(ζ₁₂)`, they are [Liu Lemma 10.6 and Remark 12.16](https://arxiv.org/abs/2610.26835v1), respectively. The Liu z=0 ordinary clause does not require the extra κ-dependent zero-free hypothesis for marked factors. These source statements permit the needed fixed finite twists, norm-frequency heights and profile seminorms; the row restriction is sixth-free for the inverse and nonprincipal for the ordinary moment.

The fixed-field buffered detector, applied to a nonprincipal presentation and its conjugate with conductor and deleted radical `≪U`, gives one common zero and simultaneous witnesses `r≤t`, `m≤1/2`, `r+m≥t`, up to arbitrarily small fixed losses, with squared thresholds `U^(δr)` and `U^(δm)`. Its common-profile and Sobolev treatment is detailed in [the uniform detector proof](../2026-10-29-direct-nfree-density/UNIFORM-DETECTOR-PROOF.md). The χ and conjugate cases are separated and the latter's coefficient vector conjugated, without changing row norms. The row-varying real and imaginary parameters are handled before applying (3)–(4); the finite Sobolev order, polynomial height loss and individual zero-count cost are absorbed after choosing τ small.

## Scalar deduction and height

Set

    t=5/(5−2δ),       L=2t/3.                                    (5)

For `0<δ<5/6`, `1<t<3/2` and `2/3<L<1`. By the inverse witness and (3), the row-count exponent is

    f(r) = 1−δr                    (r≤1),
           1/6+(5/6−δ)r            (r≥1);                       (6)

by the plain witness and (4), it is `g(m)=1−2δm`. If r≥L, f is at most its common endpoint value at L and t, namely R. If r<L, the simultaneous constraint gives `m>t/3` and hence `g(m)≤1−2δt/3=R`. This proves the shell estimate at a sufficiently small U-power height. The case r=1, fixed dyadic endpoints, and small detector losses are absorbed by ε.

For the global X-power height in (2), choose fixed η>0 sufficiently small relative to R and ε. The labels `Nu≤X^η` cost at most `X^(η+τ+ε)` by ordinary ideal counting and the individual zero count. For each larger dyad U, choose τ less than η times its admissible U-height exponent and absorb all polynomial height factors into `X^ε`. Summing O(log X) dyads proves (2).

## Family matching and comparison

The presentations in the two moment sources are sextic symbols `ν(n)χ_n(u)` with natural zero extensions and fixed finite S-supported ν. For each good sixth-free FHL label, choose one allowed source generator. The ratio of its Kummer presentation to the frozen FHL one represents a class in the finite group `K(S,6)`; partition rows by this fixed finite class and use the corresponding ν. The original presentations agree on all good ideals including their noncoprime zero masks. Equality at good primes dividing an auxiliary ideal of a frozen FHL decomposition is interpreted through its primitive Kummer Artin character, not by naively evaluating a zero-extended raw symbol there; see [the finite-phase comparison](../2026-10-29-general-field-collapsed-sieve/README.md). Nonprincipal filtering is preserved. The exact allowed-generator and finite-ray convention is a source-matching assumption, not a conclusion from conductor size alone.

Good squarefree FHL labels yield ≫X distinct primitive characters, since their good local conductor supports distinguish them. Thus (2) is a density-one statement for this natural-label family. For `1/3<δ<5/6`, de Faveri Corollary 1.5's middle branch has exponent D₆ and

    D₆−R = −δ(252δ²−312δ+55)
              /[6(2δ−5)(18δ²−30δ+5)] > 0.                     (7)

The numerator quadratic is convex and negative at both endpoints; the two denominator factors are negative throughout the interval. For fixed σ the strict fixed-height gap persists at sufficiently small polynomial heights. At σ=4/5 the source exponent is `209/326`, versus `9/19`. This compares named bounds; it does not assert priority over other results. OpenAI Proposition 19.2/Remark 19.3 and Liu Proposition 2.7 already contain the relevant source counting ingredients, so the calculation should be viewed as making a source consequence explicit.

**Independent review.** High_match checked Liu's precise shell and twist hypotheses, the zero-slot fourth moment, the balance and both displayed numerical exponents, and the shell/global-height passage. The source results and presentation bridge remain as identified inputs.
