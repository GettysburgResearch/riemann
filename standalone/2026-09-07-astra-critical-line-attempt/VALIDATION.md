# Validation scope

## Mathematical status

The near-linear B bound, the critical-line subpower estimate and RH remain
unproved. PROOF.md contains component analytic proofs, not a proof-kernel
formalization or an independent review. The nontrivial quantitative input
in CL26.3 is the imported Lee--Leong/classical Mertens estimate. No numerical
constants from that paper or its external zero calculations were replayed.
The critical-line tail constant is known to exist, not numerically certified.

## Frozen bytes and code isolation

The connected PR read identified parent commit
`ccd0a80dbd9844d06ccd6331a15b085b9c9afa41` and root tree
`337bdca76711226bb6c95a68cef3910277df2b2f`. Its proof was read through GitHub
and from the supplied local file. The local file is 17,079 bytes, has Git
blob `2af125b452015a0b73483eef66b0995b6c874097`, and SHA-256
`02669fd041a1327f214c0212027bda4dac631909e1c2144e90764e55d25914ee`.
The checker requires these literal identities. No parent code is imported or
executed. The new code uses the Python standard library only. Acceptance uses
explicit exceptions, not removable assertions. Its exact flat payload inventory
is nonempty and rejects missing/extra entries and symlinks. Rational outputs are
canonical strings; floats, duplicate JSON keys and boolean/integer aliases do
not compare equal under the canonical serialized result comparison.

## Finite coverage

- Ordinary Mobius sieve and independent trial factorization: every n through
  361, including n=1, nonsquarefree n and even n.
- Complete actual-source quadratic fixtures: Y=3,5,9,17. Every odd a,b and
  every admissible odd third factor is included. A separate long-source Q
  calculation and finite Dirichlet-coefficient expansion agree exactly.
- Harmonic balance, first coefficient, terminal correction, total coefficient,
  zero endpoint weight, and both formal principal-pole coefficients.
- Predetermined grid pairs (Y_j,Y_(j+1))=(3,9),(9,19), with three rational
  interpolation points per squared-cutoff interval. The largest primitive
  endpoint is therefore 19^2=361, not 17^2.
- The exponent calculation making the frequency tail O(Y) is exact rational
  algebra only. No actual complex contour integral is numerically evaluated.

There are 425 bounded checks. This count is not a count of proved analytic
lemmas; 361 of the checks are the independent primitive Mobius comparison.
No large prime/zero/Mobius campaign, Gram sweep or extrapolation was performed.

## Commands and results

Executed in the Linux container on the sealed packet:

```text
python3 check.py
PASS_BOUNDED_SOURCE_CHECKS count=425 rh_proved=false
python3 -O check.py
PASS_BOUNDED_SOURCE_CHECKS count=425 rh_proved=false
python3 check.py --self-test
PASS_BOUNDED_SOURCE_CHECKS count=425 rh_proved=false
PASS_REJECTIONS cases=9
python3 -O check.py --self-test
PASS_BOUNDED_SOURCE_CHECKS count=425 rh_proved=false
PASS_REJECTIONS cases=9
```

The nine actual CLI rejection cases per mode are a false near-linear claim,
wrong scalar, omitted source row, float alias, duplicate JSON key, empty
manifest, extra path, changed parent proof and a symlink. Semantic result
mutations are resealed to test reconstruction, not just old hashes. Each
subprocess is bounded by a 15-second timeout. A pristine copied packet passes
before the corruption cases; each failed case must produce the explicit
REJECT diagnostic. No timeout is counted as PASS. One combined 20-second
container invocation reached its outer limit after completing the normal
self-test; its partial optimized run is not counted. A separate optimized
invocation completed all checks and nine refusals.

An initial fixture-generation command failed with IndexError because the
second interpolation interval reaches 361, while its sieve cap was 289.
The cap and explicit range check were corrected before sealing; that failed
run is not counted as a successful verification. This was a local test-range
bug, not evidence for or against any analytic theorem. No predecessor was
modified. Final execution receipts and publication identities accompany the
external delivery; those are distinct from an independently accepted theorem.

## Not performed

No Lean/kernel build, Windows execution, authenticated remote CI run, new zero
verification, external numerical-constant replay, or non-author referee review.
No actual-subpower moment, one-sided arithmetic sign bound, original uniform
gain, new zero-free strip, or RH proof. The standard-library checks do not
certify those conclusions. Existing sources, main, settings and permissions
are not repair targets in this packet.
