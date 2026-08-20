# L-99900 — Exact weighted Boolean-cube Hasse transport

Claim ID: `L-99900`  
Status: **PROVED EXACT FINITE FLOW THEOREM**  
Created: 2026-08-20  
Depends on: PR #658 occurrence-level Hasse ledger  
RH status: **not assumed**

Let \(B=\{1,\ldots,k\}\) be a finite labelled set and choose activities

\[
0\le r_i\le1.
\]

For \(S\subseteq B\), put

\[
w(S)=\prod_{i\in S}r_i.
\]

Regard odd subsets as demand vertices and even subsets as capacity vertices.
Edges are the ordinary Hasse edges joining sets whose symmetric difference is
one label.

Then there exists an explicit nonnegative Hasse flow with the following
properties:

1. every odd vertex exports exactly \(w(S)\);
2. every even vertex receives at most \(w(S)\);
3. the only unused even capacity is at the empty set;
4. that residual is exactly

\[
\boxed{
\Delta_B=\prod_{i=1}^k(1-r_i).
}
\tag{L-99900.1}
\]

## Inductive construction

For \(k=0\) the statement is immediate. Assume a flow on the first \(k-1\)
labels, saturating every odd vertex and leaving residual

\[
\Delta_{k-1}=\prod_{i<k}(1-r_i)
\]

at the empty even vertex.

Adjoin label \(k\) with activity \(r=r_k\).

- On the zero face, retain the old flow.
- On the one face, reverse the old flow and multiply every edge amount by
  \(r\). Since parity flips on that face, this saturates every one-face odd
  vertex except the singleton \(\{k\}\), whose residual demand is
  \(r\Delta_{k-1}\).
- Send \(r\Delta_{k-1}\) along the vertical Hasse edge
  \(\{k\}\to\varnothing\).

The empty vertex had residual capacity \(\Delta_{k-1}\), so the new unused
capacity is

\[
(1-r)\Delta_{k-1}=\Delta_k.
\]

All capacities are respected and every edge toggles exactly one labelled
source.

## Optimality and reversed parity

The total even-minus-odd mass is

\[
\sum_S(-1)^{|S|}w(S)=\prod_i(1-r_i)=\Delta_B.
\]

Hence no flow can leave less residual. If the external channel convention is
reversed, the negative channel is the heavier one and the exact unmatched
negative mass is \(\Delta_B\).

No asymptotic estimate or form of RH enters this theorem.
