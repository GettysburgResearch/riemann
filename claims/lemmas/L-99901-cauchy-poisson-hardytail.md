# L-99901 — The GPMOC Cauchy–Poisson square is exactly a Hardy tail energy

Claim ID: `L-99901`  
Status: **PROVED EXACT FINITE HILBERT-SPACE IDENTITY**  
Created: 2026-08-20  
Depends on: PR #659 `L-99803`  
RH status: **not assumed**

Let `(c_n)` be any finitely supported real sequence and let `tau>0`. Put

\[
D_\tau(\gamma)=\sum_n c_n n^{\tau-i\gamma},
\qquad
P_\tau(\gamma)=\frac{\tau}{\pi(\tau^2+\gamma^2)},
\]

and

\[
Q_\tau(c)=\int_{\mathbb R}|D_\tau(\gamma)|^2
P_\tau(\gamma)\,d\gamma.
\]

The characteristic function of the Cauchy law is

\[
\int_{\mathbb R}e^{-i\gamma v}P_\tau(\gamma)d\gamma
=e^{-\tau|v|}.
\]

Therefore

\[
\begin{aligned}
Q_\tau(c)
&=\sum_{m,n}c_mc_n(mn)^\tau
 e^{-\tau|\log(m/n)|}\\
&=\boxed{\sum_{m,n}c_mc_n\min(m,n)^{2\tau}}.
\end{aligned}
\tag{L-99901.1}
\]

Since

\[
\min(m,n)^{2\tau}
=\int_0^{\min(m,n)}2\tau t^{2\tau-1}dt,
\]

finite Fubini gives the exact Hardy representation

\[
\boxed{
Q_\tau(c)
=2\tau\int_0^\infty t^{2\tau-1}
\left(\sum_{n\ge t}c_n\right)^2dt.
}
\tag{L-99901.2}
\]

At `tau=1/2`, this becomes the exact discrete identity

\[
\boxed{
Q_{1/2}(c)=\sum_{k\ge1}
\left(\sum_{n\ge k}c_n\right)^2.
}
\tag{L-99901.3}
\]

Applied to the literal coefficients `c_{L,y}(n)` of PR #659, `GPMOC99800` is
therefore not an unspecified two-dimensional phase estimate. It is one
weighted cumulative-tail square-function estimate. The diagonal bound does
not control (L-99901.2); cancellation in the cumulative tails remains the
load-bearing arithmetic input.
