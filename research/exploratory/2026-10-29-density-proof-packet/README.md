# A source-conditional density-one zero-free rectangle for cubic Hecke families

**Status:** A consolidated proposed proof, conditional on the cited rectangular sieve and on the stated fixed-field detector and uniformity inputs. It has not been checked line by line as a complete proof and makes no priority claim. It is a zero-density result for a family, **not** an individual zero-free half-plane or a proof about the Riemann zeta function.

Fix a number field K containing μ₃, a fixed finite set S as in [De Faveri, arXiv:2610.04045v1](https://arxiv.org/abs/2610.04045v1), and a fixed unitary Hecke character ν with conductor supported on S. Let χ_g be the source cubic character indexed by a good cube-free ideal g, with its original zero extension, and let `N_g(σ,T)` count zeros with multiplicity of the **primitive** Hecke L-function inducing νχ_g in `Re s≥σ`, `|Im s|≤T`.

Assume De Faveri's Proposition 8.1 and finite-ray reciprocity with their stated uniformity. Assume also the standard fixed-field unitary Hecke continuation, functional equation, uniform polynomial strip bounds, individual zero counting, and the short saturated detector described and derived in §2 below, including its common-profile/height controls. The latter is a replay of [OpenAI Proposition 8.3](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) outside that proposition's printed parameter interval; it is an explicit input to the conditional result, not a claim that the source states it verbatim.

Under these inputs, for every fixed `1/2<σ<1` and ε>0 there is a τ>0 such that

    Σ_{g good cube-free, N cond(νχ_g)≤X} N_g(σ,X^τ)
       ≪_{K,S,ν,σ,ε} X^{R(σ)+ε},
    R(σ)=1−(2σ−1)/(2(3−2σ))=(7−6σ)/(6−4σ).             (1)

For example, `R(4/5)=11/14`. The number of distinct primitive characters in the family with conductor norm at most X is `≫X/log X`; hence all but a power-saving fraction have no zero in the displayed rectangle. The height power τ is positive but may depend on the fixed data and ε. Neither (1) nor its corollaries say that any one character is zero-free at all heights.

## 1. Two common-scale moments

Write g=a b² with a,b good squarefree and coprime. At every good prime dividing ab the cubic local character is ramified, and its fixed-S conductor factor is bounded. Thus the condition `N cond(νχ_g)≤X` implies `N(ab)≪ν X`, while the original deleted-factor radical and every primitive conductor are `Oν(X)`.

De Faveri Proposition 8.1 bounds, for arbitrary squarefree column coefficients and a,b in dyadic boxes, the kernel χ_q(a b²) by

    (ABQ)^ε [AB+M^(2/3)N^(1/3)Q+M^(1/3)N^(2/3)Q^(2/3)],

where M=min(A,B), N=max(A,B), and Q is the column length. Split the finite reciprocity ray class of g; in each class χ_g(q) differs from χ_q(g) by a fixed function of q. On noncoprime inputs both are zero. If AB≪X, the displayed bracket is `≪ X+sqrt(X) Q` up to a fixed factor: the Q term has `M^(2/3)N^(1/3)≤sqrt(MN)`, and the Q^(2/3) term is ≤X for `Q≤sqrt X` and ≤sqrt(X)Q otherwise. Summing O(log²X) dyadic boxes costs a subpower.

For a centrally normalized smooth inverse block of length D=X^r, Möbius support is squarefree and the column coefficient squared mass is `≪1`. Thus uniformly for common profiles and fixed reciprocity classes,

    Σ_g |M_r(g)|² ≪ X^ε [X+X^(1/2+r)].                  (2)

For a centrally normalized **plain** block S_m of length D=X^m≤X^(1/2+η), decompose each good ideal uniquely as q=q₁v² with q₁ squarefree. No coprimality of q₁,v is imposed. For fixed v the row multiplier χ_g(v²) has modulus ≤1 and is independent of q₁, so it may be dropped after taking the row norm. The inner q₁ coefficients have squared mass `≪(Nv)^(−2)` and length `≪D/(Nv)²`. Apply the preceding squarefree sieve and Minkowski, and use `Σ_(Nv≤C√D)(Nv)^(−1)≪log(2D)`. This gives

    Σ_g |S_m(g)|² ≪ X^(1+O(η)+ε).                         (3)

Fixed bad-prime factors are either excluded throughout or split into a convergent fixed-prime sum. A norm phase and fixed ν are row-independent inside each q₁ block; all zero masks are retained. The [Sobolev lemma](../2026-10-29-cubic-detector-sobolev/README.md) explains how finitely many derivatives and an `O(T)` factor turn these fixed-parameter bounds into the required rowwise-profile bounds. In particular, mere pointwise moment uniformity is not used as a substitute for a supremum estimate.

## 2. The short saturated detector input

For each fixed `t∈(1/2,1]`, sufficiently small fixed detector loss κ>0, and a sufficiently small height power chosen after the analytic orders, the detector supplies, for every row having a zero with Re ρ≥σ and `|Im ρ|≤X^τ`, a common bin a≥σ−O(κ), a common presentation, and two dyadic blocks satisfying

    r+m≥t−O(κ),  0≤r≤t+O(κ),  0≤m≤1/2+O(κ),
    |M_r|²≥X^{δr−O(κ)},  |S_m|²≥X^{δm−O(κ)},  δ=2a−1. (4)

The presentation and dyadic labels are chosen from fixed finite and logarithmic lists; the remaining real profile parameter and common twist height are handled by the Sobolev reduction. A possible principal or norm-character presentation occurs only in a bounded row and is counted separately. Deletion factors do not introduce zeros in Re s>0.

The source proof gives the following reason to expect (4) for `t<1`: choose a sentinel floor `a₀∈(1/2,σ)`, use nested zero maxima to obtain the buffered rectangle, and let D*=X^t. At the selected zero integrate the smoothly truncated inverse against `Y*^z Γ(z)L(ρ+z)`, with `Y*=X^B` and B chosen large enough for this fixed field's strip bounds. The single Gamma residue at zero vanishes. On the absolute line, Möbius convolution cancels all nonunit coefficients through D*, leaving a tail of magnitude ≫1. Dyadic and logarithmic-Fourier separation yield `r≤t+O(1/log X)`, `r+m≥t−O(1/log X)` and the product lower bound `|M_r S_m|²≫X^{δ(r+m)−κ}`. Buffered Mellin shifts and the functional equation give the individual upper bounds `|M_r|²≪X^{δr+κ}` and `|S_m|²≪X^{δ min(m,1−m)+κ}`. Since δ has a fixed positive lower bound, comparison forces `m≤1/2+O(κ)` and then both individual lower bounds in (4). For the finite-height joins, every introduced frequency is charged to one cumulative buffer, and the external tail order is selected only after the internal profile orders and τ.

The detailed [fixed-field replay](../2026-10-29-fixed-field-saturated-detector/README.md), [lowered-floor audit](../2026-10-29-detector-floor-extension/README.md) and [short-cutoff review](../2026-10-29-short-cubic-conductor-detector/INDEPENDENT-REVIEW.md) identify the nontrivial imported strip, Mellin, uniformity and mask assertions. They do not independently verify the whole cited analytic literature.

## 3. Counting the witnesses

Set δ₀=2σ−1>0 and choose `t=1/(2−δ₀)=1/(3−2σ)`, which lies in (1/2,1). After binning, grouping the logarithmically many lengths and applying (2) and (3) to common differentiated profiles, Chebyshev gives the two row-count exponents

    max(1,1/2+r)−δ₀r,       1−δ₀m,

up to arbitrarily small fixed losses. Since m≥t−r−O(κ), their minimum is at most

    min{max(1,1/2+r)−δ₀r, 1−δ₀(t−r)}.

For r≤1/2 this is at most `1−δ₀ max(r,t−r)≤1−δ₀t/2`. For r≥1/2 it is at most `1/2+(1−δ₀)t`. The choice of t equates these bounds, giving `R(σ)=1−δ₀/[2(2−δ₀)]`. The O(κ) and small m-overflow losses are fixed below ε before X grows. The standard individual Hecke zero-count bound costs a fixed polynomial in X^τ and logarithms; choose τ afterward so all height and Sobolev factors fit into ε. This proves (1) from the stated detector and sieve inputs. □

## 4. Consequences and comparison

For ν=1, every nontrivial cubic χ_g cuts out a cyclic cubic extension L/K and Artin factorization gives `ζ_L/ζ_K=L(s,χ_g)L(s,conjugate(χ_g))`. Thus the same exceptional-count bound applies to fields in this constructed family, with at most two character labels per extension. The relative discriminant is `f_g²`, so under absolute-discriminant ordering the exceptional exponent is `R(σ)/2`; at `σ=4/5` it is `11/28`. This concerns the quotient, not the base zeta factor or an individual L/K.

For K imaginary quadratic, finite χ_g not fixed by complex conjugation induce irreducible odd dihedral Artin representations over Q and weight-one theta forms, with conductor `|D_K|Nf_g`. Split-prime labels give `≫X/log X` distinct forms up to the two possible inducing characters. The same conditional exceptional exponent therefore gives density-one zero-free rectangles for this degree-two family. The [dihedral note](../2026-10-29-dihedral-density/README.md) records the extension to suitable CM quadratic fields and its independent internal review.

The cited cubic sieve is a recent preprint and has not been independently proved here. A targeted comparison with [Khale et al., Lemma 3.3](https://arxiv.org/abs/2008.09677v3), and the named cubic sources is recorded in [the conductor-detector note](../2026-10-29-cubic-conductor-detector/README.md). In the fixed-Galois finite-order comparison at small height, the displayed exponent (1) is smaller near σ=4/5; the broader prior bound becomes smaller above `(47−sqrt(97))/44≈0.84434`. This is not an exhaustive literature or priority assessment. For n>3, a [separately proposed general-order sieve](../2026-10-29-conjugate-conductor-sieve/README.md) would yield (1) for the restricted `a b^(n−1)` family, but the full n-th-power-free family is not covered by that extension.
