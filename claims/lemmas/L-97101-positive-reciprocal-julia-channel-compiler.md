# L-97101 — The reciprocal state behind the unique scalar has a positive coefficient-one Julia compiler

Claim ID: `L-97101`  
Status: **PROVED EXACT ARITHMETIC THEOREM**  
Created: 2026-08-17  
Depends on: `L-97100`  
RH status: **not assumed**

Write `n=2^e m` with `m` odd. From
\[
G_\diamond(z)
=
\frac{\zeta_{\rm odd}(z)}{(1-2^{-z})^2(1-2^{-z-1})},
\]
one obtains
\[
\boxed{g_\diamond(2^em)=2e+2^{-e}>0.}
\tag{L-97101.1}
\]
Together with (L-97100.4),
\[
\boxed{|b_\diamond(n)|\le g_\diamond(n).}
\tag{L-97101.2}
\]
Define
\[
u_\diamond^\pm(n)=g_\diamond(n)\pm b_\diamond(n)\ge0
\]
and
\[
\Sigma_\diamond(n)=
\begin{pmatrix}
g_\diamond(n)&b_\diamond(n)\\
b_\diamond(n)&g_\diamond(n)
\end{pmatrix}\succeq0.
\tag{L-97101.3}
\]

Define the generalized von Mangoldt source by
\[
-\frac{G_\diamond'(z)}{G_\diamond(z)}
=
\sum_{n\ge2}\frac{\Lambda_\diamond(n)}{n^z}.
\]
Its only nonzero values are
\[
\boxed{
\Lambda_\diamond(p^r)=\log p\quad(p\text{ odd}),
\qquad
\Lambda_\diamond(2^r)=(2+2^{-r})\log2,
}
\tag{L-97101.4}
\]
so `Lambda_diamond>=0`.

Coefficient comparison in the logarithmic derivatives of `G_diamond` and `B_diamond=1/G_diamond` gives
\[
g_\diamond(n)\log n
=
\sum_{d\mid n,d>1}
\Lambda_\diamond(d)g_\diamond(n/d),
\tag{L-97101.5}
\]
\[
b_\diamond(n)\log n
=-
\sum_{d\mid n,d>1}
\Lambda_\diamond(d)b_\diamond(n/d).
\tag{L-97101.6}
\]
Hence the two positive channels swap exactly:
\[
\boxed{
u_\diamond^+(n)\log n
=
\sum_{d\mid n,d>1}\Lambda_\diamond(d)u_\diamond^-(n/d),}
\tag{L-97101.7}
\]
\[
\boxed{
u_\diamond^-(n)\log n
=
\sum_{d\mid n,d>1}\Lambda_\diamond(d)u_\diamond^+(n/d).}
\tag{L-97101.8}
\]
Every coefficient is spent once. A rough-prime parity flip conjugates `Sigma_diamond` by the channel-swap matrix and therefore preserves positive semidefiniteness. This is the parity-safe replacement for the terminal sign promotion refuted in `R-97100`.

The remaining difficulty is not source positivity. It is a trace-free extraction of the boundary defect `1-B_diamond` from this positive two-channel state.
