# Rational capture of the complete residual form

Status: proposed component proofs; independent mathematical/code review required.
RH and a subpower arithmetic upper bound remain UNPROVED.
Date: 2026-09-08. Continuation of PR #803 at bcec690c1607e281bd6f741b68f5c50f556670c7.

The load-bearing result is a uniform multiplicative certificate for the SAME
complete residual norm, valid before choosing or optimizing its coefficients.
For any balanced polynomial supported through N, let E be its full dx/x^2
error, Q_H its first H-1 exact integer-cell contributions, and V its complete
period mean square. Then

    |E-(Q_H+V/H)| <= C_N V/[H(H+1)],
    C_N=N^2(1+2ceil(log2 N)).

V is the explicit rational positive divisor quadratic in PROOF.md (4), not
an estimated period average. No lcm-sized period is enumerated. Consequently

    (1-delta)(Q_H+V/H) <= E <= (1+delta)(Q_H+V/H),
    delta=C_N/(H+1).

These are Loewner inequalities on the complete balanced coefficient space.
They apply unchanged after imposing the actual Mobius prefix and BOTH of
the parent's p(1)=0,p'(1)=1 constraints. They control all coefficients,
including large optimized ones; no a priori coefficient envelope is needed.

The proof also gives V<=4C_N E and hence the sharper relative error

    |(Q_H+V/H)-E| <= eta_H E, eta_H=4 C_N^2/[H(H+1)].

Taking H=2C_N ceil(sqrt(N)) gives eta_H<1/N at EVERY rank. A finite
minimizer of the middle form has full energy within
(1+eta_H)/(1-eta_H) of the full finite-support optimum. The physical
horizon is O(N^(5/2) log N). The matrix is rational. The derivative constraint
still contains logarithms; it has NOT become rational.

The proof uses finite Fourier/CRT algebra, an elementary rational-frequency
mean-square bound, and exact Abel summation. All cross terms and the entire
future are retained. This is not a proof that the resulting minima are small.

## Further completed components

- A three-index correction imposes p(0)=-2 at arbitrarily small energy cost,
  preserving the exact prefix and both safe jets; support can grow. It gives
  an equality of unrestricted infima, NOT a fixed-support comparison.
- An explicit rational bounded-coefficient centered completion has support
  <4Y and full remote error O(log Y/Y) beyond the integer horizon 16Y^2.
  Its finite earlier energy is not estimated at subpower strength.
- Three entire-norm minimum brackets are reconstructed with rational-only
  arithmetic, for Y=2,3,4, N=4Y, H=4096 and p(1)=0 ONLY. They are distinct
  from the parent's derivative-normalized minima. No numerical trend is used.

Read PROOF.md, REVIEW.md and VALIDATION.md. The complete analytic arguments
are paper proofs, not consequences of bounded test counts. No mathematical
priority, independent acceptance, new zero-free region or RH proof is claimed.

Run from this directory:

    python -I -S -B verify.py --check result.json
    python -I -S -B -O verify.py --check result.json
    python -I -S -B test_rejections.py --part 1
    python -I -S -B test_rejections.py --part 2
    python -I -S -B -O test_rejections.py --part 1
    python -I -S -B -O test_rejections.py --part 2

No parent Python is imported or executed. No floating-point, logarithm,
gamma, zeta, digamma, numerical contour, or zero oracle enters acceptance.
