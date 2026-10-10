# Independent weighted rational dilation audit

Read-only hostile audit by `kappa_proof_audit`, 2026-10-10. Base:
`/workspace/riemann/research/exploratory/2026-10-10-four-hour-wave/heights`.
No Git or checkout mutation. All new outputs are in `/tmp`.

## Scoped finding

PASS for the substantive W1–W19 proof and exact checker, conditional on
the explicitly imported complete xi source, classical strip and published
complete count discrepancy. The global statement also imports the
published verified critical-line height; the tail statement does not.
The positive tail range 6n^2<=T gives largest even order
sqrt(T/6)+O(1), and at T=3*10^12 directly permits 707106, hence the
conservative global headline 700000. Smaller orders follow by principal
submatrices and repeated nodes by continuity. Increasing tail orders are
statements about changing tail kernels, not an all-order full-kernel or
RH deduction. No substantive gap found.

Minor exact qualifications identified: the strict lower side of W11 is
for nonzero R (its non-strict upper side is also valid when R=0); the
vertical depths a_b in W12 are real. The orthogonal polynomial basis in
W4 may be chosen real, even though all tested polynomial numerators may
be complex. The checker's endpoint_controls sums the known Legendre
trace formula, rather than constructing the polynomials; an independent
Gram inverse reconstruction is supplied below.

## Key gates

1. W2 is exact. Reversing a proper numerator of degree<=n-1 at b=T/t
   produces R(T/t)=T^-1 t P(t)/Q(t). The Jacobian cancels the two t
   factors in |R|^2, giving the stated norm with weight
   log(T/t)/prod(1+beta_i^2 t^2), independently of pole signs. The
   logarithmic singularity at zero is integrable. The weight is at least
   its positive endpoint value for every pole scale, with no separation
   assumption.

2. W3 is a norm-of-evaluation comparison, not a pointwise polynomial
   bound. Weighted norm >=W(1) times the unweighted norm, so weighted
   endpoint evaluation has trace at most n^2/W(1), by shifted Legendre
   orthogonality. It applies to all complex coefficient vectors using a
   real orthonormal polynomial basis.

3. W4–W7 hold for the full polynomial space. D=t d/dt preserves degree
   and has triangular matrix with real diagonal 0,...,n-1 in the
   degree-ordered orthonormal basis. Integration by parts has zero
   boundary term at t=0 because tW=O(t log(1/t)). Its Hermitian part is
   the rank-one endpoint term minus a compressed real multiplier. The
   rank-one Frobenius norm is at most n^2; the multiplier bound is
   (2n+1/28)sqrt(n). The triangular Frobenius identity is exact, including
   complex off-diagonal entries. The stated worst-case n=256 rational
   estimates prove ||D||<(13/16)n^2, uniformly for every n>=256 and every
   beta/sign. Consequently ||D^k P||<=n^(2k)||P|| for every k; no finite
   derivative extrapolation is made.

4. W8–W9 correctly return to the rational space. The extra multiplier
   1-tQ'/Q has modulus at most n+1 on the real interval. The sum of its
   allowance and the strict 13/16 polynomial bound is below n^2. Endpoint
   evaluation gives log T |R(T)|^2 <=(n^2/T) B_R, with the factor T
   restored exactly from the change of variables.

5. W10 uses the exact positive reference measure 2dN_+, including all
   off-line upper zeros with their multiplicities. Stieltjes integration
   by parts on (T,infinity) uses N_+(T)'s right-continuous value and thus
   excludes an atom at T. Its infinity boundary vanishes. The boundary
   cost is (1/2)n^2 B_R/T; the variation cost is at most n^2 B_R/T, via
   |(|R|^2)'|<=2|R R'|, 1/b<=1/T and the W8 weighted Cauchy inequality.
   The sum is exactly (3/2)n^2 B_R/T.

6. The main-density constants in W11 are correct: pi<22/7 and
   log(2pi)<2, log T>28 give lower coefficient
   (7/22)(13/14)=13/44; pi>3 gives upper coefficient 1/3. These combine
   with W10 to give the stated source sampling bound. The non-strict
   upper side applies to all proper rational numerators, including the
   transformed D^kP numerators that can vanish. This uniform coefficient
   class is exactly what the following Minkowski step needs.

7. W12 is valid with independently varying real vertical depths. The
   branch of gamma=-log(1+i a_b/b) is unambiguous near one and bounded
   by 2A/T. The dilation exponential is an exact polynomial identity.
   In the positive discrete source Hilbert space, bound each varying
   coefficient by its common supremum before using W11 and W7. Summing
   the norm bounds gives exp(2An^2/T). This does not compare arbitrary
   variable-depth sampling with one constant-height sample or restrict
   an unrelated full-axis Hardy norm.

8. W13 has the exact prefactor ratio. Each shifted denominator is at
   least (1-A/T) times its real-axis modulus; |z/b|<=1+A/T. The stated
   ratio and exponential bound follow, uniformly in signs and scales.
   Combined exponent <=q(1+2/n)<=129/768<1/5 for A<=1/2, q<=1/6 and
   n>=256, so the family amplification is strictly below 5/4. Applying
   the same argument to D^jP yields the stated bound for every j.

9. W14 is algebraically exact. With B=1-tQ'/Q, differentiating twice
   gives D^2P+(2B+1)DP+(B^2+B+DB)P. On real vertical paths,
   |i sigma x/(z+i sigma x)|<=2 and |z/(z+i sigma x)|<=2. Thus
   |B|<=3n, |DB|<=4n, |2B+1|<=7n and the final multiplier <=13n^2
   in the required range. Together with W7/W12 and |b/z|<=1, this
   gives both W15 derivative bounds. They are uniform simultaneously
   for every independently chosen depth, including Taylor remainder
   depths tau a_b.

10. W16 is the prior exact arbitrary-node congruence, restricted to the
    complete height tail. Its real symmetric moment-block quadratic
    vectors have real P; the owner explicitly clarified this premise.
    For j=0,1, z^j P(z^2) has degree at most n-2+j<=n-1. Both rational
    functions are therefore proper and in the uniform dimension-n class.
    R_- is the real-axis conjugate of R_+, with the same positive norm B.
    Their product is exactly s^j P(s)^2/q_x(s) at s=z^2, with no missing
    sign, norm normalization or pole multiplicity.

11. W17–W18 preserve all complete source weights. The two outer
    second-derivative product terms cost 2 each and the middle term
    costs 8, in units kappa^2 n^4 S(q)B/T^2. The sum is 12, hence
    75q^2 S(q)B/4 at kappa=5/4. Real coefficients and conjugate source
    groups cancel the imaginary first Taylor term. The integral
    remainder contributes exactly A^2/2 times the uniformly bounded
    derivative sum, so A<=1/2 gives 75q^2 S(q)B/32. Both reflected
    upper zeros and all multiplicities are already in 2dN_+; there is
    no extra missing or duplicated factor two.

12. W19's worst case is truly uniform. Every coefficient of its
    subtracted q polynomial is positive; q<=1/6 therefore suffices.
    At the endpoint the count cost is 1/4 and strip cost 175/4608,
    leaving exactly 379/50688>0. Complete sums and remainders converge
    absolutely by proper rational decay and N_+(b)=O(b log b).
    Invertible node congruence gives strict tail positivity for every
    distinct packet. At the published verified height, the complete
    source below or at T is a nonnegative critical-pair Gram kernel,
    so adding the strict tail proves the fixed global statement.

## Exact controls and replay boundary

Both normal and optimized Fraction checker runs passed all declared
uniform scalar guards, 16 triangular controls, 64 endpoint trace-sum
controls and sample largest-even orders. The owner clarified the real-P
premise and execution status in the manuscript during the audit; the
checker was unchanged. A final replay freeze will be recorded below.

`/tmp/review_weighted_rational_oracle.py` supplies separate controls:

- Exact inverse monomial Gram matrices reconstruct endpoint evaluation
  norms n^2 through dimensions 1–12, independently of the Legendre sum.
- At weight 29-log t (the zero-beta limiting case), exact weighted Gram
  matrices verify the endpoint comparison, integration-by-parts matrix
  identity and adjoint Frobenius identity in the actual weighted norm.
- Symbolic differentiation verifies both W14 identities for arbitrary
  numerator and denominator functions, not just a fitted polynomial.
- A rational bound e<=65/24+1/100<11/4 and the exact inequality
  (11/4)^28<3*10^12 independently certify log H0>28.
- An independent integer-square-root calculation verifies maximal even
  orders at the five checker heights and at equality/adjacent-height
  boundary cases, including enormous integer heights.

All these controls passed. Output:
`/tmp/review-weighted-rational-oracle.json`.

The source count discrepancy, all-height analytic statements and published
critical-line computation are not replayed by these finite controls.

## Final frozen replay provenance

Both independent normal and optimized executions match the retained receipts exactly, SHA256 `974265c90a69ce1f0aa98a55b716259635fb60f8a6acb81f9c2106eadf89697e`. Frozen manuscript SHA256 `2ca7783dede49c9f9c382a92ad640e30e8803db506acd672581dfd4dc5ddb2cd`; checker SHA256 `b3f0829b290e4154e6f7a0352ca944fc95038de12976237ac2ebd79d318a4947`. The coordinating reviewer independently read W1–W19 and the exact checker and concurs with the scoped result above.
