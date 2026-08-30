# L-108310 — Every odd endpoint has one direct entire companion phase

Claim ID: `L-108310`  
Status: **PROVED EXACT REAL-ANALYTIC AND FOURIER-SOURCE THEOREM**  
Created: 2026-08-31  
Depends on: `L-108300`; PR #772 `L-107401` for the later source constant only  
RH status: **not assumed**

Let `K>=1` be odd and let `f` be real analytic on a neighbourhood of a
compact interval. Put

\[
g=f^{(K)},
\qquad
W_K=f'g-fg'.
\tag{L-108310.1}
\]

For `sigma in {+1,-1}` and `epsilon>0`, define the entire companion

\[
E_{K,\sigma,\epsilon}
=
g+i\sigma\epsilon f.
\tag{L-108310.2}
\]

## 1. Exact phase identity

On every regular real component,

\[
\boxed{
{d\over dx}\arg E_{K,\sigma,\epsilon}(x)
=
{\sigma\epsilon W_K(x)
 \over g(x)^2+\epsilon^2f(x)^2}.
}
\tag{L-108310.3}
\]

Accordingly define the negative phase variation

\[
\boxed{
\mathscr U_{K,\sigma,\epsilon}(f;I)
=
{1\over\pi}\int_I
{\epsilon(-\sigma W_K(x))_+
 \over g(x)^2+\epsilon^2f(x)^2}
\,dx.
}
\tag{L-108310.4}
\]

At a noncommon zero `c` of `g`, write

\[
{g\over f}
=
\alpha_c(x-c)^r+O((x-c)^{r+1}).
\]

The same Cauchy-angle calculation as in `L-108300` gives the local limiting
weight

\[
\omega_{K,\sigma}(c)=
\begin{cases}
1,&r\text{ odd and }\sigma\alpha_c>0,\\
0,&r\text{ odd and }\sigma\alpha_c<0,\\
1/2,&r\text{ even}.
\end{cases}
\tag{L-108310.5}
\]

Thus

\[
\boxed{
\lim_{\epsilon\downarrow0}
\mathscr U_{K,\sigma,\epsilon}(f;I)
=
\sum_{f^{(K)}(c)=0,\ f(c)\ne0}
\omega_{K,\sigma}(c).
}
\tag{L-108310.6}
\]

At a simple zero define

\[
\rho_{K,c}
=
{f(c)\over f^{(K+1)}(c)}.
\]

Since

\[
W_K(c)
=-f(c)f^{(K+1)}(c)
=-\rho_{K,c}\,f^{(K+1)}(c)^2,
\]

one has

\[
\boxed{
\omega_{K,\sigma}(c)
=
\mathbf1_{\{\sigma\rho_{K,c}>0\}}.
}
\tag{L-108310.7}
\]

The companion is entire, so an ordinary real zero of `f` which is not shared
with `f^(K)` creates no quotient pole or artificial phase atom.

## 2. Exact positive Fourier source

Assume now the full-line convention

\[
f(t)=\int_{\mathbb R}\Phi(u)e^{iut}\,du,
\qquad \Phi(u)\ge0,
\qquad \Phi(-u)=\Phi(u),
\]

with enough decay to justify the products. Put

\[
\tau_K=(-1)^{(K+3)/2}.
\]

The symmetrized product calculation gives

\[
\boxed{
\tau_KW_K(t)
=
\int_{\mathbb R}L_K(\xi)e^{i\xi t}\,d\xi,
}
\tag{L-108310.8}
\]

where, up to the Fourier-convolution normalization,

\[
\boxed{
L_K(\xi)
=
{1\over2}
\int_{u+v=\xi}
(u-v)(u^K-v^K)\Phi(u)\Phi(v)\,du
\ge0.
}
\tag{L-108310.9}
\]

The sign follows because `K` is odd and

\[
(u-v)(u^K-v^K)\ge0.
\]

Equivalently, the algebra used in the symmetrization is

\[
uv^K-v^{K+1}+vu^K-u^{K+1}
=-(u-v)(u^K-v^K).
\tag{L-108310.10}
\]

Thus every odd endpoint has a literal positive Fourier source after the
fixed sign `tau_K`. As `R-108310` shows, this positive source does not by
itself control the minority phase count.

## Scope

The theorem is exact for every fixed positive odd endpoint. It neither
estimates the Xi phase variation nor converts the carrier-adapted Fourier
source constant into a physical companion count.
