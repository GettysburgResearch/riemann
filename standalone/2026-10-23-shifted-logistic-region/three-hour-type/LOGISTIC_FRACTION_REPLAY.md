# Independent rational replay of the logistic master inequality

2026-10-21. The companion program `verify_logistic_master_fraction.py`
certifies the scalar inequality below over a full closed rectangle.
It uses only Python's integer/Fraction arithmetic. This is independent
of the parent's directed mpmath interval implementation: the two
programs use different moment evaluations, polynomial evaluations,
and rectangle subdivisions. Their common mathematical inequality is
stated explicitly here.

## 1. The exact scalar resource

Let a1=865534/497079, aP=2919857/828465, theta=5669/5000, and let w,W
be the source Heath-Brown kernel and its Laplace transform. Put w0=w(0).
For

    0<=A<=25/121,  28<=l<=81,

define

    c=log(16+10^10 exp(-l)),  mu=l/(l+c),
    eta=A/l,  sigma=1-A/(l+c),  a=2sigma-1,
    z0=sigma-1,  z1=z0+eta,  z2=sigma-eta,
    J(z,a)=integral_0^infinity exp(-zu)/(1+exp(au))du.

The checker proves strict positivity of

    a1 W(1-mu)-W(-mu)
      +eta*w0[a1/z2+J(z0,a)-a1 J(z1,a)-a1 J(z2,a)]
      -1000 eta^3[(z0+a)^-3+a1(z1+a)^-3+a1 z2^-3]
      -w0[A*aP/4-(15063/5000)*eta/2]-10^-7.             (M1)

The closed face A=0 is a scalar limiting value; the analytic detector
is applied only for A>0. The rectangle itself implies eta<.0075,
sigma>.99, a>0, z0+a>0, z1+a>0, and z2>0. These conditions are checked
or follow directly from the positive interval denominators.

The correction follows by writing logistic F as W minus its small-u
logistic complement. The global Taylor inequality

    |w(v)-w0|<=500 v^2

holds even beyond the support, since the compact extension is C2,
w'(0)=0 and ||w''||<1000. Its integral against exp(-b u) gives
1000 eta^3/b^3. Thus the three error terms in (M1) have their indicated
sign and denominators. The resource uses the independently certified
C_arch<=-3.0126. The 10^-7 budget and the global zero-free inference
are separate analytic obligations recorded by the parent proof.

## 2. Kernel bounds used in the Taylor remainder

The source gives w>=0 and Re W(iy)>=0. The even extension of w is C2
and compactly supported, so its Fourier transform is integrable and
equals 2Re W(iy). Fourier inversion gives w(0)-w(u)>=0 by integrating
this nonnegative transform against 1-cos(yu). Consequently

    0<=w(u)<=w0<6,  U=2theta cot(theta)<1.1.

For |z|<=1, expand exp(-zv) through degree24 inside the integral.
The absolute remainder is bounded by

    6.6 * 3.1 * (1.1)^25 / 25! < 10^-20.               (M2)

The checker verifies this rational inequality and exp(1.1)<3.1.

## 3. Independent moment evaluation

Let k=tan(theta), so kU=2theta exactly. Rather than the other replay's
integration-by-parts recurrence, this program uses the convergent series

    integral_0^U v^n exp(ikv)dv
       = U^(n+1) sum_(m>=0) (2i theta)^m/[m!(n+m+1)].

It takes the appropriate even/odd terms through degree64. A valid
absolute tail for either real or imaginary part, after factoring out
U^(n+1), is

    10*(2.3)^65/65!,

because 2theta<2.3 and exp(2theta)<10. The elementary sine/cosine
formula for w then gives each moment. W itself is evaluated as a
direct sum of interval monomials, not with the other replay's Horner
scheme. The independent trigonometric constants are enclosed by
alternating rational Taylor series.

## 4. Positive beta series for the logistic complement

Substitution t=exp(-au), followed by
1/(1+t)=sum_(n>=0)(1-t)^n/2^(n+1), gives a positive series for J.
Writing b=z+a>0, its first term is 1/(2b), and consecutive terms obey

    term_n/term_(n-1)=n*a/[2(b+n*a)].

This ratio is less than 1/2. After term48, the entire omitted tail is
at most 1/[2^49 b]. The program includes this as a one-sided interval
remainder; no alternating cancellation or numerical integration is
assumed.

## 5. Exact arithmetic and complete rectangle coverage

Each interval endpoint is a Fraction. Every arithmetic operation is
rounded outward to a multiple of 2^-192, using exact integer floor
and ceiling. Exponentials use a positive Taylor series after reduction
to [0,1], an explicit Lagrange remainder, and repeated squaring.
Logarithms use the positive atanh series after powers-of-two reduction
to [1,2], with a geometric tail. No platform floating-point comparison
controls any decision.

The program alternately bisects the height and A coordinates until
the full interval lower endpoint of (M1) is strictly positive. It also
checks that all accepted rectangles lie in the declared domain, that
their interiors are pairwise disjoint, and that their exact total area
is (25/121)*53. The closed rectangles therefore cover the entire
domain, including all boundary points. Their rational endpoints and
margin bounds are saved in `LOGISTIC_FRACTION_CERTIFICATE.json`.

The full rectangle is certified by 42 accepted boxes in 83 evaluations;
the smallest certified lower bound is greater than 0.0000655. A
deliberately overlarge A=1/4 at l=81 has a strictly negative upper
bound and is rejected as a negative control. The program also checks
exp(21.233*(25/121))<81 and exp(28)<3*10^12, which are the numerical
interfaces to the parent's large-height and finite-verification inputs.

Informational decimal renderings in the JSON are not used to establish
any bound. The finite certificate proves (M1), not the imported finite
RH verification, the large-height Littlewood theorem, or the global
zero-free conclusion without the separate analytic argument.
