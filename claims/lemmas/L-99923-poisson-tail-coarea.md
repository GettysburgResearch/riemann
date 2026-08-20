# L-99923 — The Cauchy-Poisson owner square is an exact coefficient-tail coarea

Claim ID: `L-99923`  
Status: **PROVED EXACT FINITE IDENTITY**  
Created: 2026-08-20  
Depends on: PRs #666--#667  
RH status: **not assumed**

Let `(c_n)` be finitely supported real coefficients and `tau>0`.  With

\[
P_\tau(\gamma)=\frac{\tau}{\pi(\tau^2+\gamma^2)},
\]

put

\[
Q_\tau(c)
:=\int_{\mathbb R}
\left|\sum_nc_nn^{\tau-i\gamma}\right|^2
P_\tau(\gamma)\,d\gamma.
\]

Since

\[
\int_{\mathbb R}e^{-i\gamma u}P_\tau(\gamma)d\gamma
=e^{-\tau|u|},
\]

we obtain

\[
\boxed{
Q_\tau(c)
=\sum_{m,n}c_mc_n\min(m,n)^{2\tau}.
}
\tag{L-99923.1}
\]

Using

\[
\min(m,n)^{2\tau}
=2\tau\int_0^{\min(m,n)}u^{2\tau-1}du
\]

and finite Fubini,

\[
\boxed{
Q_\tau(c)
=2\tau\int_0^\infty
u^{2\tau-1}
\left(\sum_{n\ge u}c_n\right)^2du.
}
\tag{L-99923.2}
\]

Equivalently, because the support lies in `n>=1`,

\[
Q_\tau(c)
=\left|\sum_nc_n\right|^2
+2\tau\int_1^\infty
u^{2\tau-1}
\left(\sum_{n\ge u}c_n\right)^2du.
\]

Thus the Poisson/Hardy frontier and the priority-Hasse frontier are governed by the same multiplicative suffix/product-boundary geometry.  This identity does not bound those tails; it removes an artificial distinction between the two formulations.
