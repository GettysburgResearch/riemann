# L-90415 — Exact divisor-modulus reindexing of the PIG major arc

Claim ID: `L-90415`  
Title: The `O(sqrt N)` low additive residues are a divisor-indexed family of large-modulus rational phases, with an explicit inverse-square weight  
Status: **PROPOSED COMPLETE EXACT FINITE REINDEXING — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90411`, `L-90414`  
Scope: finite major-residue energy only; no arithmetic estimate or RH conclusion

Let

\[
1\le K\le N/2.
\]

For every \(1\le a<K\), put

\[
g=(a,N),\qquad q=N/g,\qquad b=a/g.
\]

Then \(q\mid N\), \((b,q)=1\), and

\[
a=\frac{bN}{q}.
\]

Moreover

\[
a<K
\quad\Longleftrightarrow\quad
b<\frac{Kq}{N}.
\]

Thus the map \(a\mapsto(q,b)\) is a bijection between

\[
\{1\le a<K\}
\]

and

\[
\left\{
(q,b):
q\mid N,\ q>N/K,\ 1\le b<Kq/N,\ (b,q)=1
\right\}.
\tag{L-90415.1}
\]

For a real prefix coefficient, the sine sums satisfy

\[
S_{N-a}=-S_a.
\]

Hence the nonzero two-sided major-residue energy is exactly

\[
\boxed{
\begin{aligned}
\mathcal E_{\rm major}^{\ne0}(N;K)
={2\over N^2}
\sum_{\substack{q\mid N\\q>N/K}}
\ \sum_{\substack{1\le b<Kq/N\\(b,q)=1}}
\frac{
\left|S_{bN/q}(N)\right|^2
}{
\sin^2(\pi b/q)
}.
\end{aligned}
}
\tag{L-90415.2}
\]

When \(K\le N/2\), every occurring \(b/q<1/2\), and therefore

\[
\frac{2b}{q}
\le
\sin\frac{\pi b}{q}
\le
\frac{\pi b}{q}.
\tag{L-90415.3}
\]

Consequently

\[
\boxed{
\mathcal E_{\rm major}^{\ne0}(N;K)
\asymp
\sum_{\substack{q\mid N\\q>N/K}}
\left(\frac qN\right)^2
\sum_{\substack{1\le b<Kq/N\\(b,q)=1}}
\frac{|S_{bN/q}(N)|^2}{b^2},
}
\tag{L-90415.4}
\]

with absolute comparison constants.

At the square-root cutoff \(K=\lceil\sqrt N\rceil\),

```text
q runs over divisors of N larger than sqrt(N);
b runs only to q/sqrt(N);
the reduced additive modulus is q;
the Green weight is comparable to (q/N)^2 / b^2.
```

In particular, for every \(a\) coprime to \(N\), one has \(q=N\). Thus the
hardest part already contains the one-modulus family

\[
1\le a<\sqrt N,\qquad (a,N)=1,
\]

at modulus exactly \(N\). No argument relying only on averaging over many
different moduli can close the major arc.

Combining (L-90415.2) with the character-modulus expansion of `L-90414` gives a
fully explicit hybrid large-modulus Dirichlet-character form of the remaining PIG energy.
The required estimate remains open.
