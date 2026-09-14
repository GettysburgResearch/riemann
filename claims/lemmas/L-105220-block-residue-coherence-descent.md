# L-105220 — Block critical-residue coherence controls cumulative reverse Rolle

Claim ID: `L-105220`  
Status: **PROVED EXACT, FINITE REGULAR-WINDOW THEOREM**  
RH status: not assumed

Let \(F_0,\ldots,F_K\) be a derivative chain,
\(F_k=F_0^{(k)}\), on a compact real interval \(I=(a,b)\). Assume:

1. \(F_k(a)F_k(b)\ne0\);
2. every real zero of \(F_k\) in \(I\), \(1\le k\le K\), is simple;
3. \(F_{k-1}\) and \(F_k\) have no common zero in \(\overline I\).

Let \(R_k\) be the number of real zeros of \(F_k\) in \(I\). At a real zero
\(c\) of \(F_k\), define
\[
\rho_{k,c}=\frac{F_{k-1}(c)}{F_{k+1}(c)}.
\]
Put
\[
A_k=\left(-\sum_{F_k(c)=0}\rho_{k,c}\right)_+,
\qquad
B_k=\sum_{F_k(c)=0}\rho_{k,c}^2,
\]
and for a block \(1\le k\le K\),
\[
R_{\rm blk}=\sum_{k=1}^KR_k,\quad
A_{\rm blk}=\sum_{k=1}^KA_k,\quad
B_{\rm blk}=\sum_{k=1}^KB_k.
\]
If \(B_{\rm blk}>0\), define
\[
\mathfrak C_{\rm blk}
=\frac{A_{\rm blk}^2}{R_{\rm blk}B_{\rm blk}}.
\]

Then
\[
\boxed{
R_0
\ge
R_K
-
2R_{\rm blk}\bigl(1-\mathfrak C_{\rm blk}\bigr)
-K.
}
\tag{1}
\]

## Proof

At level \(k\), a residue is negative exactly at a Rolle-generating extremum.
Let \(G_k\) and \(E_k\) be the good and wrong extrema, so
\(R_k=G_k+E_k\). Cauchy--Schwarz on the negative residues gives
\[
G_k\ge\frac{A_k^2}{B_k}.
\]
Summing and applying Engel's form of Cauchy--Schwarz,
\[
\sum_{k=1}^KG_k
\ge
\sum_{k=1}^K\frac{A_k^2}{B_k}
\ge
\frac{A_{\rm blk}^2}{B_{\rm blk}}.
\]
Hence
\[
\sum_{k=1}^KE_k
\le
R_{\rm blk}-\frac{A_{\rm blk}^2}{B_{\rm blk}}
=
R_{\rm blk}(1-\mathfrak C_{\rm blk}).
\]
The exact real reverse–Rolle count at each level gives
\[
R_{k-1}\ge R_k-2E_k-1.
\]
Summing over \(k=1,\ldots,K\) proves (1).

## Variance form

If \(A_{\rm blk}>0\), regard the numbers
\(x_{k,c}=-\rho_{k,c}\) as one block sample. With block mean
\(\bar x=A_{\rm blk}/R_{\rm blk}\) and second moment
\(m_2=B_{\rm blk}/R_{\rm blk}\),
\[
\mathfrak C_{\rm blk}=\frac{\bar x^2}{m_2}
=\frac1{1+\operatorname{Var}(x)/\bar x^2}.
\]
Thus the entire cumulative descent is controlled by one coefficient of
variation, including both within-level residue dispersion and drift of the
mean residue scale between derivative orders.
