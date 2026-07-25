# X-2814 — Rigorous phase-grid accelerator

Experiment ID: `X-2814`  
Agent: `gpt56-01-f`  
Issue: #28 / #42  
Status: exact target-wide Taylor remainder proved; directed moment producer pending

## Purpose

The direct X-2805 reference backend evaluates a high-precision sine and cosine
for every one of the `4,118,082,969` target prime powers.  L-2813 replaces those
billions of trigonometric calls by:

1. directed phase assignment to `M=32768` roots-of-unity cells;
2. directed complex moments through order `R=3`;
3. one finite root/Taylor contraction per occupied phase cell;
4. one explicit global remainder moat.

The prime stream, vector, cutoff, carrier, and D-0801 normalization are
unchanged.

## Exact target gate

The committed certificate uses only

```text
N < 2
pi > 3
pi < 22/7
log(10^11) < 26
sqrt(10^11) < 316228
M = 32768
R = 3
```

and proves

```text
W_x < 11,000,000
pi/M < 1/10,000
Taylor remainder < 1/21,816,000,000
                 < 1/20,000,000,000.
```

Thus the accelerator's target-wide approximation moat is below `5e-11`, less
than one tenth of the independently proved nonprime correction gate
`1/(2*10^9)`.

The exact checker performs no floating-point operation.

## Reproduction

```bash
python verify_target_remainder.py \
  certificates/target-c1e11-m32768-r3.json

python -m unittest discover -s tests -v
```

## Producer plan

For every term, a directed producer will enclose the phase and prove a unique
nearest phase-grid node.  A boundary-touching term is evaluated directly or
hulled across every possible assignment.  It then updates outward complex
moment intervals.  At shard completion, MPFR-enclosed roots of unity contract
the moments and the exact L-2813 remainder widens the scalar interval.

The direct X-2805 producer remains the reference and fallback.  A strict sign
from either inclusion-valid backend suffices; overlap is the preferred
independent reproduction.

## Proof boundary

The committed result proves only the global Taylor error budget.  It does not
claim that a phase-grid production stream has run, nor does it claim a sign for
the target.  Any final negative still requires complete coverage, exact
alpha/correction composition, T-2801 review, and independent backend
reproduction.
