# From rank-one Hecke inputs to higher-rank families: exact boundary

**Status:** Exploratory reductions and obstruction; no new zero-free theorem. All source preprints cited below remain unaudited here.

**Scope:** Standard L-functions of unitary cuspidal representations of GL(2)/Q, especially their base changes to E = Q(sqrt(-3)), and symmetric powers of E-dihedral representations. No result is asserted for a general automorphic L-function or an infinite-order Hecke character at the stronger boundary.

## Quadratic base change gives an equivalence, not a free improvement

Let epsilon be the quadratic Dirichlet character of E/Q, let pi be a unitary cuspidal automorphic representation of GL(2)/Q, and write pi_E for its quadratic base change. Standard local and global base-change compatibility gives, as meromorphic functions including the ramified factors,

    L_E(s, pi_E) = L_Q(s, pi) L_Q(s, pi tensor epsilon).

The two standard L-functions on the right are entire. Consequently, for any region D, nonvanishing of the left-hand side on D implies nonvanishing of each factor on D; conversely nonvanishing of both factors implies nonvanishing of the product. Since quadratic twisting permutes the class of unitary cuspidal GL(2)/Q representations, a proposed uniform zero-free theorem for the full class of quadratic base changes is exactly equivalent to the same theorem for the original full GL(2)/Q class. The base-change identity alone therefore does not pay for a zero-free theorem.

There is a further structural boundary. Quadratic base change is noncuspidal precisely when pi is automorphically induced from a Hecke character of E; otherwise pi_E is cuspidal. In particular, for a non-E-dihedral pi, the automorphic base change cannot be an isobaric sum of Hecke characters. Its standard Euler product therefore is not obtained by the above straightforward positive factorization into rank-one Hecke L-functions. Standard sources for these statements are the quadratic base-change and automorphic-induction theorems; their full hypotheses and normalizations must be supplied in any use beyond this note.

## A narrower concrete target: infinite infinity type

Theorem 1.1 of [Xu–Sang](https://arxiv.org/abs/2610.15291), assuming its listed analytic inputs, states the numerical boundary B = 0.8748867 for finite-order Hecke characters of E and Dirichlet characters. The later [Liu preprint](https://arxiv.org/abs/2610.26835v1) claims the slightly stronger boundary 0.874886647039964... for finite-order Hecke characters over every number field. Neither source covers a general algebraic Hecke character of nonzero infinity type, including the unitary normalization of the Hecke character attached to a CM elliptic curve with CM by E. The [conditional finite-image transfer](../2026-10-28-dihedral-transfer/README.md) shares this limitation.

Let chi be any *unitary* Hecke character of E and rho its two-dimensional induced Weil representation. The index-two algebra in the companion note still gives, for every integer n >= 0, a factorization of L(s, Sym^n rho) into finitely many L-functions of unitary characters of E and, when n is even, one L-function of a unitary character of Q. Thus a single theorem giving the same boundary for all unitary Hecke characters of E and Q would transfer it to every one of those symmetric-power L-functions. Any poles coming from unitary norm characters must be excluded at their actual shifted locations, rather than silently treated as a pole at 1.

[Hu](https://hexagonmath.org/2610.00216v1) claims the broader unitary Weil family at the weaker boundary 7/8. Proving the stronger 0.8748867 region for all unitary characters of E would therefore improve that claimed region for CM families, but the finite-order Xu–Sang theorem does not itself supply this extension. One must prove the needed uniform arithmetic and analytic estimates for the fixed nonzero archimedean types, including conductor dependence, and redo the probe and contour comparison. Finite-order characters and finite experimental tables alone are not such a proof.

## What was checked and smallest open step

The index-two factorization and the logical consequences of the base-change identity were checked algebraically. The cited automorphic base-change theorem and the 2026 analytic claims were not independently proved or formally checked here. A concrete theorem-sized analytic target is: for each fixed archimedean type and every finite conductor, prove the Xu–Sang-style zero-free bound for the resulting unitary Hecke characters of E, with exact dependence on conductor, height, and type sufficient for the source's family comparison. The present note does not establish that estimate, or any strengthened zero-free region.
