# Finite-window coercivity: an explicit high-frequency sign, not RH

**Status: proposed component proofs; independent review required. RH and the
original subexponential inequality remain unproved.**

This is an add-only continuation of PR #792 at
`2c3184545bafb4f5d873d2fa0ffc2c335a25d048`. Publication has NOT been performed
in this session. The accompanying patch is ready to apply to that base after
checking whether the live branch has advanced.

## Result

For the literal full-source damped resolvent operator `T_L` on ANY finite
interval of length L, the note constructs an explicit closed subspace V
of finite codimension on which

    <f,T_L f> >= (3/4)||phi'||_2^2 > 0  for nonzero f in V.

The primitive phi solves `phi''-phi/4=exp(-3t/4)f` with clamped endpoints.
The constraints defining V consist of two exponential moments, one cosh
moment, and finitely many Dirichlet sine coefficients of phi. All prime
powers, the entire gamma source, and the exact omitted-prime correction
are retained. No PNT, zero data, simplicity assumption or RH input is used.

An explicit gamma barrier supplies the dimension bound. At L=1, a rational
source calculation proves `Q_3<9/8`, and the choices `m=152`, `K=101` give

    n_-(T_1) + dim ker(T_1) <= 104.

This is an upper bound, not evidence that any negative eigenvalue exists.
For arbitrary L the bound is finite but can be very large. There is no
uniform bound as L tends to infinity.

## What this does not prove

The exceptional directions and their cross terms with the positive subspace
remain uncontrolled. A positive compression on a chosen complementary
finite subspace is NOT by itself a valid Schur-complement test. No bounded
inverse of the positive compact block is assumed.

Thus the result does not prove `T>=0`, positivity on all interval lengths,
or the original coefficient inequality. The general finite-codimension
phenomenon is classical: see Yoshida as discussed in Suzuki's 2026 paper.
The purpose here is an explicit adapter for the exact #792 normalization,
not a novelty claim for a general RH criterion or finite-index theorem.

## Replay

    python verify.py --check result.json
    python -O verify.py --check result.json
    python test_verify.py
    python -O test_verify.py
    sha256sum -c SHA256SUMS

The checker runs 275 finite exact rational/source controls, including the
Q_3 enclosure, gamma constants, differential multiplier identity, frequency
thresholds, endpoint cancellations and a three-mode high-frequency family.
It does not evaluate the actual infinite quadratic form or machine-prove
any infinite analytic theorem. `VALIDATION.md` records the actual runs.
