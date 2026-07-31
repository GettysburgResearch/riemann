# X-20501 — Conditional line-frame kernel replay

This experiment is an exact rational regression for `L-20501`–`L-20503`.

It contains no zeta evaluation. It checks the finite algebra that a production
certificate must consume after directed evaluation and residual producers have
finished.

## Main control

The packet has one \(R\)-coordinate and one \(W\)-coordinate. The first
evaluation row is

```text
V_Z = [1/2, 2].
```

It frames \(W\) and produces the graph kernel

```text
J = (1,-1/4)^T.
```

The second row is

```text
V_Y = [1,1].
```

Its conditional value on the graph is

```text
S_(Y|Z)=1-1*(1/2)/2=3/4.
```

The checker certifies a selected positive frame, a nontrivial negative residual,
a nonzero positive-complement Schur correction, and final generalized floor

```text
3191/3400.
```

The Hardy representer Gram gives the independent extension-tail floor

```text
6/17.
```

## Positive-residual control

A second certificate replaces the residual by a graph value of \(100\). The
absolute-tail criterion fails badly, but the one-sided residual endpoint is
zero. The corrected floor remains strictly positive:

```text
3551/3400.
```

## Run

```bash
python3 -m unittest discover -s tests -v
python3 verify.py certificates/synthetic.json
python3 verify.py certificates/positive-residual.json
sha256sum -c SHA256SUMS
```

The verifier uses only the Python standard library and `fractions.Fraction`.
