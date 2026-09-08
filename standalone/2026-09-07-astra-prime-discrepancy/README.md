# Prime-discrepancy continuation: a simpler target, not an RH completion

Status: proposed component proofs; independent review pending. RH is NOT proved.
Scope: the ordinary-prime forward completion on Re(s)=1/2; full Cauchy-weighted
frequency norms; all real prime-base cutoffs X>=2.
Parent: PR811 at 9e05a2b345369cd16c0973c531650eb37727445e.
What was run: exact bounded rational identities and package/rejection checks;
no actual entropy integral, prime-counting-error norm or zero computation.
Smallest remaining gap: a subpower L1 bound for the literal first-prime
discrepancy, or the sufficient quadratic majorant I(X), on an unbounded sequence.

## Proposed results

- Every higher-prime-power contribution has a uniformly bounded physical L2
  norm; its COMPLETE infinite prime-base tail is at most
  8/sqrt(log X)+4/sqrt X. Under ordinary PNT its squared norm is asymptotic to
  1/(4log X); the real-part squared tail is asymptotic to 1/(8log X).
- The parent's entropy satisfies |2E(X)-||Re C_X||_(1,mu)|<32 at EVERY cutoff.
  This removes the need to estimate the nonlinear tanh feedback separately.
- The complete quadratic norm is an exact one-state energy of
  R(x)=sum_(p<=x)sqrt p-integral_2^x sqrt u/log u du, including its infinite
  stopped-input future. No physical-to-product measure switch occurs.
- The conditional RH bound improves to E(X)=O(log^(3/2) X). This is conditional,
  not evidence that the requested unconditional bound has been established.

Read PROOF.md, then ATTEMPT_AND_REVIEW.md. The latter records the attempted
unconditional estimate and its failure. The new work supplies no fixed-power
saving, no new zero-free region, and no original-domain completion.

All inherited sources remain unchanged. This is a new research packet, not a
Reviewer D verdict or automatic canonical integration. No external novelty
claim is made for the classical Fourier, PNT or Hardy mechanisms.

## Replay

From this directory:

    python checks.py --verify checks.normal.json
    python -O checks.py --verify checks.optimized.json
    python validate.py
    python test_rejections.py

The tests are finite algebra and integrity tests, not a machine proof of the
analytic statements. The packet is prepared for an add-only application to the
named research branch; consult the external publication receipt for actual
remote status rather than inferring publication from these files.
