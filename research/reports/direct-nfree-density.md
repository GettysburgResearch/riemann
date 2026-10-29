# A fourth-witness zero-density estimate for fixed-order Hecke families

## Abstract

For a fixed integer n≥4 and a fixed number field containing μ_n, we combine the n-th-order large sieve of de Faveri with a long-cutoff zero detector and a fourth moment of its ordinary witness. Subject to the source hypotheses stated below, the resulting natural-label zero-density exponent is strictly smaller throughout a nonempty interval than the exponent in de Faveri’s Corollary 1.5. The estimate holds to a sufficiently small polynomial height. It is a family-density result, not an individual zero-free region. We also give a conditional density-one full Dedekind-zeta consequence for a specific family of cyclic quintic extensions, using a separately checked Dirichlet input for the fixed base field.

## 1. Statement and inputs

Fix n≥4, a number field K containing μ_n, and the fixed FHL family data and finite bad-prime set S in [de Faveri, *Optimal large sieve for fixed order characters*, arXiv:2610.04045v1](https://arxiv.org/abs/2610.04045v1). Ideals below are integral and coprime to S. Write `N a` for the ideal norm and call an ideal n-free if all its prime exponents are less than n. Let χ_u be the source character indexed by u, with the original zero extension at the primes dividing its presentation, and let `L(s,χ_u^*)` be its primitive inducing Hecke L-function. For `1/2<σ<1` and T≥1, let

    N_u(σ,T) = #{ρ : L(ρ,χ_u^*)=0, Re ρ≥σ, |Im ρ|≤T},

with zeros counted with multiplicity.

We use the following named inputs.

1. **FHL family and local data.** The source's multiplicative character identities and zero conventions hold. For good n-free u, the primitive conductor and the radical of the presentation's deleted Euler factors have norms `≪_{K,S,n} Nrad(u)`. Every good prime dividing a nonunit u contributes a nontrivial tame local character; the good conductor support is therefore exactly the support of u. The archimedean type belongs to a fixed finite set. These are source inputs, not derived here from the sieve.
2. **Classical fixed-field Hecke theory.** Primitive finite-order Hecke L-functions have their standard analytic continuation, Euler products, functional equations, fixed-strip polynomial growth in conductor and height, and individual zero-count bounds. The principal pole is treated separately. We use the standard finite-ideal counting and divisor bounds, Mellin inversion, Borel–Carathéodory, three-circles, and Sobolev inequalities.
3. **The printed n-th-order sieve.** De Faveri’s Theorem 1.1, including its stated reciprocity and fixed ray-sector conventions, applies to n-free row and column ideals with arbitrary complex column coefficients. Explicitly, for a column supported on n-free ideals `Na≤D`,

       Σ_{u n-free, Nu≤Y} |Σ_a c_a χ_u(a)|²
         ≪_ε (YD)^ε [Y+D+Y^(1−1/n)D^(2/n)
                                  +Y^(2/n)D^(1−1/n)] Σ_a |c_a|².   (1.1)

The source allows fixed finite ray partitions and the original noncoprime zeros. Its preprint proof and the local FHL statements have not been independently verified in this work.

**Theorem 1.** Fix

    1/2+1/n < σ < 1−1/(2n),       δ=2σ−1.

Define

    R_n(σ)=2/n + 3(n−3)(1−1/n−δ)/[n(3−δ)−7].                  (1.2)

Under inputs 1–3, for every ε>0 there exists τ>0 such that, for X≥2,

    Σ_{u n-free, Nu≤X} N_u(σ,X^τ)
       ≪_{K,S,n,σ,ε} X^(R_n(σ)+ε).                            (1.3)

The constants and τ may depend on the fixed field, order, σ and ε. The estimate is ordered by the natural label Nu; it does not count all Hecke characters by conductor. Good squarefree labels alone give `≫X` distinct primitive characters: their good conductor support is their label, and squarefree ideal counting has positive density. Here `1−R_n(σ)=[δn(2n−7)−n+5]/[n(n(3−δ)−7)]>0`, using δ>2/n. Thus (1.3) gives a density-one zero-free rectangle in this specified family at a sufficiently small power height.

## 2. Uniform long-cutoff detector

We record the detector in the form used in the proof. The derivation is included here; full contour and profile details, with an independent source-level review, are in [the detector proof](../exploratory/2026-10-29-direct-nfree-density/UNIFORM-DETECTOR-PROOF.md) and [its review](../exploratory/2026-10-29-direct-nfree-density/DETECTOR-INDEPENDENT-REVIEW.md). It is based on the gamma-convolution method and buffering in [OpenAI, Lemmas 4.9–4.10 and 8.1–8.3](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf); we need only 1<t<3/2.

**Detector lemma.** Fix `1<t<3/2`, `1/2<σ₀<1`, and a prescribed small loss η>0. For sufficiently small τ>0, every nonprincipal row u with `Nu≤X` and a primitive zero in `Re s≥σ₀`, `|Im s|≤X^τ` has, after a finite binning, a parameter `a≥σ₀−η`, two dyadic scales D=X^r and N=X^m, and a common real frequency h such that, up to arbitrarily small prescribed endpoint losses,

    0≤r≤t,       0≤m≤1/2,       r+m≥t,                         (2.1)
    |M_u(D)|² ≥ X^[(2a−1)r−η],
    |S_u(N)|² ≥ X^[(2a−1)m−η].                                  (2.2)

The selected zero may belong to χ_u or its complex conjugate; the same presentation is used in both witnesses. On good ideals, for common smooth annular profiles and their common cutoff,

    M_u(D)=D^(−1/2) Σ_l μ_K(l)χ_u(l) W_M(Nl/D)(Nl/D)^(−β−ih),
    S_u(N)=N^(−1/2) Σ_k χ_u(k) W_S(Nk/N)(Nk/N)^(−β−ih),        (2.3)

where β is the selected zero's real part. Unit-scale endpoints are included by a fixed annular convention. There are finitely many bin and orientation choices and O(log²X) dyadic pairs. The only row-varying real profile parameters are β in a fixed compact interval and `|h|≪X^τ`.

*Proof.* Fix a floor `1/2<σ_f<σ₀` and a small e>0. For each row take nested maxima of the real parts of zeros of the primitive character and its conjugate at heights `3jX^τ`. Since the maxima lie between σ_f and 1, two consecutive maxima differ by at most e for one of O(1/e) indices. Grid rounding gives a bin a and a zero ρ=β+iγ with `a≤β<a+e`, `a≥σ₀−e`, and a larger height rectangle zero-free for both presentations to the right of `a+2e`.

The conductor and deletion bounds in input 1 are uniform by X. In that rectangle, anchor `log L` at real part 2 by its Euler series. Classical fixed-strip growth, Borel–Carathéodory and three-circles give, for any fixed small η₁>0,

    |L^S(s,χ_u)|+|L^S(s,χ_u)|^(−1) ≪ X^η₁

on a slightly smaller right-hand rectangle `Re s≥a+6e`; the same holds for the conjugate. On `Re s=1−a−6e`, the functional equation and deleted-factor bound give `|L^S|≪X^(a−1/2+12e+η₁)(1+X^τ)^A`, with fixed A. All shifts of the selected height and Fourier parameter share one reserved height budget.

Mellin inversion and partial contour shifts inside this buffer give, for bounded r,m and sufficiently small combined losses,

    |M_u(D)|² ≪ X^[(2a−1)r+η₁],
    |S_u(N)|² ≪ X^[(2a−1)min(m,1−m)+η₁].                     (2.4)

The first line uses the right-hand reciprocal bound; the second uses either that line or the reflected left line. On the remaining high-frequency tails, stay on absolute-convergence lines and use arbitrarily high fixed profile decay. Profile and strip-growth orders are fixed before τ; the external tail order is then chosen large enough.

For the lower bound set D*=X^t, choose a smooth cutoff V equal to 1 on [0,1] and 0 past 2, and put

    C_u(s)=Σ_l μ_K(l)χ_u(l)V(Nl/D*)(Nl)^(−s).

Integrate `X^(Bz)Γ(z)L^S(ρ+z,χ_u)C_u(ρ+z)` on Re z=2. The selected nonprincipal L-function is entire. Shifting to Re z=−1/4 crosses only the Γ pole at zero, whose residue vanishes at ρ. Uniform strip growth makes the shifted integral o(1) after choosing a fixed sufficiently large B and then sufficiently small τ. On the original line the unit coefficient tends to 1; for every good nonunit ideal of norm ≤D*, the Möbius convolution coefficient is zero. Insert a product cutoff and a polynomial terminal cutoff, dyadically partition the two factors, and separate the smooth product profile by Fourier inversion in its logarithm. Uniform logarithmic derivatives and one common frequency yield a dyadic pair satisfying (2.1) and

    |M_u(D) S_u(N)|² ≥ X^[(2a−1)(r+m)−η₁].                      (2.5)

Here the multiplicativity and the convolution cancellation include the original zero masks. Comparing (2.5) with (2.4) forces `m≤1/2+O(η₁)` because `2a−1` is bounded away from zero. Dividing by the opposite upper bound in each case gives both inequalities in (2.2). Shrink the preliminary losses to obtain η. The principal row, if present, is not put through this contour argument; its individual zero count is negligible in (1.3). □

## 3. Common coefficients and the fourth moment

The moment estimate must apply to a common coefficient vector, while the detector selects β and h row by row. In a fixed bin, dyadic pair and presentation orientation, the other profile data in (2.3) are common. Apply the two-parameter first-order Sobolev inequality to M and to S² on the fixed β interval and the height interval `|h|≪X^τ`. For each parameter value and each of the four mixed derivatives, all rows use one common coefficient vector. Annular logarithms are bounded up to powers of log X; the height integration costs at most a fixed polynomial power of X^τ. If the selected presentation is conjugate, conjugate the entire coefficient vector in (1.1); do not relabel u, which can change its norm.

The inverse vector is supported on squarefree, hence n-free, ideals and has squared coefficient mass `≪X^ε`. For the ordinary fourth moment first square the ordinary block. Its normalized coefficients are divisor-bounded and its length is `≪N²`. Write each column ideal uniquely as `a=a₁v²`, with a₁ squarefree and no coprimality requirement. At fixed v,

    χ_u(a)=χ_u(a₁)χ_u(v²),       |χ_u(v²)|≤1,

including shared-prime zeros. The second factor is a row contraction outside the common a₁-sum. The squared a₁-coefficient mass is `≪X^ε/(Nv)²`. Apply (1.1) to each vector and use Minkowski in the row ℓ² norm; `Σ_(Nv≲X^C)1/Nv≪log X`. The same argument applies after each fixed profile derivative. Thus, for a dyadic vector of length D=X^x, both the inverse second moment and the ordinary fourth moment at D=N² have the exponent of the bracket in (1.1), with arbitrarily small losses.

Choose all bin, contour, profile and moment losses before choosing τ, and then choose the external Fourier-tail order. The O(X^τ) Sobolev and individual zero-count factors and the fixed polynomial height costs are absorbed into X^ε. This also turns a bound on bad rows into a bound on zeros counted with multiplicity.

## 4. Four-face proof of Theorem 1

With δ=2σ−1, divide the sieve bracket for length X^x by the squared witness threshold X^(δx). Its four exponents are

    f₀(x)=1−δx,            f_D(x)=(1−δ)x,
    f₂(x)=1−1/n+(2/n−δ)x, f₃(x)=2/n+(1−1/n−δ)x.                (4.1)

The selected bin has `a≥σ−η`, so using δ in place of 2a−1 loses only O(η), since all lengths are bounded. Set

    t=3(n−3)/[n(3−δ)−7],       L=2t/3.                          (4.2)

The interval `2/n<δ<1−1/n` gives `1<t<3/2` and `1/2<L<1`. On [L,t], f₂ decreases and f₃ increases. Moreover

    f₂−f₃=(1−3/n)(1−x),
    f₂−f₀=(2x−1)/n,       f₃−f_D=(2−x)/n.

Consequently the maximum of the four faces throughout [L,t] is at most

    max{f₂(L),f₃(t)}=R_n(σ).                                   (4.3)

For a row with a detector witness, if r≥L use the inverse second moment. If r<L, (2.1) gives `2m≥2(t−r)>L`, while `2m≤1≤t`; use the ordinary fourth moment. Both cases give the exponent (4.3). Fixed detector overflows are absorbed by the preliminary loss. Summing bins, dyads and orientations, then applying the uniform zero count, proves (1.3). □

## 5. One named-source comparison

In this σ interval the middle branch of de Faveri’s Corollary 1.5 gives the natural-label fixed-height exponent

    D_n(σ)=1−δ[δn²−(1+3δ)n+3]
                    /[n²δ(2−δ)−2n(1+δ)+2].                     (5.1)

Algebra yields

    D_n−R_n = (nδ−2)[n(1−δ)−1][n(n−4)δ−n+5]
       /{n[n(3−δ)−7][n²δ(2−δ)−2n(1+δ)+2]}.                    (5.2)

The first two numerator factors are positive by the σ interval. The third is 1 for n=4 and exceeds n−3 for n≥5. The last denominator factor is concave in δ and has positive endpoint values `2(n−3)` and `(n−3)(n−1)`; the other denominator factors are positive. Thus `D_n(σ)>R_n(σ)` for every fixed admissible pair. The strict gap persists at a sufficiently small polynomial height after taking account of both bounds' height losses. This comparison addresses that named preprint, not every possible prior or later result; it is conditional on the stated source inputs. At σ=4/5, for example, `R_5=16/25` whereas the cited source exponent is `23/35`.

## 6. A cyclic quintic full-zeta family

Take p=5 and `K=Q(ζ₅)`. Let θ=4369347/5000000=0.8738694. Assume, in addition to inputs 1–3, that replacing the FHL root-of-unity embedding by its j-th power gives the same indexed family for χ_u^j, for each j=1,2,3,4, with the same label cutoff and masks. This is a source compatibility input: replacing u by an exponent-reduced label is not sufficient, since that can change Nu. Assume also the conventional analytic interpretation and tracker admission of the separately kernel-replayed [Dirichlet candidate at θ](../exploratory/2026-10-29-return-retune-8738694/README.md), which asserts zero-freeness for Dirichlet L-functions in Re s>θ, apart from their principal pole.

For each nonunit good fifth-free u, χ_u has exact order five, since any good prime dividing u carries a nontrivial local character. Let L_u/K be its cyclic degree-five class field. Artin factorization gives

    ζ_(L_u)(s)=ζ_K(s) ∏_(j=1)^4 L(s,χ_u^j).                  (6.1)

The primitive and original factors have the same zeros in Re s>0 because their deleted Euler factors do not vanish there. Apply Theorem 1 at σ=θ separately to the four fixed embedding families and take their finite union. For some τ>0, all but

    O_ε(X^[5045224/10653265+ε])                                (6.2)

of the labels Nu≤X have all four relative factors zero-free in `Re s≥θ, |Im s|≤X^τ`. The fixed base ζ_K is the product of ζ and the three nonprincipal Dirichlet L-functions modulo 5; the admitted Dirichlet input gives its nonvanishing for Re s>θ, with its pole at 1 not counted as a zero. Therefore the corresponding full ζ_(L_u) is zero-free in the **open** rectangle `Re s>θ, |Im s|≤X^τ`, outside the exceptional labels in (6.2).

Good squarefree labels supply `≫X` distinct primitive order-five characters, and a field has at most four generating characters; consequently they supply `≫X` distinct fields. The conductor–discriminant formula and `Nf(χ_u)≪Nu` give `|D_(L_u)|≪_{K,S}X⁴`. Taking X to be a sufficiently small fixed multiple of Y^(1/4) yields a specified family of `≫Y^(1/4)` distinct fields with `|D_(L_u)|≤Y`, at most

    O_ε(Y^[1261306/10653265+ε])                                (6.3)

of which fail the stated rectangle at a suitably scaled small power height. This is a family produced from a label cutoff; it is not a count of every cyclic quintic extension by discriminant. The conclusion is conditional on the separately admitted Dirichlet input and the stated sieve/FHL assumptions. It gives neither an individual improved half-plane nor all-height nonvanishing for the varying relative factors.
