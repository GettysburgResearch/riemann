# L-99810 — The Cauchy–Poisson packet is exactly a Hardy square of truncated native tails

Claim ID: `L-99810`  
Status: **PROVED EXACT ANALYTIC IDENTITY**  
Created: 2026-08-20  
Depends on: the Poisson packet of PR #659  
RH status: **not assumed**

Let `(c_n)` be a finitely supported complex sequence on the positive integers
and let `tau>0`. Put

\[
 D_\tau(\gamma)=\sum_n c_n n^{\tau-i\gamma},
 \qquad
 P_\tau(\gamma)=\frac{\tau}{\pi(\tau^2+\gamma^2)},
\]

and

\[
 Q_\tau(c)=\int_{\mathbb R}|D_\tau(\gamma)|^2
 P_\tau(\gamma)\,d\gamma.
\tag{L-99810.1}
\]

## 1. Exact minimum kernel

The characteristic function of the Cauchy law is

\[
 \int_{\mathbb R}e^{-i\gamma u}P_\tau(\gamma)d\gamma
 =e^{-\tau|u|}.
\]

Finite expansion therefore gives

\[
\begin{aligned}
 Q_\tau(c)
 &=\sum_{m,n}c_m\overline{c_n}(mn)^\tau
   e^{-\tau|\log(m/n)|}\\
 &=\boxed{\sum_{m,n}c_m\overline{c_n}\min(m,n)^{2\tau}.}
\end{aligned}
\tag{L-99810.2}
\]

## 2. Exact truncated-tail square

For `m,n>=1`,

\[
 \min(m,n)^{2\tau}
 =1+2\tau\int_1^\infty
 t^{2\tau-1}\mathbf1_{t\le m}\mathbf1_{t\le n}\,dt.
\tag{L-99810.3}
\]

Insert (L-99810.3) into (L-99810.2) and use finite Fubini. The result is

\[
\boxed{
 Q_\tau(c)
 =\left|\sum_nc_n\right|^2
 +2\tau\int_1^\infty t^{2\tau-1}
   \left|\sum_{n\ge t}c_n\right|^2dt.
}
\tag{L-99810.4}
\]

Thus the Poisson point-evaluation inequality of PR #659 is simply the first
summand of an exact orthogonal positive decomposition. The entire off-diagonal
problem is the Hardy square of the truncated physical tails.

For ordered support `1<n_1<...<n_N`, (L-99810.4) is equivalently

\[
 Q_\tau(c)
 =\left|\sum_{j=1}^Nc_{n_j}\right|^2
 +\sum_{j=1}^N
 (n_j^{2\tau}-n_{j-1}^{2\tau})
 \left|\sum_{k=j}^Nc_{n_k}\right|^2,
\tag{L-99810.5}
\]

with `n_0=1`.

## 3. Application to the canonical block packet

For PR #659, take

\[
 c_n=c_{L,y}(n)
 =\frac{\beta_{67}(n)}{\sqrt n}(\mathcal F_LT)(y/n),
 \qquad \tau=\tau_L.
\]

Then `Q_L(y)` is exactly the right side of (L-99810.4). Consequently the
remaining `GPMOC99800` estimate is not a mysterious phase average: it is a
weighted Carleson estimate for the actual truncated native tails

\[
 S_{L,y}(t)=\sum_{n\ge t}c_{L,y}(n).
\]

No diagonal estimate, owner variance or free labelled norm controls these tails
without an additional arithmetic packing theorem.