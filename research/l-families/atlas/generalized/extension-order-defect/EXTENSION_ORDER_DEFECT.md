# The boundary module of two extension orders

Status: proposed all-grade source comparison, not integrated mathematics.
Scope: finite-monodromy constructible graded algebras on a curve; explicit
S3 ramification, two different scalar shadows, and arithmetic pole transfer.
Exact predecessor: `c3cdd2528595cbf22c31d88a40c8a611b6385752`, present in
the starting branch head `7b320b3a9a55a16e73d99dd9bbab5bf592d50c93`.
Computation: the companion replay declares its independent primitive checks
and execution separately. No infinite conclusion is inferred from a cutoff.

## 1. Objects, comparison and relative universal properties

Let X be a smooth projective curve over a finite field, j:U->X a dense
open immersion with finite complement D, and K a characteristic-zero
coefficient field. Let A be a commutative nonnegatively graded local-system
algebra on U, with finite-dimensional grades and A_0=K, and let S be a
finite-dimensional local system. Assume their monodromy factors through one
finite group. All constructions below are ordinary sheaf operations on each
finite grading degree. The notation S<2> places S in internal grading degree
two; it is not a cohomological shift.

Define the generic algebra G=A tensor Sym(S<2>) and its two extensions

    B=(direct-sum_m j_*A_m) tensor Sym((j_*S)<2>),
    C=direct-sum_m j_*G_m.

There is a natural graded algebra morphism iota:B->C. At a geometric
boundary point with inertia I its degree-m map is the direct sum, for
0<=k<=floor(m/2), of the inclusions

    A_(m-2k)^I tensor Sym^k(S^I)
                -> (A_(m-2k) tensor Sym^k S)^I.              (1.1)

Indeed each input inclusion is injective, symmetric powers preserve
inclusions of vector spaces, and every vector in the displayed image is
I-fixed. Tensor products and direct sums over a field preserve these
inclusions. On U the map is the identity on G. Stalks therefore show that
iota is injective and give exact sequences

    0 -> B_m -> C_m -> Q_m -> 0                               (1.2)

with Q_m constructible and supported on D. The sum Q is a graded B-module:
B acts on C and preserves its submodule B. It is not the quotient of C
by an algebra ideal, since B contains the unit. No algebra structure on Q
is supplied. In the derived category of the underlying sheaves, the cone
of B_m->C_m is quasi-isomorphic to Q_m in degree zero. Merely renaming this
cone does not produce additional higher defect groups.

The comparison is natural in homomorphisms of A and S. Its two universal
properties are precise but relative. B is the free commutative graded
j_*A-algebra equipped with a K-linear sheaf map j_*S->B_2. C is terminal
among sheaf algebras H equipped with a specified generic map j^*H->G:
the map H->j_*G is exactly the ordinary restriction/direct-image
adjunction. The same statement holds in the subcategory where the generic
map is an isomorphism. Applying these properties gives the displayed iota.

These are classical free-algebra and adjunction statements, not uniqueness
of B among all sources with a given scalar Euler function. In particular
C is a different extension of the same generic algebra. The elementary
sheaf facts are recalled in Stacks Project [03PV](https://stacks.math.columbia.edu/tag/03PV),
[03PZ](https://stacks.math.columbia.edu/tag/03PZ), and the symmetric-algebra
stalk statement [01CH](https://stacks.math.columbia.edu/tag/01CH).
For the finite-monodromy sources here the boundary-stalk description is
the invariant-space construction already fixed in the predecessor.

## 2. Two scalar shadows, with different multiplication laws

Let phi normalize I and denote residual Frobenius at a closed point v.
Put F_A(h,t)=sum_m tr(h|A_m)t^m. Reynolds averaging gives the all-grade
local trace functions

    F_C,v(t)=1/|I| sum_(i in I)
                F_A(phi i,t)/det(1-t^2 phi i|S),
    F_B,v(t)=F_(A^I,phi)(t)/det(1-t^2 phi|S^I),
    F_Q,v(t)=F_C,v(t)-F_B,v(t).                              (2.1)

For each fixed degree m, block-triangularity in (1.2) gives

    L(X,C_m,T)=L(X,B_m,T)L(X,Q_m,T),
    L(X,Q_m,T)=product_(v in D)
          det(1-T^deg(v) phi_v | Q_(m,v))^(-1).              (2.2)

This is the ordinary arithmetic L-function of a finite-grade sheaf.
The exponent deg(v), and Frobenius on the complete cokernel stalk, are
essential. A trace that vanishes does not imply a zero stalk.

For the nonlinear full-place Hilbert Euler functions, instead write

    E_B(z)=product_v F_B,v(z^deg(v)),
    E_C(z)=product_v F_C,v(z^deg(v)).

Where the products initially converge, or as formal series, good factors
cancel and leave the finite rational correction

    E_C(z)/E_B(z)=product_(v in D)
                    F_C,v(z^deg(v))/F_B,v(z^deg(v)).         (2.3)

Equation (2.3) is not equation (2.2) for Q. Nor does it equal the
product over m of L(X,Q_m,z^m). One uses a ratio of sums of characters;
the other uses determinants of the additive cokernel. Section 4 supplies
an exact discrepancy in the fourth coefficient, immediately after the
known degree-three match.

## 3. The actual S3 source and every boundary type

Retain the predecessor's hypotheses: Q=p^f, p>3, and the generic smooth
cubic family y^2=x^3+a x+b with a!=0 and 4a^3+27b^2!=0. The degree-three
map to the y-line has geometric monodromy S3, four old finite C2 branch
points, and C3 inertia at infinity. Adjoin the actual quadratic cover
w^2=y and let chi denote its character. On the common good open set use

    A_m=Sym^m(V) tensor Sym^m(W) tensor chi^m,
    S=V,

where V is the standard rank-two S3 module and W the rank-three
permutation module. The quadratic group acts trivially on S. The generic
character series, before the coherent quadratic sign is inserted, are

    F_e(t)=(1+2t)/(1-t)^4,
    F_s(t)=1/(1-t^2)^2,
    F_c(t)=1/(1-t^3).                                       (3.1)

The standard determinants are D_e(u)=(1-u)^2,
D_s(u)=1-u^2, and D_c(u)=1+u+u^2. Put

    P(t)=1+t+3t^2+t^3,
    R(t)=1+3t^2+t^3+t^4,
    J(u)=1+3u+10u^2+7u^3+3u^4,
    K(u)=1+2u+20u^2+14u^3+22u^4+10u^5+3u^6.                (3.2)

The following table gives exact rational functions in every degree.
At an old finite branch epsilon is the actual residue-field quadratic
sign; at infinity u=t^2. The split/nonsplit distinction is Q modulo3.

| Stratum | F_B(t) | F_C(t) |
| --- | --- | --- |
| Good class (h,epsilon) | F_h(epsilon t)/D_h(t^2) | same |
| New zero, old class h | even(F_h(t))/D_h(t^2) | same |
| Old C2 branch, epsilon | P(epsilon t)/((1-epsilon t)^5(1+epsilon t)^3) | R(epsilon t)/((1-epsilon t)^6(1+epsilon t)^3(1+t^2)) |
| Split infinity | J(u)/((1-u)^4(1+u+u^2)) | K(u)/((1-u)^6(1+u+u^2)^2) |
| Nonsplit infinity | 1/(1-u)^2 | 1/((1-u)^3(1+u)) |

Here even(F)=(F(t)+F(-t))/2. At zero central quadratic inertia kills
the odd A grades, while its action on S is trivial, so extension commutes
with the added S factor in every grade. This proves Q_(m,zero)=0, not
merely vanishing of a first trace.

At an old branch, N_S3(C2)=C2, so residual Frobenius acts on invariant
vectors only by the coherent sign epsilon^m. Formula (2.1) reduces to

    F_C,old(t)=1/2 [F_e(epsilon t)/(1-t^2)^2
                            +F_s(t)/(1-t^4)].              (3.3)

Combining denominators and canceling 1-epsilon t gives the table.
For split infinity, averaging over C3 and projecting onto even grades
gives

    F_C,inf+(t)=1/3 [(1+14u+9u^2)/(1-u)^6
                       +2/((1-u)(1+u+u^2)^2)].             (3.4)

Its common numerator is exactly K(u). For nonsplit infinity the three
elements of the Frobenius coset are transpositions, and even projection
leaves F_s(t)/D_s(t^2), giving the last row. This uses the residual
Frobenius coset, not an invariant dimension substituted for its trace.

## 4. Actual boundary modules and the first scalar-shadow failure

At an old C2 branch choose S=Kx direct-sum Ky with inertia acting by
plus one on x and minus one on y. Both have grading degree two.
Write A=A^+ direct-sum A^- as inertia eigenspaces, so B=A^+[x]. Then,
as graded B-modules,

    C=B[y^2] direct-sum (A^-[x]) y K[y^2],
    Q=y^2 B[y^2] direct-sum (A^-[x]) y K[y^2].               (4.1)

The second summand is a module: the product of two anti-invariant
coefficients belongs to A^+, not to A^-. This is a decomposition using
the actual inertia eigenspaces, not subtraction of fitted dimensions.
It exhibits both mechanisms missed by extending first: invariant
polynomials in noninvariant generators, and crossed invariant tensors.

For epsilon=1, subtraction of the old rows in Section 3 simplifies to

    F_Q,old(t)=t^3(3+2t^2+t^3)
                      /((1-t)^6(1+t)^3(1+t^2)).            (4.2)

For general epsilon substitute epsilon t. In particular Q_0=Q_1=Q_2=0,
dim Q_3=3, and dim Q_4=9. Directly, A_1 is the regular S3 module, so
dim A_1^-=3; A_2 has dimension18 and transposition trace2, so
dim A_2^-=8. Formula (4.1) gives the grade-three crossed term3 and the
grade-four terms8+1. The corresponding B/C degree-three traces are
23epsilon and26epsilon.

At this one rational old branch,

    F_C/F_B = 1+3epsilon t^3+0 t^4+O(t^5),
    product_m det(1-t^m phi|Q_m)^(-1)
              =1+3epsilon t^3+9t^4+O(t^5).                 (4.3)

Indeed F_B has first coefficient3epsilon and F_Q has fourth
coefficient9; division subtracts their product at degree four. Thus the
first Euler characteristic of the additive defect agrees in degree
three, but does not identify the two complete scalar constructions.

At infinity let d_m be the coefficient of F_C,inf+-F_B,inf+ and let
s_m be the coefficient of F_C,inf--F_B,inf-. The former is the
dimension of the actual geometric Q_m stalk. The latter is the trace
of its order-two residual Frobenius when Q is nonsplit. Consequently

    multiplicities_(plus,minus)=((d_m+s_m)/2,(d_m-s_m)/2).    (4.4)

They are nonnegative integers because this is an actual quotient of
finite representations. All odd m vanish. In degree four d_4=13 and
s_4=1, so nonsplit Frobenius has seven plus and six minus eigenvectors;
its ordinary factor is (1-T)^(-7)(1+T)^(-6). A scalar trace1 would
miss twelve dimensions. Split infinity has the factor (1-T)^(-13).
The nonsplit trace series of Q is particularly simple:

    F_Q,inf-(t)=t^4/((1-t^2)^2(1-t^4)).                     (4.5)

Thus all finite-grade ordinary factors of Q are explicit. At an old
closed branch of degree d, they are
(1-epsilon^m T^d)^(-q_m), where q_m is the coefficient of (4.2).
At infinity use (4.4), and at zero there is no factor. These formulas
give the ordinary global L(X,Q_m,T) without suppressing branch degrees.

## 5. The finite rational nonlinear boundary correction

Define

    Xi_2(t)=R(t)/((1-t)(1+t^2)P(t)),
    Xi_3+(t)=K(t^2)/((1-t^2)^2(1+t^2+t^4)J(t^2)),
    Xi_3-(t)=1/(1-t^4).                                    (5.1)

The comparison theorem for the actual source is

    E_C(z)=E_B(z) Xi_inf(z)
                  product_(old closed branches v) Xi_2(epsilon_v z^deg(v)).
                                                               (5.2)

Use Xi_3+ for Q=1 modulo3 and Xi_3- for Q=2 modulo3. Zero makes no
contribution. This is a finite rational identity of source-defined
Euler functions, first proved in their common absolute-convergence
disk and then continued wherever either side is meromorphic.

The correction is not identically one in this S3 family. This can be
proved without guessing the sign of its first coefficient. Xi_2(t)
has a simple pole at t=1 with leading term1/(2(1-t)), while
Xi_2(-1)=1/2. Xi_3+ has a pole of order two at z=1 and Xi_3- has
a pole of order one. Consequently the rational multiplier in (5.2)
has pole order

    2 + number of old closed branches with epsilon=+1,      (split),
    1 + number of old closed branches with epsilon=+1,      (nonsplit)

at z=1. Branch degrees change the nonzero leading constant, not this
order. No negative-sign factor supplies a canceling zero. Thus these
two actual extensions are distinguished even by their global full-place
Euler function. This special calculation is not a general faithfulness
theorem for scalar Euler observables on constructible sources.

## 6. Which arithmetic poles survive reversing the extension order?

Write H=E_B=P_E(z^2)E_chi, the already proved constructible source.
The frozen predecessor gives its meromorphic continuation to |z|<1
and its exact arithmetic pole divisor. The same continuation and
the SAME ENTIRE INTERIOR POLE DIVISOR hold for E_C. This says nothing
about equality of their zero divisors or their Taylor coefficients.

First, (5.2) gives meromorphic continuation because its multiplier is
finite rational. At a positive-weight arithmetic point z_0, every
inverse power z_0^(-d) is an algebraic integer, all its conjugates have
the same modulus greater than one, and its nonzero norm is supported
only at the characteristic prime p. This is the norm lemma in the
frozen arithmetic pole-divisor theorem. The new local numerator
reciprocals are monic integer polynomials with constant terms

    R: 1,       K: 3.                                      (6.1)

The after-source numerators have the same property with constant
terms1 or3; unramified generic factors retain the original constants2
or3. All displayed denominators are cyclotomic. Since p>3, no local
numerator or denominator in the finite ratio (5.2) can vanish at an
arithmetic point. Thus Xi is finite and nonzero there, proving equality
of orders at every arithmetic pole or zero.

It remains to exclude new nonarithmetic poles caused by denominators
of Xi. Let G_good be the common good-place Euler function. The frozen
finite compact-support extraction expresses it on every smaller disk
as finitely many proper cohomological and boundary factors times a
holomorphic Euler remainder. Proper poles are the same positive-weight
arithmetic points; boundary factors have roots on the unit circle.
Hence G_good has no other interior poles. The new bad factors F_C have
only cyclotomic denominators, so E_C=G_good product_bad F_C cannot
acquire nonarithmetic interior poles. Apparent denominator zeros in
(5.2) merely remove zeros already contributed by the old bad factors.

The consequences are exact. If both actual elliptic sectors E,D are
fully resonant, meaning every eigenvalue alpha satisfies alpha^2=Q,
then E_C is holomorphic in |z|<1 and its coefficient root-limsup is1.
Otherwise its first poles have radius Q^(-1/8) and its coefficient
root-limsup is Q^(1/8). These are the after-source dichotomy, now proved
to survive this different extension order. Multiplication by a nonzero
finite rational function cannot remove a meromorphic natural boundary;
therefore E_C retains the unit-circle natural boundary in both cases.

No argument here identifies the two sources, transfers an infinite
operator topology, or supplies an archimedean completion. In particular
the ordinary graded determinant of Q and the rational multiplier Xi
must remain separate even though both arise from the same exact sequence.

## 7. Primitive checks and the next genuine boundary

The companion replay builds V as the sum-zero subspace of the literal
three-letter permutation representation W. It forms finite symmetric
powers and the generic tensor source before applying actual inertia
projectors. The independent low-grade invariant calculation checks
injectivity, the quotient dimensions, and residual transposition traces;
it does not use the rational functions above to construct those spaces.
All-grade rational identities and larger character tables are then
compared with these primitives and with the frozen source. New field
counts are not required: old branch degrees/signs come from the
authenticated source panels, including residue-field signs.

The smallest remaining conceptual gap is unrestricted source uniqueness:
the relative free-algebra and adjunction properties do not classify all
constructible extensions with a prescribed scalar Euler function. Also,
the graded boundary module does not by itself supply a convergent
infinite-rank cohomology theory. Those questions need separately stated
categories, observables and topologies, rather than a reinterpretation
of (1.2) or a low-degree trace match.
