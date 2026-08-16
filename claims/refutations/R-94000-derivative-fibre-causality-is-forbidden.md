# R-94000 — Derivative-fibre causality is forbidden in the reset candidate

Claim ID: `R-94000`  
Status: **EXACT REFUTATION / NORMATIVE FIREWALL**  
Date: 2026-08-16  
Frozen witness source: review PR #503 at `db77e5792966edf080604fd4b69fb00f07739681`

The reset candidate preserves the exact Volterra antiderivative, rank-one small-divisor coupling, and rough-change-of-variable results of frozen PR #495 at

```text
50f45b46cbe3c471d6e702c41c7ef178b530e1ab
```

but never invokes `L-91763` or `T-92910`.

For

\[
g_s(m)=\left(\sqrt m-\frac m{\sqrt s}\right)\mathbf 1_{m\le s},
\qquad p_s=\mathcal Rg_s,
\]

the canonical rough subtraction is not positive. At

\[
(p,y,s,j)=(67,15,1005,14)
\]

one has the exact directed enclosure

\[
-\frac{184291}{10^9}
< p_{1005}(14)-67^{-1/2}p_{15}(14)
< -\frac{184290}{10^9}<0.
\]

Every successor replay must fail if it calls a derivative-fibre causal operator, treats a rough lift as the native parent marginal, or imports `L-91763/T-92910` as a theorem. The construction below uses `p_s` only as a direct positive row inside complete outer cells.
