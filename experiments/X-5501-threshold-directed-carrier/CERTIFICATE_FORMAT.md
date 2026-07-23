# X-5501 certificate formats

## Exact dyadic vector

Schema: `riemann.dyadic-complex-vector.v1`

Required fields:

```text
bits
dimension
real_numerators[dimension]
imag_numerators[dimension]
metadata.threshold
metadata.cutoff
canonical_sha256_without_digest
```

Coordinate `j` equals

```text
(real_numerators[j] + i*imag_numerators[j]) / 2^bits.
```

The digest is SHA-256 of canonical compact sorted JSON after removing only the
digest field.

## Exact manifest

Schema: `riemann.threshold-prime-manifest.v1`

The manifest stores cutoff, exact coverage, prime/higher-power counts, separate
sequence digests, and a combined digest. Higher powers store `(q,p,a)` so the
von Mangoldt weight is unambiguous.

## Directed replay

Schema: `riemann.threshold-directed-replay.v1`

Every numerical interval endpoint is serialized as

```json
{"mantissa2":"SIGNED_BINARY_INTEGER","exp2":0,"digits":0}
```

with exact interpretation

```text
integer(mantissa2) * 2^(exp2-digits_without_sign).
```

The replay stores:

- exact threshold, cutoff, carrier, K, dyadic bits, MPFR precision, and threads;
- complete term counts and ambiguous-hat count;
- vector and manifest digests;
- directed leading scalar, prime sums, margins, event, smooth bound, whole-cell
  envelope, and nonprime gate;
- an explicit proof-boundary string.

## Acceptance logic

Let `N` be the exact vector norm and `B=1/(4*10^9)` the compact operator gate.
The checker verifies that the serialized gate encloses `BN`.

```text
margin_right_hi < -B*N
    -> CERTIFIED_NEGATIVE_FIXED_VECTOR
margin_right_lo >  B*N
    -> CERTIFIED_POSITIVE_FIXED_VECTOR_CONTROL
otherwise
    -> UNRESOLVED
```

For a next-threshold microcell it separately checks

```text
whole_microcell_lower_envelope
 <= margin_threshold_lo
    - smooth_background_upper
    - max(0,event_upper).
```

If that lower envelope exceeds `BN`, the whole microcell is a positive control
for the exact vector.

## Candidate boundary

`CERTIFIED_NEGATIVE_FIXED_VECTOR` is not by itself a project counterexample. It
is a finite numerical witness pending the D-0801 admissibility/normalization
audit and independent reproduction. Positive statuses are local exclusions
only.
