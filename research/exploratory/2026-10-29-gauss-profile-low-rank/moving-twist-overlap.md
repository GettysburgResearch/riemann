# Polynomially many low-conductor Gauss profiles

**Status.** This is a source-qualified deduction from the explicit completed reflection in OpenAI's [quasi-RH draft, Proposition 5.1 and (5.18)–(5.19)](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), the cited sextic large sieve, [Han Wu's uniform GL(1) subconvexity theorem](https://arxiv.org/abs/1604.08551), and standard Hecke analytic continuation. It controls the projection of a smooth Möbius vector onto certain explicitly chosen coefficient vectors. It does not identify those vectors with the exceptional eigenspace, control the complementary operator, or prove a zero-free region. The source reflection itself is imported, not independently proved here.

Fix the Eisenstein field and the source's primary convention. Let S contain the fixed bad primes and finite-ray data. Let W,V be fixed smooth compactly supported functions on (0,∞), with V nonzero, and fix a nonempty good finite-ray sector C. For each good sixth-power-free primary h, write R_h=max(1,N rad(h)), and define on good squarefree primary s in C, with Ns in the supports of W,V,

    m_P(s) = P^(−1/2) μ(s)ν(s) W(Ns/P)(Ns/P)^(−it),
    v_(P,h)(s) = P^(−1/2) γ₁(s) χ_s(h) V(Ns/P)(Ns/P)^(−1/2).

Here ν is a fixed finite-ray character, χ_s(h) retains the zero at (s,h)>1, and γ₁ is the source's unit normalized sextic Gauss sum. The scalar-product orientation may conjugate both sides. For every ε>0 there is A, independent of h,P,t, such that

    |⟨m_P,v_(P,h)⟩| ≪ P^(−1/2+ε) R_h^(1/2+ε) (1+|t|)^A.       (1)

All implied constants may depend on ε,S,C,W,V,ν, but not h,P,t. Sixth-power-freeness is only needed below for separation; (1) itself holds for arbitrary good h after keeping its zero mask.

## Uniformity in the reflection

Expand the fixed sector and the source's finite-ray phase from (4.7) into the finite ray-character basis. Reciprocity, including noncoprime zeros, expresses each summand in (1) as a sum of γ₂(s) ᾱ(s) Ψ_h(s), where

    Ψ_h = Ψ₀ ∏_(p|h) χ_p^(j_p),       j_p in {0,…,5}.

The zeroth power in the source retains the p-zero. The number of possible Ψ₀ and their moduli are fixed independently of h. Write D(z,Ψ_h) and T(z,Ψ_h)=L₀(z,Ψ_h)D(z,Ψ_h) as in Proposition 5.1. Choose 0<η<1/12. The direct series gives T(1+η+it,Ψ_h) ≪_η 1 uniformly in h and t.

On Re z=−η, (5.18)–(5.19), after the finite local Fourier calculation of Proposition 5.1, give

    |T(−η+it,Ψ_h)| ≪_(η,ε,S) 4^ω(h) R_h^(1+2η+ε) (1+|t|)^(2+4η).  (2)

Indeed, the reflected sum has at most O_S(4^ω(h)) terms; each has c=c_F r with Nc≪_S R_h, and its scalar is bounded. Use the explicit support and size bound (5.2) for the fixed cusp functions: µ=uλ^k n b³, k≥−4, n squarefree, and |d(µ)|≪3^(k/6)|b|. The Euler majorant of the reflected series at Re(1−z)=1+η has, at a good prime p of norm q, independent exponents e∈{0,1} in n and t≥0 in b, with weight q^[t/2−(1+η)(e+3t)]. This permits n and b to share primes.

For an active source exponent j=4, B_p(λ⁴µ)=q^(−1/2)(−1+q 1_(p|µ)). Its weighted absolute local sum is O_η(q^(−1/2)): the contribution with e+3t=0 is q^(−1/2), while the remaining contribution is bounded by q^(1/2) O_η(q^(−1−η)). For j=0 the absolute factor is at most q^(−1/2); for all other j it is at most one. Consequently the whole cusp-series majorant, including all active B_p, is ≪_(η,ε,S) R_h^ε: the ordinary good-prime factors are absolutely convergent and any fixed constants per active prime cost at most C^ω(h)≪_ε R_h^ε. The fixed additive cusp character and unit phases have modulus at most one. This improves the crude pointwise product bound R_h^(1/2). The conductor factor contributes (Nc)^(1+2η), and Stirling gives the indicated gamma-quotient growth, with exponential factors cancelling.

The source proves T entire and, for each h separately, sufficient strip growth to apply the maximum principle to T(z)(B+z)^(−N)exp(a z²), with fixed B,N and a↓0. The boundary estimates above are uniform in h, so the resulting bound is uniform even though the preliminary growth constant may depend on h. At Re z=1/2+η, interpolation gives

    T(1/2+η+it,Ψ_h) ≪_(η,ε,S) R_h^(1/2+ε) (1+|t|)^A      (3)

for some A independent of h. (The interpolation weight of the left boundary is 1/[2(1+2η)], giving the exponent 1/2; the divisor bound absorbs the remaining losses.) Since Re(3z−1/2)=1+3η, both L₀ and its reciprocal are bounded uniformly on this line by absolutely convergent Euler products, including the prime masks. Mellin inversion and the fixed annular profile then give the unnormalized sum O(P^(1/2+η)R_h^(1/2+ε)(1+|t|)^A), proving (1) after the two P^(−1/2) factors. Choose preliminary η and ε smaller than the displayed ε.

## A conditioned growing family

Let 1≤H≤P^(128/359−δ), with fixed δ>0, and choose distinct good sixth-power-free principal ideals (h) with N rad(h)≤H, one primary generator for each. With fixed C and V as above, their normalized coefficient vectors

    u_h = v_(P,h)/||v_(P,h)||₂

have Gram matrices with eigenvalues in [1−o(1),1+o(1)], uniformly for every such choice of h. This follows from the following elementary estimates. For h≠k,

    |⟨v_(P,h),v_(P,k)⟩| ≪_ε P^(−1/2+ε)(R_h R_k)^(103/512+ε),       (4)
    ||v_(P,h)||₂² ≫_ε H^(−ε).                                     (5)

For (4), use reciprocity and the fixed-ray partition to write the product χ_s(h) overline(χ_s(k)) as a bounded combination of nonprincipal finite-order Hecke characters χ, with the original masks at primes dividing hk. At a good prime where the exponents of the two sixth-power-free ideals differ, χ is ramified, hence nonprincipal even after a fixed S-ray twist; its conductor norm Q is O_S(N rad(hk)). The squarefree Dirichlet series is L(z,χ)/L(2z,χ²), times finite bad-prime factors and deletion factors. On Re z=1/2+η, the reciprocal denominator is uniformly absolutely convergent; the finite deletion factors are ≪_ε (R_h R_k)^ε. Han Wu's Theorem 1.1, with the admissible GL(2) Ramanujan exponent θ=7/64, gives L(1/2+it,χ)≪_ε [Q(1+|t|)²]^(103/512+ε) uniformly for primitive χ. Interpolating with the absolutely convergent line Re z=1+η gives L(z,χ)≪_(η,ε) Q^(103/512+ε)(1+|Im z|)^A on Re z=1/2+η, with A independent of h,k; imprimitive masks were already accounted for in the deletion factors. Shift the entire Mellin transform of the fixed annular profile to this line. The nonprincipal numerator has no pole, and its rapid decay absorbs the fixed height order, proving (4) after dividing by P. The deletion-factor estimate follows, for example, by taking the product over primes of (1−(Np)^(−1/2−η))^(−1) and absorbing it in an arbitrarily small power of the radical.

For (5), squarefree ideal counting in the fixed sector, with the primes of h deleted, has a positive main term with local factors Np/(Np+1); shifting the corresponding principal series to Re z=1/2+η gives normalized error O(P^(−1/2+ε)H^ε). The local product is ≫_ε H^(−ε). All sector and local constants are fixed; the estimated error is smaller than the main term in the stated range.

There are at most O_ε(H^(1+ε)) such sixth-power-free ideals: each squarefree radical d has at most 5^ω(d) choices of its exponents in {1,…,5}, and Σ_(Nd≤H)5^ω(d)≪_ε H^(1+ε). Their full norms can be as large as H^5. Consequently (4)–(5) and Gershgorin give an off-diagonal row sum ≪ P^(−1/2+ε)H^(359/256+ε)=o(1). The normalization accounts for the nonconstant deleted-prime density. No assertion is made that 128/359 is the optimal conductor exponent. Repeating each h with a fixed finite set of independent norm profiles requires the corresponding fixed profile Gram matrix to be nonsingular; the same off-diagonal estimate applies, and a fixed-dimensional block version gives conditioning after within-h orthonormalization.

Let V_(P,H) be their span. From (1), (5) and the Gram inverse,

    ||Proj_(V_(P,H)) m_P||₂² ≪ P^(−1+ε) H^(2+ε)(1+|t|)^A. (6)

This holds for any subset of the admissible h, including an empty subset. A finite fixed profile multiplicity only changes the constant. If t is allowed to grow, its cost must be included in the common height budget.

## Consequence for the projected source energy

Let T_(Y,P) be the full-row sextic matrix with source norm scale P and row norm scale Y, and use an independently established upper bound ||T_(Y,P)||². The row restriction to any subset can only decrease this norm. At P=Y^(6/5), the cited unrestricted-row large sieve gives

    ||T_(Y,P)||² ≪ Y^(41/30+ε).

With H=P^(25/72−δ), (6) yields

    ||T_(Y,P) Proj_(V_(P,H)) m_P||₂²
       ≪ Y^(1−(12/5)δ+ε)(1+|t|)^A.                        (7)

The exponent follows from 41/30+(6/5)(−1+25/36−2δ)=1−12δ/5, and 25/72<128/359. For sixth-power-free rows, the corresponding source bound is Y^(4/3+ε), giving 29/30−12δ/5. The stronger explicit bound Y^(29/30−12δ/5+ε) on all rows also holds for the smaller range H=P^(1/3−δ). These estimates apply to the projection alone, at the fixed coefficient and norm profiles displayed above. They do not bound the contribution of its orthogonal complement, nor do they justify discarding the cross term in the energy of the original vector. Prime-only coefficients, moving detector masks, and a uniform physical height budget require additional work.

## What the high-radical local factor does and does not show

For comparison, [Xu–Sang Proposition 3.1](https://arxiv.org/abs/2610.17675) treats a Gauss vector with **unrestricted** source moduli and a fixed nonnegative smooth profile. Write h=∏_(p|d)p^e_p with d=rad(h), 1≤e_p≤5, and D=Nd. In the source orientation its displayed main-term factor is

    Ω(d,e)=∏_(p|d) (Np)^(−j_p/6)/(1+(Np)^(−1))²,    j_p=6−e_p.

Thus Ω(d,e)≤D^(−1/6); conjugating the twist changes the exponents but preserves this upper bound. After translating the source's 1/P normalization to an ℓ²-unit-scale coefficient vector, its unrestricted-modulus norm formula has main term proportional to Y^(5/6)P^(1/3)Ω(d,e). At P=Y^(6/5), this is O(Y^(37/30)D^(−1/6)). The coarse local inequality alone forces this main term below Y only for D≥Y^(7/5); even at D=P it yields merely Y^(31/30). Some exponent patterns have stronger local decay, but no uniform stronger exponent follows from the displayed product.

This comparison is not a full norm bound: the source's error, after the same normalization, is O_ε((YPD)^ε[Y(1+Y^(7/60))+PD]) at this scale. Nor is the source's unrestricted-modulus formula automatically the squarefree-column matrix or a Gram decomposition for different h. Consequently neither this local factor nor (7) controls the complementary spectral space.

**Independent review.** Two researchers independently checked the original full-norm version; one of them independently checked the radical extension. The Hecke-convexity improvement and the averaged j=4 reflection factor have each subsequently been checked independently. The further Wu subconvexity extension has been submitted for independent review. Those reviews checked the local reflection factors and PL uniformity, the conductor and zero-mask bookkeeping in the Gram estimate, squarefree inversion and diagonal density, the Gershgorin range, fixed-profile blocks, and the two projected-energy exponents, conditional on the stated source and standard Hecke inputs; they do not supply complement control.
