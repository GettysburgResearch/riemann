# Signed combinations: positive full-source sparse triples and growing-rank tail cancellation

**RH and the unrestricted arithmetic matrix inequality remain UNPROVED.**
Complete proposed component proofs are in PROOF.md; independent mathematical
review remains pending. No external novelty or priority claim is made.

Base: PR #790 at f0584f7a49550540eaed005868422a83cb3e1011, including BOTH
signed-tail-pass6/ and the author's imported prime-cutoff-pass6/. This packet
changes none of their files. All additions are under signed-block-pass7/.

## What is genuinely positive for arbitrary coefficient signs

For U_j(A)=A/(A+1)^j, ANY three distinct orders 5<=j_1<j_2<j_3 have
positive definite FULL arithmetic Gram matrix:

    [sum_A A^2/(A+1)^(j_r+j_s)]_(1<=r,s<=3) > 0.

This means every nonzero real combination of those three generators has positive
full heat-Hankel form, not merely positive diagonal or pair entries. The
proof uses a positive three-variable Schur factor to control ARBITRARY exponent
gaps, and retains three real low-zero evaluations BEFORE bounding the entire
unverified tail. It gives Q>(2/3) times that positive reservoir norm.

This result uses V100 from published Platt--Trudgian, plus three line zeros
in (14,15),(21,22),(25,26). The latter are separately reverified by six
interval endpoint signs with a proved eta-series tail. No simplicity is
needed. The finite-reservoir generalization states its exact rank cost.
This is a new packet deduction, not a claim that fixed-rank Hankel positivity
has never been studied.

## Actual prime-tail inequality on arbitrarily large SIGNED spaces

Set c=5/4 and

    R(A)=[c/(A+1)]^m q((A-1/4)/(A+1)),
    deg q<=D, q(-1/4)=0; all other real coefficients arbitrary.

This is exactly the D-dimensional span of U_(m+1),...,U_(m+D). Put
I=int_R R(x^2+1/4)^2 dx, G=int_R R(x^2+1/4)^2 Omega(x)dx, and let P_leX,
P_gtX denote the literal von Mangoldt Fourier sums below/above X.
For EVERY D>=1, m>=256D, and 2<=X<=exp(sqrt(m/(12D))),

    Q_X < -I/pi,
    P_gtX < -I,
    |P_gtX-G/2+P_leX| < 2pi exp(-m/2) I.

These are inequalities for the entire finite quadratic forms, including ALL
signed cross terms. The tail is strictly negative definite in the displayed
spectral metric. No zero verification, PNT, prime scan, or scalar heat
positivity is used by this theorem: the elementary source budget x>1,
y^2<=x and sum 1/x<1 suffices, together with the explicit formula.

The proof uses a Jacobi polynomial energy inequality to control the second
moment uniformly over all coefficients, and a Legendre evaluation bound to
prove |Q|<exp(-m/2)I for the COMPLETE full source. The last estimate is
TWO-SIDED, not a proof that Q is nonnegative.

## Why this is not an RH completion

The three-sparse theorem fixes support size three, but not exponent gaps. The arbitrary-rank theorem controls
prime-tail compensation but leaves the exponentially small full residual's
sign open. An exact synthetic source satisfying the same budget and positive
heat retains a negative full residual; it is NOT actual xi.

The growing spaces also escape in the original time metric:

    int_0^T |f(t)|^2dt <=(3T/m)||f||_2^2.

They cannot converge strongly, with bounded norms, to a fixed nonzero test
as m grows. Their union's linear span is not the same as the union. Thus no
unproved density passage or overlapping-triple induction is used.

## Replay and review

    python verify.py --check result.json
    python -O verify.py --check result.json
    python verify_low_prefix.py --check low_prefix.json
    python -O verify_low_prefix.py --check low_prefix.json
    sha256sum -c SHA256SUMS

The finite exact suite has 495 controls per clean mode. The six directed
endpoint signs are separate. mpmath 1.3.0 interval gamma is an explicit trust
dependency only for that certificate. See VALIDATION.md and REVIEW.md.
