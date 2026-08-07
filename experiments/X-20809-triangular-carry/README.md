# X-20809 — Triangular carry saturation verifier

This experiment has two deliberately separated layers.

## Exact synthetic layer

```bash
python3 verify.py --x 10000
```

The `Fraction` path verifies:

- exhaustive carry counting against the closed coefficient
  `beta_(nq)`;
- exact backward reconstruction of a frozen positive rational coefficient
  vector;
- exact reconstruction through the independent Möbius-adjoint formulas of
  `R-20805`;
- exact equality of every synthetic target coefficient.

The retained verdict is

```text
PASS_EXACT_AVERAGED_CARRY_AND_ADJOINT_RECONSTRUCTION
```

This verifies algebra only. It does not verify the Riemann-data positivity
conjecture.

## Ordinary Riemann reconnaissance

The ordinary path uses the actual target

```text
w_X(q)=q^(-1/2) log(X/q)
```

and emits the canonical coefficients using the `O(X log X)` adjoint
reconstruction. It also compares

```text
sum_n c_X(n) G_n
```

against the independently enumerated complete von Mangoldt ramp.

The default retained run is `X=10000`. `O-20808` records larger in-session runs
through `X=1000000`.

The ordinary verdict is explicitly

```text
ORDINARY_RECONNAISSANCE_NOT_A_CERTIFICATE
```

because binary floating positivity at any finite cutoff cannot establish the
universal Carry Saturation Lemma.

## Review boundary

A production proof would need either:

1. a symbolic proof that the recurrence emits `c_X(n)>=0` for every `X,n`; or
2. an equivalent exact positive formula for those coefficients.

Increasing `--x` is useful for discovery but cannot close that quantifier.