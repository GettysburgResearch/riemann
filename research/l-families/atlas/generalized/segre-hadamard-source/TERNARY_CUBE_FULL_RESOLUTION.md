# Actual higher maps in the marked ternary Chow resolution

Status: source construction and staged verification contract; the coordinating
agent's stage results and final validation must be recorded separately before
this packet is treated as executed. The author runs no scientific jobs.

The module and its general theorems are classical. We use the same finite Chow
module as the preceding source packets, with their explicit attribution to
Raicu–Sam–Weyman, *On some modules supported in the Chow variety*,
[arXiv:2108.10910](https://arxiv.org/abs/2108.10910). This packet's task is to
construct the actual remaining polynomial maps in one marked resolution,
rather than to infer their existence from an alternating numerator.

## 1. The frozen source and what remains to be constructed

Let `V=Q^3`, `W=Sym^3 V`, `S=Sym(W)` with its ten degree-one generators, and
`R=direct_sum_j (Sym^j V) tensor (Sym^j V) tensor (Sym^j V)`.
The map `W -> R_1` is the literal symmetric sum of tensor words. The complete
marked first presentation is frozen at
`4c635b2ee8d7cf6caa41efde2d2e0c7baea1b787`:

`F1 --D1--> F0 --epsilon--> R -> 0`,

where `F0=S +17S(-1)+11S(-2)` and `F1=20S(-2)+65S(-3)`.
All 29 generator lifts and all 85 D1 polynomial columns are given there.
The proof of its global exactness uses the actual low-degree Koszul homology,
not only a Hilbert-series match.

The imported Chow-module theorem makes R Cohen–Macaulay of dimension seven
over the ten-variable polynomial ring, with projective dimension three.
Its canonical-module calculation gives the actual graded Tor duality

`Tor_(3-i,7-j)(R,Q) = Tor_(i,j)(R,Q)^* tensor det(V)^7`.

Thus the full weight tables, not merely total dimensions, predict

`F2=65S(-4)+20S(-5)`,
`F3=11S(-5)+17S(-6)+S(-7)`.

The new calculation must construct D2 and D3. It may use these predictions
only as independent checks after computing the source kernels and quotients.
The degree-four acquisition at `1a5a63f1148fb884e9ae7aae9e9324a40aee9f33`
has already supplied 65 genuine D1-kernel columns with a frozen exact digest.
That acquisition is reconstituted, not replaced by a newly chosen basis.

## 2. Actual graded maps and exact minimality quotients

For any marked free module, the degree-j basis is ordered first by the marked
generator and then by lexicographic weak compositions in the ten polynomial
variables. If a column of D has an entry `c*x^alpha` at target generator g,
its multiple by `x^beta` has the literal entry `c*x^(alpha+beta)` at g.
This rule constructs each finite graded matrix directly from the frozen D1
or from already computed higher polynomial columns.

Every term is checked for degree and torus weight, and every original-coordinate
kernel witness is substituted into that graded matrix. Rational elimination
keeps a witness in the original domain while reducing its image. A dependency
therefore supplies an explicit polynomial vector, not merely a nullity count.
Denominators are cleared and the integer vector is normalized by its gcd and
the sign of its final nonzero coordinate. These markings are deterministic;
they are not asserted to be equivariant choices under all of GL3 or factor S3.

The required stages are:

| Map and internal degree | Full domain dimension | Kernel dimension | Actual old rank | New columns |
| --- | ---: | ---: | ---: | ---: |
| D1, degree4 | 1750 | 65 | 0 | 65 for D2 |
| D1, degree5 | 7975 | 659 | 639 from650 old multiples | 20 for D2 |
| D2, degree5 | 670 | 11 | 0 | 11 for D3 |
| D2, degree6 | 3775 | 127 | 110 from110 old multiples | 17 for D3 |
| D2, degree7 | 15400 | 776 | 775 from775 old multiples | 1 for D3 |

These numbers are preregistered predictions until the corresponding exact
stage passes. In every noninitial stage, the old subspace is constructed by
literal multiplication of all previously selected columns by every monomial
of the required complementary degree. Each such vector is checked to lie in
the current kernel. A new class is selected only if exact elimination shows
it increases the span of that old subspace and previously selected new classes.
The final span is checked to have the dimension of the complete computed
kernel. In particular the rank639 is not assigned by subtracting11 from650.

All minimal columns have strictly positive polynomial degree in every nonzero
entry. Their complete weight multiplicities are compared with the frozen dual
tables, by `weight -> (7,7,7)-weight`. The comparison is made against the actual
frozen D1 and F0 weight records, independently of the higher elimination.

## 3. Why the staged computation gives a complete resolution

This section is a conditional implication from the declared exact stage checks
and the frozen source theorems. It explains the global step which no finite
matrix census by itself could supply.

Put `K0=ker(F0 -> R)` and `K1=ker(D1:F1 -> F0)`. The first presentation is
minimal and globally exact. Its long exact Tor sequences imply

`K1/S_+K1 = Tor_2^S(R,Q)`.

The frozen Tor theorem places this quotient precisely in degrees four and
five, with the displayed weight tables. The degree-four calculation gives
the full kernel in its first possible degree. In degree five the old
subspace is exactly `(S_+K1)_5`, because the only lower degree is four.
The 20 selected quotient classes therefore supply all remaining minimal
generators. Since S is Noetherian and K1 is finitely generated, graded
Nakayama proves that the 85 actual D2 columns generate K1 in every degree.

Now let `K2=ker(D2:F2 -> F1)`. The same argument gives

`K2/S_+K2 = Tor_3^S(R,Q)`.

This quotient occurs precisely in degrees five, six and seven. At degree six
its old part consists of variable multiples of the degree-five classes. At
degree seven it consists of all quadratic multiples of degree-five classes
and variable multiples of degree-six classes. The explicit old-span checks
are exactly these spaces; they do not remove a source relation by a selected
trace or character. The 29 computed D3 columns therefore generate K2 globally.

Finally, put `K3=ker(D3:F3 -> F2)`. Minimality of this free cover identifies
`K3/S_+K3` with `Tor_4^S(R,Q)`, which vanishes because the imported projective
dimension is three. Another application of graded Nakayama gives K3=0.
Consequently the resulting complex

`0 -> F3 --D3--> F2 --D2--> F1 --D1--> F0 -> R -> 0`

is the complete minimal free resolution. This proof does not replace an
uncomputed D3 matrix by a formal transpose of D1. It uses the actual maps and
minimality quotients, then the independently established Tor theorem to rule
out further generators and higher homology.

## 4. Certificate, negative controls and scope

The certificate retains every minimal polynomial column and every exact kernel
witness in the original free-module coordinates. Old-multiple quotient
matrices are retained explicitly. Expanded ambient matrices have reproducible
ordered basis specifications, complete column weights, block ranks and bit
statistics, and streamed basis/column digests. Their coefficients are uniquely
reconstructed from the retained polynomial maps; the artifact need not repeat
tens of thousands of ambient zero rows.

The checker reconstructs these objects from the authenticated source. Altering
one coefficient of an actual D2 or D3 column is tested by its resulting nonzero
composition. Numerical aliases in JSON, changed source identities, and changed
coverage are rejected. Bounds are checked before any out-of-cap elimination.

This is one marked characteristic-zero resolution of the actual Chow module.
Its torus homogeneity does not provide an equivariant choice of all minimal
splittings, a new general finite-resolution theorem, or a finite operator whose
superdeterminant is automatically the additive K-polynomial. No arithmetic
Frobenius or RH assertion is made.
