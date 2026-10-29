# A short detector for conductor-ordered cubic density

**Status:** Proposed source-conditional density results, not an individual zero-free theorem. It uses the global inverse moment and fixed-field detector transfer in the [cubic conductor detector note](../2026-10-29-cubic-conductor-detector/README.md), and a replay below of [OpenAI Proposition 8.3](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) at shorter inverse cutoff than the interval printed in that proposition. The source analytic inputs and their fixed-field and fixed-unitary-type transfer remain assumptions pending independent verification. No priority claim is made.

Fix K containing μ₃, the good-prime set S in de Faveri's cubic family, and a unitary Hecke character ν of fixed infinite type and finite conductor supported on S. For good cube-free ideal labels g let χ_g be the cubic character, retaining its original zero extension at primes dividing g. Assume the fixed-field buffered detector, original-versus-primitive conductor and deleted-factor estimates, and common-coefficient differentiated-profile estimates stated in the linked note, including the short-cutoff extension proved conditionally below and the [fixed-floor extension](../2026-10-29-detector-floor-extension/README.md) from 51/100 to any fixed value strictly between 1/2 and σ. Then the basic inverse-only argument gives, for each fixed `1/2 < σ < 1` and ε>0, a τ>0 such that

    Σ_{g good cube-free, N cond(νχ_g)≤X} N(σ,X^τ;νχ_g)
      ≪_{K,S,ν,σ,ε} X^{1−(2σ−1)²/2+ε}.                            (1)

The zero count includes multiplicity and uses the primitive inducing L-function. Principal or pure norm-character presentations are separated, as in the linked note. The exponent is strictly less than one, so the ≫X/log X distinct characters supplied by good prime labels give density-one zero-free rectangles. This conclusion does not give a uniform zero-free region for each character. The printed source fixes the bin floor at 51/100; extending below it uses the linked floor replay, whose constants may depend on the fixed gap from 1/2.

Examples, with sufficiently small power heights and arbitrarily small fixed exponent losses:

    σ             4/5      5/6      17/20     7/8
    exponent      41/50    7/9      151/200   23/32.

At 4/5, the previous t=1 inverse-only result in the linked note gives 9/10; the general primitive-Hecke-family comparator quoted there gives exponent 1 at fixed height in its fixed Galois-field setting. At 17/20 the cited rStation paper 52 v5 reordering gives 45/58, while the general-family comparator gives the stronger 12/17. These comparisons concern the displayed consequences and do not assert priority or preclude sharper conductor-specific theorems. All height exponents must be chosen sufficiently small for the comparison.

For the standard principal-twist Eisenstein cubic-residue family, [rStation paper 52 v5, Theorem 5.7](https://rstation.ai/problems/riemann_hypothesis/papers/52) also claims a cumulative natural-index bound for every fixed `1/2<σ<1`, with exponent `D(σ)=(8−7σ)/(3(2−σ))` at height `P^h` for some small h. Choosing the smaller conjugate label for each conductor-ordered cubic character and applying that cumulative theorem at P=X^{3/2} yields exponent `(3/2)D(σ)=(8−7σ)/(2(2−σ))`, including the small labels automatically; take τ≤3h/2. At `σ=4/5` this gives exponent 1, versus `41/50` in (1) and `11/14` in the stronger conditional estimate (4) below. Theorem 5.7 counts primitive inducing zeros with multiplicity, including repeated natural presentations and principal rows. Its principal-twist hypothesis is narrower than this note's fixed unitary twist, and the source claim has not been independently verified here. The paper's separate Theorem 1 is dyadic; a single global-height transfer from that theorem uses the small-index split in [the review](../2026-10-29-cubic-conductor-density-review.md).

## Short-cutoff detector and optimization

Let δ₀=2σ−1 and t=(1+δ₀)/2=σ. Put U=X, D*=U^t and retain the bin conventions, rowwise original character and masks of the linked note. The required extension of Proposition 8.3 is: for every zero counted in (1), a finite-bin and logarithmic-dyad choice supplies a zero ρ in bin a≥σ−e and a normalized inverse block M_r with

    t−1/2−O(η) ≤ r ≤ t+O(1/log U),
    |M_r|² ≫ U^{(2a−1)r−η}.                                        (2)

Here e and η are arbitrarily small fixed preliminary losses. The pointwise constants may depend on these losses and σ; the permissible polynomial height exponent τ is chosen later. As in the source, profile choices and frequencies are row-dependent and require the common Sobolev step before the moment is applied.

The source's displayed range is 1≤t≤3/2, so (2) at t<1 is not being attributed to its formal statement. The following is the source proof replay: choose a fixed smooth truncated inverse Cψ of length D* and choose Y*=U^B with B sufficiently large for the fixed field's strip-growth bound. In the Gamma integral `J=∫Y*^z Γ(z)L_orig(ρ+z,ψ)Cψ(ρ+z) dz`, shift to Re z=−1/4. The z=0 residue vanishes because the original L-function vanishes at ρ; the nonprincipal function is entire. The new-line bound has the form `U^{C−B/4} D*^{5/4−Re ρ}(1+T₁)^C` with fixed C. Since t is fixed and bounded, choose B sufficiently large and then τ sufficiently small. In the original expansion, Möbius convolution cancels all coefficients of norms between 1 and D*, while the unit term is 1+o(1). Dyadic separation of the remaining tail gives r≤t+O(1/log U), r+m≥t−O(1/log U), and a product of centrally normalized inverse and plain blocks of squared magnitude at least U^{δ(r+m)−η}, with δ=2a−1. A terminal cutoff at U^{B+1}, bounded profile seminorms, and one cumulative Fourier-height allowance are handled exactly as in the linked t=1 replay.

The same buffered pointwise bounds give `|M_r|²≪U^{δr+η}` and `|S_m|²≪U^{δ min(m,1−m)+η}`. Thus saturation forces m≤1/2+O(η/δ), and (2) follows by division. On this fixed σ range, choose e small so δ has a fixed positive lower bound. In the printed source proof the only numerical use of t≥1 occurs in the declaration of the range; the shifted-integral inequality is easier for smaller t. The source pointwise lemma covers bounded nonnegative r,m, and the support and saturation arguments above remain valid for this t>1/2. This is a replay of the proof, conditional on the field, profile and height inputs; it is not a claim that the published proposition explicitly states t<1.

The global inverse moment of the linked note, from [de Faveri Proposition 8.1](https://arxiv.org/abs/2610.04045v1), is

    Σ_{g: N cond(νχ_g)≤U} |M_r(g)|²
       ≪ U^ε [U+U^{1/2+r}],                                        (3)

for common smooth profiles, with the fixed polynomial height loss. Its coefficient classes include the Möbius support, the fixed twist ν, finite reciprocity phases and the unchanged noncoprime masks. Dyadic partition and the common-profile Sobolev reduction permit (3) to count the rowwise witnesses in (2). Write δ=2a−1≥δ₀−2e. On the interval `t−1/2−O(η)≤r≤t+o(1)`, the resulting exponent, up to small fixed losses, is

    F(r) = max{1−δ₀r, 1/2+(1−δ₀)r}.

The first affine function decreases and the second increases. The maximum on the interval occurs at an endpoint; with t=(1+δ₀)/2 those endpoints are δ₀/2 and (1+δ₀)/2, and both contribute at most `1−δ₀²/2`. Specifically, at the lower endpoint the second term is no larger than the first, and at the upper endpoint the first is no larger than the second. The O(e+η) loss is made smaller than ε. The O(log² U) dyads, boundedly many bins and finite reciprocity classes are absorbed into ε. Finally the standard individual zero count and the Sobolev/height factors cost a fixed polynomial in U^τ and a logarithm, so τ is chosen small enough to absorb their total exponent. This gives (1), subject to the stated inputs. □

## Stronger count using the plain witness

The same assumptions and short-detector replay yield the stronger conditional estimate

    Σ_{g good cube-free, N cond(νχ_g)≤X} N(σ,X^τ;νχ_g)
      ≪ X^{1−(2σ−1)/(2(3−2σ))+ε}.                                (4)

Here σ, ε and all fixed field and twist data determine τ>0 and the implied constant. At σ=4/5 this exponent is 11/14; at σ=5/6 it is 3/4; at σ=17/20 it is 19/26; at σ=7/8 it is 7/10. The same density-one and relative-zeta conclusions apply. In conductor ordering, the exceptional relative-quotient count has exponent `1−(2σ−1)/(2(3−2σ))`; under absolute discriminant ordering, it is `1/2−(2σ−1)/(4(3−2σ))`, with suitably shrunk height power and arbitrarily small fixed exponent loss. This remains a proposed source-conditional derivation, not a claim that the detector or the nonsquarefree-column moment is stated verbatim in either source.

On the principal-twist Eisenstein family, the displayed exponent is below the conductor-reordered Theorem 5.7 comparator throughout the open half-strip: their difference is `(1−σ)(5−4σ)/[(2−σ)(3−2σ)]>0`. This comparison does not replace the sharper higher-strip Theorem 1 comparison or the broad Hecke-family comparator, which can be stronger in parts of the range.

To prove the additional moment, take a normalized plain polynomial of length D=U^m, where `m≤1/2+O(η)`, with original row characters and a fixed smooth annular coefficient profile. Write each good column uniquely as q=q₁v² with q₁ squarefree; no coprimality between q₁ and v is imposed. Multiplicativity including zero extensions gives `χ_g(q)=χ_g(q₁)χ_g(v²)`. For each fixed v, the multiplier `χ_g(v²)` has modulus at most one and is independent of q₁. The common-profile squarefree-column bound (3) applies to the inner q₁-polynomial; its squared coefficient mass is `≪ (Nv)^(−2)` up to U^ε because `Nq₁≪D/(Nv)²`. Thus its row L² norm is at most `U^{1/2+O(η)+ε}/Nv`. Minkowski over v and the ideal estimate `Σ_{Nv≤C√D}(Nv)^(−1)≪log(2D)` give

    Σ_{g: N cond(νχ_g)≤U} |S_m(g)|² ≪ U^{1+O(η)+ε}.                (5)

The original row masks are retained exactly: if a prime divides both g and v, the outer multiplier is zero. The fixed ν(v²) and any norm-twist factor of absolute value one may be included in the outer multiplier, while the real-exponent profile remains smooth and uniformly bounded on the original q-annulus. For row-dependent zero ordinates and real parts, apply the same finite-order Sobolev argument as for the inverse block to each inner vector, uniformly in v: its profile is supported where `Nq₁/(D/(Nv)²)` lies in a fixed annulus, with uniformly bounded logarithmic derivatives. Summing the resulting uniform bounds over v preserves the logarithmic loss. Heights contribute only the fixed polynomial factor already absorbed by choosing τ. This paragraph is an additional analytic interface to be independently reviewed.

Set `δ₀=2σ−1` and now choose `t=1/(2−δ₀)=1/(3−2σ)`, which lies in (1/2,1). The short detector gives both individual saturation bounds and `r+m≥t−O(η)`, `m≤1/2+O(η)`. By Chebyshev, (3) bounds witness rows by `U^{max(1,1/2+r)−δ₀r+O(e+η)+ε}`, while (5) bounds them by `U^{1−δ₀m+O(e+η)+ε}`. The latter is at most `U^{1−δ₀(t−r)+O(e+η)+ε}`; therefore the count exponent is the minimum of those two displayed expressions. If r≤1/2, it is at most `1−δ₀ max(r,t−r)≤1−δ₀t/2`. If r≥1/2, it is at most `1/2+(1−δ₀)r≤1/2+(1−δ₀)t`. The chosen t equates these bounds, giving `1−δ₀/[2(2−δ₀)]`. The small endpoint, bin, finite-class and height losses are absorbed as above, proving (4) under the stated inputs. □

## Relative-zeta consequence

For ν=1, each nontrivial cubic character gives a cyclic cubic extension L/K, and class field theory gives `ζ_L/ζ_K=L(χ_g)L(conjugate(χ_g))`. The symmetric height window and (1) imply that, with at most O(X^{1−(2σ−1)²/2+ε}) exceptions, fields in this family with character-conductor norm ≤X have a zero-free relative quotient on the same rectangle. Distinct good prime conductor supports supply ≫X/log X such fields. The conductor–discriminant identity `|D_L|=|D_K|³ (N f_g)²` changes the exceptional exponent to `1/2−(2σ−1)²/4+ε` under discriminant ordering, with a suitably shrunk power height. Base ζ_K zeros remain; neither an individual uniform region nor a zero-free statement for ζ_L itself follows.

## Restricted families of arbitrary fixed order

There is a parallel conditional statement for fixed n≥3 and K containing μ_n. Let the labels be only `g=a b^(n−1)`, with a,b good squarefree coprime ideals, and let χ_g be the de Faveri order-n family with its original masks. Fix a unitary background ν, enlarge S to include its conductor, and impose the same fixed-type buffered detector, short-t, common-profile and height assumptions. In addition assume the general-n [rectangular squarefree-column sieve replay](../2026-10-29-conjugate-conductor-sieve/README.md), including its cited source inputs. Then the same exponent (4) holds for this restricted family, at any fixed `1/2<σ<1` and sufficiently small power height. Good prime labels give ≫X/log X distinct primitive characters, so it has the corresponding density-one zero-free rectangles.

Indeed, if A≤B and AB≤X, the two off-diagonal terms in that sieve are `A^(1−1/n)B^(1/n)D` and `A^(1/n)B^(1−1/n)D^(2/n)`. The first is at most `X^(1/2)D`. The second is at most `X^(1−1/n)D^(2/n)`, which is at most X for D≤X^(1/2), and at most `X^(1/2)D` for D≥X^(1/2). Summing dyads yields the same inverse moment (3). The plain moment (5) uses the decomposition q=q₁v², multiplicativity and modulus at most one only, so it applies equally to order n. The identical short-t optimization follows.

For n>3 this is a restricted ±1-exponent family, not the full n-th-power-free family. In particular, a zero-free statement for χ_g and its conjugate alone does not control all nontrivial character factors in a cyclic degree-n relative zeta quotient. The general-n sieve is a source-conditional replay, not a quoted general-n form of the printed cubic proposition.

**Independent review:** The cubic short-t argument, both moments, bin and height quantifiers and numerical examples were checked in [INDEPENDENT-REVIEW.md](INDEPENDENT-REVIEW.md), conditional on the source and uniformity inputs. The reviewer subsequently checked the arbitrary-order extension and the separate floor replay; both remain conditional on their stated source inputs.
