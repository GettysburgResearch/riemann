# Fixed entire onsite energies cannot complete this strip transfer class

Status: **PROPOSED complete native closure theorem.** This is the
culmination of the Gaussian-mediated construction attempts. It permits
an arbitrary quadratic counterterm, controlled nonreal auxiliary zeros,
and a fixed finite family of positive entire onsite energies. It gives
an entire-density closure, not just a quartic tail bound. The actual
theta density has a nonanalytic modular cusp and is excluded.

No claim of priority or exclusion of all cofinal constructions is made.
In particular direct spin observables, onsite families with uncontrolled
growing degree, noncompact complex energy profiles and other transfer
representations remain outside the theorem.

## 1. Exact theorem

Fix finitely many even entire functions U_1,...,U_K, real on R, such
that `u -> U_k(sqrt(u))` is convex for u>0 and strictly convex between
any three positive points. Quadratic terms can be removed from each U_k
and handled separately. Examples are x^(2m), m>=2, and cosh(cx)-1 with
c!=0. Adding a constant to an onsite energy does not matter.

For each N let Y_N be a symmetric bounded-support law whose entire
characteristic function has all zeros in one fixed finite band
`|Im z|<=epsilon`. The bound epsilon is independent of N; support,
variance and auxiliary graph size are unrestricted. Write M_N(z)=E exp(zY_N).
Choose alpha_{k,N}>=0 and c_N in R such that

    p_N(x)=Z_N^(-1)
       exp[-sum_k alpha_{k,N}U_k(x)-c_N x^2] M_N(x)  (1)

is integrable.

**Theorem.** If the laws(1) converge weakly to a law with a positive
continuous even density p on R, then p agrees on R with an entire
function. In particular p cannot be the actual complete theta density.

The bounded-support hypothesis can be replaced by the exact paired
Hadamard representation used below, provided its quadratic exponential
factor is explicitly absorbed into c_N. No such extension is silently
assumed for an arbitrary auxiliary law.

## 2. Normalize the fixed zero band

A single change of variables x=L y, with `L=10max(epsilon,1)`, reduces
the MGF zero band to `|Re zeta|<=1/10`. Replace U_k by U_k(Ly), still a
fixed finite family of entire energies with the same convexity property.
Thus it suffices to prove the result in that normalization.

As in STRIP_MEDIATOR_OBSTRUCTION.md, group the MGF zeros into quartets
represented by `zeta=beta+i gamma`, beta>=0,gamma>0, and pure imaginary
pairs. Put r=|zeta| and

    P_zeta(z)=(1-z^2/zeta^2)(1-z^2/bar zeta^2).

For a genuine quartet use m=1 and the entire factor F_zeta=P_zeta.
For a pure imaginary pair use m=1/2 and the entire factor
`F_zeta(z)=1+z^2/gamma^2`; on R its logarithm equals m log P_zeta.
Multiplicity is retained by repeated factors. The order-one, even
Hadamard product gives

    M_N(z)=product_zeta F_zeta(z),
    sum_zeta m/r^2<infinity.                        (2)

There is no square-root branch in the complex factor at a pure
imaginary pair. The expression with m is only convenient real-log
notation.

## 3. Weak convergence yields local ratios and bounded resources

The exact calculation in STRIP_MEDIATOR_OBSTRUCTION.md gives

    partial_u^2 log P_zeta(sqrt(u))
                       =-2 Re[(u-zeta^2)^(-2)]<0,  u>1/50. (3)

Indeed `u+gamma^2-beta^2>2|beta gamma|` there. After adding the
nonpositive convex onsite contributions and the quadratic counterterm,
the logarithm of(1) is concave as a function of u=x^2 on this interval.

The native compact weighted-restriction lemma from
RANK_ONE_HIERARCHY_OBSTRUCTION.md therefore applies: restrict X_N^2 to
I inside (1/50,infinity), weight by sqrt(u), normalize, and use
logconcavity. Its anchor/secant proof gives

    V_N(x)-V_N(y)->-log[p(x)/p(y)],        x,y>=1,    (4)

where

    V_N(x)=sum_k alpha_{k,N}U_k(x)+c_N x^2-log M_N(x).

This step uses only weak convergence and the positive continuous target
density. It makes no tail-continuity assumption.

Define the fixed onsite differences

    D_k=U_k(3)-(8/3)U_k(2)+(5/3)U_k(1)>0.           (5)

Their positivity is exactly strict convexity in u at1,4,9. The same
finite difference applied to each quartet log gives

    G(zeta)=-log P_zeta(3)+(8/3)log P_zeta(2)
                                          -(5/3)log P_zeta(1)>0.

The previous native proof establishes the uniform comparison

    G(zeta)>=c min(r^(-4),1),                       (6)

using strict concavity, the uniform far limit r^4G->40, the positive
near-zero limit `2[(8/3)log4-log9]`, and compactness of the remaining
parameter region. Thus

    V_N(3)-(8/3)V_N(2)+(5/3)V_N(1)
                     =sum_k alpha_{k,N}D_k+sum_zeta mG(zeta). (7)

By (4) its left side is bounded. Every right-hand term is nonnegative.
There is consequently a finite uniform S such that

    alpha_{k,N}<=S for every k,
    sum_(r>=1)m/r^4<=S,          sum_(r<1)m<=S.     (8)

All exact series converge for each N by(2); positivity justifies the
infinite resource sum without cancellation.

## 4. The renormalized quadratic coefficient is also bounded

For r>=1 set

    A_zeta=2(gamma^2-beta^2)/r^4,
    B_zeta=r^(-4),
    q_zeta(x)=A_zeta x^2-log P_zeta(x).

In this range beta<=1/10 gives

    1.96/r^2<=A_zeta<=2/r^2,
    A_zeta^2>=2B_zeta,
    0<=q_zeta(x)<=2r^(-4)x^4, x real.              (9)

The nonnegative q increases for x>=0. For r<1 the ratio
`P_zeta(x)/P_zeta(1)` increases from1 for x>=1, and its value at2
is at most `[5/(1-1/100)]^2`. Define the finite renormalized coefficient

    C_N=c_N-sum_(r>=1)m A_zeta.                     (10)

The sum is finite for each N by(2). Evaluating V_N(2)-V_N(1) and
using (8)--(9) bounds every term except3C_N. The onsite contributions
are bounded because there are finitely many fixed U_k and their
coefficients are bounded. The far q increment is bounded by32S, and
the near log increment is bounded by a fixed multiple of S. By(4),
therefore

    |C_N|<=C.                                      (11)

An unbounded original c_N is permitted; its exact cancellation against
the small-zero quadratic part is retained in(10).

## 5. Uniform complex bounds for all paired factors

For r>=1 introduce the entire renormalized factor

    E_zeta(z)=F_zeta(z) exp(-m A_zeta z^2).          (12)

For every fixed R<infinity there is a finite C_R such that

    |E_zeta(z)|<=exp(C_R m/r^4),       |z|<=R.      (13)

To verify this for r>=2max(R,1), expand each logarithm
`log(1-z^2/zeta^2)` in its convergent Taylor series. The order-z^2 term
is exactly m A_zeta z^2 and is canceled in(12); the remaining series
is O_R(m/r^4), uniformly in the zero argument. At a pure imaginary
pair use its single factor, so the same cancellation holds without
selecting a square root.

For `1<=r<2max(R,1)`, direct multiplication gives

    |E_zeta(z)|
       <=exp(2mR^2)(1+R^2)^(2m).

Since r is bounded on this remaining range, increasing C_R proves(13)
there as well. No complex logarithm near a zero is used in this part.
At the real anchor1, (9) gives

    E_zeta(1)=exp[-m q_zeta(1)],
    E_zeta(1)^(-1)<=exp(2m/r^4).                    (14)

Thus (8), (13)--(14) bound the complete far normalized product
`product E_zeta(z)/E_zeta(1)` uniformly on every compact complex disk.
The tail also converges locally uniformly by its O_R(m/r^4) estimate.

For r<1, normalization removes every possible small-radius problem:

    F_zeta(z)/F_zeta(1)
      =[(zeta^2-z^2)(bar zeta^2-z^2)]
                    /[(zeta^2-1)(bar zeta^2-1)]

for a quartet. The denominator factors have modulus at least
`1-beta^2+gamma^2>=99/100`; the numerator factors have modulus at most
`1+R^2`. Hence its modulus is at most
`[(1+R^2)/(99/100)]^2`. For a pure imaginary pair the ratio is
`(gamma^2+z^2)/(gamma^2+1)`, bounded by1+R^2. The weighted count in(8)
bounds the actual number of such factors by2S. Therefore their complete
normalized product is uniformly bounded on every compact disk too.

## 6. Entire normality and identification of the weak limit

The entire density ratios H_N(z)=p_N(z)/p_N(1) have the exact form

    exp[-sum_k alpha_{k,N}(U_k(z)-U_k(1))-C_N(z^2-1)]
       · product_(r>=1) E_zeta(z)/E_zeta(1)
       · product_(r<1) F_zeta(z)/F_zeta(1).          (15)

Here p_N(z) denotes the entire continuation of its finite formula,
not an assumed continuation of a weak limit. Fixed entire U_k, (8),
(11) and section5 give a uniform bound on every compact disk. Montel
therefore supplies entire locally uniform subsequential limits.

By(4), on every real x>=1 these limits equal p(x)/p(1). The identity
theorem makes all subsequential limits the same, and H_N(1)=1 prevents
the zero limit. Thus the full sequence converges locally uniformly to
an entire H with

    H(x)=p(x)/p(1),                 x>=1.          (16)

The remaining probability normalization identifies the density also on
the inner interval, where section3 did not use logconcavity. For the
fixed real interval J=[1,2], weak convergence and absence of limiting
endpoint atoms give

    p_N(1) integral_J H_N(x)dx=integral_J p_N(x)dx
                                  ->integral_J p(x)dx.

The denominator converges by compact uniform convergence, and (16)
makes its limit `integral_J p/p(1)>0`. Hence p_N(1)->p(1). Therefore
p_N(x)->p(1)H(x) uniformly on every compact REAL interval. Weak
convergence identifies this local density limit with p almost
everywhere, and continuity gives equality everywhere. This proves the
opening entire-density conclusion without any prior analyticity
assumption on p or local ratio estimate at0.

## 7. The actual target has no such entire tail extension

The root track's BESSEL_COMPLETION_ATTEMPT.md gives a native complete
Jacobi-theta proof of the nonanalytic cusp at t_0=i pi/4. In brief,
put v=exp(2t) and

    Theta(v)=sum_(n in Z) exp(-pi n^2 v),
    Phi(t)=2v^(9/4)Theta''(v)+3v^(5/4)Theta'(v).

Along v=epsilon+i with epsilon decreasing to0, Poisson summation gives

    Theta(epsilon+i)=epsilon^(-1/2)
         sum_(m in Z) exp[-pi(m+1/2)^2/epsilon].     (17)

The complete theta kernel has modulus bounded there by
`epsilon^(-C)exp[-pi/(4epsilon)]`. Also
`(1/2)Log(epsilon+i)-i pi/4` is a nonzero constant times epsilon plus
O(epsilon^2). An entire extension agreeing with Phi on a positive real
interval would agree on its analytic strip, hence be smaller than every
power of its distance from t_0 along this path. Its Taylor series at t_0
would vanish to every order, making it identically zero. That conflicts
with Phi's positive real values. The detailed complete-source flatness
proof remains in the root file; nonvanishing along the cusp path is
unnecessary for this contradiction.

Thus (16) already rules out the actual theta law. The known real-axis
tail `-log Phi(x)=pi exp(2x)-(9/2)x+O(1)` is no longer needed once
the onsite family includes cosh-like growth.

## 8. Scope

The theorem covers a fixed finite collection of positive entire onsite
energies, arbitrary quadratic renormalization, and arbitrary bounded
symmetric auxiliaries with one uniformly bounded zero strip. It permits
changing graph sizes, weak Gaussian mediation, arbitrarily many zeros,
zeros approaching0 and noncompact original quadratic coefficients.
Its proof pays all of those effects with the local finite difference.

It does not cover an uncontrolled growing family U_N, loss of the
bounded auxiliary zero strip, general nonsymmetric densities, or a
direct graph observable lacking the exact density formula(1). An actual
cofinal theta construction must escape at least one of those stated
conditions; no assertion that such an escape is impossible is made.
