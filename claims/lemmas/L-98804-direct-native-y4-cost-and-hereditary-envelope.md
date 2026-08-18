# L-98804 — Direct native `Y_4` pricing closes the hereditary envelope

Claim ID: `L-98804`
Status: **PROPOSED NATIVE-COST COMPOSITION — CONSTANT LIVE LEDGER UNPROVED**
Depends on: `L-98801/L-98803`; exact `L-91378` dual; frozen local-cost ledger
RH status: **not assumed**

Publication reconciliation: the replay checks the arithmetic sum producing
`60989`; it does not derive that ledger for an arbitrary mass-one live
endpoint realization. The frozen root estimate does not by itself supply this
uniform statement.

## 1. Exact native deficit

For every feasible nonnegative row,

\[
\boxed{
 \Delta_X(d_X)
 :=J_\Lambda(X)-\mathcal H(d_X)
 =\sum_{q\ge2}Y_4(q)s_X^{(4)}(q)\ge0.
}
\]

This is an identity, not a comparison with `4sqrt(X)`.

Pairing the slack cocycle of `L-98803` with the positive dual gives

\[
\boxed{
 \Delta_X(d_X)
 =\delta_X+
  \sum_b\beta_b\Delta_{Y_b}(d_{Y_b}),
 \qquad
 \delta_X=\langle Y_4,r_X\rangle\ge0.
}
\]

## 2. Root-local cost ledger

On the frozen factor-67 response estimates, direct absolute `Y_4` pricing gives
one conservative root-local ledger:

```text
common square-root thinning        < 12012
retained mismatch/collar/knot      <     4
terminal and fixed-base terms      < 48972
one narrow current-only port       <     1
------------------------------------------------
root-local cost                    < 60989 < 61000
```

In the zero-port specialization the last line is absent.  Anchored exact finite
packets have zero realization discrepancy.  Signed errors are paid by absolute
`Y_4` pairing, never by invented positive source mass.

Hence

\[
\boxed{0\le\delta_X<60989.}
\]

## 3. Per-unit target-mass envelope

Let `Lambda(X)` be the supremum of the native deficit over unit-target-mass
packets of the hereditary type.  Positive homogeneity, `L-98801`, and
`Y_b<=X/67+1` give

\[
\boxed{
 \Lambda(X)
 \le60989+\frac18\Lambda(X/67+1).
}
\]

Iteration yields

\[
 \Lambda(X)
 \le60989\sum_{n\ge0}8^{-n}+C_{\rm base}
 <\frac87\,60989+C_{\rm base}.
\]

The retained physical root target mass is uniformly bounded by the frozen
factor-67 estimate `<3020`; therefore the unnormalised native root also has a
uniform absolute deficit.

Consequently

\[
\boxed{
 \Delta_X(d_X)=O(1)=o(\log^2X).
}
\]

## 4. Firewalls

```text
J_Lambda-4sqrt(X) upper bridge     forbidden
source mass substituted for loss   forbidden
Hall bonus recursively charged     forbidden
root corrections copied to child   forbidden
Y4 price from another row          forbidden
```
