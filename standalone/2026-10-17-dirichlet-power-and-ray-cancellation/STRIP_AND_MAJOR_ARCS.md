# Uniform reciprocals and major arcs for a finite reciprocal product

Status: complete proposed component deduction from the common-strip
hypothesis below. The deep common-strip theorem is an imported input,
not independently proved here. The reciprocal and rational Mobius
major-arc mechanisms are classical; no historical priority is claimed.
The purpose of this note is a complete adapter for fixed finite reciprocal
products, including principal poles and the exact bad-prime coefficients.

## 1. Hypothesis and coefficients

Assume ZF(theta): every primitive Dirichlet L-function has no zero in
Re(s)>theta, for one fixed 1/2<theta<1. The principal pole at s=1 is
permitted. Fix r>=1 and fixed Dirichlet characters xi_1,...,xi_r, retaining
their usual zero values. Set

    a=(mu xi_1)*...*(mu xi_r).

The ordinary Dirichlet series is product_j L(s,xi_j)^(-1). At each prime,

    sum_(e>=0) a(p^e)z^e=product_j(1-xi_j(p)z).

Thus a is multiplicative, a(p^e)=0 for e>r, and
|a(p^e)|<=binom(r,e). Globally |a(n)|<=d_r(n), so for each fixed nu>0
it is O_(r,nu)(n^nu). No one-boundedness is asserted.

## 2. Conductor-uniform reciprocal lemma

For each delta>0 and eta>0,

    |1/L(s,chi)| <<_(theta,delta,eta)
                    [q(3+|Im s|)]^eta,
    Re(s)>=theta+delta,                                  (R)

for EVERY Dirichlet character chi modulo q, with reciprocal values at a
principal pole defined by holomorphic continuation. It suffices to prove
this for 0<delta<(1-theta)/2; larger delta follows from a smaller one.

First take a nonprincipal primitive chi. Its partial sums are bounded by q,
so partial summation gives polynomial growth in q and |s| on each fixed
closed half-plane Re(s)>0. Around 2+it take the disk radii

    R=2-theta-delta/4,
    r_o=2-theta-delta/2,
    r_t=2-theta-delta,
    r_i=1-delta/4.

These satisfy R>r_o>r_t>r_i>0. ZF(theta) supplies an analytic logarithm
throughout the R disk, normalized at its center by the Euler logarithm.
The polynomial bound and Borel--Caratheodory give

    max_(|s-(2+it)|<=r_o) |log L(s,chi)|
           <<_(theta,delta) log(q(3+|t|)).

The Euler logarithm is uniformly bounded on the r_i disk because its real
part exceeds 1+delta/4. Hadamard's three-circles theorem applied to the
analytic function log L therefore yields

    max_(|s-(2+it)|<=r_t) |log L(s,chi)|
         <<_(theta,delta) [log(q(3+|t|))]^lambda,
    lambda=log(r_t/r_i)/log(r_o/r_i)<1.

Exponentiation is bounded by [q(3+|t|)]^eta for every later eta>0, with
one constant independent of q, chi and t. This proves (R) on
theta+delta<=Re(s)<=2. To the right of 2, Euler convergence suffices.

For the principal primitive character use instead

    f(s)=(s-1)zeta(s)/(s+1).

This function is holomorphic and nonzero on Re(s)>theta, including s=1,
and has the same elementary polynomial bound. On Re(s)>1 its logarithm
is the sum of the Euler logarithm and a bounded analytic logarithm of
(s-1)/(s+1) on each of the inner disks. The preceding argument applies
to f. Since

    1/zeta(s)=[(s-1)/(s+1)]/f(s),

and the displayed rational factor has modulus at most one for Re(s)>0,
the principal case follows, including its zero at one. No residue of
1/zeta occurs there.

Finally let chi be induced by a primitive character chi* of conductor f|q.
Then

    L(s,chi)=L(s,chi*) product_(p|q,p not|f)(1-chi*(p)p^(-s)).

Uniformly for Re(s)>=theta+delta,

    product_(p|q)(1-p^(-theta-delta))^(-1) <<_eta q^eta.

To prove this last inequality, choose a fixed large prime cutoff beyond
which each local inverse is at most p^eta; the finitely many smaller
primes contribute a constant. Renaming eta completes (R). Consequently,
for any character psi modulo l,

    D_psi(s)=sum a(n)psi(n)n^(-s)
             =product_j L(s,xi_j psi)^(-1)

is holomorphic in Re(s)>theta and satisfies (R) with q replaced by l.
The fixed xi_j moduli change only constants. Allocate the reciprocal
loss separately to the r factors. This includes every possibility that
one or more xi_j psi is principal.

As a simpler consequence, ordinary truncated Perron on the half-integer
cutoff floor(y)+1/2, shifted to theta+delta with height y^4, gives

    sum_(n<=y) a(n)psi(n) <<_(eta) l^eta y^(theta+eta).   (P)

For completeness, on c=1+1/log(2y) the distant truncation terms are
O(y(log(2y))^r/T), since sum d_r(n)n^(-c)=zeta(c)^r.
Terms near y are O_(nu)(y^(1+nu)log(2y)/T), using the half-integer
distance and d_r(n)<<n^nu. On the new vertical line the integral is
O(l^eta y^(theta+delta)T^eta log(2T)); horizontal edges are
O(l^eta y^c T^(-1+eta)). Choose delta and the initial eta sufficiently
small relative to the final loss. All coefficients and all constants
in this Perron argument are uniform in psi and l.

## 3. Keep the oscillatory phase inside the Mellin integral

For every y>=2, real gamma and Dirichlet character psi modulo l,

    |sum_(n<=y) a(n)psi(n)e(gamma n)|
       <<_(theta,r,xi,eta)
          l^eta y^(theta+eta)(1+y|gamma|)^(1/2+eta).      (W)

This is stronger than taking absolute values in partial summation after
(P). Here is a proof retaining the sharp integer cutoff.

It suffices to treat integer intervals whose endpoints L,U are
half-integers, with U comparable to L and to a scale Y>=2. A dyadic
partition supplies O(log(2y)) such intervals, plus a bounded initial
interval. Write A=Y|gamma| and

    K(s)=integral_L^U v^(s-1)e(gamma v)dv,
    T=Y^4(1+A)^2.

Partial summation applied to truncated Perron on the original line
c=1+1/log(2Y) gives

    sum_(L<n<=U) a(n)psi(n)e(gamma n)
       =(1/(2pi i)) integral_(c-iT)^(c+iT) D_psi(s)K(s)ds
          + O_(nu)(Y^(1+nu)(1+A)(log(2YT))^C/T).         (18)

The kernel identity is exact: the two endpoint Perron kernels and the
phase derivative combine, by integration by parts, to K(s). To justify
the error also at the intermediate real integration points, integrate
the usual truncation majorant. Each n comparable to Y contributes at
most O(Y log(2T)/T), because

    integral_(v comparable Y) min(1,Y/(T|v-n|))dv
                      << Y log(2T)/T.

There are O(Y) such n, each with coefficient O(Y^nu). Distant terms use
zeta(c)^r as in (P). Multiply this integral error by |gamma| and add
the two half-integer endpoint errors to obtain (18). Thus no unproved
uniform error at integer integration points is being assumed.

For sigma in a fixed compact subinterval of (0,infinity), the kernel has
the following truncated weighted L1 estimate, for every eta>0:

    integral_(-T)^T |K(sigma+it)|(3+|t|)^eta dt
       <<_(sigma,eta) Y^sigma[(1+A)^(1/2+eta)+T^eta].    (19)

On |t|<=C(1+A), put v=Y exp(u) and use Plancherel followed by Cauchy.
The compactly supported function of u has uniformly bounded L2 norm:
the oscillation has modulus one. The interval of t has length O(1+A),
giving its square root. Sharp endpoints do not obstruct this L2 step.
For |t|>C(1+A), one integration by parts in the phase
t log(v/Y)+2pi gamma v gives |K(sigma+it)|<<Y^sigma/|t|.
Its phase derivative is bounded away from zero in that range, including
at both endpoints. Integration up to T proves the second term of (19).

Move the finite contour in (18) to sigma=theta+delta. D_psi is
holomorphic there; the pole of a principal L has become a zero of its
reciprocal. On the horizontal edges, the same nonstationary bound gives
O(l^eta Y^c T^(-1+eta)). On the new vertical edge combine (R) and (19).
Since T=Y^4(1+A)^2, first choose delta and all internal small exponents
so that their finite multiples fit within the final eta. The error in
(18) is smaller as well. This proves (W) on the dyadic interval.
Summing intervals proves (W), retaining their full sharp endpoints.

## 4. Rational phases and the exact q-supported cofactor

Let (b,q)=1 and alpha=b/q+gamma. Then

    |sum_(n<=x) a(n)e(alpha n)|
       <<_(theta,r,xi,eta)
          x^(theta+eta)q^(1/2+eta)
                         (1+x|gamma|)^(1/2+eta).        (MA)

For each integer n let d=(n,q^infinity), meaning the full part of n
supported at primes dividing q; put m=n/d. Then (m,q)=1 and (d,m)=1,
so multiplicativity gives a(n)=a(d)a(m) exactly. Only
d|rad(q)^r contribute. This cofactor is NOT merely gcd(n,q).

For a fixed d put g=gcd(d,q) and Q=q/g. The rational phase reduces to
e(b(d/g)m/Q), whose numerator is coprime to Q. Expand this function on
the unit group modulo Q in Dirichlet characters. Parseval gives squared
coefficient sum one, hence coefficient l1 norm at most sqrt(phi(Q))
and therefore sqrt(Q). Lift each character to modulus q, retaining
the condition (m,q)=1 even at primes removed from Q. Its twist of a(m)
has exactly the Dirichlet series D_psi in Section 2.

Apply (W) at length x/d and phase gamma d. Its oscillatory parameter
is at most x|gamma|. Sum the positive cofactor majorants. Since

    sum_(d|rad(q)^r) |a(d)|d^(-theta)/sqrt(gcd(d,q))
       <= product_(p|q)[1+sum_(e=1)^r binom(r,e)
                        p^(-theta e-min(e,v_p(q))/2)]
       <<_(r,theta) 1,

we obtain (MA). The product is bounded uniformly in q: every
nonconstant local term is O_r(p^(-theta-1/2)), and theta+1/2>1.
Dropping the extra factor d^(-eta) only enlarges the bound. The finitely
many very short inner intervals are covered by the same bound with an
adjusted constant. This completes the major-arc adapter without deleting
ramified coefficients, assuming squarefreeness of d, or losing a power
depending on r.

## 5. Primary-source comparison and review limits

The elementary reciprocal argument agrees with He--Huang, Lemma 2,
printed page 4, in their paper dated April 10, 2015:
https://bingronghuang.github.io/expsum2016he.pdf . Its next proof uses
oscillatory Perron to obtain the corresponding square-root phase cost
for its nonlinear setting; no nonlinear theorem is being imported into
the present linear proof.

For r=1 and xi_1 principal, (MA) is the classical Baker--Harman estimate,
also explicitly stated in Wei Zhang, arXiv:2204.04613v2, Lemma 2.2:
https://arxiv.org/html/2204.04613v2 . The latter paper's introduction
records the uniform exponent (1+theta)/2 for theta>=3/5. Its separate
new density argument is not an input here. The fixed-product extension
above is proved directly rather than attributed to that rational-only
statement.

This pass also reviewed the finite inverse identity, Type I/II bounds,
dyadic grouping and cutoff removal in DIRECT_FOURIER.md. Its use of
an OUTER dyadic interval x/2<n<=x makes the product lengths comparable
to x and justifies its grouping. A minor Type I wording correction
concerning multiples of q' in M<m<=2M was sent to the author; it has
no effect on the estimate. No structural flaw was identified in those
steps. Neither this review nor finite arithmetic checks establish the
deep imported common-strip theorem, global novelty, or RH.
