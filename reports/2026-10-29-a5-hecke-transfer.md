# A low-height A5 Artin zero-free region via nonreal Hecke characters

**Status:** Proposed proof; requires independent check of the character decompositions, conductor bookkeeping, imported analytic theorem, and prior art.  
**Scope:** Unconditional using the cited 2014 Hecke theorem; Galois extensions K/Q with group A5 and their nontrivial irreducible Artin L-functions. No Artin holomorphy conjecture is assumed.  
**Novelty:** The group identities and transfer may be known. This note records a concrete comparison to two named published results, not a worldwide priority or best-known claim. A later unreviewed 2026 preprint claims a much stronger fixed half-plane for all finite-order Hecke L-functions, which would imply a stronger A5 result if its analytic inputs are correct.  
**What was run:** Hand-derived finite group character and conductor calculations; no certified computation.  
**Smallest remaining gap:** Independent review and literature search for the exact A5 region, in particular other explicit Hecke bounds.

Let K/Q be finite Galois with G=A5 and absolute discriminant dK. For every nontrivial irreducible complex representation ρ of G, L(s,ρ) is holomorphic and nonzero on

    Re(s) > 1 − 1/(7.55 log dK),    |Im(s)| < (1/3) tan(π/8).      (1)

For the five-dimensional irreducible, one can replace 7.55 by **1.8875** in (1), at the same heights. The statement includes s=1. It is a zero-and-pole-free region, not an assertion of holomorphy elsewhere. The inherited strict inequalities are intentional.

## Proof

Use the nontrivial characters of the cyclic subgroups C5, C3 and of the quotient A4/V4≅C3. Choose λ of order 5 on C5; ψ of order 3 on C3; and ω of order 3 on A4. Define the induced characters

    A=Ind_C5^G λ,   B=Ind_C5^G λ²,
    C=Ind_C3^G ψ,   D=Ind_A4^G ω.

Label the irreducibles 1, 3, 3′, 4, 5 so that 3 restricted to C5 contains λ and λ⁻¹. Frobenius reciprocity and the ordinary A5 character table give

    A=3+4+5,   B=3′+4+5,
    C=3+3′+4+2·5,   D=5.

Indeed, on C5 the restrictions of 3 and 3′ are respectively 1+λ+λ⁻¹ and 1+λ²+λ⁻², while those of 4 and 5 are Σ_{j=1}^4 λ^j and Σ_{j=0}^4 λ^j. On C3 their restrictions are 1+ψ+ψ⁻¹ for both 3 and 3′, 2+ψ+ψ⁻¹ for 4, and 1+2ψ+2ψ⁻¹ for 5. Finally, taking the inner product with ω on A4 gives multiplicity one in 5 and zero in the other irreducibles. Consequently, in the integer representation ring,

    3=C−B−D,  3′=C−A−D,  4=A+B−C,  5=D.       (2)

By Artin induction and class field theory, the L-functions of A, B, C and D are primitive finite-order Hecke L-functions of order 5, 5, 3 and 3, over F5=K^C5, F3=K^C3, and F12=K^A4 respectively. (The subscript is the order of the subgroup, not the field degree.) There are no missing finite Euler factors when the primitive Hecke characters are attached to the corresponding one-dimensional Artin representations. In particular, these four Hecke L-functions are entire, since their characters are nontrivial.

For a prime-degree cyclic extension M/F of degree p=3 or 5 and a nontrivial character χ of its Galois group, all p−1 nontrivial characters have the same conductor fχ. The conductor-discriminant formula and the discriminant tower formula give

    dM = dF^p (N_F/Q fχ)^(p−1),
    Aχ := dF N_F/Q fχ = (dM/dF)^(1/(p−1)).       (3)

For A and B take M=K and F=F5, so Aχ≤dK^(1/4). For C take M=K and F=F3, so Aχ≤dK^(1/2). For D take M=K^V4 and F=F12; then [K:M]=4 and dM^4≤dK, so Aχ≤dK^(1/8). All these Aχ>1 because their base fields have degree >1.

Ahn and Kwon, [Some explicit zero-free regions for Hecke L-functions](https://doi.org/10.1016/j.jnt.2014.06.008), prove for a primitive character of order at least 3 that L(s,χ) has no zeros when

    Re(s)>1−1/(15.10 log Aχ),    |Im(s)|<(1/3)tan(π/8).     (4)

Their result applies to the four Hecke factors. Since Aχ≤dK^(1/2), (4) covers (1). For the five-dimensional representation D alone occurs, and A_D≤dK^(1/8) strengthens the denominator to 15.10/8=1.8875. Each factor is entire and nonzero there, so all integer products and quotients in (2) are holomorphic and nonzero there, including at s=1. Artin formalism establishes equality by analytic continuation from Re(s)>1. This proves (1).

## Comparison and boundaries

Theorem 1.2 of [Das–Gaba–Lee–Savalia–Wong (2026)](https://arxiv.org/html/2506.19319) gives at most one simple real zero of ζ_K when Re(s)>1−1/(11.51910 log dK), |Im(s)|≤1, for [K:Q]=60. Stark's low-order theorem then makes all nontrivial A5 Artin L-functions holomorphic and nonzero on that region: the only possible zero can belong to a one-dimensional character, and A5 has only the trivial one. For |Im(s)| below (1/3)tan(π/8), (1) is 11.51910/7.55≈1.526 times as wide measured by 1−Re(s). This compares only to that named uniform bound. Ahn–Kwon's ζ_K bound with constant 2, transferred by Stark, is stronger for the three- and four-dimensional cases at the smaller heights |Im(s)|<1/(2 log dK); the five-dimensional denominator 1.8875 is smaller even there. Take unions of the applicable regions. More refined published Hecke constants or field-specific estimates may improve (1).

[B. Liu, 2026](https://arxiv.org/abs/2610.26835) claims the much wider uniform half-plane Re(s)>0.874886647… for finite-order Hecke L-functions of all number fields; combined with (2), it would dominate (1) for A5 fields. That preprint builds on other recent claimed analytic estimates and has not been audited here; neither it nor the claimed fixed half-plane is used in the proof above. The assertion of a fixed half-plane must not be described as established on the basis of this comparison alone.

## Candidate asymptotic fixed-height refinement

The following transfer uses a stronger cited theorem but has a non-numerical threshold, so it does not replace (1) as an explicit bound for every field. It also awaits independent review.

Fix T≥1 and put ν(x)=4+log(x+4). For sufficiently large dK, with the threshold depending on T, every nontrivial irreducible A5 Artin L-function is holomorphic and nonzero in

    Re(s) ≥ 1 − 0.1227 / [(3/8) log dK + 20ν(20)],   |Im(s)|≤T.   (5)

The analytic input is [Zaman, thesis, Theorem 4.1.1](https://www.math.toronto.edu/zaman/files/thesis.pdf): for a congruence subgroup with conductor maximum Q, degree n and discriminant dF, the product of characters of order at least 2 has at most one zero in the fixed-height rectangle with width 0.1227/(log dF+(3/4)log Q+nν(n)); that zero, if present, belongs to a real character. The size condition dF Q n^n sufficiently large is essential. A cyclic order-3 or order-5 extension M/F supplies a congruence subgroup with character group of that same odd prime order and Q=N fχ. Its nontrivial characters are nonreal; thus there is no exceptional zero. This applies to all factors A, B, C and D.

For each such extension write L=log dK. Formula (3) gives log Q=(log dM−p log dF)/(p−1). For C, p=3, M=K and n=20, so its Zaman denominator is (3/8)L−(1/8)log dF+20ν(20) ≤ (3/8)L+20ν(20). For A and B, p=5, M=K and n=12; the denominator is (3/16)L+(1/16)log dF+12ν(12) ≤ (1/5)L+12ν(12), because dF^5≤dK. For D, p=3 and n=5, and dM^4≤dK, giving denominator ≤(3/32)L+5ν(5). Hence the denominator displayed in (5) dominates all four, and the conclusion follows from (2).

As dK→∞ all three Zaman size parameters tend to infinity: for C and A/B this follows directly from dK=dF^p Q^(p−1); for D, M=K^V4 has trivial normal core in A5 and therefore normal closure K, so Hermite's finiteness theorem makes dM tend to infinity with dK, and dM=dF^3 Q². This gives a sufficient threshold without specifying its numerical value. The asymptotic coefficient of log dK in the reciprocal width is (3/8)/0.1227≈3.05624. It is a comparison to the named 11.51910 ζ_K bound, not an assertion that no stronger direct Artin result exists.

## A stronger nonreal comparison for the four-dimensional member

Let M=K^A4, so [M:Q]=5 and Ind_A4^G 1=1+4. Artin formalism yields L(s,4)=ζ_M(s)/ζ(s). Theorem 1.2 of Das et al. gives at most one simple real ζ_M zero when σ≥1−1/(13.71235 log dM), |t|≤1. By the tower formula dM^12≤dK, so for nonreal s the same theorem gives nonvanishing in the larger-looking dK region

    σ≥1−1/[(13.71235/12) log dK],   0<|t|≤1.       (6)

The quotient is holomorphic there too: the denominator ζ(s) has no zero in this rectangle. One way to justify this is the published [Platt–Trudgian partial RH verification](https://doi.org/10.1112/blms.12460), since the displayed real part is strictly greater than 1/2 (dM≥2), along with the usual Euler product for σ>1. At s=1 the pole ratio extends to a nonzero value. At real points away from s=1, ζ(s) is nonzero for σ>0, while ζ_M(s) may have the theorem's one exceptional real zero. Thus this comparison cannot remove the real exception on the wider strip; combine it with (1), which has no exception at smaller height. The permutation identity is classical, and (6) is recorded only to avoid overstating the novelty or strength of the common 7.55 bound. The source theorem also requires its exact stated boundary conventions; (6) may be taken strictly inside the displayed boundary if desired.

## A full-height-one region for the five-dimensional member

Let M=K^V4 and F=K^A4, so M/F is cyclic cubic and [M:Q]=15. Its two nontrivial Hecke characters are complex conjugates but induce the same irreducible character 5 of A5. Artin formalism gives the exact identity

    ζ_M(s)=ζ_F(s) L(s,5)^2.

Theorem 1.2 of Das et al. bounds ζ_M by at most one simple real zero when σ≥1−1/(11.51910 log dM), |t|≤1. Away from s=1, ζ_F is holomorphic and L(s,5) is entire, so a zero of L(s,5) forces a zero of ζ_M of multiplicity at least two. Thus it has no zeros in this region. At s=1 it is nonzero by the classical nonvanishing of nontrivial Hecke L-functions. Since dM^4≤dK, the five-dimensional member is holomorphic and nonzero in the explicit region

    σ≥1−1/(2.879775 log dK),   |t|≤1.                (7)

This yields a larger height range than the 1.8875-denominator result above but a narrower width; retain their union. The cyclic factorization is classical and the transfer is included as a named comparison, without claiming priority.

**Multiplicity source:** In applications of the Das et al. low-height result above, the exceptional zero is real and lies within distance 1/(A log d_M) of 1, with A>2. Its simplicity follows separately from the Ahn–Kwon result for ζ_M in the region Re(s)>1−1/(2 log d_M), |Im(s)|<1/(2 log d_M). The simplicity claim is not inferred from “at most one zero” without counting multiplicity.
