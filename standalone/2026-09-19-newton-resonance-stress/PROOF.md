# NSR26: native regrouping and an unbounded ternary resonance obstruction

**Proposed component mathematics; independent review required. No native
unbounded energy gain or RH proof is supplied.** Date: 19 September 2026.
This is an execution of #902 on the #848 Newton route, not a change to the
accepted mathematical baseline. Classical convolution inversion and finite
Euler factorization are credited, not claimed as new discoveries.

## 1. State and the distinction that matters

For a real prefix a(1),...,a(Y), put b=Y+1, B=b^2-1, and

    A_a(x) = sum_(n<=x) a(n),
    E_Y(a) = sum_(k<=Y) A_a(k)^2/[k(k+1)],
    u_Y(a) = sum_(k<=Y) A_a(k)/[k(k+1)],
    mathcal A_Y(a) = E_Y(a) + 2b u_Y(a)^2.

The canonical completion c preserves that prefix, has cumulative value
-2b u_Y on [b,2b), and is zero afterwards. Its two added coefficients are

    c_b = -A_a(Y)-2b u_Y,     c_(2b) = 2b u_Y.

Thus sum c_n=sum c_n/n=0 and J(c)=integral A_c(x)^2 dx/x^2=mathcal A_Y(a).
This elementary finite minimization is BNR26-1; all its costs are retained.
Let N(c)=2c-1*c*c, using ordinary Dirichlet convolution and 1(n)=1.
Write V_c(x)=sum_(n<=x)N(c)(n). Recomplete its full prefix through B to
obtain the next energy mathcal A_B(N(c)). In particular

    mathcal A_B(N(c)) >= integral_J V_c(x)^2 dx/x^2              (1)

for every interval J contained in [1,b^2]. This needs no assumption about mu.

For the ACTUAL Mobius prefix, BNR26 proves N(c)(n)=mu(n) for n<b^2. The
remaining native target includes

    1+mathcal A_B(mu) <= 2(1+mathcal A_Y(mu))^(3/2).             (G)

This packet does not prove or refute (G) on mu. It proves something materially
stronger than the old generic counterexample: even bounded input energy,
ternary prefix coefficients, and uniformly bounded completion coefficients
cannot give an energy-only bound for Newton on the larger nonnative class.

## 2. NSR26-1: an unbounded counterfamily with a ternary prefix

There are constants C,c>0 such that for every sufficiently large integer R
one can choose a prefix a_R through Y=2R satisfying all of the following:

* a_R(n) is in {-1,0,1}, a_R(1)=1, and a_R agrees with mu through n=5;
* its total is zero, its canonical completion satisfies both moment balances,
  and EVERY completed coefficient has absolute value at most one;
* mathcal A_Y(a_R)<=C;
* for that completed source,

      integral_(R^2)^((4R/3)^2) V_c(x)^2 dx/x^2 >= c R.          (2)

The endpoint changes of O(R) used in discretization do not change this
assertion; the proof below controls the error on the displayed interval itself.
Consequently no constants K,p<infinity can give

    1+mathcal A_B(N(c)) <= K(1+mathcal A_Y(a))^p

on this whole class. Nor can any locally bounded function of the input energy
alone do so. The theorem remains false if a fixed power of log Y is allowed
on the right. This is NOT a counterexample to the native Mobius estimate.

### 2.1 Exact two-moment discrete sources

Fix L=log(4/3) and a nonzero real C-infinity function phi supported strictly
inside (0,L), with 0<=phi<=1. All constants below may depend on phi, never on R.
Set T=kappa sqrt(R), where for example kappa=1/2. For a phase theta define

    H(x) = sqrt(x)/T * phi(log(x/R)) cos(T log(x/R)+theta),
    z_n = n [H(n-1)-2H(n)+H(n+1)].

H is zero outside its stated positive compact interval. Every sum is finite.
Two telescopes give exactly

    sum z_n = 0,     sum z_n/n = 0,
    Z(k):=sum_(n<=k)z_n = k H(k+1)-(k+1)H(k).                  (3)

Let F(x)=x H'(x)-H(x), and u=log(x/R). Then

    F(x)=sqrt(x) f_(theta,T)(u),
    f_(theta,T)(u)=Re{exp(i theta+i T u) q_T(u)},
    q_T=i phi+(phi'-phi/2)/T.                                 (4)

Direct differentiation gives, uniformly on the support,

    x H''(x) = [ (phi''-(T^2+1/4)phi) cos(Tu+theta)
                   -2T phi' sin(Tu+theta)]/[T sqrt(x)].       (5)

Taylor's formula for the central second difference, with the bounded
fourth derivative of the chosen bump, gives

    z_n = n H''(n)+O(R^-1),
    |z_n| <= kappa+O(R^-1/2) <1,                              (6)
    sup_(x>0) |Z(floor x)-F(x)| = O(1).                       (7)

For clarity, H^(j)(x)=O(T^(j-1)R^(1/2-j)) for j>=1 (with fixed-bump
lower-order terms included). The central remainder n O(H'''') is O(R^-1)
when T=kappa sqrt R. In (7), the first forward Taylor remainder is
k H''(k)/2=O(1); movement across one unit cell also costs O(1).
The compact support ensures the same bounds at its ends.

Round the cumulative values, not the source coefficients:

    C(k)=floor(Z(k)+1/2),     w_n=C(n)-C(n-1).                 (8)

Since |z_n|<1, w_n is ternary. Its total is zero. The rounded cumulative
function differs from F by a bounded amount, uniformly in R and theta.
The rounding error relative to Z is at most 1/2. Therefore (3) implies

    |sum_n w_n/n|
      = |sum_k [C(k)-Z(k)]/[k(k+1)]|
      <= (1/2)[1/(R-O(1))-1/(4R/3+O(1))]
      = 1/(8R)+O(R^-2).                                    (9)

No cancellation of this error is assumed. The estimate is a complete
weighted-cell sum, not a pointwise quadrature estimate extrapolated to a tail.

### 2.2 Fix the initial coefficient and pay the canonical tail

Add the fixed, disjoint, ternary baseline

    alpha_1=1;
    alpha_2=alpha_3=alpha_5=alpha_6=-1;
    alpha_10=alpha_15=alpha_30=1;
    alpha_n=0 otherwise.

Its total and reciprocal sum are both zero; J(alpha)=23/15, by the exact
finite cumulative sum. It agrees with mu through 5, but NOT at 6. Put

    a_R = alpha+w,     Y=2R.

Both cumulatives vanish between their disjoint supports, so their J energies
add without a cross term. Equations (4),(7),(8) give

    E_Y(a_R)=23/15 + ||f_(theta,T)||_2^2 + O(R^-1/2)=O(1).

Here the comparison error has weighted L2 norm O(R^-1/2). Also the total
prefix is zero, and (9) bounds its u_Y. The canonical added coefficients are
-2b u_Y and +2b u_Y. Each has magnitude at most 1/2+O(R^-1), hence at most
one for large R; their complete energy price is O(1/R). This proves all
input assertions, uniformly for each of the three phases used below.

### 2.3 The quadratic resonance in the actual output interval

First use the continuous signed measure dF(x)=F'(x)dx. Its product cumulative is

    W_F(x)=integral integral_(rs<=x) dF(r)dF(s).

If x=R^2 exp(v), elementary logarithmic convolution and integration by parts give

    W_F(x)=sqrt(x) [(D+1/2)(f_(theta,T)*f_(theta,T))](v),       (10)

where * in (10) is ADDITIVE convolution on the real line, not arithmetic
Dirichlet convolution. Both functions have compact support. To verify (10),
the logarithmic density of dF is sqrt(R) exp(u/2)(D+1/2)f(u). Convolve the
two densities, then integrate once; the boundary terms vanish. Consequently

    integral_(R^2)^((4R/3)^2) W_F(x)^2 dx/x^2
       = ||(D+1/2)(f_(theta,T)*f_(theta,T))||_2^2.             (11)

The entire convolution support is inside [0,2L], so nothing is omitted.

Write q=q_T, U_T=(D+1/2)[exp(iTv)(q*q)(v)]. Expanding the real parts in (4)
shows that the output in (11) has the form

    (1/2) Re(exp(2i theta) U_T) + B_T,

where B_T is real and independent of theta. Average its squared L2 norm over
THREE fixed phases theta=0,pi/3,2pi/3. Both sums of exp(2i theta) and
exp(4i theta) vanish, so the average is EXACTLY

    ||B_T||_2^2 + (1/8)||U_T||_2^2.                          (12)

Moreover q_T*q_T=-phi*phi+O(1/T) in H^1. Thus

    ||U_T||_2 >= T||phi*phi||_2-O(1).                         (13)

At least one of those three real phases has output norm at least
(T||phi*phi||_2-O(1))/sqrt(8). This is a proof for each sufficiently large
R, not a random-source assertion or a claim that every phase works equally well.

### 2.4 Discrete errors and EVERY other Newton term

Let W_w(x)=sum_(rs<=x) w_r w_s. By (7),(8) the cumulative difference between
the signed measures sum w_n delta_n and dF is uniformly O(1). Their total
variations are O(R): the first follows from the ternary cap and support,
the second from (5). Expanding the difference of the two tensor products and
integrating first in one variable gives the uniform bound

    |W_w(x)-W_F(x)| <= O(1)(sum|w_n|+integral|F'|)=O(R).       (14)

There is no assumption about the number of divisors of an individual product.
On x comparable to R^2, an O(R) pointwise error has bounded weighted L2 norm.

On the displayed interval all products of two wave-support indices are
larger than x/2, for large R, because (4/3)^2<2. Therefore the wave-wave part
of the Newton FLOOR sum is exactly W_w(x), with no second or later multiple.
Products involving a wave index and a canonical tail index are larger than
x; products of two tail indices are also larger than x. These terms are zero
on this interval, not estimated by an unbounded remainder. Since x exceeds
the whole support of c, the linear cumulative term 2A_c(x) is zero.

The remaining terms involve alpha. Its two exact moments kill both rank-one
pieces of floor(t)=t-1/2-psi(t), where |psi|<=1/2, including integer arguments.
Writing L_w=sum|w_n|=O(R) and L_tail<=2, their total absolute contribution is
at most

    8 L_w + 32 + 8 L_tail = O(R).                            (15)

Equations (14),(15) have bounded weighted L2 cost, while (12),(13) provide
an output norm of order T. The reverse triangle inequality therefore yields
an energy at least c T^2=c kappa^2 R for a suitable one of the three phases
and all sufficiently large R. This proves (2) and the theorem.

This argument is based on an oscillatory, nonmultiplicative source. It does
not assert that mu has such a wave packet. The family fails the full finite
inverse identities; the example already fails at n=6. The obstruction says
exactly why those identities cannot be replaced by energy, balance and a
ternary coefficient cap.

## 3. NSR26-2: a fully rational finite counterexample

The authoritative finite input is `counterexample.json`. Its compressed
word decodes to 21,251 ternary entries at indices 65,737 through 86,987,
including 6,288 nonzero entries. Outside that interval the prefix through
Y=131,072 is the fixed alpha above and zeros. A floating scout selected the
word; the accepting calculation uses only that EXACT word, integers and
rational inequalities. No enclosure for the scout's sine or logarithm is
claimed or needed. The finite example is checked on its own terms, not
asserted to equal the analytic bump family exactly.

Let w be this word, C its cumulative, L_w=sum|w_n|, and

    B_w=sum |w_n|/n.

For all real x,y,

    |W_w(x)-W_w(y)| <= |x-y| B_w+L_w.                         (16)

Indeed, for each outer index r, there are at most |x-y|/r+1 inner integers
between the two thresholds, and |w_s|<=1. Sum against |w_r|. Endpoint jumps
are paid by L_w. This is a continuum bound, not an interpolation assumption.

The checker computes W_w at 4,096 integer midpoints using BOTH ordered
product fibers and a separate hyperbola split

    W_w(m)=2 sum_(r<=sqrt(m)) w_r C(floor(m/r))-C(floor sqrt(m))^2.

All sums include the full support. On each adjacent interval [l,u), with
midpoint m and D=max(m-l,u-m), the whole Newton output therefore obeys

    |V_c(x)| >= (|W_w(m)|-D B_w-9 L_w-32-32b|u_Y|)_+.        (17)

The extra 8 L_w+32 pays every alpha term, and 32b|u_Y| pays its interaction
with the canonical tail of total variation 4b|u_Y|. The support tests in the
checker justify every zero product sector. Integrate (17)^2 against dx/x^2
EXACTLY on the complete interval [l,u). No claim of sign constancy is needed.

Integer directed sums with denominator 2^96 give

    1.629167080304 <= mathcal A_Y(a) <= 1.629167080305,
    |c_b|=|c_(2b)| < 0.001160835923236,
    integral_4294967296^7635788689 V_c(x)^2 dx/x^2
         > 15.732535140697.

The entire output window is within [1,b^2], b^2=17,180,131,329. It is covered
by the 4,096 inequalities, not by enumerating seventeen billion coefficients.
The checker verifies the stronger exact rational comparison

    (1+output_lower)^2 > 4(1+input_upper)^3.

Thus the generic version of (G) fails. Recompletion of the entire output can
only add nonnegative energy beyond this lower bound. No mu computation at
these billion-sized coordinates is performed or represented by this example.

## 4. NSR26-3: source-first native reconstruction and causal prime grouping

We also attacked the ACTUAL native update, not just the countermodel.
Let g(n)=mu(n) for n<=Y and zero afterwards, and put

    e=delta-1*g,     F_Y(t)=sum_(n<=t)e(n)
                             =1-sum_(n<=Y)mu(n)floor(t/n)    (t>=1),
    F_Y(t)=0 for t<1.

The exact inverse identities imply e(n)=0 for n<b and F_Y(t)=0 for t<b.
Ordinary Dirichlet algebra gives N(g)=g+g*e. Thus for b<=x<b^2,

    M(x)=M(Y)+sum_(r<=x/b) mu(r) F_Y(x/r).                    (18)

This uses inverse/divisor cancellation BEFORE taking squares. N(g) and the
balanced N(c) agree on this prefix by BNR26's late-completion invariance.
N(g) is not assigned a finite full-line norm here; it is only a finite-prefix
producer. Huxley--Watt's classical short-source inversion is relevant prior art.

For any squarefree product P of finitely many primes define

    H_(Y,P)(t)=sum_(d|P) mu(d) F_Y(t/d).

Unique squarefree factorization n=d r, d|P, (r,P)=1 yields exactly

    M(x)=M(Y)+sum_(r<=Y,(r,P)=1)mu(r)H_(Y,P)(x/r),
                                              b<=x<b^2.     (19)

There is NO omitted cutoff correction: a term with rd>=b is zero because
x/(rd)<b and F_Y vanishes there. This is a causal application of classical
finite Euler factorization, closely related to PPD26 but WITHOUT averaging,
a sign selector, a growing-prime comparison theorem, or a change of source.
It is not claimed to be a new general convolution identity.

Group the r's in (19) into [2^j,2^(j+1)), and keep M(Y) as a separate constant
channel. If these real annular channels are v_1,...,v_q, then

    I_Y = ||sum_j v_j||^2 = D_(Y,P)+C_(Y,P),
    D_(Y,P)=sum_j||v_j||^2,
    C_(Y,P)=2sum_(i<j)<v_i,v_j>,
    I_Y <= q D_(Y,P).                                       (20)

The last is a valid Cauchy upper bound regardless of the sign of C. D alone
is NOT a universal upper bound. All norms use [b,b^2] with dx/x^2. The signed
mean update u_B=u_Y+integral_b^(b^2)M(x)dx/x^2 remains in mathcal A_B; neither
(19) nor a favorable value of D pays that balancing term automatically.

At Y=255, every one of the 65,280 integer output cells is exactly reproduced
for P=1,6,30,210. Directed rational calculations give:

| P | Sum of separate channel energies D | Complete I (unchanged) |
|---|---:|---:|
| 1 | 2.460478055389... | 0.179852003503... |
| 6 | 0.303702274816... | 0.179852003503... |
| 30 | 0.238532674099... | 0.179852003503... |
| 210 | 0.219222763075... | 0.179852003503... |

There are nine declared rows, including zero rows. Thus qD is reduced by the
same factors. The remaining signed cross term is kept in `results.json`.
This is a concrete finite improvement to the separated Cauchy budget, not an
all-scale estimate, a proof of quasi-orthogonality, or a new RH criterion.
A sufficiently large prime bank would eventually encode the original source
almost tautologically; increasing the bank is NOT itself an analytic gain.

## 5. Two additional exact checks on where cancellation can occur

### Product coalescence does not create Mobius sign cancellation

For r,s squarefree, mu(r)mu(s)=(-1)^Omega(rs). Consequently every nonzero
summand at a fixed product q in (g*g)(q) has the SAME sign. The coalesced
coefficient is lambda(q) times the number of allowed squarefree factorizations.
Combining equal products is important bookkeeping, but not itself a source
of cancellation. Divisor fibers in (18), or interactions between DIFFERENT
products, must supply the gain. This elementary observation has no priority claim.

### Short additive separations are already a controlled part of E_X

For integer X and |a_n|<=1,

    E_X(a)=sum_(m,n<=X) a_m a_n [1/max(m,n)-1/(X+1)].

The absolute contribution of all ordered pairs |m-n|<=H is at most

    (2H+1) sum_(n<=X)1/n <= (2H+1)(1+log X).                 (21)

Order by the larger index: at most 2H+1 pairs are charged to each index,
and the kernel is nonnegative and at most its reciprocal. Thus bounded or
polylogarithmic additive separations have a polylogarithmic budget without
assuming a Chowla estimate. This elementary bound does NOT control the
long-range pairs or the additional 2(X+1)u_X^2 balancing price. It is included
as a scope check, not advertised as a new prime-distribution theorem.

## 6. Native evidence and the actual remaining mathematical work

The accepting program reconstructs mu independently by a linear sieve and
by sign flips plus square removal, comparing all 1,048,575 positive entries.
It verifies (G) at EVERY integer cutoff 1<=Y<=1023 using directed bounds for
both E and u, with no interpolation. The largest certified squared gain ratio
is below 0.141345679012346, at Y=1. This is finite evidence only.

Six separate divisor-first Newton reconstructions at Y=1,3,15,63,255,1023
compare 1,118,478 output coefficients in total to the independently generated
source. This count includes overlaps; it is not 1,118,478 distinct new integers.
The four native bank experiments cover the complete declared annulus, retain
all cross terms, and do not replace native coefficients by optimized signs.

The mathematical pass did NOT obtain the all-scale native gain. It rules out
an energy-only proof even after strengthening the fake-source controls to
ternary prefixes and bounded completion coefficients. Its affirmative result
is the exact source-first regrouping and the finite reduction of a legitimate
Cauchy budget. The most concrete remaining work is to prove a uniform estimate
for those divisor-cancelled, prime-grouped native channels, including their
remaining signed covariance AND the updated mean. Neither a fixed-bank norm
inequality nor the finite table is asserted to provide it.

The proposed infinite counterfamily proof, finite certificate's envelope
inequality, and source-first native formulas require independent review. No
independent mathematical acceptance, formal verification, or novelty priority
claim is made by the successful exact replays.
