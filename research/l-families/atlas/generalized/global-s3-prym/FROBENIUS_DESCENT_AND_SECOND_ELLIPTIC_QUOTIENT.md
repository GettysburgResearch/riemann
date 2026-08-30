# Frobenius-orbit descent and a second elliptic quotient

Status: proposed extension of the Kummer tower frozen at
`ed8139953de75d5ef0d1c9fab5402360b7b7e9b7`.
Scope: tame smooth function-field sources; no integer-source transport or
number-field RH claim. No external priority for the classical geometry is claimed.

This extension removes the assumption that all deck roots of unity lie in
the base field. Individual geometric character spaces can then fail to be
Frobenius stable. The correct determinant belongs to a whole Frobenius orbit.
In the cubic case that descent forces an elliptic factor, which also has
an explicit second quotient curve as its source.

## 1. Arithmetic descent of the geometric Kummer decomposition

Keep `E:y^2=x^3+Ax+B`, with A!=0, nonzero discriminant and characteristic
p not dividing 6m. Let k=F_q, but no longer require q=1 modulo m. Work over
the algebraic closure with Q_ell(zeta_m) coefficients, ell not dividing pm,
and form `C_m:w^(2m)=x^3+Ax+B`. The genus and geometric deck-character
dimensions from the frozen tower theorem remain unchanged after extending
constants:

    dim H_0=2,
    dim H_j=4-1_(order(j)=3),  j!=0.

Choose sigma:w->eta*w over the algebraic closure. With the previously
specified pullback and geometric-Frobenius convention, F sends

    H_j -> H_(qj),                                         (FD-1)

where character indices are modulo m. Indeed geometric Galois Frobenius
conjugates eta to eta^(q^-1), so
`F sigma* F^-1 = (sigma*)^(q^-1)`; applying this to an eigenvector gives
(FD-1). The coefficient field is kept fixed by this linear action.

Let O be an orbit of multiplication by q, with length r, and choose j in O.
The direct sum H_O is Frobenius stable, while a single H_j generally is not.
Then

    P_O(T) = det(1-TF | H_O)
           = det(1-T^r F^r | H_j).                        (FD-2)

To prove (FD-2), use the cyclic block decomposition. The trace of F^n
vanishes unless r divides n; if n=rs, it is r times the trace of (F^r)^s
on H_j. Substitution into the formal determinant logarithm proves the
identity coefficient by coefficient. In particular the right side is the
actual character factor over F_(q^r), evaluated at T^r; it is not a base-field
degree-dim(H_j) determinant obtained by pretending H_j was stable.

The product of P_O over all character orbits is the numerator of C_m.
Each orbit factor lies in the appropriate cyclotomic coefficient field;
one q-orbit need not be a full orbit under the cyclotomic Galois group.
Consequently no rational-coefficient claim is made for an arbitrary single
orbit. The full product has integer coefficients. In the inverse pair for
order three considered below, the orbit is the full nontrivial cyclotomic
Galois orbit, and its coefficients are integers.

Cup product pairs H_O with H_(-O). If O=-O, it restricts to a perfect
alternating pairing on H_O. The usual curve Frobenius is a q-similitude
for that pairing, so dim H_O is even, its determinant is q^(dim H_O/2),
and P_O has the corresponding self-reciprocity. Distinct inverse orbits
instead obey the paired equation of the frozen tower theorem.

## 2. The order-three inverse orbit forces a factor

Assume 3 divides m and q=-1 modulo three. The two order-three characters
form a single orbit O of length two. Each character space has dimension
three, so H_O has dimension six. By (FD-2), write

    P_O(T)=Q(T^2),  deg Q=3.

The perfect alternating pairing on H_O gives

    P_O(T)=q^3 T^6 P_O(1/(qT)),
    Q(S)=q^3 S^3 Q(1/(q^2 S)).                            (FD-3)

At S=-1/q, (FD-3) is Q(S)=-Q(S), hence Q(-1/q)=0. Thus

    1+qT^2 divides P_O(T).                                (FD-4)

The sign is fixed: the forced factor is 1+qT^2, not 1-qT^2. Writing the
remaining integer coefficient as b gives

    P_O(T)=(1+qT^2)(1+bT^2+q^2T^4).                      (FD-5)

The curve weight theorem implies |b|<=2q. This is an imported weight
statement applied to a source-defined direct summand; neither finite
point samples nor the earlier positive fibre projector proves it.

## 3. The changed ramified factor at infinity

For the cubic Kummer tower C_3 there are three geometric points at infinity,
indexed by the cube roots of one in the leading ratio `w^2/x`. When
q=-1 modulo three, Frobenius fixes the identity root and interchanges the
other two. The original elliptic quotient E has one rational infinity point.
After removing its constant fibre contribution, the descended order-three
pair therefore has infinity determinant

    1-T^2,    hence Euler factor (1-T^2)^(-1).             (FD-6)

It cannot be replaced by two independent `(1-T)^(-1)` factors over F_q.
Its infinity trace is zero in odd extension degrees and two in even
degrees. The complete C_3 infinity contribution is correspondingly one
or three; the elliptic E contribution is always one.

At the sheaf level the descended pair has generic rank four. Its tame
drops are four at zero, two at each of the four old finite branch points,
and two at infinity. The total 14 gives Euler characteristic 8-14=-6,
consistent with the degree-six cohomological determinant. The determinant
proof already follows from the frozen geometry and cyclic block identity.

## 4. A second elliptic quotient explains the forced factor geometrically

For m=3 there is an additional degree-two map

    C_3 -> E',   z=w^2,
    E': z^3=x^3+Ax+B.                                    (FD-7)

The projective equation is

    Z^3=X^3+AXT^2+BT^3.

It is smooth: on the affine chart a singularity would require z=0 and a
repeated root of the cubic; at infinity both X and Z are nonzero and the
corresponding partial derivatives are nonzero because p!=3. It is a smooth
plane cubic, hence genus one, with the rational point (1:1:0). Thus E' is
an elliptic curve, specified before any polynomial factorization.

When q=-1 modulo three, the cube map is bijective on F_q. There is exactly
one affine z for each x, and exactly one rational infinity point. Therefore

    #E'(F_q)=q+1,   P_(E')(T)=1+qT^2.                    (FD-8)

Pullback on H1 is injective for both finite quotient maps, using pullback
followed by trace equal to the map degree. The two elliptic images are
disjoint. Under the full geometric mu_6 action on C_3, H1(E) is the
order-two character (index three), H1(E') is the two order-three characters
(indices two and four), and the residual space is the primitive order-six
pair (indices one and five). These are distinct character summands.

The dimension assertion for E' can also be read directly from its order-three
automorphism: the invariant part is H1 of its P1_x quotient, hence zero;
duality makes the two nontrivial character dimensions equal, so each is one.
The full C_3 genus is four. We obtain an actual Frobenius-stable splitting
over a coefficient field, with rational character projectors for these three
unions, and hence

    P_(C_3)(T)=P_E(T) P_(E')(T) P_R(T),    deg P_R=4.     (FD-9)

The character projectors are sums over full cyclotomic Galois orbits. Thus
their cohomological summands descend rationally; alternatively the formal
quotient of the integer curve polynomials, once polynomiality is known,
shows P_R has integer coefficients. The residual union is stable under
inversion, so cup product is nondegenerate on it.

Since p>3 and q=-1 modulo three imply q=-1 modulo six, Frobenius interchanges
the two primitive-six character spaces. Their equal dimensions are two.
Equation (FD-2) and the residual pairing therefore give

    P_R(T)=1+bT^2+q^2T^4.                                (FD-10)

This proves that the factor in (FD-4) comes from the explicit elliptic
quotient E', rather than an accidental zero of a fitted polynomial. The
residual factor resembles the polynomial of an elliptic Weil restriction,
but no such isogeny classification is asserted without an additional theorem.
For m divisible by three the map w -> w^(m/3) pulls this C_3 quotient into
the larger tower and identifies the same order-three contribution.

## 5. Exact finite descent replay and its embedding boundary

The bounded replay uses two curves over F5, m=3, and complete extension
degrees one through six. A separate declared field cap of 15625 elements
and maximum degree six extends the earlier polynomial-field implementation;
none of the frozen earlier files is changed. Compressed field coefficients
require only a few MiB, and all jobs remain serialized.

For even extensions, construct a nontrivial cube root eta in the actual
field model and evaluate the cubic character from `t^((5^n-1)/3)`. The
same character polynomial computed over F25 must govern F_(25^r).
Ordinarily this would require compatible field embeddings and character
labels. Here a special source symmetry removes that ambiguity: F exchanges
the two geometric character spaces and commutes with F^2, so the F^2
character polynomials coincide and are conjugate, hence have integer
coefficients. Reversing eta only interchanges two equal trace sums.

The replay explicitly verifies that every such cyclotomic trace is
rational and that twice it equals the complete C_3-minus-E count. It does
not advertise unrelated primitive-root choices as a general compatible
norm-character system. Three even extension counts reconstruct the cubic
Q; all odd extensions have zero C_3-minus-E difference because the cube
map is bijective there. The base-field determinant is Q(T^2).

An independent route reconstructs the genus-four curve numerator from
its first four complete point counts and the proved reciprocity, then
predicts the fifth and sixth counts. Exact counts of E' and the quotient
identities check (FD-8)--(FD-10), including the sign of the forced factor.
Wrong infinity counts, omitted T^2 substitution and false individual
base-field character factors are explicit negative-control targets.

The completed replay gives the following exact factors over F5:

| (A,B) | P_E(T) | P_(E')(T) | P_R(T) |
| --- | --- | --- | --- |
| (1,1) | 1+3T+5T^2 | 1+5T^2 | 1+10T^2+25T^4 |
| (-1,0) | 1+2T+5T^2 | 1+5T^2 | 1+25T^4 |

In the first row Q(S)=(1+5S)^3; in the second it is
1+5S+25S^2+125S^3. These are finite controls, not an inference that
the residual factor is always a square or always has b=0.

What was actually run: Ruff format and check; primitive `--write`,
`--check` and optimized-Python `--check`; and all 11 dedicated unit tests
in ordinary and optimized Python. Every check passed. The six extension
counts per curve enumerate every point of the declared field, with maximum
field order 15625; no broad repository test-suite claim is made.

All finite computations authenticate only these declared curves and fields.
The all-field orbit determinant, elliptic quotient and pairing statements
are mathematical proofs using the classical finite-pushforward, duality,
curve-weight and genus results already identified in the frozen packets.
