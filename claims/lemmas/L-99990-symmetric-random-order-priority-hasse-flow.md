# L-99990 — Exact symmetric random-order priority-Hasse flow

Claim ID: `L-99990`  
Status: **PROVED EXACT FINITE FLOW THEOREM**  
Created: 2026-08-20  
Sibling input: PR #670 at `f5d37a5f1880749dd33b103d98e2d85bac60ae28`  
RH status: **not assumed**

Let \(B=\{1,\ldots,k\}\) be labelled prime vertices with activities
\(0<a_i<1\). For \(A\subseteq B\), write \(w(A)=\prod_{i\in A}a_i\).

PR #670 gives an exact priority flow for every total order. Average that flow
uniformly over all orders.

For the Hasse edge joining \(A\) and \(A\cup\{i\}\), \(i\notin A\), its averaged
mass is

\[
\boxed{
\overline J_{i,A}
=
a_iw(A)\int_0^1
(1-t)^{|A|}
\prod_{h\notin A\cup\{i\}}(1-a_ht)\,dt.
}
\tag{L-99990.1}
\]

## Proof

Give every label an independent uniform key in \([0,1]\), and order labels by
their keys. Conditional on the key of \(i\) being \(t\):

- every \(h\in A\) must occur after \(i\), contributing probability \(1-t\);
- for \(h\notin A\cup\{i\}\), an earlier label contributes the priority
  survival factor \(1-a_h\), while a later label contributes one. Its average
  factor is \(t(1-a_h)+(1-t)=1-a_ht\).

Multiplication and integration give (L-99990.1).

Because this is a convex average of exact feasible flows, it saturates every
odd vertex, respects every even capacity, and leaves exactly

\[
\prod_i(1-a_i)
\]

at the empty even vertex. The formula is permutation invariant and keeps the
two \(67\) labels distinct when \(a_i=1/67\).

For a product-monotone potential \(\Phi\), truncate every edge by the smaller
endpoint potential. The averaged unmatched boundary is

\[
\boxed{
\overline{\mathcal U}_\Phi
=
\sum_i\sum_{\substack{A\subseteq B\setminus\{i\}\\|A|\ {\rm odd}}}
\overline J_{i,A}
\,[\Phi(P_A)-\Phi(p_iP_A)].
}
\tag{L-99990.2}
\]

This is a canonical, order-free replacement for choosing one priority order.
It is exact but does not by itself give the required half-order bound.
