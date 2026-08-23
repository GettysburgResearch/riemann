# L-105331 — Shifted log-derivative coefficients differentiate to the reciprocal source

Claim ID: `L-105331`  
Status: **PROVED EXACT SAFE-LINE AND FINITE-DIRICHLET IDENTITY**  
Created: 2026-08-23  
Depends on: `L-105320`; pinned xi-prime coefficient definitions  
RH status: **not assumed**

Let `F` be zero-free on a safe line and put

\[
\mathcal L={F'\over F}.
\]

For `E_alpha=F'-alpha F=F(\mathcal L-\alpha)`, one has the exact logarithmic
derivative identity

\[
\boxed{
{E_\alpha'\over E_\alpha}
=\mathcal L+{\mathcal L'\over\mathcal L-\alpha}.}
\tag{L-105331.1}

Therefore

\[
\boxed{
\left.\partial_\alpha{E_\alpha'\over E_\alpha}\right|_{\alpha=0}
={\mathcal L'\over\mathcal L^2}
=\left(-{1\over\mathcal L}\right)'.}
\tag{L-105331.2}

After contour integration by parts, this is precisely `F/F'` as in
`L-105330`.

## 1. Xi-prime coefficient parameter

On the xi safe line write the frozen arithmetic part as

\[
\mathcal L(s)=L-A(s),
\qquad
A(s)=\sum_{n\ge2}\Lambda(n)n^{-s},
\]

with the archimedean and pole terms retained separately.  The prime
coefficients of `E_alpha'/E_alpha` are

\[
\boxed{C(N;L-\alpha).}
\tag{L-105331.3}

Indeed the unshifted identity is

\[
C=-\Lambda+{\Lambda\log\over L-A},
\]

in Dirichlet-convolution notation, and `alpha` only replaces `L` by
`L-alpha`.

Differentiating at zero gives

\[
\boxed{
\left.\partial_\alpha C(N;L-\alpha)\right|_0
=-\partial_LC(N;L)
=\log N\,b_L(N),}
\tag{L-105331.4}

where `b_L` is the reciprocal coefficient family of `L-105320`.

## 2. Hardy division is the primitive test

In the explicit formula, differentiating the zero statistic introduces the
primitive `H_ij`, while the desired Pick test is `-H_ij'`.  On a prime
frequency `log N`, this integration by parts divides the differentiated
coefficient by `log N`.  Thus (L-105331.4) becomes exactly `b_L(N)`.

Equivalently,

\[
{1\over\log N}=\int_0^\infty N^{-u}\,du
\]

is a positive safe-line Hardy average.  No inverse dyadic filter or new signed
coefficient source appears.

## 3. Reflection covariance

For Riemann xi, `xi(1-s)=xi(s)` and `xi'(1-s)=-xi'(s)`. Hence

\[
\boxed{E_\alpha(1-s)=-E_{-\alpha}(s).}
\tag{L-105331.5}

A single shifted zero set is not reflection invariant.  The correct explicit
formula is the oriented `+alpha/-alpha` pair, whose derivative at zero is the
low-order Pick current.  Treating one shifted field as an ordinary symmetric
ZeroConfig is invalid.
