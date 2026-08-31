# Actual first presentation of the ternary cube: preregistration

This is a new source-map calculation, not a refit of the signed Hilbert numerator.
The rank-three, third-power example is a comparison case already used by this
programme and by the separately credited full-ambient bridge. Its **actual
Chow-base presentation maps** are the new deliverable here. No novelty is claimed
for existence of a finite presentation or the classical Chow-module construction.

Let `R_r = (Sym^r Q^3)^{tensor 3}` and
`S = Sym(W)`, where `W = Sym^3 Q^3` enters `R_1` by the literal coefficient-one
orbit sums. All calculations use characteristic-zero rational arithmetic. The
frozen source is `a895f47628b0bc7c7ee5e0392df2f79c24166f92`; no executable
predecessor is imported.

## Fixed choices and predictions, before execution

Order weak compositions lexicographically. A basis of `R_r` is the lexicographic
product of three degree-`r` compositions, flattened to nine exponents. The ten
variables of `S` are the degree-three compositions of length three, in that order.
The image of a variable is the sum of the tensor words having its content, each
with coefficient one. Multiplication adds the nine exponents.

Start with the unit. At degree one, take the images of the ten variables, then
greedily append the first source basis monomials independent of their span.
At degree two, first take all products of the generators already chosen and then
apply the same greedy rule. Prediction: the resulting minimal generators number
`1, 17, 11` in degrees `0, 1, 2`, respectively.

The resulting free module `F0` has degree-two dimension `236` and degree-three
dimension `1265`; the corresponding source dimensions are `216` and `1000`.
Compute both maps from multiplication, not from dimensions. Predictions:

| grade | actual map rank | kernel dimension | old-relation rank | new relations |
|---|---:|---:|---:|---:|
| 2 | 216 | 20 | 0 | 20 |
| 3 | 1000 | 265 | 200 | 65 |

The 200 old degree-three columns are the ten actual variable multiples of each
degree-two relation. Their independence is to be checked, not assumed. New
relations are greedily chosen from an exact kernel basis modulo those columns.
Every displayed relation is normalized to primitive integer coefficients with
the last nonzero coordinate positive. Every relation is substituted into the
actual source map and must give zero.

These are deterministic choices relative to a marked basis, and are homogeneous
for the diagonal torus. They are **not claimed to be GL3 or factor-S3 equivariant
splittings**. The Tor quotients and the multiplication maps are equivariant; a
marked complement need not be. A factor-permutation control will test this
distinction directly.

## Retained output and resource gates

Retain all 29 generator lifts, all 85 polynomial columns of the first
differential, and both full sparse source evaluation matrices. Retain the ordered
bases needed to interpret them, the old-relation multiplication matrix, complete
weight-block ranks, and hashes binding the complete record. A digest alone is
not a substitute for the matrices.

The first parent-serialized scout computes only through degree two. The full job
then extends to degree three. Declared caps are source grade 3, 1000 source rows,
1265 evaluation columns, 512 rows/columns per weight block, 4096-bit exact
numerators or denominators, and a 16 MiB serialized result. No random sampling,
finite-characteristic rank inference, CAS, matrix fitting, or expanded higher
degree module is allowed. Root must run and measure jobs; the writer runs none.

## Global scope gate

The bounded maps prove the displayed composition is zero and the asserted
degree-two/three exactness. Their promotion to a complete first presentation
also uses the frozen actual Koszul homology, the proved Chow-module duality, and
graded Nakayama: `Tor0` has no generators beyond degree two and `Tor1` has no
relations beyond degree three. This imported scope must receive independent
proof review. The packet constructs `F1 -> F0 -> R`; it does not construct the
second and third differential matrices or infer them from Betti numbers.
