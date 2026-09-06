# Native slow variation and the sharp Euler-tail stability threshold

**PROPOSED COMPLETE COMPONENT PROOFS; independent mathematical/code review required.
RH and native positivity at unbounded scales remain unproved.**

Continuation of PR #803 at `93e5d45b63f6a9a60f981e81df589feff1ba1cfb`.
All predecessor files are unchanged. This packet does not enlarge the preceding
native positive range or certify another all-functions window.

## Results

For the exact native annular scalar D(m), the paper proves

    -435/128 <= D'(m) <= 339/64 almost everywhere,
    |D(m)-D(n)| <= (339/64)|m-n|,
    ess sup_(m>=M)|D'(m)| -> 0.

The first two statements use elementary binomial/Chebyshev arithmetic only.
The last uses the ordinary unconditional PNT, with no effective threshold.
This improves square-grid interpolation but does not prove monotonicity.

If the prime-power source changes by at most C Lambda(n)n^(-eta), the exact
uniform scalar error norm is asymptotic to

    C J(1-eta) X^(1/2-eta),  J(1/2)=49/144.

Thus an independently positive comparison source can transfer positivity at
unbounded scales if its actual error has supercritical exponent eta>1/2, or
sufficiently small critical coefficient. Such a comparison is NOT supplied.

The attempted weaker bootstrap is rigorously obstructed. For every finite
prefix, every eta0<1/2 and every epsilon>0, the paper constructs an EXISTING
meromorphic Euler-product counterfamily with:

* strictly positive multiplicative Dirichlet coefficients and positive
  logarithmic-derivative coefficients on ordinary prime powers;
* unchanged local factors at every prime in the prefix, all powers included;
* exactly the same infinite P2=-zeta'(2)/zeta(2) moment and exact local kernel;
* coefficient error <=epsilon Lambda(n)n^(-eta0) and a PNT main term;
* every generalized Selberg derivative coefficient nonnegative at every order;
* nevertheless two-sided unbounded annular excursions on the integer samples.

The parameters are chosen by an analytic existence argument, NOT a numerical
root certificate. This is NOT zeta: its large-prime local factors differ and
its completion explicitly fails the Riemann functional equation. The native
identity Lambda*1=log is not preserved either. It does not refute a method
that actually uses those additional hypotheses. It also does not preserve an
entire safe-source jet; the last section proves the relevant uniqueness fact.

## Read and replay

Read PROOF.md, ATTEMPT_LEDGER.md, SOURCES.md and VALIDATION.md. The exact parent
proof hashes in SOURCE_LOCK.json are authenticated, not re-proved by the code.

    python -B verify.py --check result.json
    python -B -O verify.py --check result.json
    python -B test_rejections.py
    python -B test_rejections.py --optimized

For a detached archive, use --parent-root to point to the included context
folder containing annular-scalar-route/PROOF.md and
height-transfer-and-prime-squares/PROOF.md.

836 bounded controls in 15 groups are exact arithmetic checks, not 836 theorems.
No interval root for the global counterfamily, new prime/zero census, formal
build, external acceptance or remote CI execution is claimed.
