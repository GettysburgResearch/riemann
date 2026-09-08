# CCT26 — Critical finite energy and a horizon-preserving cutoff taper

Status: PROPOSED COMPONENT PROOFS; independent mathematical review pending.
This is NOT an unconditional RH proof. The all-scale mean-square hypothesis
used below is explicitly RH-conditional. The unsuccessful attempt to remove
it is in ATTEMPT.md. Date: 2026-09-08. Author: Astra.

Parent freeze: PR811 at 946dedfa3f6ec2d74f3f0f00f9ca511abf9652d7.
The cutoff taper is new to this packet. Classical Cramer mean-square and
Hardy-space results are credited, not claimed as new arithmetic estimates.

## 1. Literal source, measure, and the endpoint that must not be dropped

All primes are ordinary primes. Put a=log 2, and for x>=2 let

    R(x)=sum_(p<=x) sqrt(p)-integral_2^x sqrt(u)/log(u) du,
    v(t)=exp(-t)R(exp t) for t>=a, and v(t)=0 for t<a.

At a prime the full right-continuous jump is included. Isolated values do
not affect the Lebesgue integrals. Define the possibly infinite quantity

    J=integral_2^infinity R(x)^2/x^3 dx = ||v||_2^2.       (1)

For a finite real X>=2, L=log X, retain

    C_X(y)=sum_(p<=X)p^(-1/2-iy)
                 -integral_2^X x^(-1/2-iy)/log x dx,
    dmu(y)=dy/[pi(1+y^2)].                              (2)

The compact signed measure behind C_X is

    nu_X=sum_(p<=X)p^-1/2 delta_(log p)
                     -exp(t/2)/t 1_[a,L](t)dt.

Let k(t)=exp(-t)1_(t>=0). Its convolution with nu_X is exactly

    v^L(t)=v(t)                     (t<=L),
           exp(-(t-L))v(L)          (t>L).              (3)

Thus C_X=(1+iy) Fourier(v^L), with Fourier(f)(y)=integral exp(-iyt)f(t)dt.
Plancherel, with norm dy/(2pi), proves

    ||C_X||_(2,mu)^2=2||v^L||_2^2
       =2 integral_2^X R(x)^2/x^3 dx + R(X)^2/X^2.      (4)

This is the parent's one-state identity, reconstructed directly. In
particular J<infinity does NOT permit dropping the last term in (4), or
asserting pointwise v(L)->0. A spike can have small L2 mass but a large value.
No such pointwise assertion is used here.

## 2. The explicit logarithmic cutoff average

For every X>=2 define

    Cbar_X(y)=integral_0^1 C_(X exp u)(y)du.             (5)

Equivalently this is the finite first-prime sum and the full continuum
integral with identical weight

    w_X(x)=1                              (2<=x<=X),
           1-log(x/X)                     (X<x<eX),
           0                              (x>=eX):

    Cbar_X(y)=sum_(p<=eX)w_X(p)p^(-1/2-iy)
                     -integral_2^(eX)w_X(x)x^(-1/2-iy)/log x dx.
                                                               (6)

The value at p=X is one, the value at p=eX is zero, and all cross terms use
the same weights. The interval width is fixed (one in logarithmic time).
This is NOT the old sharp cutoff and is not silently substituted for it.
The averaged state vbar_L=integral_0^1 v^(L+u)du equals v before L. Afterwards,
with q=t-L, it is

    vbar_L(t)=(1-q)v(t)+integral_0^q exp(-(q-u))v(L+u)du, 0<q<1,
    vbar_L(t)=exp(-q)integral_0^1 exp(u)v(L+u)du,         q>=1.
                                                               (7)

Every finite averaged state is in L2. Its full future in (7) is retained.
The corresponding norm is exactly

    ||Cbar_X||_(2,mu)^2=2||vbar_L||_2^2.                 (8)

**Theorem CCT26.T1 (endpoint-safe approximation).** IF J<infinity, set
C_infinity(y)=(1+iy) Fourier(v)(y) in L2(mu). Then, for every X>=2,

    ||Cbar_X-C_infinity||_(2,mu)^2
                        <=6 integral_L^infinity |v(t)|^2dt.    (9)

Proof. For almost every T, (3) and (r-s)^2<=2r^2+2s^2 give

    ||v^T-v||_2^2 <= |v(T)|^2+2 integral_T^infinity |v|^2.

Jensen's inequality for the average in u in [0,1] yields

    ||vbar_L-v||_2^2
      <=integral_L^(L+1)|v|^2+2 integral_L^infinity |v|^2
      <=3 integral_L^infinity |v|^2.

Equations (8) and Plancherel prove (9). This proves the complete frequency
norm, not merely convergence on compact frequency intervals. Local boundedness
of v makes all finite Bochner averages legitimate. J<infinity is a hypothesis.

Conversely, if ||Cbar_(X_j)||_2 is bounded for any X_j->infinity, then the
identity vbar_(log X_j)=v before log X_j and (8) give

    2 integral_a^(log X_j)|v|^2 <= ||Cbar_(X_j)||_2^2.

Monotone convergence proves J<infinity. No conditioning bound, matrix inverse,
zero data, or unknown optimizing coefficients are involved.

## 3. Finite energy implies RH: construct the logarithm, do not assume it

**Theorem CCT26.T2.** J<infinity implies RH.

For Re s>1/2 define the analytic function

    C(s)=(s+1/2) integral_a^infinity
                            exp(-(s-1/2)t)v(t)dt.               (10)

Cauchy--Schwarz on compact subsets justifies analyticity. On Re s>1, ordinary
absolute convergence and integration by parts give

    C(s)=sum_p p^-s-integral_2^infinity x^-s/log x dx.            (11)

There is no lower endpoint term: R(2-)=0. Prime 2 is already its full jump.
Let

    B(s)=-gamma-log(a)+Ein((s-1)a)-2log s,
    V(s)=sum_p sum_(k>=2)p^(-ks)/k,
    G(s)=B(s)+C(s)+V(s).                                       (12)

Here Ein is the entire function sum_(k>=1)(-1)^(k+1)z^k/(k k!), and log s
is its ordinary right-half-plane branch. V converges absolutely locally
uniformly on Re s>1/2. Thus G is analytic there. In the Euler half-plane,
use E1(z)=Ein(z)-gamma-log z and
integral_2^infinity x^-s/log x dx=E1((s-1)a), to obtain

    exp(G(s))=(s-1)zeta(s)/s^2.                                (13)

Analytic uniqueness extends this identity to Re s>1/2. Its left side has
no zero; the zeta pole at 1 is removable in the right side with value 1.
The functional equation then excludes left-of-line nontrivial zeros too.
This proves the implication with full multiplicity and no choice of log zeta
across an unknown zero. The missing assertion is J<infinity itself.

## 4. The actual available mean-square input is conditional

We import ONLY the following classical implication, denoted CM:

    RH => there exists K>0 such that, for all Y>=2,
        integral_Y^(2Y) |psi(x)-x|^2 dx <= K Y^2,                (CM)
    psi(x)=sum_(n<=x) Lambda_VM(n).

Cramer proved the qualitative upper bound; Brent--Platt--Trudgian give a
quantitative refinement. Their paper explicitly assumes RH for the upper
bound. We do not import their numerical 0.8603 constant or replay their zero
calculations. Enlarging K covers compact Y. This is not deduced from ordinary
PNT or from its unconditional lower mean-square estimate.

**Theorem CCT26.T3 (conditional critical finite energy).** Assuming RH,
J<infinity. More quantitatively, for T>=2,

    integral_T^infinity |v(t)|^2dt <= K_v/T,
    K_v=28K_e+36, K_e=2(2K+1200).                              (14)

The constants are deliberately loose and depend on the imported CM constant.
They are not numerically certified RH-independent constants.

### Transfer from psi to the literal first-prime source

The elementary central-binomial argument gives theta(x)<3x, x>=2.
Indeed sum the log prime products in (2^(j-1),2^j] dividing the central
binomial coefficient, then place x between dyadic endpoints. Consequently

    0<=psi(x)-theta(x)
       =sum_(k>=2)theta(x^(1/k)) <=20sqrt x.                    (15)

For completeness, k=2 costs 3sqrt x; all k>=3 cost at most
3(log x/log2)x^(1/3). Since (log x)x^-1/6<=6/e, e>2 and log2>2/3,
this is below (27/2)sqrt x; 20 is ample.
By (CM), (15), and |r+s|^2<=2r^2+2s^2,

    integral_Y^(2Y)|theta(x)-x|^2dx <=(2K+1200)Y^2.              (16)

Put E(t)=exp(-t/2)[theta(exp t)-exp t]. Cover [exp T,exp(T+1)] by
[Y,2Y] and [2Y,4Y], using e<4, to get

    integral_T^(T+1)|E(t)|^2dt <= K_e,             T>=a.        (17)

Set z(t)=E(t)/t for t>=a, and zero before a. Summing length-one blocks gives

    ||z||_2^2 <=(15/4)K_e,
    integral_T^infinity |z(t)|^2dt <=2K_e/T,       T>=1.        (18)

These follow from sum_(j>=0)(T+j)^-2<=T^-2+T^-1 and a>2/3.

### Stable Volterra transfer and the complete tail

Stieltjes integration by parts at the lower endpoint 2- gives EXACTLY

    R(x)=sqrt x/log x [theta(x)-x]+2sqrt2/log2
                       -integral_2^x [theta(u)-u]d(sqrt u/log u).

In logarithmic coordinates this is

    v(t)=z(t)+c0 exp(-t)-[k*(q z)](t), t>=a,
    c0=2sqrt2/a, q(t)=1/2-1/t for t>=a.                       (19)

Extend all sources by zero below a; the c0 term also starts at a. Since
|q|<=1 and ||k||_1=1, (18) proves J<infinity. This is a signed identity;
the sign change of q is not discarded in the identity.

For the tail, split qz at T/2. The part from before T/2 has squared norm
on t>=T at most (1/4)exp(-T)||z||_2^2. The later part has global norm at
most (4K_e/T)^(1/2). Including the direct z and c0 terms gives

    ||1_[T,infinity) v||_2
      <=(sqrt2+2)sqrt(K_e/T)
               +exp(-T/2)[2/a+(1/2)sqrt(15K_e/4)].             (20)

Squaring, using 2(sqrt2+2)^2<24, T exp(-T)<1 for T>=2,
and a>2/3, proves (14). All time tails are included.

Combining Theorems T1--T3 gives the equivalences

    RH <=> J<infinity
       <=> liminf_(X->infinity) ||Cbar_X||_(2,mu)<infinity
       <=> Cbar_X converges in L2(mu).                        (21)

Moreover, UNDER RH,

    ||Cbar_X-C_infinity||_(2,mu) <=sqrt(6K_v/log X), X>=e^2.   (22)

This is a conditional strong-convergence theorem, not a new unconditional
prime-error estimate. The converse in Section 3 is independent of (CM).

## 5. The taper also produces zero-free full-domain Euler approximants

For Re s>0 use the parent's canonical analytic logarithm

    h_X(s)=log A_X(s),
    A_X(s)=exp(-gamma)exp(Ein((s-1)log X))
                     product_(p<=X)(1-p^-s)^(-1)/[(log X)s^2].

Define the geometric, NOT arithmetic, cutoff average

    hbar_X(s)=integral_0^1 h_(X exp u)(s)du,
    Abar_X(s)=exp(hbar_X(s)).                                (23)

All logarithms are real at positive s. This is explicit without zero data:

    hbar_X=B+Cbar_X+Vbar_X,
    Vbar_X(s)=sum_(p<=eX) w_X(p)sum_(k>=2)p^(-ks)/k.           (24)

In (24), Cbar_X(s) denotes (6) with s in place of 1/2+iy. Each prime BASE
has the same weight on all its powers. The entire initial normalization B
from (12) is not averaged away. The powers are defined by the canonical
local Euler logarithm; no arbitrary branch of a fractional power is used.

**Theorem CCT26.T4.** For every fixed X, Abar_X(1/2+z) is zero-free, bounded analytic, and in H2
on Re z>0. It is outer. Here is the needed proof rather than an appeal to
positivity of its coefficients (no such positivity is claimed).
For a fixed X, all cutoffs Xe^u lie in [X,eX]. On Re s>=1/2 the finite Euler
product is bounded uniformly in u. The standard horizontal representation

    E1(w)=exp(-w)integral_0^infinity exp(-t)/(w+t)dt, Im w!=0,

bounds |E1(w)| by exp(-Re w)/|Im w|. Together with
Ein(w)=gamma+log w+E1(w), this gives |A_(Xe^u)(s)|<=C_X/|s| uniformly
in u. The bounded-imaginary remainder follows by compactness and the
positive-real estimate. Geometric averaging preserves that bound.
Analytic nonvanishing continuation across each finite boundary point excludes
singular inner factors there. At positive real infinity Abar_X(s)~1/s,
excluding an exponential inner factor. Standard Hardy factorization now proves
outerness. Constants may depend strongly on X.

The causal inverse of Abar_X(1/2+z) agrees with the actual factorial source
before t=log X. To verify the horizon without relying on a boundary quotient,
work first on Re s>1. The difference hbar_X-h_X is the Laplace transform of
a signed measure supported at logarithmic locations >=log X: it consists of
the newly included prime powers and their exact continuum correction.
Expanding its exponential gives delta_0 plus convolution powers with supports
>=j log X; there are only finitely many on any compact interval. The same
argument compares h_X with the full Euler expression (12)-(13) in the initial
absolute half-plane. Laplace uniqueness proves the stated horizon locally.
This is a local source identity, not a global norm bound.

## 6. Conditional convergence of the COMPLETE complex logarithm and entropy

The higher-prime-power series V_X(1/2+iy) converges in L2(mu) unconditionally,
with the elementary bound retained from PDS26:

    ||V_infinity-V_X||_(2,mu)<=8/sqrt(log X)+4/sqrt X.          (25)

Its short proof is as follows. For the square harmonics over P<p<=Y the
exact norm is

    (1/4)sum p^-2 + (1/2)sum_(P<q<=Y)q^-3 sum_(P<p<q)p.

The elementary pi(x)<8x/log x and partial summation bound this by 64/log P,
uniformly in Y. Terms k>=3 have absolute tail at most 4/sqrt P. This proves
(25) by completeness, not an assumption about almost-orthogonal primes.
There is no pointwise convergence assertion at y=0. Averaging preserves the
bound in (25) with the smaller cutoff X.

The fixed complex B(1/2+iy) is in L2(mu). Its finite integral for Ein gives
|B|<=C(1+log(1+|y|)): split the sine/cosine integrals at 1/|y|, and use
|sin u|<=min(|u|,1), 1-cos u<=min(u^2/2,2). This bound controls both real and
imaginary parts with the chosen branch; log^2(1+|y|) is Cauchy integrable.

**Theorem CCT26.T5 (conditional on RH).** Theorem T3 and (25) give

    ||hbar_X(1/2+i.)-G_boundary||_(2,mu)
      <= [sqrt(6K_v)+8]/sqrt(log X)+4/sqrt X,   X>=e^2.       (26)

For precision, identify traces after dividing expressions at s=1/2+z by
z+1. Then C/(z+1) is the Laplace transform of v. B/(z+1) is H2 by its
logarithmic bound, and V/(z+1) is H2: the positive-coefficient Cauchy Gram
bound used in (25) only decreases under additional real damping. Thus the
limit G_boundary is the weighted Hardy boundary trace of the canonical
analytic log[(s-1)zeta(s)/s^2] from Re s>1/2. Identification is in that half-plane
by (10)--(13) and Hardy trace uniqueness, not by a branch choice at boundary
zeros. Such zeros have measure zero; their logarithmic singularities cause
no missing L2 mass. No simplicity or zero-derivative bound is used.

In particular, with

    Ebar(X)=integral log^+|Abar_X(1/2+iy)|dmu(y),
    E_*=integral log^+|(-1/2+iy)zeta(1/2+iy)/(1/2+iy)^2|dmu(y),

UNDER RH, |Ebar(X)-E_*| is bounded by the right side of (26). This uses the
1-Lipschitz positive-part map and ||.||_1<=||.||_2. It is not L2 convergence
of Abar_X itself: exponentiation is not continuous on L2 without extra control.

Conversely bounded Ebar along one unbounded sequence suffices for RH. The
outer logarithm has real value hbar_X(3/2) uniformly between -3 and 3.
Indeed A_X(3/2)=(2/9)exp(E1((log X)/2))Z_X(3/2), with
1<=Z_X(3/2)<3 and 0<E1((log X)/2)<2/log2<3; averaging preserves the bounds.
Its Poisson formula makes its full weighted boundary absolute integral at
most 2Ebar+3. The Schwarz derivative formula and integration along compact
paths from the real point 1 give locally uniform bounds on
hbar_X(1/2+z). Montel and its Euler-safe limit produce an analytic G with
exp G=(s-1)zeta(s)/s^2. Identity (13) again proves zero exclusion. Thus

    RH <=> liminf_(X->infinity) Ebar(X)<infinity.               (27)

The upper premise in (27) remains unproved unconditionally. Neither the
finite target integral E_* nor local horizon agreement bounds the sequence.

## 7. Review boundary

Unconditional: definitions, physical norm identities, endpoint-safe taper,
local horizon, outerness for each finite approximant, and implications from
finite energy/bounded cost to RH. Conditional on RH via classical CM:
finite total energy, rate (22), and the complete logarithmic/entropy limit.

The missing arithmetic estimate is still J<infinity, or an adequate weaker
subpower bound from the parent. Importing CM as unconditional would prove
nothing: it would simply assume an RH-strength assertion. The paper and
checker do not do so. No new unconditional zero-free region is claimed.
