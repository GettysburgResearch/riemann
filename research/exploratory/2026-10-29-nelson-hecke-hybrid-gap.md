# Nelson's cube-free Weyl bound and the remaining hybrid gap

**Status.** Source comparison and a conditional exponent calculation; no stronger hybrid estimate or zero-free region is proved here.

Paul Nelson, [*Eisenstein series and the cubic moment for PGL(2)*, arXiv:1911.06310v3, Theorem 1.6](https://arxiv.org/abs/1911.06310v3), states that for a fixed number field F and a unitary Hecke character χ with **trivial infinite component** and **cube-free entire finite conductor**,

    |L_F(1/2,χ)| ≪_(F,ε) C(χ)^(1/6+ε).                       (1)

This includes finite-order cubic or sextic characters with arbitrary composite squarefree full conductor, and is stronger than the 3/16 Burgess target at the central point. Here C is analytic conductor; because the infinite component is trivial it is the arithmetic conductor norm times a fixed field factor. The printed theorem does not state a growing-t bound for the original nonquadratic character, nor does it cover an arbitrary angular infinite component. Its proof in §4.2 chooses an archimedean test majorizing the unitary spectral range `|t|≤1`; deriving polynomially uniform large-t tests is an additional source replay, not a stated conclusion.

Nelson's Theorem 1.1 separately treats **quadratic** χ over arbitrary F, with no cube-free restriction. It bounds the quadratic twist of a fixed cuspidal or unitary Eisenstein representation with polynomial dependence on the representation's conductor. Varying the Eisenstein parameter gives

    |L_F(1/2+it,χ)| ≪_(F,ε) C_fin(χ)^(1/6+ε)(1+|t|)^A, (2)

for some fixed A; Nelson's Corollary 1.3 explicitly uses this polynomial-height consequence over Q(i). More generally, fix any unitary Hecke character ξ and take the unitary Eisenstein representation σ=Ind(ξ|·|^{it}, ξ^(−1)|·|^(−it)). Then the central L-function of σ⊗χ is |L_F(1/2+it,ξχ)|², and Theorem 1.1 gives the same exponent 1/6 with a fixed-ξ constant and polynomial t cost. The finite conductors of ξχ and χ are comparable up to factors depending only on ξ. In particular a **fixed** nonquadratic twist orbit of quadratic characters is covered, with no cube-free assumption. This does not provide (2) for a family in which the nonquadratic part of ξ itself has growing conductor: the polynomial dependence on C(σ) must then be paid.

Balkanova–Frolenkov–Wu, [arXiv:2108.12283v5](https://arxiv.org/abs/2108.12283v5), establish a cube-free hybrid Weyl result over **totally real** fields; Q(ω) is not in that class. Petrow–Young's [hybrid cube-free Weyl theorem](https://doi.org/10.4007/annals.2020.192.2.3) is for Dirichlet characters over Q. Han Wu's [2019 Theorem 1.1](https://doi.org/10.1112/S0010437X19007309) gives for general number fields and arbitrary unitary characters the hybrid exponent `103/512`, with no cube-free restriction. None of these statements, as cited, supplies the desired nonquadratic 1/6 hybrid over Q(ω) with arbitrary fixed wild S data.

For the Gram application, same-ray coprime squarefree quotient conductors are exactly the good product by De Faveri Lemma 2.4; such characters can meet (1). However, expanding a fixed source-row ray sector can introduce a fixed bad-prime character whose conductor has cube factors. One must check each actual primitive numerator after the sector expansion, not just the good conductor, before applying (1). Deleted Euler factors at primes in an imprimitive presentation contribute only subpower costs on Re s≥1/2+η, but deleting them does not make a ramified primitive conductor cube-free.

Suppose instead that a suitable source proves, for every primitive nonprincipal character ξ actually occurring after all fixed sector expansions,

    |L_F(1/2+it,ξ)| ≪_(F,S,ε) Q_ξ^(1/6+ε)(1+|t|)^A,     (3)

uniformly in ξ,t, including the finite S-local types present. Together with the usual interpolation, Mellin shift and finite-deletion bounds in [the moving-twist Gram note](2026-10-29-hecke-gram-subconvex.md), (3) would replace its off-diagonal bound by

    |⟨v_h,v_k⟩| ≪ P^(−1/2+ε) (R_h R_k)^(1/6+ε).

For radicals Rh,Rk≤H and O(H^(1+ε)) indexed profiles, the row sum is `≪P^(−1/2+ε)H^(4/3+ε)`. Thus Gershgorin conditions the whole radical-index family for `H≤P^(3/8−δ)`, instead of Wu's `H≤P^(128/359−δ)`. This is a conditional calculation, not an application of (1). It does not improve the separate projected-energy threshold `H≤P^(25/72−δ)`, which is already smaller, or the existing growing-rank witness range constrained by another moment error. It supplies no bound for the ambient spectral complement.

**Independent observation and review:** Amplified_opt identified the fixed-unitary-twist extension from Theorem 1.1; Literature and High_match checked the Eisenstein factorization, conjugation, conductor comparison and polynomial height dependence. This is a source-qualified deduction, not an independent proof of Nelson’s theorem.
