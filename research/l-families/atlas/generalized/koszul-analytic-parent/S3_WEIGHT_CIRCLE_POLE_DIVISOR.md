# Exact arithmetic pole divisor of the two S3 place Euler sources

Status: proposed source-specific pole classification for the untwisted
and coherent quadratic full place-Euler products. This is a classification
of poles inside the unit disk, not of every zero: the local Segre
numerators also produce zeros away from the arithmetic factors.

Use the actual generic cubic and joint quadratic covers in
[the untwisted source theorem](S3_SEGRE_EULER_MEROMORPHIC_BOUNDARY.md)
and [the coherent source theorem](COHERENT_QUADRATIC_PLACE_EULER.md).
Write Q=p^f with p>3. All ramification, finite extraction and source
normalizations in those theorems remain in force. No new number-field
or RH conclusion is asserted.

## 1. The source multiplicities and finite arithmetic factors

Let A_n, B_n, C_n be the multiplicities of the trivial, sign and standard
representations in the actual Koszul Lie grade M_n. Use uppercase letters
to distinguish these multiplicities from Euler coefficients. Put
epsilon_n=(-1)^(n+1). The proper untwisted factor is

    L(M_n,T)=P_D(T)^(B_n) P_E(T)^(C_n)
                          /((1-T)^(A_n)(1-QT)^(A_n)).     (1.1)

P_D and P_E are the two actual elliptic numerator polynomials. The
coherent quadratic operation replaces odd grades by M_n tensor chi;
their proper factors are the polynomials

    P_(D,chi)(T)^(B_n) P_(E,chi)(T)^(C_n),                (1.2)

with no H^0 or H^2. The trivial constituent tensored with chi also has
no proper H^1, since w^2=u is a genus-zero cover. Even grades retain
(1.1). Compact-support boundary determinants have roots only on the
unit circle and cannot affect the interior pole divisor.

For every r<1, finite extraction gives the product of these factors
through a cutoff N satisfying Q r^(N+1)<1, times actual finite bad
factors and a normally convergent holomorphic good-place remainder.
Consequently any pole inside |z|<r comes from these finitely many
cohomological factors. A zero of the Euler remainder could still cancel
it; the next section excludes that at the precise arithmetic points.

## 2. A uniform prime-support noncancellation lemma

Suppose z_0 is an interior zero or pole of a positive-weight arithmetic
factor. Thus either z_0^n=alpha^(-1), where alpha is an actual Q-Weil
number of weight one, or z_0^n=Q^(-1). The inverse z_0^(-1) is an
algebraic integer, and all its conjugates have the same modulus greater
than one. For every positive integer d, beta=z_0^(-d) is therefore an
algebraic integer whose nonzero absolute norm is a positive power of p.
The same holds with d replaced by 2d.

If beta is a root of a monic polynomial in Z[X] with constant term k,
its monic integral minimal polynomial divides that polynomial over Z.
Hence |Norm(beta)| divides |k|. This is impossible if all prime divisors
of k are among 2 and 3.

Apply this observation to the actual source numerator polynomials. The
following reciprocal polynomials are monic; signs at unramified quadratic
places may change coefficients but not their constant-term prime support.

| Local numerator | Reciprocal polynomial | Constant prime support |
| --- | --- | --- |
| Good identity, 1+2t or 1-2t | X+2 or X-2 | 2 |
| Old finite C2, 1+t+3t^2+t^3 | X^3+X^2+3X+1 | empty |
| Old split C3, 1-t+3t^2 | X^2-X+3 | 3 |
| New coherent zero, 1+14s+9s^2, s=t^2 | X^2+14X+9 | 3 |
| New coherent split infinity, 1+3s+10s^2+7s^3+3s^4 | X^4+3X^3+10X^2+7X+3 | 3 |

The remaining local numerators are one. Their denominators are products
of cyclotomic factors and have no zero inside the unit disk. With
t=z_0^d, the table and the norm argument show that every actual good or
bad local factor is finite and nonzero at z_0. The finitely extracted
local Lie determinants also have roots only on the unit circle. Finally,
the normally convergent small-factor tail is nonzero by the uniform
|H-1|<1/2 estimate. Thus the full Euler remainder is nonzero at every
arithmetic factor point under discussion.

This statement concerns these exact algebraic points. It is not a claim
that a local numerator has no zeros anywhere on a circle of the same
radius with an unrelated phase.

## 3. Exact signed orders and pole classification

Write m_D(n,z) for the multiplicity of z as a root of P_D(z^n), and
define m_E similarly. Define h_n(z)=1 if z^n=1/Q and zero otherwise;
these roots are simple. At an interior arithmetic factor point, the
untwisted source has the exact order

    ord_z E = sum_(n>=1) epsilon_n
                     (B_n m_D(n,z)+C_n m_E(n,z)-A_n h_n(z)).            (3.1)

Only finitely many terms can occur at one radius. Positive order means
a zero and negative order a pole. Boundary factors are absent, and
Section 2 proves that no unrecorded local numerator cancels this order.

The weight-one radius at grade n is Q^(-1/(2n)); the weight-two radius
at grade m is Q^(-1/m). They can coincide only when m=2n. It follows
that the entire interior pole list has the following form.

* For each odd m, every solution z^m=1/Q is an untwisted pole of order
  A_m when A_m>0. No integer weight-one grade has that radius.
* For each even n and each z with P_D(z^n)P_E(z^n)=0, put
  alpha=z^(-n). Its pole order, for BOTH untwisted and coherent sources,
  is exactly

    max(0, B_n m_D(n,z)+C_n m_E(n,z)
                          -A_(2n) 1_(alpha^2=Q)).        (3.2)

  Coincident elliptic eigenvalues are added with their multiplicities.
  If this number is zero, the point may be regular or a zero, according
  to the signed order; no pole is asserted there.
* The coherent source has no odd-grade H^2 poles, and it has no other
  interior poles. Its odd-grade proper factors (1.2) contribute only
  zeros, while the even factors give exactly (3.2).

In particular (3.2) accounts for a real cancellation that a pole list
formed from denominators alone would miss. An even grade's H^1 pole can
be removed by the H^2 zero of twice that grade.

## 4. Nonsquare fields and a second natural-boundary proof

If Q is not a square, an elliptic Q-Weil number cannot satisfy alpha^2=Q.
Indeed alpha also satisfies alpha^2-t alpha+Q=0 with integer trace t,
so t=2 alpha would be an integer and Q would be a square. Trace-zero
eigenvalues alpha=+/- i sqrt(Q) have alpha^2=-Q and do NOT cause the
cancellation in (3.2).

Thus for nonsquare Q every even-grade elliptic denominator pole survives.
The untwisted source has these poles and the odd-grade trivial poles;
the coherent source has exactly the even-grade elliptic poles.
The actual Lie multiplicities are identity-dominated:

    A_n ~ dim(M_n)/6, B_n ~ dim(M_n)/6,
    C_n ~ dim(M_n)/3, dim(M_n) ~ 2^n/n.

In particular C_n>0 for all sufficiently large even n. Fix an actual
elliptic eigenvalue alpha. All n roots of z^n=alpha^(-1), for those
even n, are poles approaching every point of the unit circle. This
gives a second proof of a meromorphic natural boundary there: an
extension would have interior accumulating poles. The earlier split-place
zero proof remains valid also for square Q and does not depend on this
nonsquare-field simplification.

### 4.1 Exactly when the coherent source has only finitely many poles

For this fixed S3 source, the coherent product has finitely many poles in
the unit disk if and only if every elliptic eigenvalue in P_D and P_E
satisfies alpha^2=Q. Equivalently Q is a square and each elliptic
polynomial has one of the forms

    (1-sqrt(Q) T)^2 or (1+sqrt(Q) T)^2.                  (4.1)

The two signs need not agree. This is a condition on these actual
Frobenius polynomials, not a general assertion about square fields.

If one eigenvalue fails the condition, its B_n or C_n multiplicity is
positive for every sufficiently large even n. Equation (3.2) then gives
infinitely many poles approaching every unit-circle point. Conversely,
if all eigenvalues satisfy it, every possible even-grade pole is subject
to the A_(2n) zero. The source asymptotics give

    A_(2n) ~ 4^n/(12n),
    2(B_n+C_n) ~ 2^n/n.

Thus A_(2n)>2(B_n+C_n) for every sufficiently large n. Formula (3.2)
cancels all sufficiently large even-grade poles, leaving only finitely
many possible grades and therefore finitely many poles. The exact
remaining finite list is still determined by (3.2); no uniform cutoff
or uncomputed finite list is asserted here. The untwisted product always
has infinitely many poles, since A_m>0 for all sufficiently large odd m.

For the untwisted source these odd-grade poles alone approach every point
of the unit circle, over every Q: their complete m-th-root grids have
radius Q^(-1/m) tending to one and angular spacing tending to zero.
Thus its pole-based natural-boundary proof does not require Q nonsquare.
For the coherent source a nonresonant elliptic eigenvalue similarly gives
dense poles; in the all-resonant case the earlier split-place zero proof
supplies the natural boundary despite the finite interior pole set.

In the finite-pole coherent case, subtract the sum of its finitely many
principal parts. This sum is a rational function with complex coefficients;
its residues are not asserted algebraic or rational. The remainder is
holomorphic throughout the unit disk and still has the same meromorphic
natural boundary, since a rational function extends across that circle.
Its Taylor coefficients consequently have limsup n-th-root magnitude one.
This is an analytic decomposition of the same function, not a newly
normalized Euler source or an improvement of the original coefficient
scale Q^(1/4).

## 5. A genuine square-field cancellation, without a large field count

The generic source with A=1, B=0 over F_7 is still a geometric S3 cover:
A is nonzero and -4A^3-27B^2 is nonzero. Its two elliptic sectors are

    E: y^2=x^3+x,
    D: v^2=u^4+3  over F_7.

Direct counts over this seven-element field give #E(F_7)=#D(F_7)=8.
For E the finite count is seven and there is one point at infinity.
For D the finite count is six and there are two points at infinity.
Both Frobenius matrices have trace zero and determinant seven, hence
their squares are -7 times the identity by Cayley--Hamilton. Over F_49,
without enumerating that field, their numerator polynomials are therefore

    P_E(T)=P_D(T)=(1+7T)^2.                              (5.1)

The actual Lie source has

    (A_4,B_4,C_4)=(0,1,1),
    (A_8,B_8,C_8)=(4,6,10).

At a root of z^4=-1/7, the grade-four denominator order is
2B_4+2C_4=4, and the grade-eight H^2 zero has order A_8=4.
Equation (3.2) says the apparent pole cancels exactly, for both sources.
This is not a cancellation of every even grade: at grade two the
elliptic pole survives because A_4=0, as proved in the earlier packets.
The example satisfies (4.1), so the coherent product has only finitely
many poles by Section 4.1, while retaining its unit-circle natural boundary.
We have not asserted that grade two is its only surviving pole grade.
The example demonstrates why the nonsquare hypothesis cannot be silently
dropped from the simpler pole list. No large-field enumeration, fitted
Frobenius polynomial or new curve family is needed.

## 6. Bounded verification and scope

The companion replay authenticates the existing source character and
curve adapters, computes finitely many actual Lie multiplicities, and
checks the recorded reciprocal-numerator table. It compares finite proper
factors with the signed-order rule, retains coincident E/D multiplicities,
and verifies the seven-point counts and Frobenius squaring in Section 5.
No F_49 enumeration is needed for that new example; the established
source panels keep their previous field caps.

The all-grade exact pole formula, eventual positive multiplicities and
natural boundary are mathematical arguments. Finite calculations do not
certify them by sampling. This pole classification does not claim an
entire zero divisor, a new cohomology theory, a universal classification
for other groups or ranks, or an RH implication.
