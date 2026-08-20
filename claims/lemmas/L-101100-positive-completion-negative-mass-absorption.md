# L-101100 — Positive-completion negative-mass absorption

## Statement

Let `(Omega,nu)` be a measure space.  For `1<=i,j<=m`, let `K_ij` be positive linear operators on real measurable functions: `u>=0` implies `K_ij u>=0`.  Assume

\[
 \int K_{ij}u\,d\nu\le m_{ij}\int u\,d\nu
 \qquad(u\ge0),
\]

where `M=(m_ij)` is a finite nonnegative matrix.

Let

\[
 g_i=f_i+\sum_jK_{ij}f_j.
\]

Put

\[
 n_i=\int(f_i)_-\,d\nu,
 \qquad r_i=\int(g_i)_-\,d\nu,
 \qquad b_i=\sum_j\int K_{ij}f_j\,d\nu.
\]

Whenever the displayed quantities are finite,

\[
 \boxed{\;n\le r+b+Mn.\;}
\]

Consequently, if `b<=e` and the spectral radius `rho(M)<1`, then

\[
 \boxed{\;n\le (I-M)^{-1}(r+e).\;}
\]

The inverse is entrywise nonnegative.

## Proof

For each `i`,

\[
 (f_i)_-=\left(\sum_jK_{ij}f_j-g_i\right)_+
 \le (g_i)_-+\left(\sum_jK_{ij}f_j\right)_+.
\]

Positivity of every `K_ij` gives

\[
 \left(\sum_jK_{ij}f_j\right)_+
 \le \sum_jK_{ij}(f_j)_+.
\]

Since `(f_j)_+=f_j+(f_j)_-`,

\[
 (f_i)_-
 \le (g_i)_-+\sum_jK_{ij}f_j+\sum_jK_{ij}(f_j)_-.
\]

The right side is nonnegative because its last two sums combine to
`sum_j K_ij(f_j)_+`.  Integration and the operator bounds prove
`n<=r+b+Mn`.

For a finite nonnegative matrix with `rho(M)<1`, the Neumann series

\[
 (I-M)^{-1}=\sum_{k\ge0}M^k
\]

converges and is entrywise nonnegative.  Multiplying the preceding vector
inequality by this inverse proves the conclusion.  No absolute value is
placed on the signed flux `b`.

## Two-channel criterion

For

\[
 M=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad a,b,c,d\ge0,
\]

one has `rho(M)<1` exactly when

\[
 a<1,\qquad d<1,\qquad bc<(1-a)(1-d).
\]

Indeed, these are precisely positivity of the leading principal minors of
`I-M` together with nonnegativity of `M`; equivalently, the Perron root lies
below one.

## Why this is an AND gate

One row by itself permits the uncontrolled channel to be arbitrarily large.
Two rows with subcritical Perron coupling force both negative masses to be
small.  This is the formal mechanism sought in T-101100.
