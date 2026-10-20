# Claim ledger and invalidation boundaries

All identities below are local to this packet and use the prefix L26. No
historical claim identifier is reassigned. Every mathematical statement here
is proposed for review; `IMPORTED` identifies an external preprint theorem,
not an independent certification of its proof.

| ID | Status | Exact scope | Smallest load-bearing premise or failure point |
|---|---|---|---|
| L26-IMPORT | IMPORTED | Every number field, every finite-order Hecke character; open Re(s)>B_flat; principal pole at one allowed | Liu 2610.26835v1 Theorem 17.1, including the moment derivations, field transfer and descent. Only a focused source audit was completed. |
| L26-ARTIN | PROPOSED, complete implication | Under H(B), every finite-image Artin representation; normalized by (s-1)^(dim invariants); holomorphic unit on Re(s)>B | Brauer induction with integer coefficients, full ramified induction identity, and individual Hecke units. |
| L26-A5 | EXACT_RATIONAL / CERTIFIED_INTEGER_COVERAGE | Two explicit irreducible degree-three A5 characters and their Brauer factorizations | All 60 even permutations, subgroup homomorphisms, induction sums, and character inner products are recomputed. Does not evaluate an L-function. |
| L26-CHEB | PROPOSED, complete implication | Each fixed finite Galois extension and class function; O(x^(B+epsilon)) error; alpha strictly greater than B for short intervals | Fixed-character logarithmic-derivative bound, Perron inversion, finite Brauer factorization. No discriminant-uniform onset or boundary-line conclusion. |
| L26-PRIMES | PROPOSED, complete implication | H(B), 1/2<=B<1; all fields, finite ray moduli and real-place signs; degree-one generators, including subgroups with index factor | Uniform smoothed error O(X^B(log(DNf)+n)); character orthogonality and O(n sqrt X) removal of higher rational prime powers. Constant C_B not computed. |
| L26-MOBIUS | PROPOSED, complete implication | Each fixed field; primitive finite-order characters; conductor-uniform q^epsilon X^(B+epsilon) signed ideal-Mobius bound | Common zero-free domain plus conductor-uniform polynomial growth, the written logarithm argument and signed Perron inversion. No field-uniform constant. |
| L26-BARRIER-BAL | PROPOSED, exact scalar proof | Balanced system, fixed source count R, pointwise/averaged choice separately in every class | Four-witness exact sign cover and monotonicity. Formal classes need not be arithmetically nonempty. |
| L26-BARRIER | PROPOSED, exact scalar proof | Four explicit endpoints, full source direct cost, free total length, either sign of asymmetry; kappa_0<=kappa<=1 | Exact affine reduction, positive direct dual, full witness coverage, paid negative-asymmetry slopes. No universal barrier for unknown estimates or new contours. |
| L26-PRINCIPAL | PROPOSED, complete component proof | Source principal residues w=1,z=1/6; F contains mu_12; finite-order target eta; S contains bad primes | Identification with source §13.3 local correction. K is a unit on Re(s)>1/2; H has the extracted angular zeros. This does not control nonprincipal rows. |
| L26-STRIP | PROPOSED, exact transform and estimate | Complete angular Mobius convolution of the principal Mellin function; Gaussian retained | The assumed large-Y bound and proved rapid small-Y decay. Absolute values preserve B only above 2/3; no angular cancellation estimate is supplied. |
| L26-MIXED-TARGET | OPEN | The complete #1006 U^(6/5+epsilon) source mean, with every profile, local overlap, twist and height covered | The missing 7/40 corner power saving. Neither this packet's scalar algebra nor its finite-order reciprocal consequence proves it. |

## Endpoints and poles

The zero-free assertion is open at B_flat. Principal Hecke functions have a
simple pole at one. Artin representations with m invariant vectors have
exactly a pole of order m at one; their normalized functions have nonzero
continued values there. Virtual representations can have a zero at one if
their invariant multiplicity is negative. Full finite-image representations
and arbitrary virtual representations must therefore not be conflated.

The principal correction's unit domain Re(s)>1/2 concerns K, not H. The
ordinary Euler product gives H nonzero for Re(s)>2/3. The extracted
infinite-order angular character is outside H(B)'s finite-order scope.

## What the computation means

The barrier checker starts from explicit rational formulas and authenticates
the critical algebraic identity directly in Q[k]/(Q). It checks all divisions
and the complete affine cover of the b half-line; decimals do not determine
acceptance. The A5 checker constructs the underlying finite objects.
The local Euler checker keeps the three local variables independent.

These are finite certificates for the stated mathematical subclaims.
They cannot certify the external theta identities, analytic moments,
normal-convergence proof, contour arguments, or global zero-freeness.
The written analytic implications and their source assumptions remain
separate review objects.

## Supersession and novelty

Liu's imported B_flat numerically supersedes older all-field finite-order
boundaries at matching scope. That comparison neither accepts nor retracts
the older component proofs. The broader Artin closure and arithmetic
consequences use established methods, with no claim of worldwide novelty.
The scalar barrier and principal-factor extraction are compared with the
specific earlier repo objects inspected in the companion notes.

No claim here proves RH, a smaller universal B, global Artin holomorphy,
a practical least-prime search limit, a small prime in every residue class,
or the required infinite-order angular moment.
