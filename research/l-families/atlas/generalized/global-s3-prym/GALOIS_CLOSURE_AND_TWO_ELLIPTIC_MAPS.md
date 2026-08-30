# The discriminant sector and two explicit elliptic maps

Status: proposed geometric sequel to the S3 source frozen at
`23ad35cc8010f72cf1df54f09eccb4dcba108879`.
Scope: every finite field k=F_q of characteristic p>3, A!=0 and
Delta=-4A^3-27B^2!=0. All curves below mean their smooth projective models.
No claim about integer-source transport, a global Euler product, or RH is made.
The classical quotient and Jacobian principles are not claimed as new.

The sign representation missing from the standard elliptic source has a
concrete discriminant curve. The same S3 closure also produces a genus-two
curve with two explicit, separable degree-three elliptic maps. Thus the
representation sectors can be checked against complete algebraic sources,
including ramification, without fitting eigenvalues.

## 1. Explicit curves and the S3 closure

Set f(x)=x^3+Ax+B and g(x)=-3x^2-4A. Define

    E: y^2=f(x),
    Z: y^2=f(x), v^2=g(x),
    H: w^2=f(x)g(x),
    D: s^2=-4A^3-27(B-u^2)^2,
    D2: S^2=U[-4A^3-27(B-U)^2].                    (GC-1)

E, D and D2 have genus one; H has genus two; Z has genus three. D2 has
its rational point at infinity, so is an elliptic curve with a specified
origin. D is initially a genus-one quartic without a chosen origin.

Here are the smoothness and connectedness checks. The roots of f are simple
by Delta!=0. The two roots of g are distinct by A!=0. A common root would
satisfy x^2=-4A/3 and B=Ax/3, forcing Delta=0. Thus fg is squarefree of
degree five. On E, g has four simple zeros and a pole of order four, so
adjoining its square root gives a geometrically connected double cover
ramified at exactly four points. Riemann--Hurwitz gives g(Z)=3. Equivalently
the biquadratic cover of P1_x has six branch points, including infinity.
The discriminant quartic has repeated roots only if A=0 or Delta=0;
the cubic defining D2 is squarefree under the same hypotheses.

The map Z->P1_u uses u=y. Once x is one root of f(X)-u^2, the other two are

    r2=(-x+v)/2,       r3=(-x-v)/2.                    (GC-2)

Consequently k(Z) is the splitting field of that cubic, of degree six.
It is the actual geometric and arithmetic S3 closure. Its deck generators
are defined over k, even when k lacks cube roots of unity:

    s0:(x,v,y) -> (x,-v,y),
    r0:(x,v,y) -> ((-x+v)/2,(-3x-v)/2,y).             (GC-3)

Direct substitution gives s0^2=r0^3=1 and s0*r0*s0=r0^(-1). These maps
permute the three roots, so preserve both equations. Frobenius commutes
with this k-defined S3 action; no constant-field character twist is hidden.

The sign quotient Z/A3 is D. The map is explicitly

    u=y,       s=v(3x^2+A),
    g(x)(3x^2+A)^2=-4A^3-27(B-f(x))^2.               (GC-4)

The right side is the cubic discriminant. The expression on the left is
the square of the Vandermonde product, with the chosen ordering fixing an
irrelevant overall sign of s.

## 2. Two complementary decompositions of the same source

Over P1_x, the three quadratic quotients of Z are E, H and the smooth
conic v^2=g(x). Rational-character projectors, or pullback and trace,
give the Frobenius-compatible decomposition

    H1(Z) = H1(E) direct-sum H1(H),
    P_Z(T)=P_E(T)P_H(T),                             (GC-5)

because the conic has zero H1. Here P_C(T)=det(1-TFrob_q|H1(C)).

For the S3 action over P1_u, its trivial H1 sector vanishes. Write its
remaining representation as sign tensor M_sign, plus standard tensor
M_std. A3-invariants identify M_sign with H1(D). Invariants under the
transposition fixing x identify M_std with H1(E), since the sign has no
such invariant and the two-dimensional standard representation has a
one-dimensional invariant. All maps commute with Frobenius. Hence

    H1(Z) = (sign tensor H1(D))
                  direct-sum (standard tensor H1(E)),
    P_Z(T)=P_D(T)P_E(T)^2.                           (GC-6)

These are identifications of Frobenius multiplicity spaces, not assertions
that a chosen geometric basis is canonical. Combining (GC-5) and (GC-6)
gives the all-field theorem

    P_H(T)=P_E(T)P_D(T).                             (GC-7)

The quotient/cohomology principle follows by finite pushforward and the
exact averaging projector in characteristic-zero coefficients. It is the
same source principle used in the frozen packet. Group-algebra Jacobian
decompositions are classical; see [Kani--Rosen, 1989](https://eudml.org/doc/164555).
The determinant assertion here does not require inferring an isogeny from
a finite list of matching point counts.

## 3. A genuine degree-three map from H to E

On g(x)!=0 define

    X=(x^3+4B)/g(x),
    Y=w(x^3+4Ax-8B)/g(x)^2.                          (GC-8)

Then Y^2=X^3+AX+B. A derivation keeps track of the source: on Z, let
Q2=(r2,y) and Q3=(r3,y) on E. The group-law point Q2-Q3 is invariant under
(y,v)->(-y,-v), so descends to H with w=yv. Its slope is 2y/v, giving

    X=4y^2/v^2+x,       Y=-y(x+2X)/v,

which reduces to (GC-8). Equivalently the integer-polynomial identity is

    f(x)(x^3+4Ax-8B)^2
      =(x^3+4B)^3+A(x^3+4B)g(x)^2+B g(x)^3.         (GC-9)

The numerator and denominator of X are coprime: a common zero of g and
x^3+4B would also be a zero of f, excluded above. Thus the rational
function X(x) has degree three on P1_x. Comparing the two hyperelliptic
degree-two x-coordinate maps shows H->E has degree three. It is separable
because p>3. Rational maps between these smooth projective curves extend
at the apparent denominators. The two points with g=0 and the unique
point at infinity of H all map to the origin of E; they account for its
degree-three fibre. These are geometric points, not a claim that all three
are rational over every base field.

## 4. The other degree-three map and the discriminant isogeny

There is a second everywhere-defined projective map, with affine formula

    H -> D2:       U=f(x),       S=w(3x^2+A).         (GC-10)

Identity (GC-4) proves its equation. The rational function U(x) has degree
three, so the same degree comparison proves that this is a separable
degree-three map. The point at infinity maps to infinity.

The connection between D and D2 is not a guessed equality of polynomials:

    D -> D2:       U=u^2,       S=u s.               (GC-11)

It is the quotient by tau:(u,s)->(-u,-s). There is no affine fixed point:
u=s=0 would contradict Delta!=0. At infinity tau exchanges the two
geometric points, because it negates the leading ratio s/u^2. Thus this
degree-two map is etale. It induces a degree-two isogeny between Jac(D)
and D2. Without choosing an origin on D, the raw curve map is not described
as an origin-preserving homomorphism. It follows in particular that

    P_D(T)=P_D2(T),       P_H(T)=P_E(T)P_D2(T).       (GC-12)

There is also an elementary all-extension point-count proof. Put
d(U)=-4A^3-27(B-U)^2 and let chi be the quadratic character with chi(0)=0.
Its quadratic discriminant is -432A^3!=0, so
sum_U chi(d(U))=-chi(-27). The standard identity follows by completing
the square and counting (a-b)(a+b)=constant. Since u^2=U has 1+chi(U)
solutions, the affine sums for D and D2 differ by -chi(-27); their infinity
counts differ by +chi(-27). Their total counts therefore agree over every
finite extension. This independently proves the last determinant identity.

No claim about principal polarizations, a (3,3)-isogeny kernel, or an
isomorphism of the two elliptic factors is needed here. Those would require
additional data beyond the two explicit maps and the cohomological split.

## 5. Ramification and exact arithmetic infinity terms

Let N(u) be the number of distinct roots of f(x)=u^2 in F_Q, where Q is
any extension cardinality. Let d(u^2) be its discriminant. Counting the
normalized Z fibre directly in (GC-1) gives

    #Z_u = sum_(x:f(x)=u^2) [1+chi(g(x))]
          = 2N(u)-1+chi(d(u^2)).                     (GC-13)

The complete finite-fibre cases are:

| cubic fibre | N(u) | sign trace | standard trace | #Z_u |
| --- | ---: | ---: | ---: | ---: |
| three distinct linear roots | 3 | 1 | 2 | 6 |
| irreducible cubic | 0 | 1 | -1 | 0 |
| linear times irreducible quadratic | 1 | -1 | 0 | 0 |
| double root and simple root | 2 | 0 | 1 | 3 |

There is no triple-root case under A!=0. At a double root r, A=-3r^2
and g(r)=9r^2 is a nonzero square; the other root -2r has g(-2r)=0.
This proves the last row on the normalized closure, with three rational
points rather than six formal ordered tuples counted with multiplicity.
The unramified rows are the regular, sign and standard S3 characters.

E and H each have one rational point at infinity. Z and the conic each
have 1+chi(-3) points there, possibly zero; D has
1+chi(-27)=1+chi(-3); D2 has one. In the S3 cover, infinity inertia is C3.
Its sign invariant line has Frobenius eigenvalue chi(-3), while the
standard invariant space is zero. Thus (GC-13) at infinity becomes
1+chi(-3), consistent with the regular representation identity
regular=trivial+sign+2 standard. Replacing infinity by a compulsory
rational point would corrupt both odd-extension traces and Euler factors.

Summing the fibre identity over all points of P1 yields

    #Z(F_Q)=#D(F_Q)+2#E(F_Q)-2(Q+1),
    #Z(F_Q)=#E(F_Q)+#H(F_Q)-(Q+1).                   (GC-14)

The second equality also follows directly from the biquadratic equations
and the conic count Q+1. Hence (GC-7) can be checked by exact all-field
character counting as well as by cohomology. Imported curve weight and
duality theorems apply to these actual smooth curves; they do not follow
from finite Gram positivity.

## 6. Replay contract and boundaries

The completed bounded replay uses five declared smooth curves over F5 and
F7, all extension degrees one through four, and the unchanged field cap
2401. It independently counts E, H, D, D2, Z and the conic from their
primitive equations. It checks each finite u-fibre, both deck generators,
both elliptic maps on every rational affine H point, and all infinity
terms. First two counts determine the elliptic factors and predict two
held-out counts. All four genus-two counts determine P_H independently.
There is no numeric eigenvalue fit, floating arithmetic or unspecified
family sweep. The all-field proofs above do not depend on the finite
enumeration.

For example, the F5 source (A,B)=(-1,0) gives
P_E=1+2T+5T^2, P_D=P_D2=1-4T+5T^2 and
P_H=1-2T+2T^2-10T^3+25T^4. The F7 source (4,4), which has a rational
double-root fibre at u=3, gives P_E=1+2T+7T^2,
P_D=P_D2=1-4T+7T^2 and P_H=1-2T+6T^2-14T^3+49T^4.
These finite controls exercise different traces and the normalized branch
fibre; they do not replace the all-field argument.

What was actually run: Ruff format/check, primitive `--write`, ordinary
and optimized-Python `--check`, and all 12 dedicated tests in ordinary
and optimized Python. All passed. The tests include both polynomial map
identities over Z[A,B,x], independent direct prime-field equation counts,
the ramified fibre, projective map exceptions, constant-extension infinity,
source authentication and rejection of the two geometric degenerations.
The degree-six closure factor is derived from the proved decomposition and
checked against four primitive extension traces; six independent closure
counts are not claimed. This is not a repository-wide test-suite result.

The A=0 cyclic degeneration is deliberately outside this source: g becomes
a square times a constant and fg has a repeated factor. Neither the genus
nor the S3 decomposition may be transported through that degeneration
unchanged. Delta=0 is also rejected. These are source hypotheses, not
optional checker tolerances.
