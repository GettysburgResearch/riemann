# Actual Xi currents: one global saddle for every separated odd order

Status: PROPOSED ANALYTIC THEOREMS; independent exact-source review pending.
Scope: real source frequency xi tending to infinity, arbitrary positive odd
integer K, the literal Xi theta kernel, and scalar current observables.
This extends the changed-order family; it does not choose a new physical
gauge in a fixed-order problem or prove source capture, innerness, or RH.

Dependencies: the full-line theta identity and real positivity at
`3b6972320899a82c6caa3a98e2ada5ff703a605a`; the scalar definitions and
earlier two-scale packet at `af809698fe6cb5046a5bcc00e9175296e4597060`.
Those frozen sources remain unchanged. The earlier bounded-b theorem is
not invoked outside its stated range.

The principal new step is to keep the theta kernel's reflection at the
low argument inside a globally concave phase. This gives a normal limit
without an upper growth restriction on K, and exposes a failure of naive
balanced-kernel centering when the order grows too fast.

## 1. An exact bounded correction to a piecewise concave phase

Let xi>=2, E=exp(xi), and use the full-line even Xi kernel Phi. For t>=0,
the exact first-orbit factorization is

    Phi(t)=4pi^2 exp[(9/2)t-pi exp(2t)] theta_*(exp(2t)),
    theta_*(X)=sum_(n>=1)[n^4-3n^2/(2pi X)]
                                  exp[-pi(n^2-1)X], X>=1.     (1.1)

The following absolute bounds suffice:

    1/2<=theta_*(X)<=32/31,
    |d/du log theta_*(exp u)|<=6             (u>=0).           (1.2)

Indeed the n=1 term is at least 1-3/(2pi)>0 and all terms are positive.
The parent bounds the n>=2 sum by (512/31)exp(-3pi X), at most 1/31
using pi>3 and e>2. For the derivative use y exp(-y)<=2exp(-y/2).
The sum of n^4 exp[-(pi/2)(n^2-1)X], n>=2, is at most 16/15:
its first term is below one, and consecutive terms have ratio below
(3/2)^4 2^(-7)<1/16. Hence |X theta_*'(X)| is at most
1/2+1/62+32/15<3. Dividing by theta_*>=1/2 proves the bound six.
All these are bounds for the entire theta series, not a finite truncation.

On the positive d-axis put

    H_xi(d)=Phi((xi-d)/2) Phi((xi+d)/2),
    F_(K,xi)(d)=K log(xi+d)+(9/2)max(xi,d)
                        -pi[exp(xi+d)+exp(|xi-d|)],
    B_xi(d)=theta_*(exp(|xi-d|)) theta_*(exp(xi+d)).          (1.3)

Evenness of Phi makes the identity

    (xi+d)^K H_xi(d)=16pi^4 exp(F_(K,xi)(d)) B_xi(d)       (1.4)

literal on the entire positive half-line. Both B and its reciprocal are
bounded by absolute constants, and log B is globally Lipschitz in d,
with constant at most 12, independent of xi. In particular B is between
1/4 and 1024/961. Its possible corner at d=xi is harmless;
the product in (1.4), not either factor separately, is the smooth kernel.

Away from d=xi,

    F'(d)=K/(xi+d)-2pi E sinh d                  (d<xi),
    F'(d)=K/(xi+d)+9/2-2pi cosh(xi)exp(d)        (d>xi).    (1.5)

The derivative jumps DOWN at xi by 2pi-9/2>0. Its ordinary second
derivative on either side is

    F''(d)=-J(d),
    J(d)=K/(xi+d)^2+pi[exp(xi+d)+exp(|xi-d|)].              (1.6)

J is continuous and positive, including at the corner. Thus F is strictly
concave, tends to minus infinity at infinity, and has a unique maximum
a=a_(K,xi)>0. This defines the center before numerical fitting.

For an explicit computation define

    K_L=2pi xi(E^2-1),
    K_R=2xi[pi(E^2+1)-9/2],
    K_R-K_L=xi(4pi-9)>0.                                 (1.7)

If K<K_L, a<xi is the unique root of the first equation F'=0. If
K_L<=K<=K_R, a=xi. If K>K_R, a>xi is the unique root of the second
equation F'=0. Set J=J(a), with no ambiguity at a=xi.

The corner interval in (1.7) belongs to the auxiliary phase, not a plateau
of exact Xi modes. Its finite slope jump is invisible on the Gaussian
scale; lower-order carrier corrections still require the literal kernel.

## 2. Uniform all-order normal limit

Retain the exact current probability

    dmu_(K,xi)(d) proportional to
       d[((xi+d)/2)^K-((xi-d)/2)^K] H_xi(d) dd,
    kappa=K/(xi sqrt(pi E)).                              (2.1)

**Theorem GS1.** Let xi->infinity and let K be any sequence of positive
odd integers with kappa->infinity. There is NO upper bound on K in this
theorem. Conditional on d>0, the variable

    v=sqrt(J)(d-a)                                        (2.2)

converges to N(0,1). Its density converges in L1 with every fixed weight
(1+|v|^m)exp(T|v|), m a nonnegative integer and T>=0. The negative half
of the full current law is its exact reflection.

More precisely, put L=a sqrt(J). For fixed m,T, once J and L are
sufficiently large, the weighted L1 error is at most

    C_(m,T)[J^(-1/2)+L^(-1)].                            (2.2a)

The constant and the lower thresholds are independent of K and xi.

The same normal limit holds for either of the positive half-line
probabilities with densities proportional to

    (xi+d)^K[1+/-r(d)^K]H_xi(d),
    r(d)=(xi-d)/(xi+d).                                   (2.3)

In particular, writing I_j^+/- for the integrals of d^j times these
densities, for each fixed integer j>=0,

    I_j^+/-/(a^j I_0^+) ->1.                              (2.4)

Consequently the parent's literal scalar gain and phase satisfy

    E_mu[d^(2j)]/a^(2j)->1       (j>=1 fixed),
    2a g_K/xi->1,
    2xi p_K/a->1.                                        (2.5)

### Proof: center separation and the current factor

Always J>=2pi E. If a<=1, the first equation in (1.5) implies both
kappa<=C a sqrt(E) and J comparable to E. If a>=1, a sqrt(J)>=sqrt(2pi E).
It follows in every case that

    J->infinity,   a sqrt(J)->infinity.                   (2.6)

In a fixed v-neighborhood, d/a->1. Also |r(d)|^K->0 there, uniformly
under these assumptions. To verify the latter without a balanced-region
assumption, use

    -log|(xi-d)/(xi+d)|
       >=2 min(xi,d)/max(xi,d).                          (2.7)

For a<=1, Ka/xi is bounded below by a constant times kappa^2. For
1<=a<=xi it is at least a constant times E. For a>=xi, the second
saddle equation (or the endpoint bounds (1.7)) gives K xi/a->infinity.
The same estimates hold for nearby d since d/a->1. Thus both brackets
in (2.3) tend locally to one, even on the unbalanced side.

### Proof: local quadratic law, including the corner

On either smooth side, |J'(d)|<=2J(d) for xi>=2. Continuity of J gives
the corresponding log-Lipschitz bound across xi. Hence on |d-a|<=1,

    exp(-2)J<=J(d)<=exp(2)J.                             (2.8)

The only extra first-order term in crossing the corner is bounded by
(2pi-9/2)|d-a|. At a corner maximum the two one-sided slopes are also
bounded in absolute value by this same jump. Integration of (1.6) and
(2.8) therefore gives, for each fixed v,

    F(a+v/sqrt(J))-F(a)=-v^2/2+o(1),                    (2.9)

uniformly on bounded v-intervals. For example the error is bounded by
C(|v|+|v|^3)/sqrt(J). The Lipschitz bound for log B in (1.2)--(1.4)
shows B(a+v/sqrt(J))/B(a)->1. This proves the local Gaussian law using
the exact kernel, whether a stays near xi or moves arbitrarily far past it.

### Proof: full tails, not a local saddle substitution

Strict concavity and (2.8) give absolute c,C>0 such that

    F(d)-F(a)<=-cJ(d-a)^2              (|d-a|<=1),
    F(d)-F(a)<=-cJ|d-a|                (|d-a|>=1,d>=0),   (2.10)

after decreasing c in the second line. These follow by using the tangent
at a+1, or at a-1 if the left exterior exists. The one-sided slope at a
has the sign required at a maximum, so no positive linear term is lost.

The exact correction B(d)/B(a) is bounded globally; both current brackets
are between zero and two. After rescaling, an integrable upper bound is
a constant times

    exp(-c v^2)                  (|v|<=sqrt(J)),
    exp(-c sqrt(J)|v|)           (|v|>=sqrt(J)).           (2.11)

For the d^j integrals multiply by (d/a)^j<=(1+|v|)^j once (2.6) holds.
Given a fixed exponential weight exp(T|v|), the second line is bounded
by exp(-(T+1)|v|) for large enough J. Local normalization stays positive
by (2.9). Dominated convergence, including all tails, proves the stated
weighted L1 limits and (2.4). The exact identities

    g_K=(xi/2)I_0^+/I_1^-,
    p_K=(1/(2xi))I_2^+/I_1^-

then prove (2.5). QED.

For completeness, the rate in (2.2a) follows from the same estimates,
without assuming a uniform Taylor expansion on the entire line. On
|d-a|<=1, the phase error is at most C(|v|+|v|^3)/sqrt(J); both phase
exponentials have Gaussian upper bounds. The elementary inequality
|exp(x)-exp(y)|<=|x-y|[exp(x)+exp(y)] gives weighted integral error
O(J^(-1/2)). The bounded Lipschitz correction B contributes the same
order, and the current factor d/a=1+v/L contributes O(L^(-1)).

To control the brackets quantitatively put
R=K min(xi,a)/max(xi,a). On |d-a|<=a/2, (2.7) gives |r(d)|^K<=exp(-R).
The saddle equations imply R>=c min(J,L^2): for a<=1, use
coth(a)<=1+1/a in
J=K/(xi+a)[coth(a)+1/(xi+a)]; for 1<=a<=xi the same identity gives
R>=cJ; for a>=xi use the second equation or (1.7), again obtaining
R>=cJ. The tails |v|>L/2 in (2.11) have weighted integrals bounded by
C exp[-c min(J,L^2)], after adjusting constants for fixed m,T. The
|d-a|>1 tail has the same type of bound. These exponential errors are
absorbed by J^(-1/2)+L^(-1). Finally divide by the Gaussian-sized positive
normalization. This proves the rate also for the two laws in (2.3).

The estimates are sequentially uniform for xi->infinity and kappa->infinity;
in particular their constants do not depend on an upper cap for K. Finite
computational resource caps do not alter these written quantifiers.

## 3. A universal translated-current response

Let C_(K,h)=J_(K,h)/(h L_K)=E_mu[sinhc(hd)], with the continuous value at
h=0. Here J_(K,h) is the literal translated current, not the curvature J.

**Theorem GS2.** Under GS1, uniformly for real |tau|<=T fixed and
h=tau sqrt(J),

    C_(K,h)/sinhc(h a) -> exp(tau^2/2).                  (3.1)

Thus for bounded real h the relative asymptotic is simply
C_(K,h)~sinhc(h a), even when a tends to infinity. The reciprocal scalar
ratio has the reciprocal asymptotic. No absolute-error claim is made when
sinhc(h a) itself grows without bound.

Proof. Normalize the minus density in (2.3) WITHOUT the factor d, and
write its expectation as E_-. Direct cancellation, for h!=0, gives

    C_(K,h)/sinhc(h a)
      =(a I_0^-/I_1^-)
         E_-[cosh(tau v)+coth(tau a sqrt(J))sinh(tau v)]. (3.2)

The prefactor tends to one. GS1 gives E_-cosh(tau v)->exp(tau^2/2)
and E_-sinh(tau v)->0 uniformly on bounded tau-intervals. The apparent
coth singularity is removable uniformly: |coth s-sign(s)|<=1/|s| and

    E_-|sinh(tau v)|<=|tau| E_-[|v|exp(T|v|)].

Its extra contribution is at most C/(a sqrt(J)), which tends to zero.
At tau=0 the ratio is exactly one. This proves (3.1). Bounded h follows
by taking tau=h/sqrt(J)->0, uniformly on bounded h-intervals. QED.

## 4. The global scalar phase diagram

Suppose for fixed b>0 and gamma>1 that

    K~b xi exp(gamma xi),
    r=gamma-1>0.                                        (4.1)

The saddle equation on either side, including its corner interval, gives

    a=r xi+log[b/(pi gamma)]+o(1),
    J/exp(gamma xi)->b/gamma,
    g_K->1/(2r),   p_K->r/2.                            (4.2)

To see the first formula, a is O(xi) and tends to infinity; the leading
term in (1.5) is pi exp(xi+a), while the reflected exponential and 9/2
term are lower order. Taking logarithms gives
a+log(1+a/xi)=log[K/(pi xi E)]+o(1). The other limits follow from
(1.6) and GS1. This also holds at gamma=2 when the limiting constant
shift is zero and the maximizing auxiliary phase has a corner.

The positive scalar carrier rho(eta)=g/eta+(p-g)eta therefore has:

* for 1<gamma<2, one positive zero with
  eta_c->1/sqrt[1-(gamma-1)^2];
* for gamma>2, no positive zero for all sufficiently large xi;
* for gamma=2 and b<2pi, a positive zero for sufficiently large xi;
* for gamma=2 and b>2pi, no positive zero for sufficiently large xi.

For the last two assertions, use the plus law in GS1:
E_+[d^2]-a^2=O(a/sqrt(J)+1/J), whereas
a^2-xi^2~2xi log[b/(2pi)]. At b=2pi this coarse statement does not
decide the sign. The separately frozen actual-kernel carrier theorem
resolves the finer odd-lattice window at

    K=2pi xi exp(2xi)-(7/2)xi-3/2-1/(4xi+2)
                         +O(xi exp(-2xi)).               (4.3)

The error in (4.3) describes a threshold uncertainty, not a definition of
the original polynomial current at noninteger K. None of these scalar
zeros is asserted to select an admissible prescribed physical lambda.

## 5. Why the old balanced saddle cannot be continued blindly

Let a_hat be the unique solution

    K/(xi+a_hat)=2pi E sinh(a_hat),                       (5.1)

even when a_hat>xi. This agrees with the correct phase only on its balanced
branch. Under (4.1) with gamma>2,

    exp(2xi)(a-a_hat)->-1.                               (5.2)

Indeed the derivative of the unbalanced phase at a_hat differs from zero
by 9/2-pi[exp(a_hat-xi)+exp(xi-a_hat)]. Its curvature is asymptotic to
pi exp(xi+a_hat), and the mean-value theorem gives (5.2). The 9/2 term
is negligible after this normalization because gamma>2, and so is the
exp(xi-a_hat) term. Both saddle locations differ by o(1), validating that
curvature comparison.

Consequently the standardized displacement is

    sqrt(J)(a-a_hat)
       ~-sqrt(b/gamma) exp[(gamma/2-2)xi].                (5.3)

At gamma=4 the normal limit centered at a_hat is N(-sqrt(b)/2,1), not
N(0,1). For gamma>4 that incorrectly centered mass escapes to negative
infinity in standardized coordinates. For 2<gamma<4 the centering error
is negligible on the Gaussian scale.

This does not refute the earlier bounded-b saddle theorem: (5.1) was valid
there and these growth rates were expressly excluded. It shows why an
apparently tiny reflected-kernel correction must be retained for an
unrestricted growing-order normal limit.

## 6. Acceptance boundaries

Independent review must verify the exact identity (1.4), downward derivative
jump, full-tail concavity estimate (2.10), the uniform current-bracket bound,
the removable coth singularity in (3.2), and the centering comparison (5.2).
Any numerical saddle scout is a bounded, non-directed falsification tool;
it is not the proof of the uniform all-K quantifiers.

No growing moment-order limit, complex-frequency theorem, full zero census,
inner-factor identification, cofinal physical capture, trace-class conclusion,
or external novelty assertion is made. The saddle method itself is classical.

## 7. Reproduction and non-directed falsification campaign

The new exact producer authenticates four frozen commit/path/blob/LF inputs
before rebuilding all 2,048 rational current controls, ten symbolic phase
identities, two amplitude identities, the complete-series bounding constants,
and thirteen normal-response coefficients. It does not execute ancestral
code, numerically evaluate Xi, or turn those controls into the analytic proof.
The source manifest also identifies the earlier theta evaluator because the
SEPARATE scout authenticates that file byte-for-byte before importing it.

    python -B research/exploratory/xi_global_odd_order_saddle.py --check
    python -B -O research/exploratory/xi_global_odd_order_saddle.py --check
    python -B -m unittest discover -s tests -p test_xi_global_odd_order_saddle.py

The resident `xi_global_odd_order_scout_results.json` records ten declared
parameter cases, always nearest positive odd K to b*xi*exp(gamma*xi), using
50 requested decimal digits and the window -24<=v<=24 intersected with d>=0.
The working precision adds the decimal length of K plus 24 cancellation
guard digits. This is bounded NON_DIRECTED_HIGH_PRECISION: the theta-series
stopping test and quadrature window are not interval certificates. Artifact
hashes bind these numerical records; the exact producer does not rerun them.

Selected falsification controls (b=1):

| xi | gamma | E_mu[v] | E_mu[v^2] | sqrt(J)(a-a_hat) |
|---:|---:|---:|---:|---:|
| 4 | 1.5 | 0.03724 | 0.99742 | 0 |
| 12 | 0.75 | 0.12483 | 0.999998 | 0 |
| 12 | 3 | -1.11e-8 | 1.00000000000000038 | -0.001455 |
| 12 | 4 | -3.34e-11 | 1+3.42e-21 | -0.507880 |
| 12 | 5 | -9.51e-14 | 1+2.8e-26 | -183.043 |
| 20 | 5 | -2.04e-22 | 1 to displayed digits | -9936.69 |

The gamma=0.75 case is deliberately not cosmetically close in mean: kappa
is only moderately separated there. The gamma=4 and gamma=5 comparisons
test the wrong-center prediction rather than just counting accurate digits
in the correct-center computation. The campaign also includes b=2pi at
gamma=2 and xi=8, retaining the literal low-argument kernel.

For each case the scout checks translated-response comparisons at tau=0,
1/4, 3/4 and 1, using formula (3.2) so that sinh(h*a) is never evaluated as
an enormous common factor. A representative replay command is

    python -B research/exploratory/xi_global_odd_order_scout.py --xi 12 --gamma 4 --b 1 --dps 50 --radius 24

Ordinary JSON loading is used for the fixed authenticated fixture. No hostile
unbounded-input parser or directed numerical oracle is claimed. Local code
rejects its declared integer, rational, precision, parameter and window caps;
those finite execution caps do not limit the theorem's all-K quantifier.
