# CCS26: exact root susceptibility and the sharp price of anchoring

Status: proposed complete COMPONENT proofs; independent review required.
RH, the full Weil sign, and the native coherent-energy upper bound are not proved.
Date: 2026-09-08. This is a separate synthesis of the prime-power graph work in
#825 and #826, not a replacement of either source or a review verdict.

## 1. The graph, two different constants, and the theorem

For a finite prime set P let S_P be its squarefree divisor box:

    S_P = {product_(p in F) p : F subset P},
    Z_P = sum_(n in S_P)1/n = product_(p in P)(1+1/p),
    pi_P(n)=1/(Z_P n).

Use the literal graph form from #790/#825/#826, specialized to this support:

    E_P(f)= (1/Z_P) sum_(p j in S_P) (log p)/(p j) |f(pj)-f(j)|^2.  (1)

There are no higher-power edges on a squarefree support. They have not been
dropped from a larger support. The factor 1/Z_P normalizes both the metric and
the energy, and therefore changes no Poincare constant. Complex scalar functions
are used below; the scalar constants also apply to Hilbert-valued functions.

Write mean(f)=sum pi_P(n)f(n). Define the CENTERED and ANCHORED constants by

    C_P = sup_(f nonconstant) ||f-mean(f)||_pi^2 / E_P(f),
    A_P = sup_(f nonconstant) ||f-f(1)||_pi^2 / E_P(f).          (2)

They are different quantities. Put

    nu_p=(1+1/p)log p,
    a(n)=sum_(p|n) nu_p,
    K_P=sum_(n in S_P,n>1) 1/[n a(n)].                         (3)

**CCS1 (exact finite theorem).** If P contains 2, then

    C_P=1/nu_2=2/(3log2),
    K_P <= A_P <= K_P+1/nu_2.                                (4)

More precisely, A_P is the unique real A>1/nu_2 satisfying

    sum_(n in S_P,n>1) 1/[n(A a(n)-1)] = 1.                  (5)

The finite Green quantity K_P is exactly

    K_P=integral_0^infinity
         [product_(p in P)(1+p^(-1)exp(-nu_p t))-1] dt.       (6)

No unknown zero occurs in any definition. The general Green-function,
rank-one resolvent and product-chain methods are classical; their use does not
constitute a spectral identification of this graph with xi.

**CCS2 (sharp all-prime anchoring scale).** Let P_y contain every prime <=y,
y>=2. Then, as y tends to infinity,

    K_(P_y) = (1/zeta(2)) log log y + O(1),
    A_(P_y) = (1/zeta(2)) log log y + O(1).                   (7)

Moreover A_(P_y)-K_(P_y)=O(1/K_(P_y)). Thus the O(log log P) anchored
inequality in #825 has the correct order, already on these finite boxes.
A rank-independent anchored constant on ALL divisor-closed supports is false.
The CENTERED constants on these same boxes are exactly 2/(3log2).
This neither proves nor refutes an absolute centered gap on arbitrary
nonrectangular divisor-closed sets or on the ordinary cutoffs {1,...,N}.

The proof below uses elementary squarefree counting and an elementary upper
Euler-product bound. PNT, Mertens' product asymptotic, RH, and zero data are not
inputs. The O(1) constants in (7) exist by the displayed estimates; no numerical
value of their optimal size is asserted.

## 2. Complete diagonalization, including normalization at the root

Identify S_P with its prime-subset cube. The p coordinate is present with
probability 1/(p+1), absent with probability p/(p+1). The two-state generator
of minus the Laplacian has birth rate (log p)/p and death rate log p.
Its nonconstant normalized real eigenfunction is

    chi_p(absent)=-1/sqrt(p),   chi_p(present)=sqrt(p),

with mean zero, squared norm one, and eigenvalue nu_p. Thus

    chi_F=product_(p in F)chi_p, F subset P,

is a complete orthonormal basis; its eigenvalue is sum_(p in F)nu_p. For
F empty it is the constant. For n=product_(p in F)p,

    |chi_F(1)|^2=1/n.                                       (8)

This is exact product-measure algebra on a BOX. It does not assert statistical
independence of primes in the physical prime-discrepancy problem.
The map p -> (1+1/p)log p is strictly increasing for p>=2: its derivative
is (p+1-log p)/p^2>0. Hence the centered gap is nu_2 when 2 is included.

For mean-zero f=sum_(F nonempty)c_F chi_F,

    ||f-f(1)||_pi^2=sum |c_F|^2+|sum c_F chi_F(1)|^2,
    E_P(f)=sum a(F)|c_F|^2.                                 (9)

Set y_F=sqrt(a(F))c_F and u_F=chi_F(1)/sqrt(a(F)). The optimal anchored
constant is the largest eigenvalue of

    diag(1/a(F)) + u u^*.                                   (10)

Its rank-one part has norm ||u||^2=K_P and its diagonal part has norm 1/nu_2.
This proves (4). Since the coordinate F={2} couples nontrivially to u, the
largest eigenvalue is strictly above 1/nu_2. Solving the rank-one eigenvalue
equation gives (5). Its left side is continuous, strictly decreasing from
infinity to zero on that interval, proving uniqueness.

Finally 1/a(F)=integral_0^infinity exp(-t a(F))dt. Expand the finite product
in (6) and integrate. No limit interchange over an infinite prime set is used.
One may equally call K_P the mean-zero Green evaluation at the empty subset.
The generator stays conservative; grounding the root is a DIFFERENT operator.

## 3. Elementary ingredients for the asymptotic

We supply the needed estimates rather than importing a prime-distribution result.
Let Lambda be ordinary von Mangoldt and Psi(x)=sum_(n<=x)Lambda(n). The central
binomial coefficient bounds the increase Psi(2r)-Psi(r) by 2r log2. Dyadic
summation, monotonicity and log2<3/4 give Psi(x)<3x for x>=1. The factorial
identity

    sum_(n<=x) Lambda(n) floor(x/n)=log(floor(x)!)

then implies

    sum_(n<=x)Lambda(n)/n <= log x+3.                        (11)

For z>=2 let Zgeom(z)=product_(p<=z)(1-1/p)^(-1). Normalize the absolutely
convergent harmonic mass of z-smooth integers to a probability measure. Its
mean logarithm is B(z)=sum_(p<=z)log p/(p-1). By (11) and convergence of
sum_(n>=2)log n/[n(n-1)],

    B(z)<=log z+C_0.

At least half the mass lies below exp(2B(z)), by Markov's inequality. Thus

    Zgeom(z)<=2[1+2B(z)]<=C_1 log(z+1).                     (12)

The full geometric exponent sum is retained. In particular Z_(P_y)<=C_1 log(y+1).

The squarefree identity mu(n)^2=sum_(d^2|n)mu(d) gives, by finite interchange,

    Qsf(x):=sum_(n<=x)mu(n)^2 = c_sf x+O(sqrt x),
    c_sf=sum_(d>=1)mu(d)/d^2=1/zeta(2).                     (13)

The error follows from at most sqrt x floor errors and
x sum_(d>sqrt x)d^-2=O(sqrt x). Absolute Euler convergence at 2 proves c_sf.
Partial summation of (13) therefore gives

    sum_(2<=n<=x) mu(n)^2/[n log n]
        = c_sf log log x+O(1).                             (14)

All uses of zeta in (12)-(14) are at real arguments >1, where its absolutely
convergent series and Euler product suffice. The value 1/zeta(2)=6/pi^2 is
classical and not necessary for the argument.

## 4. Proof of the sharp logarithmic coefficient

### Lower bound

All squarefree n<=y occur in S_(P_y). For squarefree n>=3 write

    a(n)=log n+b(n), b(n)=sum_(p|n)(log p)/p.

Split at p=log n. Equation (11) bounds the small-prime sum by log log n+3;
the large-prime part is at most (log n)^(-1) sum_(p|n)log p=1. Thus

    0<=b(n)<=log log n+4.

Consequently the sum of the differences between
mu(n)^2/[n log n] and mu(n)^2/[n a(n)] is bounded absolutely, uniformly in
the cutoff, by a constant times

    sum_(n>=3)(1+log log n)/[n(log n)^2] < infinity.

Equations (3) and (14), with n=2 handled separately, give

    K_(P_y)>=c_sf log log y-O(1).                           (15)

### Upper bound

Put F_y(t)=product_(p<=y)(1+p^-1 exp(-nu_p t)). For t>0,

    F_y(t)<=product_p(1+p^(-1-t))
           =zeta(1+t)/zeta(2+2t).                          (16)

Here nu_p>=log p. Also F_y(t)<=Z_(P_y)<=C_1 log(y+1).
For 0<t<=1, integral comparison gives zeta(1+t)=1/t+O(1).
Termwise differentiation of the absolutely convergent series near 2 gives
zeta(2+2t)=zeta(2)+O(t). Thus the right side of (16) is

    c_sf/t+O(1),                                          (17)

with an absolute uniform constant. For t>=1 the right side minus one is
O(2^-t): use sum_(n>=2)n^(-1-t)<=3*2^(-t)/2 and exp(u)-1<=C u on a bounded
interval. Split (6) at t0=1/log(y+1) and at 1. The first part is O(1), the
middle part is <=c_sf log log(y+1)+O(1), and the last part is O(1). Therefore

    K_(P_y)<=c_sf log log y+O(1).                           (18)

This proves the first assertion of (7). Equation (4) proves the second.

### An improved comparison between the optimal constant and K

Let K2_y=sum_(n in S_(P_y),n>1)1/[n a(n)^2]. From (6),

    K2_y=integral_0^infinity t(F_y(t)-1)dt<=C_2             (19)

uniformly in y, using (16)-(17) and the exponential tail. Rearranging (5),
with A=A_(P_y), gives

    A=K_(P_y)+sum_(n>1)1/[n a(n)(A a(n)-1)].

Since a(n)>=nu_2 and A>=K_(P_y), the last term is at most
C_2/[K_(P_y)-1/nu_2] once that denominator is positive. Equations (15)-(18)
show K_(P_y)->infinity. Thus A-K=O(1/K), as claimed.

The finite grounded form, obtained by imposing f(1)=0, has lowest eigenvalue
1/A_P in the harmonic metric. Hence on these boxes it is asymptotic to
zeta(2)/log log y. This is not the centered spectral gap nu_2.

## 5. A usable positive result: the optimal anchored inverse is explicit

The finite solve need not search an unknown vector. Once A is the unique root
of (5), the coefficients of an extremizing mean-zero f are proportional to

    c_F=chi_F(1)/[A a(F)-1].                               (20)

Subtract f(1) to obtain the positive-grounding extremizer's root-zero form;
no sign of that extremizer is needed for the variational statement. Formula
(20), the diagonal product basis and the one-dimensional monotone equation
fully specify the best constant and its optimizing vector at EVERY finite
box. The fixed finite certificates use directed rational logarithms and a
monotone rational bisection of (5), not floating eigenvalues.

This can sharpen anchored inverses used in fixed-prime modules, and proves
that the log-log order in the more general #825 theorem cannot be removed
while retaining an anchored conclusion on all supports. The maximum-depth
bound in #826 and the largest-prime bound in #825 are compatible: use the
smaller valid cost in a given irregular support. Neither is an RH theorem.

## 6. A consequence: the grounded dynamics have one slow exponential scale

This statement concerns the SAME finite prime box, not the ordinary integers
with an inferred stochastic independence. Kill the Markov chain at the root 1;
equivalently let L_D be the positive graph operator on the subspace f(1)=0.
Let 1_D be one away from the root and zero there. Its stationary survival mass is

    S_P(t)=<1_D, exp(-t L_D)1_D>_pi, t>=0.

The least eigenvalue is exactly 1/A_P. A complete finite formula for its normalized
weight in this survival mass is obtained by putting

    V_P=sum_(n in S_P,n>1)1/[n(A_P a(n)-1)^2].

Then

    (1+V_P)^(-1) exp(-t/A_P) <= S_P(t) <= exp(-t/A_P).       (21)

For all primes <=y, V_P=O(1/(log log y)^2). Consequently the rescaled survival
mass converges UNIFORMLY for t>=0 to exp(-t):

    sup_(t>=0) |S_(P_y)(A_(P_y)t)-exp(-t)|
                      =O(1/(log log y)^2).                 (22)

Here the root can carry initial stationary mass, which is correctly counted as
already killed. The statement is also the stationary root-hitting-time law.
It is not a statement about prime locations or the Mobius signs.

Proof. With A=A_P, set

    F=sum_(F nonempty) chi_F(1) chi_F/[A a(F)-1],  g=1-F.

The secular equation gives F(1)=1, so g(1)=0. Completeness of the product basis
implies sum_(F nonempty)chi_F(1)chi_F=1_{root}/pi(root)-1. Therefore off the root,
L F=(F-1)/A and L_D g=g/A. Its norm is 1+V_P and its mean is 1. Thus the squared
coefficient of 1_D on the normalized ground vector is 1/(1+V_P). The remaining
spectral weights are nonnegative, their sum is at most 1, and every eigenvalue
is at least 1/A. This proves (21). Equation (19) bounds

    V_P <= K2_y/[A_P-1/nu_2]^2,

which proves (22) using CCS2. No diagonalization limit or infinite chain is
required. Finally the root Poisson solution u=sum chi_F(1)chi_F/a(F) has u(1)=K_P
and mean zero. The function K_P-u is zero at the root and solves L_D(K_P-u)=1
elsewhere. Its stationary mean is K_P, the exact mean lifetime. This explains
why K_P and A_P become asymptotically equal while the centered mixing rate
stays bounded away from zero. The finite checker reconstructs the root Poisson
equation and norm independently at rational rates; it does not numerically
simulate the asserted all-prime asymptotic law.

## 7. The connection to the proposed full proof

COHERENT_SOURCE.md identifies an ACTUAL Mobius source norm with the harmonic
coherent projection of a natural Hilbert-valued vertex field. That projection
is exactly what the graph gradient annihilates. Its full edge energy is
c_sf N log N+O(N), proved unconditionally, even though the desired norm is
only required to be subpower. Therefore one cannot combine the graph gap with
the source-domain/capture theorems by silently treating the coherent channel
as a harmless scalar or a discarded mean.

The proposed completion attempted in this pass is NOT obtained. The new
results solve the anchoring optimization and characterize the precise native
channel missed by that attempted composition. They do not bound the native
coherent energy, the intrinsic entropy J, or the full Weil form.
