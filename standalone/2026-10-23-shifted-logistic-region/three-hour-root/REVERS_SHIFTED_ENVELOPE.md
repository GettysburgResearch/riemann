# A global smoothing envelope from a high-height critical-line estimate

2026-10-21. Proposed analytic adapter, requiring independent review.
This note supplies the smoothing input to the corrected Ford minimum-zero
adapter. It does not substitute a constant into Ford's final theorem.

## Source and exact constants

The sole new high-height import is Michael Revers, arXiv:2602.05614v1,
equation (3.32), <https://arxiv.org/html/2602.05614v1#S3.E32>.
Set a=469028/10^6, b=399399/10^5, t0=897*10^15. Dropping its negative
constant gives |zeta(1/2+iy)| <= y^(1/6)(a log y+b) for y>=t0.
This is a preprint input, not a claim that its proof has been formally
verified here. For 3<=y<=t0, use Hiary--Patel--Yang's published bound
|zeta(1/2+iy)| <= .618 y^(1/6)log y (JNT 256 (2024), Theorem 1.1).
No intermediate-range computational claim from Revers is needed.

## A bound at every real ordinate

Let D=2*10^18 and define

    E(v)=(v+D)^(1/6)[a log(v+D)+b],  v>=0.

We claim |zeta(1/2+iy)|<=E(|y|) for every real y. Conjugation reduces
to y>=0. For y>=t0, the high-height import and monotonicity prove it.
For 3<=y<=t0, the published bound is at most .618*t0^(1/6)*log t0.
The elementary inequalities

    log t0<42<log D, D/t0>2, 2^(1/6)>28/25

show

    E(0)/t0^(1/6) > (28/25)(42a+b) > .618*42.

For 0<=y<=3, Euler summation at s=1/2+iy gives

    zeta(s)=1/(s-1)+1/2
             +s integral_1^infinity (floor(x)-x+1/2)x^(-s-1) dx.

The integral's absolute value is at most 1, so |zeta(s)| is at most
2+1/2+sqrt(37)/2<6. Also E(0)>6. This completes the global bound.
The logarithmic singularities at zeros cause no problem for the following
upper bounds or for the locally integrable smoothing integral.

## Uniform smoothing with an explicit negligible loss

Put j(v)=log E(v). For v>=0,

    0<j'(v)=[1/6+a/(a log(v+D)+b)]/(v+D)<1/D.

Indeed a,b>0, log D>0, and 1/6+a/b<1. Thus, for t>=0,

    log|zeta(1/2+i(t+u/pi))|
       <= j(t)+|u|/(pi D).

Since integral_R sech(u)^2 du=2 and
integral_R |u| sech(u)^2 du=2 log2, the integral I(t) used in Ford's
Lemma 9.1 satisfies

    I(t)<=2j(t)+2log2/(pi D)<2[j(t)+1/D].              (R1)

This treats the entire integration line, including the low-height tail;
using a high-height estimate directly at t+u/pi would not suffice.

For h=log t>=70, log2+30log10<70 implies D exp(-h)<10^-12. Therefore

    0<log(t+D)-h=log(1+D/t)<10^-12.

The function q(x)=x/6+log(ax+b) has derivative below 1 for x>=0.
Consequently j(t)+1/D <= q(h)+10^-12+1/D < q(h)+10^-10. Define

    Jnew(t)=log(t)/6+log(a log(t)+b)+10^-10,  t>=exp(70).

Equation (R1) proves I(t)<=2Jnew(t) throughout this range. Jnew is
increasing. When the minimum-zero detector is applied at log t>=70,
all four centers jt, j=1,...,4, lie in this range, so monotonicity permits
the common upper bound Jnew(4t+1).

## Corrected Ford substitution at the minimizing zero

Use FORD_MINIMUM_ZERO_ADAPTER.md with l=log t, h=log(4t+1),
B=(1-beta)l, lambda=B/h, and r=666550/200211. Its inequality becomes

    .16521 <= .1876(h-l)/l +5.646 B^2/(l h)
       +r B [1/6+(log(a h+b)+10^-10)/h]+.851 B/h
       +1.35 r B^2[3.5691/h+5.316 log(h)/h^2+18.475/h^2]. (R2)

Every term on the right increases with B>=0. Every term decreases with
l>=70 for fixed B>=0: the only new verification is

    d[(log(a h+b)+10^-10)/h]/dh
      =[a h/(a h+b)-log(a h+b)-10^-10]/h^2 <0,

because a h+b>e for h>=70. Thus a strict rational upper bound below
.16521 at B=1/R,l=L>=70 excludes every global minimizing violating
zero at log-height >=L. The separate logistic detector must still cover
the full rectangle 0<=B<=1/R, 28<=l<=L. Yang's published Littlewood
result remains the device that guarantees existence of the finite
global minimum; its numerical cap is not used for this shorter rectangle.

The exact endpoint checker is a separate component. This analytic note
alone does not assert a final value of R or a new Riemann hypothesis proof.
