# The Segre parent on an actual ramified S3 source

This companion binds the analytic parent to the cubic covering source
frozen at `23ad35cc8010f72cf1df54f09eccb4dcba108879` in
[`global-s3-prym/GLOBAL_S3_PRYM_SOURCE.md`](../global-s3-prym/GLOBAL_S3_PRYM_SOURCE.md).
It uses its generic S3 stratum only. The construction below is a family
of actual finite-image sheaves, one in each finite grade. No infinite
product over arithmetic places is formed. Classical finite-group
representation theory and the established trace formula supply the
global L identities; external novelty is not claimed.

## 1. Specify the source before its graded characters

Let k=F_Q, char(k)>3, A!=0, and Delta=-4A^3-27B^2!=0. Let

    E: y^2=x^3+Ax+B,             f:E -> P^1_u, u=y.

Here u is the coordinate on the arithmetic base. The variable z below
counts an internal algebra grade; T is the global L-function variable.
The frozen source proves that f has geometric and arithmetic monodromy
S3, with four geometric finite branch points having transposition inertia
and infinity having three-cycle inertia. The finite branch divisor is

    d(u)=-4A^3-27(B-u^2)^2=0.

Write W for the rank-three permutation representation over Q and V for
its rank-two augmentation summand. This V is the representation called W
in the frozen geometric note. Form, before evaluating any character,

    R = direct_sum_(n>=0) R_n,       R_n=Sym^n(V) tensor Sym^n(W).

The multiplication is the Segre multiplication. The source-defined
quadratic dual B and homotopy-Lie modules M_n=L_n^* are exactly those of
the frozen (2,3) parent, now restricted from GL(V) x GL(W) to this S3.
All these objects and maps are defined over Q. Base change to Q_ell,
ell!=char(k), gives finite-image lisse sheaves on the unramified open U;
base change to C gives the unitary analytic realization. No canonical
embedding of Q_ell in C, or positivity on Q_ell, is asserted.

Let e,s,c denote the identity, a transposition, and a three-cycle. The
source character generating functions are

    F_e(z) = (1+2z)/(1-z)^4,
    F_s(z) = 1/(1-z^2)^2,
    F_c(z) = 1/(1-z^3).                                      (1.1)

Proof. The identity coefficient is (n+1) binom(n+2,2). At s, the spectra
on V,W are (1,-1) and (1,1,-1). Hence Sym^n(V) has trace one in even
degree and zero in odd degree, while Sym^(2m)(W) has trace m+1. At c,
the spectra are (omega,omega^2) and (1,omega,omega^2). The latter
symmetric trace is one exactly in degrees divisible by three and zero
otherwise; in those degrees the former trace is one. This proves (1.1)
directly from the two input representations.

Put

    d_n=(n+1) binom(n+2,2),
    t_n=n/2+1 if n is even, and 0 otherwise,
    r_n=1 if 3 divides n, and 0 otherwise.

Character orthogonality gives the actual decomposition

    R_n = a_n 1 direct_sum b_n sgn direct_sum c_n V,
    a_n=(d_n+3t_n+2r_n)/6,
    b_n=(d_n-3t_n+2r_n)/6,
    c_n=(d_n-r_n)/3.                                         (1.2)

These are nonnegative integers because they are multiplicities in an
already constructed representation. Equivalently their generating
series are (F_e+3F_s+2F_c)/6, (F_e-3F_s+2F_c)/6, and (F_e-F_c)/3.
No fitted coefficient sequence defines R.

## 2. Two different ramification shortcuts fail

At a ramified point, the unshifted extension j_*R_n has stalk R_n^I.
Finite-group averaging in characteristic zero gives its dimension.

For I=C2,

    H_(R^I)(z)=(F_e+F_s)/2
       =(1+z+3z^2+z^3)/[(1-z)^4(1+z)^2].                    (2.1)

Its degree-one and degree-two dimensions are 3 and 10. In contrast,
dim V^I=1 and dim W^I=2, so forming the Segre algebra after taking the
input invariants gives (1-z)^(-2), with degree-one dimension only 2.
Moreover Sym^2((R^I)_1) has dimension 6<10. Thus R^I is not generated
in degree one and requires at least four new degree-two generators.
The original quadratic Koszul construction cannot simply be applied
unchanged to this invariant algebra.

For I=C3,

    H_(R^I)(z)=(F_e+2F_c)/3.                                (2.2)

The first two dimensions are 2 and 6. Taking input invariants first gives
V^I=0, W^I=Q and an algebra supported only in degree zero. Also
dim Sym^2((R^I)_1)=3<6, requiring at least three degree-two generators.

There is a subtler failed shortcut: construct the native Lie parent
first, then replace each M_n by M_n^I in its superdeterminant. In low
degrees the native modules are

    M_1=V tensor W,        M_2=det(V) tensor exterior^2(W).

Their (e,s,c) characters are respectively (6,0,0) and (3,1,0).
Consequently the dimensions of M_1^I,M_2^I are (3,2) for C2 and (2,1)
for C3. A super-Euler product using these invariant modules has
degree-two coefficient

    dim Sym^2(M_1^I) - dim M_2^I
       =4 for C2,          =2 for C3,                       (2.3)

instead of the actual values 10 and 6. This shortcut agrees in degree
one, making degree two an essential falsification. The issue is not
inexactness of invariants; it is their failure to preserve tensor
products. The crossed nontrivial sectors have been discarded.

## 3. The correct invariant complex keeps the tensor sectors

The native Koszul complex is equivariant and exact. In each internal
degree N it is a finite exact complex with terms

    R_(N-n) tensor B_n^*,          0<=n<=N,

resolving the unit in degree zero. Apply I-invariants to these full
tensor terms. This remains exact: averaging over a finite group is an
idempotent projection in characteristic zero and makes the invariants
functor exact. In particular division by |I| is available in Q_ell even
when ell divides |I|. The new terms are

    (R_(N-n) tensor B_n^*)^I,                               (3.1)

not R_(N-n)^I tensor (B_n^*)^I. Over U these complexes form local
systems; taking j_* gives the same exact stalk complexes on the complete
base. This exactness assertion is confined to the finite-image S3
category in use, not arbitrary lisse sheaves with infinite inertia.

The representation-ring identity encoding (3.1) is

    [R](z) [B^*](-z)=1.                                   (3.2)

In the S3 basis (1,sgn,V), write [R]=a+b sgn+c V. Multiplication by it
is the matrix

    [[a,b,c],
     [b,a,c],
     [c,c,a+b+c]],                                         (3.3)

because sgn^2=1, sgn tensor V=V, and V tensor V=1+sgn+V.
The corresponding matrix for [B^*](-z) is its inverse, with constant
term the identity matrix. Character evaluation diagonalizes these
operators with eigenvalues F_e,F_s,F_c and their reciprocals.
The invariant part of (3.2) pairs all dual irreducible sectors. It is
not merely the product of the two trivial-sector Hilbert series.

For example, after restricting to C2, write [R]=H_+ + H_- sign and
[B^*](-z)=K_+ + K_- sign. The exact invariant Euler identity is

    H_+ K_+ + H_- K_-=1,      H_+ K_- + H_- K_+=0.            (3.4)

Dropping H_- K_- is precisely the tensor-sector error. All constructions
are defined before solving these formal inverse identities.

On the analytic disk |z|<1/2 each F_h is also the proved superFredholm
determinant of the same canonical Hilbert-space parent evaluated at h.
The ramified graded dimension series is its finite Molien average
|I|^(-1) sum_(h in I) F_h(z). This is an average of determinants, not the
superdeterminant of the invariant Lie grades disproved in (2.3).
The analytic convergence statement is local in z and introduces no
infinite arithmetic Euler product.

## 4. Arithmetic Frobenius survives the inertia projection

Use the geometric Frobenius convention of the frozen source. At a
finite branch point, N_(S3)(C2)=C2, so every residual Frobenius acts
trivially on R_n^C2. Its graded trace series is (2.1), and its local
denominator is

    (1-T^(deg v))^(a_n+c_n).                                (4.1)

At infinity, I=C3 is normal in S3, and the quotient of its normalizer
by I is C2. Tame Frobenius conjugation sends an inertia generator to its
Q-th power (or Q^(-1)-th power under the inverse convention; these have
the same sign modulo three). Therefore the residual coset is trivial
for Q=1 mod 3 and is a transposition for Q=2 mod 3.

The dimension of R_n^C3 is a_n+b_n=(d_n+2r_n)/3, but its trace is

    a_n+b_n, if Q=1 mod 3;
    a_n-b_n=t_n, if Q=2 mod 3.                              (4.2)

Indeed all three elements of the nontrivial coset are transpositions.
The graded trace series in the second case is F_s, not (2.2). The
actual local denominator at infinity is

    (1-T)^a_n (1-epsilon_Q T)^b_n,
    epsilon_Q=+1 if Q=1 mod 3, and -1 if Q=2 mod 3.           (4.3)

In particular using invariant dimensions as Frobenius traces gives a
false arithmetic local factor when b_n>0 and Q=2 mod 3.

At an unramified closed point put Z=T^(deg v). The three local
denominators, obtained directly from (1.2), are

    e: (1-Z)^d_n,
    s: (1-Z)^(a_n+c_n) (1+Z)^(b_n+c_n),
    c: (1-Z)^(a_n+b_n) (1+Z+Z^2)^c_n.                      (4.4)

Equations (4.1)--(4.4) specify every local factor of each finite-grade
sheaf. They distinguish the grade variable from the Euler variable and
the invariant dimension from the Frobenius trace.

## 5. A genuine global family in every finite grade

Let D be the smooth projective genus-one curve with affine equation

    v^2=d(u)=-4A^3-27(B-u^2)^2.

The quartic has four distinct roots by the frozen S3 source assumptions.
Its degree-two map to P^1_u has four tame branch points and is unramified
at infinity; Riemann--Hurwitz gives genus one. A rational point is not
assumed in calling D genus one. Its generic nontrivial character is
sgn, since the square root of a separable cubic discriminant transforms
under a permutation by its sign. Hence the finite pushforward splits

    (D -> P^1)_* Q_ell = Q_ell direct_sum j_*sgn.

This includes inertia invariants at all branch points. Write P_D(T)
and P_E(T) for their degree-two cohomological numerator polynomials.
The trace formula and the direct summands give

    L(j_*sgn,T)=P_D(T),          L(j_*V,T)=P_E(T).            (5.1)

Combining this with the actual decomposition (1.2) proves, for every
fixed n>=0,

    L(P^1,j_*R_n,T)
       = Z(P^1,T)^a_n P_D(T)^b_n P_E(T)^c_n.                (5.2)

This is an actual finite-sheaf identity, with every ramified local
factor already specified. It is not a formal decomposition of a
guessed rational function. All global determinants act on finite
cohomology groups. In particular

    H^0(j_*R_n)=Q_ell^a_n,
    H^2(j_*R_n)=Q_ell(-1)^a_n,
    H^1(j_*R_n)=H^1(D)^b_n direct_sum H^1(E)^c_n.            (5.3)

The tame conductor ledger independently agrees. Each of the four
geometric finite points contributes (d_n-t_n)/2; infinity contributes
2(d_n-r_n)/3. Thus the total conductor is

    f_n=(8d_n-6t_n-2r_n)/3,

and Euler--Poincare gives

    dim H^1=f_n-2d_n+2a_n
            =d_n-t_n=2b_n+2c_n.                            (5.4)

At infinity the two points of D have leading equation v^2=-27u^4.
Their split/nonsplit sign is the quadratic character of -27, equivalently
of -3. In a field of characteristic greater than three, -3 is a square
exactly when the nontrivial third roots of unity lie in the field.
Thus its sign is epsilon_Q of (4.3), giving a second geometric check
of the residual Frobenius sector.

The finite-dimensional dualities and weight-one critical circles of
P_D and P_E are the established smooth-projective-curve theorems, not
consequences of an auxiliary positive matrix. Formula (5.2) transports
those properties with explicit trivial-sector poles. It does not prove
a new arithmetic RH statement, nor define an infinite-rank global
L-function by exchanging the grade sum and the Euler product.

## 6. Replay and next gate

The companion replay binds the frozen analytic and geometric sources.
It reconstructs the symmetric-power characters from the finite group,
checks the three character series, integral irreducible multiplicities,
both ramification failures, the full fusion inverse, conductor and
cohomology ledgers, and both residual Frobenius cosets. Low Lie grades
are checked against the original quadratic-source construction.

These finite exact controls verify the stated identities and expose
specific false adapters. They do not establish the general trace formula
or the Weil theorem numerically. The independent geometric discriminant
and Galois-closure companion supplies further source comparisons without
changing this parent.

The next nontrivial construction would be a useful global analytic
completion of these infinitely many finite-grade objects with explicit
topology, ramification, and convergence. Nothing here licenses commuting
j_*, taking invariants, PBW superdeterminants, and infinite products.
