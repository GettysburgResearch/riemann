# Independent review and exact replay of the variable-sigma detector

2026-10-21. The Type-I agent reviewed the following frozen files:

* `../three-hour-boundary/VARIABLE_SIGMA_LOGISTIC_DETECTOR.md`, SHA256
  `b996d3f1ee0e5f674b0fda0f00ec60c90c9d7886e622233ceabfde86541a9f4c`;
* `../three-hour-boundary/SHIFTED_SECH_POSITIVITY.md`, SHA256
  `2a0143aad2ab349843dc27a0a52ee6cff9a4edc1b41619b9d903901e75a62964`;
* directed producer `certify_variable_sigma.py`, SHA256
  `8860a3d2f38b92ece03494ed2c4219116d4183f67f25fa163b8478e189ae9337`;
* its margin source `probe_variable_sigma.py`, SHA256
  `c229caa9fea5820d965af5ca13c7d3275f15e63abdf66ec2d70c1fcd42d6be03`.

No issue was found in the new interfaces. The reciprocal cosh product
makes sech(sqrt(s)) completely monotone. Squaring and multiplying by
1/(2sqrt(s)) gives the completely monotone derivative of tanh(sqrt(s)),
so the latter is Bernstein. The reciprocal affine composition is
completely monotone, and the hyperbolic addition identity has the
correct sign and normalization. Its Gaussian-mixture representation
therefore proves positive definiteness of sech(a+b|k|), including the
shift a. The exact two-square representation of the polynomial then
proves positivity of the combined arithmetic term, separately for
every n. This argument does not assume equal smoothing functions.

The finite retained-prime comparison has coefficient3/2: the factors
are eta/2, w<=6, and |sech'|<=1/2. Its remaining factors are exactly
sum k*a_k and sum(log p)^2*m*p^(-m/2), giving the stated168*eta*delta.
Only the retained terms incur this loss; dropping the rest is licensed
by the preceding arithmetic positivity. The previously certified
constant-sigma prime lower bound applies at sigma_0.

The individual cutoff inequality is in the favorable direction:
c+kd>=C_k implies (c+kd)/l>=C_k/(l+C_k). Thus each sigma_k controls
all zeros below kt+T0, while k=0 uses the verified finite-height range.
The common eta still bounds1-sigma_k. Consequently each discarded-zero
pair lies in the same adapter strip. The direct Lehman estimate in the
baseline already enlarges its integration range to q+T0, so it remains
valid when that is the actual cutoff. Its use here does not silently
retain a common12t+T0 cutoff.

The explicit formula is applied separately before summation. The
common f_k(0), positive a_k and sigma_k<=1 preserve the gamma bound.
The real correction is the old bound at(sigma_0,f_0); the high-frequency
errors remain inside the same uniform parameter domain. The pole
transform uses alpha_0, while both selected transforms use alpha_1.
Those distinctions are correctly retained in the sufficient inequality.
The global minimum-zero argument is the previously reviewed one, with
the new target Astar=1000/4813 and the individual cutoffs just checked.

## Independent exact arithmetic

`verify_variable_sigma_fraction.py`, SHA256
`e4cd2cadf3f8512f4956f311c7bba924a7c015c9aa1d61a523c46473f3f4c3db`,
reconstructs the margin using the frozen exact Fraction arithmetic and
kernel moments, independently of mpmath. It certifies all of

    A in[0,1000/4813],      log(t) in[28,8241/100].

Normal and optimized Python runs produce identical output. There are
59 accepted closed rectangles after117 evaluations. The minimum lower
margin exceeds6.24493e-7. Exact containment, pairwise disjoint interiors
and total area54410/4813 certify complete coverage. The unsupported
point A=1/4 is rejected. All cutoff logarithms, prime-loss constants,
eta/sigma ranges and Littlewood endpoint are independently enclosed by
exact rational series. Floating output is informational only.

The certificate `VARIABLE_SIGMA_FRACTION_CERTIFICATE.json` has SHA256
`ba4c7bee6612ba37e588db84df6fedbe5bdf52c415bc726b53e638c071560ed0`.

The resulting proposed classical denominator is4.813. This review
does not establish a new fixed-width Hecke boundary or RH. It depends
on the separately reviewed logistic explicit-formula adapter, exact
kernel and prime certificates, published finite RH verification,
Littlewood region and Lehman zero count. Independent human review of
the assembled mathematical proof remains outstanding.
