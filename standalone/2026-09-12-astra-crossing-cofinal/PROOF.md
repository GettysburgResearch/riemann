# XCC26: cofinal crossing cuts and a sign-faithful native source

**Status: PROPOSED component arguments, pending independent mathematical review.
The required cofinal covariance bound and RH remain OPEN.**

Date: 2026-09-12. Parent research: PR848 at
`2f0056d542603cb8118b9ac9da45b397162778e4`.
No statement or artifact in an earlier packet is changed. The Mellin,
Littlewood, Landau, Perron, convolution and Hilbert-space ingredients are
classical. This packet reconstructs the needed applications; no external
priority claim is made for the resulting growth criterion.

The change in strategy is not a fourth Newton order. We prove that the native
energy has a true logarithmic growth exponent, so a successful contraction need
not recur on a predetermined ladder. We then use unconditionally cofinal
arithmetic sign crossings to build a different completion: one small late
coefficient, negligible added energy, and exactly Liouville-coherent signs.
The new finite covariance tests are negative, but an all-cofinal sign theorem
is NOT proved. Section 6 exhibits why sign coherence alone cannot supply it.

## 0. Fixed objects

Throughout mu is the ordinary Mobius function, lambda(n)=(-1)^Omega(n),

    M(k)=sum_(n<=k) mu(n),     m(k)=sum_(n<=k) mu(n)/n,  m(0)=0,
    F_Y=sum_(k=1)^Y m(k)^2,
    E_Y=sum_(k=1)^Y M(k)^2/[k(k+1)].                         (0.1)

For a finite real coefficient source a define

    P_a(s)=sum a_n n^(-s), A_a(x)=sum_(n<=x)a_n,
    J(a)=integral_1^infinity A_a(x)^2 dx/x^2.              (0.2)

The entire constant future after the final coefficient is included. Finite
expansion of the kernel gives

    J(a)=sum_(r,s) a_r a_s/max(r,s)
        =sum_(k>=0) [P_a(1)-sum_(n<=k)a_n/n]^2.            (0.3)

For the second equality use 1/max(r,s)=min(r,s)/(rs) and count k<min(r,s).
Both sides are finite even though the physical integral is over an infinite
interval. Summation by parts gives

    E_Y=F_Y-(Y+1)u_Y^2,  u_Y=(sum_(k=0)^Y m(k))/(Y+1),    (0.4)

so E_Y<=F_Y. These are the NIR26 coordinates, not new normalization choices.

Let Theta be the supremum of the real parts of all nontrivial zeta zeros.
Classical zeta continuation, existence of nontrivial zeros, zero freedom on
Re s=1, and reflection give 1/2<=Theta<=1. The case Theta=1 is not excluded.
No actual zero coordinates, simplicity or numerical zero census is used.

## 1. XCC26-1: the native energy has a limit, not only a limsup

Unconditionally, as a relation to the as-yet-unknown Theta,

    lim_(Y->infinity) log(1+E_Y)/log(Y+1)
      = lim_(Y->infinity) log(1+F_Y)/log(Y+1)
      = 2Theta-1.                                       (1.1)

This is not an evaluation of Theta and not a bound implying RH. It is not
regular variation: no asymptotic constant or fixed-ratio quotient is asserted.
We supply the lower bound at EVERY prefix and a classical zero-free-half-plane
upper bound. Their combination is what permits sparse-cutoff arguments below.

### 1.1 Every fixed off-line zero forces every sufficiently long prefix to pay

For each Y the finite completion

    C_Y(s)=sum_(n<=Y)mu(n)n^(-s)-M(Y)(Y+1)^(-s)

has full energy E_Y and matches the literal prefix through Y. Its cumulative
source is zero after Y+1. Put h_a(t)=exp(-t/2)A_a(exp t), so ||h_a||_2^2=J(a).
For s=z+1/2 its Laplace transform is P_a(s)/s.

Use the actual causal factorial source

    d(t)=exp(-t/2)[floor(exp t)(1-t)+log(floor(exp t)!)].

If x=exp t and n=floor x, integral comparison for log gives
0<n(1-log x)+log(n!)<=1+log x. For the lower bound, use
log(n!)>=integral_1^n log u du=n log n-n+1 and
n log(1+1/n)<1. The upper bound follows by integrating to n and retaining
log n. Thus ||d||_1<=integral_0^infinity exp(-t/2)(1+t)dt=6.
Direct finite summation/integration in Re s>1, followed by continuation, gives

    Ld(z)=(s-1)zeta(s)/s^2.

The pole at s=1 is removable in this expression. Therefore y_Y=d*h_(C_Y)
is an ordinary L2 source of norm at most 6 sqrt(E_Y), with transform
(s-1)zeta(s)C_Y(s)/s^3. Before T=log(Y+1), finite divisor inversion gives

    y_Y(t)=h_*(t):=exp(-t/2)(t-t^2/2).

For a direct check, expand the convolution as exp(-t/2) times
sum_(r<=exp t)(sum_(n|r)a_n)[v-v^2/2], v=t-log r. The divisor coefficient
is delta_(r=1) on this initial interval. Also ||h_*||_2=sqrt(2) and
Lh_*(z)=(s-1)/s^3.

If rho=beta+i gamma is any nontrivial zero with alpha=beta-1/2>0, then
Ly_Y(rho-1/2)=0 and Lh_*(rho-1/2)=(rho-1)/rho^3 !=0.
The entire difference is supported at t>=T. Cauchy--Schwarz yields

    6sqrt(E_Y)+sqrt(2)
       >=sqrt(2alpha)|rho-1|/|rho|^3 * (Y+1)^alpha.        (1.2)

This is an all-Y lower bound, not an Omega value on a selected sequence.
It gives liminf >=2beta-1. Taking the supremum over beta gives the lower
bound 2Theta-1. When Theta=1/2, nonnegativity of the logarithmic ratio gives
the required lower bound zero. Neither the supremum nor any zero must be
attained on the critical boundary. The same lower bound holds for F>=E.

This causal lower argument is credited to the native-source line, including
PR829's COHERENT_SOURCE.md and EPC26. It has been repeated to expose its
quantifiers rather than imported as a reviewed global upper bound.

### 1.2 The generalized Littlewood upper bound, with its zero assumption exposed

We need the classical implication: if 1/2<=theta<1 and zeta has no zero
in Re s>theta, then, for every epsilon>0,

    M(x)=O_(theta,epsilon)(x^(theta+epsilon)).            (1.3)

Here is a reconstruction using elementary analytic estimates and truncated
Perron; it does not assume RH when theta>1/2.

First fix sigma0 in (theta,1). For large |t| put the center at 2+it and choose
three radii r1<1<2-sigma0<r2<R<2-theta. Every disk of radius R is zero-free
and misses the pole at one. It admits the branch g=log zeta agreeing with the
Euler logarithm at its center. Euler summation (DLMF 25.2.8), truncated at an
integer comparable with |t|, gives a polynomial upper bound for |zeta| on
this disk. Thus Re g<=C log(|t|+2). The center value is uniformly bounded by
the absolutely convergent Euler logarithm. Borel--Caratheodory consequently
gives max_(|z-(2+it)|<=r2)|g(z)|=O(log(|t|+2)). On the radius-r1 disk the
Euler logarithm itself is O(1). Hadamard's three-circles theorem, applied
between r1 and r2 at radius 2-sigma0, gives

    |log zeta(sigma+it)|=O((log(|t|+2))^nu),  nu<1,
                      sigma0<=sigma<=2.

The branch is the same at all these points. On sigma>=2 use the Euler product.
Therefore for every eta>0, uniformly on any required compact real interval
sigma>=sigma0,

    |1/zeta(sigma+it)|=O((|t|+2)^eta).                   (1.4)

At bounded height this follows from holomorphy of 1/zeta, including its zero
at one. No inverse-zeta bound on the zero boundary sigma=theta is asserted.

For completeness, take a half-integer x=N+1/2, c=1+1/log x and T=x^2.
Termwise truncated Perron for the absolutely convergent inverse series gives

    M(x)=(1/(2pi i))int_(c-iT)^(c+iT) x^s/[s zeta(s)]ds
                        +O(x log^2 x/T).                (1.5)

The scalar Perron kernel has error
O(u^c min(1,1/(T|log u|))) at u!=1; integrating its two infinite tails by
parts proves this estimate. For n between x/2 and 2x, use
|log(x/n)|>=const |x-n|/x and |x-n|>=1/2. Summing gives O(x log x/T).
Outside that range sum (x/n)^c/T, using sum n^-c=O(log x), to obtain the
stated safe logarithm-squared error. Thus no integer-endpoint ambiguity or
unquantified truncation is hidden in (1.5).

Shift the contour to sigma0=theta+epsilon/2<1, using (1.4) with eta=epsilon/8.
There are no poles in the rectangle. The vertical integral is
O(x^sigma0 T^eta); the two horizontal pieces are
O(x^c T^(-1+eta)). Together with (1.5) these are O(x^(theta+epsilon)).
The bounded initial range and integer x follow by the half-integer choice.
For larger epsilon, use a smaller one. This proves (1.3).

Apply (1.3) with theta=Theta when Theta<1. For any sufficiently small delta,
M(x)=O(x^(Theta+delta)) with Theta+delta<1. Partial summation and the limiting
Euler value 1/zeta(1)=0 give

    m(Y)=M(Y)/Y-int_Y^infinity M(x)dx/x^2
        =O(Y^(Theta-1+delta)).                           (1.6)

To justify the limiting value, (1.3) makes the inverse Dirichlet series
locally uniformly convergent in Re s>Theta+delta by partial summation; it
agrees with 1/zeta on Re s>1 and hence at s=1 by continuation. Summing the
squares in (1.6) gives F_Y=O_epsilon(Y^(2Theta-1+epsilon)). This includes
Theta=1/2 after absorbing logarithmic endpoints in epsilon.

If Theta=1, the complete divisor identity gives |m(Y)|<=1: indeed
Y m(Y)=1+sum_(n<=Y)mu(n){Y/n}, with the n=1 fractional part zero. Hence
F_Y<=Y. This handles the otherwise unavailable fixed zero-free gap.
Together with Section 1.1 and E<=F, these bounds prove (1.1).

### 1.3 Sparse scales really suffice

Let r>1 and 0<delta<r be fixed. If on ANY unbounded integer sequence Y_j,

    1+F_(floor((Y_j+1)^r)-1)
       <= exp(o(log Y_j)) (1+F_(Y_j))^(r-delta),          (1.7)

then RH follows. If kappa=2Theta-1>0, divide logarithms by log Y_j and use
(1.1): r kappa <=(r-delta)kappa, a contradiction. No bound on Y_(j+1)/Y_j,
no prior ladder membership, and no cofinal-to-global interpolation across
those gaps is used. Kappa=0 is equivalent to RH by reflection and the
definition of Theta. This is a sufficient condition, not a claimed converse
for the stronger relative-energy inequality (1.7).

## 2. XCC26-2: an unconditional unbounded set of nearly balanced cuts

Define the weak sign-crossing set

    X={Y>=2: mu(Y)!=0 and m(Y-1)m(Y)<=0}.                 (2.1)

Then X is unbounded. At every Y in X,

    |m(Y)|<=1/Y,
    m(Y)!=0 => sign(m(Y))=mu(Y)=lambda(Y).               (2.2)

The local assertions follow by adding the single term mu(Y)/Y. Zeros are
permitted in (2.1); no theorem claiming m(Y) never vanishes is assumed.

For unboundedness, we give a Landau oscillation proof. For Re z>0, ordinary
partial summation gives

    int_1^infinity m(x)x^(-z-1)dx=1/[z zeta(z+1)].        (2.3)

The right side is analytic at every REAL z>-1. At zero use the simple pole
of zeta; for -1<z<0 the alternating eta series shows zeta(z+1)<0, and for
z>0 the Euler product is positive. On the other hand, each nontrivial zero
rho gives a genuine pole at z=rho-1 in Re z>-1.

If m were eventually of one sign, remove an initial compact interval and
change its sign if necessary. On t=log x this gives a nonnegative Laplace
density f(t), and changes (2.3) by an entire function. Its convergence
abscissa a is at most zero because |m|<=1. Landau's elementary principle
says a finite abscissa is a real singularity: if its Laplace transform were
analytic at a, Taylor expansion about a+epsilon has nonnegative integral
coefficients when evaluated to the left. Monotone convergence then proves
convergence at a-epsilon, a contradiction. More explicitly, take a disk of
analyticity centered at a, use a center a+r/4, and expand toward a-r/4 within
that disk. The exponential series consists of nonnegative terms. Derivatives
under the integral are valid to the right of a by exponential domination.

As (2.3) is analytic along the whole real interval (-1,infinity), that
abscissa would have to be <=-1 (or -infinity). The integral would then be
holomorphic throughout Re z>-1, contradicting its nonreal pole at any
rho-1. Thus m has positive and negative values arbitrarily far out. Passing
between these signs supplies arbitrarily late indices in (2.1), including
a crossing through an intervening zero when necessary. This uses classical
existence of a nontrivial zero, not its location, simplicity, or RH.

## 3. XCC26-3: one sign-faithful collar with O(1/Y) energy cost

For Y in X, retain the native prefix and define the finite source

    c_n=mu(n) for n<=Y,   c_(2Y)=-2Y m(Y),
    c_n=0 otherwise.                                    (3.1)

When m(Y)=0 the extra coefficient is simply absent. Exactly,

    P_c(1)=0,  |c_n|<=2,  support(c)<=2Y,
    J(c)=F_Y+(Y-1)m(Y)^2 <= F_Y+1/Y.                    (3.2)

The reciprocal coordinates equal m(k) through Y, equal m(Y) for
Y<k<2Y, and vanish from 2Y onward. Thus (0.3) proves the full norm formula,
including the original cumulative source's possibly nonzero infinite tail.
No future Mobius coefficient is used to complete the source.

There is an additional exact algebraic benefit:

    c_n=lambda(n)b_n with b_n>=0 for EVERY n.             (3.3)

For the native prefix use mu=lambda |mu|. If m(Y)!=0, (2.2) and
lambda(2Y)=-lambda(Y) show that the late coefficient has precisely the
required sign, even if Y is even or 2Y is not squarefree. Thus, for every
integer degree j>=1,

    (c^(*j))(d)=lambda(d)b_j(d),  b_j(d)>=0.              (3.4)

This follows from complete multiplicativity of lambda and summing all
factorizations of the SAME product d. The old clipped collar did not impose
(3.3). This is not a license to discard correlations of different products.

## 4. XCC26-4: the actual quadratic energy at a crossing

Put b=Y+1, B=b^2-1, z=c*c and v=2c-1*z. In the convolution ring,
e=delta-1*c vanishes below b and

    mu-v=mu*e*e.

Hence v(n)=mu(n) for all n<=B, and the first excluded error at b^2 is
mu(b^2)-v(b^2)=e(b)^2. This is the classical short-source Newton identity.
It uses every native divisor equation through Y, not just (3.2) or (3.3).

Let H_0=0, H_j=sum_(n<=j)1/n and define

    K_d(k)=[H_floor(k/d)-H_k+log d]/d,
    Q(k)=sum_d z(d)K_d(k).

The two exact moment identities sum z(d)/d=sum z(d)log d/d=0 follow from
P_c(1)^2 and its derivative. Thus Q(k)=sum z(d)H_floor(k/d)/d is rational,
and the complete reciprocal output is

    sum_(n<=k)v(n)/n=2m_c(k)-Q(k).                       (4.1)

All terms with the same product d are coalesced BEFORE defining

    D_Y=sum_d z(d)^2 sum_(k=b)^B K_d(k)^2,
    C_Y=sum_(d!=e)z(d)z(e)sum_(k=b)^B K_d(k)K_e(k).       (4.2)

C is ORDERED and signed. It differs from the previous clipped-completion
covariance even at the same Y, and is not added to it or to the cubic one.
Let T=(Y-1)m(Y)^2 and L=sum_(k=b)^B m_c(k)Q(k). Exactly,

    F_B=F_Y+4T+D_Y+C_Y-4L.                               (4.3)

### The complete collision diagonal stays logarithmic

For all d>=1, the whole-packet estimate is

    sum_(k>=1)K_d(k)^2<=18/d.                            (4.4)

To rederive it, write r(x)=H_floor(x)-log x-gamma. Harmonic integral estimates
give |r(x)|<=1/x for x>=1 and |r(x)|<=log(1/x)+1 for x<1. The decreasing
small-x integral is 5d and the reciprocal-square part at most 2d; hence
sum_(k>=1)r(k/d)^2<=7d and sum r(k)^2<=2. Now
d K_d(k)=r(k/d)-r(k); square and sum to obtain 14/d+4/d^2<=18/d.
This includes every integer endpoint and the entire unbounded k tail.

The cap two gives |z(d)|<=4 tau_2(d). Prime-power comparison
(e+1)^2<=binomial(e+3,3) gives tau_2(d)^2<=tau_4(d). Thus

    D_Y<=288 H_(4Y^2)^4.                                (4.5)

All same-product multiplicities have been included. In particular no
large single collar coefficient creates artificial diagonal energy.
The exact inequality (2t-Q)^2<=8t^2+2Q^2 now gives

    F_B<=F_Y+8/Y+576H_(4Y^2)^4+2C_Y.                    (4.6)

Unlike the previous general clipped construction, the old-energy coefficient
here is ONE; the collar costs less than 1/Y. This is a different source,
not a correction of the earlier valid bound.

The raw quadratic v is also a legitimate full-energy source: for x>=2Y,
its cumulative value is 2sum c_n+sum_d z(d){x/d}, which is bounded. Its full
physical energy is finite, with a constant-times-1/X tail above X. Identity
(4.3) concerns exactly the displayed finite native annulus. No later energy
is declared zero; at the next prefix the explicit one-atom or bounded
completion supplies its own entire source.

## 5. XCC26-5: an infinitely-often sign theorem would now finish RH

If C_Y<=0 for arbitrarily large Y in the unconditionally unbounded set X,
then RH holds. More generally it suffices along such a subsequence that

    C_Y <= exp(o(log Y)) (1+F_Y)^(2-delta),
                    some fixed 0<delta<=1.              (5.1)

Indeed, under failure of RH let kappa=2Theta-1>0. By (1.1),
F_Y=Y^(kappa+o(1)), F_B=Y^(2kappa+o(1)). Equation (4.6) contradicts
C_Y<=0 along any unbounded sequence. For (5.1), the maximum exponent on its
right side and in (4.6) is max(kappa,(2-delta)kappa)<2kappa.
No relation between consecutive selected Y's is required.

There is a sharper obstruction under the SAME hypothetical failure:

    C_Y/F_((Y+1)^2-1) -> 1 as Y->infinity through X.      (5.2)

On the annulus, Q=2t-m. Hence
||Q||^2=(F_B-F_Y)+4T-4<t,m>. Here T<=1/Y and
|<t,m>|<=sqrt(T(F_B-F_Y)). Equation (1.1) gives F_Y/F_B->0,
and the logarithmic D_Y from (4.5) is o(F_B). Therefore
C_Y=||Q||^2-D_Y=(1+o(1))F_B, proving (5.2).
So any off-line zero would force this new covariance to be EVENTUALLY positive
at every sufficiently late crossing, not just large on an unspecified set.
There is no evaluated threshold, because neither Theta nor convergence rates
in (1.1) have been determined. The reverse assertion that RH implies an
infinitely-often negative sign is NOT claimed.

This is the intended complete ending. THE UNPROVED PREMISE IS infinitely-often
control of the ACTUAL covariance at X. Cofinality of crossings, cheap
completion, multiplicative signs, and finitely many negative panels do not
prove it. The central estimate is not left for reviewers as a routine detail.

## 6. XCC26-6: the direct sign attack and two explicit failures

The 34 finite native panels consist of all crossing cuts through 127 and
three additional cuts 173,210,431. Every displayed covariance is strictly
negative in directed arithmetic. All products and all annular integers are
included by exact quotient-block aggregation. This is finite support for the
candidate sign, not an extrapolation beyond the tested cutoffs.

### Pairwise negativity is false even at the first crossing

At Y=5 the exact completed source is

    c_1=1,c_2=c_3=c_5=-1,c_10=1/3.

It has z(2)=z(5)=-2. The pair 2,5, including both orientations, contributes

    2 z(2)z(5) sum_(k=6)^35 K_2(k)K_5(k) > 1/100.         (6.1)

The total covariance is negative. Thus even at a crossing with exact
Liouville signs, not every pair has a favorable sign.

### Sign coherence and a small crossing residual are also insufficient

Take Y=19 and the NON-NATIVE prefix

    a_1=1, a_3=-16328359/38798760,
    a_n=-1 for n in {5,7,8,11,12,13,17,18,19},
    all other a_n=0 for 1<=n<=19.

Its reciprocal sums immediately before and after 19 are exactly 1/38 and
-1/38. Every coefficient obeys |a_n|<=1 and lambda(n)a_n>=0. Completing at
38 gives c_38=1. Thus all conditions (3.2)--(3.4), including negligible
added energy and complete multiplicative sign coherence, hold for this fake
input. Nevertheless its actual covariance in (4.2) satisfies

    177/100 < C_19(fake) < 178/100.                       (6.2)

The computation evaluates the actual Newton output, NOT a supposed Mobius
continuation of this input. The source violates divisor inversion already
at n=2: a_1+a_2=1 rather than zero. Therefore (6.2) refutes the generic
sign-coherence shortcut, not the native criterion or RH.

The remaining attack must use the native equalities sum_(d|n)c_d=delta_(n=1)
for EVERY n<=Y inside the signed distinct-product sum. The construction
restores the multiplicative signs and pays the entire completion, but no
successful inequality using those equalities is supplied. Both failed
shortcuts above remain in the proposed proof packet rather than being hidden
behind the positive finite panels.

## 7. Dependencies, execution, and review

DLMF 25.2.8 supplies the classical Euler-summation surface used in Section 1;
25.2.3,25.4 and25.10 supply continuation, real-axis signs, reflection and zero
existence/location boundaries. Borel--Caratheodory, three circles, scalar
Perron and Landau's positivity argument are used with their domains stated
above. The generalized Littlewood argument is reconstructed, not a numerical
zero-free input. The convolution identity is classical (Huxley--Watt,
arXiv:1807.05890 and antecedents), and the source-energy lower bound is the
credited earlier causal construction. No theorem from the new gamma/Ising
branches is assumed.

The two same-author implementations reconstruct the finite source, crossing
list, entire output coefficients, complete coalesced products and directed
covariances by different arithmetic routes. Their normal/-O agreement and
mutation tests do not independently prove the analytic assertions. Read
VALIDATION.md for exact scope, including the difference between billions of
terms represented algebraically and the much smaller number of quotient blocks
actually evaluated. No full repository validation or formal proof build is
claimed. Independent review should prioritize the all-prefix lower bound,
zero-free upper bound, Landau cofinality argument, the sign of the 2Y collar,
and the sparse-subsequence quantifiers in Section 5.
