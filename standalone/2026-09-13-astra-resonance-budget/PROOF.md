# RBR26: annular resonance lower bounds and a budgeted causal filter attack

**PROPOSED component proofs, pending independent mathematical review. RH is
not proved.** Date: 2026-09-13 (Asia/Jerusalem). Intended add-only continuation
of PR848 at `99101457b32b6f10f4eda88ca998048404b860ea`.

The new direction is to distinguish polynomial growth caused by critical-line
resonances from exponential growth caused by an off-line zero. The former is
not an error that RH itself excludes. We first give an explicit annular lower
bound and use it to expose an extra consequence of the proposed covariance
sign target. Then we construct causal filters which can suppress resonances,
with an exact energy ledger and a uniform bound preventing concealment of any
fixed right-half-plane zero. The missing assertion is an upper bound for the
actual filtered native energy, not an existence or normalization convention.

Classical ingredients: convolution/Laplace transforms, Littlewood's implication
from RH to Mertens estimates, finite Bessel inequalities, approximate-identity
limits, minimum-norm moment interpolation, stable rational filters and Lyapunov
identities. No general priority claim is made. Ingham/weak-Mertens mean-square
work is relevant background; no theorem from a paper not inspected in full is
silently imported. The local arguments needed here are written out.

## 0. The unchanged native source and exact causal equation

Let mu be the ordinary Mobius function and

    M(x)=sum_(n<=x)mu(n),  m(x)=sum_(n<=x)mu(n)/n,
    F_Y=sum_(k=1)^Y m(k)^2.

For t>=0 define

    h(t)=exp(t/2)m(exp t),       g(t)=t exp(-t/2),
    d(t)=exp(-t/2)[floor(exp t)(1-t)+log(floor(exp t)!)].       (0.1)

All three functions are zero at negative times. The elementary log-factorial
integral comparison gives

    0<d(t)<= (1+t)exp(-t/2),       ||d||_1<=6.                 (0.2)

With s=z+1/2, the Laplace transforms, initially Re z>1/2, are

    D(z)=(s-1)zeta(s)/s^2,
    H(z)=1/[(s-1)zeta(s)],       G(z)=1/s^2.

These formulas follow by finite summation and integration of the floor series
and ordinary divisor inversion. The values at s=1 are removable. In particular
Laplace uniqueness, or direct divisor summation on every finite time interval,
gives the exact causal equation

    d*h=g.                                                   (0.3)

No RH or global square-integrability of h is used in (0.3). Locally all
integrals exist, and |m(x)|<=1 follows from
x m(x)=1+sum_(n<=x)mu(n){x/n} at integer x and then by taking integer parts.
Thus h(t) is at most exp(t/2). Also ||g||_2^2=2.

Put b=Y+1 and T=log b. The compact native input

    h_T(t)=h(t)1_(0<=t<T)

has exact whole norm

    ||h_T||_2^2=F_Y.                                         (0.4)

Indeed the change x=exp t leaves integral_1^b m(x)^2 dx, one full unit cell
for each k=1,...,Y. The output d*h_T agrees with g before T. This input is
in reciprocal-sum coordinates, not the old stopped-Mertens source; its norm
is F, not the different E or J.

## 1. RBR26-1: a sharp annular lower bound from a boundary resonance

### Statement

Assume RH in this section only. Let r>1, and let S be ANY finite set of distinct
critical-line zeros rho=1/2+i gamma, each of EXACT multiplicity m>=1. Then

    liminf_(T->infinity) T^(-(2m-1)) integral_T^(rT)|h(t)|^2 dt
      >= [m^2(r^(2m-1)-1)/(2m-1)]
             * sum_(rho in S) 1/|(rho-1) zeta^(m)(rho)|^2.    (1.1)

The derivative zeta^(m) is the ordinary m-th derivative, not a Taylor
coefficient. A conjugate pair counts as two distinct zeros in the sum. This
is a bound for EVERY sufficiently long logarithmic annulus, in the liminf
sense, not an Omega bound on selected large values. Other zeros, arbitrarily
high zeros and other multiplicities are not removed or assumed absent.
No assertion about the existence of a multiple zero is made.

For r=2 and T=log(Y+1), the left numerator is EXACTLY

    F_((Y+1)^2-1)-F_Y.                                      (1.2)

There is no incomplete unit cell at either endpoint.

### 1.1 The explicitly RH-dependent input bound

We use only the classical consequence

    RH => M(x)=O_epsilon(x^(1/2+epsilon))
       => m(x)=O_epsilon(x^(-1/2+epsilon))
       => |h(t)|<=C_epsilon exp(epsilon t)                    (1.3)

for every epsilon>0. For the middle step, partial summation gives
m(x)=M(x)/x-integral_x^infinity M(u)du/u^2. The limiting reciprocal sum is
zero: the Dirichlet series continued by the first bound agrees with 1/zeta
at s=1. The first implication is classical Littlewood, with a reconstruction
in the pinned XCC26 Section1.2. This is a CONDITIONAL use of RH, never a new
unconditional subexponential bound. Section2 eliminates this assumption by
combining the alternatives RH and not RH.

### 1.2 A compact adjoint test with no early-source contamination

Fix 1<a<b<r, and let

    A_m(a,b)=integral_a^b u^(2m-2)du
            =(b^(2m-1)-a^(2m-1))/(2m-1).

Define psi by specifying

    psi^(m)(u)=(-1)^m (m-1)! u^(m-1)/A_m(a,b), a<u<b,
    psi^(m)(u)=0 elsewhere,
    psi=psi'=...=psi^(m-1)=0 at u>=b.                       (1.4)

Equivalently

    psi(u)= [1/A_m(a,b)] integral_(max(u,a))^b
                               (v-u)^(m-1)v^(m-1)dv

when u<b, and zero otherwise. Hence psi(0)=1, psi is C^(m-1), and on u<a
it is one polynomial of degree at most m-1. Piecewise m-th derivatives are
bounded and compactly supported; their jumps cause no missing atoms below
order m. Furthermore

    ||psi^(m)||_2^2=((m-1)!)^2/A_m(a,b).                    (1.5)

For lambda=i gamma put

    V_(T,lambda)(s)=integral_0^infinity
              d(u)exp(-lambda u)psi((s+u)/T)du,
    v_(T,lambda)(s)=exp(-lambda s)V_(T,lambda)(s), s>=0.

The integral is actually zero beyond u=bT-s. Fubini on the finite triangle
and (0.3) give

    integral_0^(bT) h(s)v_(T,lambda)(s)ds
      = integral_0^(bT) g(t)exp(-lambda t)psi(t/T)dt
      = G(lambda)+o(1).                                    (1.6)

The last limit is dominated convergence: psi is bounded on [0,b] and g has
an exponential tail. No actual unknown-zero evaluation is supplied by code;
lambda here is an arbitrary fixed zero in the mathematical argument.

Multiplicity m implies

    integral_0^infinity u^j d(u)exp(-lambda u)du=0, j<m.

For 0<=s<=T, replace psi((s+u)/T) by the left polynomial from (1.4).
Its full integral is zero. The two functions agree when u<aT-s; the rest
is bounded using (0.2). For fixed a,b,m this gives

    |v_(T,lambda)(s)|<=C(1+T)^C exp(-(aT-s)/2), 0<=s<=T.

Combined with (1.3), choosing epsilon<(a-1)/2, this proves

    integral_0^T h(s)v_(T,lambda)(s)ds=o(1).                 (1.7)

This exponentially separated buffer is essential. Merely using an adjoint
polynomial with a nonzero boundary jet at T would leave an uncontrolled
boundary layer. The proof does NOT assume local energies are regularly
varying or infer an annular lower bound by subtracting two liminf bounds.

### 1.3 The complete scaled adjoint norm

Extend psi to the left by its polynomial. Taylor's formula with integral
remainder and the m vanished moments gives, on the scaled variable v=s/T,

    T^m V_(T,lambda)(Tv)
      = 1/(m-1)! integral_0^infinity u^m d(u)exp(-lambda u)
           integral_0^1(1-theta)^(m-1)
                    psi^(m)(v+theta*u/T)dtheta du.

Translations are continuous in L2(R). The dominating norm is integrable by
(0.2), since every absolute moment of d is finite. Therefore, strongly in L2,

    T^m V_(T,lambda)(T v)
       -> [(-1)^m D^(m)(lambda)/m!] psi^(m)(v).             (1.8)

In particular its norm on [T,rT] is

    T^(1-2m) |D^(m)(lambda)|^2/m!^2
                           * ||psi^(m)||_2^2 (1+o(1)).

Because psi^(m) is supported in (a,b), the full leading norm lies inside
that annulus. Equations (1.6),(1.7), followed by Cauchy--Schwarz, give

    liminf T^(-(2m-1)) integral_T^(rT)|h|^2
         >= m^2 A_m(a,b) |G(lambda)/D^(m)(lambda)|^2.

At rho=lambda+1/2 the quotient is exactly

    G(lambda)/D^(m)(lambda)
                    =1/[(rho-1)zeta^(m)(rho)].              (1.9)

Let a decrease to1 and b increase to r AFTER the T limit. The constants in
the leakage bound need not be uniform in these endpoint limits.

### 1.4 Several resonances and optimality of the test constant

For a fixed finite set S, normalize the adjoint vectors by T^(m-1/2).
By (1.8), their diagonal Gram entries converge to
|D^(m)(lambda)|^2||psi^(m)||^2/m!^2. Distinct frequencies have off-diagonal
entries tending to zero: the leading term is the Fourier transform of the
compact integrable function |psi^(m)|^2 at (gamma-gamma')T, and the errors
converge in L2. Apply the finite Gram/Bessel bound to (1.6),(1.7). This sums
the lower constants and proves (1.1). No infinite Gram inverse is used.

For any test with the same left/right polynomial conditions and psi(0)=1,
repeated integration gives

    (m-1)! = |integral_a^b u^(m-1)psi^(m)(u)du|.

Cauchy--Schwarz proves ||psi^(m)||^2 >=((m-1)!)^2/A_m(a,b).
The explicit test attains equality. Thus its constant is sharp in this
adjoint-test class. Rational stable examples in Section7 also attain the
limiting spectral constant; no sharp asymptotic for the literal Mobius energy
is asserted.

## 2. RBR26-8 and RBR26-2: an unconditional annular detector and multiplicity

### 2.1 RBR26-8: off-line zeros force EVERY late logarithmic annulus to pay

Suppose rho=beta+i gamma is a nontrivial zero with beta>1/2 and multiplicity
at least m. Put alpha=beta-1/2. For EVERY fixed r>1/beta there is an explicit
positive c(r,rho,m) and a finite T0 such that

    integral_T^(rT) |h(t)|^2 dt
        >= c(r,rho,m) exp(2alpha T) T^(2m-1), T>=T0.       (2.1)

This statement assumes the existence of that zero for its conditional
conclusion, NOT RH, a Mertens power saving, or the parent's growth-limit
upper theorem. For every right-of-line zero r=2 is admissible. In particular
any unbounded sequence of subexponential energies on [T,2T] would imply RH.

Use the SAME test from Section1, now with lambda=alpha+i gamma. Choose

    1/beta<a<b<r.

Since beta<1 for a nontrivial zero, a>1 as required. For s<=T the left
polynomial cancels the first m Laplace moments of d at lambda. The complete
leakage bound, using ONLY |h(s)|<=exp(s/2), is

    |h(s)v_(T,lambda)(s)|
       <=C(1+T)^C exp(-beta a T+s).

Indeed the d-kernel contributes exp(-beta(aT-s)), the factor outside its
integral contributes exp(-alpha s), and h contributes at most exp(s/2).
Their s exponent is beta-alpha+1/2=1. Therefore the entire early-source
integral is O((1+T)^C exp(-(beta a-1)T))=o(1). The buffer condition is
beta a>1, not an unproved smallness assumption on the native source.
Fubini still gives the nonzero right side G(lambda)+o(1)=1/rho^2+o(1).

For the remaining adjoint norm use the integral Taylor remainder from
Section1.3, with absolute moments rather than a boundary limit. Define

    J_m(beta)=beta^(-m-1)+(m+1)beta^(-m-2).

The bound (0.2) implies

    (1/m!) integral_0^infinity u^m |d(u)|exp(-alpha u)du
       <=J_m(beta).

Minkowski and the integral remainder give

    ||V_(T,lambda)||_(L2(R))
       <=T^(1/2-m) J_m(beta)||psi^(m)||_2.

On s>=T the additional exp(-lambda s) has modulus at most exp(-alpha T).
Thus Cauchy--Schwarz, once the nonzero pairing is at least 1/(2|rho|^2),
proves (2.1) with

    c(r,rho,m)=1/[4 |rho|^4 J_m(beta)^2 ||psi^(m)||_2^2].   (2.2)

Choose any displayed rational a,b between 1/beta and r to evaluate the
constant from (1.5); for non-effectively given rho the formula is an analytic
constant rather than a claimed numerical certificate. No subtraction of
cumulative liminf bounds or assertion of regular variation is used.

### 2.2 The unchanged crossing covariance, with its full diagonal

Use EXACTLY the source of XCC26. At a crossing Y, retain c_n=mu(n) through Y,
c_(2Y)=-2Y m(Y), and z=c*c. Put B=(Y+1)^2-1 and

    K_d(k)=[H_floor(k/d)-H_k+log d]/d,
    D_Y=sum_d z(d)^2 sum_(k=Y+1)^B K_d(k)^2,
    C_Y=sum_(d!=e) z(d)z(e) sum_(k=Y+1)^B K_d(k)K_e(k).

For completeness, the required native identities have elementary proofs.
Crossing gives |m(Y)|<=1/Y, coefficient cap two and P_c(1)=0. If
e=delta-1*c, then mu-(2c-1*c*c)=mu*e*e and e vanishes below Y+1. Hence
the Newton output is mu through B. Its reciprocal sum is 2m_c-Q, where
Q=sum_d z(d)K_d; the centering terms cancel by P_c(1)^2 and its derivative.
Squaring on the complete annulus gives

    C_Y=F_B-F_Y-D_Y+R_Y,
    R_Y=4(Y-1)m(Y)^2-4m(Y)sum_(k=Y+1)^(2Y-1)m(k),
    |R_Y|<4.                                                (2.3)

This collar identity is CREDITED to #869. Products above B remain in D_Y.
To recall the whole-packet bound, put r(x)=H_floor(x)-log x-gamma. Harmonic
integral bounds give |r(x)|<=1/x for x>=1 and |r(x)|<=log(1/x)+1 below1.
The small-argument decreasing integral is 5d, and the remaining reciprocal-
square sum is at most 2d. Thus sum_k r(k/d)^2<=7d and sum_k r(k)^2<=2.
Since d K_d(k)=r(k/d)-r(k), sum_k K_d(k)^2<=18/d. Coefficient cap two gives
|z(d)|<=4 tau_2(d); the prime-power inequality tau_2^2<=tau_4 and the four
harmonic sums yield the complete bound

    D_Y<=288 H_(4Y^2)^4=O(log^4 Y).                         (2.4)

These are the preceding construction's credited bounds, rederived rather
than claimed as new estimates.

### 2.3 RBR26-2: the strong covariance target restricts multiplicity too

If C_Y<=K D_Y for a fixed K>=0 on an unbounded sequence of native crossings,
then RH holds AND every nontrivial zero has multiplicity at most TWO.

Indeed (2.3)--(2.4) give F_B-F_Y=O(log^4 Y) along that sequence. RBR26-8
excludes every right-of-line zero directly, without using the proposed XCC26
upper exponent. Reflection gives RH. If now a critical zero had multiplicity
m>=3, RBR26-1 would force F_B-F_Y>=c(log(Y+1))^(2m-1) for every large Y,
a contradiction. Equivalently, conditional on such a multiple zero and RH,
C_Y-KD_Y is eventually positive for each fixed K.

More generally, an eventual annular energy budget O(log^A Y) excludes zeros
with 2m-1>A once RH holds. No actual multiple zero is asserted, and we do NOT
prove logical non-equivalence of RH and the strong sign target. The precise
conclusion is its extra multiplicity ceiling. The weaker subpower target
imposes no fixed multiplicity ceiling. None of the finite native signs is
refuted by this argument.

## 3. RBR26-3: a causal resonance filter with an exact full-energy ledger

Let a>0 and omega real. On a causal L2 input f define

    x'(t)=(-a+i omega)x(t)+f(t), x(0)=0,
    N_(a,omega) f=f-a x.

Its Laplace multiplier is

    N_(a,omega)(z)=(z-i omega)/(z+a-i omega).                 (3.1)

This is a bounded causal operator (identity plus a stable L1 kernel) with
norm at most one. There is no zero in Re z>0, although the multiplier has a
zero at i omega on the boundary. EXACTLY,

    ||f||_2^2=||Nf||_2^2+a^2||x||_2^2.                     (3.2)

Indeed |f|^2-|Nf|^2=a(d/dt)|x|^2+a^2|x|^2. A stable L2 state is H1 and
vanishes at infinity; integrate from0 to infinity. For compactly supported
f with endpoint T, the explicit output tail is

    (Nf)(T+u)=-a exp((-a+i omega)u)x(T),
    integral_T^infinity |Nf|^2=a|x(T)|^2/2.                 (3.3)

Thus frequency rejection cannot be credited while forgetting its stored
terminal state. The removed energy also has the positive kernel expression

    a^2||x||^2=(a/2)int int f(s)conj(f(t))
                  exp(-a|s-t|)exp(-i omega(s-t)) ds dt.    (3.4)

For the exactly matched boundary wave f_T(t)=exp(i omega t) on[0,T],

    ||N_(a,omega) f_T||^2=(1-exp(-aT))/a <=1/a,

where the unfiltered norm is T. Both the pre-T transient and the post-T stored
state are included in this identity. A conjugate pair of factors similarly
bounds the whole output energy of a truncated real cosine by 1/a, by linearity,
commutation and contraction. These are all-T synthetic boundary-wave results,
not actual Mobius estimates. They demonstrate that boundary oscillation can
be removed while the exponential detector of Section4 is retained.

For a finite cascade W=N_L...N_1, every stage acts on the ACTUAL output of the
previous one, and

    ||f||^2-||Wf||^2=sum_(j=1)^L a_j^2||x_j||^2.            (3.5)

No stage is restarted from the original input, and no independence assumption
is made. Pairing (+omega,-omega) with equal widths gives a real filter on real
inputs; complex filters are also admissible.

### A finite-dimensional exact accounting of the entire cascade tail

Let x=(x_1,...,x_L)^T, b=(1,...,1)^T, c=(a_1,...,a_L)^T. Then

    x'=A x+b f,
    A_jj=-a_j+i omega_j, A_jk=-a_k for k<j, A_jk=0 for k>j,
    Wf=f-c^T x.

A is Hurwitz. After a compact input ends at T,

    tail energy=x(T)^* P x(T),
    A^*P+PA=-cc^T,
    P=int_0^infinity exp(A^*u)cc^T exp(Au)du.               (3.6)

It is the UNIQUE Hermitian solution. It is positive semidefinite and bounded
above by S=diag(a_j), because

    A^*S+SA= -cc^T-diag(a_j^2).                            (3.7)

All coincidences of poles are permitted by (3.6); no diagonalization or
simple-pole assumption is needed. For rational a_j,omega_j, the finite
Lyapunov system has Gaussian-rational coefficients and an exact solution.
The classical control identities are not claimed novel. Their use here is
an auditable all-future native-energy computation, not an unstable backward
filter or an unpriced spectral modification.

## 4. RBR26-4: a width budget prevents hiding off-line zeros

For any lambda=alpha+i beta with alpha>0, (3.1) gives

    |N_(a,omega)(lambda)|
       >=exp(-a/|lambda-i omega|)>=exp(-a/alpha).

For ANY finite cascade, with total width A(W)=sum_j a_j,

    exp(-A(W)/alpha)<=|W(lambda)|<=1.                      (4.1)

The lower bound is uniform in the number of factors, all their real
frequencies, repeated factors and a data-dependent choice of parameters.
Width is summed over EVERY scalar factor; a conjugate pair contributes twice
its individual width. There is no upper-half-plane zero hidden in a filter.

Take any unbounded sequence of integers Y, T=log(Y+1), and independently
chosen finite cascades W_Y such that A(W_Y)=o(T). Define the ACTUAL whole energy

    R_Y(W)=||W_Y h_T||_2^2.                                (4.2)

Every R_Y is finite by contraction. Causality and (0.3) imply

    d*(W_Y h_T)=W_Y g before T.

At any hypothetical zeta zero rho=1/2+alpha+i beta with alpha>0, the transform
of the left side vanishes. The transform of W_Y g is W_Y(lambda)/rho^2, nonzero.
Cauchy--Schwarz on the COMPLETE delayed difference therefore gives

    6 sqrt(R_Y)+sqrt2
       >= sqrt(2alpha)/|rho|^2
                  * exp(alpha T-A(W_Y)/alpha).              (4.3)

The changing target W_Y g is not assumed fixed: its norm is <=sqrt2, and its
value at EACH fixed hypothetical zero is explicitly retained by (4.1).
Hence an unbounded subpower filtered-energy sequence

    log(1+R_Y)/log(Y+1) ->0                                 (4.4)

with A(W_Y)=o(log Y) implies RH. The converse follows from RH -> F_Y=Y^o(1)
and R_Y<=F_Y, for ANY such filter family. Thus (4.4) is an RH-equivalent
criterion with no added finite multiplicity ceiling.

Using the parent's true native exponent, one obtains the stronger robust
identity, for ANY choices with this width budget,

    lim log(1+R_Y)/log(Y+1)=2Theta-1.                       (4.5)

For this optional exponent statement only, the XCC26-1 upper-exponent theorem
is a pinned proposed dependency. The lower half follows directly from (4.3)
for each fixed off-line zero. When Theta=1/2, nonnegativity and R<=F suffice.
When Theta=1 the parent bound F<=Y and the same lower limit handle the endpoint.
There is no claim of uniformity in a zero moving with Y.

This result does NOT estimate R_Y from above at the required subpower scale.
It gives freedom to remove critical resonances while ensuring that successful
small energy cannot be an artifact of suppressing the unknown zero detector.

## 5. RBR26-5: a concrete finite search, and why the full proof is still missing

A fully predeclared family is available. Put L=max(1,floor(log_2(Y+1))).
Use L conjugate pairs, every scalar width 1/(2L), with frequencies selected,
with repetitions allowed, from {j/L:0<=j<=L^2}. Then total width is exactly1.
There are finitely many choices. Their entire energy is determined by the
native prefix, elementary cell integrals and (3.6); no future Mobius values
or zero-location oracle enter the definition. Exact comparison of equal computable real energies is NOT assumed decidable.
Instead enclose each energy to interval width at most one and select the
smallest upper endpoint. This terminates on the finite family and gives an
actual filter whose energy is at most one above the finite minimum.

Let R_Y^min be the infimum (a minimum for this finite family) of those whole
energies. The proof in Section4 is uniform over every tuple, so

    R_Y^min subpower on an unbounded sequence => RH.

Conversely RH gives subpower R_Y^min. A near-minimizer found by a terminating
finite search also satisfies (4.3). This is a COMPLETE ALGORITHM DEFINITION,
not a proved success estimate. No assertion of efficient enumeration, new
all-Y cancellation or numerical minimization of this full grid is made.

The exact ledger (3.5) turns the desired estimate into native resonant energy
capture. A future proof must show that the chosen cascades remove all but
exp(o(T)) energy while their width sum stays o(T). Generic L2 contraction
only gives R_Y<=F_Y and does not achieve this. A fixed positive energy
reduction, a frequency fit on a window, or deletion of the cascade tail cannot
be iterated into a full proof.

### A precise obstruction to pretending that the filters force success

For any alpha>0 let f_T(t)=exp(alpha t) on[0,T], zero otherwise. On the
Fourier boundary its transform satisfies

    |Lf_T(iu)| >= (exp(alpha T)-1)/sqrt(alpha^2+u^2).

Plancherel and the Hardy evaluation bound applied to W(z)/(z+alpha) give

    ||W f_T||_2^2 >= (exp(alpha T)-1)^2
                     * ||W(z)/(z+alpha)||_(H2)^2
                  >= (exp(alpha T)-1)^2 |W(alpha)|^2/(2alpha)
                  >= (exp(alpha T)-1)^2 exp(-2A(W)/alpha)/(2alpha). (5.0)

Thus ANY data-adaptive family of width o(T) retains exponential energy on
this ordinary nonnative input. This uses its whole Fourier line and the
complete stable tail, not just a boundary value. It is not a Mobius example,
but it rules out proving native capture from L2 passivity alone.

For an elementary exact failure of generic contraction-to-zero, consider the
single factor N_(a,omega) on the infinite L2 input f(t)=exp(-bt), b>0. Its whole
output energy is

    ||N f||^2 = [b(b+a)+omega^2]/[2b((b+a)^2+omega^2)].       (5.1)

It is strictly positive for all finite a,omega and tends to the unchanged
input energy as |omega| tends to infinity. Cascading factors does not permit
raising one sample reduction to a power without passing the actual output.
No universal nonlinear success rule follows from these elementary examples.

## 6. RBR26-7: compile away the terminal state without erasing its cost

The stored tail in (3.6) need not be an irreducible penalty. There is an EXACT
infimum theorem in the new, explicitly different metric.

Fix a finite cascade W, an arbitrary causal L2 prefix f on[0,T], and let

    I_T(W,f)=integral_0^T |W(f1_[0,T])(t)|^2 dt.

Among ALL compactly supported L2 continuations f_ext agreeing with f before T,

    inf ||W f_ext||_2^2 = I_T(W,f).                         (6.1)

A constructive continuation gives a complete excess at most K(W,x(T))/R for
any R>=1. It is supported through T+2R. The finite constant is explicitly determined by
the cascade and its actual terminal state. The numerical recipe is effective
for rational filter parameters and effectively given state enclosures, in
particular for the native finite prefix used here. Finite attainment is NOT asserted.
The pre-filter input norm can grow polynomially in R and is NOT claimed small.
What is bounded is the actual post-filter source norm used in (4.3).

This does not contradict the earlier minimum E_Y or the #875 unfiltered
completion-price theorem: both of those optimize a DIFFERENT, unfiltered
metric. The new convolution input is W f_ext; the target is W g, whose fixed
interior values are paid by (4.1). No bounded inverse for W is assumed.

The empty cascade is the identity, for which zero extension already attains
the infimum. Assume at least one factor for the remaining construction.

### 6.1 Exact zero-output continuation

In the state realization (3.6), impose f_ext=c^T x after T. Then the output
is zero and

    x'(T+u)=Z x(T+u),   Z=A+bc^T.

Z is UPPER triangular: its diagonal is i omega_j, its entry (j,k), k>j,
is a_k, and its lower entries are zero. Thus the formally uncut tail

    f_zero(u)=c^T exp(Zu)x(T), u>=0,

is an explicit finite sum of exp(i omega u) p_omega(u), with

    deg p_omega <= m_omega-1,

where m_omega is the number of occurrences of that frequency in the filter.
It is generally not L2, so it is NOT used as an admissible final input.
For u>0 it is annihilated by

    P(partial_u)=product_j(partial_u-i omega_j).

This follows directly from Cayley--Hamilton for the finite Z matrix.

### 6.2 A finite taper with a complete tail budget

Let L be the number of scalar factors. Define chi(v)=1 for v<=1, chi(v)=0
for v>=2, and for 0<=w<=1 set

    chi(1+w)=1-[integral_0^w t^L(1-t)^L dt]/B(L+1,L+1).

It is C^L, piecewise polynomial, and all derivatives of orders1,...,L vanish
at both joins. Use the ADMISSIBLE compact continuation

    f_ext(T+u)=chi(u/R) f_zero(u), u>=0.                    (6.2)

Until u=R its filtered output is exactly zero. Write

    Q(z)=product_j(z+a_j-i omega_j),  W=P/Q.

Relative to the uncut zero-output continuation, the error source is
(chi(u/R)-1)f_zero(u), zero before R. Applying P(partial_u) to this difference
gives an ordinary compactly supported function r_R on[R,2R]; there are no
Dirac terms, because the join derivatives through order L-1 match. Its output
is the causal convolution Q(partial_u)^(-1) r_R.

Here is the uniform power count, INCLUDING repeated frequencies. For one mode
exp(i omega u)p(u) with degree d<=m_omega-1, expand

    P(partial_u)[exp(i omega u)chi(u/R)p(u)]
       =exp(i omega u) sum_l q_(omega,l)
                             partial_u^(m_omega+l)[chi(u/R)p(u)].

In every nonzero Leibniz term at least one derivative falls on chi. On
u=Rv in[R,2R], each term has scale R^(d-m_omega-l), at most R^-1.
All remaining polynomial coefficients and derivatives of chi are bounded on
1<=v<=2. Therefore an explicit finite C(W,x(T)) satisfies

    |r_R(u)|<=C/R,   ||r_R||_2^2<=C^2/R.                   (6.3)

For example compute C by expanding those finitely many polynomials, taking
absolute coefficient sums on[1,2], and summing over modes and derivative
orders. For rational filter parameters this is an algorithmic upper constant from
state enclosures, not merely an asymptotic existence assertion.
No unknown future Mobius coefficient enters it.

The stable inverse Q^-1 is the convolution of exp((-a_j+i omega_j)u)1_(u>=0),
so its L1 norm is at most product_j a_j^-1. Young's inequality pays the ENTIRE
output after T+R, including its unbounded exponential tail:

    0<=||W f_ext||^2-I_T(W,f)
           <= (product_j a_j^-2) C^2/R.                   (6.4)

Taking R arbitrarily large proves (6.1); causality gives the opposite bound.
For effectively given data and any prescribed rational epsilon>0, a rational
upper bound on C supplies a finite sufficient integer R. Exact equality comparisons of computable
constants are unnecessary. Prefix discontinuities at integer-log cells cause
no issue: the initial filter states are computed from L2 input, and the
comparison difference is zero on a neighborhood of the new taper joins.

### 6.3 A new native target, with no numerically omitted future

Set f=h on[0,T], T=log(Y+1), and put

    I_Y(W)=integral_0^T |W h(t)|^2 dt.                      (6.5)

For each compact continuation (6.2), causality still gives

    d*(W f_ext)=W g before T.

Thus (4.3) holds with ||W f_ext|| in place of ||W h_T||. Let R tend to infinity
at this FIXED Y and FIXED finite W, using (6.4). The exact lower detector is

    6sqrt(I_Y(W))+sqrt2
       >=sqrt(2alpha)/|rho|^2
                   *exp(alpha T-A(W)/alpha).              (6.6)

There is no exchange of a growing-Y limit with an uncontrolled completion.
For each Y the finite R can instead be chosen to make the excess <=1.
The original norm at finite R, not the non-L2 zero-dynamics input, is then the
actual legitimate witness in the complete RH argument.

The finite-time passive ledger is also exact:

    I_Y(W)=F_Y-sum_j[a_j|x_j(T)|^2
                         +a_j^2 integral_0^T |x_j(t)|^2dt]. (6.5a)

Every x_j is driven by the ACTUAL preceding stage. This follows by integrating
the differential identity behind (3.2) up to T and telescoping. The positive
terminal-state subtraction cannot be credited for zero extension without
adding its emitted tail; (6.2)--(6.4), not deletion of a tail, justify the
prefix-only infimum. Thus the remaining target is a specific positive native
state-energy capture estimate, not a termwise-negative covariance assertion.

Consequently, with A(W_Y)=o(log Y), an unbounded subpower sequence of these
FINITE-TIME filtered prefix energies implies RH. Under RH it follows from
I_Y(W)<=||W h_T||^2<=F_Y, so the converse holds too. The optional robust
exponent (4.5) holds for I_Y as well, under the same pinned exponent premise.

This is the positive completion result of the pass: the finite prefix energy
is an admissible target because an explicit finite source compiles its entire
future within any specified excess. The native upper bound is STILL OPEN.
The large unfiltered continuation norm and possibly enormous R are disclosed;
they do not enter the correctly retained detector or disappear from a theorem
that charged them. No covariance number from the older unfiltered construction
is reused as this new filtered energy.

### 6.4 The prefix-only objective still cannot erase arbitrary exponential growth

The stronger completion freedom does not make the new upper target automatic.
For f(t)=exp(alpha t), alpha>0, and any finite filter W, let I_T denote its
filtered prefix energy as above. Then

    I_T >= [exp(alpha T-A(W)/alpha)-1]_+^2/(2alpha).         (6.7)

To prove this without any parameter-uniform transient approximation, use the
stable all-pass operator

    B_alpha(z)=(z-alpha)/(z+alpha),
    B_alpha f=exp(-alpha t).

It is a norm-one L2 multiplier (identity minus a stable exponential kernel),
and it has a zero at the TEST point alpha. Every finite continuation from
Section6.2 therefore has B_alpha W f_ext=W exp(-alpha t) before T. Hardy
Cauchy--Schwarz at alpha gives

    ||W f_ext||+1/sqrt(2alpha)
           >=exp(alpha T)|W(alpha)|/sqrt(2alpha).

Take the fixed-filter completion infimum, then apply (4.1). This proves (6.7)
for arbitrary filter count, repeated frequencies and adaptively chosen widths.
Thus A(W_T)=o(T) retains positive exponential rate even for the optimized full
future. This synthetic identity is not a zero or a property of zeta. It keeps
the remaining native upper bound from being replaced by a general filtering
or finite-time approximation claim.

### 6.5 RBR26-9: a commuting bridge to the concurrently published prime dephasing

During preparation, PR848 advanced to `9ddd3dd029d9191cf409bc944132569630361a6f`
with PPD26. Its finite-prime Euler comparison and character dephasing are
CREDITED, not claimed as discoveries here. Its native metric is E, not the
F/prefix-filter metric of this packet. The following bridge is rederived on
our actual coordinates; no old energy numbers are transferred.

Let S be a finite prime bank and epsilon_p in{+1,-1}. Put

    a_epsilon(n)=mu(n)chi_epsilon(n),
    h_epsilon(t)=exp(t/2)sum_(n<=exp t)a_epsilon(n)/n,
    B_S=product_(p in S)(1+p^(-1/2))/(1-p^(-1/2)).

Here chi is completely multiplicative, equal to epsilon on S and one on other
primes. Its Euler quotient relative to mu is

    R_epsilon(s)=product_(p in S)(1-epsilon_p p^-s)/(1-p^-s).

Multiplication by d^-s acts as U_d f=d^(-1/2)f(t-log d), causal at zero.
At p^j, j>=1, the quotient coefficient is 1-epsilon_p and its inverse
coefficient is (epsilon_p-1)epsilon_p^(j-1). Their absolute operator series
are each at most B_S, on the whole half-line and on every initial interval.
Dirichlet convolution proves h_epsilon=R_epsilon h locally. These causal
operators COMMUTE with W, including after restriction to an initial interval:
no value after T can influence the output before T. Therefore

    B_S^-2 I_Y(W) <= I_Y^epsilon(W) <= B_S^2 I_Y(W),
    I_Y^epsilon(W)=integral_0^T |W h_epsilon|^2 dt.          (6.8)

Both inequalities concern the ACTUAL filtered outputs, not fresh input norms.
They hold uniformly over every signature, even one selected from the data.
No factor 2^|S| is incurred. The finite taper theorem applies to h_epsilon too;
its completed output may be mapped back by R_epsilon^-1 at norm cost at most
B_S if a literal native convolution witness is required.

For a common filter W used in the finite character average, define h_rough
by omitting integers divisible by any prime in S, and let I_rough(U,W) be its
filtered energy through time U, zero for U<=0. Finite-group Parseval gives
EXACTLY

    2^-|S| sum_epsilon I_Y^epsilon(W)
       =sum_(d|product S, d<exp T) I_rough(T-log d,W)/d.    (6.9)

The different cutoff at each d is retained, and the SAME W acts in every
summand. If W itself is selected separately for each signature, (6.8) still
holds but the common-filter Parseval identity (6.9) is NOT asserted.

The proposed growing-bank conclusion of PPD26 has a short elementary check.
Chebyshev's binomial argument gives vartheta(y)<=3y, hence
sum_(p<=y)(log p)/sqrt(p)<=6sqrt(y). Splitting at sqrt(y), enlarging the
smaller primes to integers, gives sum_(p<=y)p^-1/2<=14sqrt(y)/log y for
y>=exp(16). Since log((1+x)/(1-x))<=4x at x=p^-1/2,

    log B_S<=56sqrt(y)/log y.

In particular S contained in primes <=4T^2 has log B_S<=56T/log T for
T>=exp(8). These are deliberately conservative asymptotic thresholds, not a
new prime-counting theorem or a computation at that size.

Thus ANY selected signature, a finite signature minimum, or the common-filter
average, combined with A(W)=o(T), has a valid subpower-to-RH implication.
Under RH the reverse subpower statement follows from (6.8), contraction and
F_Y=exp(o(T)). The selection may use exponentially many candidates; its cost
is not being declared efficient. The unresolved upper bound is the residual
rough-source correlation or filtered resonant energy, not transfer back to
the principal Mobius member. Neither prime dephasing nor causal filtering has
proved that remaining native capture estimate.

## 7. RBR26-6: exact tests, synthetic sharpness and native whole-norm controls

For m>=1, a>0 and omega>0, use the SYNTHETIC stable source

    D(z)=(z^2+omega^2)^m/(z+a)^(2m+1),
    G(z)=1/(z+a)^(2m+1), H(z)=1/(z^2+omega^2)^m.

Its d and g are exponential-polynomial causal functions. Its h has only the
two boundary poles +/-i omega, order m, and polynomial growth. Partial fractions
show that its leading time terms are

    t^(m-1)/(m-1)! * [exp(i omega t)/(2i omega)^m
                     +exp(-i omega t)/(-2i omega)^m].

Thus its exact leading annular energy is

    [2(r^(2m-1)-1)/((2m-1)((m-1)!)^2(2omega)^(2m))]
                                                    *T^(2m-1).

This attains (1.1)'s two-resonance constant in the general convolution theorem.
These are NOT actual zeta zeros or substituted Mobius coefficients.

A distinct native control uses omega=0,a=1/2 on the literal compact h_T.
For log k<=t<log(k+1), the state is exactly

    x(t)=exp(t/2)m(k)-exp(-t/2)M(k).

Its terminal square is (b m(Y)-M(Y))^2/b. Direct integration of y=h_T-x/2
AND its tail, compared with the loss identity, gives

    ||N_(1/2,0) h_T||^2 = [F_Y+S_Y]/2,
    S_Y=sum_(k<=Y)m(k)M(k)log((k+1)/k).                    (7.1)

Both derivations use the complete terminal tail |x(T)|^2/4. This zero-frequency
control does not claim to remove any actual critical zeta resonance. Exact
rational log enclosures suffice to reproduce (7.1), without a zeta evaluator,
numerical ODE, zero table or floating quadrature.

The finite checker verifies polynomial moments and minimizing tests, synthetic
partial fractions and sharp constants, rational stable-cascade energy and
Lyapunov identities, and a declared set of native panels. It cannot prove the
analytic approximate-identity limit, the RH-conditional leakage estimate,
all-scale native capture, or RH. Those boundaries are retained in the results
schema, source lock and validation receipt.

## 8. Result of the end-to-end attempt

The proposed strong covariance sign carries an extra multiplicity consequence.
The budgeted filter alternative is source-faithful, causal, and does not impose
that consequence. It allows arbitrarily many adaptively selected boundary
notches while keeping a provable exponential lower detector for EVERY fixed
off-line zero. The full future and changing target are paid explicitly. The new taper
compiler even attains the prefix-only post-filter infimum asymptotically,
without using its non-L2 zero-output continuation as a final source.

**Still OPEN:** prove native subpower filtered energy, or the earlier subpower
covariance bound. Neither the annular lower theorem nor passivity supplies it.
There is no completed RH proof awaiting a routine final numerical check.
