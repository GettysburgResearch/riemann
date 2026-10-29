# Quartic and quintic density for nonabelian monomial Artin representations

**Status:** Source-dependent consequences of the [full quartic and quintic conductor-density estimates](../2026-10-29-quartic-quintic-conductor-summary/README.md), not new individual zero-free regions. The underlying estimates depend on the general-order rectangular-sieve replay, quadratic source matching when n=4, the fixed-field detector/profile replay and their cited analytic inputs. The Artin statements below additionally use standard class-field theory and Artin induction; the automorphic statements use cyclic automorphic induction. Those inputs are not independently proved here, and no priority claim is made.

Take either

    n=4,  K=Q(i),       d=[K:Q]=2,  |D_K|=4,   R=13/15;
    n=5,  K=Q(ζ₅),      d=[K:Q]=4,  |D_K|=125, R=19/20.

In the source family, take ν=1 and let χ_g be a **primitive finite-order character of exact order n** coming from a good n-free ideal label g. Retain the labels whose orbit under `Gal(K/Q)` has d distinct members. To each χ_g attach

    ρ_g = Ind_(W_K)^(W_Q) χ_g.

It is an irreducible d-dimensional finite-image monomial Artin representation, and its image is nonabelian. Standard cyclic automorphic induction attaches a cuspidal automorphic representation π_g of GL_d(A_Q) with the same standard L-function. For n=4 these are dihedral representations attached to holomorphic weight-one theta newforms. For n=5 they are monomial cuspidal GL₄ representations; no cohomological or holomorphic assertion is made about them.

Order the distinct isomorphism classes in this family by their arithmetic conductor `N(ρ_g)≤X`. Assuming the cited density estimates, for every ε>0 there exists τ>0 such that the number of classes whose standard L-function has a zero with

    Re s≥4/5,     |Im s|≤X^τ

is `O_ε(X^(R+ε))`, with the respective exponents above. There are ≫X/log X distinct classes in each family at conductor at most X. Consequently the exceptional fraction tends to zero with a power saving. The result is a density-one rectangle at sufficiently small fixed power height, not nonvanishing for each member or an unbounded-height strip.

## Irreducibility, conductors and infinity type

Global class field theory turns χ_g into a finite-order one-dimensional Weil/Artin character of K. Because K/Q is Galois and the orbit of χ_g has d members, Mackey's criterion makes its induction irreducible: restriction back to W_K is the direct sum of the d distinct conjugate characters. As an irreducible complex representation of dimension d>1 cannot have abelian image, the induced finite-image representation is nonabelian. Artin formalism gives the exact identity

    L_Q(s,ρ_g)=L_K(s,χ_g),
    N(ρ_g)=|D_K| N_K/Q(f(χ_g)).                                   (1)

The conductor identity includes the ramified primes: the relative Artin conductor of χ_g and the extension discriminant already account for every local factor. A primitive χ_g is essential here; no Euler factor is silently removed. Finite order makes the archimedean character of the complex field K trivial, so the induced infinity type is fixed throughout each family.

For n=4, complex conjugation in Gal(K/Q) exchanges the two induced cosets and has eigenvalues +1 and −1. Thus ρ_g is odd; since χ_g is not fixed by conjugation, the classical theta-series construction gives a cuspidal holomorphic weight-one newform. Its projective image is dihedral. For n=5, cyclic automorphic induction from K/Q gives a cuspidal GL₄ representation when the character has full Galois orbit. Equivalently, one may induce through the real quadratic subfield: both quadratic inductions are cuspidal under the full-orbit hypothesis. The standard L-identity and conductor in (1) persist under this correspondence. These standard automorphic-induction assertions are additional inputs, independent of the sieve/detector.

The finite central character is not generally fixed. With the usual Artin reciprocity convention it is

    det ρ_g = det(Ind_(W_K)^(W_Q) 1) · χ_g|_(A_Q×),                 (2)

where the last restriction is interpreted through the diagonal idele embedding and global class field theory. Here the determinant of the regular permutation representation is the quadratic character of K/Q for n=4 and that of the unique quadratic subfield Q(√5) for n=5. Formula (2) also gives the automorphic central character; using the opposite reciprocity convention conjugates the character factors consistently.

## Count and nonvacuity

A zero of the standard L-function of an induced representation is a zero of L_K(s,χ_g), with the same multiplicity. By (1), the conductor bound `N(ρ_g)≤X` puts the inducing character in the density theorem at scale `X/|D_K|`. Shrink τ slightly to absorb this fixed scaling in the common height window. Counting inducing labels gives the asserted upper bound on exceptional representations even if several labels induce the same representation.

For the lower bound, let p be a rational prime splitting completely in K, outside the fixed bad set, and choose one prime ideal 𝔭|p. Good-prime local Kummer theory says χ_𝔭 has exact order n and is ramified at 𝔭, while it is unramified at every other good prime. Its conjugates are ramified at the distinct primes σ𝔭, so all d conjugates are distinct. The fixed-S part of its conductor is bounded, hence `N(ρ_𝔭)≪_K p`. The splitting prime theorem gives ≫X/log X such p with conductor at most X after adjusting the fixed constant.

If `Ind χ≅Ind ψ`, restriction to W_K implies that ψ is one of the d Galois conjugates of χ. Good prime labels at different rational primes have different good conductor supports, and in general each induced representation has at most d distinct inducing characters in the full-orbit family. Thus the split-prime construction gives ≫X/log X distinct representations. Isomorphic automorphic inductions are counted once; standard cyclic induction and its L-parameter match give the same bound for the corresponding π_g. The constant-height all-Hecke comparator quoted in the density summary has exponent 1 at σ=4/5 in these Galois fields, while the source-dependent family exponents here are 13/15 and 19/20. This comparison is not an exhaustive prior-art or novelty claim. □

**Independent review:** A second researcher checked full-orbit irreducibility, nonabelian finite image, arithmetic conductor and L-identity, odd weight-one induction, cyclic GL₄ cuspidality, the determinant/transfer formula, split-prime lower counts and induction fibers. The review is conditional on the cited density and standard class-field/automorphic-induction inputs; it does not establish those inputs independently.
