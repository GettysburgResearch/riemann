# Positive holonomy defect, critical circle, and a blind principal channel

Status: exact finite mechanism and countermodel, separately labelled sequel.
Source: the based representation and word automata at
`e7fc8b0af2c42ce43384543972df2ed44f343300`, defined in [the source note](README.md).
This adds no hypothesis about arithmetic L-functions. RH and GRH remain open.

The same independently specified finite source produces an Euler/trace law,
a reciprocal duality, a spectral circle, and a positive operator. It also
shows why that positive operator need not control the principal member.
Every argument below is elementary finite unitary algebra. These mechanisms
are classical, not claims of external mathematical novelty.

## Exact positive operator

Retain U,V0 in U(d), A=UV0, B=V0U and K=A*B. Define

    H = I - (K+K*)/2.

Then, as an operator identity on the based fibre,

    H = (A-B)*(A-B)/2 = (I-K)*(I-K)/2 >= 0.

Indeed A*A=B*B=K*K=I. Expanding either product gives
I-(A*B+B*A)/2. Consequently

    <x,Hx> = ||(UV0-V0U)x||^2/2,
    ker H = ker(UV0-V0U) = ker(I-K).

Under simultaneous conjugation of the representation H transforms by the
same conjugation. The trace response from the source note is exactly
3 tr(H), so trace positivity is the shadow of this positive operator.
This is a defect form; it is not automatically a nondegenerate polarization.

On the full three-clock-state space T0^3=I and T1^3 is unitary. Hence

    Re_op(T0^3-T1^3)
      = I - (T1^3+(T1^3)*)/2
      = (I-T1^3)*(I-T1^3)/2 >= 0,

where Re_op(M)=(M+M*)/2. The three blocks are unitarily conjugate to H.
This identity is covariant under independent changes of basis on all three
clock fibres; the source includes the common based holonomies as before.

## Spectral circle and reciprocal duality from the same source

Both T0 and T1 are unitary: each block row and column has exactly one
unitary label. Thus every eigenvalue lambda has |lambda|=1, independently
of any desired determinant roots. The roots of Dj(t)=det(I-tTj) all satisfy
|t|=1, and the Euler/trace expansion converges for |t|<1. This is a finite
critical-circle statement, not a theorem about the arithmetic critical line.

The block-cycle permutation has sign +1 and
det(CUV0)=det(CV0U)=1, so det T0=det T1=1. For either j and t!=0,

    Dj(t) = (-t)^(3d) conjugate(Dj(1/conjugate(t))).

To check the identity for an arbitrary unitary N-dimensional T, factor
I-t^(-1)T*=-t^(-1)T*(I-tT) inside its determinant. This gives
D(t)=(-t)^N det(T) conjugate(D(1/conjugate(t))). Substitution of N=3d
and det(Tj)=1 proves the stated duality. It is self-inversive reciprocity;
it does not imply that every coefficient is real.

These facts join the primitive-cycle Euler product, the transfer trace,
the reciprocal involution and the spectral circle in a single finite
source model. No zeros were used to define its group representation or
operators. They do not create an archimedean factor or an arithmetic
functional equation.

## Exact permutation spectrum and the principal obstruction

If U,V0 are permutation matrices, so is K. Suppose its permutation cycles
have lengths l1,...,lr. On a cycle of length l, the eigenvalues of H are

    1-cos(2*pi*j/l),             j=0,...,l-1.

This follows by diagonalizing the cyclic shift with its finite Fourier
vectors; H is one half of that cycle's graph Laplacian. In particular

    nullity(H)=r,              rank(H)=d-r.

The vector constant on each K-cycle lies in the kernel. The global
constant vector is always present: the usual permutation principal line
is annihilated by H even when the comparison has strictly positive trace.
Thus positivity and a nonzero total defect do **not** supply a positive
lower bound on the principal line or select an arithmetic principal member.

For the source's degree-three pair U=(12), V0=(23), K is a three-cycle:
H has eigenvalues {0,3/2,3/2}, so the trace response is 9 but the principal
line remains invisible. For the real orthogonal anticommuting pair in the
source note, K=-I, H=2I and the response is 12. There is no universal
positive-definiteness assertion across these source classes.

The permutation spectrum and the exact factorization constitute a
held-out prediction from the source, not a fitted numeric eigensystem.
The five bounded companion tests authenticate the original holonomy
producer before import, compare both Gram factorizations, verify the
full transfer identity and reciprocity, and check the S3 principal kernel
and the orthogonal definite case using rational arithmetic. They do not
machine-prove the all-dimensional theorem.

```text
python -B -m unittest discover -s research/exploratory/marked-holonomy-response/tests
python -B -O -m unittest discover -s research/exploratory/marked-holonomy-response/tests
```

The directory contains nine earlier controls and five companion tests.
The earlier canonical JSON remains bound to its original six-file freeze;
this separately reviewed proof/test sequel does not rewrite that identity.
Source acquisition is the same durable graph-source ref recorded in the
programme handoff. Numerical stability, a global arithmetic trace adapter,
and transfer of this positive form to such an adapter are not proved.
