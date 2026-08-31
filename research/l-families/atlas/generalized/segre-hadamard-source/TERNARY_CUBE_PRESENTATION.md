# Actual first differential of the ternary Chow module

The result here is a marked, explicit first presentation of
`R = direct_sum_r (Sym^r V)^{tensor 3}` over `S = Sym(Sym^3 V)`, for `V = Q^3`.
It is a source-map continuation of the corrected Chow-base construction, not a
claim that a scalar numerator determines a complex. The rank-three, third-power
case and its characters have already been used in this programme. The additional
deliverable is the actual multiplication matrices and 85 relation columns.

All numerical assertions below are preregistered predictions until the exact
parent-run replay passes. See the execution record in `PRESENTATION_REPLAY.md`.
The theorem's computational hypotheses are stated explicitly rather than
silently promoted from those predictions.

## SHP1. Source and fixed markings

Fix an ordered basis `(v0,v1,v2)` of `V` and the ordered three tensor factors.
For a weak composition `a` of three, let `w_a` be the sum of the tensor words
of content `a`, with coefficient one for each word. These ten vectors are a basis
of the embedded `W = Sym^3 V`. They define the algebra map `S -> R`.

A monomial basis vector of `R_r` is a three-by-three nonnegative integer matrix
whose rows each sum to `r`. The product of two such vectors adds the matrices.
All ordered bases are lexicographic. Hence the image in `R` of every monomial of
`S` is determined without a character calculation or fitted recurrence.

The new generator lifts are chosen by the following rule. Start with `1`. In
degree one, put the ten `w_a` columns into an exact echelon basis, then append
source monomials in order when they increase its rank. In degree two, do the same
after all products of the generators already chosen. Every operation is within
one total `V`-weight, using rational arithmetic. This is deterministic relative
to the marking and preserves the diagonal torus grading.

An important limitation is deliberate: the chosen complement is not asserted
to be an equivariant splitting for `GL(V)` or factor permutation. A concrete
factor permutation sends one selected degree-one monomial to a source monomial
outside the span of the selected degree-one monomials. Its class in `R_1/W`
still transforms equivariantly; a `W` correction is needed in the chosen lift.
The producer retains this witness. The canonical objects are the multiplication
map and the Tor quotient, not the marked section.

## SHP2. Exact bounded maps and relation extraction

The source replay independently verifies that the preceding rule gives
`1,17,11` generators in degrees `0,1,2`. Define the associated free module

`F0 = S + S(-1)^17 + S(-2)^11`

and the map `epsilon: F0 -> R` by these actual monomial lifts. In degree two,
the domain has dimension `55 + 170 + 11 = 236`; the source has dimension `216`.
In degree three the dimensions are `220 + 935 + 110 = 1265` and `1000`.

For each of these two degrees, form every column by multiplication. Eliminate
within weights, retaining an identity witness whenever an input column reduces
to zero. Such a witness is a kernel vector in the **original** free-domain
coordinates, not merely a zero row of a reduced matrix. Clear its denominators,
divide the coefficient gcd, and choose the last nonzero coefficient positive.
Direct substitution verifies that each resulting integer relation maps to zero.

The required exact results are:

| degree | rank of epsilon | kernel dimension |
|---|---:|---:|
| 2 | 216 | 20 |
| 3 | 1000 | 265 |

Multiply each of the 20 degree-two kernel vectors by each of the ten variables.
The resulting 200 columns are computed in the original degree-three domain.
Their rank is separately verified to be 200. Greedily append degree-three kernel
vectors independent of their span; exactly 65 are required. Thus the producer
constructs the actual polynomial map

`D1: F1 = S(-2)^20 + S(-3)^65 -> F0`

and verifies `epsilon D1 = 0`, the rank statements above, and positive polynomial
degree of every matrix entry. It retains the 85 polynomial columns, not just
their character, rank, or hash. It also retains both complete sparse evaluation
matrices and the 200-column old-relation multiplication matrix.

## SHP3. Why this is a complete first presentation

This global statement uses more than bounded matrix exactness. The independently
computed low-degree Koszul complexes in source freeze
`a895f47628b0bc7c7ee5e0392df2f79c24166f92` give the actual weight dimensions
of `Tor_i^S(R,Q)` through internal degree three. The computation here checks the
weight dimensions of its new generators and relations against those frozen
quotients; it does not use them to manufacture the maps.

The imported Chow-module theorem `MATHEMATICS.md`, SHS1–SHS2, gives finiteness,
Cohen–Macaulay dimension seven, projective dimension three, and duality

`Tor_(3-i,7-j) = Tor_(i,j)^* tensor det(V)^7`.

These are the classical finite Chow-module and canonical-module results, with
the exact conventions proved in that note and credited to Raicu–Sam–Weyman,
*On some modules supported in the Chow variety*,
[arXiv:2108.10910](https://arxiv.org/abs/2108.10910),
§2 and §3. The explicit presentation below is a marked calculation in that
classical module; no novelty claim is made for the general existence theorems.

The frozen complexes have `Tor_0` dimensions `17,11,0` in degrees `1,2,3`,
and `Tor_1` dimensions `0,20,65`. Their `Tor_2` and `Tor_3` entries through
degree three are zero. Duality and nonnegative grading therefore show that
`Tor_0` has no other positive-degree generators and `Tor_1` has no other
relations. Degree zero is the single unit. This conclusion uses the actual
homology and duality, not the signed numerator `1+17t-9t^2-65t^3+...`.

Graded Nakayama now proves that the 29 chosen lifts generate `R` over `S`.
Let `K = ker(epsilon)`. Because `F0` is a minimal free cover, the exact sequence
gives `K/S_+K = Tor_1^S(R,Q)`. Its degree-two part is the 20 computed kernel
vectors. Its degree-three part is the kernel modulo the actual variable
multiples of those vectors, with dimension 65. There is no higher part.
Consequently the 85 columns generate `K`, again by graded Nakayama. Therefore

`F1 --D1--> F0 --epsilon--> R -> 0`

is exact and minimal. The global conclusion is conditional only on the stated
classical hypotheses and the frozen and new exact source calculations; these
imports and the new calculation require independent review before release.

This does **not** assert that `D1` is injective. The higher free modules have ranks
85 and 29 from the separately recorded Tor theorem, but their differential
matrices have not been constructed here. Nor does the marking turn this matrix
presentation into an equivariantly chosen minimal resolution.

## SHP4. Falsifiers and resource scope

The smallest falsifiers are a single retained relation with nonzero source
substitution, an old-relation multiplication rank below 200, or a disagreement
between the computed generator/relation weight multiplicities and frozen Tor.
A signed-numerator match would not repair any of those failures.

The negative controls alter an actual relation coefficient and show its image
becomes nonzero, reject incorrect claimed equivariant-section behavior, reject
out-of-cap inputs before cached computation, and reject Boolean/float/integer
counterfeit JSON values even when the old stored proof hash is unchanged.

All work is bounded at source degree three. The largest ambient evaluation
matrix has 1000 rows and 1265 columns, but only weight blocks are eliminated.
There is no characteristic-p rank inference, floating arithmetic, prime search,
external CAS, or executable import of the predecessor. See the preregistration
for the resource caps and the separate parent-run scout before full replay.
