# R-106511 — Outer Dirichlet domination can pay favorable inner degree

Claim ID: `R-106511`  
Status: **PROVED EXACT SHARPNESS FIREWALL**  
Created: 2026-08-25  
RH status: **unproved**

`L-106507` proves the valid topology-safe inequality

\[
\|H_{B_+\overline{B_-}}\|_{\mathcal S_2}^2
\le\|B_+-B_-\|_{\mathcal D}^2.
\]

The inequality is not an equivalence and can be very wasteful in the favorable
inner direction.

## Exact counterfamily

Take

\[
B_-=1
\]

and let `B_+` be any finite inner function of degree `m`.  Then

\[
U=B_+
\]

is analytic, so

\[
\boxed{H_U=0.}
\]

On the other hand,

\[
\begin{aligned}
\|B_+-1\|_{\mathcal D}^2
&=\|B_+\|_{\mathcal D}^2\\
&=\boxed{m}.
\end{aligned}
\]

Thus the outer Dirichlet majorant may be linear in the full favorable inner
degree even when the adverse all-pass charge vanishes identically.

## Consequences

```text
OUTERDIR106520 is a valid sufficient condition.
OUTERDIR106520 is not a necessary or source-blind sharp condition.
Small source difference before oriented inner projection does not
automatically imply a small outer Dirichlet norm.
```

For a sharp fifth-endpoint attack, one should retain either

\[
\|H_U\|_{\mathcal S_2}^2
=\operatorname{tr}(T_{B_+}^*P_{K_{B_-}}T_{B_+})
\]

or the exact positive remainder of `L-106507.6`.  Any use of
`OUTERDIR106520` must genuinely prove its stronger bound rather than infer it
from the absence of adverse winding in a model problem.
