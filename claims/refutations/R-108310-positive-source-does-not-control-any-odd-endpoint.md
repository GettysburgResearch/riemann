# R-108310 — Positive Fourier source does not control the direct phase at any odd endpoint

Claim ID: `R-108310`  
Status: **PROVED EXACT COUNTERMODEL FAMILY**  
Created: 2026-08-31

Fix `c>1`, `n>=1`, and put

\[
F(t)=c+\cos(nt).
\]

For every odd

\[
K=2m+1,
\]

one has

\[
F^{(K)}(t)=(-1)^{m+1}n^K\sin(nt),
\]

\[
F^{(K+1)}(t)=(-1)^{m+1}n^{K+1}\cos(nt).
\]

At the simple real zeros

\[
c_j={j\pi\over n}
\]

of `F^(K)`,

\[
\rho_{K,j}
=
{c+(-1)^j
 \over
 (-1)^{m+1+j}n^{K+1}}.
\]

Because `c+(-1)^j>0`, the residue signs alternate at every adjacent edge.
The parent `F` has no real zero.

On the other hand, with

\[
\tau_K=(-1)^{(K+3)/2}=(-1)^m,
\]

a direct calculation gives

\[
\boxed{
\tau_K
\left(F'F^{(K)}-FF^{(K+1)}\right)
=
n^{K+1}(1+c\cos nt).
}
\tag{R-108310.1}
\]

The right side is the Fourier transform of the positive even measure

\[
n^{K+1}\delta_0
+{cn^{K+1}\over2}
(\delta_n+\delta_{-n}).
\]

Thus, for every odd endpoint, all of the following may hold simultaneously:

```text
positive even parent Fourier source;
positive endpoint-Wronskian Fourier source after the canonical sign;
100% simple real zeros of the odd derivative;
residue-sign transition on every adjacent edge;
no real parent zero.
```

Therefore neither positive Fourier source, high-derivative real-rootedness nor
their formal conjunction proves `XI31MINPHASE108310`. A valid completion must
use a genuinely Xi-specific physical phase/index theorem.
