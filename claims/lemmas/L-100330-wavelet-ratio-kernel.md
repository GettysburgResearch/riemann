# L-100330 — Exact multiplicative autocorrelation kernel for the minimal wavelet

Claim ID: `L-100330`  
Status: **PROVED EXACT MELLIN/PHASE EXPANSION**  
Created: 2026-08-20  
Depends on: PR #675 minimal wavelet definitions  
RH status: **not assumed**

Let `K_0` be the compact ratio-eight kernel of PR #674/#675 and define

\[
F_\gamma(X)=\sum_{n\ge1}\mu(n)n^{1/2-i\gamma}K_0(X/n),
\]

\[
Q_X=\int_{\mathbb R}|F_\gamma(X)|^2
\frac{d\gamma}{\pi(1+\gamma^2)}.
\]

The Cauchy characteristic function gives

\[
\int_{\mathbb R}(m/n)^{-i\gamma}
\frac{d\gamma}{\pi(1+\gamma^2)}
=e^{-|\log(m/n)|}
=\frac{\min(m,n)}{\max(m,n)}.
\]

Hence

\[
\boxed{
Q_X=\sum_{m,n}\mu(m)\mu(n)\sqrt{mn}
\frac{\min(m,n)}{\max(m,n)}
K_0(X/m)K_0(X/n).
}
\tag{L-100330.1}
\]

For `sigma>3/2`, absolute Fubini is legitimate.  If `m<=n`, put `r=n/m` and
`X=mu`.  Compact support forces `1<=r<=8`, and define

\[
\boxed{
\kappa_\sigma(r)=r^{-1/2}
\int_r^8K_0(u)K_0(u/r)u^{-2\sigma-1}\,du.
}
\tag{L-100330.2}
\]

Then the complete weighted energy is

\[
\boxed{
\begin{aligned}
\mathcal E(\sigma)
={}&\kappa_\sigma(1)
\sum_m\frac{\mu(m)^2}{m^{2\sigma-1}}\\
&+2\sum_{m<n\le8m}
\mu(m)\mu(n)m^{1-2\sigma}\kappa_\sigma(n/m).
\end{aligned}
}
\tag{L-100330.3}
\]

Thus the open spectral theorem is not an unrestricted long-range correlation:
it is a fixed multiplicative band `1<n/m<=8` with one explicit kernel.

For `1<sigma<=3/2`, (L-100330.3) is used on finite physical truncations; the
remaining theorem is precisely uniform convergence as the truncation grows.
