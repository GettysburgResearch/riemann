# NRC32: native resolution and constant-error covariance compression

Status: **proposed component proofs; independent mathematical review required.**
The full native coarse-covariance upper bound and RH are not proved here.
Date: 21 September 2026. Parent: PR #905 at
`98cf588261473724178231c667595fc09cc216fe`.

Two changes are made deliberately. First, estimate the actual native output
on a complete square step, rather than the arbitrary infinite continuation
of a short-source Newton polynomial. A specified endpoint continuation then
has an unconditional sharp high-Mellin bound at frequency O(Y), with a bounded
energy budget. Second, an orthogonal cubic mesh compresses the entire native
square-step energy to fewer than 10(Y+1) block means, with additive error <5/6.
Neither change bounds the remaining coarse signed quadratic forms.

These are applications of elementary variance and translation estimates,
not a new zeta subconvexity theorem or a priority claim. They improve the
native-output resolution budget; they do NOT improve the old global Newton
source projection by silently replacing its continuation.

## 1. Objects and exact finite native reconstruction

For integer Y>=1 put b=Y+1, Lambda=b^2, and N=Lambda-1. Let

    m(k)=sum_(n<=k) mu(n)/n,        F_K=sum_(k=1)^K m(k)^2,
    g(n)=mu(n) for n<=Y, and 0 otherwise,
    z=g*g,                        v=2g-1*g*g.

Here * is Dirichlet convolution and 1(n)=1. The classical Newton identity

    mu-v=mu*(delta-1*g)*(delta-1*g)

shows v(n)=mu(n) for EVERY n< b^2: delta-1*g vanishes below b. This is the
strict square endpoint, not a statement at n=b^2. Consequently, for Y<k<b^2,

    m(k)=2m(Y)-sum_(d<=Y^2) z(d)/d H_floor(k/d).          (1.1)

H_0=0. Products larger than k give zero by this exact formula. No signed
constant, future harmonic tail, or above-endpoint product is discarded from
an infinite representation: (1.1) is a finite coefficient identity.

The source g is UNCOMPLETED. Reciprocal balance is unnecessary for this
finite identity; using g in DMC31's global Mellin formula would be invalid.
No completion energy is being optimized or set to zero. This avoids mixing
the old full-tail object with the new finite native object.

The Newton identity and weighted short-source calculation are classical;
see Huxley--Watt, arXiv:1807.05890, and the existing repository packets.
No future Mobius values are needed to GENERATE (1.1). The full-length Mobius
sieve in the checker is an independent finite comparison, not producer input.

## 2. Native endpoint bound

For every integer k>=1,

    |m(k)|<=1.                                         (2.1)

Indeed sum_(n<=k) mu(n) floor(k/n)=1. Therefore

    |k m(k)| <=1+sum_(n<=k) |mu(n)| {k/n}
              <=1+sum_(n<=k)(1-1/n)=k+1-H_k<=k.

Only literal divisor inversion and |mu(n)|<=1 enter this bound. It is not
the RH-strength bound m(k)=O(k^(-1/2+epsilon)).

## 3. Sharp high-Mellin control for a specified native continuation

Write S_N(x)=sum_(n<=N,n<=x) mu(n)/n for x>0. This is zero below 1 and
constant m(N) above N. Define

    f_Lambda(x)=0,                         x<Lambda,
                  1-Lambda/x,             x>=Lambda,
    m_tilde(x)=S_N(x)-m(N) f_Lambda(x).                 (3.1)

Thus m_tilde agrees with m(floor x) on EVERY cell 1<=x<Lambda and equals
m(N)Lambda/x for x>=Lambda. The endpoint continuation is explicit and
continuous at Lambda. In particular the final cell [N,N+1) is retained.
The complete energy of this continuation is

    integral_0^infinity |m_tilde(x)|^2 dx=F_N+Lambda*m(N)^2. (3.2)

The second term may be large. It is NOT claimed to be a cheap full-energy
completion. It is retained in the following transform and separately paid
only in the HIGH-FREQUENCY estimate.

Set G(u)=exp(u/2)m_tilde(exp u), with Fourier convention
Ghat(t)=integral_R G(u)exp(-itu)du. Then G belongs to L2(R). For
s=1/2+it, D_N(s)=sum_(n<=N)mu(n)n^(-s),

    Ghat(t)=[s D_N(s)-m(N)Lambda^(1-s)]/[s(s-1)].        (3.3)

To prove this, first integrate S_N(x)x^(-s) for Re(s)>1 and integrate the
taper explicitly. The result is D_N(s)/(s-1) minus
m(N)Lambda^(1-s)/[s(s-1)]. The pole at s=1 cancels since D_N(1)=m(N).
The defining integral for m_tilde is analytic for Re(s)>0, so continuation
proves (3.3) on the desired line. No zeta zero or special-function estimate
enters this calculation.

### Theorem 3A: complete infinite high-frequency bound

For every T>=6,

    (1/(2pi)) integral_(|t|>=T) |Ghat(t)|^2 dt
       <=528 Lambda/T^2 +48 H_N/T.                     (3.4)

In particular, at T=6b,

    high energy <=44/3+8H_N/b.                         (3.5)

This bounds the entire infinite frequency tail of the WHOLE signed native
output continuation, not individual denominators or only diagonal terms.
It is an absolute constant asymptotically, not a conjectured source-energy
gain. The constant 6 and the displayed energy constants are not optimized.

#### Proof: retain both the jumps and the endpoint correction

For 0<=v<=1, the change S_N(x)-S_N(x exp(-v)) is a sum of terms mu(n)/n
with x exp(-v)<n<=x. There are at most vx+1 such integers. Cauchy--Schwarz
and integration over each n<=x<n exp(v) give

    integral_0^infinity |S_N(x)-S_N(x exp(-v))|^2 dx
      <= (N v/2)(exp(2v)-1)+H_N(exp(v)-1)
      <= (7/2)N v^2+2H_N v.                            (3.6)

Convexity on [0,1] gives exp(2v)-1<7v and exp(v)-1<2v.
This calculation integrates over the COMPLETE positive half-line, including
x>N; it does not drop a boundary strip.

The taper has the exact translation norm

    integral_0^infinity |f_Lambda(x)-f_Lambda(x exp(-v))|^2 dx
      =2 Lambda(exp(v)-1-v)<=2 Lambda v^2.              (3.7)

For example, split at Lambda and Lambda exp(v). After scaling x/Lambda,
the first integral is exp(v)-exp(-v)-2v and the second is
exp(v)-2+exp(-v). Their sum is 2(exp(v)-1-v).
The bound follows from exp(v)-1-v <= (e-2)v^2 < v^2.

Using |m(N)|<=1, (a-b)^2<=2a^2+2b^2 and N<Lambda yields

    integral |m_tilde(x)-m_tilde(x exp(-v))|^2 dx
      <=11 Lambda v^2+4H_N v.                          (3.8)

For 0<h<=1 use the causal log-average

    (A_h m_tilde)(x)=(1/h) integral_0^h m_tilde(x exp(-v))dv.

Jensen's inequality gives

    ||m_tilde-A_h m_tilde||_(L2(dx))^2
       <=(11/3)Lambda h^2+2H_N h.                     (3.9)

On the logarithmic L2 space, A_h has multiplier

    a_h(t)=[exp((1/2-it)h)-1]/[h(1/2-it)].              (3.10)

For |t|>=6/h, |a_h(t)|<=3/(h|t|)<=1/2, using exp(h/2)+1<3.
Thus |1-a_h(t)|>=1/2 there. Plancherel and (3.9) bound the sharp high
projection by four times its right side. Taking h=6/T proves (3.4).
All integrals and projections are for the declared continuation (3.1).

### Scope and transfer

G includes ALL source terms and the endpoint correction before squaring.
On [b,Lambda), m_tilde is the actual native reciprocal output. Restricting
the inverse low/high projections to this interval is valid, but their
orthogonality need not survive restriction; a triangle inequality would
retain its cross term. Section 4 avoids this loss with a different, explicitly
orthogonal finite-window compression.

DMC31 controls the global Newton function from a short balanced source and
uses zeta subconvexity at a cutoff L^(164/137). Theorem 3A instead controls
the exact native output with the specified endpoint continuation at O(Y).
These are different global objects. There is no implied bound for the old
Pi_low Q, no commuting-projection assertion, and no comparison of their
entire low-frequency energies.

## 4. Orthogonal compression with a complete constant error

Partition the integer output cells b,...,Lambda-1 into consecutive blocks
I=[a,a+h), h>=1. Let

    mbar_I=(1/h)sum_(k=a)^(a+h-1)m(k),
    S_Y=sum_I h*mbar_I^2,
    D_Y=sum_I sum_(k in I)(m(k)-mbar_I)^2.

Orthogonal projection onto block-constant vectors gives exactly

    F_(b^2-1)-F_Y=S_Y+D_Y.                              (4.1)

In particular the mixed term between means and fluctuations is ZERO by
exact algebra. This is not a sign assertion about prime/composite sectors.

For any sequence satisfying |m(k)-m(k-1)|<=1/k, one block obeys

    D_I=(1/h)sum_(0<=i<j<h)(m(a+j)-m(a+i))^2
        <=h(h^2-1)/(12a^2).                            (4.2)

Indeed each difference is at most (j-i)/a, and
sum_(i<j)(j-i)^2=h^2(h^2-1)/12. Define the exact mesh budget

    Z_Y=sum_I h(h^2-1)/(12a^2).                         (4.3)

Then 0<=D_Y<=Z_Y. The whole native sum is formed before this projection, so
all dense arithmetic covariance inside either projected component is kept.

### Theorem 4A: cubic mesh, fewer than 10b means, additive error <5/6

Start at a=b and repeatedly take

    h=min(Lambda-a, floor((a^2/b)^(1/3))),              (4.4)

then advance a by h until a=Lambda. All quantities are integers; floor of
the cube root can be computed by exact comparison. Since a>=b>=2, h>=1.
For this complete partition,

    number of blocks <10b,             Z_Y<5/6,
    S_Y <= F_(b^2-1)-F_Y < S_Y+5/6.                    (4.5)

#### Proof of the complete count and error budget

For every nonfinal block set x=(a^2/b)^(1/3)>=1. Its length satisfies
h=floor x>=x/2 and h<=a. Hence

    integral_a^(a+h) t^(-2/3) dt
       >=h/(a+h)^(2/3)>=1/[2^(5/3)b^(1/3)].

If there are J blocks, at least J-1 have the full nominal length. Summing
and integrating up to b^2 gives

    J<=1+3*2^(5/3)(b-b^(2/3))<10b.                     (4.6)

The last inequality uses 3*2^(5/3)<10 and
1<3*2^(5/3)b^(2/3). It also covers a shortened final block. Every block
satisfies h^3<=a^2/b, so its contribution to Z_Y is at most 1/(12b).
Therefore Z_Y<=J/(12b)<5/6. This proves (4.5) without an asymptotic base gap.

For integer precision R>=1 and b>=R^3, replace b in the cube-root denominator
by R^3 b. The identical proof gives

    J<10Rb,        Z_Y<5/(6R^2).                       (4.7)

For the finitely many b<R^3, unit blocks give zero detail error; no O(Rb)
count is asserted for that separate fallback. Thus any prescribed constant
accuracy is available with O(Y) block means, with an explicit accuracy cost.

This is the reciprocal F energy, not DSE27's physical E energy. DSE27's
nearest-value square-root mesh pays a logarithmic physical error and a
triangle-inequality cross term. The present use of exact means, a cubic
adaptive mesh and reciprocal increments gives a constant additive F error.
The mesh/sample idea itself is credited to that predecessor and standard
orthogonal approximation; no general priority claim is made.

## 5. Every coarse mean is an explicit quadratic form in the OLD prefix

For integer d,t>=1 put

    r=floor((t-1)/d),       A_d(t)=t H_r-d r.           (5.1)

Finite summation gives A_d(t)=sum_(k=0)^(t-1)H_floor(k/d), because each
1/j is counted t-jd times. Thus for every block I=[a,a+h),

    mbar_I=2m(Y)-(1/h)sum_(d<=Y^2) z(d)/d
                         [A_d(a+h)-A_d(a)].            (5.2)

Equivalently expand z(d) as all ordered mu(r)mu(s) with rs=d, r,s<=Y.
All product coincidences and signs are retained. The term -d r in (5.1)
is load-bearing. The exact checker verifies (5.2) separately on small
sources; larger panels reconstruct every Newton coefficient and accumulate
its reciprocal partial sums with directed integer arithmetic.

Consequently S_Y is an explicit sum of fewer than 10b squares of KNOWN
prefix quadratic forms. O(Y) here is the number of means / certificate
coordinates, NOT the arithmetic runtime of their evaluation. The supplied
producer computes a full square-step coefficient array. No O(Y) runtime
or new record-height calculation is claimed.

## 6. What has and has not been proved about the closing gap

The native high-resolution fluctuations cost at most a constant on EVERY
square step, in two precisely specified senses: (3.5) for a sharp Mellin
projection with its endpoint term, and (4.5) for exact block-mean projection.
These are complete component bounds, not extrapolations from a finite plot.

The coarse quadratic-form energy S_Y is NOT bounded in terms of F_Y with
a strictly subquadratic exponent. An estimate of the form

    S_Y <= C (log(2Y))^A (1+F_Y)^(2-delta), delta>0,    (6.1)

on sufficiently large native ladder stages would close the inherited
subpower-energy iteration. We have not proved (6.1), not even with the
particular constants suggested by the finite panels.

Regularity alone cannot do this. For the NONNATIVE arithmetic sequence
alpha(n)=1, its reciprocal sums are H_k. The same compression theorem
applies, but on the square step its energy is at least
(b^2-b)H_b^2, whereas its previous energy is at most Y H_Y^2. The additive
error <5/6 leaves the same power-scale growth in S_Y. For every fixed
delta>0 and A, the analogue of (6.1) fails as Y grows (powers outrun logs).
This is a counterexample to a bounded-output-increment shortcut, NOT to the
literal Mobius source, the Newton inverse identities, or RH.

The missing estimate must therefore exploit signed native inverse structure
INSIDE the retained coarse forms. Neither orthogonal projection, endpoint
regularization, small finite values, nor absolute values of their kernels
supply that estimate. This packet does not present the remaining step as a
routine reviewer task.

## 7. Executed finite results and limitations

The checker reconstructs native coefficients through 1,048,575 from the
prefix through 1,023 and compares every coefficient with a separate sieve.
It encloses the COMPLETE reciprocal energy on ten square steps, not just
sampled points or selected covariance sectors. On the largest step,

    blocks:          2784
    annular F:       [0.203275848900, 0.203275848901]
    coarse S:        [0.200596020299, 0.200596020300]
    detail D:        [0.002679828601, 0.002679828602]
    exact Z budget:  [0.223071773760, 0.223071773761].

Endpoints here are outward 12-place decimal displays of much narrower
integer dyadic enclosures, not floating-point estimates. The low-resolution
part carries almost all observed energy. This supports choosing the coarse
forms as the next object to investigate; it does NOT establish their
unbounded upper bound.

Finite checks of (3.3) at positive integer s and symbolic checks of (3.7)
are algebraic regression tests. They are not numerical evaluations of the
infinite high-Mellin integral and do not independently certify Plancherel
or the analytic estimates. See VALIDATION.md and RECEIPT.json for actual
execution and the preserved predecessor/source boundaries.
