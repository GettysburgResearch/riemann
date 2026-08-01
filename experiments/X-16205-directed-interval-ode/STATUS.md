# Source-bound DIRECTED_INTERVAL_ODE production prefix

## Result

A parameterized emitter produced source-bound CCM/prolate primitives at

- gamma = 4096,
- gamma = 32768,
- gamma = 262144,

with modes 0, 4, 8, 12. Each primitive includes directed angular separation
intervals, regular pole Cauchy boxes, transition and residual ledgers,
horizontal-strip companion bounds, tail-energy charges, a p=4 endpoint ledger,
exact repaired-source definitions, and SHA-256 bindings.

The unchanged X-16204 consumer accepts all three wrappers byte-for-byte on
replay. The retained consumer proof-object digests are listed in
`cofinal-prefix.json`.

## Rigorous components

- separation upper endpoints: Rayleigh--Ritz plus directed Sturm count;
- separation lower endpoints: Schur tail floor plus directed Sturm count;
- pole data: Arb Frobenius evaluation plus rational parameter/truncation
  majorants;
- repaired sources: determinant formulas imposing both CCM source constraints;
- transition bound: explicit L-16229 potential/interaction ledger;
- digests: producer, source, primitive, wrapper, consumer result.

## Placeholder replacement

X-16207 replays the actual gamma=4096 repaired packet and replaces

```text
t2=1
t2_derivative=4
||f^(4)||_1<=10^100
```

by the source-derived outward ceilings

```text
radial tail L2 squared              <= 1e-4181
frequency-derivative tail L2^2      <= 1e-4174
horizontal-strip tail L2^2          <= 1e-4180
source packet fourth derivative L1  <= 45000
endpoint point charge               <= 1e-5
endpoint L2 squared charge          <= 2e-10
deterministic error                 <= 1/40000.
```

The first-alias profile Gram is enclosed by

```text
0.9999999 I <= D_first <= 1.0000001 I.
```

`bind_downstream.py` writes these fields into X-16204 only after a complete
arithmetic higher-alias Gram moat is present.

## Exact remaining blocker

Writing

```text
D_full=D_first+P_self+C_cross,
P_self>=0,
```

the one remaining production number is an outward operator enclosure for
`||C_cross||` on the same repaired gamma=4096 packet. The current certificate
leaves this value null and is classified

```text
SOURCE_FIELDS_CLOSED_COMPLETE_ALIAS_GRAM_OPEN.
```

No additional support block is promoted before this operator moat closes. The
retained prefix is a real source-bound emitter/consumer integration result, not
a proof of RH.
