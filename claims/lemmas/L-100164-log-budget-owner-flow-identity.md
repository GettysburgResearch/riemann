# L-100164 — Exact log-budget identity for product-threshold reciprocal layers

Status: **PROVED EXACT COMBINATORIAL IDENTITY; INDEXING REPAIRED; CONVERSION TO UNWEIGHTED DEBT OPEN**  
Created: 2026-08-20  
RH status: **unproved**

Let `P` be a finite rough-prime label set, put

\[
a_p={1\over p-1},
\qquad
w(A)=\prod_{p\in A}a_p,
\qquad
P_A=\prod_{p\in A}p,
\]

and define

\[
E_k(x)=\sum_{\substack{A\subseteq P\\|A|=k\\P_A\le x}}w(A).
\]

For every active subset `A`, its remaining logarithmic budget is

\[
R_x(A)=\log x-\log P_A\ge0.
\]

Double counting all admissible one-prime extensions gives exactly

\[
\boxed{
\sum_{\substack{A\subseteq P\\|A|=k\\P_A\le x}}
 w(A)
 \sum_{\substack{p\in P\setminus A\\p\le x/P_A}}
 a_p\log p
=
\sum_{\substack{B\subseteq P\\|B|=k+1\\P_B\le x}}
 w(B)\log P_B.
}
\tag{L-100164.1}
\]

Indeed, a fixed child `B` is reached from the parent `B\setminus{p}` for each `p in B`; its total contribution is

\[
w(B)\sum_{p\in B}\log p=w(B)\log P_B.
\]

The earlier abbreviated “equivalent” display omitted the restrictions `|A|=k` and `p notin A`; that notation is withdrawn.

## Scope

Identity (L-100164.1) shows that logarithmically weighted extension flow is paid by product-scale consumption rather than by an unrestricted prime-harmonic sum.  However, the assertion

\[
\log p\le R_x(A)
\]

is valid only for each **admissible** extension `p<=x/P_A`; it does not by itself bound the sum of all extension weights by `R_x(A)`.  Recovering the unweighted flow from `a_p log p` still costs at least `1/log67`, and repeated generations require a genuine product-band/Bellman theorem.

Thus (L-100164.1) is an exact bookkeeping identity, not a contraction estimate for the alternating reciprocal prefix.
