# Arithmetic completion attempt: sharper witnesses and a finite source adapter

**Proposed component results. RH and the closing arithmetic upper bound remain
open.** Read [PROOF.md](PROOF.md) for all hypotheses and derivations.

This continuation reads DG26 (#866) and the latest XCC26 (#848) at their frozen
heads, then attacks a missing quantitative connection rather than changing the
arithmetic source.

The proved proposed components are:

1. A high-order Fourier/Chebyshev approximation constructs an actual odd
   polynomial at every large degree. A hypothetical zero with real part beta
   forces Lambda_N >= c N^(b(2 beta-1)) for every fixed b<1. This removes the
   predecessor's fixed factor-ten loss without assuming uniformity as b tends
   to one.
2. The exact logarithmic growth exponents of the entire positive trace S_N and
   finite operator norm Lambda_N both equal 2 Theta-1, where Theta is the
   unknown rightmost zeta-zero supremum. This sharpens sparse quantitative
   zero exclusion; it does not evaluate Theta.
3. The actual effective rank S_N/Lambda_N is unconditionally N^o(1), improving
   the generic dimension-N bound. Thus only subpower-many eigenvalues exceed
   a fixed fraction of the largest one. This controls relative operator
   approximation, not the largest eigenvalue or capture of the full trace.
4. A finite native-source adapter gives, for N>=2,

   S_N <= 26 F_(3 ceil((2N-1)^(3/2))) + 1296,

   with F_Y=sum_(k<=Y)(sum_(n<=k)mu(n)/n)^2. It explicitly translates the odd
   Legendre source to the all-integer Newton source and pays the entire
   unresolved origin region. No future Mobius coefficient is assumed.
5. [BOUNDARY_CHANNELS.md](BOUNDARY_CHANNELS.md) retains the exact first origin
   channel instead of bounding it away. Its finite arithmetic surrogate has
   Hilbert--Schmidt error at most 11(2N-1)^(7/2)/M^3 and needs Mobius data only
   through 3M, plus 1/Z(2)=8/pi^2. Thus coverage O(N^(7/6)) pays a constant
   error; fixed higher Taylor channels bring this exponent arbitrarily close
   to one. The mixed terms remain part of the surrogate's norm.

The final arithmetic sign/upper bound is still missing. The finite adapter
consumes COMPLETE F, so XCC26's polylogarithmic collision diagonal cannot be
substituted for it while dropping its signed distinct-product covariance.

The executable check.py reconstructs bounded actual traces from two directed
even-zeta primitive routes, checks native energy identities against independent
trial factorization, checks the finite adapter, and integrates the complete
one-channel approximation error on every output cell. Its result file records
the exact coverage. No actual zeta zero, large campaign, or asymptotic law is
computed. These tests do not machine-prove the analytic theorems.
