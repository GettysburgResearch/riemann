# Independent native-window and primitive completion audit

Date: 2026-10-10. Read-only checkout/Git. Scoped PASS for the analytic
implication and exact extraction code. No actual completed continuum R
or weighted lower receipt was replayed in this audit, and no numerical
native lower sign is inferred from a pending computation.

Reviewed files and SHA256:

- NATIVE_WINDOW_CERTIFICATE_FRAME.md:
  5c3dbb70dca1506ca7e8b63e27572b92d73a5573aff3298ce0a50267d7e0a20c.
- QUANTITATIVE_PRIMITIVE_COMPLETION.md:
  a7c9dcbd4923dbbbe3172070c5bc4400b4465f3d90675020b936294133780251.
- enclose_primitive_norm.py:
  a84255c51d8409fa33ab00ddbab42199e0e19a86a44bb066dcaf7740d657a5f0.

## Complete weighted residual implication

The frame lines 84-115 use the exact native decomposition h=z_x+w with
w in V. The imported coupling and mode-dependent energy inequality
imply both the completed-square lower bound and the dual inequality
|q(w,z_x)|^2 <= q(w,w) x*B_N*x. In particular, the factor b and factor
2 for unnormalized cosine moments are correct. The inverse lambda_n
decreases with n. R is the complete L2 residual Gram matrix, so Parseval
uses the entire remaining cosine tail; no high modes are truncated.
All finite correction weights are positive. Therefore B_N is PSD and
a valid complete dual upper bound. A true outward U-B_N >= 1e-11 I
does give strict positivity when x is nonzero. When x=0, the primitive
gap and injectivity give positivity directly, without an L2 minimizer.

The native q convention in OPERATOR_AUDIT.md lines 42-46 is antilinear
in the first argument. The frame writes U_ij=q(z_i,z_j), while the
quantitative note writes U_ij=q(z_j,z_i). This is harmless for these
specific tests: the real kernel, exact real basis and exact real Galerkin
solve make U real symmetric. Consequently x*U*x is the same native
quadratic form for all complex x. No complex extension is omitted.

Frame lines 117-121 correctly transfer the native literal kernel form
by zero extension from a shorter interval. This needs the same W and
fixed b, which are exactly the inherited native normalization. It says
nothing about L>1 or an L2 spectral gap.

## Quantitative primitive reserve

The Young inequality in the quantitative note lines 58-71 is valid for
complex tests and q(w,w)>=0: the cross term is bounded by
(1-theta)q(w,w)+(x*B*x)/(1-theta). For
theta=epsilon/(2M+epsilon), theta/(1-theta)=epsilon/(2M).
PSD B has operator norm at most trace B <= M, so the remaining finite
reserve is at least epsilon/2. There is no unstated lower spectral gap
against ||w||_2.

The synthesis estimate lines 73-83 follows by Hilbert-space Cauchy:
||G z_x||^2 <= (sum_i ||G z_i||^2)||x||^2. Orthogonality gives
Pi_E h=e_x, hence the norm comparison with coefficients 1+2K and 2
is correct. The prescribed delta pays both terms simultaneously.
The Volterra G is the derivative of the initial-value primitive for
every native L2 h; G h=0 forces h=0. Zero extension restricts G exactly
to G_L, and its full squared norm is at least the restricted norm.

The Hilbert--Schmidt bound and cosh series remainder in lines 87-106
are valid: the first omitted term after 1+1/8 is 1/384, and the later
ratios are <=1/120. Their rational sum is 2147/1904<6/5, giving
||G||^2<18/25. The projected high sines have norm <=1, and e_i is
orthogonal to u_i, so the column absolute-sum coefficient bound indeed
controls sum_i ||G z_i||^2. The upper producer lines 202-217 identify
the high-sine coefficient rows exactly as minus the Galerkin coefficients.

## Extraction guards and directed endpoints

enclose_primitive_norm.py lines 46-66 binds a completed residual file by
its exact byte SHA, chooses one of the two reviewed weighted checker
hashes, verifies that current file, and reruns it at last=128/bits=256.
Full semantic identity ignores only elapsed times and a movable path;
it retains all numerical matrices, source/producer hashes, actual input
SHA, trial coefficients, primitive certificates and mathematical fields.
The status, positive 1e-11 reserve and m in {5,11} are then required.
Both frozen weighted checker hashes match their current files:
cc96f85d80d348bc3e2f11ab37e2b7f4c9d4eedfcda16b5a8533b32c1f1ce236
and 0ba57657eef0ea728134e846c2861f778793715c5d091c3c47090cc87f003f25.

Lines 67-85 extract trace(U-(U-B)) from independently enclosing ball
entries. Lost dependency can widen this bound, never narrow it. Its
finite directed upper endpoint and exact integer ceiling give M>=1
and M>=trace B. The complete d+100 by d inventory is checked before
using all 100 high-sine rows; outward absolute endpoints and an upper
integer ceiling give a safe K. The imported gaps 1/6 and 6/5 agree with
the reviewed supporting lines. Epsilon, theta and delta remain exact
Fractions; the decimal float is explicitly display-only.

exact_upper uses the finite exact upper Arb endpoint's mantissa and
binary exponent, preserving an exact rational upper bound. The ceiling
formula works for every sign, and max(1,...) preserves the required
M>=1. Nonfinite endpoints fail via an explicit require that survives -O.
No permissive catch, sampled matrix or synthetic receipt is accepted.

The parent's independent rational/endpoint controls are present at
/tmp/review-primitive-{normal,optimized}.json and are byte-identical:
2 supporting-line constants, 54 exact Young/synthesis comparisons,
24 dyadic endpoint/ceiling cases and 2 nonfinite rejection controls.
This audit independently checks the analytic argument and extraction
logic, rather than repeating a full source integration.

No mathematical gap found. The conclusions remain conditional on an
actual completed outward weighted lower receipt and inherited O1-O4;
all L>1 and the all-window positivity gate remain open.
