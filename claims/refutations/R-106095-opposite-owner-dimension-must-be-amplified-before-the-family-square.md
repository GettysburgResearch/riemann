# R-106095 — The opposite-owner dimension must be amplified before the family square

Claim ID: `R-106095`  
Programme aliases: `LFAM1.OPPOSITE_OWNER_CAUCHY_FIREWALL`, `LFAM2.Q_DIMENSION_CORRECTION`, `STRESS.T106090_SELF_AUDIT`  
Status: **BINDING SOURCE-WEIGHT CORRECTION; `L-106094` AND THE Q-INDEXED CONTROLLING STATUS OF `T-106090` ARE RETRACTED**  
Created: 2026-08-25  
Depends on: `L-106090--L-106094`, `R-106090`; parent `R-102840`, PR #751 `R-106071`, `R-106080`  
Programme issues: #743, #736, #737  
RH status: **unproved**

A reconstruction of the source-dual moment in the first version of
`T-106090` finds one omitted coherent dimension.

That version fixed the opposite semiprime owner product \(Q\), formed one
family amplitude \(Z_{g,\ell,Q,\sigma,h}\), and then used Cauchy across \(Q\)
with moment weight \(Q\).

For one fixed \(Q\), `L-106092` correctly gives

\[
\sum_{h\ne0}\|B_{\alpha;g,Q,\sigma,h}\|^2
\ll {X^{o(1)}\over g^2Q}.
\tag{R-106095.1}
\]

But multiplying by the proposed source-dual moment weight \(g^2\ell Q\)
cancels the reciprocal \(Q\):

\[
g^2\ell Q
\cdot |A_\alpha|^2
\cdot {X^{o(1)}\over g^2Q}
=
X^{o(1)}\ell |A_\alpha|^2.
\tag{R-106095.2}
\]

The subsequent sum over all admissible opposite owner products is therefore a
**count of \(Q\)-fibres**, not the polylogarithmic reciprocal sum
\(\sum_Q1/Q\).

This is the missing factor in the first `L-106094`.

## 1. No scalar Cauchy weight pays both sides

More generally, suppose the \(Q\)-Cauchy weight is \(Q^\theta\).  Its dual
index cost is

\[
\sum_Q Q^{-\theta},
\]

while the weighted fixed-fibre diagonal costs

\[
\sum_Q Q^{\theta-1}.
\]

For semiprime owner products on a growing horizon, a source-blind argument
cannot make both sums subpower: the first requires \(\theta\ge1\), whereas the
second requires \(\theta\le0\).

Thus no scalar reweighting after the \(Q\)-fibres have been separated repairs
the problem.

## 2. Exact finite coherence fixture

Let \(N\) different opposite owner fibres produce the same normalized physical
tail vector \(e\).  Each fixed-fibre source energy is \(N^{-1}\|e\|^2\), but
their coherent physical aggregate has energy \(N\|e\|^2\).  A \(Q\)-weighted
Cauchy step merely moves this dimension between the moment and its dual; it
does not remove it.

## 3. Correct operation order

The opposite owner must be treated exactly like the left anchor:

```text
fix only the common core g, least discrepancy prime ell,
and owner quadratic class sigma;

sum both the left anchors and all opposite owner products Q
inside one scalar family amplitude;

only then take the Gauss/family square.
```

The corrected construction is `L-106095`.

## Binding consequence

```text
L-106090 least-discrepancy incidence                 RETAINED
L-106091 fixed-Q exact even-character family         RETAINED
L-106092 fixed-Q long-core estimate                  RETAINED
L-106093.4--.8 fixed-Q amplified identities          RETAINED LOCALLY
L-106093.9 Q-indexed controlling moment              OVERSTRONG / SUPERSEDED
L-106094 same-anchor diagonal theorem                RETRACTED
T-106090 Q-indexed controlling frontier              SUPERSEDED
Riemann Hypothesis                                   UNPROVED
```

The exact corrected moment and its valid atomic diagonal are
`L-106095--L-106096`; the live theorem is `T-106100`.
