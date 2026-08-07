# X-23202 — Terminal-Euler / balanced-Type-II proposal audit

This standard-library-only experiment checks the finite algebra introduced in
the post-review correction of PR #233.

It verifies:

- the corrected internal Type-I dichotomy at `delta=1/5`;
- all 715 rational exponent triples on a denominator-60 grid;
- rejection of the reviewer's `delta=2/5` counterexample;
- acyclicity of a finite complexity graph;
- the necessity of signed recombination before rowwise energy;
- terminal amplitude and energy exponents `3/10` and `3/5`;
- the fail-closed required-field schema for `BTP(K)`.

Run:

```bash
python experiments/X-23202-terminal-euler-btp/verify.py
python -m unittest discover \
  -s experiments/X-23202-terminal-euler-btp/tests -v
```

Retained proof-object SHA-256:

```text
172d510bc2b256e593c586f9fb9aab14d9b69edc024bc73ef845ec3c30c60726
```

## Proof boundary

This is exact synthetic arithmetic. It does not emit the actual Heath--Brown
tuple manifest, prove a terminal BV/Euler bound for a production window, prove
`BTP(K)`, establish an unbounded coefficient-rate theorem, or prove RH.
