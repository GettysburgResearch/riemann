# IE26: the intrinsic floor, its logarithmic entropy, and target sensitivity

Status: PROPOSED COMPONENT PROOFS; independent mathematical review required.
**RH, J=0, and the requested growing-horizon statement (10) are NOT proved.**
Date: 2026-09-08. This is a direct attempt at the intrinsic term left by HC26,
not a review verdict and not a claimed solution of a Millennium problem.

The main identification below is a source-specific reconstruction of the
classical Balazard--Saias--Yor criterion. Its discovery is NOT claimed here.
The new work makes its exact connection to the project's two targets,
finite Toeplitz solves and sensitivity losses explicit, and supplies one
full-tail arithmetic certificate. The sign needed for completion remains open.

## 0. Literal source, metric and classical analytic boundary

Let H=L2(0,infinity), with causal shifts, inner products conjugate-linear in
the first slot and Laplace norm (1/(2pi)) integral_R |Lf(it)|^2 dt. Set

    d(t)=exp(-t/2)[floor(exp t)(1-t)+log(floor(exp t)!)],
    D(z)=(z-1/2)zeta(z+1/2)/(z+1/2)^2,
    r(z)=(z-1/2)/(z+1/2),        phi_j=R^j d.

The removable value D(1/2)=1 is analytic, not the value of a raw totalized
meromorphic product. The elementary formula 0<g(t)<=1+t, d=exp(-t/2)g,
gives ||d||_1<=6 and ||d||_2^2<=5. Integrating the floor function gives D
first in the absolute Euler half-plane and then by analytic continuation.

The unitary disk transform is

    U f(w)=Lf((1+w)/(2(1-w)))/(1-w),
    A(w)=U d(w)=w zeta(1/(1-w)), A(0)=1, ||A||_H2^2<=5.

Here dm=dtheta/(2pi) on the circle. Write A=B O, O outer with O(0)>0,
B inner, and M=closure{A p:p a polynomial}=B H2. The equality uses
classical Hardy inner--outer factorization and outer cyclicity. NO claim
that B=1 is made. Conjugation symmetry makes B's Taylor coefficients real;
write B(w)=b0+b1 w+..., so b0=1/O(0)>0.

For clarity, B has no singular inner factor. A extends analytically through
every circle point except 1. At an ordinary boundary zero, log|A| has only
an integrable finite-order logarithm; it creates no singular inner measure.
Thus any singular measure could only be an atom at 1. Its factor decays
like exp[-a(1+r)/(1-r)] along the real radius. Since
|O(r)|<=sqrt(5)/sqrt(1-r^2), such an atom would force A(r)->0. But
A(r)=r zeta(1/(1-r))->1. Hence the atom is absent.

Every disk zero is a=(rho-1)/rho for a zeta zero Re rho>1/2, counted with
multiplicity. Classical Euler nonvanishing and the functional equation are
used to locate the nontrivial zeros in the strip and reflect them. No
simplicity, finite height census or inverse-zeta critical bound is used.

## 1. IE26.1: an exact identity for the remaining obstruction

Define the absolutely convergent logarithmic integral

    J = integral log|A(e^(i theta))| dm(theta)
      = (1/(2pi)) integral_R log|zeta(1/2+it)|/(t^2+1/4) dt.    (1.1)

A nonzero H2 function with A(0)=1 has integrable logarithmic modulus, by
Hardy factorization/Jensen; log+ is also bounded by its squared modulus.
The coordinate change t=(1/2)cot(theta/2) proves the normalization in (1.1).
This is an ordinary integrable logarithm, not a chosen branch of log zeta.

The outer formula at zero and A(0)=1 give

    O(0)=exp(J),  b0=exp(-J),
    0<=J<= (1/2)log ||A||_H2^2 <= (1/2)log5 <1.              (1.2)

The nonnegative sign follows equivalently from |b0|<=1. For the UNIT
exponential target u(t)=exp(-t/2), whose disk image is 1, let

    delta = dist(1,M)^2 = dist(u,U^(-1)M)^2.

The projection is P_M1=conjugate(b0) B; consequently

    **delta=1-exp(-2J).**                                    (1.3)

Indeed M_B is an isometry and M_B*1=conjugate(b0). This proves (1.3)
without taking any limit of computed Grams.

For completeness the pure Blaschke product gives

    J=sum_(Re rho>1/2) m_rho log |rho/(rho-1)|.               (1.4)

The sum is absolutely convergent: the disk Blaschke condition and A(0)!=0
control the logarithms. Both signs of the ordinates and all multiplicities
are retained. Every summand is strictly positive. Thus

    J=0  iff delta=0 iff B is constant iff RH.               (1.5)

Equations (1.1), (1.4), (1.5) reconstruct the classical BSY criterion, not a
new easier RH criterion. In particular a small positive upper bound for J
is NOT a proof of J=0, and a positive finite approximation error is NOT a
positive lower bound for J.

## 2. IE26.2: the old ramp target has a sharp cubic sensitivity loss

The original target h(t)=t exp(-t/2) has disk image q=1-w and squared norm 2.
At horizon ZERO its intrinsic error is C0=dist(1-w,M)^2. Since

    P_+(conjugate(B)(1-w)) = (conjugate(b0)-conjugate(b1))
                                      -conjugate(b0) w,

one has the exact identity

    **C0=2-|b0-b1|^2-|b0|^2.**                              (2.1)

This is the unconstrained horizon-zero minimum, not a finite-rank error,
not a positive-horizon minimum, and not an error of a compact inverse input.

For ANY inner B with |B(0)|=x, 0<=x<=1, Schwarz--Pick gives
|B'(0)|<=1-x^2. Hence, after an irrelevant constant phase normalization,

    C0 >= 2-x^2-(x+1-x^2)^2 = (1-x)^3(1+x).

Also ||P_(M-perp)1||^2=delta and
||P_(M-perp)w||^2=delta-|b1|^2<=delta. The triangle inequality gives

    **delta^3/4 <= C0 <=4delta.**                            (2.2)

The more precise lower bound (1-x)^3(1+x) is attained by the single
Blaschke factor B(w)=(x-w)/(1-xw), 0<x<1. The ratio C0/delta then equals
(1-x)^2. Thus cubic sensitivity is real, not a weakness of this proof.
The upper constant 4 is asymptotically attained by B(w)=(x+w)/(1+xw)
as x increases to one. These are synthetic factors, not zeta zeros.

For a single hypothetical zeta zero rho=1/2+alpha+i gamma, its evaluation
constraint alone gives

    delta >= 2alpha/|rho|^2,
    C0    >= 2alpha/|rho|^4.                                (2.3)

Indeed the squared norm of disk evaluation at a is 1/(1-|a|^2),
1-|a|^2=2alpha/|rho|^2, and |1-a|^2=1/|rho|^2. Multiple constraints must be
combined by their complete Gram inverse, NOT by summing (2.3).

The practical implication is not that the old small errors are wrong.
Their target has a boundary zero at w=1 and can attenuate high-ordinate
obstructions more strongly. The new unit exponential target measures the
Jensen defect directly; its certificate is a DIFFERENT experiment.

## 3. IE26.3: the two logarithmic moments give the ramp cost exactly

Put

    J1=integral cos(theta) log|A(e^(i theta))| dm
      =(1/(2pi)) integral_R (t^2-1/4) log|zeta(1/2+it)|
                                               /(t^2+1/4)^2 dt.

The outer derivative formula is O'(0)/O(0)=2J1. Expanding zeta at 1 gives
A'(0)=gamma_E-1. Therefore L=B'(0)/B(0)=gamma_E-1-2J1 and

    **C0=2-exp(-2J)[1+(2-gamma_E+2J1)^2].**                  (3.1)

The formula is a source identity, NOT an evaluation of J or J1.
Conjugation symmetry makes these quantities real. The logarithmic moments
are absolutely convergent by Section 1 and the boundedness of cos(theta).

There is a useful strip-qualified positivity refinement. The image a of
any nontrivial zero with 1/2<Re rho<=1 obeys Re a<=|a|^2. For its normalized
Blaschke factor the logarithmic derivative at 0 is conjugate(a)-1/a.
Consequently, summing conjugate zeros with multiplicity,

    L=-sum_a (1-|a|^2) Re(a)/|a|^2 >= -2J.                  (3.2)

These sums converge absolutely; A(0)!=0 keeps the zeros away from zero,
and the remaining convergence follows from the Blaschke condition.
Each contribution to tau=2J+L is explicitly nonnegative:

    -log(1-q)-q + q[1-Re(a)/|a|^2],  q=1-|a|^2.

It is positive for q>0. From Schwarz--Pick,
L<= (1-b0^2)/b0=2sinh J. Since 0<=J<1, sinh J<=1+J, and hence
0<=tau<=2(1+2J). Substituting L=-2J+tau into (2.1) gives

    C0 = Phi(J)+exp(-2J)[2(1+2J)tau-tau^2],
    Phi(J)=2-exp(-2J)[1+(1+2J)^2]
          =8 integral_0^J t^2 exp(-2t)dt.

In particular,

    **C0 >=8 integral_0^J t^2 exp(-2t)dt.**                  (3.3)

This is a further proved positive lower bound, not the missing upper sign.
Both J and tau would be zero under RH. Neither is set to zero in this note.

## 4. IE26.4: finite arithmetic entropy decreases to J, not automatically to zero

Let G_N be the full source Gram of d,Rd,...,R^N d. Every G_N is positive
definite; no finite Gram assumes RH. Set D_N=det G_N, D_(-1)=1. Since A(0)=1,
the target 1 has cross-correlation vector e0. Thus its optimized error is

    delta_N=1-(G_N^(-1))_(0,0)
           =1-D_(N-1)/D_N.

The cofactor equality uses the Toeplitz structure; all infinite source tails
remain in G_N. Define the finite entropy

    j_N=(1/2)log(D_N/D_(N-1)) = -(1/2)log(1-delta_N).

Projection monotonicity and Hardy cyclicity prove

    **0<=J<=j_(N+1)<=j_N<=(1/2)log5,  and j_N->J.**          (4.1)

This reconstructs the relevant prediction/Szego limit. It is not an argument
that the limit vanishes. For example A(w)=1-2w has G with diagonal 5 and
adjacent entries -2, and with n=N+1,

    D_N=(4^(n+1)-1)/3,
    delta_N=3*4^n/(4^(n+1)-1) ->3/4,
    j_N -> log2 >0.

In this synthetic example the convergence to the nonzero floor is exponential.

HC26's PROPOSED quantitative-capture theorem, at the pinned #817 source,
adds a rate for the actual source. Applying its HC1 only to q=1 yields
0<=delta_N-delta<=C exp(-c sqrt(log(N+2))). Since
1-delta_N>=1/||A||^2>=1/5, the elementary logarithm inequality gives

    0<=j_N-J <=(5/2)(delta_N-delta)
              <=C' exp(-c sqrt(log(N+2))).                 (4.2)

The rate (4.2) explicitly INHERITS HC1's independent-review obligation;
Sections 1-3 and the certificate below do not depend on HC1. No numerical
value of C' or c is newly certified. Rapid convergence to J is not J=0.
The determinant ratios in (4.1) are analytic exact quantities, not newly
computed finite matrix determinants in this packet.

## 5. IE26.5: a full-tail actual-source upper certificate for J

Consider the CLOSED-DOMAIN trial f=p(R)d for the NEW unit exponential target
u(t)=exp(-t/2), where

    (c0,...,c6)=(949546,345582,16668,-144367,-201931,-191089,-125322)/10^6,
    p(w)=sum_(j=0)^6 c_j w^j.

The rational coefficients are a trial, not an asserted optimum. There is no
prefix-matching condition in this experiment and no compact-input realization
claim. The exact source domain contains every such polynomial output.
The directed certificate proves

    **||f-u||^2 <13/250,
      0<=J<=-(1/2)log(237/250)<27/1000.**                    (5.1)

The lower bound 0 is the only lower bound for J claimed. The positive lower
endpoint for the TRIAL ERROR is NOT a positive lower bound for the optimum.

Here is the complete numerical contract. Put beta_k=(-1)^k sum_(j>=k)
c_j binom(j,k). If I denotes ordinary time integration from zero, then

    p(R)d(t)=exp(-t/2) sum_(k=0)^6 beta_k I^k g(t).

On [log n,log(n+1)) the function g is affine, so every I^k g is a polynomial
in t-log n with coefficients given by its state at the left endpoint.
The squared error integral on that cell is integrated by the exact recurrence

    M_0=1-n/(n+1),
    M_j=j M_(j-1) - [n/(n+1)]log((n+1)/n)^j.

All quantities use 160-bit outward integer intervals, including logarithms.
Exactly 2047 integer cells, through X=2048, are integrated. The finite part
lies in (0.047034408869,0.047034408870).

The ENTIRE tail is bounded as follows. The periodic-Bernoulli remainder gives

    g(t)=t/2+c-1/2+r(t), c=log(2pi)/2,
    |r(log X+s)|<=1/2+1/(6X),
    |integral_0^s r(log X+v)dv|<=1/(3X), s>=0.

For the last inequality write r=d[epsilon(exp t)]/dt-epsilon(exp t),
|epsilon(exp t)|<=exp(-t)/6, and integrate. Higher primitives are bounded
by s^(k-1)/[3X(k-1)!]. Thus the entire future polynomial state is a known
smooth polynomial plus a polynomial absolute majorant. Integrate their
squares against exp(-s)/X using factorial moments and apply the triangle
inequality to their norms. The complete tail upper bound is below
0.004308660629, and the full trial error is enclosed by

    (0.047034408869, 0.051343069499).

Equation (1.3) and delta<=||f-u||^2 prove (5.1). No direct logarithmic-zeta
quadrature, gamma/zeta oracle, actual zero, or prime enumeration is used.
The copied interval arithmetic core is byte-authenticated; it is not a new
independent implementation. The numerical certificate is modest and is not
claimed to compete with bounds obtained from known zero verification heights.

## 6. Direct closure attempt: what still does not follow

The specific missing assertion in these coordinates is **J<=0**, since J>=0
has been established. I did not prove J<=0, and I did not obtain a sequence
of bounds tending to zero. This is the original BSY equality, not a new
unconditionally discharged source condition.

Three attempted completions fail precisely:

(a) The functional equation gives |chi(1/2+it)|=1 and conjugate reflection.
On that line it places no additional bound on log|zeta|; integration does
not turn (1.1) into zero. Deleting the Blaschke sum in (1.4) would assume RH.

(b) The finite entropy decreases, and HC26 supplies a rate to its true limit.
Neither fact specifies that limit. The exact polynomial example after (4.1)
obeys both excellent conditioning and fast convergence with J=log2.

(c) A small ramp-target error or a strong fixed-horizon improvement may
reflect target attenuation and removable synthesis error. Sections 2-3
price the attenuation, and the earlier optimal-tail decomposition retains
the intrinsic term. A factor-of-300 improvement cannot be iterated into
J=0 without an independently proved uniform statement.

If J=0 WERE proved, M=H2 and the intrinsic cost C(T) at every feasible
horizon would vanish. HC26 then supplies a rank schedule exp(O((1+T)^2))
for small error and FR26 supplies ordinary compact-input realization with
an explicit tolerance. That conditional chain would prove the requested
(10). Conversely a right-of-line zero rho=1/2+alpha+i gamma forces

    C(T)>=2alpha exp(2alpha T)/|rho|^4,

by delayed Laplace evaluation for h(t)=t exp(-t/2). It excludes (10).
None of these implications establishes their open premise.

A general bound illustrating the unresolved dependence is

    dist(q,BH2)^2 <=||q-Bq||^2
                 <=2(1-exp(-J))||q||_infinity^2<=2J||q||_infinity^2.

For the parent horizon targets this still has exponential T dependence.
A small FIXED J cannot be substituted for J=0 in a cofinal theorem.

## 7. What may be sent for independent review

The complete new component arguments are (1.3), the exact moment and target
identities, sharp cubic sensitivity, the strip-qualified positive refinement,
the finite entropy identity, and the new complete-tail certificate. The BSY
criterion and Hardy/Szego background are explicitly classical. The rate
corollary has a precisely declared predecessor dependency. No new mathematical
priority, zero-free region, full RH proof, Lean build or independent acceptance
is claimed. Finite tests check algebra, arithmetic and corruption handling;
they do not establish the infinite equality J=0.
