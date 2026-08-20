# L-100711 — The long double-owner sector is eventually positive

Claim ID: `L-100711`  
Status: **PROVED UNCONDITIONALLY**  
Created: 2026-08-20  
Depends on: `L-100710`; PR #689 compact Abel–Mertens frame; the classical quantitative PNT  
RH status: **not assumed**

With the notation of `L-100710`,

\[
\boxed{
G_{\rm lo}(X)
=\kappa_0{\sqrt X\over\log X}
+O\!\left({\sqrt X\over\log^2X}\right).
}
\tag{L-100711.1}
\]

In particular

\[
\boxed{G_{\rm lo}(X)>0}
\qquad\text{for all sufficiently large }X.
\tag{L-100711.2}
\]

Consequently `LRNM100704` is true in the stronger form

\[
\int_{2^L}^{2^{L+1}}(G_{\rm lo}(X))_-{dX\over X}=0
\]

for all sufficiently large `L`.

## Proof

PR #689 gives the exact compact Abel–Mertens frame

\[
G_\mu(X)
=X^{-1/2}\int_1^8M(X/y)V(y)\,dy,
\tag{L-100711.3}
\]

where `M(t)=sum_(n<=t)mu(n)` and `V` is a fixed bounded piecewise-smooth
function.

The classical zero-free region for `zeta` gives the unconditional estimate

\[
M(t)\ll t\exp\!\left[-c(\log t)^{3/5}(\log\log t)^{-1/5}\right].
\tag{L-100711.4}
\]

Substitution in (L-100711.3) yields

\[
G_\mu(X)
\ll\sqrt X\exp\!\left[-c'(\log X)^{3/5}
 (\log\log X)^{-1/5}\right]
=o\!\left({\sqrt X\over\log^2X}\right).
\tag{L-100711.5}
\]

Since the source partition is exact,

\[
G_{\rm lo}=G_\mu-G_{\rm sh}.
\]

Combining (L-100711.5) with `L-100710.2` proves (L-100711.1) and eventual
positivity.

## Meaning

The long region is not the obstruction in the submitted matrix. Its leading
positive carrier is exactly the cancellation partner of the negative singleton
prime carrier in the short region. The original gluing loses this cancellation
by replacing `G_sh` with `|G_sh|`.
