# Conditional transfer to symmetric powers of a dihedral family

**Status:** Proposed elementary corollary of an imported preprint, not an independent proof of its analytic input. Novelty of this application has not been established. It does not improve the zeta boundary or establish the imported theorem.

**Scope:** Artin L-functions of symmetric powers of finite-image representations induced from the Eisenstein field, with finite-order Dirichlet twists. The proof uses standard induction and multiplicativity for complete Artin L-functions, including ramified Euler factors. It does not cover general automorphic forms or non-finite-order Hecke characters.

**Source:** Xu–Sang, [*Amplified moments and a refinement of the quasi-Riemann hypothesis*, arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291), Theorem 1.1, claims that every finite-order Hecke L-function over E = Q(sqrt(-3)) and every Dirichlet L-function has no zeros for Re(s) > B = 8748867/10000000, allowing principal poles. Their theorem assumes the analytic inputs in their Section 2, including OpenAI's 7/8 result; we have not independently audited either proof. Everything below is conditional on their stated conclusion.

## Conditional statement

Let chi be any finite-order Hecke character of E, identified by class field theory with a finite-image character of W_E; let rho = Ind_{W_E}^{W_Q} chi. For every integer n >= 0 and finite-order Dirichlet character psi, the Artin L-function L(s, Sym^n rho tensor psi) has no zeros in Re(s) > B. It has no poles there except possibly at s=1.

This is valid whether rho is irreducible or reducible. If chi differs from its conjugate, rho is irreducible and gives a dihedral weight-one Artin family; identifying its L-function with that of the associated weight-one form uses the standard modularity theorem, but modularity is unnecessary for the Artin statement.

## Proof

Let tau be the nontrivial element of Gal(E/Q), epsilon the quadratic character of E/Q, and chi^tau the conjugate character. For m < n/2 put

    theta_m = chi^(n-m) (chi^tau)^m.

For n odd, induction in stages and the monomial basis for Sym^n rho give the representation identity

    Sym^n rho = direct_sum_{0 <= m < n/2} Ind_{W_E}^{W_Q} theta_m.

For n even, add the one-dimensional character

    (det rho * epsilon)^(n/2).

Indeed restriction to W_E diagonalizes rho as chi + chi^tau. In the monomial basis, the two basis monomials with exponents (n-m,m) and (m,n-m) form an invariant two-dimensional induced summand whenever m < n/2. In the even middle term the nontrivial coset interchanges the two basis vectors n/2 times; its action is exactly that of (det rho * epsilon)^(n/2). This remains an identity of representations when some summands coincide.

By induction compatibility and multiplicativity of complete Artin L-functions, after twisting by psi the induced summand contributes

    L_E(s, theta_m * (psi o N_{E/Q})).

The middle summand, when present, is a finite-order Dirichlet L-function. Every theta_m and every twist displayed has finite order. The assumed theorem therefore makes every factor zero-free on Re(s)>B, with a possible pole at s=1. A finite product of meromorphic functions that are nonzero away from their poles is nonzero away from its poles. Since the factors have at most a principal pole at s=1, the assertion follows. No cancellation of a zero by a pole is used.

The same input also gives zeta_K(s) nonvanishing for Re(s)>B, apart from its pole at 1, for every finite abelian extension K/E, by the standard factorization zeta_K = product_chi L_E(s,chi). This includes fields of unbounded degree, but is likewise a direct consequence of the imported Hecke result.

A wider representation-theoretic version covers every finite-image complex representation r of W_Q whose restriction to W_E has abelian image. Indeed, after passing to a finite quotient, the irreducible characters of its abelian index-at-most-two normal subgroup have orbits of size one or two. Clifford theory says that irreducible constituents of r are either one-dimensional characters of W_Q or inductions of characters of W_E; in the invariant-character case, extension to the cyclic index-two quotient supplies the one-dimensional constituents. The same factorization argument gives L(s,r) nonzero for Re(s)>B, apart from a possible pole at 1. Thus the symmetric-power calculation is an explicit example of the general index-two transfer, not a claim that symmetric powers require a new analytic theorem. Twisting any such constituent by |.|^{it}, with real t, merely shifts its L-function vertically and preserves the half-plane, with a correspondingly shifted possible pole.

## Comparison and gaps

Hu's [2026 preprint](https://hexagonmath.org/2610.00216v1) claims Re(s)>7/8 for all finite-dimensional unitary Weil representations over arbitrary number fields, including Artin representations. The present conditional numerical boundary is slightly further left for the much narrower family above. The source theorem is also conditional on earlier analytic inputs, and this is a routine representation-theoretic specialization rather than a new analytic mechanism. It is not a significant numerical improvement over the strongest cited zeta/Hecke claim. We have not established whether this particular corollary was previously recorded, nor independently reviewed the source preprints.

**What was checked:** The index-two symmetric-power decomposition and the form of the middle character, by direct matrix and basis calculation; the source's theorem statement and its stated assumptions. No full analytic proof, Lean build, or complete literature survey was performed.

**Smallest remaining gap:** An independent proof audit of Xu–Sang and its imported analytic inputs would be needed before treating the boundary as unconditional. To obtain a genuinely stronger family theorem, one needs a boundary left of B or a class not already covered by a comparable result, with all local factors and analytic hypotheses checked.
