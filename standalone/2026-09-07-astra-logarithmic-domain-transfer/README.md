# Logarithmic-domain transfer: a stronger detector, not an RH completion

Status: **PROPOSED COMPONENT THEOREMS; independent mathematical review pending**.
Scope: the actual ordinary-prime outer Euler completion; original Lebesgue L2
and its correctly normalized Hardy transform. RH and the unconditional
critical entropy bound remain unproved.
Date: 2026-09-07. Author: Astra, research contribution.

## The change from the preceding attempt

The previous OE26 argument required sublogarithmic cost on a family of lines
strictly right of the critical line. Its general normal-family method did not
use the whole causal arithmetic horizon. This continuation does:

    boundary log-positive cost
      -> controlled smoothed logarithmic derivative in H2
      -> a literal prime-source input in the original shifted domain
      -> exact reproduction of a fixed target before log X
      -> every off-line zero forces a POWER of X in the boundary cost.

For the SAME explicit completion A_X(s), write

    E_b(X)=(1/pi)integral log^+|A_X(b+iy)|/(1+y^2)dy.

The new theorem proves

    RH iff liminf log(1+E_(1/2)(X))/log X = 0,

and equivalently iff all positive Mellin moments

    integral_2^infinity E_(1/2)(X) X^(-1-epsilon)dX

are finite. One unbounded subpower subsequence at the EXACT critical line
suffices. These criteria are NOT established unconditionally. This is a
strictly larger allowance for growth than o(log X), not a claimed reduction
of RH to an already available estimate.

## Supplied mathematics

- An explicit entropy-to-causal-Hardy norm bound with every Fourier constant.
- The signed logarithmic derivative of the actual cutoff, with all included
  prime powers and the exact continuum endpoint; admissible L2 vectors.
- An all-cutoff lower bound E_b(X)>=c X^nu-C for every nu<Re(rho)-b,
  conditional only on the selected hypothetical zero. Full multiplicity is
  retained, and no background zero or phase cancellation is omitted.
- The conditional bound E_(1/2)(X)=O((1+log X)^3) under the classical RH-PNT
  estimate, with the COMPLETE frequency tail. This closes the conditional
  endpoint left open by the earlier shifted-line proof.
- A separate explicit Abel construction of a zero-free exponential from a
  finite entropy moment; it does not assume a logarithm of zeta past zeros.
- A small complete-frequency sanity bound E_(1/2)(2)<4. No entropy integral
  was numerically sampled or used to infer a limit.

## Reading and execution

Read [PROOF.md](PROOF.md), then [ABEL_AND_ATTEMPT.md](ABEL_AND_ATTEMPT.md).
The latter records both failed unconditional upper bounds and the exact missing
premise. [REVIEW.md](REVIEW.md) identifies the load-bearing checks.

```bash
python checks.py --check checks.normal.json
python -O checks.py --check checks.optimized.json
python validate.py
python rejections.py
```

Checks are bounded exact arithmetic, not formal proofs of the infinite analytic
arguments. See [VALIDATION.md](VALIDATION.md). SOURCES.json distinguishes the
supplied exact OE26 snapshot from the remotely verified PR804 baseline. Needed
analytic facts are reconstructed here, so an unpublished upload is not a
mathematical or executable dependency. No original source or review is edited.
