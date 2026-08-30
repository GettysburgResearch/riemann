# The S4 sign sector: explicit polarized elliptic splitting

Retain the frozen Bring-quartic source, with characteristic p>3,
b!=0 and Delta=256c^3-27b^4!=0. Its sign curve is

    D: s^2=h(u^2),      h(r)=256(c-r)^3-27b^4.

This sequel supplies explicit elliptic maps, a polarized degree-four
Jacobian isogeny and its source-defined two-torsion graph. The splitting
is classical even-sextic geometry. The claim is its authenticated
realization in this S4 arithmetic source, not a new general gluing theorem.

## 1. Two quotient maps with specified origins

The two elliptic quotients are

    E+: s^2=h(r),          O+=the cubic infinity,
    E-: S^2=r h(r),        O-=(r,S)=(0,0).

The maps from D are

    phi+(u,s)=(u^2,s),     phi-(u,s)=(u^2,us).          (SS-1)

The cubic h is squarefree and h(0)=Delta!=0, so both targets are smooth
of genus one with the stated rational origins. Their convenient
Weierstrass equations are

    E+: Y^2=X^3-432b^4,
         X=16(c-r), Y=4s;

    E-: Y^2=X^3-768c^2 X^2+768c Delta X-256 Delta^2,
         X=Delta/r, Y=Delta S/r^2.                     (SS-2)

The second birational map extends by sending O- to Weierstrass infinity.
It must not use one of the two quartic infinity points as O-. On D its
affine expression is X=Delta/u^2, Y=Delta*s/u^3 away from u=0.

Let i(u,s)=(-u,s), and let j(u,s)=(u,-s) be the hyperelliptic involution.
The degree-two quotient maps in (SS-1) correspond to i and ij. The first
is ramified at the two geometric points u=0; the second is ramified at
the two geometric points at infinity. These pairs may be nonsplit over
the base field. All divisor statements below use the pairs as rational
divisors and do not assume their individual points are rational.

## 2. Integral polarization and the exact kernel

Define Phi:E+ x E- -> Jac(D) as phi+* + phi-*. The adjoints for the
canonical principal polarizations are the norm maps. Each diagonal
norm-pullback composite is multiplication by two. On Jac(D), j acts as
-1, while the two pullback images have opposite i-eigencharacters.
Their cross norm composites therefore equal their own negatives.
Homomorphism groups of abelian varieties are torsion-free, so the cross
terms vanish integrally, also in positive characteristic. Consequently

    Phi^dagger Phi = diag([2],[2]),
    Phi^*lambda_D = 2(lambda_+ product lambda_-),
    deg Phi = 4.                                       (SS-3)

The map is separable since p!=2. Each individual pullback is injective.
Indeed any nonzero line bundle in its kernel would have order two; the
associated connected etale double cover of its genus-one target would
then admit a degree-one lift from D, contradicting the genera.

Write D_0 for the two points u=0 and D_infinity for the two sextic
infinity points. The origin pullbacks satisfy

    phi+*(O+) = D_infinity,
    phi-*(O-) = D_0,
    D_0 - D_infinity = div(u).                          (SS-4)

If r_i is a root of h, the three nonzero two-torsion points are
P_i=(r_i,0) on E+ and Q_i=(r_i,0) on E-. Their source pullback point
divisors are both the two Weierstrass points u=+-sqrt(r_i), s=0.
Equation (SS-4) makes their degree-zero pullback classes equal. Therefore

    ker Phi = {(0,0), (P_i,Q_i): h(r_i)=0}.              (SS-5)

The graph is defined from the common cubic root, not by matching
Frobenius traces. It is Galois equivariant. Any bijection between the
three nonzero points of two rank-two F2 spaces is linear and preserves
their unique nondegenerate alternating pairing. At order two, the
inverse Weil pairing equals the original pairing, so this is also the
required anti-isometry. The four displayed elements exhaust the kernel
by (SS-3). Equivalently, it is a maximal isotropic subgroup for the
product two-torsion pairing.

In particular the elliptic Frobenius polynomials agree modulo two.
Their integer polynomials need not agree, and equality modulo two alone
would not construct the polarized isogeny.

## 3. Arithmetic factor and forced CM constituent

All maps and polarizations above are defined over the source field, so

    P_D(T) = P_+(T) P_-(T).                             (SS-6)

The first elliptic curve has j=0. Whenever Q=2 mod3, cubing is a
bijection of F_Q. Directly summing the quadratic character of
X^3-432b^4 then gives #E+(F_Q)=Q+1, hence

    P_+(T)=1+QT^2,
    P_D(T)=(1+QT^2)P_-(T).                              (SS-7)

Thus the S4 sign sector has a forced factor in those fields. This is a
consequence of its explicit quotient and the cube bijection. It is not
an unexplained factor fitted from the degree-four numerator, and no
external priority is claimed for the classical CM observation.

Combining (SS-6) with the precursor further refines its full genus-19
factorization. It does not assert that either of the other S4
constituents is irreducible as a Frobenius module.

## 4. Exact replay and proof dependencies

The bounded source replay counts both Weierstrass equations and checks
every rational affine D point under both maps in every declared field.
It handles u=0, the two geometric infinity points, and their rationality
explicitly. It reconstructs both elliptic polynomials from their first
two counts, compares all remaining extension counts, and checks their
product against the separately frozen D polynomial.

For F25 at (b,c)=(1,1), F343 at (1,1), and F7 at (3,4), the common cubic
splits. The replay constructs all four two-torsion points on each
elliptic curve, verifies their group laws, recovers the common-root
graph, and checks all Frobenius and pairing identities. The Frobenius
on point coordinates is x -> x^p; equivariance also holds for its
inverse. Their source
Weierstrass pullback divisors are represented by u^2-r_i, s=0, which
remain defined even when the individual square roots are outside the
field. No complete enumeration of Jac(D) or general-purpose divisor
addition on an even-sextic model is claimed.

The divisor equality (SS-4), integral orthogonality, kernel injectivity
and polarization degree are proved above; they are not inferred from
the finite controls. The imported norm/pullback and polarization facts
are standard, for example Milne,
[Abelian Varieties](https://www.jmilne.org/math/CourseNotes/AV.pdf),
the duality and polarization sections. The earlier source packets retain
their original immutable proofs and acceptance bindings.

Ruff, complete primitive generation, ordinary and optimized producer
checks, and all 14 focused tests in each Python mode passed. The test
suites took approximately 0.05 seconds each. An independent reviewer
read the proof, producer and tests without claiming re-execution. Root
serialized the computations; the largest field had 2401 elements.
