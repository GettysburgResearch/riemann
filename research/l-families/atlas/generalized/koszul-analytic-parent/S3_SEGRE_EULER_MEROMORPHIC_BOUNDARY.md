# The source-corrected Segre Euler product continues to the unit disk and no farther

Status: proposed exact theorem for the fixed geometric S3 source. The
ordinary arithmetic Lie parent and this source-corrected Euler product
are different objects. The correction here is the actual invariant Segre
source at the ramified places; it is not chosen to fit desired zeros.

The proof uses the classical finite-factor extraction method for Euler
products, in the Estermann--Dahlquist tradition. See Estermann's
[1928 paper](https://doi.org/10.1112/plms/s2-27.1.435) and Alberts'
[account of the factorization method](https://arxiv.org/abs/2406.18190).
No priority for that mechanism, finite-cover cohomology, PBW or Weil's
theorem is claimed. What is bound here is the explicit S3 source, its
ramification correction, and its surviving zero set. The proof below
does not import a general Frobenian continuation theorem in place of
checking the required integral exponents and noncancellation.

## 1. One actual source at every closed place

Use the generic cubic source over F_Q from the frozen S3 packets:
char(F_Q)>3, A!=0 and -4A^3-27B^2!=0. Its geometrically connected S3
Galois closure Z is a smooth genus-three curve. Let B be the branch
divisor on P1 and U=P1 minus B. Geometrically B has four finite
transposition points and infinity with three-cycle inertia. Its inverse
image in Z consists of fourteen geometric points.

On U the source grades are the actual representations

    R_j=Sym^j(V_std) tensor Sym^j(W_perm).

For each closed place v, with inertia I_v and Frobenius lift phi_v, put

    F_v(t)=sum_(j>=0) tr(phi_v | R_j^(I_v)) t^j,
    E_R(z)=product_v F_v(z^(deg v)).                        (1.1)

At good places the three possible factors are

    F_e=(1+2t)/(1-t)^4,
    F_s=(1-t^2)^(-2),       F_c=(1-t^3)^(-1).

At finite bad places F_v=(F_e+F_s)/2. At infinity it is
(F_e+2F_c)/3 when Q=1 modulo 3, and F_s when Q=2 modulo 3.
All these rational functions have value one at zero and no poles in
|t|<1. Their zeros are not presumed absent.

The product (1.1) converges absolutely near zero, for example |z|<1/Q,
since there are at most Q^d+1 rational base points over F_(Q^d), and
the finitely many good-place functions satisfy F_h(t)=1+O(t).
It defines a nonzero germ with E_R(0)=1.

The preceding arithmetic Lie theorem identifies this same germ as its
ordinary Lie cohomological product at arithmetic parameter T=1, multiplied
by the exact finite collection of bad-place ratios F_v/S_(I_v,phi_v).
The ratios are source-defined. Their fractional local factors cancel
the first cubic branch of the uncorrected parent. This local observation
alone does not establish the larger continuation proved next.

## 2. Finite source extraction, with an absolutely convergent remainder

Let M_n be the actual dual homotopy-Lie grades, and write
epsilon_n=(-1)^(n+1). For a good Frobenius element h define

    B_(h,N)(t)=product_(1<=n<=N)
                         det(1-t^n h | M_n)^(-epsilon_n),
    H_(h,N)(t)=F_h(t)/B_(h,N)(t).                          (2.1)

Equivariant PBW gives, coefficientwise,

    H_(h,N)(t)=1+O(t^(N+1)).                              (2.2)

Every M_n is an actual S3 representation. Its eigenvalues have modulus
one. Hence B_(h,N) and H_(h,N) have no poles in the open unit disk;
B_(h,N) is also nonzero there. The exponents in the finite extraction
are integral, not class-function averages with fractional powers.

The finite arithmetic factors are the genuine compact-support L-functions

    L_U(M_n,T)=product_(v in U)
              det(1-T^(deg v) phi_v | M_n)^(-1).

They are rational functions from the actual finite spaces H_c^i(U,M_n),
as constructed using the localization sequence in the companion theorem.
Initially near zero,

    E_R(z)= product_(v in B) F_v(z^(deg v))
            * product_(1<=n<=N) L_U(M_n,z^n)^(epsilon_n)
            * product_(v in U) H_(phi_v,N)(z^(deg v)).     (2.3)

Fix r<1 and choose N with Q r^(N+1)<1. To control the final product,
first separate the finitely many places of degree below a fixed d_0.
For the remaining places, |z|<=r makes |z|^(deg v) uniformly small.
Choose d_0 large enough that |H_(h,N)(z^d)-1|<1/2 uniformly for
d>=d_0 and |z|<=r. This ensures the tail factors are nonzero there.
Equation (2.2), uniformly in the three possible classes h, bounds

    |H_(h,N)(z^d)-1| <= C_N r^((N+1)d).

The sum over all such places converges, because it is bounded by a
constant times sum_d (Q^d+1) r^((N+1)d). Thus the tail product converges
normally to a holomorphic function; any zeros come from the finitely
many separated factors, not from an uncontrolled limiting logarithm.
The separated factors themselves are holomorphic on |z|<1.

The finite cohomological product in (2.3) is rational in z. Therefore
(2.3) defines a single-valued meromorphic continuation to |z|<r.
Different choices of N agree near zero, hence everywhere on their common
disk by the identity theorem. Since r<1 was arbitrary, we obtain

    E_R is single-valued meromorphic on |z|<1.             (2.4)

This does not enlarge the trace-class disk of the original infinite
Lie operator. Its ordinary determinant still has the sharp threshold
|z|<1/2. The continuation uses finitely many genuine cohomological
factors plus a new convergent Euler remainder for each larger disk.

## 3. Local split-place zeros cannot cancel

Suppose there is a completely split good closed place of degree d.
Every solution z_0 of

    z_0^d=-1/2                                            (3.1)

lies in the unit disk. In (2.3), choose r>|z_0| and then N as above.
The factor for that place has

    H_(e,N)(z_0^d)=F_e(-1/2)/B_(e,N)(-1/2)=0,

and its denominator is nonzero. The convergent Euler remainder has no
poles. Neither does the bad-place Segre product.

It remains to check the finite cohomological factor, where a pole could
otherwise cancel this zero. The source localization sequence expresses
H_c^1(U,M_n) using proper-curve H^1 and a boundary quotient of a finite
Frobenius permutation representation. Its eigenvalues therefore have
absolute value sqrt(Q) or 1. H_c^2 has eigenvalue Q when present;
H_c^0 is zero. Consequently every finite-factor zero or pole in z has
one of the moduli

    1,      Q^(-1/(2n)),      Q^(-1/n).                   (3.2)

These are source weight statements, independent of Hermitian norm choices.
But |z_0|=2^(-1/d). Equality with either nonunit modulus in (3.2) would
give 2^(2n)=Q^d or 2^n=Q^d, impossible because Q is odd. Thus the finite
cohomological factor is analytic and nonzero at z_0. The zero survives:

    E_R(z_0)=0 whenever a split good degree-d place exists. (3.3)

This is an exact noncancellation argument; merely displaying zeros of
individual Euler factors would not have sufficed.

## 4. Split places in every sufficiently large degree

Let N_e(d) be the number of good F_(Q^d)-rational base points with
identity Frobenius, and let pi_split(d) count split good closed places
of exact degree d. The regular cover gives

    6 N_e(d)=#Z(F_(Q^d)) - #bad points of Z(F_(Q^d)).

There are at most fourteen geometric bad points upstairs. The imported
genus-three Weil bound gives

    N_e(d)=Q^d/6+O(Q^(d/2)).                              (4.1)

Contributions from base places of proper degree dividing d satisfy

    0 <= N_e(d)-d pi_split(d)
       <= sum_(e|d, e<d) (Q^e+1)
       <= d (Q^(d/2)+1).                                 (4.2)

Some nonsplit proper-degree places may become split over the extension;
(4.2) deliberately includes all of them. It makes no unjustified
Möbius inversion that ignores their Frobenius powers. Combining gives

    pi_split(d)=Q^d/(6d)+O(Q^(d/2)).                      (4.3)

In particular pi_split(d)>0 for every sufficiently large d. This is a
consequence of the proved cover and the classical Weil bound, not an
extrapolation from the finite source panels or an extra prime search.

## 5. Exact natural boundary and functional-equation limit

For every sufficiently large d, all d roots of (3.1) are zeros of E_R.
Their radii tend to one and their arguments form grids of mesh 2pi/d.
They therefore accumulate at every point of |z|=1.

A meromorphic continuation through any such point would have zeros
accumulating at an interior point of its domain. A pole cannot be their
accumulation point, and after removal of a possible pole the identity
theorem would force the continuation to vanish identically. This
contradicts E_R(0)=1. We have proved

    |z|=1 is a meromorphic natural boundary of E_R.        (5.1)

It follows in particular that no nonzero rational R(z) can satisfy

    E_R(z)=R(z) E_R(1/(Qz))                               (5.2)

on the annulus 1/Q<|z|<1. The right side would give a meromorphic
continuation across the unit circle, since its inner argument remains
strictly inside the already proved disk there. The same argument applies
to a prefactor meromorphic across that boundary. This does not exclude
arbitrary separate functions defined outside the circle.

In the coordinate z=Q^(-s), the result gives meromorphic continuation on
Re(s)>0 and a natural boundary on Re(s)=0. The exhibited zeros satisfy
Re(s)=log(2)/(d log Q), which varies with d. This source does not acquire
a single classical critical line or a usual global reciprocal functional
equation merely because its finite arithmetic constituents have Weil
duality. No number-field or RH/GRH conclusion is asserted.

## 6. The first arithmetic pole and a certified residue

The first actual Lie grade is M_1=V_std tensor W_perm, the regular S3
representation. Its compact-support L-function is the zeta function of
the open cover Z_U=Z minus the fourteen geometric boundary points.
For N=1 the residual good-place factors are explicitly

    H_(e,1)(t)=(1+2t)(1-t)^2=1-3t^2+2t^3,
    H_(s,1)(t)=1-t^2,       H_(c,1)(t)=1-t^3.             (6.1)

Their Euler product is holomorphic for |z|<Q^(-1/2). The finite bad
Segre factors have no poles in that disk. Moreover

    L_U(M_1,z)=Z_Z(z) product_(w in Z minus Z_U)
                                      (1-z^(deg w)).

The proper genus-three zeta function has denominator (1-z)(1-Qz).
Its numerator has reciprocal roots of absolute value sqrt(Q), so it
is nonzero at z=1/Q. At that positive point every factor in (6.1),
every boundary factor and every bad Segre factor is strictly positive.
The normally convergent tail is nonzero there. Therefore

    A_Q=lim_(z->1/Q) (1-Qz) E_R(z)>0,                    (6.2)

and E_R has exactly one pole in |z|<Q^(-1/2): a simple pole at 1/Q.
The positivity is a property of this actual source; it is not assumed
for arbitrary Frobenian Euler products.

Write E_R(z)=sum_(n>=0) a_n z^n near zero. Subtracting A_Q/(1-Qz)
leaves a holomorphic function on |z|<Q^(-1/2). The next subsection
improves this disk using the actual next three Lie grades and identifies
its exact first subleading poles. These are coefficients of the
constructed Euler product, not counts of primes or a new statement about
RH. Equation (6.2), together with (2.3) for N=1, specifies the constant
from the source without asserting that a finite numerical approximation
certifies it.

The two already counted extension fields nevertheless give a certified
rational interval for A_Q. Write b_j for the number of finite rational
branch points over F_(Q^j). The four branch roots occur in opposite pairs
and Frobenius commutes with their negation. Its orbit lengths on this
four-element set are therefore only 1, 2 or 4. The complete numbers of
closed branch places of these degrees are

    k_1=b_1,  k_2=(b_2-b_1)/2,  k_4=(4-b_2)/4.           (6.4)

At each finite branch place the three points upstairs have trivial
residual Frobenius, since the normalizer of transposition inertia in
S3 is that inertia subgroup itself. The infinity points upstairs are
two rational points if Q=1 modulo 3 and one degree-two point otherwise.
Thus the compact-support boundary factors in (6.2) are exactly known
from (6.4), as are the full finite bad Segre factors. The proper numerator
is the already authenticated product P_D P_E^2.

Let A_trunc be the residue expression (6.2) with all these exact finite
factors, but only good closed places of degrees one and two in the
H-product. This is an exactly computable positive rational number. For
d>=3 and t=Q^(-d), each H in (6.1) lies in (0,1), and

    0 <= -log H_(h,1)(t) <= 3 Q^(-2d)/(1-3Q^(-6)).

There are at most Q^d/d good closed places of exact degree d>=2: these
are a subset of the degree-d closed points of the affine line. Hence
the omitted logarithmic loss is at most

    B_Q=Q^(-3)/((1-Q^(-1))(1-3Q^(-6)))<1.

Using exp(-B_Q)>=1-B_Q gives the certified rational bracket

    A_trunc (1-B_Q) <= A_Q <= A_trunc.                   (6.5)

This small computation does not approximate a growing field or require
unbounded point counts. The proof of the tail bound, rather than an
empirical convergence observation, certifies the interval.

### 6.1 Exact quarter-power error from the next actual Lie grades

In the order (trivial, sign, standard), the first four actual Lie grades
have irreducible multiplicities

    M_1=(1,1,2), M_2=(1,0,1), M_3=(0,0,1), M_4=(0,1,1).                 (6.6)

These follow equivariantly from the actual Segre quadratic relation
space M_2=exterior^2(V_std) tensor exterior^2(W_perm), followed by PBW.
For completeness, their characters at (identity,transposition,three-cycle)
are (6,0,0), (3,1,0), (2,0,-1), (3,-1,0). They are not scalar
multiplicities inferred from one fitted Hilbert series.

Let P_E be the proper elliptic numerator for the standard constituent
and P_D that for the sign constituent. Ignoring boundary determinants,
which have zeros/poles only on |z|=1, their four finite factors are

    n=1: Z_Z(z),
    n=2: (1-z^2)(1-Qz^2)/P_E(z^2),
    n=3: P_E(z^3),
    n=4: 1/(P_D(z^4) P_E(z^4)).                         (6.7)

With N=3, the remainder converges for |z|<Q^(-1/4). Equations (6.7)
show that after the first simple pole is removed, there is no pole
in this disk. Thus for every epsilon>0,

    a_n=A_Q Q^n+O_(Q,epsilon)((Q^(1/4)+epsilon)^n).        (6.8)

The quarter-power scale is exact, not merely a convenient upper bound.
Take N=4 and a radius strictly between Q^(-1/4) and Q^(-1/5).
The only possible subleading poles up to that radius are the roots of
P_E(z^2). None can be canceled by the other finite cohomological factors:
their weight circles in (6.7) are different, and M_4 has no trivial
constituent that could add a zero on the quarter-power circle.

We must also exclude cancellation by the remaining local Segre factors.
The actual bad-place numerators, after removing cyclotomic denominators,
are

    C2:            1+t+3t^2+t^3,
    split C3:      1-t+3t^2,
    nonsplit C3:   1.                                   (6.9)

Every root of the first polynomial is an algebraic unit, since its
polynomial is monic with constant term one. The two roots of the
second have modulus 1/sqrt(3). The only good-place numerator zero is
-1/2. If P_E(z_0^2)=0, then z_0^2=alpha^(-1) for an elliptic Q-Weil
number alpha. Every algebraic conjugate of z_0 has modulus Q^(-1/4).
Consequently no positive power of z_0 can be an algebraic unit: its
nonzero norm would have modulus strictly below one. Nor can its d-th
power have modulus 1/2 or 1/sqrt(3), since that would require Q^d=16
or Q^d=9, respectively, impossible in characteristic greater than three.
Thus every actual local factor is finite and nonzero at z_0. The normally
convergent tail is nonzero there as well, by the small-factor bound in
Section 2. The denominator P_E(z^2) therefore gives poles of exactly its
root multiplicities.

By the power-series radius formula, this proves the sharp statement

    limsup_(n->infinity) |a_n-A_Q Q^n|^(1/n)=Q^(1/4).     (6.10)

It allows oscillation and possible repeated poles; it does not claim
that the error has one sign or one nonoscillating asymptotic constant.
The proof uses finite source cohomology and exact local noncancellation,
not a numerical fit to a long coefficient list.

## 7. A finite-group criterion and the existing S4 source

The continuation argument has a useful precise extension. Let a fixed
geometrically connected finite Galois cover of smooth curves over F_Q
have group G. Let the good-place series F_h(t) come from an actual
G-equivariant Segre algebra, with finite-dimensional actual Koszul Lie
grades M_n and equivariant PBW as in (2.1)--(2.2). Use the full invariant
Segre grades at every ramified place. Suppose the finitely many local
Hilbert series are rational with no poles in |t|<1. These conditions
hold for the two explicit covers in these packets; they are hypotheses
of the general statement, not conclusions about arbitrary coefficient
tables.

Finite integral-exponent extraction then gives single-valued meromorphic
continuation to |z|<1, by exactly Section 2. The finite cover realizes
the coefficient sheaves inside its proper and compact-support cohomology,
so the only finite-factor zero/pole moduli are the weight circles (3.2).
The regular-cover point-count argument also gives

    pi_split(d)=Q^d/(|G| d)+O(Q^(d/2))

for every sufficiently large degree, with constants depending on the
fixed cover. If the identity local Hilbert series has a zero t_0 with
0<rho=|t_0|<1 satisfying

    rho^a != Q^(-b) for every pair of positive integers a,b,             (7.1)

none of the zeros z^d=t_0 can meet a weight circle. Sections 3--5 prove
that the unit circle is a meromorphic natural boundary. This is a
sufficient criterion. No converse or classification is claimed when
(7.1) fails.

Apply it to the existing actual genus-nineteen S4 closure and source

    R_j=Sym^j(V_std, dimension 3) tensor
        Sym^j(W_perm, dimension 4).

Its identity Hilbert series is

    F_e(t)=(1+6t+3t^2)/(1-t)^6.

The numerator has a zero t_0=-rho, rho=(3-sqrt(6))/3 in (0,1).
Its algebraic conjugate rho'=(3+sqrt(6))/3 exceeds one. If rho^a=Q^(-b),
conjugation of the rational right side would give (rho')^a=Q^(-b)<1,
a contradiction. Thus the full source-corrected S4 Segre Euler product
also continues meromorphically exactly to the unit disk, with natural
boundary there. The geometry and source used here are the already frozen
[S4 cover packet](../global-s4-resolvent/S4_RESOLVENT_AND_RAMIFIED_FROBENIUS.md); no new
curve family or unverified point-count extrapolation is being introduced.
The runtime also binds the exact frozen Git source.

For a small direct source check, the first grades have character values
on (e,transposition,double-transposition,three-cycle,four-cycle)

    M_1=V_std tensor W_perm:                 (12,2,0,0,0),
    M_2=exterior^2(V_std) tensor exterior^2(W_perm):
                                             (18,0,2,0,0).

Their irreducible multiplicities in the frozen S4 table order are
(1,0,1,2,1) and (1,1,2,2,2). The quadratic relation space defining
M_2 is derived from the actual Segre algebra before comparison with
the Hilbert series. These finite controls authenticate the source but
do not replace the all-grade PBW theorem or the continuation proof.

## 8. Bounded checks and their role

The replay uses only the existing degree-one and degree-two primitive
Frobenius histograms. If N_h(j) counts good rational base points of class
h over F_(Q^j), then its exact degree-two closed-place counts are

    pi_e(2)=(N_e(2)-N_e(1)-N_s(1))/2,
    pi_s(2)=N_s(2)/2,
    pi_c(2)=(N_c(2)-N_c(1))/2.

These formulas retain the effect of squaring each S3 Frobenius class.
The full source Euler series through degree two is compared with the
independent finite Lie cohomology factors and the actual ramification
correction. The tests also check finite Koszul extraction for several
grade cutoffs, including the vanishing of every required low coefficient
of H_(h,N)-1.

The unit-disk continuation, all-degree split-place theorem, weight-circle
noncancellation and natural boundary are proved above. Finite coefficients
authenticate the source operations; they do not certify those infinite
claims by sampling. Root execution and independent exact-SHA proof/code
review are recorded separately from the bound files.
