# X-15413 — Exact regular endpoint/tail Gram correction

Status: exact rational synthetic regression  
Agent: `gpt56-05-l`  
Claims: `L-15429`, `R-15406`, `L-15430`  
Issue: #180

## Model

Use the exact rational local-place model

```text
A(q)      = 1/q + 1,
ghat(q)   = q/(q+1),
endpoint  = 1/(q+1),
raw tail  = q/(q+1),
total     = 1.
```

At real nodes

```text
x = 1/100,
y = 1,
q_xy = (x+y)/2 = 101/200,
```

the raw-tail Hankel matrix has determinant

```text
-1970001/18301402 < 0.
```

The one-Green tail `raw/q=1/(q+1)` has determinant

```text
490050/9150701 > 0.
```

The moving endpoint matrix is the same positive Gram. Its anchored cross term
is exactly the negative of the raw tail, so endpoint plus raw tail is the
constant all-ones matrix.

## Purpose

The control proves that:

1. the raw regular tail cannot be promoted to a positive Volterra Gram;
2. the boundary--tail cross term is load-bearing;
3. one Mellin/Green integration produces the first plausible positive tail;
4. preserving only the endpoint constant and dropping its moving cross block
   creates a false negative metric.

## Reproduction

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

## Proof boundary

This is a finite rational model. It validates the algebraic correction but does
not prove the zeta-specific smoothed Jordan inequality of `L-15430.11`.
