# X-15121 — Exact Chebyshev dilation-energy Gram replay

This experiment is the standard-library exact regression for `L-15145`.

It verifies, for one finite rational source package,

\[
\sum_{m,n}w_mw_nK_{a,Y}(m,n)
=
\int_1^Y
\left|
\sum_n w_n
{\mathbf1_{t\ge n}-a\mathbf1_{t\ge an}\over t}
\right|^2dt.
\]

The left side is contracted from the exact rational Gram kernel; the right side
is recomputed independently by integrating on the complete threshold partition.
The checker also verifies symmetry, exact leading principal minors, the diagonal
and off-diagonal ledgers, and a deterministic proof digest.

Retained control:

```text
scale                  4
Y                      100
nodes                  2,3,5,7
energy                 420643/25200
diagonal               69409/8400
off diagonal           13276/1575
proof SHA-256          d593b65b7c9353f2afdedd8b34f92beca15a4f482d778ea87b58cd416d33094d
```

The six adversarial tests reject Booleans, a nonexpanding scale, duplicate
nodes, negative weights, out-of-range nodes, and malformed arithmetic.

This is an exact synthetic identity check. It contains no Riemann prime data and
no RH verdict.

Run:

```bash
python experiments/X-15121-chebyshev-dilation-energy/verify.py \
  experiments/X-15121-chebyshev-dilation-energy/certificates/synthetic.json \
  /tmp/x15121-result.json

PYTHONPATH=experiments/X-15121-chebyshev-dilation-energy \
python -m unittest -v \
  experiments/X-15121-chebyshev-dilation-energy/tests/test_verify.py
```