# R-106800 — Endpoint-only sampling and source-blind low-rank control do not yield the spectral-abscissa theorem

Claim ID: `R-106800`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-27  
RH status: **unproved**

## 1. The maximal prefix is load-bearing

For every \(m\ge1\), consider the finite coefficient sequence

\[
c_1=\cdots=c_m=1,
\qquad
c_{m+1}=\cdots=c_{2m}=-1.
\]

Then

\[
\max_{N\le2m}
\left|\sum_{n\le N}c_n\right|
=m,
\]

while

\[
\sum_{n\le2m}c_n=0.
\]

The same construction may be embedded in a modulated sequence by multiplying
\(c_n\) by \(n^{it}\). Hence a common-period maximal-prefix theorem cannot be
replaced by the single endpoint \(Y=X\) through finite Fourier algebra alone.

`T-106800` makes no assertion that the endpoint beta energy
\(\mathcal E_B(X)\), without a maximum over \(Y\le X\), has exponent
\(2\Theta-1\).

## 2. Low rank does not control the source-blind norm

The pinned first-harmonic firewall constructs the literal unsigned beta
vector and proves

\[
\lambda_{\max}(G_X)
\gg_r
\frac{X}{(\log X)^{2r+2}}
\]

for the retained critical Gram \(G_X\), even though

\[
\operatorname{rank}G_X=X^{o(1)}.
\]

Thus the upper bound in `L-106801` must pass through the actual signed
Mertens source. It cannot be replaced by an operator-norm, Bessel, low-rank,
support-count, or unsigned beta estimate.

## 3. Faster rough deletion is not included

The rough coordinate is power-isomorphic only when

\[
\limsup
\frac{\log y_X}{\log\log X}\le2.
\]

For \(y_X=(\log X)^A\) with fixed \(A>2\), the positive conditioning masses
already have power exponent \(1/2-1/A\). The theorem does not claim that the
signed rough coordinate loses the zeta exponent beyond this boundary; it
only refuses to delete that polynomial conditioning cost without a new
signed argument.
