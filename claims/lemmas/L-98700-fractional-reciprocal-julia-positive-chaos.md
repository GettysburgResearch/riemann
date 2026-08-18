# L-98700 — Fractional reciprocal-Julia powers have an exact positive two-channel chaos

Claim ID: `L-98700`  
Status: **PROVED EXACT ALGEBRAIC THEOREM**  
Created: 2026-08-18  
Depends on: `L-97100`, `L-97101`  
RH status: **not assumed**

Let

\[
G_\diamond(s)
=\frac{\zeta_{\rm odd}(s)}{(1-2^{-s})^2(1-2^{-s-1})},
\qquad
B_\diamond(s)=G_\diamond(s)^{-1}.
\]

On `Re s>1`, write

\[
L_\diamond(s)=\log G_\diamond(s)
=\sum_{q\in\mathcal Q}\lambda_\diamond(q)q^{-s},
\]

where `mathcal Q` is the generalized-prime-power alphabet and

\[
\lambda_\diamond(p^r)=\frac1r\quad(p\text{ odd}),
\qquad
\lambda_\diamond(2^r)=\frac{2+2^{-r}}r.
\]

Every coefficient is nonnegative. For `0<theta<=1`, define

\[
Q_\theta(s)=\cosh(\theta L_\diamond(s)),
\qquad
S_\theta(s)=\sinh(\theta L_\diamond(s)).
\]

Their Dirichlet coefficients are nonnegative, because the exponential of a Dirichlet series with nonnegative coefficients has nonnegative convolution coefficients and `cosh`/`sinh` retain the even/odd chaoses separately. Moreover

\[
G_\diamond(s)^\theta=Q_\theta(s)+S_\theta(s),
\qquad
B_\diamond(s)^\theta=Q_\theta(s)-S_\theta(s),
\]

and

\[
Q_\theta^2-S_\theta^2=1.
\]

At `theta=1/2`, putting `Q=Q_(1/2)`, `S=S_(1/2)`, one has the exact factorization

\[
\boxed{1-B_\diamond=2S(Q-S).}
\]

Thus the conclusion-producing reciprocal-Julia defect is a convolution of one positive odd-chaos source with one signed parity channel. No unsigned rough reservoir and no parity-blind terminal promotion is introduced.

The generalized-prime first chaos is

\[
P_\diamond(s)=\sum_{p\text{ odd}}p^{-s}+\frac52\,2^{-s}.
\]

The higher-chaos remainder

\[
R_\diamond(s)=L_\diamond(s)-P_\diamond(s)
\]

converges absolutely in `Re s>1/2`. Hence

\[
B_\diamond(s)^\theta
=\exp[-\theta P_\diamond(s)]\,
 \exp[-\theta R_\diamond(s)],
\]

where the second factor is holomorphic and zero-free in the full open critical half-plane. Every possible off-line singularity is therefore carried by the explicit first-chaos prime phase, not by the higher Euler chaos.
