# X-23802 — Exact binary–ternary carry-flow replay

This experiment checks only the finite algebra in `L-23810/L-23811`.

It deliberately starts from a signed rational coefficient vector, constructs
its binary–ternary split flow, computes the node divergence and carry target,
and then reconstructs the original coefficients in the reverse order:

```text
signed split coefficients
-> divergence
-> floor-transform target
-> Möbius tail inversion
-> descending binary–ternary recurrence
-> direct carry-load comparison.
```

Run:

```bash
python verify.py
```

Expected verdict:

```text
PASS_EXACT_BINARY_TERNARY_FLOW_ALGEBRA
```

Retained proof-object SHA-256:

```text
4d88135afeda954aa0c1c9f2951bfd0518a3352a8f3b03f2fb33727e6237dea0
```

The replay uses `fractions.Fraction` throughout.  It does **not** check the
prime-ramp target, the BTF rate, BCT, or RH.  Its purpose is to catch rounding,
child-multiplicity, node-one, and Möbius-inversion mistakes in the new explicit
producer.
