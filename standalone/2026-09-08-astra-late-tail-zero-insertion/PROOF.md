# LT26: late-tail zero insertion while preserving positive source data

Status: proposed component proofs; independent mathematical review required.
**This is not an RH proof. J=0 and the growing-horizon estimate remain open.**
Date: 2026-09-08. Parent: PR819 at c4fb013692c51d6b26b8a3c33200615af764da82.

This continuation tests the attempted inference from positive source data,
accurate finite predictions and finite conditioning to zero intrinsic entropy.
It constructs adversarial PERTURBED sources around the actual factorial source.
They are not the original zeta source, not ordinary Euler products, and not
counterexamples to RH. The literal infinite arithmetic identity is deliberately
not preserved. General Laplace/Hardy interpolation ingredients are classical;
no novelty or priority is asserted for them.

## 0. Source and objective

Use H=L2(0,infinity), the ordinary causal shifts S_T, and Laplace transform
Lf(z)=integral_0^infinity exp(-zt)f(t)dt. Let eta=1/2 and

    g(t)=floor(exp t)(1-t)+log(floor(exp t)!),
    d(t)=exp(-t/2)g(t),
    D(z)=(z-1/2)zeta(z+1/2)/(z+1/2)^2.

The value D(eta)=1 is the analytic removable value. The unitary disk image is
A(w)=(z+eta)D(z), z=eta(1+w)/(1-w), so A(0)=1.
The parent identifies the pure Blaschke factor of A and proves

    J(A)=integral_circle log|A| dm >=0,
    J(A)=0 iff RH,                         dm=dtheta/(2pi).       (0.1)

The only zero input below is the CLASSICAL EXISTENCE of a critical-line zero
1/2+i gamma with gamma>0. No simplicity, numerical height, inverse derivative
bound or unverified zero table is assumed. Fix any such gamma. Then
D(i gamma)=D(-i gamma)=0. These boundary zeros will be used to construct
changed-source controls; they are not inputs to a proposed RH proof.

## 1. LT1: an elementary strict source envelope

For every t>=0, with the right-continuous source convention,

    (1+t)/16 <= g(t) <=1+t.                                 (1.1)

The upper bound follows from
 g=1-{exp t}+integral_0^t {exp u}du.
For the lower bound first note that g decreases between consecutive log knots.
Its left limiting minimum on the nth cell is
 a_n=n(1-log(n+1))+log(n!).
The exact difference is
 a_(n+1)-a_n=1-(n+1)log(1+1/(n+1))>0.
Thus g>=1-log2>1/4.

For a second bound, put S(x)=floor(x)log x-log(floor(x)!). The complete
periodic-Bernoulli remainder (reconstructed in the parent lineage) is

    S(x)=x-(log x)/2-c+epsilon(x), c=log(2pi)/2,
    |epsilon(x)|<=1/(6x), x>=1.                            (1.2)

For completeness, its remainder follows from Stirling normalization and

 epsilon(x)=-B2({x})/(2x)+(1/2)integral_x^infinity B2({u})du/u^2,
 B2(v)=v^2-v+1/6, |B2(v)|<=1/6.

This handles every knot and is an absolutely convergent remainder formula.
Since g(t)=exp(t)-{exp(t)}-S(exp(t)), and c>1/2, we get
 g(t)>=t/2-2/3.
For t<=3 the bound g>1/4 implies (1.1); for t>=3 use t/2-2/3.

In particular d is strictly positive, in L1 intersect L2, and

    ||d||_1<6, ||d||_2^2<5,
    integral_0^infinity t d(t)dt <=20.                       (1.3)

More explicitly, g=1-t on [0,1/4]. Comparing with 1+t there and using
exp(-t/2)>=7/8 and exp(-t)>=3/4 gives

    ||d||_1 <=761/128,       ||d||_2^2<=157/32.                (1.4)

The gaps are 7/128 and 3/32 respectively. These constants are elementary
exponential-moment inequalities, not numerical quadrature.

## 2. LT2: exact horizon and jet preserving insertion

Fix ANY finite T>0, integer r>=1, and tolerance epsilon>0. There are arbitrarily
small alpha>0 and real causal sources d_alpha with all of the following:

* d_alpha=d on [0,T];
* |d_alpha(t)-d(t)|<=epsilon d(t) for ALL t>=0;
* D_alpha^(j)(eta)=D^(j)(eta) for 0<=j<r;
* D_alpha(alpha+i gamma)=D_alpha(alpha-i gamma)=0;
* every original open-right-half-plane zero of D is retained with at least
  its original multiplicity;
* d_alpha can also be required strictly positive, ||d_alpha||_1<6,
  ||d_alpha||_2^2<5, and ||A_alpha-A||_H-infinity<epsilon.

Here A_alpha is the same disk transform, not a change of metric. In particular
its first r Taylor coefficients equal those of A EXACTLY. The new zeros are
chosen off the original divisor. Their existence is a theorem about d_alpha,
NOT about D or zeta.

### 2.1 Construction in the transform domain

Set b=3/2 and the stable rational jet filter

    H_r(z)=((z-eta)/(z+b))^r.

For 0<alpha<=1/4 let lambda=alpha+i gamma and

    q_alpha=-exp(T lambda)(lambda^2+gamma^2)/H_r(lambda),
    U_alpha=Im(q_alpha)/gamma,
    V_alpha=Re(q_alpha)-alpha U_alpha.                       (2.1)

Both U,V are real and U lambda+V=q_alpha exactly. Define

    D_alpha(z)=D(z)+exp(-Tz) H_r(z)(U_alpha z+V_alpha)
                                      D(z)/(z^2+gamma^2).    (2.2)

The quotient D(z)/(z^2+gamma^2) has removable boundary singularities because
D vanishes at both boundary nodes. It is holomorphic on Re z>0. No interior
pole or unstable inverse is introduced. Equation (2.1) makes (2.2) vanish
at lambda, and real symmetry gives the conjugate zero. At eta the correction
vanishes to order at least r, proving exact jet preservation.

The original zero i gamma is isolated. We may choose alpha in a sufficiently
small punctured interval so D(alpha+i gamma)!=0. At every original interior
zero, the multiplier of D in (2.2) is holomorphic: its only possible poles
are +/-i gamma and -b. Therefore no original interior zero is cancelled.
No assertion that these are the ONLY new zeros is needed or made.

### 2.2 Causal construction and the complete tail bound

Define the two ordinary convolution functions

    C(t)=integral_0^t d(u)cos(gamma(t-u))du,
    S(t)=integral_0^t d(u)sin(gamma(t-u))du.

The COMPLETE Fourier cancellations D(+/-i gamma)=0 imply

    |C(t)|, |S(t)| <= integral_t^infinity d(u)du
                    <=(2t+6)exp(-t/2).                    (2.3)

This is not obtained by truncating an oscillatory tail. It follows by replacing
the past integral with minus the remaining full integral. Also C(0)=S(0)=0,
C'=d-gamma S, and S'=gamma C, in the ordinary almost-everywhere sense.
Consequently

    ||C||_1,||S||_1<=20,
    ||C'||_1<=6+20gamma, ||S'||_1<=20gamma.                  (2.4)

The inverse transform of H_r is the stable signed measure

    nu_r=delta_0+sum_(k=1)^r binom(r,k)(-2)^k
                   exp(-bt)t^(k-1)dt/(k-1)!.

Its exponentially weighted total variation satisfies

    integral exp(t/2)|nu_r|(dt)<=3^r.                        (2.5)

This uses a triangle bound; no cancellation or exact equality for total
variation is claimed. Now put

    e_alpha=S_T [nu_r*(U_alpha C+(V_alpha/gamma)S)],
    d_alpha=d+e_alpha.                                     (2.6)

All of these are ordinary functions. The delta in nu_r means the identity
filter on an ordinary function; it is not a delta added to d_alpha.
Equation (2.6) realizes (2.2), and e_alpha is identically zero before T and
continuous with value zero at T.

Let L_alpha=|U_alpha|+|V_alpha|/gamma. From (2.3)-(2.5),

    |e_alpha(t)|<=6*3^r*L_alpha exp(T/2)(1+t)exp(-t/2),
    |e_alpha(t)|<=kappa_alpha d(t),
    kappa_alpha=96*3^r exp(T/2)L_alpha.                      (2.7)

Thus the entire tail is controlled RELATIVELY to the literal positive source.
There is no sampled-time qualification. Further,

    ||A_alpha-A||_infinity
       <=3^r(16+20gamma)L_alpha.                            (2.8)

To prove (2.8), use (2.4), the unweighted total variation <=3^r, and
 e_alpha(0)=0 to write
 (z+eta)Le_alpha=L(e_alpha'+eta e_alpha).
Both functions on the right are integrable. The disk change of variables
therefore gives the stated H-infinity bound uniformly on the whole disk.

### 2.3 Why the parameters can be selected

As alpha decreases to zero, lambda^2+gamma^2 tends to zero, while H_r(lambda)
tends to the nonzero number H_r(i gamma). Hence U,V,L_alpha tend to zero.
For an explicit conservative dependence when alpha<=1/4,

 L_alpha <= alpha exp(T/4)(2gamma+1/4)
             (1+7/(4gamma))^r (2/gamma+1/(4gamma^2)).        (2.9)

Indeed |lambda^2+gamma^2|<=alpha(2gamma+1/4),
|H_r(lambda)^(-1)|<=(1+7/(4gamma))^r, and the definitions of U,V give the
last factor. Choose alpha small enough that kappa_alpha<min(1/1024,epsilon)
and the right side of (2.8) is below epsilon. The rational inequalities
 (1025/1024)(761/128)<6 and (1025/1024)^2(157/32)<5
then preserve both norm bounds explicitly. This proves LT2 completely.
No effective radius isolating the chosen actual boundary zero is certified;
only its standard isolated-zero property is used. This is an existence and
explicit-formula theorem, not a new actual-zero numerical certificate.

## 3. LT3: a proper subdomain with maximal projection separation

Let M=closure{R^j d:j>=0} and M_alpha=closure{R^j d_alpha:j>=0}.
The unshifted tail q_alpha=nu_r*(U_alpha C+(V_alpha/gamma)S) is in L2 by
(2.3)-(2.5). Its transform retains every interior zero of D and has no new
pole in the right half-plane. Hardy factorization therefore gives q_alpha in
M. Thus e_alpha=S_T q_alpha is a FUTURE-ONLY CLOSED-DOMAIN CORRECTION and

    d_alpha in M,   M_alpha is a proper subspace of M,
    ||P_M-P_(M_alpha)||_op=1.                              (3.0)

The inclusion follows from invariance of M. It is strict because evaluation
at lambda annihilates M_alpha, while D(lambda)!=0, so d is not in M_alpha.
For proper nested closed subspaces, the difference of the orthogonal
projections is a nonzero orthogonal projection and has norm one.
This is an operator-norm statement: small source changes do not imply small
changes of the complete cyclic-subspace projection.

This does not claim that q_alpha is generated by an exact compact L2 INPUT.
It is an ordinary L2 OUTPUT in the original closed domain. Nor is M_alpha
silently substituted for M in any RH-facing theorem. A correction can be
admissible in the original domain while its reuse as a new generator loses
part of that domain.

## 4. LT4: the entropy is strictly larger but arbitrarily close

Both A and A_alpha extend analytically through the unit circle except at 1.
The boundary poles in (2.2) have been cancelled; the other rational pole is
outside the disk. Along the real radius A_alpha(r)->1, because T>0 and the
correction in (2.2) is exponentially small at positive real infinity.
The H2 inner/outer argument of the parent therefore excludes singular inner
factors for both sources. Namely any singular mass must sit at 1; its radial
exponential decay cannot be offset by the H2 outer evaluation bound.

Both are normalized to value 1 at zero. Jensen/Blaschke factorization yields
an absolutely convergent sum of positive zero masses for each entropy.
All original interior zeros are retained. Thus

    J(A_alpha)-J(A)
      >= log(((alpha+1/2)^2+gamma^2)/((alpha-1/2)^2+gamma^2))
      >0.                                                  (3.1)

The displayed pair is only a lower bound: other new zeros are not discarded.
No simplicity is needed. The contribution of the two specified zeros is
asymptotic to 2alpha/(gamma^2+1/4).

There is also an unconditional upper-continuity estimate. Set
 delta_alpha=||A_alpha-A||_infinity. For any normalized Hardy perturbation
with this additive bound,

    J(A_alpha)-J(A)
       <=Phi_A(delta_alpha),
    Phi_A(delta)=integral log(1+delta/|A|)dm.                 (3.2)

The inequality follows pointwise from |A_alpha|<=|A|+delta. For 0<delta<=1,
log(1+delta/|A|)<=log2+log^-|A|, an integrable majorant. Dominated convergence
therefore proves Phi_A(delta)->0. Combining with (3.1) proves

    J(A_alpha)>J(A), and J(A_alpha)->J(A).                   (3.3)

For comparison with logarithmic regularization, if
 L=log(1/delta)>0 and H_A(v)=integral(log^-|A|-v)_+dm, then exactly the
pointwise Lipschitz bound for log(1+exp(y-L)) gives

    Phi_A(delta)<=sqrt(delta)+H_A(L/2).                     (3.4)

There is even STRONG convergence P_(M_alpha)f -> P_M f for every fixed f,
although their operator-norm difference is always one. To see this, write the
inner factor of A_alpha as B C_alpha, choosing C_alpha(0)>0. Divisor inclusion
justifies this factorization, and
 C_alpha(0)=exp(-(J(A_alpha)-J(A))) ->1.
Since C_alpha is inner, ||1-C_alpha||_2^2=2(1-C_alpha(0))->0. Multiplication
by C_alpha converges strongly to I, by first testing polynomials and then
using its norm one. Its adjoint converges strongly too: on each fixed monomial
it depends on finitely many Taylor coefficients, which converge to those of 1.
Consequently the projections onto C_alpha H2 converge strongly to I, and
conjugating by the isometry of multiplication by B proves the assertion.
This is the precise distinction between fixed-test convergence and a uniform
all-directions bound.

No numerical or unproved value of H_A is inserted. An independently accepted
logarithmic-tail bound could be substituted here. LT1-LT4 do NOT depend on
the HC26 quantitative-capture theorem or its Sobolev estimates.

In particular the strict positivity of the modified entropy cannot be detected
by a positive-size gap around J(A). If RH holds, these modified positive
sources have positive entropies tending to zero. That last sentence is a
conditional interpretation, not an assumption in the construction.

## 5. LT5: finite Gram and target evidence can be made arbitrarily close

Let G_K and G_(K,alpha) be the full Grams of R^j d and R^j d_alpha, 0<=j<=K,
using the unchanged all-pass filter r(z)=(z-eta)/(z+eta). If n=K+1, then

    ||G_(K,alpha)-G_K||_op
        <=n(10kappa_alpha+5kappa_alpha^2).                  (4.1)

Each entry changes by at most 2||d||||e_alpha||+||e_alpha||^2, and (2.7)
gives ||e_alpha||<=kappa_alpha||d|| with ||d||^2<5.
The common exponential-target cross vector is EXACTLY e0 at every rank:
D_alpha(eta)=D(eta)=1, and r(eta)=0. Thus no target renormalization is used.

If G_K>=g_K I and the bound eta_K in (4.1) is below g_K/2, the resolvent
identity gives

 |dist(1,A_alpha Pol_K)^2-dist(1,A Pol_K)^2|
      <=2eta_K/g_K^2.                                     (4.2)

A positive g_K exists unconditionally for every fixed K; an explicit generic
floor is the parent's exp(-8sqrt(K+4))/(K+1)^2. The perturbed sources themselves
obey that same generic floor once ||d_alpha||^2<5, since their constant
coefficient is one. The source-specific stronger floor is not claimed with
unchanged constants.

For any fixed trial coefficients c and any fixed target q, the corresponding
output changes by at most (sum|c_j|)||e_alpha||. Hence every finite collection
of strict trial inequalities and finite Gram inequalities persists for alpha
small enough. This includes complete-tail inequalities, not just finitely
many time samples. It does NOT preserve infinite exact Gram data or the
literal factorial formula after T. It does NOT apply to a countably infinite
family with no common margin.

## 6. An exact positive rational model, and the bounded verification scope

The basic boundary-to-interior motion already occurs for the explicit positive
model

    d_*(t)=exp(-t/5)(t^2-2t+5),
    D_*(z)=5(z^2+9/25)/(z+1/5)^3.

Its only zeros are +/-3i/5. For 0<alpha<2/5 replace its numerator by
5((z-alpha)^2+9/25). The inverse is

    exp(-t/5)[5-10(1/5+alpha)t
                  +(5/2)((1/5+alpha)^2+9/25)t^2].          (5.1)

Its quadratic discriminant is 50((1/5+alpha)^2-9/25)<0, so it is strictly
positive for ALL t. Its zeros are alpha+/-3i/5. Multiplying by the positive
rational constant that fixes D(1/2) preserves positivity and those zeros.
This simplest illustration has T=0 and does not enforce the higher jets;
LT2, not this example, supplies the stronger exact-horizon statement.

The checker verifies exact Gaussian-rational cancellation and jet-factor
identities, filter coefficients and total-variation majorants, constants,
Cayley zero masses (before the logarithm), the rational example, and finite
matrix perturbation bounds. Formal nonzero delay values are algebraic test
parameters in its interpolation fixtures, NOT evaluations of exp(Tlambda).
It does not calculate an actual zeta zero or evaluate the modified actual
sources numerically. Finite code does not machine-prove the analytic theorem.

## 7. Direct closing attempt, and the exact boundary it leaves

The attempted completion was to combine the actual positive source, its exact
finite prefix, safe derivatives, small entropy upper certificates, and finite
conditioning/capture into a zero-defect conclusion by stability. LT2-LT5 show
that no inference from just these data can supply that conclusion: even the
whole positive tail may be changed by arbitrarily small RELATIVE amounts,
with arbitrarily many exact safe jets preserved, while positive intrinsic
entropy and right-half-plane zeros are present.

The new sources are NOT admissible replacements in the RH proof. They change
the full factorial identity and its exact ordinary-prime zeta factorization.
In particular their extra zeros do NOT satisfy a newly proved functional
equation or an Euler product. The conclusion is a limitation on this stability
argument, not a limitation on all arithmetic methods or a counterexample to RH.
The already-proved component identities, fixed certificates and finite
convergence-to-floor results are not retracted.

The actual remaining assertion is still J(A)=0. No signed estimate proving it
has been obtained here. A successful next step must use a property of the
UNMODIFIED infinite arithmetic source that these delayed perturbations violate,
not its finite evidence or positive causal character alone. Independent review
is requested for the explicit theorem and boundaries above, not for an RH
completion with an unstated missing lemma.
