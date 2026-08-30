# A polarized degree-nine source isogeny and its three-torsion graph

Status: proposed sequel to the explicit curve/maps packet frozen at
`567ae7aec00f6ee6d3e01bdde2004e76fec8ff6f`.
Scope: any field k of characteristic different from 2 and 3, with A!=0 and
Delta=-4A^3-27B^2!=0. This extends the geometric statements beyond finite
fields; the finite-field replay remains separately bounded. No arithmetic
RH, priority, or general classification claim is made.

Keep f=x^3+Ax+B, g=-3x^2-4A and the smooth curves

    H:w^2=f(x)g(x),       E:y^2=f(x),
    D2:S^2=U[-4A^3-27(B-U)^2].

The preceding packet proves two separable degree-three maps

    phi:H->E,
      X=(x^3+4B)/g,  Y=w(x^3+4Ax-8B)/g^2,
    psi:H->D2,
      U=f(x),        S=w(3x^2+A).

Each sends the unique infinity point of H to the chosen infinity origin
of its target. This sequel determines the polarization and kernel of the
induced Jacobian map, without inferring either from L-polynomial equality.

## 1. The theorem

Let J=Jac(H), with its canonical principal polarization, and give E x D2
the product principal polarization. Then

    Phi:E x D2 -> J,       (P,Q) -> phi^*P + psi^*Q       (PI-1)

is a k-defined separable isogeny of degree nine. If dagger denotes the
adjoint under these principal polarizations,

    Phi^dagger Phi = [3]_(E x D2),
    Phi^*lambda_J = 3 lambda_(E x D2).                   (PI-2)

The two individual pullback maps phi^*, psi^* are embeddings. The kernel
of Phi is the graph of a k-defined isomorphism of finite etale group schemes

    alpha:E[3] -> D2[3],
    e_(3,D2)(alpha P,alpha Q)=e_(3,E)(P,Q)^(-1).          (PI-3)

In particular, E[3] and D2[3] are isomorphic Galois modules. The sign in
(PI-3) is fixed by the product polarization. The theorem does not say the
elliptic curves are isomorphic or mutually isogenous, nor does it identify
their Jacobian product with J as a principally polarized variety.

## 2. An integral correspondence proof of orthogonality

Use the actual S3 closure

    Z:y^2=f(x), v^2=g(x),       pi:Z->H, (x,y,v)->(x,yv).

The degree-two map pi is a quotient by (y,v)->(-y,-v). Let q1,q2,q3:Z->E
be the three cubic-root maps, with roots x,(-x+v)/2,(-x-v)/2 and common y.
Let q_D:Z->D be the sign quotient, and eta:D->D2 the degree-two quotient
of the preceding packet. At the level of curve maps and the elliptic
group law, the explicit formulas give

    phi pi = q2-q3,       psi pi = eta q_D.              (PI-4)

These identities induce identities on Picard varieties. In Hom into Jac(Z)
put

    A0=pi^*phi^*=q2^*-q3^*,
    B0=pi^*psi^*=q_D^* eta^*.

Let r be a three-cycle of the k-defined S3 action, and set N=1+r+r^2
on Jac(Z). The three q_i^* are cyclically permuted, so their differences
telescope under N:

    N A0=0,        N B0=3B0.                            (PI-5)

Automorphisms of a curve preserve its canonical Jacobian polarization.
Their adjoints are their inverses. Therefore N^dagger=N, and

    0=(N A0)^dagger B0=A0^dagger N B0=3A0^dagger B0
      =6 phi_* psi^*.                                  (PI-6)

The last equality uses pi_*pi^*=[2]. Hom groups of abelian varieties are
torsion-free, so phi_*psi^*=0; taking the adjoint gives psi_*phi^*=0.
This argument is integral and valid in positive characteristic. Vanishing
of a differential alone would not justify it, because a nonzero purely
inseparable homomorphism can have zero differential.

The diagonal identities phi_*phi^*=[3] and psi_*psi^*=[3] follow from
the map degrees. Thus the matrix of Phi^dagger Phi is exactly diag([3],[3]),
which proves (PI-2). Its kernel is finite and its image has dimension two,
so Phi is an isogeny. The degree identity gives (deg Phi)^2=3^4, hence
deg Phi=9. Its kernel lies in (E x D2)[3], which is etale in the stated
characteristic, proving separability.

The standard pullback/norm adjunction and degree identities are used here
for actual maps of curves. For the general abelian-variety facts, see
[Milne, Abelian Varieties](https://www.jmilne.org/math/CourseNotes/AV.pdf),
Lemma 10.6 (torsion-free Hom), Proposition 13.8 and Remark 13.9
(polarization descent and degrees). Applied to (PI-2), the descent
criterion says that ker(Phi) is isotropic for the product three-Weil
pairing. Its order nine inside the rank-four symplectic three-torsion
space makes it maximal isotropic.

## 3. Why the two pullback maps have no finite kernel

It is enough to work over an algebraic closure. For either degree-three
map h:H->E0, the identity h_*h^*=[3] places ker(h^*) in E0[3]. If that
kernel were nonzero, it would contain an order-three degree-zero line
bundle L with h^*L trivial. Choose a trivialization L^3=O. The associated
cyclic cover

    E_L=Spec_(E0)(O direct-sum L direct-sum L^2) -> E0

is connected, etale and degree three. Connectedness follows from the
exact order of L; its genus is one by unramified Riemann--Hurwitz.
Over the algebraic closure a trivialization of h^*L can be rescaled so
that its cube agrees with the pulled-back trivialization of L^3. Thus the
pulled-back cyclic torsor splits, and h lifts to H->E_L. Multiplying
degrees forces that lift to have degree one. A degree-one map between
smooth projective curves is an isomorphism, contradicting genera two and
one. Therefore h^* has no nonzero geometric kernel; since its possible
kernel is etale, it is an embedding of abelian varieties.

The cyclic-cover construction is the line-bundle form of the
[Kummer sequence, Stacks Project 59.28](https://stacks.math.columbia.edu/tag/03PK).
It is used only with 3 invertible. No assumption that all three-torsion
points are rational over k is made.

Let K=ker(Phi). If an element of K has first coordinate zero, injectivity
of psi^* makes it zero; likewise for the second coordinate. Both
projections K->E[3], K->D2[3] are therefore injective, hence isomorphisms
of the two order-nine etale group schemes. They define alpha over k.
The product pairing is e_E times e_D2; isotropy gives (PI-3).

## 4. Differential and finite-field consequences

The affine formulas also give a useful independent consistency check:

    phi^*(dX/(2Y))=-3x dx/(2w),
    psi^*(dU/(2S))=dx/(2w).                            (PI-7)

For the first identity, differentiating X yields
X'=-3x(x^3+4Ax-8B)/g^2. For the second, f'=3x^2+A cancels.
These pullbacks form a basis of H^0(H,Omega^1) in the stated characteristic.
They check the explicit maps and separability; the correspondence proof
above supplies the stronger integral orthogonality and polarization.

Over F_q, alpha intertwines Frobenius. The two elliptic characteristic
polynomials therefore agree modulo three:

    P_E(T) = P_D2(T) mod 3.                            (PI-8)

The preceding exact panels already obey this congruence, but (PI-8) is a
consequence of the source-defined torsion graph for every allowed finite
field, not an extrapolation of those panels. The same is true after every
constant-field extension. Congruence modulo three does not imply equality
of the integer L-polynomials or a source-independent spectral fit.

## 5. Completed exact torsion replay

A separate bounded replay constructs both elliptic three-torsion groups
for (A,B)=(1,1) over F25 and F2401. It computes their pullback divisor
classes on H using exact polynomial arithmetic and recovers K from (PI-1).
Both graphs have exactly nine elements and pass every group, Frobenius and
Weil-pairing identity in their declared coverage. The source maps and
Jacobian operations precede graph extraction; matching Frobenius traces
alone is not used to construct alpha.

The replay contract in `TORSION_DIVISOR_REPLAY.md` states the Cantor-law
dependency and fixes all divisor and pairing conventions. In particular
phi^*(O) is not 3 infinity: its nonzero two-torsion correction must be
subtracted. Omitting it makes the displayed nonzero pullback six-torsion.
The producer checks all 81 pairs on the two source three-torsion groups;
it does not enumerate the whole Jacobian over either extension field.

Ruff, primitive write/check, optimized check and all 15 dedicated tests
in ordinary and optimized Python passed. A separate complete F5 census
contains 54 reduced divisor classes, agreeing with the frozen curve
polynomial. These finite controls authenticate the two declared examples;
the all-field isogeny and anti-isometry remain the proof above.
