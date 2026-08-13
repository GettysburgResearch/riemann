# X-92000 — Third-order Clark-curvature replay

This experiment checks the finite algebra behind `L-92000`--`R-92000` and
records a non-rigorous actual-Xi diagnostic for the remaining scalar sign.

## Run

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_THIRD_ORDER_CLARK_CURVATURE
```

## Exact gates

The standard-library rational layer verifies:

1. the exact three-node determinant factorization of `L-92000`;
2. the exact negative rational control determinant from `R-91902`;
3. strict convexity of the reciprocal coordinate for one off-line orbit;
4. strict negativity of the `tp` curvature numerator in the same control.

## Diagnostic layer

If `mpmath` is available, the script evaluates

\[
 \mathfrak T_3(x)=x^2FF''-2x^2(F')^2+xFF'+F^2
\]

and

\[
 x^2F''+xF'-F
\]

at ten safe real points between `0.5001` and `100`.  The retained values have
the predicted positive and negative signs, respectively.

These samples are **not interval enclosures**.  They do not prove the compact
curvature certificate, all three-node positivity, or RH.

## Scope

```text
exact finite algebra                CERTIFIED
exact rational off-line firewall    CERTIFIED
sampled actual-Xi curvature          DIAGNOSTIC ONLY
compact interval theorem             OPEN
Riemann Hypothesis                    UNPROVED
```
