## Checkpoint 7 — primary-cardinal conditioning

Exact checkpoint base:
0a7b83e596534a7b9633b1c59ea4fdb057551c05.

Because every L-105105 target datum is the top local primary jet, its unique
reduced selector has a closed cardinal formula.  If
\(M=\prod_a(z-a)^{d_a}\) and \(M_c=M/(z-c)^{d_c}\), then

\[
W=\sum_{c\in\mathcal T}\gamma_c(z-c)^{d_c-1}
\frac{M_c(z)}{M_c(c)},
\qquad
\frac WM=\sum_{c\in\mathcal T}
\frac{\gamma_c}{M_c(c)(z-c)}.
\]

This exposes the exact conditioning products
\(|M_c(c)|^{-1}\), gives degree/coefficient/boundary envelopes, and reduces
each weighted edge to those products times a pole-cancelled holomorphic
factor.

The dependence is necessary.  Real-even clustered selectors grow at the
full \(\delta^{-(D-1)}\) scale, and a Blaschke lower bound rules out escape by
using a higher-degree holomorphic selector.  Completeness, multiplicity
labels, and parity therefore do not supply a cofinal Xi estimate.

Exact replay:

    PASS_T105106_PRIMARY_CARDINAL_CONDITIONING
    15/15 focused tests in normal and optimized Python
    digest 7dc8a3075e983d48032d74e14af2d3fed5611adb9735623e32a9dfa8623ace33

Xi manifests, cofinal cardinal-product/separation bounds, estimates of the
pole-cancelled holomorphic factors, weighted edge asymptotics, RCMV104530,
and RH remain open.
