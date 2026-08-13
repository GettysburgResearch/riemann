# L-91360 — Historical causal row-per-score monotonicity claim

Claim ID: `L-91360`  
Status: **REFUTED — DO NOT USE**  
Created: 2026-08-13  
Refuted by: `R-91311-l91360-causal-row-per-score-profile-is-not-continuously-monotone.md`  
RH status: **unproved**

## Refutation

The historical claim asserted that

\[
\mathcal R_{p,j}(z)
=
\frac{Q_{pz}(j)-p^{-1/2}Q_z(j)}
     {(5\sqrt{pz}-3)-p^{-1/2}(5\sqrt z-3)}
\]

is nondecreasing in `z` throughout the complete causal window.

`R-91311` gives a directed exact counterexample at

\[
 j=66,
 \qquad p=67,
 \qquad z=\frac{133}{2},
\]

where the logarithmic derivative numerator is strictly below `-1.52`.
The companion replay is `X-91137-causal-ratio-refutation`.

Therefore the following are false:

```text
continuous causal row-per-score monotonicity;
the sufficient derivative gate formerly displayed here;
the historical PASS claim attached to X-91136.
```

The valid single-endpoint theorem

\[
Y\longmapsto\frac{Q_Y(j)}{5\sqrt Y-3}
\]

from `L-91359` remains intact.  Ordering on the **discrete arithmetic divisor set** is a separate open question and is not refuted by the continuous counterexample.

```text
L-91359 single-endpoint monotonicity       RETAINED
L-91360 continuous causal monotonicity     REFUTED
finite discrete-divisor ordering           OPEN
Lorenz row subordination                    OPEN
Riemann Hypothesis                          UNPROVEN
```
