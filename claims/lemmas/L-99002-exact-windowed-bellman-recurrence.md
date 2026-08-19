# L-99002 — Exact windowed Bellman recurrence

**Status:** proved exactly.  **RH is not assumed.**

For a finite collection \(V\) of labelled costs and activities, define
\[
Z_V(t)=\sum_{S\subseteq V,\,P(S)\le t}(-1)^{|S|}r(S),
\]
with \(Z_V(t)=0\) for \(t<1\), and
\[
F_V(t)=\mathbf1_{t\ge1}-Z_V(t),
\qquad
G_V(X)=\int_{X/4}^{X}F_V(t)\frac{dt}{t}.
\]
Adjoin one label of cost \(p\) and activity \(r\).  Splitting subsets according
to whether they contain the new label gives
\[
Z_{V\cup\{p\}}(t)=Z_V(t)-rZ_V(t/p).
\]
Hence
\[
\boxed{
G_{V\cup\{p\}}(X)
 =G_V(X)+r\bigl(H_X(p)-G_V(X/p)\bigr)},
\]
where
\[
H_X(p)=\min\{\log4,\log(X/p)_+\}.
\]
For the complete generalized-prime collection in L-99001,
\(G_V(X)=\mathcal A_X/6\).

The recurrence shows exactly why scalar positivity alone is not hereditary:
a child overshoot \(G_V(X/p)>H_X(p)\) creates a negative increment.  No
unsigned replacement is made.
