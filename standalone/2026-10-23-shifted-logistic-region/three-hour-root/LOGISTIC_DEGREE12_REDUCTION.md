# Certified degree-12 scalar reduction for R=4.815

Status: proposed proof-producing component, distinct from the earlier
degree-16 R=4.84 and R=4.82 certificates. The claim is the uniform scalar
inequality below. The global zeta consequence uses the separately reviewed
explicit formula and minimum-zero wrapper.

The fixed kernel is unchanged: theta=5669/5000 and w=g*g from
LOGISTIC_KERNEL_AUTOCORRELATION.md. Its sharper curvature certificate gives

    ||w''||_infinity <= ||g'||_2^2 <51.

Hence every coefficient1000 in the transform-error inequalities (3)--(5)
of LOGISTIC_MASTER_REDUCTION.md may be replaced by51, using the identical
global Taylor proof. The W moment series and J beta series are unchanged.

## Exact new trigonometric polynomial

Take

    c=[3500513104,-5906953599,-1574092731,18166603739,6213449589,
       -38436761903,-16088159026,168141762350,447056663730,616860378424,
       541372347258,298691298328,83048065550],
    d=10^14,
    N=sum c_j^2+13d=1000000001299439064580929,
    P(x)=(|sum_(j=0)^12 c_j exp(ijx)|^2
                         +d |sum_(j=0)^12 exp(ijx)|^2)/N.

This construction proves P>=0. The exact cosine coefficients are

    a0=1,
    ak=2[sum_(j=0)^(12-k)c_j c_(j+k)+d(13-k)]/N, 1<=k<=12.

All ak are strictly positive by integer arithmetic. In particular

    a1=1738295793206197388801164/N,
    aP=sum_(k=1)^12 ak=3498832394672653287444040/N<4.

The exact constants checker proves

    -aP log(2pi)/2 + sum_(k=1)^12 ak log(k)/2
       +[-log(pi)/2+psi(3/2)/2] <-3.00317.                   (D1)

The polynomial was found by floating reconnaissance and then replaced
by these exact integers. Optimization success, approximate coefficient
signs and fitted minima are not assumptions in the certificate.

## Uniform inequality

Use K=12, T0=10^10. For

    0<=A<=200/963,           28<=l<=823/10,                  (D2)

set c_l=log(12+10^10 exp(-l)), mu=1/(1+c_l/l), eta=A/l,
sigma=1-A/(l+c_l), alpha=2sigma-1, z0=sigma-1,
z1=z0+eta, z2=sigma-eta. The physical detector uses A>0; the scalar
formula below extends continuously to A=0.

The certificate lower-bounds the isolated-zero signal by

    S_low=a1 W(1-mu)-W(-mu)
      +eta w0[a1/z2+J(z0,alpha)-a1 J(z1,alpha)-a1 J(z2,alpha)]
      -51 eta^3[(z0+alpha)^(-3)+a1(z1+alpha)^(-3)+a1 z2^(-3)].

The independently certified four-prime contribution is

    prime side >=1.26eta-90eta^3,

and the independently certified real-axis correction is E_f(sigma)<=-.31eta.
Both improve the necessary zero-detector inequality in the same direction.
Thus the sufficient margin is

    M=S_low-w0[A aP/4-3.00317eta/2]+1.57eta-90eta^3-10^(-7). (D3)

The complete directed-interval run proves M>0 on all of (D2), using39
closed rational subrectangles. Its least lower endpoint exceeds7.02e-6.
It separately checks the exact polynomial normalization/signs, eta<.0075,
sigma>.99, log(3*10^12)>28, and

    exp(21.233*(200/963))<823/10.

The output binds both the new producer and its unchanged helper source.
No positive margin from an uncertified ordinary floating calculation is
used. A deliberately unsupported A=1/4 is rejected as a negative control.

The independent Fraction implementation must reconstruct the same exact
polynomial, use the same analytic inequalities, certify complete closed
coverage, and evaluate transcendental enclosures without mpmath. Its
separate output and review are part of the final assembly evidence.

The global wrapper changes the finite-zero cutoff to12t+10^10 and uses
the minimum B=(1-beta)log t. Its tail calculation remains valid for all
frequencies k<=12 and aP<4. These analytic statements, rather than a
finite grid of zeta values, connect (D3) to the proposed classical region

    Re s >1-1/(4.815 log|Im s|),       |Im s|>=3.

This formula does not lower the repository's separate proposed uniform
boundary B_flat, and it does not imply the Riemann hypothesis.
