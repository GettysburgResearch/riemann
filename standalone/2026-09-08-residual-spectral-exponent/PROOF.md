# The exact power-growth exponent of the arithmetic residual minima

Date: 2026-09-08. Author continuation of PR #803.
Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required.
**RH and an evaluated subpower arithmetic upper bound are NOT proved.**
Source head: 6c86b5fbfe92c97ecccf17b81585744ccde33b10.
Local labels RG1--RG4 are not canonical acceptance identifiers.

This note supplies an all-scale characterization, rather than extrapolating
four finite minima. The exponent of the complete optimization is exactly the
unknown zero-edge exponent. A particularly simple, unoptimized, two-endpoint
completion already attains that exponent. This does not evaluate it as zero.
The Littlewood/Perron and Nyman--Beurling mechanisms are classical; no claim
of external novelty is made for those mechanisms or this characterization.

## 1. Statement, source, and quantifiers

For an integer Y>=2 let C_Y consist of finite REAL Dirichlet polynomials

    p(s)=sum a_n n^(-s),
    a_n=mu(n) for every integer n<Y,
    p(1)=0,  p'(1)=1.                                    (1)

Every integer tail index is allowed, including nonsquarefree indices. Put

    A_p(x)=sum a_n floor(x/n),
    E(p)=integral_1^infinity |1-A_p(x)|^2 dx/x^2,
    e_2(Y)=min_{p in C_Y, supp(p) subset [1,2Y]} E(p),
    e_inf(Y)=inf_{p in C_Y} E(p).                         (2)

The last infimum is over all FINITE supports, with no fixed upper bound.
It need not be attained. The first is attained uniquely (see Section 2).
No completion is allowed to alter the prefix in (1).

Let

    Theta=sup{Re rho: zeta(rho)=0, 0<Re rho<1},
    alpha=2Theta-1.                                      (3)

Classical zero location and functional symmetry give 1/2<=Theta<=1.
Theta need not be attained, and Theta=1 is explicitly allowed.

Write

    M_Y=sum_{n<Y} mu(n)/n,
    F_Y=sum_{n<Y} (mu(n)/n) log(Y/n),
    b_Y=(F_Y-1)/log 2,  a_Y=-M_Y-b_Y,
    p_Y^sharp(s)=sum_{n<Y}mu(n)n^(-s)
                  +Y a_Y Y^(-s)+2Y b_Y (2Y)^(-s).       (4)

This is a prescribed polynomial, not the result of a solve. It is the
parent's general two-index jet repair specialized to the endpoint-balanced
prefix. Its coefficients need not be bounded as Y grows.

**RG1 (exact all-scale exponent).** All the following limits exist, as Y
runs through EVERY integer >=2, and are equal:

    lim log(1+e_inf(Y))/log Y
     = lim log(1+e_2(Y))/log Y
     = lim log(1+E(p_Y^sharp))/log Y
     = 2Theta-1.                                        (5)

Equivalently, for every epsilon>0 there is a finite C_epsilon such that

    E(p_Y^sharp)<=C_epsilon Y^(2Theta-1+epsilon), all Y>=2. (6)

For any fixed hypothetical zero rho with beta=Re rho>1/2, EVERY p in C_Y
simultaneously satisfies

    E(p)>=(2beta-1)Y^(2beta-1)/|1-rho|^2.                 (7)

Thus the upper side in (6) has the same exponent as the complete family
of lower bounds (7). Constants in (6) depend on a chosen strict distance
from the unknown edge and are NOT numerically certified or uniform as that
distance goes to zero. In particular (6) is NOT a known fixed-power saving
unless such a restriction on Theta has already been established.

The harmless 1+ in (5) treats zero infima and possibly small norms correctly.
There is no claim E itself has a positive limiting constant or converges.

## 2. Exact admissibility, finite norms, and elementary bounds

Since sum mu(n)floor(j/n)=1 for every integer j>=1, any p satisfying (1)
has u_p(x):=1-A_p(x)=0 on 1<=x<Y. Balance gives

    A_p(x)=-sum a_n {x/n},   |u_p(x)|<=1+sum |a_n|.

Hence 0<E(p)<= (1+sum |a_n|)^2/Y. Strictness follows by taking an integer
common multiple Q of the support: A_p=0 and u_p=1 on [Q,Q+1).
For a nonzero finite balanced coefficient variation, the first nonzero
coefficient produces a nonzero floor value on its corresponding unit cell.
Its energy is therefore positive. The finite-dimensional quadratic form is
positive definite on the tangent space. Coercivity on that finite space
and (4) prove existence and uniqueness of e_2(Y).

The two jet identities for (4) follow exactly from

    M_Y+a_Y+b_Y=0,
    -sum_{n<Y}mu(n)log(n)/n-a_Y log Y-b_Y log(2Y)=1.       (8)

For use also in the case Theta=1, we give unconditional bounds requiring
neither PNT nor a zero-free strip:

    |M_Y|<=1, |F_Y-1|<2,
    |b_Y|<4, |a_Y|<5,
    E(p_Y^sharp)<196Y,
    S_Y:=sum |p_Y^sharp[n]|^2/n<60Y.                     (9)

Here is the arithmetic behind the first two bounds. For integer n>=1,

    n sum_{d<=n}mu(d)/d=1+sum_{d<=n}mu(d){n/d}.

The d=1 summand vanishes, and the other n-1 summands have absolute value
at most one, giving |sum_{d<=n}mu(d)/d|<=1. Also finite divisor inversion
of harmonic numbers gives

    sum_{n<=x} (mu(n)/n) H_floor(x/n)=1.

Use H_floor(t)=log t+gamma+epsilon(t), |epsilon(t)|<=1/t for t>=1,
and 0<gamma<1. The inequality for the harmonic remainder follows, for
N=floor t, from

    1/[2(N+1)]<H_N-log N-gamma<1/(2N)

and comparison of log(t/N) with log(1+1/N). It gives |F_x-1|<2.
The term at n=x, if x is an integer, has zero logarithmic weight, so the
strict prefix convention does not change F_Y. This proves (9), using
log 2>1/2, sum_{n<Y}|mu(n)|<=Y-1, and

    sum |p_Y^sharp[n]|<14Y-1,
    S_Y<=H_(Y-1)+25Y+32Y<60Y.

This proof uses the same elementary harmonic identity as the BMC parent;
it is reconstructed here, not replaced by numerical smallness of M_Y.

### 2.1 The exact Hardy norm and the delayed lower bound

For Re s>1, termwise floor integration gives

    integral_1^infinity u_p(x)x^(-s-1)dx=(1-zeta(s)p(s))/s. (10)

Boundedness of u_p continues its integral holomorphically to Re s>0.
The possible pole at 1 on the right is removable because p(1)=0, so
uniqueness continues the identity there. Fourier Plancherel then gives

    E(p)=(1/(2pi)) integral_R
       |1-zeta(1/2+it)p(1/2+it)|^2/(1/4+t^2)dt.          (11)

Indeed r_p(t)=e^(-t/2)u_p(e^t) is L2 and zero before L=log Y.
The shifted function has Hardy transform

    H_p(z)=Y^z [1-zeta(z+1/2)p(z+1/2)]/(z+1/2), Re z>0,
    ||H_p||^2=E(p), H_p(1/2)=0.                          (12)

At z=rho-1/2 with beta>1/2 it has value Y^z/rho. The value kernels of
Hardy space, with boundary norm (1/(2pi))integral |H(it)|^2dt, are
K(z,w)=1/(z+conj w). Orthogonally remove the kernel at 1/2. With
c=beta-1/2, the remaining kernel norm is exactly

    1/(2c)-1/|rho|^2=|rho-1|^2/(2c|rho|^2)>0.

Cauchy--Schwarz for this projected kernel proves (7), including its complex
phase and denominator. No simplicity or zero census enters this proof.
The norm is real even though the kernels are complex. This is the parent's
RN5 argument; it is supplied here to keep the limiting lower bound explicit.

## 3. RG2: inverse-zeta bounds strictly to the right of the unknown edge

Suppose Theta<1. For every fixed sigma with Theta<sigma<1 and every eta>0,

    1/|zeta(u+it)| <= C_(sigma,eta)(2+|t|)^eta,
                                  every u>=sigma.       (13)

At the pole s=1 this denotes the analytic reciprocal, whose value is zero.
This is the classical Littlewood mechanism, but the needed strict-strip
version is proved rather than being treated as an RH-conditional black box.

Choose fixed radii

    0<r0=1/4<r=2-sigma<r1<R<2-Theta.

For large |t| the disk |s-(2+it)|<=R has no zero and no pole. Let g(s) be
the analytic logarithm of zeta there, whose value at the center is fixed
by the absolutely convergent Euler logarithm. That value is uniformly
bounded. Euler summation with truncation floor((|t|+3)^2) gives a polynomial
bound for zeta throughout the disk, hence Re g=log|zeta|<=C log(2+|t|).
For example the identity

    zeta(s)=sum_{n<=N}n^(-s)+N^(1-s)/(s-1)
                          -s integral_N^infinity {x}x^(-s-1)dx

suffices uniformly since the real part of s is bounded away from zero.
Borel--Caratheodory on radii R,r1 gives sup_{|s-(2+it)|<=r1}|g(s)|
<=C'log(2+|t|). On the smaller disk r0 the Euler logarithm converges
absolutely and gives a uniform O(1) bound.

Hadamard's three-circles theorem therefore gives on radius r

    |g(s)|<=C'' [log(2+|t|)]^kappa,
    kappa=log(r/r0)/log(r1/r0)<1.                         (14)

This controls all real parts u in [sigma,2] at the same imaginary height.
Exponentiating +/-Re g proves (13) at large |t|, since log(t)^kappa=o(log t).
The compact remaining part has no reciprocal poles for u>=sigma; u>=2
is handled by the absolutely convergent reciprocal series. This proves (13).
The radii depend on sigma-Theta; no uniformity at sigma=Theta is asserted.

### 3.1 A uniform twisted-prefix estimate on a growing frequency range

**RG2.** For every fixed q with Theta<q<1 and every fixed B>0,

    sup_{|t|<=Y^B} |sum_{n<Y}mu(n)n^(-1/2-it)|
                            <= C_(q,B)Y^(q-1/2), Y>=2.   (15)

It is important that (15) is uniform on the WHOLE growing interval, not
only at each fixed t. Here is a truncated Perron proof paying that point.
Choose Theta<sigma<q and let a=1/2+1/log(2Y), x=Y-1/2, U=Y^(B+4).
The truncated Perron kernel gives, uniformly in the real t,

    sum_{n<Y}mu(n)n^(-1/2-it)
     =(1/(2pi i)) integral_(a-iU)^(a+iU)
       [1/zeta(1/2+it+w)] x^w dw/w
          +O(Y^(1/2)(1+log Y)^2/U).                     (16)

For completeness the kernel's error at y!=1 is
O(y^a min(1,1/(U|log y|))). This follows from the infinite Perron integral
and integration by parts in its two tails; the trivial bound handles
U|log y|<=1. Summing the absolute coefficient errors gives (16): outside
[x/2,2x] use |log(x/n)|>=log 2 and the absolutely convergent exponent
1+1/log(2Y); inside it use |n-x|>=1/2 and sum 1/|n-x|.
Thus no near-integer cutoff or t-dependent error is omitted.

Move the w line to b=sigma-1/2>0. The whole rectangle is reciprocal-zero-free
by the definition of Theta. In particular it crosses neither a zeta zero
nor the Perron pole w=0. On the new vertical side, (13) gives

    integral bound <= C x^b (2+|t|+U)^eta (1+log U).

On each horizontal side the bound is C x^a (2+|t|+U)^eta/U.
For |t|<=Y^B, choose eta>0 so small that
(B+4)eta< (q-sigma)/2, and absorb the logarithm by the other half of the
strict exponent gap. The Perron error and horizontal sides are smaller.
This proves (15). All choices are fixed once q,B,Theta are fixed.
There is no assertion of (15) at q=Theta or with a constant uniform in q.

### 3.2 The corresponding untwisted mean and moment tails

The same proof, using coefficients mu(n), the initial Perron line
1+1/log(2x), and the final line sigma, gives

    M(x):=sum_{n<=x}mu(n)=O_q(x^q),    every q>Theta, q<1. (17)

Half-integer thresholds give all integer partial sums, hence all real x.
One can alternatively use (15) at t=0 and ordinary partial summation.
Choose an exponent q0 strictly between Theta and a desired q<1 in (17).
Partial summation makes sum mu(n)/n and sum mu(n)log(n)/n converge.
Their values are 0 and -1 respectively: their Dirichlet series and its
first derivative converge normally for Re s>q0, equal 1/zeta(s) there by
continuation from Re s>1, and (1/zeta)(1)=0, (1/zeta)'(1)=1.
Consequently

    M_Y=O_q(Y^(q-1)),
    F_Y-1=sum_{n>=Y} mu(n)log(n/Y)/n=O_q(Y^(q-1)).        (18)

The last test vanishes at n=Y. Its partial-summation derivative is bounded
by (1+log(t/Y))/t^2, whose product with O(t^q0) integrates to
O(Y^(q0-1)[1/(1-q0)+1/(1-q0)^2]). The boundary at infinity is zero.
This explicitly retains the infinite moment tails. Differentiating an
uncontrolled pointwise remainder has not been used.
Equations (18) imply a_Y,b_Y=O_q(Y^(q-1)).

## 4. RG3: an upper bound for the COMPLETE positive energy

For every fixed q>Theta, q<1, (15) with B=4 and (18) give

    sup_{|t|<=Y^4}|p_Y^sharp(1/2+it)|<=C_q Y^(q-1/2).     (19)

Both endpoint corrections are bounded separately by a constant times
Y^(q-1/2); no accidental phase cancellation is required here.

The finite classical integral

    Z2=integral_R |zeta(1/2+it)|^2/(1/4+t^2)dt < infinity

is an UNCONDITIONAL fact. Convexity, for instance
|zeta(1/2+it)|^2<=C(1+|t|)^(5/8), proves it. Thus (19) and
|1-zeta p|^2<=2+2|zeta|^2|p|^2 bound the part |t|<=Y^4 in (11) by

    C_q(1+Y^(2q-1)).                                    (20)

The interval in (19) is not the whole frequency line. The rest must be paid.
For every finite p of support <=N and S=sum|p_n|^2/n, direct expansion gives
on every real interval of length U

    integral |p(1/2+it)|^2dt <=[U+4N(1+log N)]S.          (21)

Indeed each unordered pair costs at most 4|p_n p_k|/sqrt(nk)/log(k/n).
For k>n use log(k/n)>=(k-n)/N, then 2|uv|<=|u|^2+|v|^2 and the harmonic
row sum. This proof neither deletes cross terms nor assumes random phases.
Combining (21) and the fixed unconditional 5/8 zeta-square bound, and summing
all dyadic intervals beyond T>=1, gives

    integral_{|t|>T}|1-zeta p|^2/(1/4+t^2)dt
     <= C/T+C S[T^(-3/8)+N(1+log N)T^(-11/8)].           (22)

For (4), the unconditional bounds N=2Y, S<60Y in (9) and T=Y^4 make
(22) O(Y^(-1/2)). The entire tail is bounded, not set to zero and not
replaced by a finite zero census. Constants here are not numerically supplied.
Combining (20)--(22) proves

    E(p_Y^sharp)<=C_q Y^(2q-1) for each Theta<q<1.        (23)

This is the central upper estimate. If Theta=1, use E<196Y from (9) instead.
For every epsilon>0 these two cases prove (6), enlarging constants to cover
small Y. No limiting contour is passed through the unknown boundary.


## 5. Proof of the limit and its limits of interpretation

For each Y, 0<=e_inf(Y)<=e_2(Y)<=E(p_Y^sharp). Section 4 proves the
limsup in each expression (5) is at most alpha. If alpha=0 this and
log(1+E)>=0 finish. If alpha>0, choose ANY zero with beta>1/2 and apply (7)
before taking an infimum. Its constant is independent of the completion,
of its support, and of Y. Therefore

    liminf log(1+e_inf(Y))/log Y >= 2beta-1.

Take the supremum over the actual zeros. This gives alpha, whether or not
there is a rightmost zero and without using a simultaneous zero census.
The squeeze proves (5) for every integer Y tending to infinity. Multiplicity
was not needed for this value-level bound; repeated zeros remain allowed.

**RG4.** A precise power-scale comparison is consequently

    log[(1+E(p_Y^sharp))/(1+e_inf(Y))]/log Y -> 0.          (24)

This does NOT say the explicit candidate is a finite optimizer, gives a
bounded-factor approximation, or minimizes logarithmic losses. The parent's
finite certified improvements remain genuine. Equation (24) says that even
unrestricted finite-support optimization does not change the limiting power
exponent. It cannot be used as a new numerical stopping rule.

The exponent is the unresolved quantity alpha, not a constant now proved
positive. If RH holds it is zero; if RH fails it is positive. A finite norm
certificate is compatible with either possibility. This theorem therefore
characterizes the cost of the approximation problem; it does not establish
the upper bound needed to resolve RH.

## 6. The attempted closure and a cleaner remaining task

The attempt was to use the parent's well-conditioned finite minima to prove
a uniform improving bound. The result shows that the unoptimized endpoint
family already has the best possible POWER exponent, independently of how
far the arithmetic correction support is allowed to extend. The proof of
this fact relies on the strict-zero-free half-plane to the right of Theta;
it supplies no new information that forces Theta=1/2.

The remaining direct task can still be stated without any zero data:
construct an unbounded sequence Y_j with

    log(1+E(p_{Y_j}^sharp))/log Y_j -> 0,

or prove it for the minima, or provide the earlier signed failure-count
saving. No such unconditional subpower estimate is obtained. In particular:

- The bound (13) cannot be applied uniformly on Re s=1/2 without first
  controlling zeros there and to its right.
- Moving the Perron line to that boundary would cross precisely the poles
  of 1/zeta which the proof is supposed to exclude.
- The constants in (14)--(19) cannot be kept fixed while q decreases to Theta.
- The upper envelope alpha and lower envelopes 2beta-1 MATCH; they do not
  contradict each other. Matching exponents is not an RH proof.

The inherited four finite minima are not reinterpreted as all-scale evidence.
The full signed-count problem and native all-window positivity remain open.

## 7. Sources, review scope, and what the computer does not prove

Primary context: Baez-Duarte, arXiv:math/0011254; Burnol,
arXiv:math/0103058v2; Tao, arXiv:0908.4323 for harmonic Mobius bounds;
NIST DLMF 25.2, 25.4, 25.5, 25.9, 25.10 for classical zeta inputs.
Borel--Caratheodory, Hadamard three-circles, truncated Perron, partial
summation and Fourier Plancherel are standard analytic theorems. Their
application and all required domains are supplied above. The only
unconditional zeta growth input not rederived here is the modest convexity
bound used in (20)--(22). No external numerical constant is needed.

The predecessor's exact identities and finite minimizer scope were read at
6c86b5fbfe92c97ecccf17b81585744ccde33b10. This is author continuation,
not independent acceptance of that work. A current PR search was also read;
#819's entropy/floor description is context, not a dependency.
Maier--Rassias arXiv:1806.05070 was inspected at its statement pages while
looking for an applicable Mobius-cotangent power saving. Its theorem has a
different, long numerator versus denominator range; it is NOT imported as
an estimate for this near-diagonal quadratic minimum. No original external
proof replay or novelty assessment is claimed.

The attached checker tests exact finite prefix and jet algebra, direct
floor horizons, bounded rational logarithms, the endpoint coefficient norm,
and explicit exponent budgets. Those controls do NOT prove (13)--(24),
compute Theta, evaluate large-frequency integrals, or certify RH. No new
actual optimized minimum or new native positive range is asserted.
