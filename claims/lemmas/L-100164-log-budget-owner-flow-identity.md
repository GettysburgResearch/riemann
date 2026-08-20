# L-100164 — Exact log-budget identity for product-threshold reciprocal layers

Status: **PROVED EXACT COMBINATORIAL IDENTITY; CONVERSION TO UNWEIGHTED DEBT OPEN**  
Created: 2026-08-20  
RH status: **unproved**

Let `P` be a finite rough-prime label set, put

\[
a_p={1\over p-1},
\qquad
w(A)=\prod_{p\in A}a_p,
\qquad
L=\log x,
\]

and let

\[
E_k(x)=\sum_{\substack{|A|=k\\P_A\le x}}w(A).
\]

For every active subset `A`, define its remaining log budget

\[
R_x(A)=L-\log P_A\ge0.
\]

Double counting all one-prime extensions gives the exact identity

\[
\boxed{
\sum_{\substack{|A|=k\\P_A\le x}}
 w(A)
 \sum_{\substack{p\notin A\\p\le x/P_A}}
 a_p\log p
=
(k+1)
\sum_{\substack{|B|=k+1\\P_B\le x}}
 w(B){\log P_B\over k+1}.
}
\]

Equivalently, because each `B` is reached once from each of its `k+1` parents,

\[
\boxed{
\sum_{A}w(A)
 \sum_{p\le x/P_A}a_p\log p
=
\sum_B w(B)\log P_B.
}
\tag{L-100164.1}
\]

The significance is that the logarithmically weighted extension flow is paid by product-scale consumption rather than by the divergent unweighted prime harmonic mass. Since every active extension satisfies `log p<=R_x(A)`, the total weighted flow lives on the finite scale budget `L`.

This identity does not by itself bound the unweighted odd layer, because recovering `a_p` from `a_p log p` costs `1/log p`. For rough primes this cost is uniformly at most `1/log67`, but summing over arbitrarily many extension generations still requires a product-band/Bellman argument. The remaining target is to convert the finite log-budget flux into a one-sided bound for the alternating reciprocal prefix without reintroducing the divergent global `sum 1/p`.
