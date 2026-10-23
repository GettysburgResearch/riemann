# Degree12 detector constants and an improved kernel curvature bound

2026-10-21. This is a separate refinement; the prior 4.84 and 4.82
certificates are unchanged. The parent supplied the degree12 candidate.
The polynomial reconstruction and constants below were independently
checked with exact rational intervals.

## 1. A rational nonnegative polynomial

Let

    c=(3500513104,-5906953599,-1574092731,18166603739,6213449589,
       -38436761903,-16088159026,168141762350,447056663730,
       616860378424,541372347258,298691298328,83048065550),
    M=10^14,  N=sum c_j^2+13M=1000000001299439064580929.

Define

    P(x)=[|sum_(j=0)^12 c_j exp(ijx)|^2
                  +M|sum_(j=0)^12 exp(ijx)|^2]/N.

Thus P>=0 identically, without a root calculation. Its cosine
coefficients are a0=1 and

    a_k=2[sum_(j=0)^(12-k)c_j c_(j+k)+M(13-k)]/N.

The exact checker verifies every a_k>0 and

    a1=1738295793206197388801164/N >1.

It prints every rational coefficient and their sum aP. Hence
0<=P(x)<=P(0)=1+aP, as required by the detector and prime estimates.

The same gamma calculation as in `LOGISTIC_REAL_AXIS_CONSTANTS.md`
gives

    C_arch =1-gamma/2-(1+aP/2)log2
                    -(1+aP)log(pi)/2+(1/2)sum_(k=1)^12 a_k log k.

Using the elementary lower bound
gamma>H_1000-log1000-1/2000, Machin's formula, and rational atanh
series for logarithms, the checker proves

    C_arch < -3.003196.

The polynomial's smaller degree changes the geometric height factor
from log(16+T0 exp(-l)) to log(12+T0 exp(-l)). This change must be made
in a new master certificate; it is not silently applied to the old one.

## 2. Positive Fourier transform controls the entire second derivative

The even extension of the source kernel w has nonnegative integrable
Fourier transform, since Re W(iy)>=0. Write its Fourier representation
as w(u)=integral cos(tu)dmu(t), where mu is a finite positive measure.
Because w is C2 at zero,

    -w''(0)=lim_(u->0) integral 2(1-cos(tu))/u^2 dmu(t).

Fatou gives integral t^2 dmu(t)<=-w''(0)<infinity. The domination
2(1-cos(tu))/u^2<=t^2 then gives equality by dominated convergence.
Differentiating the Fourier representation twice is now justified and

    |w''(u)|<=integral t^2 dmu(t)=-w''(0)                (D1)

for every real u, including the compactly extended kernel. This argument
uses the same imported Fourier positivity already needed for the
detector, and does not assume pointwise positivity of w''.

Differentiating the explicit source formula at zero gives

    -w''(0)=sec^2(theta)tan^2(theta)
                         [sec^2(theta)*theta*cot(theta)-1].

At theta=5669/5000 the exact interval checker encloses this between
50 and 51 (numerically 50.06970149...). Therefore

    ||w''||_infinity<51,
    |w(v)-w0| <=(51/2)v^2 for all v>=0.                 (D2)

This permits replacement of 1000 by 51 in the master transform error,
and of 175 by 51/2 in prime-side Taylor errors, in a separately verified
refinement. It also reduces the positive error in the real-axis
archimedean estimate. No new numerical zero-free constant follows
without rerunning the corresponding full parameter certificate and
reviewing the prime and global interfaces.
