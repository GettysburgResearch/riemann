# Prime-order monomial Artin density over cyclotomic fields

**Status.** This is a source-dependent consequence of the [full fixed-order conductor-density argument](../2026-10-29-full-order-density/README.md), not an individual zero-free region. Its generalized rectangular-sieve and fixed-field detector/profile arguments are source replays, and their underlying preprints have not been independently established. We additionally use classical class-field theory, Artin induction, cyclic automorphic induction, and standard prime-ideal counting. No priority claim is made.

Fix an odd prime p≥5, put K=Q(ζ_p), d=p−1, and let S be a fixed Galois-stable finite set containing the primes above p and the fixed bad primes in the cited order-p source family. For good p-free ideals g let χ_g be the source's primitive finite-order character of K, of order dividing p. Retain those χ_g of exact order p whose orbit under Gal(K/Q) has d elements. Define the finite-image Artin representation

    ρ_g = Ind_(W_K)^(W_Q) χ_g.

Each ρ_g is irreducible and d-dimensional with nonabelian image. Cyclic automorphic induction gives a cuspidal representation π_g of GL_d(A_Q), whose standard L-function is L_K(s,χ_g). Order distinct isomorphism classes by their arithmetic conductors. Subject to the source-density inputs above, for every fixed σ with

    1−1/(p−1) < σ < 1

and every ε>0 there is τ>0 such that, for X≥2, the number of classes of conductor at most X whose L-function has a zero in

    Re s≥σ,    |Im s|≤X^τ

is O_(p,σ,ε)(X^(R_p(σ)+ε)), where

    R_p(σ) = 2−1/(p−1)−σ < 1.                                    (1)

The number of distinct classes of conductor at most X is ≫_p X(log X)^(p−2). Thus all but a power-saving proportion have no zeros in this rectangle. The same statement holds for the corresponding distinct automorphic inductions. It gives neither an individual strip nor a bound uniform over all p.

For example, p=7 and σ=17/20 give K=Q(ζ₇), d=6, |D_K|=7^5, and

    R_7(17/20) = 59/60.

For every ε>0 there is τ>0 such that O_ε(X^(59/60+ε)) of these irreducible six-dimensional monomial Artin representations, equivalently their cuspidal GL₆ inductions, have a zero in the displayed rectangle; there are ≫X(log X)^5 distinct representations in the family.

## Induction and conductor

Class field theory turns each χ_g into a finite-order character of W_K. Since K/Q is cyclic Galois and the orbit is full, restriction of ρ_g to W_K is the sum of d distinct conjugates; Mackey's criterion gives irreducibility. Its image cannot be abelian because an irreducible representation of a finite abelian group has dimension one. Artin induction gives equality at all places, including ramified primes,

    L_Q(s,ρ_g)=L_K(s,χ_g),
    N(ρ_g)=|D_K| N_K/Q(f(χ_g)),     |D_K|=p^(p−2).              (2)

The infinity type is fixed: each finite-order character is trivial on the connected complex archimedean group. Cyclic automorphic induction is cuspidal because no nonidentity element of Gal(K/Q) stabilizes χ_g. Its standard L-function and conductor agree with (2). Equivalently, one can induct through prime-degree cyclic subextensions; the full-orbit condition gives the required cuspidality at every stage. The finite central character varies with χ_g; it is the determinant of the induced parameter, equivalently the determinant of the permutation representation of Gal(K/Q) multiplied by the restriction of χ_g to A_Q×, with a consistent Artin reciprocity convention.

The character-density theorem (2) of the full-order note applies to all good p-free labels and the principal fixed twist. An exceptional induced representation supplies an exceptional inducing label of conductor ≤X/|D_K|. Shrinking τ slightly absorbs this fixed factor into the common height range. This gives the upper bound (1), without assuming that the entire Galois orbit remains inside the chosen source presentation.

## Full-orbit denominator

The cited conductor formula and good tame local symbols yield distinct primitive characters for distinct p-free labels. Their conductor at good primes is the radical of the label and their S-part is uniformly bounded. The positive-coefficient Tauberian argument in the full-order note gives ≫X(log X)^(p−2) distinct nontrivial order-p labels with conductor at most X. We show that those with a non-full Galois orbit are negligible even on this scale.

Fix 1≠σ∈Gal(K/Q), of order o≥2. If χ_g is fixed by σ, then its good conductor radical is σ-invariant. For an unramified rational prime q, let f be its residue degree in K and let l be the length of a σ-orbit of prime ideals above q. Since σ^l lies in the decomposition group of order f, o divides lf. Consequently the product of prime-ideal norms in that orbit is q^(lf) with lf≥o≥2. On each selected orbit at most (p−1)^l assignments of nonzero exponents in {1,…,p−1} are possible. The Euler product for all p-free labels with σ-invariant good support is therefore absolutely convergent for Re s>1/2: its logarithm is bounded by a constant depending on p times Σ_q q^(−2 Re s). Rankin's bound gives O_(p,ε)(X^(1/2+ε)) such labels with N rad(g)≤X. Summing over the finitely many nonidentity σ proves that deleting all non-full-orbit characters costs O_(p,ε)(X^(1/2+ε)).

If two induced representations are isomorphic, restricting them to W_K shows that their inducing characters are Galois conjugate. Hence an induced isomorphism class has at most d distinct inducing characters, even if the orbit is not wholly represented by the chosen label family. Division by d gives ≫X(log X)^(p−2) distinct full-orbit Artin representations. Equality of automorphic inductions forces equality of their unramified local parameters; Chebotarev and character theory then give the same Artin representation, so the lower count also holds for distinct automorphic representations.

The same invariant-support argument also strengthens the quartic K=Q(i) denominator in the [degree-two companion](../2026-10-29-monomial-artin-density/README.md) to ≫X(log X)^2: the only nonidentity automorphism has order two, the exact-order-four labels already have that abundance, and the bad-orbit labels are O(X^(1/2+ε)). The quintic case here similarly gives ≫X(log X)^3. These remain subject to the companion source hypotheses.

A simpler nonvacuity check is to choose one prime ideal over each rational prime splitting completely in K. Its exact-order-p character ramifies at that prime and not its conjugates, so its orbit is full and its conductor is O_p(q). Distinct q give distinct rational ramification supports, and the splitting-prime theorem alone supplies ≫X/log X classes.

**Independent review.** A second researcher checked the invariant-radical count and its residue-degree divisibility, full-orbit irreducibility, conductor and automorphic-induction assertions, the isomorphism fibers, and the p=7 exponent. The review remains conditional on the cited density and standard induction inputs.
