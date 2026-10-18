# Exact density inputs and a continuous budget certificate

Status: proposed source-qualified deductions and exact arithmetic. The selected
fourth-density argument is credited to #966, not claimed new. The new arithmetic
application is to the reflected-numerator comparison in COMPOSITION.md.

## 1. Original de Faveri density

For fixed F containing mu_6, fixed S-ray data and fixed S-supported twists, let
R(U,sigma,T) count SIXTH-POWER-FREE ideal indices of full norm <=U whose
nonprincipal inducing L-function has a zero in Re s>=sigma, |Im s|<=T.
A bound for the total number of zeros also bounds this count. DF Corollary 1.5
states, with q=2sigma-1, R<<U^(g_DF(sigma)+eta)(2+T)^C, where g_DF=1-delta and

 delta = q/(4-6q),                            sigma<=2/3;
 delta = q(36q-6(6sigma-2)+3) /
               [36q(3-2sigma)-24sigma+2],      2/3<=sigma<=11/12;
 delta = (8sigma^2-10sigma+3) /
               [1-24(1-sigma)^2],            sigma>=11/12.       (1)

The height exponent here is deliberately not optimized. Only finitely many
fixed thresholds occur. The exact norm powers in DF Section 9 can be checked
by A=U^r,B=U^b with

 r=1/2, b=2/(4-6q),                                     low;
 r=(24q-5)/D, b=(42q-8)/D, D=6q(10-6q)-10,               middle;
 r=(6q-4)/D, b=(8q-5)/D, D=1-6(1-q)^2,                   high.    (2)

With (c,d) in {(1,0),(0,1),(1/3,5/6),(5/6,1/3)}, all TEN detector powers are

 1/2+(cr+d)/2+(1/2-sigma)b                              [four];
 (2-2sigma)b; 1+(1-2sigma)r                             [two];
 1/3+(11/6-2sigma)v, v=r,b                              [two];
 5/6+(4/3-2sigma)v, v=r,b                               [two].   (3)

Their maximum is exactly (1) at every used threshold. Neither supremum
endpoint is deleted. The checker verifies this with rational arithmetic.

## 2. Credited selected-fourth improvement

DF's full sixth-free large-sieve bracket is

    K(U,V)=U+V+U^(5/6)V^(1/3)+U^(1/3)V^(5/6).                  (4)

The complete AFE, squared with all columns retained, gives the credited bound
sum|L(1/2+it,chi_u)|^4<<U^(7/6+eta)(2+|t|)^C. To see the exact column adapter,
write each product ideal n=c d^6 uniquely, c sixth-free, with NO requirement
(c,d)=1. Complete multiplicativity including zeros gives

    chi_u(c d^6)=chi_u(c) 1_((u,d)=1).                         (5)

For fixed d the last factor is a ROW restriction in the large sieve, not a
row-dependent column coefficient. Minkowski across d costs the convergent
root sum sum (Nd)^(-3+eta). Both AFE pieces, conductor-dependent Mellin weights,
root numbers and rapid tails remain; fixed S types can be separated first.
Product length V about U makes the two mixed terms in (4) U^(7/6). This is
#966/#968's numerator estimate, not the open native inverse-Mobius fourth
moment. No new claim of priority is made for AFE, powering or the large sieve.

In the BGL zero detector retain the selected rows BEFORE Holder. The first
sum is bounded by

    sum_selected |L M_A|
     <= R^(1/4) (sum_all|L|^4)^(1/4) (sum_all|M_A|^2)^(1/2).

The second side is a complete Dirichlet-polynomial tail. Its square mean is
bounded by Q below; Cauchy retains R^(1/2). With polynomial height and arbitrary
small norm losses suppressed, the resulting scalar inequality is

 R << B^(1/2-sigma) R^(1/4) U^(7/24) K(U,A)^(1/2)
          + R^(1/2) Q^(1/2),
 Q = B^(2-2sigma)+U A^(1-2sigma)
       +sup_(A<=V<=B) [U^(1/3)V^(11/6-2sigma)
                       +U^(5/6)V^(4/3-2sigma)].             (6)

The selected-ordinate reduction is the rowwise BGL (5.3) argument: choose one
zero per row, use its Mellin zero detector, truncate the exponentially decaying
Gamma integral, and separate dyadic endpoints and ordinates before the common
coefficient large-sieve means. One-dimensional Sobolev/partial summation costs
only logarithms and a polynomial in T; differentiation inserts log norms.
The indicator selecting rows is retained until the Holder/Cauchy inequalities.
This is the explicit analytic import reconstructed in #966 and the old #970
packet. It is not justified by a synthetic partition checker alone.

If R<=A0 R^(1/4)+B0 R^(1/2), splitting according to which term is at least
R/2 gives R<<A0^(4/3)+B0^2. Thus the four first powers in (3) become

    7/18+(2/3)(cr+d)+((2-4sigma)/3)b,                         (7)

while the other six powers are unchanged. On [7/10,9/10] set

 D=36sigma^2-75sigma+31,
 r=-(48sigma-29)/(2D), b=-(33sigma-19)/D,
 g4=(468sigma^2-741sigma+271)/(6D).                          (8)

The theorem only needs rational instances, all verified by (7) and the six
retained powers. The continuous interval is also valid. D<0 there, 0<r<b,
and the ten differences g4-minus-power simplify respectively to

 (180sigma^2-279sigma+97)/(9D);
 -(3sigma-2)(12sigma-1)/(9D);
 0;
 (2sigma-1)(12sigma-11)/(2D);
 (72sigma^2-117sigma+43)/(6D);
 -(3sigma-2)(12sigma-1)/(6D);
 3(2sigma-1)(12sigma-11)/(4D);
 0; 0;
 -3(2sigma-1)(3sigma-2)/D.                                  (9)

Every displayed sign is nonnegative on [.7,.9]. For the two quadratic
numerators use convexity and their negative values at both endpoints. The
other signs follow directly from sigma>2/3 and sigma<11/12. At sigma=3/4
this gives the credited exponent 43/60, not a new independent theorem here.
All these estimates have a finite polynomial height factor; choosing one
sufficiently small rho for the finite list gives count exponent g+e at
T=4U^rho. Later contour losses do not change that list or rho.

## 3. Why the new finite comparison has room

The main reflected class budget at a=21/50 is

    2tau+g(sigma) < 129/58,   tau=sigma+1/2500.               (10)

The finite checker verifies EVERY instance, including the outer DF intervals.
There is also a continuous certificate on the delicate [.7,.9] interval.
With D as above and g4 from (8), exact polynomial division gives

 129/58 - 2sigma - 1/1250 - g4(sigma) = -P(sigma)/(87D),
 P(sigma)=(7830000sigma^3-16534368sigma^2
                       +11445975sigma-2583553)/1250.        (11)

Put t=sigma-4/5. Then |t|<=1/10 and

 P=6264t^3+(1128816/625)t^2+(122931/6250)t+4787/31250.

Since 6264t^3>=-(3132/5)t^2 on this entire interval,

 P >= A t^2+B t+C,
 A=737316/625, B=122931/6250, C=4787/31250,
 4AC-B^2=524968911/1562500>0.                               (12)

Completing the square proves strict positivity. Since D<0, (10) follows
throughout [.7,.9], without sampling. The checker verifies the coefficient
identity after clearing denominators, the translated coefficients, and the
positive discriminant gap; three rational samples are additional cross-checks,
not the basis of this proof. The remaining thresholds use the explicit finite
DF certificates, not an unproved global bound on their continuum.

## 4. What has and has not changed

No stronger zero density is announced by this packet. The new contribution
uses these already available counts DIFFERENTLY in the Poisson estimate:
zero-freeness also bounds the DIRECT reflected numerator. The fourth moment
is used only in the stronger density option, not as the middle-class numerator
estimate. Theorem B in COMPOSITION.md removes even that fourth-moment input.
The statements remain source-qualified pending independent analytic review.
