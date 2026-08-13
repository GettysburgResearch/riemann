# T-91311 — Subcritical packet resets have uniformly bounded deficit

Status: **proved abstract consumer; producer separate; RH conditional**

Let `m_X` be an additive positive packet mass and `Delta_X` a positively homogeneous, subadditive packet deficit. Suppose every packet at endpoint `X` decomposes into a current packet and children at endpoints `Y_b<=X/67+C_0`, with

\[
\sum_bm_{Y_b}(P_b)\le\theta m_X(P),
\qquad 0\le\theta<1,
\]

and current-generation debt at most `C m_X(P)`.

For the worst normalized positive deficit

\[
\Lambda(X)=\sup_{Y\le X,m_Y(P)=1}\max(0,\Delta_Y(P)),
\]

subadditivity gives

\[
\boxed{
\Lambda(X)\le C+\theta\Lambda(X/67+C_0).
}
\]

Iteration yields

\[
\boxed{
\Lambda(X)\le\frac{C}{1-\theta}+O_{\rm base}(1).
}
\]

For the provenance packet budget, the total contracted-child coefficient is below `1/8`. Once its current causal generators have one capacity-faithful mass-proportional realization, the theorem applies with `theta<1/8` and gives

\[
\boxed{
\Lambda(X)\le\frac87C+O_{\rm base}(1)=O(1).
}
\]

This is stronger than the `o(log^2 X)` loss required by the endpoint consumer. The recursion is on actual typed child packets; no source fraction is multiplied by a signed native loss.

```text
subcritical recurrence                       EXACT
child mass <1/8 -> bounded packet deficit    EXACT
provenance coefficient ledger                AVAILABLE
physical current-generator typing            PRODUCER / REVIEW GATE
root endpoint implication                    INDEPENDENT REVIEW REQUIRED
Riemann Hypothesis                            UNPROVEN
```
