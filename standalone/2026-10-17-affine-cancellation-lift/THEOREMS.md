# Affine cancellation survives the weighted prime-power completions

Status: PROPOSED mathematical deductions with complete arguments below. The
logarithmic conclusions use the established logarithmically averaged Elliott
theorem of Tao, not RH, quasi-RH, or the newly released ordinary-correlation
claim. They have not received independent review. No full native moment or
new zero-free region is proved. Global literature priority is not claimed.

Scope: rational integers (the F=Q specialization), fixed Dirichlet twists and
fixed finite excluded-prime sets. This is NOT a theorem for aggregated
Eisenstein norm fibers, or for conductors/physical row boxes growing with X.
The arbitrary powerful-prime profiles are retained, not randomized.

## 1. Why this is a different attack

The preceding prime-exchange packet found a positive, power-sized selected
covariance. Its two arguments were proportional forms pr and qr. Positive
signs on that family do not control cancellation between opposite signs.
Here the arguments are arbitrary fixed NONPROPORTIONAL affine forms. We
prove cancellation of their COMPLETE signed correlations, with no selection
according to the sign. We then evaluate complete additive-filter mean squares
and the full fixed-additive-band part of the critical Gaussian energy.

The difficult external input is Tao's binary logarithmic Elliott theorem.
The new adapter is a uniform mean-square truncation of the actual unbounded
powerful coefficients, followed by a literal CRT reduction. A bounded-
multiplicative-function theorem cannot simply be applied to these coefficients.
For example, the coupled sixth-power coefficient has magnitude p^2 at p^6.

## 2. The four exact coefficient families

Fix an integer m>=2 and a finite set S of rational primes. Fix a Dirichlet
character xi; put all primes dividing its modulus in S. Thus |xi(p)|=1
outside S. For every p outside S choose z_p with |z_p|<=1, arbitrarily and
independently of any alleged arithmetic character law. Extend z completely
multiplicatively. At every prime of S the entire Euler factor is 1.

Write v_p=1-1/p, alpha=(m-2)/2. Define coefficients F(n) by ONE of:

    native:       1-xi(p)x;
    coupled:      1-v_p xi(p)x-z_p p^alpha x^m;
    two-channel:  (1-xi(p)x)(1-z_p p^alpha x^m);
    geometric:    1-v_p xi(p)x/(1-z_p p^alpha x^m).       (2.1)

These are formal local series; no infinite Euler product on the critical
line is presumed. The variable m is algebraic, not a claim to construct an
automorphic cover of every degree. Both occupied channels are zero at an
original nonunit/excluded prime. A fixed physical rational row can be included
by absorbing its finite exclusions into S; no uniformity in that row's
conductor or exclusions is asserted.

Let v(r)=prod_(p|r)(1-1/p). The exact nonzero supports are:

* coupled: n=r d^m, r,d squarefree, (r,d)=1;
  F(n)=mu(r)xi(r)v(r) mu(d)z(d)d^alpha;
* two-channel: n=r d^m, r,d squarefree, with NO coprimality restriction;
  F(n)=mu(r)xi(r) mu(d)z(d)d^alpha;
* geometric: n=r d^m, r squarefree, d arbitrary, rad(d)|r;
  F(n)=mu(r)xi(r)v(r) z(d)d^alpha.

All r,d avoid S. These representations are unique for every m>=2. This is
checked prime by prime: the valuations are, respectively, {0,1,m},
{0,1,m,m+1}, and {0,1,1+m,1+2m,...}. In the two-channel family shared primes
are necessary. In the geometric family they are forced. The native family
has only d=1 and r squarefree.

Write d(n) for this unique power parameter on the supported set. Put F_R(n)
equal to F(n) when d(n)<=R and zero otherwise, with R a positive integer. This is a coefficient support
truncation, NOT a prime randomization and NOT deletion of a signed pair term.

## 3. The decisive uniform mean-square tail

### Lemma 3.1 (ordinary and logarithmic mean-square approximation)

For all real x>=1 and INTEGER R>=1, all four families and every permitted powerful profile,

    sum_(n<=x) |F(n)|^2 <= zeta(2)x,
    sum_(n<=x) |F(n)-F_R(n)|^2 <= x/R.                  (3.1)

The constants here are independent of m, S, xi and the z_p. For an affine
form L(n)=an+b, with a>=1,b>=0 fixed,

    sum_(n<=X) |(F-F_R)(L(n))|^2/n
          <= (a+b)(1+log X)/R;                         (3.2)

the same bound without 1/R holds for F after multiplication by zeta(2).

Proof. For fixed d, |F(r d^m)|^2<=d^(m-2). The number of r allowed by
r d^m<=x is at most x/d^m. Drop squarefreeness, exclusions, and coprimality
ONLY in this positive upper count. Uniqueness makes the d supports disjoint,
so their square masses add. Their contribution is at most x/d^2. For the
geometric family the condition rad(d)|r can also be dropped in this count;
it gives an even smaller sum. Sum over d, or over d>R, and use
sum_(d>R)d^-2<=1/R. The native case is immediate.

The affine subsequence is a subset of the integers through aX+b<=(a+b)X.
Its square prefix is at most (a+b)X/R. Stieltjes partial summation gives
(3.2), including its endpoint term. QED.

The parameter can be generalized: replace alpha by any real value with
s=m-2alpha>1. The right sides become x zeta(s) and
x R^(1-s)/(s-1). The threshold is not removed by calling the coefficients
bounded: at s=1 the displayed tail majorant is not summable.

### Lemma 3.2 (a uniform error for complete binary correlations)

Let F_1,F_2 be two such families, possibly with different fixed m and xi,
and let L_i(n)=a_i n+b_i, a_i>=1,b_i>=0. For X>=2,

 |sum_(n<=X) [F_1(L_1(n)) conj(F_2(L_2(n)))
                 -F_1,R(L_1(n)) conj(F_2,R(L_2(n)))]/n|
       <= C_(L_1,L_2) (1+log X)/sqrt(R).                (3.3)

There is also the ordinary-average bound C_(L_1,L_2) X/sqrt(R).
Both are uniform over all powerful profiles. No signed assertion is used.

Proof. Subtract by changing the first factor, then the second. Apply Cauchy
and Lemma 3.1. Since a representation is unique, |F_i,R|<=|F_i| pointwise.
This proves both bounds. Importantly R is kept fixed while X tends to infinity,
and is sent to infinity only afterwards. QED.

## 4. The imported bounded theorem and its hypotheses

We use Corollary 1.5 (and the nonasymptotic Theorem 1.3) of Tao,
*The logarithmically averaged Chowla and Elliott conjectures for two-point
correlations*, arXiv:1509.05422v4, Forum of Mathematics, Pi 4 (2016), e8.
The exact statement and the Mobius application are on printed pages 5--6.

For fixed positive A_i, nonnegative B_i with A_1 B_2-A_2 B_1!=0, it implies

    sum_(j<=Y) g_1(A_1 j+B_1) g_2(A_2 j+B_2)/j
                       = o(log Y),                    (4.1)

for one-bounded multiplicative g_i if one satisfies the strong, uniform
nonpretentiousness condition of that corollary. The range in its distance
condition is |t|<=C Y for EVERY fixed C, not just fixed t. The source records
that the Mobius/Liouville functions satisfy it.

Every bounded function needed here has the form

    g_d(r)=mu(r) xi(r) v(r)^epsilon 1_((r,dS)=1),
    epsilon in {0,1}.                                 (4.2)

This satisfies exactly the imported hypothesis. At primes, it differs from
mu(p)xi(p) only at a fixed finite set and by O(1/p) elsewhere. The change in
each pretentious squared distance is consequently at most

    C_(d,S,xi) + sum_p p^-2 < infinity,                 (4.3)

uniformly in the frequency and in the cutoff. A fixed Dirichlet twist of
mu satisfies the same strong condition, since combining the two characters
in its distance produces another fixed Dirichlet character; conductor
primes make only a finite change. Complex conjugation of (4.2) is harmless.
This establishes the bounded input, rather than assuming it for F itself.

The difficult cancellation is imported here and credited to Tao. We do not
claim a new proof of binary logarithmic Chowla or an improved decay rate.
The statements below extend its applicability to the specific unbounded
completions by proving the missing truncation and arithmetic interfaces.

## 5. Complete signed affine cancellation

### Theorem 5.1 (unconditional logarithmic cancellation)

Let the two sources and forms be as in Lemma 3.2, with

    Delta=a_1 b_2-a_2 b_1 != 0.

Then

    sup_(all permitted z-profiles)
      |sum_(n<=X) F_1(a_1 n+b_1) conj(F_2(a_2 n+b_2))/n|
                       = o(log X).                    (5.1)

Every term is retained. The theorem permits different fixed power degrees
on the two sides. Its little-o threshold can depend on those degrees, the
forms, the fixed Dirichlet characters and exclusions. It is NOT uniform in
forms, conductors, growing degrees or arbitrary ordinary-prime phases.

Proof. For fixed d, write its contribution as

    gamma_d 1_(t_d|n) g_d(n/t_d).                       (5.2)

For the coupled source, d is squarefree,
t_d=d^m, gamma_d=mu(d)z(d)d^alpha, and g_d is (4.2) with epsilon=1.
For the two-channel source use the same t_d,gamma_d, epsilon=0 and NO
additional d-exclusion in g_d. For the geometric source put

    t_d=d^m rad(d),
    gamma_d=mu(rad d)xi(rad d)v(rad d)z(d)d^alpha,
    g_d(r)=mu(r)xi(r)v(r)1_((r,dS)=1).

These formulae include the shared prime powers exactly. For the native
source only d=1 occurs. For d<=R they are finite lists; the g_d are independent
of the powerful profiles, and |gamma_d| has a profile-independent bound.

For each pair d,e, solve the simultaneous congruences

    t_d | a_1 n+b_1,       t_e | a_2 n+b_2.              (5.3)

If incompatible its contribution is zero. Otherwise the full solution set
is ONE progression n=n_0+ell j. The moduli before CRT are

    t_d/gcd(a_1,t_d),   t_e/gcd(a_2,t_e),

and ell is their least common multiple. Take n_0 in {1,...,ell}. Set

    A_i=a_i ell/t_i,      B_i=(a_i n_0+b_i)/t_i.

These are integers, with A_i positive and B_i nonnegative. Exactly,

    t_d t_e (A_1 B_2-A_2 B_1)=ell Delta.                (5.4)

Thus the new bounded-function arguments remain NONPROPORTIONAL. The
normalization 1/(n_0+ell j) differs from 1/(ell j) by O_(n_0,ell)(j^-2)
for j>=1. The first term and this difference contribute O(1). Apply (4.1)
to the complete progression, including the coprimality factors in g_d,g_e.
This proves o(log X) for each fixed d,e.

There are finitely many such pairs at fixed R. Their coefficients are
uniformly bounded in the powerful profiles, so their sum is uniformly
o(log X). By (3.3), the limsup of the full normalized correlation is at
most C/sqrt(R). Now send R to infinity. This proves (5.1). QED.

In particular, for the actual rational coupled sixth-power source and each
fixed h>=1,

    sum_(n<=X) F_6(n) conj(F_6(n+h))/n=o(log X).         (5.5)

The inputs n and n+h can be arbitrarily large and can have any compatible
prime factors; their gcd is NOT artificially set to one. For example h=6 is nonvacuous when S={2,3}. With S empty and h=1 both
reduced cores are automatically coprime and both grow with n. Unlike the
previous pr/qr sector, this sum includes and cancels opposite signs.

The determinant restriction is necessary. For F=mu, L_1=L_2=n, the sum is
(1/zeta(2))log X+o(log X). Proportional distinct forms also need not cancel.
No two-point theorem licenses replacing Delta!=0 by merely L_1!=L_2.

## 6. The complete additive-filter mean square has its diagonal asymptotic

Assume one fixed source from (2.1). The powerful profile is fixed here,
though convergence for fixed m can be made uniform over its unit disk.
Its square-coefficient mean density is an explicit positive number delta_F.

For example, for the coupled source,

 delta_F=prod_(p in S)(1-1/p)
   *prod_(p notin S)(1-1/p)[1+(1-1/p)^2/p+|z_p|^2/p^2]. (6.1)

For the native, two-channel and geometric sources replace the bracket by,
respectively,

    1+1/p;
    (1+1/p)(1+|z_p|^2/p^2);
    1+(1-1/p)^2/[p(1-|z_p|^2/p^2)].                    (6.2)

Each good local product with (1-1/p) is 1+O(p^-2), positive and bounded
away from zero at a fixed prime. These products converge to positive values.
With the same profile, all these constants are independent of m. This
independence is not uniform convergence when m is allowed to grow with X.

Here is an elementary proof of the mean, not a Tauberian assumption. Let
q(n)=|F(n)|^2 and define the formal Dirichlet convolution h=mu*q.
Multiplying each local square series by 1-x gives a signed local correction
whose absolute coefficient mass at x=1/p is 1+O(p^-2). This follows by
retaining the linear term (v_p^2-1)/p and the powerful geometric terms,
whose square weights at this point are exactly |z_p|^2/p^2. It works also
at m=2, when polynomial degrees overlap and must first be added.
The finite primes in S cause no convergence issue. Hence

    sum_n |h(n)|/n < infinity,       q=1*h.

Dividing sum_(n<=X)q(n)=sum_d h(d) floor(X/d) by X and applying dominated
convergence yields

    sum_(n<=X)|F(n)|^2=delta_F X+o(X),
    sum_(n<=X)|F(n)|^2/n=delta_F log X+o(log X).         (6.3)

For fixed m the same coefficient majorant is summable independently of
z, so this convergence is uniform in the profiles. All phases of xi have
modulus one away from the fixed masks, so they do not alter the density.

### Theorem 6.1 (full signed finite-filter covariance)

For every fixed list of distinct nonnegative shifts h_0,...,h_(H-1)
and every fixed complex vector w=(w_0,...,w_(H-1)),

 sum_(n<=X) |sum_(j=0)^(H-1) w_j F(n+h_j)|^2/n
       =delta_F log X *sum_j|w_j|^2+o(log X).           (6.4)

For fixed shifts, the error divided by log X tends to zero uniformly on the
unit sphere sum|w_j|^2=1, and uniformly over the powerful profiles.

Proof. Expand the COMPLETE square. On the diagonal, shifting a fixed number
of places changes a harmonic square sum by O(1), using (3.1) and partial
summation of |F(n)|^2/n^2. Apply (6.3). Every distinct pair of shifts satisfies
(5.1). There are finitely many matrix entries. Their maximum error times H
bounds the operator norm of the error matrix. QED.

Thus both the positive and negative correlations of any fixed additive
window have been recombined, with a sharp leading constant. No independent
prime model, twist average, or sign-selected subtotal appears in (6.4).
It remains a logarithmic n-average and a FIXED window, not a full moment
at near-linear physical row height.

## 7. Consequence for the actual critical Gaussian pair kernel

Put c=5/6 (or any fixed real c), beta=2c-1 and

    kappa_c=exp(beta^2/2)/(2 sqrt(2pi)),
    K_D(v,z)=kappa_c/sqrt(vz) exp[-log(v/z)^2/8]
                  Phi(log D-(log v+log z)/2-beta),      (7.1)

where Phi is the normal distribution function. The full energy-pair expansion
is absolutely convergent at every fixed D: (3.1) and Cauchy give a first
absolute coefficient prefix O(x), and Gaussian partial summation bounds the
absolute smoothed sum by O(X). Its square is integrable against dX/X^2
on (0,D). Thus the unchanged Gaussian tail can be retained by Fubini.
This is the original kernel
of #952 specialized to rational integers. It includes the full Gaussian tail.
For fixed h>=1 define the COMPLETE additive-lag contribution

    C_h(D)=sum_(n>=1) F(n)conj(F(n+h)) K_D(n,n+h).       (7.2)

### Theorem 7.1

For every fixed h, C_h(D)=o(log D), uniformly in the powerful profiles.
Consequently, for every fixed integer H>=0,

 sum_(n,l>=1; |n-l|<=H) F(n)conj(F(l)) K_D(n,l)
                   ~ kappa_c delta_F log D.            (7.3)

This is a full signed fixed-additive-band asymptotic. Neither a truncation
of the Gaussian nor an averaging over Mellin twists is used.

Proof. From (3.1) and Cauchy,
sum_(n<=x)|F(n)F(n+h)|=O_h(x). Hence the paired series weighted by n^-2 is
absolutely summable. Uniformly in D, elementary differentiation of (7.1)
gives for all sufficiently large n

 K_D(n,n+h)=kappa_c/n *Phi(log D-log n-beta)+O_(c,h)(n^-2). (7.4)

The factors 1/sqrt(n(n+h)), log(1+h/n), and the bounded derivative of Phi
justify this bound; no sign is assumed. Thus its total replacement error is
O_(c,h)(1). Set S(t)=sum_(n<=t)F(n)conj(F(n+h))/n. By (5.1),
S(t)=o(log t), uniformly in the profiles. Stieltjes integration writes the
remaining main term, divided by kappa_c, EXACTLY as

    integral_0^infinity S(exp v) phi(log D-v-beta) dv,   (7.5)

where phi is the normal density. The endpoints vanish: S(t)=0 below 1 and
S(exp v)=O(1+v), while the Gaussian tail decays. For v beyond a fixed threshold
use |S(exp v)|<=epsilon v; on the bounded complement use its fixed bound.
The integral of v phi(log D-v-beta) is at most log D+O_c(1). Divide by log D
and send epsilon to zero. This proves (7.2). The diagonal is treated by the
same calculation and (6.3). Add the finitely many orientations to prove
(7.3). QED.

More generally K_D(L_1(n),L_2(n)) has the same leading form with prefactor
kappa_c exp[-log(a_1/a_2)^2/8]/(sqrt(a_1 a_2)n) and CDF centered at
log(D/sqrt(a_1 a_2))-log n-beta. Its summable O(n^-2) error gives the same
cancellation on every fixed nonproportional affine ray.

## 8. A stronger ordinary version: separate external-source gate

The October 2026 openai/math release includes an ordinary binary Elliott
claim. Its pinned scope note lean/docs/007.md and comparator
OrdinaryTwoPointCorrelations.lean include nonproportional affine forms for
one-bounded multiplicative functions satisfying uniform nonpretentiousness.
The pin is 1581d4cbdd69a0faf34b2089614fe2a814316a6a. These and the corresponding FinalMain.lean wrapper were read, but
neither the complete proof nor its transitive Lean dependency tree was rebuilt.
Comparator `sorry` tokens are specification placeholders, not proof audits.

IF that ordinary affine theorem is accepted as the external input, the
IDENTICAL proof of Section 5, using the ordinary version of (3.3), gives

    sup_profiles |sum_(n<=X) F_1(L_1(n))conj(F_2(L_2(n)))|=o(X), (8.1)

and (6.4) holds without 1/n, replacing log X by X. This is an elementary
transfer of that reported theorem, not a new proof of ordinary Chowla and
not a claimed independently verified unconditional checkpoint. The primary
logarithmic theorems in Sections 5--7 do NOT use this 2026 input.

The important reusable interface is that any quantitative bounded correlation
estimate uniform in the CRT-produced forms can be inserted before the final
limit. Concretely (3.3) bounds the discarded part by C/sqrt(R), while the
retained forms have slopes and offsets depending on d^m,e^m for d,e<=R.
No unspecified dependence on these forms may be discarded in choosing R=R(X).

## 9. Where this still stops short of RH

At every finite D, the entire Gaussian energy is

    E(D)=diagonal(D)+2 Re sum_(h>=1) C_h(D).             (9.1)

The sum is absolutely convergent at finite D, but the constants are NOT
uniform in D. Theorems 5--7 do not justify interchanging its infinite h-sum
with the limit D->infinity. Significant lags grow with D; the last mesoscopic
prime-exchange packet lies in that regime. Fixed-h cancellation is therefore
consistent with its positive D^(1/4) selected covariance.

The missing target is a quantitative joint estimate for those growing lags,
with enough total signed cancellation to make E(D)=D^o(1). A general ordinary
fixed-affine result, without sufficiently strong dependence on its slopes
and offsets, also does not supply that target.

We have NOT transported this proof to the coefficients aggregated from
Q(omega). Those norm fibers are divisor-sized and contain a different
convolution; the bounded skeleton and square-summable powerful tail proved
here do not silently establish their affine nonpretentiousness. Returning to
the rational specialization is deliberate: it directly retains an RH-bearing
Mobius source, while allowing the external binary-correlation theorem to
be applied with its actual hypotheses.

The contribution is a rigorous source-preserving lifting theorem and its
complete signed additive-filter/Gaussian-band consequences. It is not a
first proof of Tao's theorem, an all-field Elliott theorem, or a full RH proof.
