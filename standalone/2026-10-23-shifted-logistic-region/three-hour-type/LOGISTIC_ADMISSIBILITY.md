# Exact logistic smoothing: admissibility and the archimedean term

2026-10-21. A proposed analytic adapter for Bellotti--Trudgian--Yang,
arXiv:2603.21490v1 (BTY), Sections 2--5. No numerical zero-free constant
is asserted here. The kernel in BTY (14) is admissible; the sentence
following (16) does not correctly describe its Laplace-transform decay.

Primary source: https://arxiv.org/html/2603.21490v1 . Equations and lemma
numbers below refer to that version. We retain the source's function w
and theta=1.1338.

## 1. The endpoint derivative is not an obstruction

Fix eta>0 and 1/2<sigma<1, set a=2 sigma-1, and define

    f(u)=eta w(eta u)/(1+exp(-a u)),
    F(z)=integral_0^infinity exp(-z u) f(u) du.

The compact extension of f is C2 and piecewise smooth. At its right
endpoint f,f',f'' vanish. Since w'(0)=0,

    f(0)=eta w(0)/2,
    f'(0)=eta a w(0)/4.                                  (L1)

Two integrations by parts give, for z nonzero,

    F(z)=f(0)/z + [f'(0)+integral exp(-zu)f''(u)du]/z^2.  (L2)

Consequently F(z)=f(0)/z+O_nu(|z|^-2) uniformly on every fixed
half-plane Re z>=nu. For nu<0 the implied constant includes the compact
support exponential. A third integration, in the piecewise-smooth
sense, gives the finer expansion f(0)/z+f'(0)/z^2+O_nu(|z|^-3).
The nonzero derivative prevents the O(|z|^-3) remainder after removing
only f(0)/z; it does not prevent the O(|z|^-2) condition stated in BTY.

BTY Lemma 7 cannot be applied directly to f because it assumes g'(0)=0.
That is a restriction of the displayed lemma, resolved below.

## 2. Exact explicit formula with arbitrary first derivative

Let f be any real compact C2 function on [0,infinity), piecewise C3,
with f,f',f'' vanishing at the support endpoint. For Re s>1/2 put

    A(s)=-log(pi)/2 + psi(s/2+1)/2,
    E_f(s)=integral_0^infinity
       exp(-(s+2)u) [f(0)-f(u)]/(1-exp(-2u)) du.           (L3)

The integrand has a finite limit at zero and decays at infinity. The
generalization of BTY Lemma 7 is

    Re sum_n Lambda(n)n^-s f(log n)
      = f(0) Re A(s) + Re F(s-1)
        - Re sum_rho F(s-rho) + Re E_f(s).               (L4)

The zero sum is ordered in conjugate pairs, with multiplicities; its
real part is absolutely convergent on bounded s sets. It is the sum
over nontrivial zeros only.

Here is a derivation from exactly the imported lemma. First suppose
f'(0)=0 and set H(z)=F(z)-f(0)/z. BTY Lemma 7 writes its remainder as

    (1/(2pi)) integral_R H(s-1/2-iy) Re psi(1/4+iy/2)dy
       + H(s).

The digamma representation is

    Re psi(1/4+iy/2)
      = -gamma + integral_0^infinity
        [2exp(-2u)-2exp(-u/2)cos(yu)]/(1-exp(-2u))du.

Fourier inversion of H(s-1/2-iy), the Laplace transform of f(u)-f(0),
annuls the constant terms because f(0)-f(0)=0. The cosine term gives

    -integral_0^infinity exp(-su)[f(u)-f(0)]/(1-exp(-2u))du.

Adding H(s) gives (L3). One may first truncate the digamma integral
away from zero and regularize the y integral, then pass to the limit;
f(u)-f(0)=O(u^2) makes the zero endpoint integrable in this case, and
H decays cubically on vertical lines.

For general f with f(0) nonzero, let c=f'(0)/f(0), and
g(u)=exp(-cu)f(u). Then g'(0)=0 and f(u)=exp(cu)g(u). Initially apply
the established formula to g at s-c with Re(s-c)>1/2. The identity

    E_g(s-c)-E_f(s)=f(0)[A(s)-A(s-c)]                     (L5)

follows directly from the usual integral for the digamma difference.
All pole and zero transforms shift exactly, proving (L4). Analytic
continuation, or local uniform convergence of the conjugate-paired
zero sum, extends it to Re s>1/2. The f(0)=0 case follows by linearity
after adding and subtracting one fixed test function with nonzero
value at zero. Thus the special derivative assumption is removed.

As an independent normalization check, for f(u)=exp(-cu) the correction
in (L3) is A(s+c)-A(s). The gamma contribution therefore becomes
A(s+c), exactly as required by the shifted logarithmic derivative.
This check is an identity of the archimedean terms, not an invocation
of the compact-support theorem for a noncompact test.

## 3. A negligible high-height error with explicit coarse constants

For fixed real sigma set b=sigma+2 and

    K(u)=exp(-bu)[f(0)-f(u)]/(1-exp(-2u)).

Then Re E_f(sigma+it)=integral K(u)cos(tu)du. Twice integrating by
parts gives

    |Re E_f(sigma+it)| <= (|K'(0)|+||K''||_1)/t^2.        (L6)

The first integration has no endpoint term because sin(0)=0. The
second endpoint is K'(0), so no O(1/t) term is lost by this estimate.
In fact

    K'(0)=(b-1)f'(0)/2-f''(0)/4.                         (L7)

One convenient fully explicit bound uses M_j=||f^(j)||_infinity. Write
r(u)=u/(1-exp(-2u)) and B(u)=[f(0)-f(u)]/u. The elementary inequalities

    r(u)<=u+1/2,  0<=r'(u)<=1,  0<=r''(u)<=1

and B=-integral_0^1 f'(tu)dt give

    |K'(0)|+||K''||_1
      <= (5/2+b+1/b)M_1 +(3/4+2/b)M_2
          +(1/(3b^2)+1/(6b))M_3.                        (L8)

For completeness r''=csch(u)^2[u coth(u)-1]. On 0<u<=1 use
coth(u)<=1/u+u/3 and sinh(u)>=u; on u>=1 use coth(u)<=1+1/u
and csch(u)^2<=1/u^2. These give the stated relaxed bound.

For the source theta=1.1338, elementary differentiation of its formula
for w gives ||w^(j)||_infinity<1000 for 0<=j<=3. Very coarse sufficient
trigonometric bounds are sec^2(theta)<6.25, tan(theta)<2.4,
theta cot(theta)<.55, csc(theta)<1.12, csc(2theta)<1.34. For example
the third derivative is bounded by

    6.25[6.25(1.5*2.4^2+.55*2.4^3)
                     +(1.34+2*1.12)*2.4^3] < 1000.

The smaller derivative orders have smaller corresponding bounds.
The zero extension has continuous second derivative, so its third
derivative is bounded piecewise and suffices in (L8).

For 0<eta<=.008 and 0<a<=1, the logistic factor h obeys
|h|<=1, |h'|<=a/4, |h''|<=a^2/4, |h'''|<=a^3/4. Hence

    M1<=1000 eta(eta+1/4),
    M2<=1000 eta(eta^2+eta/2+1/4),
    M3<=1000 eta(eta^3+3eta^2/4+3eta/4+1/4).

For 1/2<=sigma<=1, substitution into (L8) yields the relaxed bound

    |Re E_f(sigma+it)| < 2500 eta/t^2,  t nonzero.        (L9)

At t=0 use the exact signed integral (L3). No estimate proportional to
eta log t is necessary. At t>=3*10^12, (L9) is negligible in the
source numerical budget. The nonzero-frequency pole terms F(s-1)
likewise have O(eta/t^2) real parts by (L2) and the bounded leftward
shift used by the source.

## 4. Positivity and the remaining numerical obligations

Let a=2sigma-1. For z=iy,

    Re F(z)+Re F(a-conjugate(z))=Re W(iy/eta)>=0.         (L10)

The same identity holds on the other boundary Re z=a. The left side
is harmonic on 0<Re z<a, continuous on its closure, and tends to
zero uniformly as |Im z| tends to infinity. Applying the minimum
principle on finite rectangles and then letting their height grow
proves positivity throughout 0<=Re z<=a. No assertion outside that
strip is made without an error term.

The distant-zero estimate can also be supplied explicitly. Suppose
eta<=.008, |y|>=10^10, and -eta<=x<=a+eta. Since w(0)<6, three
integrations by parts and the bounds above give

    |Re F(x+iy)| < 5 eta/y^2.                             (L11)

Here are sufficient constants for the remainder: the weighted L1
norm of f''' plus |f''(0)| is less than 1600 eta on Re z>=-eta.
Indeed exp(eta u)<=exp(1.1)<3.1 on the support; the four Leibniz
terms have integrals bounded by

    3.1[1100 eta^3+1500 eta^3+750 eta^2+500 eta],

using integral h'<=1/2, integral |h''|<=a/4, and integral |h'''|<=a^2/2.
Add |f''(0)|<=500 eta^3. This is less than 1600 eta in the stated range.
The first two transform terms have real parts in absolute value at
most 3 eta(1.008)/y^2 and 1.5 eta/y^2, respectively, proving (L11).
Both x and a-x lie in this same interval. Consequently

    Re F(x+iy)+Re F(a-x+iy) > -10 eta/y^2.                (L12)

In the BTY application 1-sigma<=eta, so all zero arguments have their
real parts in [-eta,a+eta]. Thus (L12) replaces the source's constant
44 by the smaller constant 10 in its distant-zero calculation. Its
already-relaxed 10^-8 discarded-zero error remains valid without
changing T0=10^10 or H=3*10^12.

The prime-side positivity is immediate from f>=0. The exact logistic
transform is an ordinary compact integral; no inverse Laplace transform
of h is needed. Equations (L3), (L4), and (L10) therefore provide a
licensed replacement for the source polynomial smoothing, provided
the numerical proof reevaluates its transform, the t=0 archimedean
term, and any positive prime-power correction. The distant-zero error
is covered by (L12) and the source's existing zero-count calculation.
This note establishes the analytic adapter, not those numerical bounds
or a new global zero-free theorem.
