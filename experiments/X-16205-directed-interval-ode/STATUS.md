# Source-bound DIRECTED_INTERVAL_ODE production prefix

## Result

A parameterized emitter produced source-bound CCM/prolate primitives at

- gamma = 4096,
- gamma = 32768,
- gamma = 262144,

with modes 0, 4, 8, 12. Each primitive includes directed angular separation
intervals, regular pole Cauchy boxes, transition and residual ledgers,
horizontal-strip companion bounds, tail-energy charges, exact repaired-source
definitions, and SHA-256 bindings.

The unchanged X-16204 consumer accepted the three historical wrappers
byte-for-byte. That acceptance was structural: the old schema allowed endpoint,
deterministic-error, and profile-Gram ledgers to be supplied independently.

## Rigorous components retained

- separation upper endpoints: Rayleigh--Ritz plus directed Sturm count;
- separation lower endpoints: Schur tail floor plus directed Sturm count;
- pole data: Arb Frobenius evaluation plus rational parameter/truncation
  majorants;
- repaired sources: determinant formulas imposing both CCM source constraints;
- normalized coefficient-tail radial, frequency-derivative, and horizontal-strip
  errors;
- exact first-alias normalized Gram;
- digests: producer, source, primitive, wrapper, consumer result.

## Placeholder audit

X-16207 replays the actual gamma=4096 repaired packet. It validly replaces

```text
t2=1
t2_derivative=4
```

by the source-derived outward ceilings

```text
radial tail L2 squared              <= 1e-4181
frequency-derivative tail L2^2      <= 1e-4174
horizontal-strip tail L2^2          <= 1e-4180
```

and encloses the first-alias profile Gram by

```text
0.9999999 I <= D_first <= 1.0000001 I.
```

The attempted replacement

```text
||f^(4)||_1 <= 10^100  ->  ||f^(4)||_1 <= 45000
```

was **not** a valid unit-profile endpoint estimate. The normalized Poisson
remainder contains

```text
||f^(4)||_1 / sqrt(first_alias_energy),
```

and the first-alias energies are superexponentially small. The previously
reported endpoint charges and deterministic error are withdrawn by `R-16205`.

## Exact remaining moat

No downstream deterministic-error or complete profile-Gram field is emitted
until one normalized radial replay supplies both:

1. the normalized endpoint channels and a relative exterior ODE/Bessel
   remainder;
2. a complete Poisson cross-alias operator bound and full Gram upper bound.

Writing

```text
D_full=D_first+P_self+C_cross,
P_self>=0,
```

one has

```text
lambda_min(D_full)>=0.9999999-||C_cross||.
```

X-16207 v2 is classified

```text
RADIAL_DERIVATIVE_CLOSED_NORMALIZED_ENDPOINT_OPEN
```

and its binder refuses X-16204 promotion. No additional support block is
promoted before this one-block relative profile moat closes. No RH proof is
claimed.
