# A residual action can hide the whole infinite resolution in one trace

Status: proposed equivariant source consequence; no arithmetic realization
of the displayed residual operator in a previously constructed global cover
is asserted. All coefficient fields have characteristic zero.
The original Chow source is frozen at `a895f47628b0bc7c7ee5e0392df2f79c24166f92`;
the new replay reconstructs the character operations without importing the
earlier matrix-factorization producer.

## 1. The commuting source action

Retain the binary cubic source R, the C2 inertia action I=diag(1,-1),
the full invariant base A=(Sym(Sym^3 V))^I, and M=(Sym(Sym^3 V))^-
from [the invariant-base construction](INVARIANT_BASE_MATRIX_FACTORIZATION.md).
Every linear operator normalizing this C2 subgroup commutes with I, because
its only nonidentity element must be fixed. Thus an invertible such operator
on V is F=diag(a,b) in the specified inertia eigenbasis.

The source W=Sym^3 V has positive weights x=a^3, z=a b^2 and negative
weights r=a^2 b, s=b^3. Put delta=r s=a^2 b^4. Write Y for the
two-dimensional negative W-space, so tr(F|Y)=r+s and det(F|Y)=delta.
These are weights of actual source vectors, not roots fitted to a numerator.

The invariant ring has generators x1,x2,u=y1^2,v=y1y2,w=y2^2 and relation
u w-v^2. Their F-weights are respectively x,z,r^2,delta,s^2. Its relation
has weight delta^2. The binary Chow quotient has the actual two characters

    B^+(F,T)=1+2 a b^2 T,
    B^-(F,T)=2 a^2 b T+a^3 b^3 T^2.                         (1.1)

These follow from the frozen literal source quotient or its acknowledged
classical descent/major-index formula. An equivariant free splitting exists
but is not chosen canonically.

## 2. Equivariant periodicity includes a character twist

Let Y be placed in generator degree one. The exact minimal resolution of M
has free terms

    F_i=A(-(1+2i)) tensor ((det Y)^i tensor Y),  i>=0.        (2.1)

To verify the representation rather than just its dimension, the two
generator weights in F_i are delta^i r and delta^i s. The matrix

    D=[-v,-w;u,v]

maps F_i to F_(i-1): its first column has output weights
delta^(i-1)r*delta=delta^i r and
delta^(i-1)s*r^2=delta^i r, and similarly for the second column.
The augmentation F0->M sends the generators to y1,y2. This proves
equivariance of every map. The source identities

    ker pi=im D,       D(a0,b0)=(-y2 pi(a0,b0),y1 pi(a0,b0))

prove exactness in every degree, as in the elementary gcd argument of the
preceding note. Minimality follows because the entries have positive degree.
Consequently the actual Tor representation is

    Tor_i^A(M,k)=(det Y)^i tensor Y in degree 1+2i.           (2.2)

In particular the two-step periodicity is twisted by (det Y)^2 as well
as shifted by four internal degrees. Omitting that character would lose
equivariance even though the repeated scalar matrix still squares to zero
over A. This is the equivariant version of the classical hypersurface
matrix factorization, not a new abstract periodicity theorem.

## 3. Character series and a finite-order trace collapse

Put

    L_F(T)=(1-xT)(1-zT)(1-r^2 T^2)(1-s^2 T^2).

Direct invariant and anti-invariant monomial counting gives

    H_A(F,T)=(1+delta T^2)/L_F(T),
    H_M(F,T)=(r+s)T/L_F(T),
    H_(R^I)(F,T)=B^+(F,T)H_A(F,T)+B^-(F,T)H_M(F,T).         (3.1)

The ratio H_M/H_A=(r+s)T/(1+delta T^2) is also the coefficientwise
Euler sum of (2.1). It is not a finite polynomial for generic invertible
a,b. Independently the original source character is

    tr(F|R_n^I)=(h_n(a,b)^3+h_n(a,-b)^3)/2.                 (3.2)

Now take the particular commuting finite-order linear operator

    F=diag(i,1),          i^2=-1.

It commutes with I; together they give a finite linear representation.
We call it a residual-action model only. No specified finite field,
global arithmetic source, or Frobenius weight assertion is part of this
example. Its negative source weights are r=-1,s=1, so delta=-1 and

    tr(F|Tor_i^A(M,k))=delta^i(r+s)=0 for every i>=0.         (3.3)

The modules in (2.2) still have dimension two and remain nonzero in
every homological degree. In this same specialization,

    H_M(F,T)=0,
    H_A(F,T)=1/(1-T^4),
    H_(R^I)(F,T)=(1+2iT)/(1-T^4).                          (3.4)

Thus this one graded trace agrees with that of the finite free A-module
A tensor B^+. The actual R^I still has the infinite minimal resolution
from the previous note. Trace agreement has not produced an isomorphism,
a finite resolution, or a canonical finite source complex.

The phenomenon has an explicit second-power falsifier. On M_1=Y, F has
eigenvalues -1,+1 and hence

    det(1-uF|M_1)=1-u^2,       tr(F^2|M_1)=2.               (3.5)

The zero first trace does not imply a trivial ordinary determinant. In
fact F^2=diag(-1,1) gives two positive Y eigenvalues, so none of the
two-dimensional Tor traces in (2.2) vanishes at that power. Keeping the
residual action and its powers restores the distinction immediately.

The specialization F=diag(1,i) gives the separate exact control
H_(R^I)(F,T)=(1-2T)/(1-T^4), again with a zero graded M trace. Generic
positive a,b provide a noncollapse control. These change character values;
they do not deform away or remove the underlying infinite-resolution modules.

## 4. Replay boundary

The producer uses exact Q(i) arithmetic, literal source monomials, and the
equivariant matrix-column weights. It compares (3.1) with (3.2), with the
Euler series of all resolution rows visible at the declared cutoff, and
with the two finite-order controls. The degree-one ordinary determinant
and its second-power trace are independently retained.

No numerical eigenvalue, fitted recurrence denominator, or assertion of
arithmetic Frobenius can enter the acceptance conditions. The all-degree
trace collapse follows algebraically from r+s=0 and (2.2), rather than
from the finite number of rows checked. Source freeness, canonical
quotients, actual modules, character traces, and ordinary determinants
remain separate throughout.
