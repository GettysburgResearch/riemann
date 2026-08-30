# Exact map-fibre divisor replay of the three-torsion graph

Status: bounded executable companion to
`POLARIZED_JACOBIAN_AND_THREE_TORSION.md`.
Primitive geometry: the six files frozen at
`567ae7aec00f6ee6d3e01bdde2004e76fec8ff6f`, authenticated against Git
before executable import. Earlier field-source authentication is retained.

The replay uses (A,B)=(1,1) over F25 and F2401, with base primes five and
seven. The first monic irreducible polynomial in the frozen base-p ordering
defines each field. Maximum field order is 2401; all arithmetic is exact.
Polynomial operations have degree cap 12, checked before allocation.
No precomputed Jacobian table, fitted spectrum or external CAS is used.

## 1. Arithmetic conventions

A reduced Mumford pair (u,v) represents the divisor defined by u(x)=0,
w=v(x), minus deg(u) times the unique infinity point on H:w^2=h(x).
Here h=f*g is the actual degree-five source polynomial, not rescaled to a
different quadratic twist. The polynomial u is monic, deg u<=2, deg v<deg u,
and u divides h-v^2. The identity is (1,0); negation replaces v by -v.

Composition uses Bezout coefficients satisfying

    d=s1*u1+s2*u2+s3*(v1+v2),
    u=u1*u2/d^2,
    v=[s1*u1*v2+s2*u2*v1+s3*(v1*v2+h)]/d mod u.

Every indicated division is checked to be exact. Reduction replaces u by
the monic normalization of (h-v^2)/u, and v by -v modulo the new u, until
degree at most two. Divisibility by h-v^2 is checked before and after
reduction. This is the standard Cantor law. The independently inspected
algorithm is [Damien Robert, notes on abelian varieties, Algorithm 2.1,
PDF page 42](https://www.normalesup.org/~robert/pro/publications/notes/notes_av.pdf).
Cantor's original 1987 paper is acknowledged, but its AMS PDF was not
retrievable in this session. No claim of independently proving the general
Cantor algorithm is made.

The dedicated controls include a complete reduced-divisor census over F5
and its cardinality from the frozen genus-two polynomial, independent
tangent doubling at a rational curve point, polynomial Bezout identities,
and group identities. These supplement the source proof; they do not
replace the standard divisor-class representation theorem.

## 2. Pullbacks are derived from the maps, before finding the kernel

For a nonzero three-torsion point P=(X,Y) on E, its phi-fibre has polynomial

    u_P=x^3+3X*x^2+4A*X+4B,
    v_P=Y*g^2/(x^3+4Ax-8B) mod u_P.

Its reduction represents phi^*(P)-3 infinity. But phi^*(O) is the sum
of the two g=0 points and infinity, not three copies of infinity.
Therefore the true pullback of (P)-(O) subtracts the two-torsion class

    T_g=(monic(g),0)=[D_g-2 infinity].

Omitting this correction generally turns a three-torsion image into a
six-torsion class; a dedicated negative control checks the difference.

For Q=(U,S) on D2, the psi-fibre instead has

    u_Q=f(x)-U,       v_Q=S/(3x^2+A) mod u_Q.

Since psi^*(O)=3 infinity, reducing this pair already gives the correct
pullback. The denominator inverses exist for nonzero three-torsion:
Y and S are nonzero; the polynomial map identities rule out a shared
zero with either fibre polynomial. Failed inversion is never suppressed.

For group arithmetic only, D2 is put in the explicitly isomorphic short
model by

    X2=-27U+18B,       Y2=-27S,
    Y2^2=X2^3+27(4A^3-9B^2)X2-486B(4A^3+3B^2).

The inverse transformation is applied before forming the actual psi-fibre.
This change of coordinates is not an isogeny or a fitted elliptic model.

## 3. Complete torsion, kernel and pairing checks

For a short curve y^2=x^3+a*x+b, every field x is tested against

    psi3(x)=3x^4+6a*x^2+12b*x-a^2.

All corresponding y coordinates are enumerated from the primitive field
square table, and each point is independently checked by addition to
satisfy 3P=O. The tangent-line condition gives the converse: for y!=0,
the tangent has triple intersection precisely when psi3(x)=0. Each declared
field is required to contain all nine three-torsion points, including O.

The two sets of nine pullback classes are computed first. Only then are
all 81 pairs added in Jac(H) to recover the kernel of Phi. Acceptance
requires exactly nine kernel pairs and a bijective graph. All 81 additive
identities on each factor, all graph homomorphism identities and all 81
pairing reversals are checked. Coefficient-wise p-power Frobenius is tested
on the actual divisor classes and on the graph.

The pairing convention is fixed as follows. At nonzero three-torsion P,
the normalized tangent line l_P has divisor 3(P)-3(O). For independent
P,Q use e3(P,Q)=-l_P(Q)/l_Q(P); for dependent pairs use one. This is the
normalized Miller-function formula stated in the official
[Magma pairing documentation](https://docs.magma-maths.org/ArithmeticGeometry/EllipticCurvesOverFiniteFields/pairings.html).
The tangent functions have the same leading coefficient at infinity, so
the leading-coefficient ratio in [Enge, *Bilinear pairings on elliptic
curves*, Eq. (8), printed page 219](https://ems.press/content/serial-article-files/44297?nt=1)
is one. The two short models use this convention. No Magma execution is
claimed. Primitive cube roots, nondegeneracy, bilinearity and the minus
sign are separately controlled.

The resulting finite graph is a source-divisor construction. The all-field
degree-nine polarized isogeny and Galois-module anti-isometry are proved
in the companion theorem. These two finite panels alone do not prove that
theorem. A full Jacobian census over F25 or F2401 is not claimed.

## 4. Acceptance and execution record

`torsion_source.json` is pinned by its canonical typed JSON hash. The
producer reconstructs fields, curves, divisor operations, torsion and the
graph before comparing the artifact. Canonical JSON comparison distinguishes
integers from booleans and floats. The provenance file binds the producer,
tests, both notes, source and artifact. Ordinary and optimized Python must
both pass; proof-critical acceptance does not use assert.

What was actually run: Ruff format and check; complete primitive `--write`,
ordinary `--check` and optimized-Python `--check`; all 15 dedicated tests
in ordinary and optimized Python. All passed. The 15-test runs took about
six seconds each on the shared machine. Jobs were serialized and no state
space was expanded beyond the declared small polynomial and point tables.

In the frozen field encodings, an extracted basis and its image have Weil
pairings 7 and 22 over F25, and 4 and 2 over F2401. In each pair their
field product is one. These integers are field element encodings, not
real numbers used as approximate roots of unity. The artifact records
all points, pullback divisor pairs, kernel indices and Frobenius actions.
