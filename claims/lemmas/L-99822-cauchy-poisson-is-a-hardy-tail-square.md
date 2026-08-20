# L-99822 — Every Cauchy–Poisson coefficient square is an exact Hardy tail square

Claim ID: `L-99822`  
Status: **PROVED EXACT FINITE HILBERT IDENTITY**  
Created: 2026-08-20  
Depends on: PR #659 `L-99803`  
RH status: **not assumed**

Let `(c_n)` be a finite complex coefficient packet and let `tau>0`. Put

\[
D_\tau(\gamma)=\sum_nc_n n^{\tau-i\gamma},
\qquad
P_\tau(\gamma)=\frac{\tau}{\pi(\tau^2+\gamma^2)},
\]

and

\[
Q_\tau=\int_{\mathbb R}|D_\tau(\gamma)|^2
P_\tau(\gamma)\,d\gamma.
\]

The characteristic function of the Cauchy density is

\[
\int_{\mathbb R}e^{-i\gamma v}P_\tau(\gamma)d\gamma
=e^{-\tau|v|}.
\]

Finite expansion therefore gives

\[
\boxed{
Q_\tau=\sum_{m,n}c_m\overline{c_n}\min(m,n)^{2\tau}.
}
\tag{L-99822.1}
\]

Since

\[
\min(m,n)^{2\tau}
=1+2\tau\int_1^{\min(m,n)}v^{2\tau-1}dv,
\]

finite Fubini yields

\[
\boxed{
Q_\tau
=\left|\sum_nc_n\right|^2
+2\tau\int_1^\infty
 \left|\sum_{n\ge v}c_n\right|^2v^{2\tau-1}dv.
}
\tag{L-99822.2}
\]

Equivalently, if `1<=n_1<...<n_N`, `S_j=sum_(ell>=j)c_(n_ell)`, and `n_0=0`,
then

\[
\boxed{
Q_\tau=\sum_{j=1}^N
 (n_j^{2\tau}-n_{j-1}^{2\tau})|S_j|^2.
}
\tag{L-99822.3}
\]

## Consequence for GPMOC

For the packet `c_(L,y)(n)` of PR #659, `Q_L(y)` is therefore not an opaque
phase square. It is exactly the point value `|f_L(y)|^2` plus the positive
square energy of every nested arithmetic tail

\[
\sum_{n\ge v}\frac{\beta(n)}{\sqrt n}(\mathcal F_LT)(y/n).
\]

The local owner gap of PR #659 controls coefficient-level dissipation. It does
not, without a further arithmetic embedding, control the nested tail sums in
(L-99822.2). Thus the remaining off-diagonal theorem is precisely a Hardy
Carleson estimate for these live tails.
