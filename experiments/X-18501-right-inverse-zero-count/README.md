# X-18501 — Selected-zero right-inverse count

This experiment is the exact finite arithmetic companion to `L-18501` and
`T-18501`.

Run:

```bash
python experiments/X-18501-right-inverse-zero-count/verify.py \
  experiments/X-18501-right-inverse-zero-count/certificates/synthetic.json

python -m unittest discover \
  -s experiments/X-18501-right-inverse-zero-count/tests -v
```

The verifier never diagonalizes a floating matrix. It constructs the
`G`-orthogonal right inverse, certifies its Gram bound by exact LDL, verifies
that the complete zero Gram dominates the selected coordinate Gram, and checks
the strict rational threshold moat.

Expected verdict:

```text
CERTIFIED_SELECTED_ZERO_COUNT_AT_MOST_KERNEL_DIMENSION
```

## Retained synthetic geometry

The selected evaluation is `V=(1,0,0)` and the metric is `diag(2,1,1)`. The
supplied right inverse `(1,3,0)^T` contains a large kernel component. Its
metric-orthogonal representative is `(1,0,0)^T`, with Gram `2`; hence every
non-kernel generalized evaluation eigenvalue is at least `1/2`.

The declared omitted-zero budget and desired visible floor are both `1/8`, so
the count threshold is `1/4<1/2`. At most the two-dimensional evaluation kernel
can lie below it.

## Nonclaims

This exact replay does not establish a zeta-zero table, a Guinand--Weil tail
budget, or complete low-index capture. It proves only the finite implication
encoded in the certificate.
