# X-7502 — Direct-xi logarithmic Loewner minors

Experiment ID: X-7502  
Agent: `gpt56-01-h`  
Issue: #75  
Status: exact checker and synthetic controls complete; Riemann-xi replay pending primitive artifacts

## Purpose

L-7504 converts direct completed-xi modulus rectangles into value-only
cross-Loewner determinant tests. Under RH, every declared determinant is
nonnegative. The checker uses no floating-point arithmetic and evaluates no
special function.

## Files

```text
verify_log_loewner.py              exact rational log and determinant checker
adapt_modulus_certificate.py       adapter from X-7501 direct-xi rectangles
configs/high-carrier-log-loewner.json
certificates/synthetic-log-loewner.json
results/synthetic-summary.json
tests/
```

## Exact arithmetic

For each positive rational endpoint, the checker performs exact power-of-two
range reduction and encloses the logarithm with the positive `atanh` series.
It then forms cross secant matrices and determinant intervals using
`fractions.Fraction` only.

The first production manifest adds to the nine-point X-7501 horizontal block:

- six interlaced order-two minors;
- four interlaced order-three minors;
- two interlaced order-four minors.

No new Arb evaluation is needed. The adapter computes exact modulus-square
intervals from the already produced complex rectangles.

## Synthetic results

The RH-compatible model `H(u)=u+1` gives a strict positive order-two determinant
approximately

```text
+9.532797895202409e-4
```

while the off-line dip `H(u)=(u-5)^2` gives

```text
-3.0748992890764892e1.
```

Both signs are proved by exact rational intervals. The negative is a synthetic
control only.

## Reproduction

```bash
python verify_log_loewner.py \
  certificates/synthetic-log-loewner.json \
  --output /tmp/synthetic-output.json

python -m unittest discover -s tests -v
```

Nine tests pass.

Once an X-7501 directed certificate exists:

```bash
python adapt_modulus_certificate.py \
  ../X-7501-xi-modulus/results/high-carrier-p256.json \
  configs/high-carrier-log-loewner.json \
  --output /tmp/high-carrier-log-loewner.json

python verify_log_loewner.py /tmp/high-carrier-log-loewner.json
```

## Proof boundary

- The checker proves rational containment and determinant signs.
- Actual Riemann-xi use requires directed primitive rectangles from X-7501.
- Any negative requires independent direct-xi reproduction and analytic review
  of L-7504/L-7501 before candidate allocation.
- No Riemann-xi negative is claimed in this experiment.
