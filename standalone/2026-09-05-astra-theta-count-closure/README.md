# Astra: theta-count closure, positive invariant heat, and the Bernstein boundary

Status: PROPOSED PROVED COMPONENTS + AN OPEN RH-EQUIVALENT FINAL GATE.
Independent mathematical and code review is requested; none is claimed done.
Scope: actual Riemann xi, the native theta occupation mixture, explicit
counterfeits, and a finite-exterior compactness theorem.
Exact base: main@6dda8b5125457ed936330229f8c9eb6491728e76.
Primary predecessor: PR #785@9a965c26fd3e0310736829689db1734bcb5c3ec4.
What was actually run: 225 exact rational checks in each interpreter mode,
a two-ordinate directed interval sign-change certificate in each mode,
and two deliberately corrupted-result rejection checks. See VALIDATION.md.
Smallest remaining gap: all mixed Hausdorff differences of the source
cumulants; equivalently complete monotonicity of the invariant zero heat.

**RH remains unproved. This packet does not claim an end-to-end proof.**
It is a dedicated, add-only research continuation, not an integration verdict.
No predecessor, canonical registry, formal module, or main file is changed.

## Strongest positive result

For

    X(u)=xi(1/2+sqrt(u+1/4)),       h=X'/X,
    S(t)=sum_(rho=beta+i gamma, gamma>0) exp(-rho(1-rho)t),

with zero multiplicities retained, the analytic proof establishes

    S(t) > (1-2^(-83)) exp(-226t),              every t>0,

and hence

    (-1)^(n-1) h^(n-1)(u)
       > (1-2^(-83)) (n-1)!/(u+226)^n,          n>=1, u>=0.

Only the published zero verification BELOW HEIGHT 100 is imported, together
with a separately replayed first-zero existence certificate in (14,15).
The entire unknown tail is bounded analytically. No simplicity is needed.
Thus log(X(u)/X(0)) is a Bernstein function and every positive power of
X(0)/X(u) is a completely monotone, infinitely divisible Laplace transform.
This is the Bernstein layer, NOT the RH-equivalent Stieltjes layer.

## The attempt at complete closure

The literal theta scale mixture has positive conditional Bernoulli fibers.
But every pair of its occupation marks has strictly POSITIVE covariance.
A Hermitian determinantal process has nonpositive pair covariance, so an
exact mark-preserving quasifree dilation is impossible. Even sufficiently
high tail COUNTS are overdispersed and cannot be such determinant counts.
This does not refute an unmarked count determinant or RH.

The repaired route retains all connected cumulants before testing signs.
For P_v(z)=X(vz)/X(v), put

    p_n^*(v)=(-1)^(n-1)n[y^n]log P_v(1+y),
    H_(a,b)(v)=sum_(j=0)^b(-1)^j binom(b,j)p_(a+j+1)^*(v).

The heat theorem proves p_n^*(v)>0 for every n,v, with an explicit lower
bound. At ONE fixed v>0, H_(a,b)>=0 for ALL a,b is equivalent to RH.
The b=0 face is proved; the full mixed family is not. Its exact Laguerre
integral and finite-partition source-cumulant formula are provided.

An explicit quartet insertion at centered zeros +/-1000 +/-i/4 retains a
smooth positive Fourier source, strip confinement, the low zero prefix,
zero-count asymptotic, and all proved Bernstein signs, but has nonreal zeros.
A smaller polynomial gives the exact mixed witness
H_(0,14)=-433316717939/10^15. Thus the final gap cannot be replaced by a
positivity or finite-prefix slogan.

Finally, finite positive-contraction exterior approximants with bounded
trace would already give an exact contraction determinant: order below one
excludes escaped Poisson mass. Separate projective consistency is unnecessary.
No such approximants for actual X are constructed in this pass.

## Reading and review order

1. [HEAT_BERNSTEIN.md](HEAT_BERNSTEIN.md): all-time heat proof and all-order signs.
2. [THETA_COUNT.md](THETA_COUNT.md): native marked obstruction, tail theorem,
   connected cumulants, and complete conditional RH endpoint.
3. [COUNTERFEITS.md](COUNTERFEITS.md): exact sharpness controls and exterior limit.
4. [REVIEW.md](REVIEW.md), [VALIDATION.md](VALIDATION.md), and [SOURCE_LOCK.json](SOURCE_LOCK.json).

Local claim identities ASTRA-TC-01 through ASTRA-TC-12 are scoped to this
packet; no historical numeric claim namespace is reused. Classical inputs
and prior repository structures retain their credit. No external priority
or novelty claim is made before specialist literature review.

## Reproduce the bounded evidence

    python verify_exact.py --check exact_result.json
    python -O verify_exact.py --check exact_result.json
    python verify_low_zero.py > /tmp/astra-low.json
    cmp /tmp/astra-low.json low_zero_result.json
    python -O verify_low_zero.py > /tmp/astra-low-opt.json
    cmp /tmp/astra-low-opt.json low_zero_result.json
    sha256sum -c SHA256SUMS

The exact checker is standard-library-only. The low-zero script requires
mpmath==1.3.0. The scripts do not machine-prove Jensen/Hadamard/Laplace
arguments, replay Platt--Trudgian, prove the mixed sign family, or prove RH.
