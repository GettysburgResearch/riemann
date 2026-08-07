# X-15402 — Exact scalar Barta mean-obstruction regression

Status: exact finite synthetic regression  
Agent: `gpt56-05-l`  
Issue: #154  
Claims: `L-15403`, `R-15401`

## Purpose

`L-15403` proves that a positive scalar supersolution cannot exploit the signs
of a signed-edge jump form. For a symmetric edge set and positive `psi`,

```text
sum_i (L_J psi)_i / psi_i
 = -sum_edges w_ij (psi_i-psi_j)^2/(psi_i psi_j) <= 0.
```

Hence

```text
min_i b_i <= average_i b_i <= average_i potential_i.
```

The same identity holds in the continuum after symmetric cutoff and limit. In
the odd Suzuki form, the exact potential mean tends exponentially to minus
infinity, so no scalar positive supersolution can produce the proposed cofinal
`-o(1)` lower floor.

X-15402 checks the finite rational analogue and explicitly verifies that changing
an edge from a difference square to a plus square does not change the local
scalar Barta residual.

## Synthetic control

The retained signed graph has

```text
potential = (11, 1, -7/3)
psi       = (1, 2, 3)
edge 0-1  weight 10, sign +1
edge 1-2  weight 10, sign -1
```

The exact local Barta values are all `1`, while

```text
potential mean = 29/9,
edge defect sum = -20/3,
Barta mean = 1.
```

Thus

```text
sum(Barta) = sum(potential) + edge defect sum
```

and the floor/mean obstruction is strict.

Changing the second edge sign leaves every local Barta value unchanged.

## Reproduction

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

Eight adversarial tests pass.

## Proof boundary

This is an exact finite signed-graph regression. The continuum no-go theorem is
proved in `L-15403`; X-15402 does not independently evaluate Suzuki's kernel or
the Riemann zeta function.
