# T-107100 — q-adic annular finite features record the exact zero abscissa

**Claim ID:** `T-107100`  
**Status:** unconditional quantitative detector theorem; open estimate remains  
**Date:** 2026-08-31  
**RH:** unproved

Let

\[
\Theta=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

For each outer horizon `Z`, form the vectors of L-107101 and define

\[
\mathfrak A_{67}(X)=\max_{2\le Z\le X}
\sum_{j=0}^{\lfloor\log_{67}Z\rfloor}\|c_{Z,j}\|^2.
\]

Then

\[
\boxed{\limsup_{X\to\infty}\frac{\log(1+\mathfrak A_{67}(X))}{\log X}
=2\Theta-1.}\tag{1}
\]

Equivalently, for `1/2<=sigma<=1`,

\[
\boxed{\zeta(s)\ne0\ (\Re s>\sigma)
\Longleftrightarrow
\mathfrak A_{67}(X)\ll_\epsilon X^{2\sigma-1+\epsilon}.}\tag{2}
\]

In particular,

\[
\boxed{\mathrm{RH}\Longleftrightarrow \mathfrak A_{67}(X)=X^{o(1)}.}\tag{3}
\]

**Upper exponent.** A zero-free half-plane gives the classical maximal
Mertens bound. Abel summation and reverse logarithmic demodulation give,
uniformly for the retained `|t|=O(loglog X)`, q-free half-weighted prefixes of
size `X^{sigma-1/2+epsilon}`. The number of frequencies and annuli and every
frame loss are polylogarithmic.

**Lower exponent.** The finite Hardy inverse recovers the outer q-free prefix
vector from its annular stack. L-107100 recovers beta with constant
conditioning. A fixed grid index has `t=O(1/log X)`; because the fixed compact
transform is analytic and nonzero, its first surviving Taylor coefficient
makes its weight `X^{o(1)}` above and below. The single-harmonic transport of
L-106800 then forces `Theta<=sigma`. The outer maximum retains the required
maximal-prefix information.

The source-locked Vinogradov--Korobov bound also transfers:

\[
\boxed{\mathfrak A_{67}(X)\ll X\exp[-c(\log X)^{3/5}(\log\log X)^{-1/5}].}\tag{4}
\]

By L-107102, the new conclusion-facing target is the assembled signed annular
primitive-core interference. It is weaker and more source-faithful than
proving a positive square separately for every core, but remains exactly of
RH strength.
