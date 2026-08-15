# PR #497 computational-certificate audit

## Frozen objects

```text
proposal head:
bd2a3c32ab50d8a8cec39c4b51ccd63349b23a74

compact retained classification:
PASS_TARGET_LORENZ_COMPACT_PROPORTIONAL_AVLT

tail retained classification:
PASS_COMPLETE_TARGET_LORENZ_TAIL_AVLT
proof object:
e30b0e4e08802002b160ddfaaefebb4b6ab8aa5a3562785fc854cc93f4101aa0

native endpoint retained classification:
PASS_TARGET_LORENZ_TWO_LEDGER_NATIVE_ENDPOINT_PACKET
proof object:
7207cbe3b241173e02d3c9a346056df861801522e4633675ecc2740711f96f02
```

No large sweep was rerun.

## Compact certificate

The retained compact object reports:

```text
702,511,095 total row cells
702,511,091 coarse directed passes
4 exact dependency exceptions
minimum certified direct lower > 0.001
```

The checker contains a stated perturbation budget and exact rational inverse-square-root intervals for the tail parity-prefix reserve. The domain is `py<166000`.

```text
review disposition: FROZEN DIRECTED INPUT ACCEPTED AT ITS STATED SCOPE
```

## Tail certificate

The C++ generator does enumerate all intended events exactly with `uint128_t`, but evaluates the proof-relevant functions with `long double`.

Missing fail-closed information:

```text
LDBL_MANT_DIG / platform pin
rounding-mode assertion
outward transcendental enclosure
prefix-sum error bound
determinant cancellation error bound
derivative lower-bound error budget
final polynomial error budget
```

The Python wrapper recompiles and checks the values printed by the same generator. It does not create independent directed enclosures.

The reported full minimum is

```text
26.786236008153155...
```

against the published lower bound `26`, leaving `0.786236...`, not a literal one-unit reserve.

```text
review disposition: EXHAUSTIVE COMPUTATIONAL SUPPORT / NOT EXACT CERTIFICATE
```

## Native endpoint fixture

The endpoint verifier contains two synthetic rational leaf fixtures. It checks:

```text
greedy removal algebra
row bonus algebra
positive-vs-signed ledger names
thinning reserve identity
60989 charge sum
schema mutations
```

It does not compute:

```text
the endpoint fibre S_(X,s)
P61 stopping-line path coefficients
causal tree weights
actual Target-Lorenz cutoffs
actual leaf rows
the common-parent integral
actual q<K responses
```

```text
review disposition: INTERFACE REGRESSION ONLY
```

## Required certificate repair

The tail generator should be replaced by an outward interval implementation, or accompanied by a rigorous error theorem tied to an exact compiler/platform contract. The native endpoint fixture should consume an authenticated actual leaf ledger generated from the missing endpoint-fibre identity.
