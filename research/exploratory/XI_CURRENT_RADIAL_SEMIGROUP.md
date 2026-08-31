# Actual odd currents: radial heat limit, composition, and a universality firewall

Status: PROPOSED ANALYTIC THEOREMS; independent exact-source review pending.
Authoring base: `af809698fe6cb5046a5bcc00e9175296e4597060`.
Scope: an explicitly defined auxiliary order-to-radius Markov kernel.
This is NOT a native physical semigroup, a zero process, a source decoder,
or an RH claim. Classical Bessel heat theory is credited, not claimed new.

## Preregistered bounded algebra, before the new computation

Reconstruct radial Gaussian moments of orders0 through12 independently by
three-coordinate Gaussian expansion and by the radial generator. Check all
moment composition laws for s,t in {1/3,1,2}. Check the odd-current
likelihood-ratio polynomials for every adjacent odd pair K,K+2 with
K=1,3,...,61. Check the squared-Laplace composition algebra for every
a in {0,1/7,1,3}, s,t in {1/3,1,2}. Retain every row. These identities have
analytic proofs below; finite checks do not establish their quantifiers.

The exact finite checks do not evaluate Xi. The actual-Xi input is the
source-pinned, independently reviewed compact-kappa theorem of the parent.
A possible numerical composition scout will be separate and explicitly
non-directed; it is not necessary for the analytic conclusions.

## 1. The declared kernel and its rounding

Use the parent's literal full Xi kernel and positive odd current:
E=exp(xi), epsilon=(pi E)^(-1/2), delta=epsilon/xi, xi>0,

    H_xi(d)=Phi_Xi((xi-d)/2) Phi_Xi((xi+d)/2),
    W_K(d)=d[((xi+d)/2)^K-((xi-d)/2)^K].

Let nu_(K,xi) be the law of u=d/epsilon under the normalized density
W_K(d)H_xi(d). It is even, positive off0, and has all moments. Its density
is proportional to

    u^2 F_K(delta u) R_xi(u),
    F_K(x)=sum_(j=0)^((K-1)/2) binom(K,2j+1) x^(2j)/K,
    R_xi(u)=H_xi(epsilon u)/H_xi(0).

For r>=0 define the positive odd order

    K_xi(r)=1+2 floor(r/delta).

Thus |delta K_xi(r)-2r|<=delta, including r=0. This rule is fixed, not fitted.
For t>0 define P_(xi,t)(r,du) to be the law of sqrt(t)|U| when

    U has law nu_(K_xi(r/sqrt(t)),xi).

This constructs a Borel Markov kernel on [0,infinity). Radius r labels an
order; t is an auxiliary scaling parameter. Neither is the companion
parameter lambda, physical Fourier frequency, or a pre-existing arithmetic
time. At fixed xi the kernels need not be Feller or a semigroup.

For measures use the full variation norm, so the norm of a difference of
two probabilities is at most2. The parent proves, uniformly for kappa=Kdelta
in each fixed compact interval, weighted density L1 error O(delta+E^-1)
from

    p_kappa(u)=(2/sqrt(pi)) e^(-kappa^2/4)
                   u^2 sinhc(kappa u) e^(-u^2).

All source tails, including |epsilon u|>=xi, were included in that proof.

## 2. Exact identification of the limiting operator

For t>0,r>0,u>0 set

    q_t(r,u)=u/[r sqrt(pi t)]
                [exp(-(u-r)^2/t)-exp(-(u+r)^2/t)],

and at r=0 use its continuous limit

    q_t(0,u)=4u^2/[sqrt(pi)t^(3/2)] exp(-u^2/t).

Write Q_t(r,du)=q_t(r,u)du and Q_0(r,du)=pointmass_r.

**Theorem RS1.** Q_t is the radial heat semigroup in dimension3, with
three-coordinate Gaussian covariance (t/2)I. In particular Q_s Q_t=Q_(s+t).

Proof. Integrate the density (pi t)^(-3/2)exp(-|v-r e1|^2/t) over the
sphere of radius u. Its angular integral is
4pi sinhc(2ru/t), giving exactly q_t above, including r=0. Independent
three-dimensional Gaussian increments add their covariance. Rotational
invariance makes the radial transition depend only on the preceding
radius, so Gaussian convolution gives the displayed semigroup identity.
This also proves normalization, positivity and its continuous extension.
QED.

This is classical Bessel(3) theory with time slowed by two. For background
see Pitman--Yor, section4.4.2, pp17--18,
[A guide to Brownian motion and related stochastic processes](https://www.stat.berkeley.edu/users/aldous/205B/pitman_yor_guide_bm.pdf).
No stochastic-process theorem beyond Gaussian integration is needed here.

For a>=0, completing squares in the same three Gaussian coordinates gives

    Q_t[exp(-a u^2)](r)
       =(1+a t)^(-3/2) exp[-a r^2/(1+a t)].                 (RS1a)

At t=1, q_1(r,u)=2p_(2r)(u) on u>0. Thus the parent's sinhc profile is
not a new stochastic law: it is the classical noncentral radial Gaussian
law. The Xi question is its source-exact approximation and limitations.

On smooth compactly supported radial functions, with the usual smooth
radial extension at0, the limiting generator is

    Lf(r)=(1/4)f''(r)+(1/(2r))f'(r), r>0,
    Lf(0)=(3/4)f''(0).

This is a statement about Q, not a generator limit for finite-xi P.

## 3. Source-exact compact approximation

**Theorem RS2.** For every fixed R<infinity,t>0, integer m>=0 and T>=0,

    sup_(0<=r<=R) integral_(0)^infinity
        (1+u^m)exp(Tu)|P_(xi,t)(r,du)/du-q_t(r,u)|du
          <= C_(R,t,m,T)(delta+E^-1)                     (RS2)

for sufficiently large xi.

Proof. The order rounding has
|kappa-2r/sqrt(t)|<=delta, with kappa in a fixed compact set.
The parent weighted L1 theorem applies uniformly to every such odd order,
including K=1. Conditioning the even laws on u>0 doubles their densities
and preserves the bound. Under scaling by sqrt(t), polynomial and
exponential weights become fixed weights of the same type.

It remains to pay rounding in the comparison density. The representation

    sinhc(kappa v)=(1/2)integral_(-1)^1 exp(kappa v z)dz

shows that p_kappa and its kappa derivative are bounded on compact-kappa
sets by a fixed polynomial times exp(A|v|-v^2). Integrating the derivative
with the fixed weights proves weighted L1 Lipschitz dependence on kappa.
This adds O(delta). The identity q_t=the scaled 2p_(2r/sqrt(t)) finishes
the proof. QED.

There is no claim that C is uniform as t decreases to0, r increases
without bound, or the tested moment order increases with xi.

## 4. Fixed finite compositions really converge

**Theorem RS3.** Fix n>=1 and positive times t1,...,tn. Then, uniformly
for r in each compact interval,

    ||P_(xi,t1)...P_(xi,tn)(r,.)-Q_(t1+...+tn)(r,.)||_var ->0.   (RS3)

In particular, for fixed s,t>0 the semigroup defect
P_(xi,s)P_(xi,t)-P_(xi,s+t) tends to0 in that same topology.

Proof. For operators on bounded functions use the exact telescoping
identity

    P1...Pn-Q1...Qn
      =sum_(j=1)^n Q1...Q_(j-1)(Pj-Qj)P_(j+1)...Pn.

This orientation is important: kernels on the RIGHT contract bounded
test functions, while kernels on the LEFT are exactly known Gaussian
radial kernels. It does not require an unproved uniform tail estimate
for an iterated finite-xi chain.

Set S=t1+...+tn and choose L>R. RS2 on [0,L] gives a common constant
C_(L,t1,...,tn) and e_xi=delta+E^-1. The full variation error is at most

    n C_(L,t1,...,tn) e_xi
       +12(n-1)exp[-(L-R)^2/(3S)].                       (RS3a)

Indeed at an intermediate Gaussian radial time s<=S, starting at r<=R,
radius>L implies that a three-coordinate Gaussian vector has norm>L-R.
At least one coordinate then has absolute value>(L-R)/sqrt(3).
The elementary Gaussian Chernoff bound and a union bound give probability
at most6exp[-(L-R)^2/(3S)]. Outside [0,L] the local kernel difference costs
at most2. The first telescoping term has no exit contribution.

First take xi to infinity with L fixed, then L to infinity. Gaussian
semigroup composition gives RS3. The two-time defect follows by adding
the single-step error from RS2. QED.

This proves a fixed finite composition limit, not a growing-step-count
diffusion limit. Total variation convergence alone does not imply
convergence of unbounded moments of the iterated chain. Neither conclusion
is silently used. Bounded squared-Laplace observables do converge by RS1a.

## 5. Exact failure of the finite-xi semigroup law

The limiting semigroup must not be promoted to an exact source identity.

**Lemma RS4a.** For every odd K>=1, the ratio F_(K+2)(sqrt(z))/F_K(sqrt(z))
is strictly increasing on z>0.

Proof. Let a_j=binom(K,2j+1)/K and
b_j=binom(K+2,2j+1)/(K+2). On the common support,

    b_j/a_j=K(K+1)/[(K+1-2j)(K-2j)],

strictly increasing in j. There is an additional positive highest
coefficient in the numerator. Expanding B'A-BA, the paired terms for
indices i>j have coefficient
(i-j)(b_i a_j-b_j a_i)>=0, with strict positive contribution.
Hence the derivative is positive for z>0. For K=1 it is the immediate
identity F3/F1=1+z/3. QED.

Multiplication by the same strictly positive R_xi preserves this strict
monotone likelihood-ratio order. Therefore for any bounded strictly
increasing test function phi, the expectation under |nu_(K,xi)| strictly
increases with the odd order K. For example take phi(u)=u^2/(1+u^2).
A direct proof uses the covariance identity for two independent copies;
the product of the two ordered differences is positive on a set of
positive measure.

**Theorem RS4.** For every fixed xi>0, the entire family P_(xi,t) does NOT
satisfy P_(xi,1)P_(xi,1)=P_(xi,2).

Proof. Set r0=0 and r1=delta(1+sqrt(2))/2. At time1 these select K1 and K3;
at time2 they BOTH select K1, since delta<r1<sqrt(2)delta.
Thus P_(xi,2)phi has equal values at r0,r1.

In contrast g(v)=P_(xi,1)phi(v) is nondecreasing and nonconstant, with a
strict upward jump at each positive quantization boundary, by RS4a.
The first transition at r1 is the K3 law, an increasing nonconstant
likelihood-ratio tilt of the K1 law at r0. The same strict covariance
argument applied to this bounded step function g gives

    P_(xi,1)P_(xi,1)phi(r1)>P_(xi,1)P_(xi,1)phi(r0).

The two operator families cannot be equal. QED.

This failure is tied to the declared odd-order discretization. It is not
a claim that no other source construction could possess a semigroup law.

## 6. Universality and its source-specificity limit

The proof of RS2 uses only delta->0, the exact odd-current factors and
Gaussian concentration of the rescaled positive kernel. More generally
suppose even R_xi>0 satisfies

    R_xi(u)<=C exp(-u^2),
    integral (1+|u|^m)exp(A|u|)
        |R_xi(u)-exp(-u^2)|du ->0

for every fixed m,A. Repeat the parent's current resummation estimate;
the bound F_K(delta u)<=exp(kappa|u|) makes the product error integrable
uniformly for compact kappa. Normalizations stay bounded away from0.
RS2 without its particular rate, and therefore RS3, follow unchanged.

The explicitly substituted Gaussian family R_xi(u)=exp(-u^2) satisfies
these assumptions exactly. It is not the Xi theta source, yet it has
the SAME limiting radial semigroup. It also has the same finite-xi
discretization obstruction RS4.

Consequently this limit alone cannot select Xi, its arithmetic source,
a physical polarization, or RH. The substantive Xi input is the audited
source approximation and its rate. The classical radial law is shared
with a much broader Gaussian-concentrating class.

## 7. Exact moment controls and acceptance boundary

For x=r^2, L[x^m]=m(m+1/2)x^(m-1). Thus the exact radial Gaussian moment is

    Q_t[u^(2m)](r)
      =sum_(j=0)^m (t^j/j!)
          product_(ell=0)^(j-1)[(m-ell)(m-ell+1/2)] x^(m-j).

The finite producer compares this with an independent three-coordinate
Gaussian multinomial expansion, then checks composition coefficients.
These are identities of the LIMITING operator; they do not override
the iterated finite-xi moment boundary after RS3.

All finite arithmetic is exact rational, with certified enumeration of the
declared rows and no rounding. The analytic convergence and all-order
statements remain written proofs requiring independent review. A matching
table is not their proof. The producer must bind the literal parent proof,
parent producer/checker and source manifest, plus this note and its tests,
and reject a freshly resealed report that changes coverage or scope.

No priority claim is made for Gaussian, Bessel, likelihood-ratio, or
semigroup methods. No actual Xi zero, physical capture, native decoder,
archimedean object or principal-member selection is established here.

The bounded packet reconstructs all13 moments,117 moment compositions,
31 adjacent-order MLR polynomials and36 Laplace compositions. Seven direct
Git/LF source bindings and all four bindings in the authenticated parent
manifest are checked. The parent analytic acceptance includes its separate
non-author review; no later growing-order theorem is imported.

    python -B [-O] research/exploratory/xi_current_radial_semigroup.py --check
    python -B [-O] -m unittest tests.test_xi_current_radial_semigroup tests.test_xi_odd_current_scaling

The fixture binds the four current proof/producer/test/manifest artifacts.
Full fresh reconstruction, duplicate-key and numeric-type checks, source
tampering controls and resealed scientific-scope attacks run under both
normal and optimized Python. The finite controls require only the standard
library and do not invoke a numerical Xi evaluator.
