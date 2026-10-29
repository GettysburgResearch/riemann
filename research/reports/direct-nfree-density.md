# A fourth-witness zero-density estimate for fixed-order Hecke families

## Abstract

For a fixed integer n≥4 and a fixed number field containing μ_n, we combine the n-th-order large sieve of de Faveri with a long-cutoff zero detector and a fourth moment of its ordinary witness. Subject to the source hypotheses stated below, the resulting natural-label zero-density exponent is strictly smaller throughout a nonempty interval than the exponent in de Faveri’s Corollary 1.5. The estimate holds to a sufficiently small polynomial height. It is a family-density result, not an individual zero-free region. We also give a conditional density-one full Dedekind-zeta consequence for a specific family of cyclic quintic extensions, using a separately checked Dirichlet input for the fixed base field.

## 1. Statement and inputs

Fix n≥3, a number field K containing μ_n, a fixed unitary Hecke character ν, and the fixed FHL family data and finite bad-prime set S in [de Faveri, *Optimal large sieve for fixed order characters*, arXiv:2610.04045v1](https://arxiv.org/abs/2610.04045v1). Enlarge S once to contain the finite conductor and any fixed deleted primes of ν. Ideals below are integral and coprime to S. Write `N a` for the ideal norm and call an ideal n-free if all its prime exponents are less than n. Let χ_u be the source character indexed by u, with the original zero extension at the primes dividing its presentation, write ψ_u=νχ_u, and let `L(s,ψ_u^*)` be its primitive inducing Hecke L-function. The unitary ν may have arbitrary fixed angular and norm type at infinity. For `1/2<σ<1` and T≥1, let

    N_u(σ,T) = #{ρ : L(ρ,ψ_u^*)=0, Re ρ≥σ, |Im ρ|≤T},

with zeros counted with multiplicity.

We use the following named inputs.

1. **FHL family and local data.** The source's multiplicative character identities and zero conventions hold. For good n-free u, the primitive conductor and the radical of the presentation's deleted Euler factors have norms `≪_{K,S,n} Nrad(u)`. At a good prime with exponent e in u, the tame local character is the e-th power of an exact order-n residue character; hence exponents 1,…,n−1 are distinct, and the good conductor support is exactly the support of u. After twisting by fixed ν, the conductor and deleted-radical bounds remain `≪_{ν}Nrad(u)`; ν is unramified at good primes, so it cannot cancel the indicated tame inertia. The archimedean type of ψ_u belongs to the fixed finite set determined by ν. These are source inputs, not derived here from the sieve.
2. **Classical fixed-field Hecke theory.** Primitive unitary Hecke L-functions of the fixed archimedean types involved here have their standard analytic continuation, Euler products, functional equations, fixed-strip polynomial growth in conductor and height, and individual zero-count bounds. Pure norm characters and their shifted principal poles are treated separately. We use the standard finite-ideal counting and divisor bounds, Mellin inversion, Borel–Carathéodory, three-circles, and Sobolev inequalities.
3. **The printed n-th-order sieve.** De Faveri’s Theorem 1.1, including its stated reciprocity and fixed ray-sector conventions, applies to n-free row and column ideals with arbitrary complex column coefficients. Explicitly, for a column supported on n-free ideals `Na≤D`,

       Σ_{u n-free, Nu≤Y} |Σ_a c_a χ_u(a)|²
         ≪_ε (YD)^ε [Y+D+Y^(1−1/n)D^(2/n)
                                  +Y^(2/n)D^(1−1/n)] Σ_a |c_a|².   (1.1)

The source allows fixed finite ray partitions and the original noncoprime zeros. Its preprint proof and the local FHL statements have not been independently verified in this work.

**Theorem 1.** Fix n≥4 and

    1/2+1/n < σ < 1,       δ=2σ−1.

Define, with h=1−δ,

    R_n(σ) = 2/n + 3(n−3)(1−1/n−δ)/[n(3−δ)−7]  if δ≤1−1/n,
             10h/(4+nh)                           if δ≥1−1/n.  (1.2)

The two formulas agree at δ=1−1/n; the endpoint is obtained from the first interval with a small ε loss, as explained below.

Under inputs 1–3, for every ε>0 there exists τ>0 such that, for X≥2,

    Σ_{u n-free, Nu≤X} N_u(σ,X^τ)
       ≪_{K,S,n,σ,ε} X^(R_n(σ)+ε).                            (1.3)

The constants and τ may depend on the fixed field, order, ν, σ and ε. The estimate is ordered by the natural label Nu; it does not count all Hecke characters by conductor. Good squarefree labels alone give `≫X` distinct primitive characters: their good conductor support is their label, and squarefree ideal counting has positive density. For δ≤1−1/n, `1−R_n(σ)=[δn(2n−7)−n+5]/[n(n(3−δ)−7)]>0`, using δ>2/n. In the high-δ range, `R_n≤2/n<1`. Thus (1.3) gives a density-one zero-free rectangle in this specified family at a sufficiently small power height.

## 2. Uniform long-cutoff detector

We record the detector in the form used in the proof. The derivation is included here; full contour and profile details, with an independent source-level review, are in [the detector proof](../exploratory/2026-10-29-direct-nfree-density/UNIFORM-DETECTOR-PROOF.md) and [its review](../exploratory/2026-10-29-direct-nfree-density/DETECTOR-INDEPENDENT-REVIEW.md). It is based on the gamma-convolution method and buffering in [OpenAI, Lemmas 4.9–4.10 and 8.1–8.3](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf); we use only the fixed bounded range 1<t<5/2; the extension beyond the source’s printed range is checked in [the long-cutoff review](../exploratory/2026-10-29-direct-nfree-density/LONG-CUTOFF-REVIEW.md).

**Detector lemma.** Fix `1<t<5/2`, `1/2<σ₀<1`, and a prescribed small loss η>0. For sufficiently small τ>0, every row whose primitive inducing character is not a pure norm character, with `Nu≤X` and a primitive zero in `Re s≥σ₀`, `|Im s|≤X^τ` has, after a finite binning, a parameter `a≥σ₀−η`, two dyadic scales D=X^r and N=X^m, and a common real frequency h such that, up to arbitrarily small prescribed endpoint losses,

    0≤r≤t,       0≤m≤1/2,       r+m≥t,                         (2.1)
    |M_u(D)|² ≥ X^[(2a−1)r−η],
    |S_u(N)|² ≥ X^[(2a−1)m−η].                                  (2.2)

The selected zero may belong to ψ_u or its complex conjugate; the same presentation is used in both witnesses. On good ideals, for common smooth annular profiles and their common cutoff,

    M_u(D)=D^(−1/2) Σ_l μ_K(l)ψ_u(l) W_M(Nl/D)(Nl/D)^(−β−ih),
    S_u(N)=N^(−1/2) Σ_k ψ_u(k) W_S(Nk/N)(Nk/N)^(−β−ih),        (2.3)

where β is the selected zero's real part. Unit-scale endpoints are included by a fixed annular convention. There are finitely many bin and orientation choices and O(log²X) dyadic pairs. The only row-varying real profile parameters are β in a fixed compact interval and `|h|≪X^τ`.

*Proof.* Fix a floor `1/2<σ_f<σ₀` and a small e>0. For each row take nested maxima of the real parts of zeros of the primitive character and its conjugate at heights `3jX^τ`. Since the maxima lie between σ_f and 1, two consecutive maxima differ by at most e for one of O(1/e) indices. Grid rounding gives a bin a and a zero ρ=β+iγ with `a≤β<a+e`, `a≥σ₀−e`, and a larger height rectangle zero-free for both presentations to the right of `a+2e`.

The conductor and deletion bounds in input 1 are uniform by X. In that rectangle, anchor `log L` at real part 2 by its Euler series. Classical fixed-strip growth, Borel–Carathéodory and three-circles give, for any fixed small η₁>0,

    |L^S(s,ψ_u)|+|L^S(s,ψ_u)|^(−1) ≪ X^η₁

on a slightly smaller right-hand rectangle `Re s≥a+6e`; the same holds for the conjugate. On `Re s=1−a−6e`, the functional equation and deleted-factor bound give `|L^S|≪X^(a−1/2+12e+η₁)(1+X^τ)^A`, with fixed A. All shifts of the selected height and Fourier parameter share one reserved height budget.

Mellin inversion and partial contour shifts inside this buffer give, for bounded r,m and sufficiently small combined losses,

    |M_u(D)|² ≪ X^[(2a−1)r+η₁],
    |S_u(N)|² ≪ X^[(2a−1)min(m,1−m)+η₁].                     (2.4)

The first line uses the right-hand reciprocal bound; the second uses either that line or the reflected left line. On the remaining high-frequency tails, stay on absolute-convergence lines and use arbitrarily high fixed profile decay. Profile and strip-growth orders are fixed before τ; the external tail order is then chosen large enough.

For the lower bound set D*=X^t, choose a smooth cutoff V equal to 1 on [0,1] and 0 past 2, and put

    C_u(s)=Σ_l μ_K(l)ψ_u(l)V(Nl/D*)(Nl)^(−s).

Integrate `X^(Bz)Γ(z)L^S(ρ+z,ψ_u)C_u(ρ+z)` on Re z=2. The selected non-norm inducing L-function is entire. Shifting to Re z=−1/4 crosses only the Γ pole at zero, whose residue vanishes at ρ. Uniform strip growth makes the shifted integral o(1) after choosing a fixed sufficiently large B and then sufficiently small τ. On the original line the unit coefficient tends to 1; for every good nonunit ideal of norm ≤D*, the Möbius convolution coefficient is zero. Insert a product cutoff and a polynomial terminal cutoff, dyadically partition the two factors, and separate the smooth product profile by Fourier inversion in its logarithm. Uniform logarithmic derivatives and one common frequency yield a dyadic pair satisfying (2.1) and

    |M_u(D) S_u(N)|² ≥ X^[(2a−1)(r+m)−η₁].                      (2.5)

Here the multiplicativity and the convolution cancellation include the original zero masks. Comparing (2.5) with (2.4) forces `m≤1/2+O(η₁)` because `2a−1` is bounded away from zero. Dividing by the opposite upper bound in each case gives both inequalities in (2.2). Shrink the preliminary losses to obtain η. A pure norm-character or principal presentation, if present, is not put through this contour argument: it can occur only at u=1, because ν is unramified at every good prime dividing a nonunit u. Its individual zero count is negligible in (1.3). □

## 3. Common coefficients and the fourth moment

The moment estimate must apply to a common coefficient vector, while the detector selects β and h row by row. In a fixed bin, dyadic pair and presentation orientation, the other profile data in (2.3) are common. Apply the two-parameter first-order Sobolev inequality to M and to S² on the fixed β interval and the height interval `|h|≪X^τ`. For each parameter value and each of the four mixed derivatives, all rows use one common coefficient vector. Annular logarithms are bounded up to powers of log X; the height integration costs at most a fixed polynomial power of X^τ. If the selected presentation is conjugate, conjugate the entire coefficient vector in (1.1); do not relabel u, which can change its norm.

The inverse vector is supported on squarefree, hence n-free, ideals and has squared coefficient mass `≪X^ε`. For the ordinary fourth moment first square the ordinary block. Its normalized coefficients are divisor-bounded and its length is `≪N²`. Write each column ideal uniquely as `a=a₁v²`, with a₁ squarefree and no coprimality requirement. At fixed v,

    ψ_u(a)=ψ_u(a₁)ψ_u(v²),       |ψ_u(v²)|≤1,

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

For a row with a detector witness, if r≥L use the inverse second moment. If r<L, (2.1) gives `2m≥2(t−r)>L`, while `2m≤1≤t`; use the ordinary fourth moment. Both cases give the exponent (4.3). Fixed detector overflows are absorbed by the preliminary loss. Summing bins, dyads and orientations, then applying the uniform zero count, proves (1.3) in the first open interval. □

**High-δ range.** Suppose `1−1/n<δ<1`, put `h=1−δ`, and choose

    t=10/(4+nh) ∈(2,5/2),    L=4t/5,    R=ht.                 (4.4)

The inverse witness gives the count exponent f(r); the ordinary **eighth** moment gives f(4m). For the latter, convolve four common ordinary blocks, write the resulting column as `a=a₁v²`, and retain ψ_u(v²) as a fixed-v row contraction. The divisor-bounded coefficients, fixed Sobolev derivatives and Minkowski argument of §3 give exactly the bracket in (1.1) at length N⁴. On `[L,2]`, f=f₃ decreases; on `[2,t]`, f=f_D increases, and `f₃(L)=f_D(t)=R`. If r≥L, the inverse witness gives R. Otherwise `4m≥4(t−r)>L` and `4m≤2`, so the ordinary eighth witness gives R. This uses the entire allowed m interval; it does not assume m=t−r.

At δ=1−1/n the two formulas both give `R=2/n`. For each requested ε apply the first-range estimate at a fixed slightly smaller σ; its zero count dominates the count at the endpoint, and its exponent differs from 2/n by less than ε. Its resulting positive height power is fixed after that choice.

**Theorem 2 (cubic high range).** Under the same three named inputs with n=3, for each fixed `5/6<σ<1` and ε>0 there is τ>0 such that

    Σ_{u cube-free, Nu≤X} N_u(σ,X^τ)
       ≪ X^[10h/(4+3h)+ε],       h=2(1−σ).                     (4.5)

The argument in the preceding high-δ paragraph remains valid for n=3: f₂=f₃, with f₃ dominating until x=2 and f_D thereafter. All cutoff, height and masks have the same fixed-field qualifications. The cubic assertion concerns this high range only; the middle-range formula (1.2) was derived for n≥4.

## 5. One named-source comparison

For the untwisted family ν=1, in the middle interval `2/n<δ<1−1/n`, the middle branch of de Faveri’s Corollary 1.5 gives the natural-label fixed-height exponent

    D_n(σ)=1−δ[δn²−(1+3δ)n+3]
                    /[n²δ(2−δ)−2n(1+δ)+2].                     (5.1)

Algebra yields

    D_n−R_n = (nδ−2)[n(1−δ)−1][n(n−4)δ−n+5]
       /{n[n(3−δ)−7][n²δ(2−δ)−2n(1+δ)+2]}.                    (5.2)

The first two numerator factors are positive by the σ interval. The third is 1 for n=4 and exceeds n−3 for n≥5. The last denominator factor is concave in δ and has positive endpoint values `2(n−3)` and `(n−3)(n−1)`; the other denominator factors are positive. Thus `D_n(σ)>R_n(σ)` for every fixed admissible pair. The strict gap persists at a sufficiently small polynomial height after taking account of both bounds' height losses. This comparison addresses that named preprint, not every possible prior or later result; it is conditional on the stated source inputs. At σ=4/5, for example, `R_5=16/25` whereas the cited source exponent is `23/35`.

In the high interval `0<h=1−δ<1/n`, the cited source's upper branch and its difference from (4.4) are

    D_high=h[3−(n+2)h]/(1−nh²),
    D_high−R_high=h(1−nh)[2+(n−8)h]/[(4+nh)(1−nh²)] > 0.          (5.3)

The last numerator factor is positive: for 3≤n<8 it is at least `3−8/n>0` at h=1/n, and for n≥8 it is at least 2. Thus the inequality is strict for every n≥3 in its high range. At δ=1−1/n the two rates agree; no strict comparison is claimed there.

A second named comparison is available only when ν is finite order and K is in the fixed Galois-field, finite-order setting of [Khale–O’Kuhn–Panidapu–Sun–Zhang](https://arxiv.org/abs/2008.09677v3). Their fixed-height conductor-family exponent can be written

    K(δ)=6(1−δ)/(3−δ)  for δ≤3/5,
         4(1−δ)/(1+δ)  for δ≥3/5.                              (5.4)

The natural n-free labels inject into this larger conductor family by their good local characters, and their conductors are `≪Nu`. In the middle interval K>R_n. For δ≤3/5 this follows from K≥1>R_n. For δ≥3/5, clearing positive denominators gives

    K−R_n = P_n(δ)/[n(1+δ)(n(3−δ)−7)],
    P_n=7n(n−1)δ²−(16n²−27n−5)δ+9n²−22n+5.

On the relevant interval P_n decreases to the positive value `4(n−3)/n` at δ=1−1/n. In the high interval,

    K−R_high=2h[(2n+5)h−2]/[(2−h)(4+nh)].                     (5.5)

The bracket is strictly increasing on `(0,1/n)` and has the unique root

    h_c=2/(2n+5).

Thus R_high is smaller than that named bound for h>h_c, equal at h_c and larger for h<h_c. These are comparisons of displayed exponents, with sufficiently small polynomial heights and the named source's field hypotheses; they are not exhaustive priority claims.

For n≥4 the entire high-δ interval has σ>7/8. Recent preprints of Liu and Hu claim individual all-height regions to the right of approximately 0.874886647 and 7/8 respectively; if validated, Liu’s finite-order claim supersedes the corresponding n≥4 high-interval family statement when ν has finite order, while Hu’s stated unitary scope would also include fixed angular ν. Their claims have not been independently verified here. For n=3 the high range starts at 5/6, so it is not wholly covered by those claimed individual regions. It nevertheless has stronger known *claimed density* comparators in important cases: at θ=0.8738694, (4.5) gives `6306530/11891959≈0.530319`, whereas [rStation paper 52 v5, Theorem 1](https://rstation.ai/problems/riemann_hypothesis/papers/52/v5), for its Eisenstein cubic family with fixed finite twist, gives `1891959/4564490≈0.414495` at sufficiently small polynomial height. That comparison is source-dependent and does not imply the same bound over arbitrary fixed number fields containing μ₃.

## 6. A cyclic quintic full-zeta family

For this application take ν=1, p=5 and `K=Q(ζ₅)`. Let θ=4369347/5000000=0.8738694. Assume, in addition to inputs 1–3, that replacing the FHL root-of-unity embedding by its j-th power gives the same indexed family for χ_u^j, for each j=1,2,3,4, with the same label cutoff and masks. This is a source compatibility input: replacing u by an exponent-reduced label is not sufficient, since that can change Nu. Assume also the conventional analytic interpretation and tracker admission of the separately kernel-replayed [Dirichlet candidate at θ](../exploratory/2026-10-29-return-retune-8738694/README.md), which asserts zero-freeness for Dirichlet L-functions in Re s>θ, apart from their principal pole.

For each nonunit good fifth-free u, χ_u has exact order five, since any good prime dividing u carries a nontrivial local character. Let L_u/K be its cyclic degree-five class field. Artin factorization gives

    ζ_(L_u)(s)=ζ_K(s) ∏_(j=1)^4 L(s,(χ_u^j)^*).              (6.1)

The Artin factorization uses primitive all-place Hecke factors. The primitive and original factors have the same zeros in Re s>0 because their deleted Euler factors do not vanish there. Apply Theorem 1 at σ=θ separately to the four fixed embedding families and take their finite union. For some τ>0, all but

    O_ε(X^[5045224/10653265+ε])                                (6.2)

of the labels Nu≤X have all four relative factors zero-free in `Re s≥θ, |Im s|≤X^τ`. The fixed base ζ_K is the product of ζ and the three nonprincipal Dirichlet L-functions modulo 5; the admitted Dirichlet input gives its nonvanishing for Re s>θ, with its pole at 1 not counted as a zero. Therefore the corresponding full ζ_(L_u) is zero-free in the **open** rectangle `Re s>θ, |Im s|≤X^τ`, outside the exceptional labels in (6.2).

Good squarefree labels supply `≫X` distinct primitive order-five characters, and a field has at most four generating characters; consequently they supply `≫X` distinct fields. The conductor–discriminant formula and `Nf(χ_u)≪Nu` give `|D_(L_u)|≪_{K,S}X⁴`. Taking X to be a sufficiently small fixed multiple of Y^(1/4) yields a specified family of `≫Y^(1/4)` distinct fields with `|D_(L_u)|≤Y`, at most

    O_ε(Y^[1261306/10653265+ε])                                (6.3)

of which fail the stated rectangle at a suitably scaled small power height. This is a family produced from a label cutoff; it is not a count of every cyclic quintic extension by discriminant. The conclusion is conditional on the separately admitted Dirichlet input and the stated sieve/FHL assumptions. It gives neither an individual improved half-plane nor all-height nonvanishing for the varying relative factors.

## 7. A common moving twist and simultaneous finite-order twists

The same argument has a conductor-uniform form. Here fix the FHL set S **before** choosing the twist; do not enlarge S by primes whose number or norm grows with X. Let A be a fixed compact set of archimedean parameters. For each X let ν=ν_X be one common unitary Hecke character with primitive conductor norm `Nf_ν≤X^κ` and infinity parameters in A. Use the canonical conductor-zero extension of ν; more general presentations require a separate bound on their additional deleted radical. Write `ψ_u=νχ_u` and count zeros of its primitive inducing L-function.

For any fixed `κ≥0`, retain the t and R of the applicable branch and put

    E = max{R, f(1+κ)}              in the middle range,
    E = max{R, 2h(1+κ)}            in the high range,           (7.0)

where f is the maximum of the four affine faces in (4.1). Under the same sieve/FHL inputs and the standard Hecke estimates **uniform in conductor and compact archimedean type**, for every ε>0 there is a τ>0 and an implied constant, both uniform over every such common ν, such that

    Σ_{u n-free, Nu≤X} N(σ,X^τ;(νχ_u)^*) ≪ X^(E+ε).           (7.1)

Here zeros are counted with multiplicity. The constants may depend on fixed K,S,n,σ,κ,ε,A; no uniformity as these data vary is asserted. The statement at the joining point δ=1−1/n is not claimed for positive κ by this argument.

The proof modifies §2 as follows. The primitive product conductor divides the product of the two conductors, and the radical of the original product's deleted Euler factors is `≪X^(1+κ)`. This includes good primes where the local characters cancel on inertia: the primitive product may be unramified there even though the original presentation still has a zero mask. Fixed-field Hecke functional equations, strip growth and zero counts are uniform as the finite conductor varies and the archimedean parameters range in A. The same buffered logarithmic control therefore applies; the reflected bound has conductor exponent `(1+κ)(a−1/2)` up to arbitrarily small fixed losses. Saturation yields

    r≤t,     r+m≥t,     m≤(1+κ)/2                              (7.2)

with the same two squared witness thresholds as in (2.2). A pure norm inducing character, which can have a shifted principal pole, is excluded from the contour argument. For a fixed common ν there is at most one such n-free label: at each good prime its required inertia fixes the exponent of u uniquely, while a prime where ν is unramified must have exponent zero. Its individual zero count is absorbed.

The Θ_n source is used with the same fixed S: ν(a) is simply a common coefficient multiplier of modulus at most one, with its conductor zeros retained. This remains true after convolving two or four ordinary blocks, after `a=a₁v²`, and for all fixed Sobolev derivatives. The inverse case r≥L has exponent at most R. In the middle range, if r<L=2t/3, (7.2) gives `L<2m≤1+κ`; convexity of f bounds the ordinary fourth-moment exponent by the maximum of f(L) and f(1+κ). In the high range, if r<L=4t/5, (7.2) gives `L<4m≤2(1+κ)`; convexity and `f(x)=hx` for x≥2 give the second expression in (7.0). Fixed preliminary detector losses are absorbed into ε. In particular E=R if `κ<t−1` in the middle range or `κ<t/2−1=(1−nh)/(4+nh)` in the high range. A full source-qualified argument and independent review are recorded in [the moving-twist note](../exploratory/2026-10-29-moving-unitary-twist-density/README.md).

The high-range argument also permits any fixed integer k≥2 with `k≥4−5nh`. Set

    t_k=2(k+1)/(k+nh),   L_k=2k/(k+nh),   R_k=h t_k,
    E_k=h max{t_k, k(1+κ)/2}.                                  (7.2a)

Then (7.1) holds with E replaced by E_k. Here `t_k≤5/2`, `L_k≥1`, and `f(x)≤R_k` on `[L_k,t_k]`. For r<L_k, the 2k-th ordinary moment has `L_k<km≤k(1+κ)/2`; if its upper endpoint is below L_k, that witness case is empty. If the endpoint is at least t_k, then `f(x)=hx` for x≥t_k, which gives (7.2a). The k-fold convolution has divisor-bounded coefficients and the same squarefree-kernel masks; k is fixed before the profile orders and height power are chosen. Thus one may take the best bound among finitely many fixed k choices. For n=3 at θ and κ=1/10, k=3 gives `E_3=5045224/9391959≈0.53718548`, improving the k=4 moving-twist exponent at that κ.

There is a further per-twist extension with growing archimedean type. Suppose the full archimedean analytic conductor of the common unitary ν at height zero is at most `X^λ`, with λ≥0 fixed, and retain `Nf_ν≤X^κ`. Under conductor-uniform Hecke functional-equation, gamma-ratio, buffered reciprocal and zero-count estimates, the preceding per-ν bounds remain valid with κ replaced by `q=κ+λ` in (7.0) and (7.2a). The full gamma conductor counts each local degree, so `C∞(ν,it)≪C∞(ν)(1+|t|)^[K:Q]`; this is the input for the witness ceiling `m≤(1+q)/2` up to fixed losses. The one possible pure-norm row can have a pole shifted to polynomial height; its zeros are bounded uniformly by a local zero count in an interval of length O(X^τ), rather than by a global count up to the shift. For example, n=4, σ=4/5, κ=1/20 and λ=1/10 have q=3/20<2/13 and retain E=35/52. This assertion is uniform for one common ν per X; it does not license a union bound over a continuum of archimedean twists. See [the growing-infinity proof](../exploratory/2026-10-29-moving-unitary-twist-density/EXPANDED-INFINITY.md) for its source assumptions and independent review.

For finite-order twists this gives a simultaneous row statement. The number of primitive finite-order Hecke characters with conductor norm ≤Q is `≪_K Q²`: the narrow ray class group for modulus f has order `≪_K Nf`, and there are `O_K(Q)` ideals of norm ≤Q. Their archimedean types form a fixed finite set. If `E+2κ<1`, the uniformity of (7.1) and a union bound show that all but

    O(X^(E+2κ+ε))                                               (7.3)

of the good n-free labels Nu≤X have **every** finite-order twist ν with `Nf_ν≤X^κ` zero-free in `Re s≥σ, |Im s|≤X^τ`, after primitive induction. The at-most-one pole-bearing row for each twist is included in the uniform estimate. For example, n=4, σ=4/5 and κ=1/10 satisfy `κ<2/13`, and (7.3) gives exponent `35/52+1/5=227/260<1`. At n=3, θ and κ=1/10 the k=3 bound in (7.2a) gives the union exponent `34618079/46959795≈0.73718548`. This is a finite-height simultaneous family statement; it is not an individual all-height strip. The de Faveri comparison in §5 remains the untwisted comparison, and §6 uses ν=1.

The last cubic example does not improve every published broad-family comparison. Over a fixed Galois base K, [Khale et al., Lemma 3.3](https://arxiv.org/abs/2008.09677v3), together with the FHL tame-inertia identification, yields the smaller exponent `32118079/43693470≈0.735077` for all finite-order twists at κ=1/10, after choosing τ sufficiently small. For each primitive product character ψ, at most `X^(κ+ε)` pairs `(u,ν)` occur: outside the conductor of ν, the local inertia of ψ determines each good exponent of u; on its support there are at most three choices per prime, and the possible conductor ideals sum to `X^(κ+ε)`. A principal ψ is treated separately by an individual zero count. The sharper comparison depends on the cited Galois-field, finite-order and height hypotheses and does not cover arbitrary unitary infinity types.
