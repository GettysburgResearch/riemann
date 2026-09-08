# Normalization as an oblique projection and certified arithmetic minima

Date: 2026-09-08. Author continuation of PR #803.
Status: proposed complete COMPONENT proofs and four computer-assisted finite
minimum certificates; independent mathematical and code review required.
**The unbounded residual upper bound, sparse-sign bound, and RH are not proved.**

Source: positive-residual-review/PROOF.md at
`f7d786b2f827fd89e55947d1f2140c0ea6b1d9f8`, blob
`9d49700e4378b2d5d0f1ebfe41861ac1dd01bd6e`.
Local labels RN1--RN5 are not canonical claim IDs. No external priority claim.

The attempted finish was to make the genuinely positive residual norm small
by solving its constrained arithmetic minimization. This pass supplies a
uniform normalization operator, polynomial conditioning in the actual integer
coefficient coordinates, and a completely enclosed primal/dual calculation.
None of these is an estimate of the constrained minimum at unbounded Y.

## 1. The unchanged problem

Let Y>=2 and N>=Y be integers. A real finite Dirichlet polynomial

    p(s)=sum_(n<=N) a_n n^(-s)

is admissible when a_n=mu(n) for n<Y and p(1)=0. Here mu is the ordinary
Mobius function. All correction indices, including nonsquarefree ones, are
allowed. Put

    A_p(x)=sum_n a_n floor(x/n),
    u_p(x)=1-A_p(x),
    E(p)=integral_1^infinity |u_p(x)|^2 dx/x^2.             (1)

Mobius inversion gives u_p=0 on [1,Y). Balance gives
A_p=-sum a_n {x/n}, so u_p is bounded and E is finite. The norm is strictly
positive for every finite p: at an integer common multiple Q of its support,
A_p=0 throughout [Q,Q+1), and u_p=1 there. Endpoint values do not affect (1).

For Re s>1 termwise integration gives

    integral_1^infinity u_p(x)x^(-s-1)dx
                      =(1-zeta(s)p(s))/s.                (2)

Boundedness extends the left side holomorphically to Re s>0. The possible
pole at 1 on the right is removed by p(1)=0, so analytic continuation proves
(2) throughout that half-plane. In particular, writing d=p'(1),

    integral_Y^infinity u_p(x) dx/x^2 = 1-d.              (3)

With r(t)=exp(-t/2)u_p(exp t), the same formula and Fourier Plancherel give

    E(p)=(1/(2pi)) integral_R
        |1-zeta(1/2+it)p(1/2+it)|^2/(1/4+t^2)dt.          (4)

The positive norm (4) is NOT the signed p(s)^2 contour functional from the
annular construction. Classical Nyman--Beurling approximation supplies the
context; neither density nor an RH-equivalent upper estimate is imported.

## 2. RN1: impose the derivative normalization at uniformly bounded cost

Define the binary step function

    b_Y(x)=floor(x/Y)-2floor(x/(2Y)).

For x>=0 it takes only the values 0 and 1, and it vanishes below Y.
Alternating harmonic sums, or integration of its unit cells, give

    integral_Y^infinity b_Y(x) dx/x^2 = (log 2)/Y,
    integral_Y^infinity b_Y(x)^2 dx/x^2 = (log 2)/Y.        (5)

For example after x=Yt, the first integral is Y^-1 times
sum_(j>=0)[1/(2j+1)-1/(2j+2)]=(log 2)/Y. Thus no unknown constant enters.

Given an admissible p, put

    c=Y(1-p'(1))/log 2,
    p_tilde(s)=p(s)+c Y^(-s)-2c(2Y)^(-s).                (6)

Then p_tilde retains the exact prefix, p_tilde(1)=0 and p_tilde'(1)=1.
Its support is at most max(N,2Y), even when the new coefficients overlap
old ones. Its error is u_p-c b_Y.

**RN1.** For every admissible p,

    E(p_tilde) <= E(p)/(log 2).                          (7)

This is not obtained by estimating the two errors separately with a triangle
inequality. Work in H_Y=L2([Y,infinity),dx/x^2). Let ell(u)=integral u dx/x^2
and define

    P_Y u = u - [Y ell(u)/log 2] b_Y.                   (8)

Its range is ker ell; it is a bounded idempotent projection. Set
s=sqrt(Y)*1 and h=sqrt(Y/log 2)*b_Y, so ||s||=||h||=1 and
<s,h>=sqrt(log 2)=:c0. In the orthonormal plane with basis s and
(h-c0 s)/sqrt(1-c0^2), its matrix is

    [[0,0],[-sqrt(1-c0^2)/c0,1]].

On the orthogonal complement it is the identity. Consequently

    ||P_Y||^2=1/c0^2=1/log 2.                           (9)

Equations (3), (6), and (8) prove (7), for real or complex errors. The operator
constant is sharp on H_Y: u=1-b_Y gives equality. This extremizing function
is NOT asserted to be the error of a finite native-prefix polynomial.
Therefore (9) is not a sharpness assertion within that smaller arithmetic class.

There is also a useful coefficient-cost bound. Cauchy--Schwarz in (3) gives

    Y |1-p'(1)|^2 <= E(p).

If v=p_tilde-p, its two coefficients satisfy exactly

    sum_n |v_n|^2/n = 3Y|1-p'(1)|^2/(log 2)^2
                    <= 3E(p)/(log 2)^2.                (10)

Thus S(p_tilde)^(1/2) <= S(p)^(1/2)+sqrt(3E(p))/log 2,
where S(p)=sum |a_n|^2/n. Overlapping old coefficients do not invalidate the
triangle inequality in this weighted coefficient space.

### What this does and does not finish

Existence of an unbounded prefix sequence with subpower E is equivalent with
or without the extra condition p'(1)=1: apply (6)-(7) in one direction and
use the subclass in the other. Support increases only to max(N,2Y).
This is compatibility of TWO still-unproved construction tasks, not a proof
that either task is achievable. A fixed linear support bound is preserved
only when it was already available.

Repeating (8) cannot progressively lower E: P_Y^2=P_Y. In particular its
norm is greater than one, not a contraction. Its orthogonal counterpart
u -> u-Y ell(u)*1 would reduce the norm, but that constant step is not proved
realizable by a finite balanced arithmetic correction. Substituting it for
b_Y would drop precisely the arithmetic realization requirement.

The parent's two small jet-normalized examples arise from (6): start with
1-2*2^(-s) at Y=2, or 1-2^(-s)-3^(-s)-(2/3)4^(-s) at Y=4. No new inference
of a cofinal bound is obtained from explaining those examples.

## 3. RN2: the exact source-coordinate Gram has a polynomial lower bound

For integer n>=2 define

    f_n(x)={floor(x)/n}, x>=1,
    G_mn=integral_1^infinity f_m(x) f_n(x) dx/x^2.

These are fractional parts of floor(x)/n, NOT the unweighted functions
{x/n} on a finite period. For balanced p, on each integer cell,

    A_p(x)=-sum_(n>=2) a_n f_n(x).

Moreover integral f_n(x) dx/x^2=(log n)/n. One derivation applies (2) to
the balanced two-term polynomial n^(-s)-1/n, taking the removable value at
s=1. It can equally be obtained from the convergent floor integrals.
Consequently

    E(p)=1+2sum_(n>=2) a_n log(n)/n + sum_(m,n>=2)a_m G_mn a_n.
                                                               (11)

For p'(1)=1 this simplifies to E(p)=-1+a^T G a.
The constant -1 is essential. A positive Gram alone does not pay it.

Let v be any coefficient variation supported on the integers [Y,N], satisfying
sum v_n/n=0, so the prefix and balance are preserved. Allow complex v, and put
F_j=sum_n v_n floor(j/n), with F_0=0. For b_j=F_j-F_(j-1),

    b_j=sum_(n|j) v_n,
    v_j=sum_(k|j) mu(k)b_(j/k).                           (12)

Both b and v vanish below Y. In (12), j<=N implies k<=H:=floor(N/Y).
On l2({1,...,N}), the map b_j -> b_(j/k) 1_(k|j) has norm at most one.
Triangle inequality and the norm of the first-difference operator give

    ||v||_2 <= H ||b||_2 <= 2H ||F||_2.

The full nonnegative norm dominates its first N cells, so

    integral_1^infinity |A_v(x)|^2 dx/x^2
      >= sum_(j=1)^N |F_j|^2/[j(j+1)]
      >= ||F||_2^2/[N(N+1)].

**RN2.** Combining these inequalities proves, at EVERY Y,N,

    v^*Gv >= ||v||_2^2/[4 floor(N/Y)^2 N(N+1)].           (13)

This also holds on the smaller tangent space preserving p'(1)=1. It is a
lower bound for the quadratic coefficient matrix G; the literal Hessian is
2G. Its upper bound on that subspace is (N-Y+1)I, since 0<=f_n<1 and
integral_1^infinity x^-2 dx=1. In orthonormal tangent coordinates the condition
number is therefore at most

    4 floor(N/Y)^2 N(N+1)(N-Y+1).                         (14)

For N=2Y this is polynomial, O(Y^3). This is about the finite INTEGER-
coefficient residual problem. It does not strengthen or contradict another
branch's conditioning bound in a different all-pass or smooth source basis.
A poorly chosen nonorthogonal parameterization can itself have extra condition
losses not covered by (14).

For a fixed nonempty affine coefficient class, coercivity proves existence
and uniqueness of its minimizer. Neither (13) nor (14) bounds the distance of
the affine target from the span. They do not give E_min(Y,N)=Y^o(1).

## 4. RN3: no single huge common period is needed

For each PAIR m,n put q=lcm(m,n)<=mn. The product f_m f_n is q-periodic.
Nonnegative summation over its integer cells gives exactly

    G_mn=sum_(r=1)^q [(r mod m)/m][(r mod n)/n] omega(q,r),
    omega(q,r)=sum_(k>=0) 1/[(r+kq)(r+1+kq)].             (15)

The r=q summand vanishes but may be retained. Every infinite weight remains
in (15). Constructing all entries through N uses at most O(N^4) finite cell
terms by the simple estimate sum_(m,n<=N) lcm(m,n)<=N^4. This is an arithmetic
operation-count statement for fixed primitive accuracy, not a near-linear
algorithm or a bit-complexity claim for arbitrary precision.

In contrast, directly enumerating the period of the complete residual could
require lcm(1,...,N) cells. At N=32 that number is 144403552893600; the largest
pair period in (15) is only 992. There are still infinitely many periods in
each omega. Their complete remainder is enclosed as follows.

### Explicit Euler--Maclaurin weight enclosure

Fix K=32 and p=8. Put a=r+Kq. Separate the terms 0<=k<K. With
f(t)=1/(r+qt)-1/(r+1+qt), Euler--Maclaurin gives the tail approximation

    W = (1/q)log(1+1/a)+1/[2a(a+1)]
       +sum_(j=1)^p B_(2j)/(2j) q^(2j-1)
                         [a^(-2j)-(a+1)^(-2j)].          (16)

The complete error is at most

    R=|B_(2p)|/(2p) q^(2p-1)
                         [a^(-2p)-(a+1)^(-2p)].          (17)

Indeed the standard remainder after including the B_(2p) term is an integral
of the periodic Bernoulli function against f^(2p). The Fourier series of
that Bernoulli function bounds its modulus by |B_(2p)|; f^(2p)>=0 and its
integral is -f^(2p-1)(K), yielding (17). All derivatives are integrable and
vanish at infinity. Equivalently one can derive this from DLMF 2.10.1 by
separating its constant B_(2p) from the periodic part. No asymptotic sign is
assumed in the checker: both W-R and W+R are used.

The used Bernoulli values B2 through B16 are

    1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6,-3617/510.

The logarithm is independently enclosed by

    log((1+z)/(1-z))=2sum_(j=0)^(T-1) z^(2j+1)/(2j+1)+R_T,
    0<=R_T<=2z^(2T+1)/[(2T+1)(1-z^2)], 0<=z<1.            (18)

For log(1+1/a), z=1/(2a+1), T=20. Other integer logarithms use binary range
reduction, z<=1/3, and T=100. Integer rounding is outward at 192 bits after
every primitive operation. Formulae (16)-(18), not digamma evaluations or
numerical quadrature, are the acceptance inputs.

The standard Euler--Maclaurin and Bernoulli Fourier facts are credited to
DLMF 2.10 and 24.8. Ehm's work on Nyman--Beurling Gram matrices is relevant
prior art; this note does not assert novelty for fractional-part Grams.

## 5. RN4: certify the minimum, not just a candidate value

Fix N=2Y and retain all coefficients mu(n) for n<Y. On the tail indices
Y,...,N impose the TWO linear constraints for p(1)=0 and p'(1)=1. Their rows
are

    C_0n=1/n, C_1n=log(n)/n.

They are linearly independent. Values at Y+1,...,N-1 in candidates.json are
exact rational numbers. The two remaining coefficients are defined EXACTLY
from those and the prefix. With sums over n other than Y,N, including n=1,
put

    s0=sum a_n/n, s1=sum a_n log(n)/n,
    y=(-1-s1+s0 log Y)/log 2, x=-s0-y,
    a_Y=Yx, a_N=Ny.                                      (19)

This proves feasibility algebraically. Merely observing that an interval
contains zero would not prove the constraints; the checker additionally
checks those interval identities as bounded controls.

Let E_p be the candidate's full norm, and choose ANY real two-component dual
vector lambda. Let

    r=(G a)_tail-C^T lambda,
    lambda0=1/[4 floor(N/Y)^2 N(N+1)].

For any feasible variation v, C v=0, and (11),(13) give

    E(p+v)>=E_p+2 Re(r^*v)+lambda0||v||^2
           >=E_p-||r||^2/lambda0.

Thus if E_p in [L,U] and ||r||^2<=R are certified,

    L-R/lambda0 <= E_min(Y,N) <= U.                       (20)

The upper side is furnished by an actually admissible polynomial. The lower
side covers EVERY real polynomial in the declared finite support/prefix/jet
class. It is not a bound for arbitrary longer completions.

Floating SciPy calculations proposed coefficients and dual variables. They
were rounded to rational numbers with denominator dividing 2^40. Their
floating objective, solver status, and floating Grams are not used by the
accepting producer. Equations (15)-(20) reconstruct the full interval proof.

The completed certificates give these outward decimal enclosures:

    (Y,N)=(2,4):   0.072123117281951 <= E_min <= 0.072123117281952;
    (Y,N)=(4,8):   0.026111243144081 <= E_min <= 0.026111243144082;
    (Y,N)=(8,16):  0.023695806559291 <= E_min <= 0.023695806559292;
    (Y,N)=(16,32): 0.022118909935520 <= E_min <= 0.022118909935521.

Exact dyadic endpoints and squared stationarity upper bounds are in result.json.
These four cases include every integer correction index through N. They
improve the two specified, unoptimized parent examples at the SAME Y,N, but
are not an annular-positivity extension or a new zero-free region. The four
classes are not a nested sequence with fixed prefix: Y also changes.
Neither the numerical decrease nor apparent leveling is an all-Y theorem.

## 6. RN5: the normalization changes the exact zero-forced lower bound

This section attempts to use (7) and (20) to close the proof, by exposing the
remaining cost. Suppose rho=beta+i gamma is a hypothetical nontrivial zero
with beta>1/2. Write z=rho-1/2 and alpha=Re z>0. Formula (2), shifted by the
exact delay L=log Y, defines an H2 function

    H_p(w)=Y^w [1-zeta(w+1/2)p(w+1/2)]/(w+1/2),
    ||H_p||^2=E(p).

Its known values are

    H_p(z)=Y^z/rho, H_p(1/2)=sqrt(Y)(1-d), d=p'(1).

The two evaluation kernels have Gram entries

    K(1/2,1/2)=1, K(z,z)=1/(2alpha),
    |K(z,1/2)|^2=1/|rho|^2.

Projecting first on the safe kernel and then on its orthogonal complement
therefore gives

    E(p)>=Y|1-d|^2
       +(2beta-1)|Y^(rho-1/2)-sqrt(Y)(1-d)|^2/|rho-1|^2.   (21)

For clarity, the complementary kernel norm squared is
1/(2alpha)-1/|rho|^2=|rho-1|^2/(2alpha|rho|^2)>0; this accounts for every
factor and complex phase in (21). No zero simplicity is assumed: a value
constraint alone suffices. This is the elementary two-point Hardy Gram
calculation, not an arithmetic realization of its abstract minimizer.

After RN1 normalization, (21) strengthens the parent bound to

    E(p)>=(2beta-1)Y^(2beta-1)/|1-rho|^2.                 (22)

Therefore a sequence of actual finite completions at Y_j -> infinity with
E(p_j)=Y_j^o(1) would contradict every right-of-line zero; reflection would
prove RH. By RN1, requiring the extra derivative normalization does not
change that existence question. NO SUCH SEQUENCE OR UPPER BOUND IS PROVED.

## 7. The attempted finish and the precise unresolved statement

The finite optimization is now well-conditioned in the specified coefficient
metric, computable without a global least-common-multiple period, and equipped
with a dual lower certificate. The positive-residual and signed-contour
normalizations are compatible at a fixed factor <=1/log 2. These complete
component tasks do not determine the global residual cost.

In particular, no argument above proves

    E_min(Y,2Y)=Y^o(1),

or the weaker existence of subpower minima on a single unbounded sequence
allowing larger finite supports. A bound on a Gram inverse controls sensitivity
of a finite minimizer, NOT its distance from an affine target. In (11), the
positive quadratic still has the nontrivial intercept -1 after normalization.
Replacing an explicit feasible candidate by the word 'minimum' does not
estimate that minimum.

The old 625Y candidate upper bound and the new four finite upper certificates
cannot contradict (22), whose exponent may be any number strictly between
zero and one. The oblique projection is idempotent, so repeated normalization
cannot create decay. No extrapolation from the four norms is used.

No complete RH proof is submitted. The original sparse-sign and low-frequency
count statements are also not established here. Reviewers can check these
components without being asked to supply the missing arithmetic theorem.
