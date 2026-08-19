# L-99102 — A one-sided optimal notch localizes the entire surviving problem to one multiplicative annulus

Claim ID: `L-99102`  
Status: **PROVED LOCALIZATION THEOREM**  
Created: 2026-08-19  
Depends on: `L-99101`  
RH status: **not assumed**

Let `chi` be a fixed smooth cutoff supported in `[0,1]` and equal to one in a neighborhood of `2delta`. Insert

\[
\chi(\log n/T)
\]

into the optimally notched packet, with

\[
M=2q^2T+O(1),
\qquad q=\frac12-\delta.
\]

The cutoff removes the second magnitude saddle

\[
x_+=2-2\delta>1
\]

without changing the hypothetical-zero contribution at `rho`. The unique remaining magnitude saddle is

\[
x_-=2\delta.
\]

Laplace localization therefore confines the arithmetic problem to

\[
\boxed{
\log n=2\delta T+O_\delta(\sqrt T),
\qquad
n=\exp(2\delta T+O_\delta(\sqrt T)).
}
\tag{L-99102.1}
\]

All regions outside this annulus are exponentially smaller than `exp((delta-delta^2)T)`.

The first `theta` variation of the localized packet is the generalized-prime phase carrier

\[
-\sum_{r\in\mathcal Q}
 \frac{\Lambda_\diamond(r)}{\sqrt r}
 \chi(\log r/T)
 \left(\frac{1-\log r/T}{2q_0}\right)^M
 e^{-(\log r)^2/(4T)}e^{-i\gamma\log r},
\]

with `q_0=1/2-delta`. Hence the surviving theorem is a genuinely phase-locked prime-power cancellation statement on one sharply prescribed multiplicative annulus. It is not a common-half-plane alignment, block-count, or source-blind large-sieve estimate.
