# Positive full signed blocks, and the obstruction in higher fixed width

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required.
RH and positivity in arbitrary width remain UNPROVED.
Local labels SP7-4 through SP7-6. No external novelty claim.
Definitions, full source Q, and packets E_(m,d) are in SIGNED_TAIL_MATRICES.md.

## 1. SP7-4: every actual three-dimensional consecutive block is positive

For every integer m>=5, the original full xi form is strictly positive on

    E_(m,2)=span{u_m,u_(m+1),u_(m+2)},
    Laplace(u_j)(A)=A/(A+1)^j.                            (B1)

Coefficients may have arbitrary real signs. In matrix language, every
three-by-three matrix

    M^(m)_ij=sum_A A^2/(A+1)^(2m+i+j),     0<=i,j<=2,     (B2)

is strictly positive definite. All zero multiplicities are retained.
This is an infinite family in m, not a finite scan or only pairwise signs.
It is an explicit pole-dominance deduction, not a new general moment theorem.

### Inputs and a quantitative form

Import V100: every nontrivial zeta zero with 0<Im rho<=100 is on the line.
This is a restriction of Platt--Trudgian's published verification [V1];
that full computation is not rerun. Separately verify by directed intervals
that Xi has a sign change in each of

    (14,15), (21,22), (25,26).                             (B3)

The six endpoint signs are reconstructed in verify_low_zeros.py. This
only proves existence of a line zero in each interval, not uniqueness or
simplicity. The mpmath interval-Gamma implementation is an explicit trust
dependency for this small numerical input; see VALIDATION.md.

Choose one zero from each interval and write its real invariant parameter
as a_i=gamma_i^2+1/4, and w_i=1/(a_i+1). For any real polynomial P of
degree at most two the stronger statement is

    sum_A A^2/(A+1)^(2m) P(1/(A+1))^2
       > (31/32) 196^2/678^(2m) sum_(i=1)^3 P(w_i)^2.     (B4)

The right side is strictly positive when P is nonzero. Replacing
P(w) by p(1-(5/4)w) identifies this with the notation in the sibling proof.
The w_i occur only in the proof and its lower bound, NOT in the definition
of the source matrices or their test vectors.

### Complete tail proof

The intervals (B3) imply the following decreasing, disjoint intervals:

    4/905  < w_1 < 4/789,
    4/1941 < w_2 < 4/1769,
    4/2709 < w_3 < 4/2505.                               (B5)

Let l_i and h_i be the displayed lower and upper bounds. Let r=1/10001,
and let sep_ij be the minimum distance between the i-th and j-th intervals:
sep_ij=l_i-h_j for i<j and sep_ij=l_j-h_i for i>j.
For |w|<=r the Lagrange cardinal polynomial at w_i satisfies

    |L_i(w)| <= K_i:=product_(j!=i) (r+h_j)/sep_ij.

Every number here is rational, and direct integer arithmetic gives

    K_1^2+K_2^2+K_3^2 < 164.                             (B6)

Thus Lagrange interpolation followed by Cauchy--Schwarz yields, uniformly
over all real coefficient choices,

    |P(w)|^2 <=164 sum_i P(w_i)^2,   |w|<=1/10001.        (B7)

For every unverified zero gamma>100, x=Re A>10000, so
|1/(A+1)|<1/10001. The source budget (S1) from the sibling proof gives

    sum_(gamma>100) |A|^2/|A+1|^(2m)
       <=2*10000^(3-2m),            m>=2.                (B8)

Indeed each summand is at most 2x^(3-2m)/x, and sum_A 1/x<1.
Combine (B7)--(B8) to bound the absolute tail by

    328*10000^(3-2m) sum_i P(w_i)^2.                     (B9)

Every low zero contributes nonnegatively by V100. Each selected zero
has a_i>196 and a_i+1<678, hence its weight is >196^2/678^(2m).
At m=5 exact rational arithmetic gives

    [328*10000^3/196^2]*(678/10000)^10 <1/32.             (B10)

The ratio decreases by (678/10000)^2 when m increases by one. Therefore
(B9) is less than 1/32 of the retained reservoir at every m>=5. This proves
(B4) and (B2). All omitted zeros and all polynomial cancellation are paid.
Multiplicity merely supplies additional nonnegative low terms. QED.

The preceding formula also gives an explicit general finite-reservoir
lemma: for any r disjoint intervals for real invariant parameters below a
verified height T, replace (B6) by the sum of squares of their Lagrange
bounds and compare the tail 2T^(6-4m) with the minimum retained weight.
For polynomials of degree at most r-1, a strict comparison proves positivity
for all real coefficients. No claim for arbitrarily many such real nodes
is made without the corresponding input.

## 2. Endpoint certificate and its analytic remainder

For s=1/2+it, Euler's transformation of eta(s) is

    eta(s)=sum_(k>=0) 2^(-k-1)
                  sum_(j=0)^k (-1)^j binom(k,j)(j+1)^(-s).

The kth inner difference is

    1/Gamma(s) integral_0^infinity
                x^(s-1)exp(-x)(1-exp(-x))^k dx.

Its absolute value is <=sqrt(pi)/|Gamma(1/2+it)|
=sqrt(cosh(pi t)). Thus truncating at k=K-1 leaves absolute error
<=2^(-K)sqrt(cosh(pi t)). For all six endpoints t<=26,

    sqrt(cosh(pi t)) < exp(41) < 3^41 < 2^65.

The script takes K=192, so error<2^(-127), enclosed in a complex rectangle
of half-width 2^(-120). It divides by 1-2^(1-s) and multiplies the completed
xi factors using directed intervals at 80 decimal places. The returned
real intervals have the prescribed alternating signs, and every imaginary
interval contains zero. Endpoint signs are an input to (B3), not a complete
verification of V100. The exact returned rational bounds are in low_zeros.json.

## 3. SP7-5: eventual fixed-width inertia of a leading pole cluster

This theorem clarifies the unbounded-width obligation rather than hiding it.
It uses no finite zero verification. Let R>0 be such that no invariant
parameter satisfies |A+1|=R and at least one satisfies |A+1|<R.
Let S be the finite set of DISTINCT parameters with |A+1|<R. It is closed
under conjugation. Put s=|S|, and let q count its nonreal conjugate pairs.

For all sufficiently large integers m, the full form on E_(m,s-1) has

    exactly q negative eigenvalues and s-q positive eigenvalues. (B11)

This is about the inertia of the finite form, not about its eigenvalue
magnitudes in the L2 metric. Its threshold depends on the actual separated
cluster. It is not claimed computable without that cluster's data.

### Proof

Write w_A=1/(A+1). The finite set has

    q0=min_(A in S)|w_A| > q1=max_(A outside S)|w_A| >=0.

If the complement is empty its contribution below is zero. For the actual
infinite xi list, the positive maximum q1 is attained because w_A->0.
The strict gap follows from the choice of R and discreteness.

Interpolation polynomials P of degree at most s-1 may prescribe the values

    v_A=A w_A^m P(w_A),     A in S,

arbitrarily subject to v_(bar A)=conjugate(v_A). This is an invertible
real coordinate change in E_(m,s-1). The selected part of the quadratic
form is exactly sum_(A in S) multiplicity(A)*v_A^2. A real parameter has
one positive coordinate; a conjugate pair v=a+ib contributes
2 multiplicity(A)(a^2-b^2), with one positive and one negative coordinate.
This finite form is nondegenerate and has the claimed inertia.

The complement is uniformly small in these v-coordinates. The Lagrange
cardinal polynomials of the fixed nodes w_A are uniformly bounded on
|w|<=q1, and their interpolation values have magnitude at most
C_S q0^(-m)||v||. Hence

    sup_(|w|<=q1)|P(w)|^2 <= C_S' q0^(-2m)||v||^2.

Also, for m>=2,

    sum_(A outside S)|A|^2 |w_A|^(2m)
      <=q1^(2m-4) sum_(A outside S)|A|^2 |w_A|^4.

The last sum is finite by (S1) and x>1. The complement is therefore
O_S((q1/q0)^(2m))||v||^2. Perturbation of the nondegenerate finite form
preserves its inertia once this bound is sufficiently small. Multiplicities
have remained scalar weights throughout. QED.

In particular, if even one off-line zero exists, some FIXED finite width
d has a negative direction on E_(m,d) for every sufficiently large m.
Such packets eventually satisfy the signed-tail theorem (S20) for every
fixed cutoff X. A negative omitted-tail matrix does not preclude a much
smaller negative full residue after the two large terms cancel.

Thus eventual positivity for every fixed width would imply RH. SP7-4
settles width two (three generators), not that all-width statement. The
proof does not assume that the required real reservoir is arbitrarily large.

## 4. SP7-6: an exact cancellation control at every shift

This is NOT actual xi. Take the three invariant parameters

    4, 8+i, 8-i,

each of multiplicity one. They satisfy x>1, y^2<=x and sum 1/x=1/2<1.
Their positive heat is

    S_F(t)=exp(-4t)+2exp(-8t)cos t >0, t>0.

For t<=1/4, cos t>0. For t>=1/4, exp(4t)>=e>2, proving strict positivity.
For every integer m>=2 interpolate a real polynomial p_m of degree at most
two at z_A=(A-1/4)/(A+1), with values

    p_m(z_4)=0,
    p_m(z_(8+i))= i(9+i)^m/(8+i),
    p_m(z_(8-i))=-i(9-i)^m/(8-i).

The coefficients are rational: the nodes and data are Gaussian-rational,
and conjugation invariance makes the interpolant real. The resulting
R=A/(A+1)^m p_m(z_A) has values 0,i,-i, so the FULL form is exactly

    Q_F=-2.                                               (B12)

This is a negative signed combination inside E_(m,2) at every shift.
It is compatible with the coefficient-uniform exponential smallness of
(S14): its real-frequency norm I grows to compensate the scaled coefficients.
It is not compatible with the actual three-real-zero input of SP7-4,
which this synthetic model lacks. No Euler product is assigned to it.

## 5. Where the continuation stops

SP7-3 proves an arbitrary-vector signed TAIL inequality in unbounded rank.
SP7-4 proves the FULL sign for an infinite family of three-dimensional
signed blocks. These are different advances with different inputs.
SP7-5 shows why a growing denominator order is not enough to evade the
remaining obstruction: a hypothetical exceptional cluster lives in a fixed
width and survives all sufficiently high shifts. The new tail theorem can
hold there while the exponentially smaller full form has either sign.

No theorem in this packet makes the full matrix positive at every width,
proves RH, gives a new zero-free region, or improves a zero proportion.
The unsettled arithmetic requirement is control of the sign of the full
residue after tail cancellation for arbitrary width. It is not completed
by the excellent size bound on that residue or by the sign of the tail.
