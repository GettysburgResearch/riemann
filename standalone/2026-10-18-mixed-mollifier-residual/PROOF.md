# Mixed mollifier--dual moments and a full-family signed residual bound

Status: PROPOSED complete deduction from the stated de Faveri large sieve and
the classical Hecke functional equation; independent mathematical review is
required. No RH, GRH, zero-density theorem, reciprocal-moment hypothesis or CT
theta estimate is used. The residual is L M - 1, NOT 1/L and NOT a critical
native Mobius moment. All moment orders and real parts are fixed unless stated
otherwise. The infinite analytic proof is not certified by the finite checker.

## 1. Family and the new conclusions

Fix n>=3, a number field F containing mu_n, and permissible fixed S/ray/generator
data for de Faveri's family. A row a is an n-th-power-free exterior integral
IDEAL, ordered by FULL ideal norm Na<=U. Keep a fixed finite-order Hecke twist
psi supported at S, and write

    L_a(s)=L_F^S(s,psi chi_a),
    M_A(s,a)=sum_(Nb<=A) mu_F(b) psi(b) chi_a(b) (Nb)^(-s),
    E_A(s,a)=L_a(s)M_A(s,a)-1.                         (1)

All sums retain the unit, distinct ideals with equal norm, and character zeros
at nonunits. A repeated prime in a product column is not silently removed.
The inducing conductor Q_a is bounded ABOVE by C Na, not assumed comparable
with Na. Implied constants retain all fixed family data and the compact height
interval |Im s|<=T0. No uniformity in F,n, moment order, sigma tending to 1/2,
or growing T0 is asserted. We fix 1/2<sigma=Re s<1 and put d=2sigma-1.

### Theorem A: concrete sextic improvement

For n=6, sigma=3/4 and A=U^(3/5),

    sum_(Na<=U) |E_A(3/4+it,a)|^2
             <<_(epsilon,T0) U^(11/15+epsilon), |t|<=T0.    (2)

The sum is over the ENTIRE family, with no deleted members and no cap. In
particular an actual zero, if one exists at the evaluated point, contributes
exactly one to (2). The bound does not exclude that contribution.

The strongest directly stated residual bound in #984 at sigma=3/4 uses
A=U^(1/4) and gives U^(7/8+epsilon). The new guaranteed error exponent is
smaller by 17/120, with a LONGER mollifier U^(3/5). This is a comparison of
the stated upper bounds, not a lower bound or optimality claim.

### Theorem B: threefold sextic improvement arbitrarily close to the line

For general fixed n>=3 let 0<d<=4/(5n), y=nd, and set

    a=y/4, x=1/2, A=U^a, X=U^x,
    p=ceil(4/[y(2-y)]).                                  (3)

Then

    sum_(Na<=U) |E_A((1+d)/2+it,a)|^2
             << U^(1-n*d^2/4+epsilon).                   (4)

Here p is an integer moment parameter, fixed after d and n. For n=6,
A=U^(3d/2) and the saving in the error exponent is 3d^2/2. The #984 choice
A=U^(d/2) gives saving d^2/2. Thus the new guarantee triples that saving on
EVERY fixed line 1/2<sigma<=17/30. The estimate is NOT uniform as d goes to
zero: p is approximately 2/(nd). This is not a limiting RH argument.

Theorem C below supplies all fixed even residual moments and proves both
specializations. It keeps the mixed characters in the functional-equation
remainder instead of making the false substitution chi(b)bar(chi(c))=chi(bc).

## 2. Imported input and a complete polynomial-moment lemma

The analytic large-sieve input is de Faveri, arXiv:2610.04045v1, Theorem 1.1:

    sum_(Na<=U)^flat |sum_(Nb<=V)^flat z_b chi_a(b)|^2
        << (UV)^epsilon K_n(U,V) sum_b |z_b|^2,
    K_n(U,V)=U+V+U^(1-1/n)V^(2/n)+U^(2/n)V^(1-1/n).       (5)

Both flat indices mean n-th-power-free, not squarefree. Positive row
restrictions and the conjugate matrix satisfy the same bound. Fixed psi is
absorbed into the common column coefficients. No claimed new proof of (5)
is supplied here. Its exact primary statement was freshly read.

Define the piecewise affine convex function

    k_n(v)=max(1,v,1-1/n+2v/n,2/n+(1-1/n)v), v>=0.       (6)

For common coefficients on V<Nb<=2V bounded by a fixed-order divisor function
times (Nb)^(-u), the complete-column consequence of (5) is

    squared row norm << (UV)^epsilon V^(1-2u)K_n(U,V).    (7)

Proof of support fidelity: write b=c e^n uniquely with c n-free, WITHOUT
requiring (c,e)=1. Then chi_a(b)=chi_a(c)1_((a,e)=1). The coefficient square
mass for fixed e is at most V^(1-2u+epsilon)(Ne)^(-n). Apply (5) after retaining
that row mask, then Minkowski in the row l2 norm. The root sum
sum_e (Ne)^(-n/2+epsilon) converges because n>=3. This proves (7). The argument
is a norm bound, not a claim that the mask is identically one.

For integer j>=1, raise M_A to its j-th power. Every ordered ideal tuple and
its individual cap remains in the coefficient. That coefficient is bounded
by d_j(b)(Nb)^(-sigma); its product norm is at most A^j. Applying (7) on
all dyads, with elementary d_j(b)<<(Nb)^eta and ideal counting, gives

    sum_a |M_A(s,a)|^(2j) << U^(m_j+epsilon),
    m_j=max(1,k_n(j a)-d j a), A=U^a.                    (8)

Convexity of k_n(v)-dv puts its maximum on [0,ja] at an endpoint. The unit
term explains the 1. Fixed-order divisor constants are retained. This step
uses neither inverse moments nor cancellation between different tuples.

## 3. Exact flat cutoff and the conductor-sensitive dual moments

Fix a smooth V on (0,infinity), equal to one for 0<y<=1, zero for y>=2.
Let X=U^x, 0<a<=x<=1, and put

    P_X(s,a)=sum_b (psi chi_a)(b)(Nb)^(-s)V(Nb/X).

For every NONPRINCIPAL inducing character the complete functional equation
writes L_a=P_X+R_X. For a primitive character, the dual is

    R_X(s,a)=epsilon_a Q_a^(1/2-s)
       sum_c conjugate((psi chi_a)(c))(Nc)^(s-1)
                            V_s(Nc X/Q_a).              (9)

The sign is included in V_s. Equation (9) is an exact smooth functional-
equation identity, not an assertion that a finite AFE main sum equals L.

Here are the required analytic details. Mellin inversion expresses P_X as
an integral of L_a(s+z)X^z Vhat(z) on a right line. Vhat has one simple pole
at zero, residue one, and rapid decay on fixed vertical lines. Move left
past zero to Re(s+z)<0; nonprincipal L is entire. Use the COMPLETE primitive
functional equation there and the absolutely convergent dual Dirichlet
series. This defines V_s by a Mellin integral. Moving its line further left
shows rapid decay for large positive argument; moving it to a sufficiently
small positive real z, below 1-sigma and before gamma poles, gives boundedness
at small argument after retaining the crossed residue. Fixed logarithmic
derivatives have the same properties, uniformly on |t|<=T0. Stirling and
rapid Vhat decay justify Fubini and horizontal limits. These are the standard
facts reconstructed in #984, Section 4; they do not use a reciprocal contour.

Partition by ACTUAL conductor Q and by norm C of the dual column. Localized
Fourier separation in log Q, log Nc produces common coefficient arrays with
integrable Fourier norms. Two fixed logarithmic derivatives of V_s suffice;
when a fixed j-th moment is taken, Minkowski is used before integrating these
parameters. Finite gamma and S types give finitely many such expressions.
A root number has modulus one and is harmless for the norm of R_X alone.

For a conductor dyad Q, and a dual-column dyad C, (7) applied after taking
the j-th power gives squared row norm of that power bounded by

    U^epsilon Q^(-jd) C^(jd) K_n(U,C^j)
          min(1,(C X/Q)^(-J)),                          (10)

where J can be made arbitrarily large, depending on j and the fixed data.
The common coefficients are conjugate characters throughout. For Q/X>=1,
Minkowski over C and the positive powers of C in all four monomials give

    sum_(row conductor~Q) |R_X|^(2j)
         << U^epsilon X^(-jd) K_n(U,(Q/X)^j).

All C>Q/X tails are included by choosing J sufficiently large. For Q/X<1,
EVERY C>=1 is in the decaying tail. The bound is then
O(U^(1+epsilon) Q^(-jd)(Q/X)^J), hence at most
O(U^(1+epsilon)X^(-jd)) for J>jd, after summing C. This treats subunit
lengths instead of substituting Q=U into a negative power.

As Q<=C U and K is increasing in its second variable, summing the conductor
dyads proves, for NONPRINCIPAL rows,

    sum_a |R_X(s,a)|^(2j) << U^(b_j+epsilon),
    b_j=k_n(j(1-x))-jd x.                               (11)

Fixed finite Euler omissions at S are not discarded: multiply the primitive
functional equation by their fixed Euler polynomial, and split the dual
ideal into its S-part and exterior part. The S-part has root weight
(Nc_S)^(sigma-1); its sum converges because sigma<1 and S is fixed. It only
shortens the effective exterior length. Thus all finite sums and infinite
S-supported tails preserve (10)--(11), with fixed constants.

Principal rows need different treatment. Their flat-cutoff identity includes
the pole at one. We do NOT apply (11) to them. For fixed family data there are
only finitely many inducing-principal n-free rows: any exterior prime of an
n-free index has nontrivial ramification, which an S-supported psi cannot
cancel. For these rows the FINAL residual is bounded directly by

    |E_A(s,a)|^(2r) << 1+A^(2r(1-sigma)).                (12)

At sigma=3/4 and x=3/5 the principal dual's fourth power can have size
X=U^(3/5), larger than the U^(1/2) bound in (11). This is why separating
principal rows is necessary even though their final residual fits Theorem A.

## 4. All fixed even moments of the actual signed residual

The main error has the exact coefficient expansion

    P_X M_A-1 = sum_(A<Nb<=2AX) (psi chi_a)(b)(Nb)^(-s) h(b),
    h(b)=sum_(e|b, Ne<=A) mu_F(e)V(Nb/(Ne X)).           (13)

Indeed, for 1<Nb<=A every divisor is present and Nb/Ne<=A<=X, so V=1 and
the full Mobius divisor sum vanishes. The unit contributes one and is
subtracted. This cancellation happens BEFORE applying any norm inequality.
For all remaining b, |h(b)|<=C d_2(b), uniformly in U.

Raise (13) to any fixed integer power r. Its product ideals lie in
A^r<Nb<=(2AX)^r and its coefficients are bounded by C_r d_(2r)(b)(Nb)^(-sigma).
Equation (7), all product dyads, and endpoint convexity therefore give

    sum_a |P_X M_A-1|^(2r) << U^(g_r+epsilon),
    g_r=max(k_n(ra)-dra, k_n(r(a+x))-dr(a+x)).            (14)

The common coefficient h depends on U but not the row. The uniformity of
(5) allows this dependence. No cancellation beyond the exactly zero lower
coefficients is assumed.

For the dual product, take any FIXED integer p>=2 and q=p/(p-1). Holder and
interpolation between the 2r and 4r moments give, on the nonprincipal rows,

 sum |M_A R_X|^(2r)
    <= (sum |M_A|^(2pr))^(1/p)
          (sum |R_X|^(2r))^((p-2)/p)
          (sum |R_X|^(4r))^(1/p).                       (15)

For example, p=3,r=1 uses exactly the M6, R2, R4 moments. This inequality
does NOT require statistical independence, removal of common primes, or a
same-character product identity. It stays valid for zero-selected rows.
Real fractional polynomial moments are obtained only by the displayed
interpolation, never by silently raising a Dirichlet polynomial to a
noninteger power and applying the sieve.

### Theorem C: explicit all-fixed-order envelope

With a,x,d fixed as above, r>=1 and p>=2 integers, define

    G_(r,p)=max(g_r, [m_(pr)+(p-2)b_r+b_(2r)]/p,
                         0, ra(1-d)).                  (16)

Then the COMPLETE original family satisfies

    sum_(Na<=U) |L_a(s)M_(U^a)(s,a)-1|^(2r)
                          << U^(G_(r,p)+epsilon).       (17)

Proof: E_A=(P_X M_A-1)+R_X M_A on the nonprincipal rows. Apply
|u+v|^(2r)<=2^(2r-1)(|u|^(2r)+|v|^(2r)), then (8),(11),(14),(15).
Pay the finitely many principal rows by (12); 2r a(1-sigma)=ra(1-d).
All finitely many preliminary losses are chosen after r,p and the requested
epsilon. This proves (17), with constants depending on these fixed parameters.
No zero was deleted from the final sum. QED.

## 5. Proof of Theorem A: a genuine mixed-character improvement

Set n=6,d=1/2,a=x=3/5,r=1,p=3. The exact exponents are

    m_3=max(1,k_6(9/5)-9/10)=1,
    b_1=k_6(2/5)-3/10=7/10,
    b_2=k_6(4/5)-3/5=1/2,
    g_1=max(k_6(3/5)-3/10,k_6(6/5)-3/5)=11/15.

Thus (15) has exponent (1+7/10+1/2)/3=11/15. The principal residual cost
is at most U^(3/10), which is smaller. Equation (17) proves (2).

In contrast, using the POINTWISE mollifier bound in the same new scales
would cost A^(2-2sigma) times the R2 bound, namely U^(3/10+7/10)=U.
It would not even yield a power-saving residual theorem at those scales.
The improvement is the legitimate mixed norm (15), not a false collapse
of a character times its conjugate into a character of the product ideal.

## 6. Proof of Theorem B: an explicit high-order family near 1/2

Write y=nd in (0,4/5]. For p in (3) one has

    4/[y(2-y)] <= p <= 4/y.                             (18)

To justify the ceiling in the upper bound: for y<=2/3, the difference
4/y-4/[y(2-y)] is at least one (multiply by y(2-y) and use
4-6y+y^2>=0). For 2/3<y<=4/5, the ceiling is exactly five and 4/y>=5.
In particular p>=2 and

    1/(2-y) <= p a <=1,       a=y/4<=1/5.

On 0<=v<=1/2, k_n(v)=1. On 1/2<=v<=1 it equals
1-1/n+2v/n (also for n=3, where two monomials tie). Therefore

    m_p=k_n(pa)-dpa=1-1/n+(2/n-d)pa >=1,
    b_1=1-d/2, b_2=1+1/n-d.

The mixed exponent in (16) is exactly

 [m_p+(p-2)b_1+b_2]/p
       =1+(2/n-d)a-d/2=1-da=1-n d^2/4.                 (19)

The two main endpoints in (14) have the SAME exponent 1-da: the lower
one has a<=1/5, and the upper one has a+1/2<=7/10. Equation (12)'s
principal exponent is a(1-d)<=1/5, far below 1-da. This proves (4).
The parameter inequalities are algebraic over the entire specified interval,
not an extrapolation from the finite rational samples in the checker. QED.

## 7. Relative approximation, not a forbidden deletion of exceptional rows

Theorem A remains valid with sup_(|t|<=T0) on the residual inside the sum,
after arbitrarily small U losses. To see this rigorously, apply (16) at
sigma in a sufficiently small fixed neighborhood of 3/4. All its exponents
are continuous piecewise affine in sigma, so their increase can be made
less than the allotted loss. A finite disc cover of the compact vertical
segment and the submean inequality for the HOLOMORPHIC E_A(s,a) bound its
supremum by a fixed multiple of its area integral on a slightly larger
rectangle. Tonelli and the uniform compact-height estimates then apply.
The rectangle is bounded away from the principal pole at one. This is not
a supremum in height growing with U, or an inverse-L holomorphy argument.

For any fixed 0<tau<2/15, all but

    O(U^(11/15+2tau+epsilon))                           (20)

rows therefore satisfy |E_A(3/4+it,a)|<=U^(-tau) simultaneously for every
|t|<=T0. On these rows L_a is nonzero on that segment, and

    |M_A-1/L_a| / |1/L_a| = |E_A| <= U^(-tau).          (21)

Every excluded member is accounted for by (20), but NOT bounded in inverse
value. Equation (20) is a useful relative approximation statement, not a
claim to beat the sharper zero-density count in #979, which concerns a
different observable and region. In particular we do not promote 11/15
into a best-known zero-density exponent.

## 8. The attempted RH closure and the exact unresolved step

We attempted to remove #984's exceptional-set/cap restrictions by driving
the full residual norm to zero strongly enough to control a prescribed
member. Theorem A improves a genuine signed quantity from U^(7/8+epsilon)
to U^(11/15+epsilon), and Theorem B gives an improved estimate on every
fixed line arbitrarily close to 1/2. But ALL these exponents remain positive.
A single persistent zero contributes one, which is compatible with them.
The relative estimate (21) cannot be asserted for the omitted rows.

Likewise, (17) is a real all-fixed-order residual theorem, but not a
sublinear-excess native moment theorem. At Theorem A's unchanged a,x,p,
its exponents are 11/15 for r=1 and 3r/5 for every integer r>=2. Raising
the residual to higher powers does not force an isolated error of size one
to vanish. No bound with r=r(U) follows from its fixed-r constants.

The prime-versus-continuum critical estimate in #980 and the fixed principal
moment criterion in #983 remain unproved. This packet does not construct a
bounded theta-to-native projection, prove a new zero-free half-plane, or
prove RH. The advance is the explicit mixed norm and its full-family signed
error estimates, not an equivalent RH criterion renamed as a theorem.
