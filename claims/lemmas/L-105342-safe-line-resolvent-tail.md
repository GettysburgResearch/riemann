# L-105342 — Safe-line resolvent and power-saving tail

Claim ID: `L-105342`  
Status: **PROVED EXACT**

Let `a(1)=0` and suppose

\[
A(s)=\sum_{n\ge2}a(n)n^{-s}
\]

converges absolutely on `Re s>=sigma_0>1`. Write

\[
A_{\rm abs}(\sigma_0)=\sum_{n\ge2}|a(n)|n^{-\sigma_0}.
\]

If `|L|>A_abs(sigma_0)`, then in the Dirichlet-convolution algebra

\[
R_L=(L\delta_1-a)^{-*}=\sum_{k\ge0}L^{-k-1}a^{*k}
\]

converges absolutely and satisfies

\[
\boxed{\sum_{n\ge1}R_L(n)n^{-s}=1/(L-A(s)).}
\tag{L-105342.1}
\]

Moreover

\[
\sum_{n\ge1}|R_L(n)|n^{-\sigma_0}
\le\frac1{|L|-A_{\rm abs}(\sigma_0)}.
\tag{L-105342.2}
\]

For `sigma>sigma_0` and `X>=1`,

\[
\boxed{
\sum_{n>X}|R_L(n)|n^{-\sigma}
\le\frac{X^{-(\sigma-\sigma_0)}}{|L|-A_{\rm abs}(\sigma_0)}.}
\tag{L-105342.3}
\]

For Xi on a right safe line,

\[
\xi'/\xi=G(s)-A(s),\qquad A(s)=\sum\Lambda(n)n^{-s},
\]

so freezing the archimedean carrier at `L` gives the exact split

\[
\boxed{
\frac{\xi}{\xi'}(s)
=\frac1{L-A(s)}+
\frac{L-G(s)}{(G(s)-A(s))(L-A(s))}.}
\tag{L-105342.4}
\]

The second term is the pinned archimedean-freezing error. Taking
`sigma_0=9/8`, `sigma=5/4`, and `X=T^lambda` gives a reciprocal coefficient
tail `O(T^{-lambda/8}/|L|)` once `|L|` exceeds the fixed absolute Euler sum.
