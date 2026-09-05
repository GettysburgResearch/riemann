# A sharp radial-integrability classification and a boundary-compatible norm

Status: PROPOSED complete analytic proofs; independent review required.
Scope: the actual meromorphic xi logarithmic derivative and the parent's
prime-only continuation. No RH proof or prime cancellation bound is claimed.
Local labels BR-1 and BR-2 are confined to this directory.
Dependencies and source conventions are those in PROOF.md and SOURCE_LOCK.json.

## 1. The distinction that an attempted Hardy proof must retain

Let

    s(w)=(2-w)/(1+w),
    D(w)=d_0/2+(3/8)(xi'/xi)(s(w)),
    R(w)=sum_(n>=1) r_n w^n,       R in H^2,
    P(w)=(8/3)[R(w)-D(w)+d_0].                              (1)

Near zero the nonconstant Taylor coefficients of P are exactly the
prime-only Pcal_n. Formula (1) defines P meromorphically on the full disk.
It does not assert that its original Taylor series converges there.

For p>0 define the extended radial integral

    M_p(f,r)=(1/(2pi))integral_(-pi)^pi |f(r exp(i theta))|^p dtheta.

At a finite pole on a circle, use the Lebesgue integral with its possible
value infinity. An isolated point of infinite value need not make this
integral infinite when p<1. This is an integral of MEROMORPHIC values,
not an H^p norm unless f is already holomorphic on the whole disk.

**BR-1 (complete radial threshold).** For f=D and also for f=P,

    sup_(0<r<1) M_p(f,r) < infinity       for every 0<p<1,
    sup_(0<r<1) M_p(f,r) = infinity       for every p>=1.       (2)

Both assertions are unconditional. Thus no choice of exponent in this
unqualified radial-integrability test discriminates RH from a possible
interior-pole configuration. The finite p<1 bound is a genuine global
estimate for the actual source, but not the required Taylor-coefficient
bound.

## 2. Exact Cauchy-pole representation

Index nontrivial zeta zeros rho=beta+i gamma with gamma>0, retaining each
multiplicity. Put

    b=9/4,
    k_rho=b/[(2-rho)(1+rho)],
    lambda_rho=(1+rho)/(2-rho).

The centered genus-zero product, or the parent's Chebyshev identity, gives

    D(w)=(1/2)sum_(gamma>0) k_rho
              [1/(1-lambda_rho w)+1/(1-lambda_rho^-1 w)].    (3)

For an off-line quartet, the upper-half-plane list contributes its two
upper zeros. For a line pair, it contributes one. Equation (3) introduces
neither an extra factor two nor a simplicity assumption.

For completeness, the invariant zero parameter of G(q)=xi(1/2+sqrt q)
is a_rho=-(rho-1/2)^2. The logarithmic-derivative moments are
sum k_rho^(n+1), and the Chebyshev argument is

    (lambda_rho+lambda_rho^-1)/2=2k_rho-1.

Summing the Chebyshev generating function proves (3) near zero. Since
0<beta<1,

    |k_rho| <= (9/4)/(gamma^2+2).                            (4)

The classical count N(T)=O(T log T) implies

    A_p:=sum_(gamma>0)|k_rho|^p<infinity,           p>1/2.    (5)

In the infinite tail lambda_rho and its reciprocal tend to -1. On every
compact subset of the disk avoiding the finitely many relevant poles,
the denominators in the tail are uniformly bounded away from zero.
Thus (3) converges normally there and equals the meromorphic continuation.
There is no assumption that all its poles lie on the boundary.

## 3. Proof of finite radial integrals below exponent one

For 0<p<1, the elementary uniform Cauchy estimate is

    sup_(a>=0) (1/(2pi))integral_(-pi)^pi
                      |1-a exp(i theta)|^-p dtheta
       <= B_p:=2^p+1/(1-p).                                 (6)

If a<=1/2, the denominator is at least 1/2. If a>=1/2, then

    |1-a exp(i theta)|^2=(1-a)^2+4a sin^2(theta/2)
                       >=2 theta^2/pi^2,

using sin(|theta|/2)>=|theta|/pi on the interval. Direct integration of
|theta|^-p proves (6), including the case a=1. A rotation handles complex
a in a Cauchy denominator.

For 1/2<p<1 apply |sum z_j|^p<=sum |z_j|^p to finite sums in (3), then
Fatou to their pointwise limit. Equations (5)--(6) give the explicit bound

    sup_r M_p(D,r) <= 2^(1-p) B_p A_p.                       (7)

The H^2 remainder satisfies sup_r M_p(R,r)<=||r||_2^p. Thus

    sup_r M_p(P,r)
      <=(8/3)^p [2^(1-p) B_p A_p+|d_0|^p+||r||_2^p].        (8)

For 0<p<=1/2 choose any q in (1/2,1) with p<q and use the normalized
finite-measure inequality M_p^(1/p)<=M_q^(1/q). This proves the first
half of (2) for the entire stated range. Neither (7) nor (8) assumes RH.

## 4. Proof of divergence at and above exponent one

Use one existing critical-line zero rho_0=1/2+i gamma_0, of any
multiplicity m>=1. Existence is the classical Hardy theorem. Let

    w_0=(2-rho_0)/(1+rho_0),       |w_0|=1.

The expression for D extends meromorphically across a neighborhood of
w_0, since w_0!=-1. It has a nonzero simple pole with residue

    Res_(w_0) D=-m(1+w_0)^2/8=-9m/[8(1+rho_0)^2].            (9)

The other local part is holomorphic and bounded in a smaller neighborhood.
Integrating the absolute value on a fixed small arc about arg w_0 gives
M_1(D,r) tending to infinity at least logarithmically as r increases to
one along circles where it is otherwise finite. Any intervening interior
poles only make some integrals infinite, not smaller.

Since R has uniformly bounded radial L^1 norms, the triangle inequality
in (1) transfers this divergence to P. Monotonicity of normalized L^p
norms transfers it from p=1 to every p>1. This proves the second half of
(2). The logarithmic derivative has simple poles even at multiple zeros;
only its residue is multiplied by m.

A basic exact counterexample to the attempted inference is f(w)=1/(a-w),
0<a<1. Equation (6) proves bounded radial p-means for every p<1, while
its Taylor coefficients are a^(-n-1), with exponential growth. It is
incorrect to apply Cauchy's coefficient estimate on circles enclosing its
pole as though the meromorphic continuation were the Taylor series.

## 5. BR-2: a weighted area norm has the correct boundary distinction

Define the positive extended integral

    B(D)=(1/pi) integral_(|w|<1) (1-|w|^2)|D(w)|^2 dA(w).    (10)

The weight is positive at every interior point and vanishes at the boundary.

**BR-2.** For the actual source,

    B(D)<infinity <=> RH,
    RH ==> B(D)<=d_0^2.                                    (11)

The analogous finiteness assertion for P is equivalent, since the remainder
in (1) is in H^2 and hence in this weighted area space. Finiteness of either
norm is NOT established unconditionally here.

Proof. Under RH, the positive spectral representation in PE-3 gives
|d_n|<=d_0 for all n>=0. Angular Parseval and radial integration give

    B(D)=sum_(n>=0)|d_n|^2/[(n+1)(n+2)]<=d_0^2,             (12)

because the weights telescope to one. This proof includes all boundary
zeros and their multiplicities without requiring uniform separation.

Conversely, a zero rho with beta>1/2 produces a simple nonremovable pole
at a=(2-rho)/(1+rho) inside the disk. The positive weight in (10) cannot
make |w-a|^-2 locally integrable in two dimensions. Thus B(D)=infinity.
Reflection guarantees a zero with beta>1/2 whenever RH fails.
This proves (11), without assuming holomorphy in the condition (10).

The one-boundary-pole model 1/(1-w) has B-norm squared exactly one. It
therefore passes the weighted norm even though it is not in H^2. The
interior-pole model 1/(a-w), 0<a<1, has infinite B-norm. These controls
show why (10), unlike (2), has the right local singularity discrimination.

### Exact local horizontal-defect coefficient

For any hypothetical rho=beta+i gamma with delta=beta-1/2>0 and
multiplicity m, take a sufficiently small fixed radius r_0 about
w_rho=(2-rho)/(1+rho), containing no other pole and lying inside the disk.
Then

    lim_(eta->0) 1/log(1/eta) * (1/pi)
       integral_(eta<|w-w_rho|<r_0) (1-|w|^2)|D(w)|^2 dA(w)
       =2(1-|w_rho|^2)|Res_(w_rho)D|^2
       =(243/16) m^2 delta / |1+rho|^6 >0.                 (13)

Subtracting the polar part leaves a bounded analytic function locally.
Its square and the cross term are locally integrable; the variation of the
weight changes only integrable terms. The leading annular integral is
2(1-|w_rho|^2)|Res D|^2 log(r_0/eta). Finally use (9) and
1-|w_rho|^2=6delta/|1+rho|^2. Equation (13) is a LOCAL identity, not a
claimed globally summable renormalization over all unknown zeros.

In the s-plane, (10) is exactly

    (54/pi) integral_(sigma>1/2)
      (sigma-1/2)/|s+1|^6 * |d_0/2+(3/8)(xi'/xi)(s)|^2 d sigma d t.
                                                               (14)

Here |dw/ds|^2=9/|s+1|^4 and 1-|w|^2=6(sigma-1/2)/|s+1|^2.
The same region and normalization must be retained in any arithmetic proof
of finiteness; evaluating only on a zero-free safe half-plane does not
bound (14).

## 6. Disposition of the boundary-norm attempt

The intended argument was to weaken the false H^2 target enough to permit
critical-line poles, then deduce subexponential coefficients. Below exponent
one the required radial estimates ARE proved by (7)--(8), but the deduction
fails without holomorphy. At exponent at least one the uniform radial bound
is itself false. The weighted area norm avoids both errors, at the cost of
retaining the unresolved arithmetic finiteness condition in (11).

The exact source-specific energy in PROOF.md is the independent remaining
attack. Neither the new prime diagonal nor the unconditional fractional
radial bounds prove that energy estimate. The result remains a partial
research contribution rather than an RH closure.
