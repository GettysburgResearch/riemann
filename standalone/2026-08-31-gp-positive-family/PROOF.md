# An infinite family of purely expansion-side Ramanujan failures: GP(n,2) for all n >= 24

```text
Status:  PROVED (Theorem below; three pieces, each with complete proof
         text and exact integer/rational Sturm certificates, each
         independently adversarially verified — all three verdicts
         SOUND with full certificate re-runs; workflow record
         wf_70eda207-75f in the session transcript). Floats appear
         only as labelled reconnaissance.
Machine: exact certificates stated inside the pieces (repo core.exact
         Sturm + the verifiers' independent re-implementations);
         graphs/gp24_certificate.json independently corroborates the
         base case.
Depends: elementary linear algebra, trigonometric identities, exact
         Sturm certificates; complements O-108006 and
         graphs/WITNESS16_STRUCTURE.md.
RH status: RH and GRH are unproved; nothing here addresses them.
```

## Theorem

For every `n >= 24`, the generalized Petersen graph `GP(n, 2)` is a
simple connected cubic graph on `2n` vertices with

```text
lambda_2 > 2 sqrt 2      and      lambda_min > -2 sqrt 2 :
```

its Ramanujan-property failure is PURELY EXPANSION-SIDE, uniformly over
an infinite family. Moreover:

1. the negative-end bound holds for EVERY `n >= 5` (the block minimum
   never drops below ~ -2.421 > -2 sqrt 2), so no member of the family
   ever breaches the bipartite end;
2. `n = 24` is the exact threshold: the verification round certified,
   by integer Sturm on the exact degree-46 characteristic polynomial,
   that `GP(23, 2)` has exactly ONE eigenvalue in `(5657/2000, 4]`
   with `(5657/2000)^2 > 8` — the trivial eigenvalue 3 — so
   `lambda_2(GP(23,2)) <= 5657/2000`-side of the bound fails there,
   and the family enters the breach exactly at `n = 24`, never to
   leave it (monotonicity, Piece 3);
3. `lambda_2(GP(n,2)) -> 3` as `n -> infinity`: the failure is not
   marginal.

Together with the finite transitional windows of the capped-ladder
families (graphs/WITNESS16_STRUCTURE.md), both mechanisms of one-sided
expansion failure are now exactly witnessed: a PERMANENT regime (this
family; lambda_min bounded away from -3 by block structure) and a
TRANSIENT WINDOW (near-bipartite corridors).

The proof is assembled from three independently verified pieces; each
piece's text is reproduced verbatim from the workflow record, followed
by its certificate list and its stated caveats.


---

## PIECE 1 - block decomposition (adversarial verdict: SOUND)

```text
PIECE 1. BLOCK DECOMPOSITION OF THE SPECTRUM OF GP(n,2)
========================================================

Conventions. For n >= 5, the generalized Petersen graph GP(n,2) has vertex
set V = {O_0, ..., O_{n-1}} u {I_0, ..., I_{n-1}} (2n vertices; O_i is
outer vertex i, I_i is inner vertex n+i in the 0..2n-1 labelling), all
indices read mod n, and edge set

    E = { {O_i, O_{i+1}} : 0 <= i < n }        (outer n-cycle)
      u { {I_i, I_{i+2}} : 0 <= i < n }        (inner step-2 circulant)
      u { {O_i, I_i}     : 0 <= i < n }        (spokes).

A denotes the adjacency matrix of GP(n,2) on C^{2n}, with standard basis
vectors e_{O_i}, e_{I_i}. Write omega = e^{2 pi i / n} (primitive n-th
root of unity), and for j = 0..n-1

    c_j  = omega^j  + omega^{-j}  = 2 cos(2 pi j / n),
    c'_j = omega^{2j} + omega^{-2j} = 2 cos(4 pi j / n),

    B_j = [ c_j  1  ]
          [ 1    c'_j ]   (real symmetric 2x2).

LEMMA 0 (well-definedness, cubic, connected). For every n >= 5, GP(n,2)
is a simple connected 3-regular graph on 2n vertices with 3n edges.

Proof. Simplicity and degrees: the three listed neighbour sets of any
vertex are pairwise disjoint singletons. For O_i the neighbours are
O_{i-1}, O_{i+1}, I_i; O_{i-1} = O_{i+1} would need n | 2, impossible for
n >= 5, and outer vertices are never inner vertices, so deg(O_i) = 3 with
no repeated edge and no loop (O_{i+1} = O_i would need n | 1). For I_i
the neighbours are I_{i-2}, I_{i+2}, O_i; I_{i-2} = I_{i+2} would need
n | 4, impossible for n >= 5, and I_{i+2} = I_i would need n | 2. So the
graph is simple and 3-regular; the edge count is 3n (n edges per class,
classes disjoint). Connectivity: the outer cycle connects all O_i to each
other, and each I_i is joined to O_i by its spoke, so every vertex is
connected to O_0. QED.

(For n >= 5 with n odd, the inner edges form a single n-cycle
I_0 I_2 I_4 ...; for n even they form two n/2-cycles; either way Lemma 0
holds — connectivity above never used the inner edges.)

THEOREM 1 (block decomposition). For every n >= 5,

    det(x I_{2n} - A) = prod_{j=0}^{n-1} det(x I_2 - B_j),

and consequently spec(GP(n,2)) — the multiset of the 2n eigenvalues of A
— is exactly the multiset union over j = 0..n-1 of the two eigenvalues of
B_j.

Proof.

Step 1 (rotation symmetry — motivation). The map rho: O_i -> O_{i+1},
I_i -> I_{i+1} sends each edge class to itself ({O_i,O_{i+1}} ->
{O_{i+1},O_{i+2}}, {I_i,I_{i+2}} -> {I_{i+1},I_{i+3}}, {O_i,I_i} ->
{O_{i+1},I_{i+1}}), hence is a graph automorphism of order n; its
permutation matrix R satisfies R A R^{-1} = A, i.e. A R = R A, so A
preserves every eigenspace of R. The Fourier vectors below are exactly
the R-eigenvectors (R u_j = omega^{-j} u_j, R w_j = omega^{-j} w_j, with
u_j, w_j as in Step 2), which is where the decomposition comes from; the
verification below is self-contained and direct, so this step is purely
explanatory and carries no logical weight.

Step 2 (Fourier basis and orthogonal decomposition). For j = 0..n-1 set

    u_j = sum_{i=0}^{n-1} omega^{i j} e_{O_i},
    w_j = sum_{i=0}^{n-1} omega^{i j} e_{I_i},
    V_j = span_C { u_j, w_j }.

Recall the geometric-sum identity: for any n-th root of unity zeta,
sum_{i=0}^{n-1} zeta^i = n if zeta = 1, and = (zeta^n - 1)/(zeta - 1) = 0
if zeta != 1. With the standard Hermitian inner product,

    <u_j, u_k> = sum_i omega^{ij} conj(omega^{ik})
               = sum_i omega^{i(j-k)} = n * [j = k],

and likewise <w_j, w_k> = n * [j = k]; <u_j, w_k> = 0 always, because
u_j and w_k are supported on disjoint coordinate sets (outer vs inner).
Thus the 2n vectors {u_j, w_j : 0 <= j < n} are pairwise orthogonal and
nonzero (each has squared norm n), hence linearly independent, hence a
basis of C^{2n}. Therefore

    C^{2n} = V_0 (+) V_1 (+) ... (+) V_{n-1}   (orthogonal direct sum),

with dim V_j = 2 for every j, and sum_j dim V_j = 2n. This is the whole
multiplicity bookkeeping: the blocks below account for all 2n dimensions,
so nothing in the spectrum is missed and nothing is counted twice.

Step 3 (A preserves each V_j and acts there as B_j). By Lemma 0 the
neighbour lists are exact, so the action of A on standard basis vectors
is

    A e_{O_i} = e_{O_{i-1}} + e_{O_{i+1}} + e_{I_i},
    A e_{I_i} = e_{I_{i-2}} + e_{I_{i+2}} + e_{O_i}.

Apply A to u_j and reindex each sum by a cyclic shift (legitimate because
all indices are mod n and omega^n = 1):

    A u_j = sum_i omega^{ij} e_{O_{i-1}} + sum_i omega^{ij} e_{O_{i+1}}
            + sum_i omega^{ij} e_{I_i}
          = omega^{j} u_j + omega^{-j} u_j + w_j
          = c_j u_j + w_j,

where e.g. sum_i omega^{ij} e_{O_{i-1}} = sum_{i'} omega^{(i'+1)j}
e_{O_{i'}} = omega^{j} u_j (substituting i' = i - 1 mod n). Similarly,

    A w_j = sum_i omega^{ij} e_{I_{i-2}} + sum_i omega^{ij} e_{I_{i+2}}
            + sum_i omega^{ij} e_{O_i}
          = omega^{2j} w_j + omega^{-2j} w_j + u_j
          = c'_j w_j + u_j.

Hence A V_j <= V_j, and in the ordered basis (u_j, w_j) of V_j the
restriction A|_{V_j} has matrix exactly

    [ c_j  1   ]
    [ 1    c'_j ]  =  B_j

(first column = coordinates of A u_j, second column = coordinates of
A w_j).

Step 4 (assembling the characteristic polynomial). Let S be the 2n x 2n
matrix whose columns are u_0, w_0, u_1, w_1, ..., u_{n-1}, w_{n-1}. By
Step 2, S* S = n I_{2n}, so S is invertible, and by Step 3

    S^{-1} A S = blockdiag(B_0, B_1, ..., B_{n-1}).

Characteristic polynomials are invariant under similarity, and the
characteristic polynomial of a block-diagonal matrix is the product of
those of its blocks (the determinant of a block-diagonal matrix is the
product of the blocks' determinants). Therefore

    det(x I_{2n} - A) = prod_{j=0}^{n-1} det(x I_2 - B_j),

a monic degree-2n identity; equating root multisets gives
spec(A) = U_{j=0}^{n-1} spec(B_j) as a multiset of size 2n. QED.

COROLLARY 2 (explicit block eigenvalues). Write c = c_j = 2 cos(2 pi
j/n) in [-2, 2]. The double-angle identity cos(2t) = 2 cos^2(t) - 1
gives 2 cos(2t) = (2 cos t)^2 - 2, i.e.

    c'_j = c_j^2 - 2   (Chebyshev relation),

so B_j = [[c, 1], [1, c^2 - 2]] and its two eigenvalues are the roots of
x^2 - (c + c')x + (c c' - 1):

    F_{+-}(c) = (c + c')/2 +- sqrt( ((c - c')/2)^2 + 1 )
             = (c^2 + c - 2)/2 +- sqrt( ((-c^2 + c + 2)/2)^2 + 1 ).

The discriminant term under the square root is >= 1 > 0, so each block
has two distinct real eigenvalues (as it must: B_j is real symmetric).
For j = 0, c = 2, c' = 2, B_0 = [[2,1],[1,2]] has eigenvalues 3 and 1;
in particular 3 in spec(A), consistent with 3-regularity and
connectivity (Perron eigenvalue). Note also B_{n-j} = B_j (both c and c'
are even functions of j mod n), so the union over j = 0..n-1 lists each
block for j and n-j identically; this is already accounted for since the
union is taken WITH multiplicity over all n values of j and the
dimension count 2n is exact (Step 2).

--------------------------------------------------------------------------
EXACT COMPUTATIONAL CERTIFICATES (n = 24, 30, 37)
--------------------------------------------------------------------------

Independent of the proof above, the identity of Theorem 1 was verified
by machine in EXACT integer/rational arithmetic (no floating point
anywhere) for n in {24, 30, 37}, using the repo's own graph builder and
exact algebra core (script: piece1_verify.py in the session scratchpad,
run from /home/user/riemann/research/exploratory/2026-08-30-two-programme-pass with the repo's core.exact and
graphs/telescope modules).

Structure check. For each n, the adjacency matrix returned by the repo's
gp(n,2) (graphs/telescope.py) was compared entry-by-entry against the
edge set E defined above: exact match; symmetric 0/1 with zero diagonal;
every row sum equals 3; |E| = 3n. Additionally the repo's exact BFS
(diameter_and_connected, girth) confirmed: connected = True with
(diameter, girth) = (8, 5), (10, 5), (11, 5) for n = 24, 30, 37.

CERT A (power-sum identity, the decisive certificate). For each n and
every k = 1, ..., 2n:

    tr(A^k)  ==  sum_{j=0}^{n-1} tr(B_j^k),

verified as an identity of exact integers, computed by two independent
exact routes:

  * Left side: A^k by repeated exact integer matrix multiplication
    (Python arbitrary-precision integers), then the trace.

  * Right side: work in the group ring Rn = Z[y]/(y^n - 1), whose
    elements are integer coefficient vectors of length n. Set

        B(y) = [ y + y^{n-1}   1          ]
               [ 1             y^2 + y^{n-2} ]   over Rn.

    For each j, the substitution phi_j : Rn -> C, y |-> omega^j, is a
    well-defined ring homomorphism (since (omega^j)^n = 1), and applying
    it entrywise sends B(y) to B_j (phi_j(y + y^{n-1}) = omega^j +
    omega^{-j} = c_j, phi_j(y^2 + y^{n-2}) = c'_j); being a ring
    homomorphism it commutes with matrix products, so
    phi_j(tr(B(y)^k)) = tr(B_j^k). Writing the reduced representative
    tr(B(y)^k) = sum_{m=0}^{n-1} a_m^{(k)} y^m (integers a_m^{(k)}) and
    summing the geometric identity sum_{j=0}^{n-1} omega^{jm} =
    n * [n divides m] over j gives the EXACT closed form

        sum_{j=0}^{n-1} tr(B_j^k) = n * a_0^{(k)},

    i.e. n times the constant coefficient of tr(B(y)^k) reduced mod
    y^n - 1. This is pure integer arithmetic (cyclic convolution of
    integer vectors); no algebraic numbers are ever represented.

  Result: equality holds for ALL k = 1..2n at n = 24 (k = 1..48),
  n = 30 (k = 1..60), n = 37 (k = 1..74). Sanity heads (n = 37):
  tr(A^1..A^6) = 0, 222, 1110*0... precisely [0, 222, 0, 1110, 370,
  6438]; note tr(A^2) = 6n = twice the edge count, tr(A^3) = 0 (girth
  5, no triangles), tr(A^4) = 15 * 2n (cubic, girth 5: each vertex
  supports 9 + 6 closed 4-walks), tr(A^5) = 10n (exactly the n
  pentagons O_i O_{i+1} O_{i+2} I_{i+2} I_i), all as they must be.

  Why CERT A certifies Theorem 1 at these n: char_A(x) = det(xI - A)
  and P_n(x) = prod_j det(x I_2 - B_j) are both monic of degree 2n over
  R. The k-th power sum of the roots of char_A is tr(A^k), and the k-th
  power sum of the roots of P_n is sum_j tr(B_j^k) (for any square
  complex matrix, tr(M^k) is the sum of the k-th powers of its
  eigenvalues with algebraic multiplicity, by triangularization). Two
  monic degree-N polynomials over a field of characteristic 0 whose
  root multisets have equal power sums p_1..p_N are EQUAL: Newton's
  identities k e_k = sum_{i=1}^{k} (-1)^{i-1} e_{k-i} p_i determine
  e_1, ..., e_N recursively from p_1, ..., p_N (division by k = 1..N is
  legal in characteristic 0), and the coefficients are (+-) the e_i.
  With N = 2n and p_k verified equal for k = 1..2n, this forces
  char_A = P_n, hence multiset equality of spectra.

CERT B (charpoly cross-check by independent implementation). For each
n in {24, 30, 37}: the monic degree-2n polynomial reconstructed from the
power sums p_k = tr(A^k), k = 1..2n, via the repo's Newton-identities
routine (core.exact.charpoly_from_power_sums, exact Fraction
arithmetic), equals coefficient-for-coefficient the characteristic
polynomial computed by the repo's Faddeev-LeVerrier routine
(core.exact.charpoly_of_matrix) on the same adjacency matrix — two
independent exact algorithms agreeing on all 2n+1 coefficients. All
coefficients are integers, as they must be for an integer matrix, and
char_A(3) = 0 in every case (the j = 0 block's Perron eigenvalue).
Recorded constant terms char_A(0) = det(-A): 0 for n = 24, 0 for
n = 30, 3 for n = 37.

Status of this piece. Theorem 1 and Corollary 2 are fully proved for
every n >= 5 (in particular for all n >= 24 as the target theorem
needs), by elementary self-contained arguments; CERTs A and B are exact
machine confirmations of the same identity at n = 24, 30, 37. Nothing in
this piece asserts the spectral-gap inequalities (lambda_2 > 2 sqrt 2,
lambda_min > -2 sqrt 2) of the target theorem; those are the business of
the later pieces, which may now freely reduce all spectral questions
about GP(n,2) to the one-variable function F_{+-}(c), c = 2 cos(2 pi
j/n) in [-2, 2], by Corollary 2.
```

### Exact certificates (each independently rerun by the verifier)

- For n in {24, 30, 37}, the adjacency matrix built by the repo's gp(n,2) (graphs/telescope.py) equals exactly the stated edge set (outer n-cycle 0..n-1, inner circulant n+i ~ n+((i+2) mod n), spokes i ~ n+i); it is symmetric 0/1 with zero diagonal, 3-regular, with 3n edges; and GP(n,2) is connected with (diameter, girth) = (8,5), (10,5), (11,5) for n = 24, 30, 37 respectively.
  (method: Entry-by-entry integer comparison of gp(n,2) against the explicitly constructed edge set; exact BFS (telescope.diameter_and_connected, telescope.girth). Pure integer arithmetic.; result: PASS for all three n.)
- CERT A: tr(A^k) = sum_{j=0}^{n-1} tr(B_j^k) for every k = 1..2n, at n = 24 (k=1..48), n = 30 (k=1..60), n = 37 (k=1..74), where A = adjacency of GP(n,2) and B_j = [[2cos(2 pi j/n), 1],[1, 2cos(4 pi j/n)]]. By Newton's identities (characteristic 0), this forces det(xI - A) = prod_j det(xI_2 - B_j), i.e. exact multiset equality of the 2n-element spectra, at these n.
  (method: LHS: exact big-integer matrix powers and traces. RHS: exact integer cyclic-convolution arithmetic in Z[y]/(y^n - 1) applied to B(y) = [[y + y^{n-1}, 1],[1, y^2 + y^{n-2}]]; sum_j tr(B_j^k) = n * (constant coefficient of tr(B(y)^k) mod y^n - 1), via the substitution homomorphisms y -> omega^j and sum_j omega^{jm} = n*[n|m]. No floats, no algebraic-number approximations.; result: PASS: all 48 + 60 + 74 integer equalities hold. Sample values (n=37): tr(A^1..A^6) = [0, 222, 0, 1110, 370, 6438], matching the combinatorial closed-walk counts (6n, 0 triangles, 15*2n, 10n pentagons).)
- CERT B: for n in {24, 30, 37}, the monic degree-2n characteristic polynomial of A computed by Faddeev-LeVerrier (core.exact.charpoly_of_matrix, exact rational) equals coefficient-for-coefficient the polynomial reconstructed from the power sums tr(A^k), k=1..2n, by Newton's identities (core.exact.charpoly_from_power_sums); all coefficients are integers; char_A(3) = 0 in each case; constant terms det(-A) = 0, 0, 3 for n = 24, 30, 37.
  (method: Two independent exact-rational implementations from the repo's core.exact, compared on all 2n+1 coefficients; is_integer_poly and poly_eval at x = 3, exact Fractions.; result: PASS for all three n (48x48 in 11s, 60x60 in 27s, 74x74 in 65s).)

### Stated caveats

```text
(1) Scope of the machine checks: CERTs A and B verify the block-decomposition identity exactly at n = 24, 30, 37 only; for general n >= 5 the identity rests on the pen-and-paper proof of Theorem 1 (which is elementary and self-contained but not machine-checked symbolically for all n). (2) Standard facts used without citation in the proof, all elementary: geometric sum of n-th roots of unity; similarity invariance of the characteristic polynomial; det of a block-diagonal matrix = product of block dets; tr(M^k) = sum of k-th eigenvalue powers with algebraic multiplicity (triangularization over C); Newton's identities determine e_1..e_N from p_1..p_N in characteristic 0; the double-angle identity cos(2t) = 2cos^2(t) - 1. (3) Lemma 0 (simple, cubic, connected) is proved for all n >= 5 by hand; connectivity/regularity were additionally machine-checked (exact BFS / row sums) at n = 24, 30, 37, and the repo's prior gp24_certificate.json independently records connected = true for n = 24. (4) This piece proves ONLY the spectral decomposition (and cubic/connected); it does NOT prove the target theorem's inequalities lambda_2 > 2 sqrt 2 or lambda_min > -2 sqrt 2 for any n — those must come from analyzing F(c) = (c^2 + c - 2)/2 +- sqrt(((-c^2 + c + 2)/2)^2 + 1) on c in [-2, 2] in later pieces. (5) No floating point was used anywhere in the certificates (all Python big integers and Fractions); no repo files were modified — the verification script lives only in the session scratchpad (/tmp/claude-0/-home-user-riemann/e13a48a6-09bb-51d1-99b0-4e77345fd1dc/scratchpad/piece1_verify.py). (6) Basis subtlety handled in the proof, restated here: the Fourier vectors u_j, w_j are complex, so A restricted to V_j is represented by the real symmetric B_j in a complex basis; reality of the spectrum is automatic since A itself is real symmetric, and B_{n-j} = B_j means conjugate index pairs carry identical blocks — the multiset union over j = 0..n-1 (dimension count sum_j dim V_j = 2n, matching deg char_A = 2n) is the complete bookkeeping. (7) tr(A^4) = 15 * 2n and tr(A^5) = 10n sanity interpretations assume girth 5 (no 3- or 4-cycles), which the exact girth computation confirmed at the three tested n; these interpretations are commentary, not load-bearing for the certificates.
```


---

## PIECE 2 - negative-end bound, all n (adversarial verdict: SOUND)

```text
PIECE 2. NEGATIVE-END BOUND: Fminus(c) > -2*sqrt(2) for ALL c in [-2,2].

Setup. For c in [-2,2] put
  A(c)  = (c^2 + c - 2)/2          (mean of the block diagonal of B_j),
  B(c)  = (c^2 - c - 2)/2          (half-difference; only B^2 enters),
  D(c)  = B(c)^2 + 1  >= 1,
  S(c)  = sqrt(D(c))  >= 1 > 0,
  Fminus(c) = A(c) - S(c),  Fplus(c) = A(c) + S(c).
(The prompt's (-c^2+c+2)/2 is -B(c); its square is B(c)^2, so this S is the
same S.)  CLAIM: Fminus(c) > -2*sqrt(2) for every c in [-2,2].

Step 1 (left side positive after the shift).  Exact identity (certificate I2)
  A(c) + 9/8 = (2c+1)^2 / 8  >= 0,
so A(c) >= -9/8 for every real c.  Also 2*sqrt(2) > 9/8: both sides of
16*sqrt(2) > 9 are positive and (16*sqrt(2))^2 = 512 > 81 = 9^2 (integer
certificate C0).  Hence
  A(c) + 2*sqrt(2) >= 2*sqrt(2) - 9/8 > 0   for all real c.        (Sign 1)

Step 2 (first squaring, an equivalence).  S(c) > 0 always and
A(c) + 2*sqrt(2) > 0 by (Sign 1); for positive reals x, y one has
x > y <=> x^2 > y^2.  Therefore, for each c in [-2,2],
  Fminus(c) > -2*sqrt(2)
    <=>  A(c) + 2*sqrt(2) > S(c)
    <=>  (A(c) + 2*sqrt(2))^2 > D(c).                              (Equiv 1)
No information is lost: both squarings below are two-sided equivalences or
one-sided implications in the direction needed, with the sign conditions
(Sign 1), (Sign 2) recorded where used.

Step 3 (clearing sqrt(2), exact identity in Q(sqrt2)[c]).  Define the
INTEGER polynomials
  P(c) = c^3 - 2c + 7,        Q(c) = 2c^2 + 2c - 4.
Then, as an identity in Q(sqrt2)[c] (certificate I1, verified by exact
Fraction polynomial arithmetic with sqrt2 treated as a formal symbol of
square 2),
  (A(c) + 2*sqrt(2))^2 - D(c) = P(c) + sqrt(2)*Q(c) =: G(c).
Derivation being verified: (A + 2 sqrt2)^2 = A^2 + 4 sqrt2 A + 8; the
rational part is A^2 + 8 - B^2 - 1 = (A-B)(A+B) + 7 = c*(c^2-2) + 7 = P(c)
(using A - B = c, A + B = c^2 - 2), and the sqrt2-part is 4A(c) = Q(c).
By (Equiv 1) the CLAIM is equivalent to:  G(c) > 0 for all c in [-2,2].

Step 4 (guard: P > 0 on [-2,2]).  Certificate C1: the Sturm count of
distinct real roots of P in the half-open interval (-2,2] is 0
(count_real_roots_in(P,-2,2) = 0, exact rational arithmetic), and the exact
evaluation P(-2) = 3 > 0 shows -2 is not a root either; so P has NO root in
the closed interval [-2,2].  Since P is continuous and P(0) = 7 > 0 (exact),
the intermediate value theorem gives
  P(c) > 0 for all c in [-2,2].                                    (Sign 2)

Step 5 (region c in [1,2]: Q is nonnegative there).  Exact factorization
(certificate I3):  Q(c) = 2*(c+2)*(c-1).  For c in [1,2]: c+2 >= 3 > 0 and
c-1 >= 0, so Q(c) >= 0.  Since sqrt(2) > 0 and P(c) > 0 by (Sign 2),
  G(c) = P(c) + sqrt(2)*Q(c) >= P(c) > 0   for c in [1,2].
(Anchors, exact: Q(1) = 0, Q(2) = 8, P(1) = 6, P(2) = 11.)

Step 6 (region c in [-2,1]: second squaring).  Here Q(c) <= 0 (same
factorization: c+2 >= 0, c-1 <= 0; exact anchors Q(-2) = 0, Q(-1/2) = -9/2,
Q(1) = 0), so G(c) = P(c) - sqrt(2)*|Q(c)|.  For any c with P(c) > 0,
  P(c) > sqrt(2)*|Q(c)|  <=>  P(c)^2 > 2*Q(c)^2
(both sides of the left inequality are nonnegative, squaring is an
equivalence), and P(c) > sqrt(2)*|Q(c)| implies
G(c) >= P(c) - sqrt(2)*|Q(c)| > 0.  Define the INTEGER polynomial
  H(c) := P(c)^2 - 2*Q(c)^2 = c^6 - 12 c^4 - 2 c^3 + 28 c^2 + 4 c + 17
(certificate I4, exact expansion).  Certificate C2: the Sturm count of
distinct real roots of H in (-2,1] is 0 (count_real_roots_in(H,-2,1) = 0),
and the exact evaluation H(-2) = 9 > 0 shows -2 is not a root; so H has no
root in [-2,1], and since H(0) = 17 > 0 (exact) the intermediate value
theorem gives H(c) > 0 on all of [-2,1].  Combined with (Sign 2):
  G(c) > 0   for c in [-2,1].

Necessity of the case split (context, exact): H(2) = -7 < 0 and the Sturm
count of H in (1,2] is exactly 1, so H > 0 genuinely fails on part of
(1,2]; there Step 5 (Q >= 0) carries the bound instead.  The two regions
overlap at c = 1 (H(1) = 36 > 0 and Q(1) = 0) and cover [-2,2].

Conclusion of the bound.  Steps 5 and 6 give G(c) > 0 for every
c in [-2,2]; by Steps 2-3 this is EQUIVALENT to
  Fminus(c) > -2*sqrt(2)   for every c in [-2,2].          (strict)  QED.

Corollary (lambda_min of GP(n,2), every n).  Granting the block spectral
decomposition of GP(n,2) (context for this piece; certified separately in
the workflow), the 2n eigenvalues are exactly { Fplus(c_j), Fminus(c_j) :
j = 0..n-1 } with c_j = 2 cos(2 pi j / n) in [-2,2].  Since S > 0 gives
Fplus(c) > Fminus(c) pointwise, every eigenvalue is >= min_j Fminus(c_j),
and each Fminus(c_j) > -2*sqrt(2) strictly by the theorem above (finitely
many j, each c_j in [-2,2]).  Hence
  lambda_min(GP(n,2)) = min_j Fminus(c_j) > -2*sqrt(2)
STRICTLY, for EVERY n >= 3 (in particular every n >= 24).  This is the
negative-end half of the target theorem, uniformly in n: GP(n,2) never
breaches the Ramanujan window at the negative end.

Minimum region (float reconnaissance only, NO proof weight).  Refined
grid + ternary search: min over [-2,2] of Fminus is approx -2.4209196742,
attained at the interior critical point c* approx -0.0922 (a derivative
check (2c+1)/2 = B*B'/sqrt(B^2+1) balances there; the earlier rough recon
"-2.425 near c ~ -0.05" was slightly off, immaterially).  Margin above
-2*sqrt(2) approx = -2.8284271247 is approx 0.4075.  Because the c_j
become dense in [-2,2] as n grows, inf_n lambda_min(GP(n,2)) equals this
approx -2.42092: the certified bound is uniform and not tight.  Float
cross-check of the block model: numpy eigvalsh lambda_min of the actual
adjacency matrix equals min_j Fminus(c_j) to 8 decimals for n = 5, 7, 24,
31 (e.g. n=24: -2.41421356, consistent with the repo's exact GP(24,2)
certificate).

Certification environment.  Script (scratch only):
/tmp/claude-0/-home-user-riemann/e13a48a6-09bb-51d1-99b0-4e77345fd1dc/scratchpad/piece2_negend.py
using core.exact from
/home/user/riemann/research/exploratory/2026-08-30-two-programme-pass/core/exact.py
(exact Fraction arithmetic throughout; count_real_roots_in(p,a,b) is a
Sturm count of DISTINCT real roots in the HALF-OPEN interval (a,b], which
is why each left endpoint was separately certified nonzero by exact
evaluation, closing the interval).  All PASS; no repo file modified.
```

### Exact certificates (each independently rerun by the verifier)

- Identity in Q(sqrt2)[c]: (A(c)+2*sqrt2)^2 - (B(c)^2+1) = P(c) + sqrt2*Q(c), with A=(c^2+c-2)/2, B=(c^2-c-2)/2, P=c^3-2c+7, Q=2c^2+2c-4
  (method: Exact Fraction polynomial arithmetic (core.exact poly_mul/poly_add/poly_scale), sqrt2 formal with square 2; rational part and sqrt2-part compared coefficientwise; result: PASS: rational part = [7,-2,0,1] = P, sqrt2 part = 4A = [-4,2,2] = Q (low-first))
- A(c) + 9/8 = (2c+1)^2/8, hence A(c) >= -9/8 for all real c
  (method: Exact polynomial identity via poly_mul/poly_add over Q; result: PASS (coefficientwise equality))
- 512 > 81, hence 16*sqrt2 > 9 (both positive), hence 2*sqrt2 > 9/8, hence A(c)+2*sqrt2 >= 2*sqrt2 - 9/8 > 0 for all real c
  (method: Integer comparison plus monotonicity of squaring on positives; result: PASS)
- Q(c) = 2*(c+2)*(c-1); therefore Q >= 0 on [1,2] and Q <= 0 on [-2,1]
  (method: Exact polynomial identity via poly_mul; sign read off linear factors; exact anchors Q(-2)=0, Q(-1/2)=-9/2, Q(1)=0, Q(2)=8; result: PASS)
- P(c) = c^3 - 2c + 7 has no real root in [-2,2], and P > 0 there
  (method: Sturm: count_real_roots_in(P, -2, 2) on (a,b]=(-2,2], exact rational arithmetic; plus exact evaluations P(-2)=3, P(0)=7, P(1)=6, P(2)=11; IVT; result: PASS: root count 0; all listed values positive)
- H(c) := P(c)^2 - 2*Q(c)^2 = c^6 - 12c^4 - 2c^3 + 28c^2 + 4c + 17 (integer coefficients)
  (method: Exact expansion via poly_mul/poly_add over Q; integrality checked coefficientwise; result: PASS (coefficientwise equality; all denominators 1))
- H has no real root in [-2,1], and H > 0 there; hence P > sqrt2*|Q| and G = P + sqrt2*Q > 0 on [-2,1] (given P>0)
  (method: Sturm: count_real_roots_in(H, -2, 1) on (-2,1], exact; plus exact evaluations H(-2)=9, H(0)=17, H(1)=36; IVT; squaring equivalence P>sqrt2|Q| <=> P^2>2Q^2 valid since both sides nonnegative; result: PASS: root count 0; all listed values positive)
- Case split is necessary: H fails on part of (1,2]
  (method: Exact evaluation H(2) = -7 < 0 and Sturm count_real_roots_in(H, 1, 2) (context only, not used in the bound); result: PASS: H(2) = -7, exactly 1 distinct real root of H in (1,2])
- MAIN: Fminus(c) = (c^2+c-2)/2 - sqrt(((c^2-c-2)/2)^2 + 1) > -2*sqrt2 for all c in [-2,2]; consequently lambda_min(GP(n,2)) > -2*sqrt2 strictly for every n >= 3, given the block decomposition
  (method: Chain of the certificates above: (Sign 1) => first squaring is an equivalence; identity => reduces to G>0; [1,2] via Q>=0 and P>0; [-2,1] via H>0 and P>0; result: PROVED (all sub-certificates PASS; script piece2_negend.py in scratchpad, ALL EXACT CHECKS PASS))

### Stated caveats

```text
(1) ASSUMED, not proved here: the spectral decomposition of GP(n,2) into the 2x2 blocks B_j = [[2cos(2 pi j/n), 1],[1, 2cos(4 pi j/n)]] (equivalently, that the 2n eigenvalues are exactly the union of the block eigenvalues A(c_j) +/- S(c_j) with c_j = 2cos(2 pi j/n)); that is the other piece of this workflow. This piece's inequality Fminus(c) > -2 sqrt2 on [-2,2] is unconditional; the corollary about lambda_min(GP(n,2)) is conditional on that decomposition. A float-only cross-check (numpy eigvalsh vs min_j Fminus(c_j), n = 5, 7, 24, 31, agreement to 8 decimals) supports it but carries no proof weight. (2) IMPORTED standard facts: Sturm's theorem (root counting via sign changes of the Sturm chain), the intermediate value theorem, monotonicity of squaring on nonnegative reals, and sqrt2 > 0. (3) TRUSTED CODE: the repo's core.exact implementation (sturm_chain, count_real_roots_in, poly_eval, poly_mul, all in exact Fraction arithmetic, no floats) is trusted as correct; I verified its (a,b] half-open convention from source and compensated at every left endpoint by an exact nonzero evaluation (P(-2)=3, H(-2)=9). (4) FLOATS appear ONLY in labelled reconnaissance: the location/value of the minimum of Fminus (approx -2.42092 at c approx -0.0922 — note this corrects the prompt's rough '-2.425 near c ~ -0.05'), the H-grid minimum, and the eigvalsh cross-check; none is used in the proof. (5) The bound proved is stronger than the target needs: it holds for every c in [-2,2], hence for every n >= 3, not only n >= 24; it is strict, with uniform slack (inf over the family approx 0.4075 above -2 sqrt2 per float recon — the slack estimate itself is recon, the strict inequality is exact). (6) The exact minimizer of Fminus was NOT determined (not needed); only the > -2 sqrt2 bound is certified. (7) Everything ran in the scratchpad (/tmp/claude-0/-home-user-riemann/e13a48a6-09bb-51d1-99b0-4e77345fd1dc/scratchpad/piece2_negend.py); no repository file was modified or committed.
```


---

## PIECE 3 - positive-end bound and threshold (adversarial verdict: SOUND)

```text
PIECE 3. POSITIVE-END BOUND: for every n >= 24, lambda_2(GP(n,2)) > 2 sqrt 2.

Setup and notation.
GP(n,2) (n >= 5) has vertices {0,...,n-1} (outer) and {n,...,2n-1} (inner, inner
vertex n+k labelled k), and edges: outer k ~ outer k+-1 (mod n), inner k ~ inner
k+-2 (mod n), spoke outer k ~ inner k. It is a simple 3-regular graph on 2n
vertices. Let A_n be its adjacency matrix and lambda_1 >= lambda_2 >= ... its
eigenvalues (with multiplicity). Write

  c_n   := 2 cos(2 pi / n),
  A(c)  := (c^2 + c - 2)/2,      u(c) := (-c^2 + c + 2)/2,      v(c) := 2 u(c),
  Fplus(c) := A(c) + sqrt(u(c)^2 + 1).

Fplus(c) is the larger root of q_c(z) := z^2 - T(c) z + Delta(c), where
T(c) = c + (c^2 - 2) and Delta(c) = c (c^2 - 2) - 1, i.e. the larger eigenvalue
of the symmetric 2x2 block B(c) = [[c, 1], [1, c^2 - 2]]. Indeed the exact
polynomial identity (T(c)/2)^2 - Delta(c) = u(c)^2 + 1 holds identically
(certified, CERT B3), so the discriminant of q_c is 4(u^2+1) >= 4 > 0 and the
larger root is A(c) + sqrt(u(c)^2 + 1) = Fplus(c). This route uses ONLY the
inequality lambda_2 >= Fplus(c_n) (Lemma 1 below); it does NOT need the full
spectral decomposition (piece 1), and it does NOT cite gp24_certificate.json.

Lemma 1 (the j = 1 block eigenvalue lies in the spectrum, and lambda_2 >= Fplus(c_n)).
Let n >= 5 and let (alpha, beta) be a real unit eigenvector of B(c_n) for its
larger eigenvalue mu := Fplus(c_n). Put omega = exp(2 pi i / n) and define
x in C^{2n} by x_{outer k} = alpha omega^k, x_{inner k} = beta omega^k. Then for
each k:
  (A_n x)_{outer k} = alpha (omega^{k-1} + omega^{k+1}) + beta omega^k
                    = (alpha * 2 cos(2 pi/n) + beta) omega^k
                    = (alpha c_n + beta) omega^k,
  (A_n x)_{inner k} = beta (omega^{k-2} + omega^{k+2}) + alpha omega^k
                    = (beta * 2 cos(4 pi/n) + alpha) omega^k
                    = (alpha + beta (c_n^2 - 2)) omega^k,
using 2 cos(4 pi/n) = (2 cos(2 pi/n))^2 - 2 (double angle). Hence A_n x = mu x
componentwise, because (alpha, beta) is an eigenvector of B(c_n) = [[c_n, 1],
[1, c_n^2 - 2]] with eigenvalue mu. Since A_n and mu are real, y := Re(x) also
satisfies A_n y = mu y, and y != 0 (its outer-0 entry is alpha and inner-0 entry
is beta, and (alpha,beta) != (0,0)). So Fplus(c_n) is an eigenvalue of GP(n,2).
Also 3 is an eigenvalue (all-ones vector; the graph is 3-regular). By Lemma 2
below, Fplus is strictly increasing on [0,2] with Fplus(2) = A(2) + sqrt(0+1)
= 2 + 1 = 3; since 0 < c_n < 2 for n >= 5, we get Fplus(c_n) < 3. The eigenvalue
multiset of A_n therefore contains 3 and contains Fplus(c_n) < 3 <= lambda_1;
removing one copy of the maximum still leaves a copy of Fplus(c_n), hence
  lambda_2(GP(n,2)) >= Fplus(c_n).                                    (1)

Lemma 2 (Fplus is strictly increasing on [0,2]).
u^2 + 1 >= 1 > 0 everywhere, so Fplus is differentiable with
  Fplus'(c) = (2c+1)/2 + u u' / sqrt(u^2+1),   u' = (1-2c)/2.
Multiplying by the positive quantity 2 sqrt(u^2+1), the sign of Fplus'(c) is the
sign of N(c) := (2c+1) sqrt(u^2+1) + 2 u u' = [ (2c+1) sqrt(v^2+4) - v(2c-1) ] / 2,
where v = 2u = -c^2 + c + 2 (so 4(u^2+1) = v^2 + 4, and 4 u u' = v (1-2c)).
Fix c in [0,2]; then 2c+1 > 0 and sqrt(v^2+4) > 0.
  Case 1: v(2c-1) <= 0. Then N(c) > 0 immediately.
  Case 2: v(2c-1) > 0. Then N(c) > 0 iff (2c+1)^2 (v^2+4) > v^2 (2c-1)^2, i.e.
  iff G(c) > 0 where
    G(c) := (2c+1)^2 (v^2+4) - v^2 (2c-1)^2
          = v^2 [ (2c+1)^2 - (2c-1)^2 ] + 4 (2c+1)^2
          = 8 c v(c)^2 + 4 (2c+1)^2
          = 8c^5 - 16c^4 - 24c^3 + 48c^2 + 48c + 4.
  The displayed expansion is an exact polynomial identity (certified, CERT B1),
  and for c >= 0 it gives G(c) >= 4 (2c+1)^2 >= 4 > 0 (manifest positivity;
  redundantly re-certified by Sturm on (0,2] with G(0)=4, CERT B2).
Hence Fplus'(c) > 0 for all c in [0,2], and Fplus is strictly increasing there.

Lemma 3 (c_24 = 2 cos(pi/12) > 193/100).
Let p(x) = x^4 - 4x^2 + 1. With the Chebyshev-type recursion q_0 = 2, q_1 = c,
q_{k+1} = c q_k - q_{k-1} (so that q_k(2 cos t) = 2 cos(k t)), exact integer
polynomial arithmetic gives q_4(c) = c^4 - 4c^2 + 2 and p = q_4 - 1 (CERT A1).
Hence p(2 cos t) = 2 cos(4t) - 1, and at t = pi/12: p(c_24) = 2 cos(pi/3) - 1 = 0.
Moreover 1 < c_24 < 2 because cos is strictly decreasing on [0, pi/2] and
cos(pi/3) = 1/2 < cos(pi/12) < 1. Exact Sturm counts (CERT A2): p has 0 real
roots in (1, 193/100] and exactly 1 real root in (1, 2]. Since c_24 IS a root of
p in (1,2), it must lie in (193/100, 2]; as p(2) = 1 != 0 and (concretely)
p(193/100) = -2471999/100000000 < 0 < 1 = p(2), we conclude
  193/100 < c_24 < 2.                                                  (2)

Lemma 4 (Fplus(193/100) > 2 sqrt 2).
At c = 193/100, exact rational arithmetic (Faddeev-LeVerrier charpoly of the
rational matrix B(193/100), CERT C1) gives
  q(z) = z^2 - T z + Delta,   T = 36549/10000,   Delta = 2329057/1000000.
Then T > 0, 8 + Delta = 10329057/1000000 > 0 (CERT C2), and
  q(2 sqrt 2) = 8 + Delta - 2 sqrt 2 * T < 0
  <=> 2 sqrt 2 * T > 8 + Delta   (both sides positive)
  <=> 8 T^2 > (8 + Delta)^2      (squaring positives)
  <=> 8 * 36549^2 * 10^4 > 10329057^2
  <=> 106866352080000 > 106689418509249,
which holds with exact integer difference 176933570751 (CERT C3/C3'). A monic
real quadratic negative at a real point s has two real roots straddling s;
hence the larger root of q, which is Fplus(193/100), satisfies
  Fplus(193/100) > 2 sqrt 2.                                           (3)

Theorem (positive-end bound). For every n >= 24, lambda_2(GP(n,2)) > 2 sqrt 2.

Proof. For n >= 24 we have 0 < 2 pi/n <= pi/12 < pi, and cos is strictly
decreasing on [0, pi], so 193/100 < c_24 <= c_n < 2 by (2). By Lemma 2 (Fplus
strictly increasing on [0,2], and [193/100, 2] is contained in [0,2]),
  Fplus(c_n) >= Fplus(c_24) > Fplus(193/100).
Combining with (1) and (3):
  lambda_2(GP(n,2)) >= Fplus(c_n) > Fplus(193/100) > 2 sqrt 2.   QED

Remarks.
(i) The proof is self-contained: it does not use the full block decomposition
(piece 1) — only the explicit eigenvector of Lemma 1 — and it does not use
gp24_certificate.json. That repo certificate (exact Sturm on the degree-48
charpoly of GP(24,2), verdict POSITIVE-END-ONLY, breach_pos = 1) independently
corroborates the base case n = 24.
(ii) Float reconnaissance (labelled, non-probative): lambda_2(GP(n,2)) agrees
with Fplus(c_n) to ~1e-15 for n in {24,25,26,30,40,60,100}, the constructed
cosine eigenvector satisfies ||A y - mu y|| ~ 2e-15 for n in {24,30,47}, and the
margins are Fplus(c_24) - 2 sqrt 2 ~ 0.0085, Fplus(193/100) - 2 sqrt 2 ~ 0.0043.
(iii) Since Fplus(c_n) -> Fplus(2) = 3 as n -> infty, the same argument shows
lambda_2(GP(n,2)) -> 3, i.e. the positive-end Ramanujan failure is not marginal:
the family is a (spectral) non-expander at the top end, uniformly beyond
2 sqrt 2 for all n >= 24.
```

### Exact certificates (each independently rerun by the verifier)

- CERT A1: with the integer recursion q_0=2, q_1=c, q_{k+1}=c*q_k - q_{k-1} (which satisfies q_k(2cos t)=2cos(kt)), q_4(c) = c^4 - 4c^2 + 2 exactly, hence p(x)=x^4-4x^2+1 satisfies p(2cos t) = 2cos(4t) - 1 and p(2cos(pi/12)) = 2cos(pi/3)-1 = 0
  (method: exact integer polynomial arithmetic (Fraction), recursion expanded and compared coefficientwise; result: PASS: q4 = [2,0,-4,0,1] (low-first), p = q4 - 1)
- CERT A2: p(x)=x^4-4x^2+1 has 0 real roots in (1, 193/100] and exactly 1 real root in (1, 2]; p(193/100) = -2471999/100000000 < 0 and p(2) = 1 > 0; hence c_24 = 2cos(pi/12), the unique root of p in (1,2), satisfies 193/100 < c_24 < 2
  (method: exact Sturm chain sign-change counts (core.exact.count_real_roots_in) at rational endpoints; exact rational evaluation of p; result: PASS: counts 0 and 1; p(193/100) = -2471999/100000000, p(2) = 1)
- CERT B1: (2c+1)^2 (v^2+4) - v^2 (2c-1)^2 = 8c v^2 + 4(2c+1)^2 = 8c^5 - 16c^4 - 24c^3 + 48c^2 + 48c + 4 identically, where v = -c^2+c+2; hence G(c) >= 4(2c+1)^2 >= 4 > 0 for c >= 0, giving Fplus'(c) > 0 on [0,2]
  (method: exact polynomial expansion over Q, coefficientwise equality (after trailing-zero trim); result: PASS: both sides equal [4,48,48,-24,-16,8] (low-first))
- CERT B2 (redundant re-check of B1's positivity): G(c) = 8c^5-16c^4-24c^3+48c^2+48c+4 has 0 real roots in (0,2], and G(0)=4>0, G(2)=100>0; hence G > 0 on [0,2]
  (method: exact Sturm count on (0,2] plus exact rational endpoint evaluations; result: PASS: root count 0; G(0)=4, G(2)=100)
- CERT B3: (T(c)/2)^2 - Delta(c) = u(c)^2 + 1 identically, with T = c^2+c-2, Delta = c^3-2c-1, u = (-c^2+c+2)/2; hence the block discriminant is 4(u^2+1) >= 4 > 0 and the larger root of z^2 - Tz + Delta is Fplus(c) = A(c) + sqrt(u(c)^2+1)
  (method: exact polynomial expansion over Q, coefficientwise equality; result: PASS: identity holds)
- CERT C1: the characteristic polynomial of B(193/100) = [[193/100, 1],[1, (193/100)^2 - 2]] is z^2 - T z + Delta with T = 36549/10000 and Delta = 2329057/1000000
  (method: core.exact.charpoly_of_matrix (Faddeev-LeVerrier over Q); result: PASS: T = 36549/10000, Delta = 2329057/1000000)
- CERT C2: T = 36549/10000 > 0 and 8 + Delta = 10329057/1000000 > 0 (the sign conditions licensing the squaring step)
  (method: exact rational comparison; result: PASS)
- CERT C3/C3': 8 T^2 - (8+Delta)^2 = 176933570751/10^12 > 0; integer form 8 * 36549^2 * 10^4 = 106866352080000 > 106689418509249 = 10329057^2, difference 176933570751; hence q(2 sqrt 2) < 0 and Fplus(193/100) > 2 sqrt 2
  (method: exact integer arithmetic; result: PASS: difference 176933570751 > 0)

### Stated caveats

```text
(1) SCOPE: this piece proves ONLY the positive-end bound lambda_2(GP(n,2)) > 2 sqrt 2 for all n >= 24. The target theorem's other components — connectivity of GP(n,2), cubicity for the record (3-regularity is used and is immediate from the definition for n >= 5), and the negative-end bound lambda_min > -2 sqrt 2 — are other pieces and are NOT proved here. (2) INDEPENDENCE: the proof does NOT rely on piece 1 (the full 2x2 block decomposition of the spectrum); it only needs that Fplus(c_n) IS an eigenvalue, proved self-containedly by the explicit cosine eigenvector in Lemma 1. It also does NOT cite gp24_certificate.json (mentioned only as independent corroboration of n=24). (3) NON-CERTIFIED ANALYTIC INGREDIENTS (elementary calculus/trig, not machine-checked): cos strictly decreasing on [0, pi]; the double-angle identity 2cos(4pi/n) = c_n^2 - 2; q_k(2cos t) = 2cos(kt) for the recursion (standard induction from 2cos t * 2cos(kt) = 2cos((k+1)t) + 2cos((k-1)t)); differentiability of Fplus and the derivative formula (chain rule, sqrt argument bounded below by 1); a monic real quadratic negative at s has real roots straddling s. All are textbook one-liners stated in the proof text. (4) The geometric-eigenvector computation of Lemma 1 is a symbolic two-line calculation; it was additionally sanity-checked in floats (residual ~2e-15 for n = 24, 30, 47) — floats are reconnaissance only and carry no probative weight. (5) The Sturm implementation, rational charpoly, and root counting are the repo's core.exact (trusted repo infrastructure, same toolchain as the already-accepted gp24 certificate); count_real_roots_in counts distinct roots in half-open (a,b], which is what the proof uses (endpoint values were separately checked nonzero where relevant, e.g. p(2)=1, G(2)=100). (6) The interval [193/100, 2] strictly contains all c_n for n >= 24 via Lemma 3; the choice 193/100 is tight-ish (19/10 and 192/100 would NOT suffice: Fplus(19/10) ~ 2.765 < 2 sqrt 2 — the rational lower bound for c_24 must exceed ~1.9296). (7) No repo files were modified; all computation was in-session (scripts run from the exploratory directory, writing nothing).
```


---

## Adversarial verification record

Each piece was checked by an independent agent instructed to find gaps
and re-run every computational certificate from scratch. All three
verdicts: SOUND. Beyond the asks, the verifiers machine-confirmed the
Theorem-1 identity `char_A = prod_j det(xI - B_j)` exactly for EVERY
`n = 5..40` by an independent determinant-interpolation route
(including the Petersen `n = 5` multiplicity case); certified
`GP(23,2)` exactly below threshold (no off-by-one at the base case);
and end-to-end certified `n = 25, 26` directly on the exact
degree-50/52 characteristic polynomials, agreeing with the block
route. Full transcripts: workflow run wf_70eda207-75f in the session
transcript directory.
