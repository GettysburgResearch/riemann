# L-102000 — The critical cubic admits a positive compact exponential B-spline compactifier

Claim ID: `L-102000`
Status: **PROVED EXACT KERNEL/MELLIN THEOREM**
Created: 2026-08-21
Depends on: PR #676 `L-100001/L-100002`
RH status: **not assumed**

Let

\[
\Psi(y)=64\begin{cases}
3y-y^{3/2},&0<y\le1,\\
3\sqrt y-1,&y\ge1,
\end{cases}
\]

and put \(\phi(u)=\Psi(e^u)\). Direct differentiation gives a distributional Green identity

\[
D(D-\tfrac12)(D-1)(D-\tfrac32)\phi=48\delta_0.
\tag{L-102000.1}
\]

Fix \(a>1\), write \(h=\log a\), and let \((\tau_hf)(u)=f(u-h)\). For every real \(\alpha\),

\[
(I-e^{\alpha h}\tau_h)f(u)=\int_0^h e^{\alpha t}(D-\alpha)f(u-t)\,dt.
\tag{L-102000.2}
\]

Define

\[
\mathcal K_{a,3}(e^u)=
\prod_{\alpha\in\{0,1/2,1,3/2\}}
(I-e^{\alpha h}\tau_h)\phi(u).
\tag{L-102000.3}
\]

Applying (L-102000.2) four times to (L-102000.1) gives

\[
\begin{aligned}
\mathcal K_{a,3}(e^u)
=48\int_{[0,h]^4}&e^{t_1/2+t_2+3t_3/2}\\
&\times\delta(u-t_0-t_1-t_2-t_3)
\,dt_0dt_1dt_2dt_3.
\end{aligned}
\tag{L-102000.4}
\]

Hence

\[
\boxed{\mathcal K_{a,3}(y)\ge0},\qquad
\boxed{\operatorname{supp}\mathcal K_{a,3}\subset[1,a^4]}.
\tag{L-102000.5}
\]

The Mellin multiplier is

\[
\boxed{
\widehat{\mathcal K}_{a,3}(s)
=48\prod_{\alpha\in\{0,1/2,1,3/2\}}
\frac{1-a^{\alpha-s}}{s-\alpha}.
}
\tag{L-102000.6}
\]

All apparent real poles are removable. The zeros contributed by the compactifier lie only on the vertical lines

\[
\Re s\in\{0,1/2,1,3/2\}.
\]

Therefore if \(\rho\) is a hypothetical nontrivial zeta zero with \(\Re\rho>1/2\), then \(s=\rho-1/2\) is not cancelled by this multiplier. For the duplicate-67 source \(\beta\), the compactified scalar

\[
\mathcal W_{a,3}(X)=\sum_n\frac{\beta(n)}{\sqrt n}\mathcal K_{a,3}(X/n)
\]

is thus a fixed compact reciprocal-zeta detector: subpower logarithmic negative mass implies RH through `L-100002` after the finite Mellin multiplier is inserted.

## Critical firewall

This positive compactifier does **not** have the zero continuous half-order moment used by `L-100310`. In fact

\[
\boxed{
\widehat{\mathcal K}_{a,3}(1/2)
=192(\log a)(1-a^{-1/2})(\sqrt a-1)(a-1)>0.
}
\tag{L-102000.7}
\]

Consequently it may not inherit the Type-I power decay of the signed extra-notch kernel. Positivity/compactness and Type-I zero-moment decay are distinct resources.