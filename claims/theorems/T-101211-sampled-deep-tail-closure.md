# T-101211 — A sampled deep-tail theorem closes the fixed-shell route

Claim ID: `T-101211`  
Status: **PROVED CONDITIONAL CLOSURE; ONE DISCRETE TAIL ESTIMATE OPEN**  
Created: 2026-08-21

Let

\[
x_N=N+\frac12,
\qquad
D_L(\tau)=\#\{N\in[2^L,2^{L+1}):G(x_N)<-\tau\}.
\]

Suppose there is a threshold sequence `tau_L=2^o(L)`, with `tau_L>=1` eventually, such that

\[
\boxed{D_L(\tau_L)=2^{o(L)}.}
\tag{T-101211.1}
\]

By `L-101213`, every cell containing a point below `-2tau_L` is counted by `D_L(tau_L)` for large `L`. Apply `L-101211` with depth `2tau_L` to obtain

\[
\int_{2^L}^{2^{L+1}}G_-(X)\frac{dX}{X}=2^{o(L)}.
\]

Summation over dyadic blocks gives subpower logarithmic negative mass for the fixed zero-safe scalar, and the Mellin–Landau consumer yields RH.

Thus the corrected remaining statement is not “most cells are nonnegative.” It is the weaker carrier-preserving assertion that values below a slowly growing negative threshold occur at only subpower many canonical samples per dyadic block.

```text
exact cell formula                  PROVED
unit-cell oscillation O(N^-1/2)     PROVED
sampled deep-tail -> negative mass  PROVED
sampled deep-tail estimate          OPEN / RH-BEARING
Riemann Hypothesis                  UNPROVEN
```
