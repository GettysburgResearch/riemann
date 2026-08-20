# L-100130 — Exact Poisson–Mellin energy identity for the minimal Möbius wavelet

Claim ID: `L-100130`  
Status: **PROVED EXACT HILBERT-SPACE IDENTITY**  
Created: 2026-08-20  
Depends on: PR #674 definitions  
RH status: **not assumed**

Let

\[
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},
\qquad
W_0(y)=\int_1^yT(v){dv\over v},
\]

with zero extension below one, and let

\[
\mathscr D=(I-\sqrt2S_2)(I-S_2)^2.
\]

The compact kernel of PR #674 is

\[
K_0=\mathscr DW_0,
\qquad \operatorname{supp}K_0\subset[1,8].
\]

Its Mellin transform is

\[
\boxed{
\widehat K_0(s)
=(1-\sqrt2\,2^{-s})(1-2^{-s})^2
 {s+\frac32\over s^2(s-\frac12)}.
}
\tag{L-100130.1}
\]

Indeed,

\[
\widehat T(s)={s+\frac32\over s(s-\frac12)},
\qquad
\widehat W_0(s)={\widehat T(s)\over s},
\]

and endpoint dilation has multiplier `2^(-s)`.
The apparent poles at `s=0` and `s=1/2` are removed by the displayed finite
differences, as required by compact support.

For real `gamma` define

\[
F_\gamma(X)
=\sum_{n\ge1}\mu(n)n^{1/2-i\gamma}K_0(X/n).
\tag{L-100130.2}
\]

The Cauchy–Poisson square in `MWOC99910` is exactly

\[
Q_X=\int_{\mathbb R}|F_\gamma(X)|^2
 {d\gamma\over\pi(1+\gamma^2)}.
\tag{L-100130.3}
\]

For `Re s>3/2`, absolute Fubini gives

\[
\boxed{
\int_1^\infty F_\gamma(X)X^{-s-1}dX
={\widehat K_0(s)\over
 \zeta(s-\frac12+i\gamma)}.
}
\tag{L-100130.4}
\]

For `sigma>3/2`, Mellin Plancherel and Tonelli therefore give

\[
\boxed{
\begin{aligned}
\mathcal E(\sigma)
&:=\int_1^\infty Q_X X^{-2\sigma}{dX\over X}\\
&={1\over2\pi}
\int_{\mathbb R}{d\gamma\over\pi(1+\gamma^2)}
\int_{\mathbb R}
{ |\widehat K_0(\sigma+it)|^2
 \over
 |\zeta(\sigma-\frac12+i(t+\gamma))|^2}\,dt.
\end{aligned}}
\tag{L-100130.5}
\]

The identity extends to every `sigma` in the weighted-L2 convergence
half-plane by ordinary Mellin-Hardy continuation.

## Pole-safety audit

Every zero of the finite wavelet multiplier lies on `Re s=0` or
`Re s=1/2`. Hence if `rho` is a nontrivial zeta zero with `Re rho>1/2`, then
for every real `gamma`

\[
s_{\rho,\gamma}=\rho+\frac12-i\gamma
\]

has `Re s_(rho,gamma)>1` and

\[
\widehat K_0(s_{\rho,\gamma})\ne0.
\]

Thus no off-line reciprocal-zeta pole is cancelled by the compactifier.