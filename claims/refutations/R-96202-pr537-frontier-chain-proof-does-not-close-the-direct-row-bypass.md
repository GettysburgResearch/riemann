# R-96202 — The published FRONTIER-CHAIN prose does not prove prime-sieved row positivity

Claim ID: `R-96202`  
Status: **LOGICAL GAP / DIRECT-ROW BYPASS FIREWALL**  
Created: 2026-08-16  
Targets: PR #537 `L-94200`, PR #542 direct-row consumer

PR #542 correctly bypasses the \(J_\Lambda/P_\Lambda\) normalization if one has
\[
c_X(j)\ge0
\]
for fixed component rows. Its Mellin transform and noncancellation mechanism are valuable.

The published proof of the required positivity in PR #537, however, contains an unresolved transport step. After expanding
\[
\omega_{r,j}(n)=
\sum_{d\mid(n,P_r)}\mu(d)q_j(n/d),
\]
all divisor-cube vertices for a fixed product \(n\) occupy the same logarithmic knot \(\log n\). The text then says the transport “never combines different products \(n\)” while applying convex packets at three distinct knots
\[
a<b<c.
\]
Those two statements are incompatible. A nontrivial convex packet necessarily moves reservoir between distinct products.

The local inequalities (L-94200.13)--(L-94200.16) do not, by themselves, define a global one-use cross-product allocation or prove that no reservoir is reused.

Therefore the direct-row route has the exact status:

```text
fixed-row Mellin transform and pole survival     retained;
Landau consumer                                  retained;
finite prime-sieved positivity                   promising / numerically supported;
published FRONTIER-CHAIN proof                   gap;
RH through PR #542                               unproved.
```

A successor may close this route only by depositing an explicit global transport, a positive Gram representation, or another proof of \(c_X(j)\ge0\).
