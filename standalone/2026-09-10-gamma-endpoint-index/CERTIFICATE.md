# Defining-integral certificate for the actual centered integer stage five

Status: proposed computer-assisted finite theorem. This is a zero of the
specified approximant, NOT of xi/zeta. Read PROOF.md, equation (1).

## Object and normalization

The input rates are exactly 1,4,9,16,25, each with gamma shape two. The mean
correction is the outward interval evaluation of

    tau=pi^2/3-2(1+1/4+1/9+1/16+1/25).

No floating substitute for tau is used. For x>0 the density is

    f_5(x)=sum_(a in rates) b_a (x+c_a)e^(-a x),
    b_a=a^2 product_(d!=a) [d/(d-a)]^2,
    c_a=-2 sum_(d!=a) 1/(d-a).

These are finite rational partial fractions of product (a/(a+s))^2.
The complete certificate integrates the UNNORMALIZED half transform

    I(z)=integral_0^L sqrt(f_5(pi e^(2t)-tau)
                         f_5(pi e^(-2t)-tau)) cos(zt)dt,
    L=(1/2)log(pi/tau).

Its zero set is exactly that of F_5, since the omitted factor is positive.
The strict source enclosure for L is checked through exponentials:

    1.07952912855616 < L < 1.07952912855618.

## Analytic disks and complete interval coverage

The integration ends at rational B=1.079529; the whole remaining interval
[B,L] is bounded below. Recursively bisect [0,B] until each cell, with center
c and half-width d, has

    8d <= rho=min(1/64,(L_lower-c)/4).

The exact rational partition is checked for gaps, overlaps and its endpoint.
On |t-c|<=rho the large argument x=pi e^(2t)-tau has Re x>13/5 and
|Im x|<Re x. Isolate its rate-one term. The following fully rational ceiling
for the ratio of all remaining terms is computed and is below 1/4:

    sum_(a>1) (b_a/b_1)
       [2+|c_a|/(13/5)]/[1+c_1/(13/5)] * 2^-floor((a-1)13/5).

We used e>2 and |x|<=2Re x. The positive first polynomial denominator is
retained. Thus f_5(x) is nonzero on each disk.

For the small argument y=pi e^(-2t)-tau, the restriction on rho keeps
Re y>0. In fact, with r=L-c and rho<=r/4,

    Re(pi e^(-2t))/tau >=e^(2(r-rho)) cos(2rho)>1,

using cos(2rho)>=exp(-4rho^2) at rho<=1/64. Also

    |Im y| <=4 e^(1/32)/32 <=4/31 < pi/24.

The simplex formula f_5(y)=c_5 y^9 ell_5(y) and the phase argument in GE1
prove zero-freeness of ell_5 here. Each disk is simply connected and the
square root is continued from its positive center. These branch hypotheses
are part of the quadrature proof, not an optional numerical guard.

## Taylor computation and its analytic error

On every cell we compute degree-40 interval Taylor coefficients for the two
exponential-polynomial densities, their product's positive square root, and
cos(zt), sin(zt). Multiplying by t and t^2 directly supplies I'(z), I''(z).
The Taylor variable is the SCALED coordinate v=(t-c)/rho, so the real cell
has |v|<=d/rho<=1/8. Its kth even coefficient integrates with factor
2d(d/rho)^k/(k+1). All derivative jets include the corresponding rho factors.
This scaling keeps the very small endpoint cells from generating enormous
unscaled Taylor coefficients; it changes neither the integrand nor the
Cauchy error. Every even coefficient is integrated over the exact rational
cell with outward dyadic arithmetic.

The fixed disk lies at |Re z|<32, |Im z|<1/4. On the complex t circles above,
|t|<11/10 and |Im(zt)|<1. Bounds used for a common integrand ceiling are:

- large density <2^11, by the full finite partial fractions and |x|<32;
- small density <=c_5 |y|^9<600*4^9<2^28, since Re y>0;
- cosine and sine <e<3, and |t|^2<2.

Thus M=2^32 bounds each of the three integrands on every Cauchy circle.
Summing the COMPLETE Taylor-series remainders gives at most

    2 B M (1/8)^41/(1-1/8).                            (C1)

The factor two is deliberately spare. There is no floating quadrature or
unpaid coefficient beyond degree forty.

## Both support endpoints, with no integration beyond the probability support

Evenness made the original integral twice the half integral, so it is enough
to bound [B,L]. Let r=L-t. For 0<r<L-B<13/10^8,

    pi e^(-2t)-tau=tau(e^(2r)-1)<(11/10)r,

using the checked tau<11/30 and e^(2r)-1<3r on this interval.

The simplex bound gives f_5(y)<=c_5 y^9, and f_5(x)<=4x e^-x<4. Hence
 h_5(t)<=80 r^(9/2). For j<=2, |t|^j exp(|Im z|t)<4, so the tail error in
each jet is at most

    (640/11)(13/10^8)^5/2000,                          (C2)

where sqrt(13/10^8)<1/2000. The explicit bounds in C1 and C2 are added to
both real and imaginary endpoints. The density vanishes beyond L; no
infinite probability tail is missing and no analytic continuation there
is integrated as a probability density.

## Rouché and the complete derivative budget

The unnormalized density has h_5(t)<=4pi e^tau exp(-pi cosh(2t))<8.
For |Im z|<=1/4 and 0<=t<=L<11/10, direct integration gives |I'''(z)|<32.
At the exact terminating center c specified in certificate.py, let the
computed jet bounds be R>=|I(c)|, D<=|I'(c)|, C>=|I''(c)|. For r=10^-12,

    rD > R + r^2 C/2 + 32 r^3/6.                      (C3)

Consequently I has exactly one zero, counted with multiplicity, in the disk.
It is simple. The disk is separated from both Im z=0 and Im z=1/2. The
arithmetic executes C3 with exact rational endpoints; a printed residual
from an ordinary root finder is not an input to the root count.

## Arithmetic and independence boundary

interval.py is a byte-identical copy of #855's 512-bit dyadic module,
Git blob 36d6341b574fe5a512196bfa0d66fbae897365a6. It uses Machin arctangent
series for pi, range-reduced exponential Taylor series with full remainder,
integer square-root brackets, and enclosed trigonometric series. The new
source, endpoint partition and acceptance are not the parent's two cases.
Reusing this module is not an independent primitive implementation.

The script's exact finite-density checks use independent rational moment and
transform reconstructions. These detect altered rates/coefficients and
coverage, but do not machine-prove the infinite endpoint theorem. The new
zero certificate and the GE2 exterior theorem also have distinct scopes:
there is no numerical exterior radius or exhaustive full-stage census here.
