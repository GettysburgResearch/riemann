# L-101202 — Fixed-shell amplitude plus sparse negative cells closes the detector

Claim ID: `L-101202`  
Status: **AMPLITUDE PROVED; TWO-INPUT CLOSURE PROVED; SPARSITY OPEN**  
Created: 2026-08-21  
Depends on: the fixed zero-safe compact shell of PR #665

Let \(K\) be supported in \([1,R]\), \(\|K\|_\infty\le M\), \(|\beta(n)|\le2\), and

\[
G(X)=\sum_{X/R\le n\le X}\frac{\beta(n)}{\sqrt n}K(X/n).
\]

Then

\[
|G(X)|\le2M\sum_{X/R\le n\le X}n^{-1/2}\le6M\sqrt X,
\]

so on \(I_L=[2^L,2^{L+1})\),

\[
\boxed{\int_{I_L}|G(X)|^2\frac{dX}{X}\le36M^2 2^L.}
\tag{L-101202.1}
\]

If \(\{G<0\}\cap I_L\) is contained in \(N_L\) intervals of Euclidean length at most one, then its logarithmic measure is at most \(N_L/2^L\). Hence

\[
\boxed{
\int_{I_L}G_-(X)\frac{dX}{X}\le6M\sqrt{N_L}.
}
\tag{L-101202.2}
\]

Therefore \(N_L=2^{o(L)}\) implies subpower logarithmic negative mass and RH through the fixed-shell Mellin–Landau consumer.
