# L-102832 — Same largest-two squareclass overlap is polylogarithmic

Claim ID: `L-102832`  
Status: **PROVED UNCONDITIONALLY**  
Created: 2026-08-24  
Depends on: `L-102831`; `L-102732`; `L-102749`  
RH status: **not assumed**

Fix one largest-two owner pair `p>q`. After cofactor completion its centered
physical field has the form

\[
H_{p,q}(e^u)
=
{1\over\sqrt{pq}}
\sum_a {c_{p,q}(a)\over a}
\phi\bigl(u-\log(pq)-2\log a\bigr),
\]

where `a` is squarefree, `P^+(a)<q`, and in the normalized Wick/half-divisor
core

\[
|c_{p,q}(a)|\le1.
\]

The polylogarithmic Euler/half-divisor gauge factors may be reinserted after the
estimate by the source-exact gauge theorem.

Let `R_phi` be the autocorrelation of the carrier-centered outer kernel. By
`L-102732`, its support is contained in `[-log 8,log 8]`. Hence two square cores
`a,b` can interact only when

\[
{1\over\sqrt8}<{a\over b}<\sqrt8.
\]

For every `a`,

\[
\sum_{a/\sqrt8<b<a\sqrt8}{1\over b}
\le \log 8+1.
\]

Consequently, on `pq a^2<=16Y`,

\[
\boxed{
\|H_{p,q}\|_2^2
\ll_\phi {\log(2Y)\over pq}.
}
\tag{L-102832.1}
\]

Summing over all ordered prime pairs gives

\[
\begin{aligned}
\sum_{p>q}\|H_{p,q}\|_2^2
&\ll_\phi
\log(2Y)
\sum_{p>q}{1\over pq}\\
&\ll_\phi
\log(2Y)(\log\log(3Y))^2.
\end{aligned}
\]

Thus

\[
\boxed{
\text{all different-core overlap inside one semiprime squareclass is
polylogarithmic.}
}
\tag{L-102832.2}
\]

Together with `L-102831`, this removes both equal-product and same-owner-pair
terms. Only correlations between distinct semiprime squareclasses remain.