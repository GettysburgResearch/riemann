# Fully resonant coherent source: exactly two double poles and an explicit coefficient decomposition

Retain the actual S3 coherent quadratic place-Euler source E_chi from
the frozen packets. Assume that both proper elliptic sectors are fully
resonant: every eigenvalue alpha of E and D satisfies alpha^2=Q.
Equivalently Q is a square and

    P_E(T)=(1-alpha_E T)^2,
    P_D(T)=(1-alpha_D T)^2,
    alpha_E,alpha_D in {sqrt(Q),-sqrt(Q)}.

The two signs need not agree. This note makes the finite-pole criterion
in [the exact pole-divisor theorem](S3_WEIGHT_CIRCLE_POLE_DIVISOR.md)
effective, without extrapolating a finite multiplicity table. The
source, normalization and original quarter-power coefficient growth
are unchanged.

## 1. Elementary uniform bounds on the actual source multiplicities

Write d_m=dim M_m, s_m=tr(s | M_m), c_m=tr(c | M_m), where s and c
are the actual transposition and three-cycle. The source irreducible
multiplicities are

    A_m=(d_m+3s_m+2c_m)/6,
    B_m=(d_m-3s_m+2c_m)/6,
    C_m=(d_m-c_m)/3.

In particular 2(B_m+C_m)=d_m-s_m; we will use the weaker but convenient
bound B_m+C_m<=d_m, which follows directly from the actual nonnegative
irreducible multiplicities.

Let b_r(g)=r[t^r]log F_g(t). The exact source Hilbert functions give

    b_r(e)=4-(-2)^r,
    b_r(s)=4 if 2 divides r, and0 otherwise,
    b_r(c)=3 if 3 divides r, and0 otherwise.

Equivariant PBW and Möbius inversion give the actual character formula

    tr(g | M_m)=(-1)^(m+1)/m
                 sum_(k|m) mu(k) b_(m/k)(g^k).           (1.1)

The g^k is essential: this is not inversion of a single scalar Hilbert
series. For m>1, the constant4 in the identity formula cancels because
sum_(k|m)mu(k)=0. Its leading term is 2^m/m, and every other exponent
m/k is a distinct integer at most floor(m/2). Therefore

    [2^m-2^(floor(m/2)+1)+2]/m <= d_m
       <= [2^m+2^(floor(m/2)+1)-2]/m.                  (1.2)

For either nonidentity g=s,c, its k=1 coefficient has absolute value
at most4. A divisor with g^k nonidentity again contributes at most4;
one with g^k=e must have k>=2 and contributes at most4+2^(m/k).
The number of divisors is at most m. Summing the same distinct proper
exponents proves

    abs(s_m),abs(c_m)
      <=4+[2^(floor(m/2)+1)-2]/m.                      (1.3)

These intentionally loose bounds use only the exact actual character
formula, the triangle inequality and a finite geometric sum. They
contain no asymptotic remainder constant inferred from data.

For every even n>=2, equations (1.2)--(1.3) imply

    A_(2n) >= [4^n-12*2^n-40n+12]/(12n),              (1.4)

and

    2(B_n+C_n) <= 2d_n
       <= 2[2^n+2^(n/2+1)-2]/n.                       (1.5)

The sufficient inequality for strict domination is consequently

    4^n > 36*2^n+48*2^(n/2)+40n-60.                 (1.6)

At n=6 its left side exceeds its right side by1228. Divide both
sides by2^n. The left side2^n increases; on the right,36 is constant,
48*2^(-n/2) decreases, and (40n-60)2^(-n) decreases for n>=3.
Thus (1.6) holds for every integer n>=6, in particular every even one.
We have proved the uniform source statement

    A_(2n)>2(B_n+C_n) for every even n>=6.             (1.7)

The infinitely many grades are covered by this elementary monotonicity
argument. A finite replay checks the starting margin and source formulas;
it is not being used to extrapolate the inequality.

## 2. The two low grades and the complete pole list

The actual low source multiplicities are

    (A_2,B_2,C_2)=(1,0,1), (A_4,B_4,C_4)=(0,1,1),
    (A_8,B_8,C_8)=(4,6,10).

At even grade n, the exact pole-divisor theorem gives the signed order
at an elliptic point alpha=z^(-n) as

    A_(2n)-B_n m_D(alpha)-C_n m_E(alpha),              (2.1)

because alpha^2=Q. The local numerator noncancellation has already been
proved for every such arithmetic point in characteristic greater than
three. The multiplicities m_D,m_E are each either0 or2 in this case.

At n=2, B_2=0, C_2=1 and A_4=0. Thus the two roots of

    z^2=alpha_E^(-1)                                  (2.2)

are poles of order exactly two. They are distinct and nonzero.

At n=4, A_8=4 and B_4=C_4=1. If alpha_D=alpha_E, their combined
denominator order is4 and the signed order is zero. If the signs
differ, each of the two eigenvalue sets has denominator order2 and
the signed order is positive2. In neither case is there a pole.

For even n>=6, (1.7) makes (2.1) strictly positive at every elliptic
point, including coincident E/D eigenvalues. Odd coherent grades
contribute only polynomials and have no principal H^2 poles. The
complete interior pole classification is therefore

    E_chi has exactly the two double poles in (2.2),
    and no other poles in the open unit disk.          (2.3)

No generic simplicity or agreement of the two elliptic signs is assumed.
This result is stronger than eventual disappearance of poles: it gives
the exact finite list for every fully resonant source in the family.

## 3. The excess arithmetic zeros still force the natural boundary

Fix alpha_E. For every even n>=6, all n roots of z^n=alpha_E^(-1)
are now true zeros of E_chi by strict positivity of (2.1), not merely
points at which a pole was removed. Their radii Q^(-1/(2n)) tend to1
and their angular grids have mesh2pi/n. They accumulate at every
point of the unit circle.

A meromorphic continuation through such a point would have zeros
accumulating in its interior. They cannot accumulate at a pole; after
removing a possible pole, the identity theorem would force the function
to vanish identically. This contradicts E_chi(0)=1. The fully resonant
case therefore has its own cohomological proof of the meromorphic
natural boundary at abs(z)=1, using the excess principal zeros.

This proof does not require another split-place count. It complements
the nonresonant case, where the arithmetic poles themselves form dense
grids. A finite number of interior poles does not imply continuation
across the boundary.

## 4. The exact finite exponential-polynomial coefficient part

Let z_+,z_- be the two poles from (2.2), so z_-=-z_+ and
abs(z_j)=Q^(-1/4). At each pole write its normalized principal part
as

    C_j/(1-z/z_j)^2 + D_j/(1-z/z_j).

The constants are complex and C_j!=0 because the pole has exact order
two. No algebraicity of these residues is asserted. Let P(z) be the
sum of these four terms. It is a rational function over C, determined
by the actual source's principal parts. Then

    R(z)=E_chi(z)-P(z)

is holomorphic on the unit disk. The rational P is holomorphic near
every point of its boundary, so R retains the meromorphic natural
boundary. If R(z)=sum_(m>=0) r_m z^m, the radius formula gives

    limsup_(m->infinity) abs(r_m)^(1/m)=1,
    r_m=O_eta((1+eta)^m) for every eta>0.                (4.1)

Writing E_chi(z)=sum c_m z^m and a_j=C_j, b_j=C_j+D_j yields the exact
coefficient decomposition

    c_m=sum_(j in {+,-}) (a_j m+b_j) z_j^(-m)+r_m.       (4.2)

The two complex exponentials can interfere on one parity; no fixed sign
or nonoscillating asymptotic is claimed. The original coefficient
limsup remains Q^(1/4), since the two poles are still present in the
original source. Equation (4.2) describes its finite polar contribution;
it does not silently replace E_chi by a newly normalized function.

## 5. A different finite cohomological operation clears the two poles

There is also a source-specified polynomial modification, distinct from
both E_chi and the complex principal-part subtraction above:

    H(z)=P_E(z^2) E_chi(z)=(1-alpha_E z^2)^2 E_chi(z).   (5.1)

The factor is the actual elliptic cohomological determinant from the
second relation grade. Equation (2.3) shows that H is holomorphic on
the unit disk. It retains the dense arithmetic zeros from Section3,
since those higher-grade circles differ from the two removed poles.
Thus H also has a meromorphic natural boundary at abs(z)=1.

The factor P_E(z^2) is the unique polynomial of minimal degree, normalized to have
constant term one, which clears all interior poles: any polynomial
whose product with E_chi is holomorphic must vanish to order at least
two at both z_+ and z_-. Its degree is at least4, and equality determines
the normalized polynomial P_E(z^2). This is a minimality assertion among
polynomials, not among every possible analytic regularization.

All coefficients c_m of the original place source are integers. Its
explicit invariant traces are integers at each place, and each global
coefficient involves only finitely many effective divisors. In the
fully resonant case alpha_E=+/-sqrt(Q) is itself an integer. Consequently
the Taylor coefficients of H obey the exact integer recurrence

    h_m=c_m-2 alpha_E c_(m-2)+Q c_(m-4),                (5.2)

where negative-index coefficients are zero. The boundary and radius
formula give limsup abs(h_m)^(1/m)=1. These h_m are coefficients of a
new, explicitly modified source function. This does not improve the
Q^(1/4) growth of the original c_m. It is also different from the
generally noninteger residual sequence r_m in the complex principal-part
decomposition. No new full invariant tensor-algebra model at ramified
places is inferred merely by multiplying two global determinants.

## 6. Bounded source checks

The replay authenticates the exact previous source and pole-divisor
packet. It evaluates the displayed Möbius/Adams character formula on
small actual grades and compares it with the frozen source characters,
retaining the powers of the transposition and three-cycle. It checks
the n=6 starting margin, the elementary decreasing normalized bound,
and the exact n=2,4,8 multiplicities. Low-grade checks cover both equal
and opposite fully resonant elliptic signs.

The coefficient-control examples verify the exact algebra of two
normalized double principal parts, including opposite poles and parity
cancellation. They are stated algebraic calibration examples, not
claimed computations of the actual source's complex residues. No
new point-count field or new curve source is used. The all-grade
threshold, exact pole list and boundary proof are analytic arguments,
not empirical conclusions from the finite controls.
The replay also checks the polynomial coefficient recurrence on declared
integer calibration sequences and distinguishes that modified sequence
from the original one.
