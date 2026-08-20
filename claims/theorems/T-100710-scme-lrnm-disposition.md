# T-100710 — Exact disposition of `SCME100704` and `LRNM100704`

Claim ID: `T-100710`  
Status: **ONE TERMINAL THEOREM PROVED; ONE REFUTED**  
Created: 2026-08-20  
Base: PR #693 at `2cc70798b453ce4e5059dcc25d8d3fb7c38e172e`  
RH status: **unproved**

The two proposed terminal statements of `L-100704` do not form a viable
closure pair.

`L-100710` proves

\[
G_{\rm sh}(X)
=-\kappa_0{\sqrt X\over\log X}
+O(\sqrt X/\log^2X),
\]

with `kappa_0>0`. Therefore `R-100710` proves

\[
\boxed{\mathrm{SCME100704}\text{ is false}.}
\]

`L-100711` proves

\[
G_{\rm lo}(X)
=+\kappa_0{\sqrt X\over\log X}
+O(\sqrt X/\log^2X)>0
\]

for all sufficiently large `X`. Therefore

\[
\boxed{\mathrm{LRNM100704}\text{ is true unconditionally}.}
\]

The equal and opposite main terms show that `L-100704` split an essential
cross-region cancellation before applying its regional norms.

```text
SCME100704                         FALSE
LRNM100704                         PROVED, eventually zero negative part
SCME + LRNM -> RH                  valid conditional implication, unusable
short/long absolute gluing         REFUTED AS CLOSURE MECHANISM
carrier-preserving replacement     OPEN
Riemann Hypothesis                 UNPROVEN
```

No conclusion about RH follows from `LRNM100704` alone.
