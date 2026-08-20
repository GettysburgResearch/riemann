# R-99900 — Independent source-blind cube matching cannot close PXGC99700

Claim ID: `R-99900`  
Status: **PROVED QUANTITATIVE MECHANISM NO-GO**  
Created: 2026-08-20  
Depends on: `L-99900--L-99902`  
RH status: **not assumed**

For a fully active native block, `L-99900` proves that the optimal unmatched
mass is exactly

\[
\Delta_B=
\prod_{p\in B}\left(1-\frac1p\right),
\]

up to the fixed second labelled \(67\) factor.

Suppose the block is active at quotient scale \(Y\), so

\[
P_B=\prod_{p\in B}p\le Y.
\]

Among all such blocks, the smallest \(\Delta_B\) is obtained, up to the final
endpoint prime and fixed \(67\) decoration, by using the smallest available
primes. If \(z\) is the largest such prime, Chebyshev's bound gives

\[
\prod_{p\le z}p\le Y
\quad\Longrightarrow\quad
z\ll\log Y.
\]

Mertens' prime-product estimate then gives

\[
\prod_{p\le z}\left(1-\frac1p\right)
\asymp\frac1{\log z}.
\]

Consequently

\[
\boxed{
\Delta_B\gg\frac1{\log\log Y}.
}
\tag{R-99900.1}
\]

The activation collar from `L-99901` may be power-small, but the complete-cube
parity bias is only logarithmically small. PXGC requires a half-order-scale
residual after physical normalization. Therefore no proof which independently
solves each complete source cube and then sums the residuals can establish
PXGC99700.

The no-go is mechanism-specific. It does not refute an arithmetic cross-core
flow which uses phase, owner covariance, or cancellation between distinct
squarefree cores.
