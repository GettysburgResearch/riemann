# Independent audit: auxiliary radial-current semigroup limit

Audited science: `b47af62c6efa225d731f2813e8bdf7f8b2a9a308`.
Authoring base: `af809698fe6cb5046a5bcc00e9175296e4597060`.
Immediate preregistration parent: `980801ae4c23d9482975f363390249a1b3a14ac2`.
Review date: 2026-08-31. Verdict: **PASS in the explicit auxiliary scope**.
This reviewer is not an author or co-author of the audited packet.
The frozen science and its five-file base delta were not modified.

## 1. Source reading and analytic conclusion

The complete proof, producer, tests, manifest and every fixture panel were
read. The compact-kappa parent proof and its separate non-author audit at
3f00e46e79cf928f724a9170116cb69e14f7b02f were read in full. All four parent
source notes were read at their literal Git identities, including the
actual full-line kernel proof at3b697232 and the Fourier/current/antiphase
notes L-106401, L-106500 and L-106710 at81d52e56.

The load-bearing source is the parent's weighted density L1 estimate,
uniform over odd K with K delta in a fixed compact interval. Its proof
uses the entire real source product bound, not a balanced-region-only
approximation. The current's two extra powers of u are retained. The
first-orbit correction is O(exp(-xi)), the logarithmic current resummation
costs O(delta), and normalizations stay uniformly positive. In particular
the theorem includes K=1 and kappa tending to zero. The radial packet
does not import the parent's separated-saddle or later growing-order
claims to obtain compact uniformity.

For each finite xi, every prescribed odd order defines an even positive
integrable density with all fixed moments. The piecewise-constant Borel
order selection makes P_(xi,t) a Borel Markov kernel. The exact rounding
error is delta*(1-2 fractional_part(r/delta)), of magnitude at most delta.
This includes r=0. Radius and auxiliary time are not physical lambda or
the Fourier source frequency.

RS1 passes directly by spherical integration of the three-dimensional
Gaussian with covariance (t/2)I. The angular factor is
4pi*sinhc(2ru/t); after multiplication by u^2 the displayed difference of
Gaussians has exactly the stated coefficient. The r=0 density integrates
to one, and the continuous limit is correct. Gaussian convolution and
rotational invariance prove the semigroup identity without assuming an
independent radial increment. The generator has coefficient1/4 on the
radial Laplacian, giving value(3/4)f''(0) for a smooth radial extension.

The squared-Laplace formula follows from completing squares in the three
coordinates. At t=1 the positive-half density is exactly2p_(2r), with no
missing factor of two. I personally inspected the rendered complete
printed pages17--18 of Pitman--Yor, section4.4.2: their standard Brownian
generator is one-half the radial Laplacian, so the packet's additional
factor of one-half in time is appropriate. This is classical Bessel(3)
theory, not a new probability law.

Reference: [Pitman--Yor, A guide to Brownian motion and related stochastic processes](https://www.stat.berkeley.edu/users/aldous/205B/pitman_yor_guide_bm.pdf).
The downloaded PDF SHA256 was
c2028c0e73642a0cb0ef36970f1d61fa10e1ec6e8cd2315016cdbf76d731af3c.
The cited reference supplies context; the Gaussian proof here is explicit.

## 2. Uniform approximation and composition

RS2's rounding step is paid in weighted L1. Differentiating the integral
representation of sinhc gives a common polynomial times exp(A|v|-v^2)
majorant on every fixed compact kappa interval. The normalization factor
exp(-kappa^2/4) and its derivative are bounded there. This proves the
needed Lipschitz estimate even at kappa=0. Taking the absolute value of
the even variable and then scaling by sqrt(t) preserves the claimed
fixed polynomial/exponential weight class. No t-down-to-zero uniformity
or growing moment-order constant is used.

RS3 uses the correct exact telescoping orientation: each difference
(Pj-Qj) has Q kernels on its left and P kernels on its right. The right
products contract bounded test functions; the left product is a known
radial Gaussian kernel. Hence no uniform tail estimate for an iterated
finite-xi chain is smuggled into the argument.

For r<=R, a Gaussian intermediate radius exceeding L requires at least
one coordinate increment of magnitude>(L-R)/sqrt(3). With coordinate
variance s/2 and s<=S, Chernoff and a union bound give
6 exp(-(L-R)^2/(3S)). The full variation cost of the local kernel
difference is at most2. This gives exactly the displayed12(n-1) tail
term; the first telescoping term has no Gaussian exit contribution.
First xi tends to infinity with L fixed, then L tends to infinity.
The conclusion therefore holds for every fixed finite list of positive
times. It does not prove a growing-n chain limit or iterated unbounded
moment convergence. The packet states both limitations explicitly.

## 3. Exact non-semigroup result and universality

RS4a's common coefficient ratio
K(K+1)/((K+1-2j)(K-2j)) strictly increases along the common support.
The numerator has one extra positive highest coefficient. The paired
coefficient expansion of B'A-BA yields a positive polynomial for z>0,
including the K=1 edge F3/F1=1+z/3. Multiplying both densities by the
same strictly positive R_xi preserves strict monotone likelihood order.

For RS4 the two initial radii select K1/K3 at time1 but both K1 at time2.
For phi(u)=u^2/(1+u^2), g(v)=P_(xi,1)phi(v) is bounded, nondecreasing
and has strict upward jumps. The first-step K3 law is a strictly
increasing, nonconstant likelihood-ratio tilt of the K1 law. The strict
covariance argument still applies to this discontinuous step function:
both sides of a jump have positive measure, and the tilt is strictly
ordered across them. Thus the two-step expectations differ while the
single time2 expectations agree. This disproves equality of the entire
operator family for every finite xi>0; it need not identify which one
of the two initial points witnesses the failed equality.

The proof is specifically about this odd-order quantization. It does not
exclude a different source construction with an exact semigroup law.

The universality statement retains its full weighted Gaussian-convergence
assumption and the global Gaussian majorant. The exact bound
F_K(delta u)<=exp(kappa|u|) controls the product error on compact kappa
sets. The same denominator lower bound permits normalization. Replacing
R_xi by exp(-u^2) satisfies these assumptions and preserves the limit
and the finite-xi quantization obstruction. This is a valid countercontrol
against interpreting the limit itself as a source-faithfulness criterion.

## 4. Independent exact finite reconstruction

The companion review script imports no author module. It reconstructs
the full declared fixture from the squared-radius Gaussian generating
function

    (1-tz)^(-3/2) exp[xz/(1-tz)], x=r^2,

whose coefficient is binom(m,d)*(d+3/2)_(m-d) for x^d t^(m-d).
This is an independent route from the producer's coordinate multinomial
and radial-generator loops. It reconstructs all13 moments and117
composition polynomials. For the31 MLR polynomials it uses the integral
current coefficients binom(K-1,2j)/(2j+1) and antisymmetric coefficient
pairs, not the producer's derivative-convolution routine. All36 Laplace
composition rows are reconstructed independently.

Additional controls cover17 three-time moment compositions, orders0..16,
at times2/7,3/5,11/13, and MLR pairs beginning at K=65,81,127. They also
verify the exact rational counterexample geometry1<5/4<sqrt(2).
These extra finite controls do not extend any analytic quantifier.
The held-out coefficient canonical hash is
68c2e740430c0817ab72f9363d401e3a94099c91edea5b1d40b71c1afe35cd07.

Every direct and transitive source was independently authenticated by
Git-blob identity and LF SHA256, as were all four current artifacts.
The exact base-to-source changed-file set is the claimed five files.
Fixture LF SHA256:
250a86b6c704e8ab8e3391ebaa4c41cc3039f73b8739d73770430fab2143f320.
Canonical unsigned payload SHA256:
3f0f9ab847109b9d26b2800530a8c3b8b66ec7acf62adf4139def00acbc30cf5.

Fresh review-worktree replay:

- 43 tests (19 new and24 parent), normal27.367s and optimized26.566s;
- both new and parent producer checks in both modes;
- all eight new/parent fixture/manifest emits matched exact LF bytes;
- the no-author-import review script passed in normal and optimized modes;
- eight independently resealed fresh-reconstruction attacks in each mode
  rejected changed variance, MLR sign, coverage Boolean, source identity,
  missing composition, Laplace rate, exact-semigroup scope and growing-n scope;
- Ruff lint/format and full-base whitespace checks passed.

The finite checker is relative to authenticated source bytes and exact
rational arithmetic; its matching panel does not formally verify a
probability, asymptotic, or measure-theoretic proof. The parent producer's
historically broader parser limitations remain pre-existing debt, not an
analytic input upgraded by this audit.

## 5. Accepted boundary

Accepted: the source-exact compact approximation to the classical radial
Gaussian law; fixed finite auxiliary-kernel composition convergence;
failure of the exact finite-xi semigroup identity for this quantization;
and the Gaussian-substitute universality firewall.

Not established: a native physical semigroup, growing-step diffusion limit,
iterated unbounded-moment convergence, an actual Xi zero/capture theorem,
source decoder, prescribed physical gauge transfer, outer metric,
principal-member selection, arithmetic uniqueness, or RH. No novelty or
priority claim is accepted. No source correction is requested.
