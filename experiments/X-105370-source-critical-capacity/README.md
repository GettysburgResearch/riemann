# X-105370 — Source–critical capacity replay

This standard-library replay authenticates the exact finite identities in
`L-105370`, the corrected capacity theorem `L-105372`, and the corrected
frontier `T-105371`.

Run:

```bash
python -B experiments/X-105370-source-critical-capacity/verify.py \
  --output experiments/X-105370-source-critical-capacity/results/verification.json
```

Expected verdict:

```text
PASS_X_105370_SOURCE_CRITICAL_CAPACITY
```

The checker performs 71 exact rational checks:

```text
35  polynomial source = critical atoms + boundary reserve checks;
36  positive-definite source-capacity, inverse, trace and domination checks.
```

Polynomial calibrations:

```text
F(z)=z^3-3z
  critical residues at +/-1: -1/3
  source moments: 1,2/3,2/3,...
  critical atom: weight 2/3 at s=1
  outer boundary reserve: beta_0=1/3

F(z)=z^4-2z^2+3/4
  central residue: -3/16
  residues at +/-1: -1/32
  regularized source moments: 5/16,1/16,1/16,...
  critical atom: weight 1/16 at s=1
  outer boundary reserve: beta_0=1/4
```

The synthetic capacity fixture consumes exactly one quarter of a positive
three-atom source measure, so the normalized critical operator is `(1/4)I`
at orders one through three and its trace is `k/4`.

The replay does **not** evaluate Xi, prove positivity of the actual source
matrices, establish `CRVH105330`, `OSCC105371`, `SCLC105371`, or prove RH.
