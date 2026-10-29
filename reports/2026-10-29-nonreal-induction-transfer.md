# Nonreal induction and explicit Artin zero-free regions

**Status:** Proposed, partly independently checked; the imported Hecke zero-free theorem and global proof remain to be independently reviewed.  
**Scope:** Finite Galois extensions of number fields, indicated virtual representation identities, Artin L-functions. No Artin holomorphy conjecture.  
**Novelty:** No priority claim: Brauer induction, character identities, Hecke bounds, and conductor-discriminant arguments are classical. We have not exhaustively searched the resulting quantitative region for these families. A later preprint claims a much stronger fixed half-plane for all finite-order Hecke L-functions; its analytic inputs have not been audited here.  
**What was run:** The PSL₂(7) induced characters below were independently computed from GL(3,2) by `reports/2026-10-29-gl32-check.py`; this check addresses only finite group character computations, not number-field inputs.  
**Smallest remaining gap:** Independent mathematical review of the conductor bound, all ramified local factors, Hecke theorem hypotheses, and a prior-art comparison.

Let K/k be a finite Galois extension of number fields, dK its absolute discriminant over Q, and G its Galois group. Assume dK>1. Let ρ be a virtual character with an integer decomposition

    ρ = Σ_j a_j Ind_{H_j}^G χ_j,     a_j ∈ Z,              (1)

where every χ_j is a one-dimensional character of order m_j≥3. Write N_j=ker χ_j, and define

    E = max_j 1/[ |N_j| φ(m_j) ].

Then the meromorphically continued Artin L-function L(s,ρ) is holomorphic and nonzero in

    Re(s) > 1 − 1/[15.10 E log dK],
    |Im(s)| < (1/3) tan(π/8).                            (2)

For any nonreal χ, φ(m)≥2, so E≤1/2 and the weaker universal denominator 7.55 log dK always works. More precisely one can retain each conductor individually: with F_j=K^{H_j} and Q_j the norm of χ_j's finite conductor, intersect the zero-free regions with denominator 15.10 log(d_{F_j} Q_j). The virtual ρ need not be irreducible or an actual representation. The nonreal condition applies to the *inducing characters*, not to ρ.

**Proof.** By Artin induction and class field theory, the induced L-function of χ_j equals the primitive Hecke L-function of the corresponding finite-order idele character over F_j, including ramified finite factors. Every χ_j is nontrivial, so these Hecke L-functions are entire. The published Ahn–Kwon theorem, [J. Number Theory 145 (2014), 433–473](https://doi.org/10.1016/j.jnt.2014.06.008), proves zero-freeness for order≥3 primitive Hecke characters on Re(s)>1−1/(15.10 log(d_F Q)) and the stated height range. It therefore suffices to bound the conductors.

For fixed H and χ write N=kerχ, m=ordχ, F=K^H and M=K^N. The extension M/F is cyclic of degree m. Every power χ^a with gcd(a,m)=1 has exactly the same conductor as χ: locally the corresponding one-dimensional Galois characters have the same kernels on all ramification groups. By the conductor-discriminant formula, all other finite-conductor contributions being at least one,

    dM ≥ dF^m Q^φ(m).

The discriminant tower gives dK≥dM^|N|. Since m≥φ(m), it follows that

    dK ≥ (dF Q)^{|N|φ(m)}.                             (3)

Thus each Hecke factor is holomorphic and nonzero in (2). The identity (1), Artin formalism, and analytic continuation turn L(s,ρ) into an integer product and quotient of these factors; the reciprocal of a holomorphic nonvanishing function is holomorphic. This proves the claim, including s=1. □

## PSL₂(7) and all abelian twists

Let K/k have group PSL₂(7)×B, where k is a number field and B is any finite abelian group. Let 6 and 8 be the irreducibles of PSL₂(7) of those dimensions, and let μ be any character of B. Fix subgroups H≅C7⋊C3 and J≅A4, with order-three characters λ of H/C7 and ω of J/V4. Their induced characters satisfy

    Ind_H λ=8,    Ind_J ω=6+8.                          (4)

For verification, in the ordered classes with (size, element order) equal to (1,1), (21,2), (56,3), (42,4), (24,7), (24,7), the character table has

    6 = [6,2,0,0,-1,-1],   8 = [8,0,-1,0,1,1].

The independently computed induced characters are [8,0,-1,0,1,1] and [14,2,-1,0,0,0], respectively. The finite-group check was run by the coordinating agent using the script named in the header.

Tensoring (4) with μ and using induction compatibility gives expressions of 8⊗μ and 6⊗μ using λ⊗μ on H×B and ω⊗μ on J×B. These inducing characters remain nonreal because their restrictions to H×{1} and J×{1} have order three. Their kernels contain C7×{1} and V4×{1}, respectively. Thus (3) gives E≤1/14 for 8⊗μ and E≤1/8 for 6⊗μ. The respective zero-and-pole-free regions are

    Re(s)>1−1/[(15.10/14) log dK]   (dimension 8),
    Re(s)>1−1/[(15.10/8) log dK]    (dimension 6),
    |Im(s)|<(1/3)tan(π/8).                            (5)

The constants hold for every finite abelian B and every μ, without assuming coprimality of conductors. They are a comparison to the stated Ahn–Kwon input, not a proof that (5) is the best existing region.

## A5 and all abelian twists

If G=A5×B, the A5 relations in [the A5 note](2026-10-29-a5-hecke-transfer.md) can be twisted by any one-dimensional μ of B. All inducing characters remain nonreal on restriction to the A5 subgroup. The representations 3⊗μ, 3′⊗μ, and 4⊗μ have (2) with E≤1/2, hence denominator 7.55 log dK. For 5⊗μ, the single inducing character on A4×B kills V4×{1}, giving E≤1/8 and denominator (15.10/8) log dK. Here K is the full A5×B extension; using the actual field and conductor in (2) can be considerably sharper than its discriminant.

A fixed half-plane claimed in [Liu 2026](https://arxiv.org/abs/2610.26835) would dominate these logarithmic regions if verified, but is not used as an input here. This note establishes no zero-free region for ζ itself.

## Candidate: all nontrivial PSL₂(7) representations over Q

**Review status:** This additional argument uses Stark's low-order theorem and a Dedekind zero-free region as well as (2); it awaits independent review. It applies to G=PSL₂(7), without the abelian twists above.

Let K/Q be Galois with G=PSL₂(7). For each nontrivial irreducible representation ρ, the proposed conclusion is holomorphy and nonvanishing in

    Re(s)>1−1/[(15.10/6) log dK],
    |Im(s)|<(1/3)tan(π/8).                            (6)

In addition to 1, 6 and 8, the irreducibles have dimensions 3, 3, 7; label the three-dimensional characters 3 and 3′. Let λ be a primitive character of a subgroup C7. Its six nontrivial powers form two normalizer orbits, each of size three. Label them so that

    Ind_C7 λ=3+6+7+8,
    Ind_C7 λ³=3′+6+7+8.                               (7)

This follows by restricting to C7: the eigencharacters of 3 are λ,λ²,λ⁴; those of 3′ are λ³,λ⁵,λ⁶; 6 contains each nontrivial character once; 7 contains all characters once; 8 contains the trivial character twice and each nontrivial character once. Since ker λ=1 and φ(7)=6, the conductor estimate (3) and Ahn–Kwon make the two induced Hecke L-functions holomorphic and nonzero in (6). Equation (5) covers L6 and L8 there. Consequently the products L3 L7 and L3′ L7 are holomorphic and nonzero in (6), as meromorphic identities.

Let H=C7⋊C3 and M=K^H. The degree-eight permutation character is Ind_H 1=1+7, so L7=ζ_M/ζ. We have [K:M]=21 and therefore dM^21≤dK. The [Das–Gaba–Lee–Savalia–Wong theorem](https://arxiv.org/html/2506.19319), degree at least 7 case, says ζ_M has at most one zero in σ≥1−1/(11.51910 log dM), |t|≤1, and if present it is real and simple. This region contains (6), since 11.51910/21<15.10/6. The denominator ζ is nonzero there except for its simple pole at 1: for 0<|t|≤1 this follows from [Platt–Trudgian](https://doi.org/10.1112/blms.12460), because the region lies in σ>1/2; for t=0 and σ>0 it follows from the alternating-series formula; and σ>1 is covered by the Euler product. (The σ>1/2 claim follows already from dK≥3.) At s=1 the pole quotient is nonzero. Thus L7 is holomorphic in (6), and its only possible zero there is a simple real zero.

Suppose this exceptional real zero β occurs. The two zero-free products imply ordβ L3=ordβ L3′=−1; L6 and L8 have order zero, and ζ has order zero at β. The Galois zeta factorization gives

    ordβ ζ_K = 3(−1)+3(−1)+6(0)+7(1)+8(0)+0 = 1.

Stark's theorem says that at a simple zero of ζ_K every irreducible Artin L-function of K/Q is holomorphic; see the statement and discussion in [Lemke Oliver–Thorner–Zaman](https://rlemke01.math.tufts.edu/papers/27-ApproximateArtin.pdf). This contradicts the two poles. Thus L7 is nonzero throughout (6), and (7) then shows L3 and L3′ are holomorphic and nonzero there as well. No use is made of the unreviewed claimed fixed-half-plane preprints. The result is compared only with the named Dedekind/Stark route; no independent novelty assessment has been completed.

**Multiplicity source:** In applications of the Das et al. low-height result above, the exceptional zero is real and lies within distance 1/(A log d_M) of 1, with A>2. Its simplicity follows separately from the Ahn–Kwon result for ζ_M in the region Re(s)>1−1/(2 log d_M), |Im(s)|<1/(2 log d_M). The simplicity claim is not inferred from “at most one zero” without counting multiplicity.

## Low-order transfer criterion and arbitrary base field

The preceding multiplicity argument is a special case of the following exact criterion. Let G=Gal(K/k), and let Ω be a domain avoiding s=1. Suppose S₁,…,S_r are genuine characters induced from nonreal linear characters, their irreducible constituents together cover every nontrivial irreducible character of G, and

    reg_G − Ind_H^G 1 = Σ_i b_i S_i,  b_i∈Z.             (8)

Assume each L(s,S_i) is holomorphic and nonzero on Ω, and ζ_{K^H} has zero order at most one at every s∈Ω. Then all nontrivial irreducible Artin L-functions of K/k are holomorphic and nonzero on Ω. Indeed, (8) and Artin formalism show ζ_K/ζ_{K^H} is holomorphic and nonzero on Ω, so their zero orders coincide and are at most one. Stark gives holomorphy of each irreducible Artin L-function. The product L(s,S_i) is nonzero and is a product of these holomorphic constituents with nonnegative integer exponents. Every constituent appearing in some S_i is therefore nonzero. This gives (8)'s conclusion without assuming the base zeta function is nonvanishing.

For G=PSL₂(7), let A and B be the two C7-induced characters in (7), D=Ind_{7:3}ω=8, and P=Ind_{7:3}1=1+7. The exact identity

    reg_G − P = 3A + 3B + 2D                            (9)

is immediate from the irreducible dimensions. A, B, D cover every nontrivial irreducible; (9) even has nonnegative coefficients. Each associated Hecke L-function is holomorphic and nonzero in (6), now with K/k over an **arbitrary** number field k, since the kernel–φ proof uses the absolute discriminant dK. For M=K^{7:3}, [K:M]=21 and [M:Q]≥8. The Das et al. degree≥7 theorem and the separate Ahn–Kwon simplicity bound ensure ord ζ_M≤1 throughout (6) away from s=1, because 11.51910/21<15.10/6. At s=1, L7=ζ_M/ζ_k is the ratio of two simple zeta poles with positive residues, hence is holomorphic and nonzero; the Hecke products and the nonvanishing of L6 and L8 then show the same for L3 and L3′, while L6 and L8 are already covered. Therefore the conclusion (6) holds for all number-field bases k, with no hypothesis on zeros of ζ_k. This is a direct deduction from cited theorems, not a novelty claim.
