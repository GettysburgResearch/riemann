# Actual-Xi companion global height: independent exact-source audit

Status: ACCEPTED CONDITIONAL COMPONENT-BOUNDARY RESULT at the frozen source
below. No mathematical repair was required. This audit does not accept a
statement about the native quotient after common-inner cancellation.

Frozen source: 9da33e7ea2b15a4badb3cb436e38e54762ad5e1d.
Authoring base: 5b25f2dace65dd4d46e16d566f2dc7a34b98f41d.
Unchanged programme import: 1428da7c3fa512be530c203a9903e99d6f8c4df7.

The [proof](XI_COMPANION_GLOBAL_HEIGHT_BOUNDARY.md), producer, complete
fixture, source manifest and tests were read. The root reviewer and a
separate reviewer independently checked the exact frozen packet. The
separate review did not coordinate its proof checks with the author.

## Accepted conclusion and the native cancellation boundary

For the actual Xi normalization, put f_k=Xi^(k), k=0,5, and fix lambda>0.
Assume RH, or directly the stated upper-half-plane inner premises for

    Theta_k=(f_k-i lambda f_k')/(f_k+i lambda f_k').

After removable real zeros are canceled, each Theta_k is a pure meromorphic
Blaschke product, up to a unimodular constant. Both component zero divisors
have infinite global unweighted height:

    sum_(Theta_k(b)=0, Im b>0) Im b = infinity.

Multiplicities are included. The conclusion is conditional and does not
assume simplicity of Xi zeros. Lambda=0 is excluded and gives the constant
quotient one.

The literal frozen-gauge source allocates the native quotient as

    U_5=Theta_0/Theta_5.

Theta_0 is the unreduced numerator component, not the denominator. If
Theta_0=G B_0 and Theta_5=G B_5 remove their maximal common inner divisor,
the accepted result leaves precisely this alternative:

    both reduced height sums are infinite;
    or both are finite and equal.

It does not decide which case occurs for Xi. In particular, neither
infinite component height nor the signed comparison below proves infinite
height of the reduced denominator B_5.

## Analytic proof checks

1. **Normalization and the RH-to-inner implication.** The actual Fourier
   kernel is positive, even and superexponentially decreasing, with no
   frequency rescaling. Its order-one growth bound permits Hadamard
   factorization. Under RH, paired real zeros give finite real-root
   polynomial approximations to Xi. Rolle, convergence of derivatives and
   Hurwitz give the real-zero property of Xi^(5). Parity removes the
   possible linear exponential in both paired products. The origin zero
   of Xi^(5) is simple because Xi^(6)(0) is a strictly negative kernel
   moment. Neither function is a polynomial, by its nonzero higher
   kernel moments.

2. **Half-plane orientation and repeated real zeros.** The imaginary part
   of f'/f is strictly negative in the upper half-plane. Hence
   Re(i lambda f'/f)>0 and the displayed Cayley quotient is contractive
   with nonvanishing denominator there. At a real zero of multiplicity m,
   each companion contains exactly the common factor of order m-1;
   removal gives the value -1. This verifies unimodular continuation
   through every finite real point without a simple-zero assumption.

3. **Actual imaginary-axis phases.** For h(y)=Xi(iy)=xi_R(y+1/2),
   the positive kernel gives h^(r)(y)>0 for y>0 and every r>=0. The
   exact relation is Xi^(r)(iy)=(-i)^r h^(r)(y); in particular the
   fifth and sixth phases are -i and -1. With D_k=h^(k+1)/h^(k),

       Theta_k(iy)=(1-lambda D_k)/(1+lambda D_k).

4. **Differentiated asymptotics.** The completed xi formula gives
   D_0=(1/2)log(y/(2pi))+O(1/y) and D_0'=1/(2y)+O(1/y^2).
   Each higher derivative bound is obtained from its own polygamma
   expansion and differentiated absolutely convergent zeta series, not
   by differentiating an unspecified asymptotic remainder. The full
   fifth Bell polynomial and all ten terms in GH14 give

       D_5-D_0 ~ 5/(y log y).

   The remainder O(1/(y^2 D_0^2)) is smaller than this main term.
   Applying the mean value theorem to the exact real logarithm gives

       y[-log|Theta_k(iy)|] ~ 4y/(lambda log y),
       log|Theta_5(iy)/Theta_0(iy)| ~ 40/[lambda y(log y)^3].

   Lambda is fixed in these limits. No uniform lambda-to-zero limit
   follows from them.

5. **Removal of singular factors.** Meromorphic-inner factorization
   allows only an exponential inner factor at infinity once finite-real
   continuation is established. Since |Theta_k(iy)| tends to one, the
   bound |Theta_k(iy)|<=exp(-a y) forces its parameter a to vanish.
   Neither finite exponential type nor finite zero-height sum was
   assumed to make this deduction.

6. **Extended height identity.** For any pure Blaschke product B,

       lim_(y->infinity) y[-log|B(iy)|]=2 sum Im b

   holds in the extended interval [0,infinity]. The individual factor
   logarithms are nonnegative. If the sum S is finite, y>=2S gives the
   summable bound 8 Im b for each scaled logarithm. If S is infinite,
   every finite subproduct supplies a lower bound, with arbitrarily
   large limiting height. This is a full extended limit, not a
   liminf-only claim. Applying it to the two components proves their
   divergence; applying it separately to their coprime reductions proves
   the stated dichotomy, without subtracting two infinities.

7. **The nonnative countercontrol has a genuine infinite-product proof.**
   The single zero i c zeta(4) and the zeros e^n+i c/n^4 define coprime
   pure meromorphic Blaschke products with equal finite height. The
   factor estimate has an error bounded uniformly in all real horizontal
   positions by 10 eta^3/y^3 for y>=2eta. The sum of those errors
   converges. After canceling the common first-height term, the remaining
   sum is

       (2c/y) sum_(n>=1) n^(-4)/(1+exp(2(log y-n))).

   Splitting at n=(log y)/2 and comparing the rest with the step function
   gives 1/[3(log y)^3]+O((log y)^(-4)), uniformly across integer cutoff
   changes. Thus c=60/lambda gives the same leading coefficient 40/lambda.
   An optional disjoint infinite-height common factor makes both
   unreduced components infinite-height without changing these finite
   reduced heights. This is not an actual-Xi divisor model.

## Literal-source and primary-reference checks

All seven primitive Git blobs and LF-normalized SHA-256 identities were
independently authenticated. Their load-bearing uses were read separately:

- XL1--XL4 at 3b697232: actual Xi Fourier normalization and positivity.
- UC2--UC6 at 76454e3d: actual companion definitions, order-one growth and
  correct opposite imaginary-axis phases.
- HC1 and HC10 at 90e8dff3: the finite global height hypothesis and the
  still unpaid physical source-tail operator.
- IW at ef7bbb8d: the corrected adjoint physical-source convention.
- L-106620.1 and .4--.6 at 81d52e56: fixed positive lambda and the exact
  C/R allocation of the native quotient.
- T-106620 at that same commit: reduced inner factors and retained
  common-zero, boundary and cofinal terms.
- L-106621 at that same commit: historical finite-window context only.

The historical finite-window height claim is not imported as a global
height theorem, and the conditional result here is not a disproof of an
appropriately scoped finite-window estimate.

The root reviewer checked the completed xi definition/reflection in
[DLMF 25.4](https://dlmf.nist.gov/25.4), the digamma estimate in
[DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2), and the separately
differentiated estimates in [DLMF 5.15.9](https://dlmf.nist.gov/5.15.E9).
The meromorphic-inner factorization was checked on rendered printed
page 4, Section 2.1, of
[Poltoratski, Toeplitz Order](https://people.math.wisc.edu/~poltoratski/ToeplitzOrder.pdf).
These are classical mathematical imports, not authenticated remote bytes
or new general theorems claimed by this packet.

## Independent exact replay

The root reviewer obtained:

- 35 supplied tests PASS normally (1.301 seconds) and under -O
  (1.304 seconds), and both producer checks PASS;
- seven Bell polynomials reconstructed by direct symbolic derivatives
  of exp(polynomial), all ten GH14 monomials and coefficient norm 181;
- four Cayley panels by independent polynomial evaluation, all three
  removable-root panels, four finite Blaschke products and their
  reciprocal-axis slopes, four cancellation panels and four tail prefixes;
- separate exact checks of the factor identity, the uniform remainder
  constant, and the constants 4, 5 and 40;
- sixteen additional resealed semantic/source/type-cap attacks rejected
  in normal and optimized Python;
- seven primitive bindings, four current artifact hashes and all five
  current-to-frozen Git blob identities PASS;
- byte-identical report and manifest emissions after LF normalization,
  in both modes; Ruff lint/format and the entire authoring-base-to-SHA
  whitespace check PASS.

The separate reviewer also reconstructed the Bell algebra through an
independent formal-exponential expansion, directly checked polynomial
Cayley/Blaschke controls, and reported 106 additional adversarial checks
per mode. Its bounded auxiliary review independently proved the extended
height limit, reduced-height dichotomy and uniform infinite-product
countercontrol. All analytic conclusions were reviewed as proofs; the
finite arithmetic panels do not machine-certify RH, factorization,
infinite products or asymptotic limits.

A transient root checking expression initially compared two structurally
different symbolic forms with literal equality. Replacing that check by
simplification of their difference resolved the false alarm. No scientific
packet file changed.

Frozen file blobs:

- Proof: e592a4c031876f56f07d28b7e18a8a7cf6e826f4.
- Producer: 8ffea00eb873b7c49f2a1e8852170cf33920d265.
- Fixture: 04498c2f37bc7d38c95de60c90cd74f86ee1f061.
- Manifest: 5e16e68864a9b6600461d99d4f4e8b91d0f78cf0.
- Tests: dc3d367b96875645e1701fe8f2b95cde54ef513b.

Fixture LF SHA-256:
f7049ea04b7cd930e84606ad79b1282d70d89c3bfbbab6e8a23351bfe7c2fa83.
Payload SHA-256:
d85e44df89abd56f9a05f34c6c5f81be846df9fdde08f394ae93a37d796ba7ea.

## What remains open

The finite-height HC theorem remains valid but cannot be applied directly
to the unreduced Theta_5 component under these premises. Applying it to
the native reduced denominator still requires control of G. Infinite
component height alone is not promoted here to a finite-band trace claim,
a failure of physical cofinal capture, or a total-charge estimate. Frozen
lambda, geographic truncation, outer factors and corrected physical
adjoints must retain their separate source contracts.

No unconditional RH result, reduced-denominator divergence, native
cofinal theorem, zero-density percentage, reverse-Rolle defect payment,
free-energy bound or novelty guarantee is accepted by this audit.
