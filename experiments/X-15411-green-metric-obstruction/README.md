# X-15411 — Green quotient versus physical metric obstruction

Status: exact finite rational refutation  
Agent: `gpt56-05-l`  
Claim: `R-15404`  
Issue: #180

## Control

Take

```text
C = diag(2,1),
E = C^-1,
K = [[0,1],[1,0]].
```

Then

```text
C E = I,
K^T K = I,
T = C K E = [[0,2],[1/2,0]].
```

In the ordinary physical Euclidean metric,

```text
T^T T = diag(1/4,4),
||T|| = 2.
```

Thus a unitary lifted multiplier can become expansive after compression and a
non-isometric similarity transform.

The minimum-lift quotient Gram is

```text
G_q = E^T E = diag(1/4,1).
```

In this quotient metric,

```text
T^T G_q T = G_q,
```

so the same map is an exact isometry.

## Reproduction

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

Seven deterministic tests passed. They reject a false compressed map, a bad
right inverse, a nonunitary multiplier, false physical and quotient claims, and
Boolean integer fields.

## Proof boundary

The control refutes only a metric-free inference from `C E=I` and lifted
contractivity to physical output contractivity. It does not refute a
source-specific theorem proving that the Riemann Volterra Green lift induces
exactly the original physical Weyl metric. That identity is the remaining
positive gate.
