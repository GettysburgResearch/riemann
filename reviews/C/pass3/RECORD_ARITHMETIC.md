# X-105560: independently reproduced normalization, enclosure and retention defects

Reviewer C; audit baseline `8d16f8d9c475db290bc85e53d775b93b9bcdb336`.
Scientific source PR #726: `e8e6d85221a9a85fb2a5f82a1807802f89b06b7b`.
This is a computational acceptance/fidelity finding, not a refutation of the exact
simple-zero proportion formula or of the external seven-gap theorem.

## Frozen files read

| Path | Git blob |
|---|---|
| experiments/X-105560-reviewed-record/verify.py | bd076c05c2e741758286ee3c0d378240c4be884c |
| experiments/X-105560-reviewed-record/results/verification.json | 41ec02af734f101c0255e200139fa532755847b3 |
| claims/theorems/T-105560-reviewed-simple-zero-record.md | e318d4d8e8cd498419d15ab4bcf8e016d12ab403 |
| claims/lemmas/L-105562-seven-gap-pressure-global-average.md | 7ae7d3cd39786ff4d1d2819954c60aa0e0f2a664 |

All four were read completely through the GitHub connector. The producer was
copied byte-for-byte and authenticated locally by its Git blob identity. The
references directory retains the original buggy producer, not a patched version.

## 1. The code computes the wrong H0

The theorem defines x=1/sqrt(2) and H0=3/2-x cot(x). The code's Bernoulli expansion
instead starts its accumulator at 1, although x cot(x) has constant term 1 and
the required H0 accumulator must therefore start at 1/2. Its returned interval
approximates H0+1/2.

Authenticated function calls in ordinary and optimized Python give:

- h0_lower approximately 1.1725007036794116457;
- explicit_lower approximately 1.1748730759922243;
- the internal test merely asks whether explicit_lower exceeds 0.673 and passes.

A lower bound greater than 1 cannot certify a proportion of zeros. This is a
source-normalization mismatch inside the checker; it does not show that the
correct exact formula in the theorem is false.

## 2. The remainder argument is also false

Even after correcting the constant, the stated alternating-series justification
would still be wrong. The nonconstant terms in H0 all have the same positive
sign. The implementation returns s_48 +/- a_49, omitting the positive tail after
a_49. Exact arithmetic finds its own lower endpoint at 50 terms greater than its
claimed upper endpoint at 48 terms. More decisively, an independent Taylor
quotient enclosure proves H0+1/2 is strictly above that old upper endpoint.
Thus this is an invalid upper enclosure, not merely an inaccurate comment.

## 3. The retained JSON is not output from this frozen producer

The frozen source executes 41*40=1640 scalar tests and 12*12*18=2592 positive
surrogate tests. The retained file says 1601 and 2527. Its seven_gap record has
an explicit_lower_bound_decimal field, whereas the producer emits rational
h0_lower/h0_upper/explicit_lower/explicit_upper fields instead.

The retained content hash for verify.py is
`37ee02345fa83e5c251a1f2477cfdbbf1c6224d6cd438ca9acfe6922833bff5f`;
the authenticated current source has SHA-256
`ab84355abb670a14348388636ce4bfb7a11e8bb9c6aa1f7fad1a16e981e9d6f9`.
The source uses LF already, so the declared CRLF normalization does not repair
this discrepancy. The same retained marker cannot identify both versions.

## 4. A complete replacement of the scalar calculation only

Let

    C_N = sum_{k=0}^N (-1)^k / (2^k (2k)!),
    S_N = sum_{k=0}^N (-1)^k / (2^k (2k+1)!).

These are the alternating Taylor series for cos(x) and sin(x)/x at x^2=1/2.
Each absolute term decreases strictly; the true value lies between the partial
sum and that sum plus its next signed term. If C_L<=cos(x)<=C_U and
0<S_L<=sin(x)/x<=S_U, division by positive endpoints gives

    3/2-C_U/S_L <= H0 <= 3/2-C_L/S_U.

The proof uses ordinary alternating-series remainder bounds, not floating-point
rounding. The replay constructs all endpoints as exact Python Fractions, then
applies the increasing affine map

    R=(1345000 H0-2680)/1340003.

At N=80 it proves by exact cross multiplication

    0.673008527927779 < R < 0.673008527927780.

Consequently R>673/1000 survives as a scalar fact. The theorem's printed decimal
`0.673008527927557...` is not the decimal expansion of its exact displayed
formula. The replay's first attempted inherited decimal bracket failed; that
failure is recorded rather than suppressed. Decimal displays in the receipt
are explanatory only; none is used as a bound.

References for the classical series: NIST DLMF 4.19.1, 4.19.2 and 4.19.6
(https://dlmf.nist.gov/4.19), and the Bernoulli/zeta identity 25.6.2
(https://dlmf.nist.gov/25.6). The independent scalar proof above does not require
the latter identity.

## 5. What this does not validate

The local producer copies external commit/blob strings into JSON; it does not
execute or authenticate the 707901-node Arb certificate. Its positive rational
surrogate tests do not prove the analytic three-point theorem. Full payload
production was not run because the complete sixteen-file packet was not mounted;
only the authenticated functions were run in clean, resource-limited temporary
subprocesses. The exact original target code was not changed or monkey-patched.

L-105562 imports ainta/zeta-simple-zeros at
`040c5e899e658aed7b56a2a87f501798fe10761d`, then performs seven-window/269-offset
averaging. C read this scope; C did not rerun its interval cells or establish the
full analytic deduction. Scientific disposition remains pending integrator
reconciliation. The corrected scalar certificate is not a new zero-proportion
theorem and is not a proof of RH.

Required correction propagation: rebuild the scalar certificate, source hashes,
retained JSON, theorem decimal and all consumers of this particular replay.
Check #731 and programme #744's quoted 67.3008527927% record against their own
source locks; do not revoke independently valid external proofs solely because
this wrapper is defective. Keep the source-qualified theorem separate from its
currently unusable verification artifact.

Replay: `python reviews/C/pass3/scripts/replay_record_arithmetic.py`.
Receipt: `pass3/reports/record_arithmetic_replay.json`.
