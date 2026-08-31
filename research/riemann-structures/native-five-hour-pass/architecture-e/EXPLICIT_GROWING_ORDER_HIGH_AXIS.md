# Explicit growing-order positivity on the high safe axis

Status: PROPOSED analytic sequel; independent review required.
Scope: every integer n>=1, threshold16*3^n, arbitrary node ratios and confluence.
No all-order positivity at a fixed threshold is claimed. No new computation
is required or claimed. Dependency: FOUR_NODE_HIGH_AXIS.md, sections1--4,
whose finite-space identities are proved before specializing the constants.

Root proposed the threshold16*3^n after reviewing the first four-node proof.
The following uniform inequalities prove it; no finite table is extrapolated.
The sharper four-node threshold256 and its original replay remain unchanged.

## Theorem E-n

For n>=1 let R_n=16*3^n. For any real list x_1,...,x_n>=R_n, the literal
completed-xi kernel H(x,y)=(F(x)+F(y))/(x+y), F=Y'/Y, Y(x)=xi(1/2+x),
satisfies H>=C, C(x,y)=1/(x+y). Repeated nodes are interpreted as exponential
jets or normalized Newton divided differences. In fact Re F(A)>51/64 on
the orthonormal n-dimensional exponential space.

Thus for R>=48, every dimension
1<=n<=floor(log_3(R/16)) is covered if all nodes>=R. This quantifies a
growing-order region, not the distinct older impedance theorem whose source
manifest records an unresolved moving-frame bound. It makes no assertion
for unrestricted dimensions at fixed R or for nodes below the threshold.

## 1. The same literal finite source

Use c=1/2 and the orthonormal basis and matrix A from E4.4--E4.5.
Those identities hold at every finite n and give Re A>=0. The exact identity is

    F(A)=(1/2)log((A+c)/(2pi))+(A-c)^(-1)+(A+c)^(-1)
          -integral_0^infinity q(2t)exp(-ct)exp(-tA)dt
          -sum_(m>=2) Lambda(m)/sqrt(m)exp[-(log m)A],
    q(t)=1/(1-exp(-t))-1/t,       0<q(t)<1.

Only finite-dimensional functional calculus is used. The gamma and prime
terms are retained exactly before bounding their norms; no closed ambient
F(-d/dt) is assumed.

## 2. Uniform logarithmic reserve

The exact resolvent product gives |log(A+c)_ij|<=2 for i<j. For R=R_n,

    Re[(1/2)log((A+c)/(2pi))]
      >=[(1/2)log((R+c)/(2pi))-(n-1)/2]I
      >[(1/2)log(8/pi)+1/2+(n/2)(log3-1)]I
      >(5/6)I.                                               (EN.1)

Here pi<4, log2>2/3 and log3>1 suffice. The logarithm inequalities follow
strictly by integrating the strictly convex function1/t on[1,2] and[1,3]
and comparing with its midpoint value. No approximate logarithm is used.

## 3. Rational and gamma terms

Induction gives3^(n-1)>=n, hence R>=48n. Since R>=48,

    R-c >=(95/96)R,        n/(R-c)<=2/95,
    Q=(R+c)/(R-c)=1+1/(R-c).

Using binomial(n,k)<=n^k and a geometric series,

    Q^n <=1/[1-n/(R-c)]<=95/93<2.                             (EN.2)

For n>=2 the exact resolvent bound E4.12 yields

    J_n(R)=1/(R-c)+2R/(R-c)^2 sum_(j=0)^(n-2)Q^j
      <=[(96/95)+4(96/95)^2(n-1)]/R
      <5n/R<=5/48<1/8.                                       (EN.3)

For n1 the empty-sum expression satisfies the same final bound directly.
The exact identity Re(A-c)^(-1)>=-c||(A-c)^(-1)||^2 I therefore loses less
than1/128. The second rational term has nonnegative real part.

The increasing-path convolution estimate E4.13 gives

    ||gamma remainder||<=3^(n-1)/(R+c)<1/48.                  (EN.4)

Neither bound uses node separation.

## 4. Prime term for every dimension

Weighted Young's inequality in the same orthonormal basis gives

    ||exp(-tA)||<=C_n exp(-Rt/2),
    C_n^2=2 sum_(j=0)^(n-1)25^j=(25^n-1)/12,
    C_n<2*5^(n-1).

Put K=R/2-1=8*3^n-1>=23. Since Lambda(m)<=log m<=m,

    ||prime remainder||
      <=C_n sum_(m>=2)m^(-(R-1)/2)
      <=C_n sum_(m>=2)m^(-K)
      <=C_n[2^(-K)+2^(1-K)/(K-1)]
      <2^(3-8*3^n)5^(n-1)
      <=2^(3n-8*3^n)<=2^(-21)<1/128.                         (EN.5)

The last exponent is-21 at n1 and strictly decreases: its successive
difference is3-16*3^n<0. This is a uniform argument, not a finite scan.

## 5. Conclusion and normalized residual

Combining the literal source terms,

    Re F(A)>5/6-1/48-1/128-1/128=51/64>1/2.

The Gram identities give H>=C, with the stronger relative bound
H>51C/32 on nonzero vectors in every confluent coordinate system. The
normalized last-node Schur residual is therefore at least

    1/[2x_n product_(i<n)(x_n+x_i)^2].

This follows from the Cauchy determinant and variational Schur complement,
as in E4.3, and remains valid through partial collisions. At total confluence
x it is(2x)^(-(2n-1)). These are effective finite-order conclusions in an
unbounded node region; they do not decide the remaining lower-node region.

Classical Malmquist orthogonalization and xi/Euler/digamma identities are
credited in the first packet. No external novelty claim is made. Its finite
n4 producer does not execute this all-n proof, and none of its registered
constants, coverage or test counts is changed.

