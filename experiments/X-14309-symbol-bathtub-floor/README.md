# X-14309 — Exact Fourier-density symbol floor

This experiment implements `L-14316` for a finite directed lower envelope of a
real Fourier multiplier on a time interval.

## Mathematical output

For interval length `L`, cell lower bounds `s>=L_j`, and a tail floor `s>=G`
outside the cells, the checker proves

```text
q_s(w)/||w||^2
>= G-L/(2 pi) sum_j |I_j|(G-L_j)_+.
```

On Suzuki's scaled interval `[-1,1]`, it replaces `1/pi` by the exact safe
rational upper bound `106/333`, coming from `333/106 < pi`.

The checker evaluates every breakpoint level, so no optimizer is trusted. It
returns either:

```text
CERTIFIED_NONNEGATIVE_SYMBOL_COMPRESSION
CERTIFIED_LOWER_FLOOR_ONLY
```

A negative lower floor is not a negative eigenvalue and has no RH implication.

## Strict synthetic control

The unit test uses a symbol lower bound `-1` on the cell `[-1/4,1/4]` and a
tail floor `+1`. The pointwise symbol is allowed to be negative, but the exact
support-density floor is

```text
1-(106/333)*1 = 227/333 > 0.
```

Thus the method can certify the whole compressed operator positive without
constructing a prolate packet.

## Production contract

A `SUZUKI_SYMBOL_DIRECTED` certificate must bind:

1. exact support and Fourier normalization;
2. the complete prime-power multiplier;
3. the smooth archimedean remainder;
4. pairwise-disjoint rational frequency cells;
5. outward lower symbol bounds on every cell;
6. an analytic tail floor outside their union;
7. the exact breakpoint list and claimed optimum.

A sampled symbol plot, midpoint cosine sum, or empirical tail is rejected at
the proof boundary.

## Relationship to PR #152

This is the inexpensive first gate:

```text
complete symbol
-> integrated deficit
-> ambient scalar floor.
```

If the floor is too weak, retain the same symbol cells and use:

- `L-14311` for a weighted or multiband low packet;
- `L-14308` for the finite Schur correction;
- `T-14302` for the cofinal RH implication.

The scalar floor does not supersede those tools; it can eliminate the finite
packet entirely when the low-symbol volume is small enough.

## Verification

Local standard-library replay:

```text
8 exact adversarial tests pass
strict synthetic floor = 227/333
floating-point operations in checker = 0
```

No production Suzuki symbol certificate has yet been run.
