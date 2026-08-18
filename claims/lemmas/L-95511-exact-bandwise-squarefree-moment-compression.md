# L-95511 — Exact finite moment compression of the SACF common-divisor kernel

Claim ID: `L-95511`  
Status: **PROVED EXACT REWRITING THEOREM**  
Created: 2026-08-18  
Depends on: PR #580 `L-95400--L-95402`  
RH status: **not assumed**

On dyadic band `i`, write the exact annular kernels as

\[
 J_\nu(x)=\sum_{r=1}^3 c^{(\nu)}_{i,r}x^r,
 \qquad \nu\in\{0,1\},
\tag{L-95511.1}
\]

with coefficients in `Q(sqrt(2))`.  Fix coprime odd squarefree `a,b`, one band
pair `(i,j)`, and an interval `(D_0,D_1]` on which `da/X` and `db/X` stay in
those bands.  Put

\[
 \Gamma_{a,X}(d)
 =\left(\log d+\log a\right)J_0(da/X)
  +(\log2)J_1(da/X).
\tag{L-95511.2}
\]

The corresponding SACF inner kernel is

\[
 K_{i,j}(a,b;X)
 =\sum_{D_0<d\le D_1\atop
        d\ {\mathrm{odd\ squarefree}},\ (d,ab)=1}
   \frac{\Gamma_{a,X}(d)\Gamma_{b,X}(d)}d.
\tag{L-95511.3}
\]

## Finite moment form

For `2<=ell<=6` and `0<=q<=2`, define

\[
 M_{\ell,q}(D_0,D_1;k)
 =\sum_{D_0<d\le D_1\atop
        d\ {\mathrm{odd\ squarefree}},\ (d,k)=1}
 d^{\ell-1}(\log d)^q.
\tag{L-95511.4}
\]

Expanding (L-95511.1)--(L-95511.2) gives the exact identity

\[
 \boxed{
 K_{i,j}(a,b;X)
 =\sum_{\ell=2}^6\sum_{q=0}^2
 C_{i,j,\ell,q}(a,b;X)
 M_{\ell,q}(D_0,D_1;ab),
 }
\tag{L-95511.5}
\]

where every coefficient `C` is explicit in

\[
 \mathbb Q(\sqrt2,\log2,\log a,\log b)\,X^{-\ell}.
\]

Thus each of the one hundred band pairs uses at most fifteen universal
squarefree power-log moments.  No hidden kernel or activation approximation
remains.

## Exact squarefree/coprime expansion

Let `k` be odd.  The identities

\[
 1_{d\ {\mathrm{squarefree}}}=\sum_{h^2\mid d}\mu(h),
 \qquad
 1_{(d,2k)=1}=\sum_{e\mid(d,2k)}\mu(e)
\]

give, with `L=[h^2,e]`,

\[
 \boxed{
 M_{\ell,q}(D_0,D_1;k)
 =\sum_{h\le\sqrt{D_1}}\mu(h)
  \sum_{e\mid2k}\mu(e)L^{\ell-1}
  \sum_{D_0/L<n\le D_1/L}
  n^{\ell-1}(\log L+\log n)^q.
 }
\tag{L-95511.6}
\]

This is exact, including oddness, squarefreeness, coprimality, real activation
endpoints and the `J_1` boundary channel.

## Consequence

`UOSACF` is a finite linear combination of one-sided Möbius-weighted divisor
forms whose inner arithmetic consists only of the universal moments
(L-95511.6).  The remaining cancellation is entirely in the outer coprime
parity character `mu(a)mu(b)=mu(ab)` and the short squarefree correction
`mu(h)`; it is not hidden in the Q4 kernel.

This theorem does not estimate those outer forms.  It supplies a finite exact
interface for dispersion, upper-bound sieve, or computer-assisted discovery.
