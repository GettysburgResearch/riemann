# L-97210 — Compatible-order Cauchy–Binet composition

Claim ID: `L-97210`  
Status: **UNCONDITIONAL FINITE LINEAR-ALGEBRA THEOREM**  
Created: 2026-08-17

Let \(H\in\mathbb R_{\ge0}^{m\times n}\) and
\(K\in\mathbb R_{\ge0}^{n\times2}\). Assume, in one fixed compatible ordering,

\[
\det H[I,J]\ge0
\]

for every two-element row set \(I\) and column set \(J\), and

\[
\det K[J,\{1,2\}]\ge0
\]

for every two-element \(J\). Then every \(2\times2\) minor of \(M=HK\) is
nonnegative.

Indeed, for each two-element row set \(I\),

\[
\boxed{
\det M[I,\{1,2\}]
=
\sum_{\substack{J\subset\{1,\ldots,n\}\\|J|=2}}
\det H[I,J]\det K[J,\{1,2\}]\ge0.
}
\]

This is the exact Cauchy–Binet theorem needed by the stronger blueprint.

The hypotheses are load bearing. Nonnegative entries, unique ownership, a
forest description, or rowwise terminal positivity do not imply them. In
particular, the permutation and positive-leaf counterexamples in `R-97210`
show that neither factor was proved totally nonnegative by the earlier prose.
