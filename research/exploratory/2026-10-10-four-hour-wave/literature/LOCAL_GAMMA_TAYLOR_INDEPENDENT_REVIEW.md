# Independent local gamma Taylor / Taylor phase8 audit

Date 2026-10-10. Read-only checkout/Git. Scoped PASS: no substantive
mathematical or implementation gap found in the local evaluator or the
new phase8 / weighted provenance deltas. The full continuum integration
receipt remains a separate runtime requirement; these controls do not
claim that it has already completed.

## Complete analytic enclosure

* LOCAL_GAMMA_TAYLOR_ENCLOSURE.md T1 is the exact reviewed literal
  gamma kernel split Gamma=A+B log x. The normalized quotient at zero
  has removable value one. On |x|<=1, its distance from one is at most
  e-2<3/4, and the normalized plus factor has distance from one below
  7/8. Both lie in disks excluding zero and the logarithm cut; the
  strict margins give a neighborhood of the closed disk.
* The complex logarithm bounds are log4<3/2 and log16<3. Combining
  them with exp(1/2)<2 and exp(3/2)<5 gives |A|<47/6<8 and
  |B|<5/3<2. Thus the Cauchy coefficient and complete geometric tail
  bounds in T3 are valid, not fitted numerical bounds.
* For the native real or purely imaginary frequencies, Re z<=3/2.
  The exponential remainder delta_E is a valid absolute series bound
  on the whole path. Guarding delta_E<1 gives |E_e|<3. The literal
  positive decreasing gamma series gives 0<Gamma(x)<=Gamma(0)<2/5.
* Splitting the product error as (Gamma-Gamma_d)E_e plus
  Gamma(exp(zx)-E_e), and integrating the entire x^(d+1) log x tail,
  gives exactly T5, with exponent d+2 and the displayed two inverse
  powers. It retains all product degrees through d+e. Endpoint zero
  is integrable; no false analytic Taylor expansion of log x is used.
* The complete T5 bound increases with the endpoint. Its numerator's
  derivative has positive bracket 8-2 log a; 1/(1-a) and the exponential
  term also increase. Caching the radius at the entire tier cutoff
  therefore covers every positive length in that tier, including
  arbitrarily small positive lengths and uncertain real balls.

## Directed helper and precision

* taylor_convolution_source.py lines 16–30 raises cap to 66 and
  constructs exp(-x) through degree 65, so division by x retains all
  regularized quotient coefficients through degree 64. The A/B final
  series precision is checked before their coefficient arrays are read.
* Lines 36–61 raises cap to d+e+1. It forms the polynomial exponential
  through e, explicitly pads it and the degree-d A/B polynomials to
  that precision, and multiplies before integration. The final products
  are checked at the full precision and every coefficient is retained.
  The plain and logarithmic primitive coefficient formulas are exactly
  T4. The outward error rectangle uses the full directed upper T5 radius.
* Lines 64–73 selects a local tier only if the entire length ball is
  strictly positive real and contained below 3/10, and real frequencies
  satisfy |Re z|<=3/2. Length/frequency cases outside that scope keep
  the unchanged reviewed implementation. A failed exponential remainder
  guard raises ArithmeticError even under -O.
* Successful paths restore the incoming cap, including a nondefault cap.
  Minor wording qualification: the final A/B and product precisions are
  explicitly checked. Intermediate exp(-x) and exp(zx) precisions rely
  on the correctly raised cap and the FLINT formal-series precision
  contract; there is no separate .prec assertion before reading those
  intermediate arrays. The raised caps and current implementation do
  give the required precision, and independent full-coefficient controls
  passed. This is a documentation qualification, not a lost coefficient.
* The accelerator is real-axis-only. It returns outward enclosures for
  the same literal source at the real Gauss nodes. The pre-existing
  analytic Cauchy bounds refer to that exact source and remain valid;
  they are not inferred from the real-only polynomial approximation.

## Exact replays and independent oracle

Normal and optimized check_local_gamma_taylor.py runs passed and are
byte-identical to each other and to the owner receipt:
SHA256 f9756284bcbb4f82e5603715156da94a91abdf5f6f46e9cba0c37e626a84ea89.
They contain 84 closed-form overlap controls, 5 independent literal
4096-term integral controls with complete tail 1/(8*4096^2), 3 fallback
controls and series-cap restoration checks. The literal tail follows
from lambda-Re z>=j and lambda^2-b^2>=4j^2; its complete integral bound
is valid for each tested frequency. Overlap is correctly labeled as a
consistency control, not an analytic proof.

The independent oracle /tmp/review_local_gamma_taylor_oracle.py reconstructs
all 65 A/B coefficients from Bernoulli identities for log cosh(x/2) and
log(sinh(x/2)/(x/2)), with exact rational arithmetic. It separately
reconstructs all 161 first-tier product coefficients by finite convolution,
including the highest retained degree 160. Full product degrees are
160,320,576 in the three tiers. The mathematical top logarithmic
coefficient is zero by parity, but outward zero-enclosing coefficient
balls may still retain that top polynomial degree; this is safe.
It also verifies restoration of cap 7, threshold-straddling real balls
selecting the next safe tier, a ball crossing 3/10 selecting the fallback,
and an oversized frequency failing the complete exponential error guard.
All oracle controls passed in normal and optimized modes with
byte-identical output, SHA256
dc85fccb5ea475c2b7bca44b1b2b775ff1e52651a58b36b370a0e446e21942a5.

Outputs are /tmp/review-local-gamma-taylor-{normal,optimized}.json and
/tmp/review-local-gamma-taylor-oracle.json. Owner artifacts were preserved.

## Separate producer and weighted wrapper

The source diff of enclose_residual_phase8_taylor.py against the original
phase8 producer contains only its descriptive header, substitution of
TaylorConvolutionSource for ConvolutionSource, and the new helper hash in
the receipt. Every original kernel, trial, projection, panel, Gaussian
rule, omitted-interval, analytic bound and scalar 27/2 matrix calculation
is preserved. The producer and original remain distinct files.

enclose_weighted_lower_taylor.py restricts removed to 5 before using its
frozen mapping. It binds the exact new phase8 producer hash in both the
input receipt and current producer file, the local helper in both input
receipt and current helper file, and the pre-existing Source U / closed
convolution helpers. It retains the endpoint/order/precision/trial-count,
exact coverage, source U and exact trial-coefficient comparisons. Its
matrix/moment weighting and all source/parameter guards are unchanged.
The original weighted checker remains unchanged. It does not constitute
an independent full continuum integration replay, as explicitly stated.

The wrapper may accept a source-valid R receipt whose scalar 27/2 lower
bound was inconclusive: the weighted pricing is the distinct target.
Incomplete diagnostic receipts lack the full R/source/coverage data and
cannot pass the retained guards.

## Frozen sources

Proof e28980ff704350db547dc2843bcf5551ffdad5d49a21a0f6483f0b0cf0765e52.
Helper 118e828d8bf4cb706fd94c9d179fb8d8de88319df8b20273c4e19284175af0da.
Checker 2f881c44b5b72e20f2777a5c9de0884c3217692789f05615283a5442898079e8.
Phase8 Taylor producer f10b2dad34ab16aa6f66f4693093be60657b5d395432bf29f1af33ede8bf3256.
Weighted Taylor wrapper 0ba57657eef0ea728134e846c2861f778793715c5d091c3c47090cc87f003f25.
Reviewed source convolution d53aa6c4e9c0e33d26c2327305bc1aa0ae9adef035ea4437ccd2a19b23bbf014.
Reviewed source U b3832a0cddc8bc1e2603c40240b608d1f06a868bda9436d8e88a146393fe007b.
