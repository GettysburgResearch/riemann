# X-16207 — source-derived repaired-packet moat, fail-closed v2

This experiment replaces the coarse radial and derivative tail placeholders
used by the early `DIRECTED_INTERVAL_ODE` prefix with quantities derived from
the actual `gamma=4096`, modes `0,4,8,12` repaired CCM packet.

The valid outward ceilings are

```text
radial tail L2 squared              <= 1e-4181
frequency-derivative tail L2^2      <= 1e-4174
horizontal-strip tail L2^2          <= 1e-4180
first-alias Gram                    [0.9999999, 1.0000001]
```

The checker reconstructs these from the two normalized repaired columns and
enforces the cofinal gates

```text
sum eps_rad  <= gamma^-2,
sum eps_drad <= gamma^-1.
```

## Relative endpoint correction

The first version attempted to use the absolute compact-source bound
`||f^(4)||_1<=45000` in the unit-profile Poisson remainder. This omitted the
required divisor `sqrt(first_alias_energy)`. At gamma=4096 the divisor is of
order `10^-1769` or `10^-1762` for the two repaired columns. The old endpoint
and deterministic-error ceilings are therefore withdrawn; see `R-16205`.

A production endpoint ledger must be derived from the **normalized radial
solution** itself, retaining its endpoint channels and an outward radial-ODE or
Bessel remainder.

## Deliberate promotion barriers

The checker returns

```text
RADIAL_DERIVATIVE_CLOSED_NORMALIZED_ENDPOINT_OPEN
```

until a normalized endpoint ledger is supplied. After that it still requires

```text
complete_arithmetic_alias.cross_error_upper
complete_arithmetic_alias.full_upper
```

because the first Poisson sample is not the complete arithmetic profile Gram.
The downstream binder emits an X-16204 wrapper only when both barriers are
closed.

Run:

```bash
python verify.py certificate.json --output results/verification.json
python -m unittest discover -s tests -v
```

No RH proof is claimed.
