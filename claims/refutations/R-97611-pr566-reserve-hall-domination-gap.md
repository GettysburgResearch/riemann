# R-97611 — PR #566's reserve injection does not imply Hall-current domination

Status: **EXACT LOGICAL REFUTATION OF L-96651 AS USED**
RH: unproved.

PR #566 decomposes

\[
\mathcal G_v=\mathcal H_v\oplus\mathcal R_v
\]

and defines

\[
g_v=\phi(\mathcal H_v).
\]

Its child injection lands in the disjoint reserve `R_v`. Therefore it can imply only

\[
\phi(\mathcal R_{v\to w})\ge\alpha_{v,w}\phi(\mathcal G_w),
\]

not

\[
g_v\ge\sum_w\alpha_{v,w}g_w.
\]

Countermodel:

```text
phi(H)=1/2,
phi(R)=1,
alpha phi(G_child)=1.
```

All decomposition/injection clauses hold while `g<Tg`.

The accompanying moment argument is also insufficient: equal mass and barycenter do not preserve every Hall/Lorenz prefix. A reserve-aware theorem must preserve the full prefix family on the residual source and prove an atomwise one-use identity `(I+T)U=g_total` before the positive-operator lemma can be applied.
