# R-93292 — Positive covariance spectrum does not imply the pointwise `SCID_PL` inequality

Claim ID: `R-93292`  
Status: **EXACT REFUTATION / QUANTIFIER FIREWALL**  
Created: 2026-08-18  
Depends on: `L-93293`

A positive spectral representation controls autocorrelations, not the sign of a
single carrier sample. The one-atom positive measure

\[
 d\sigma=\delta_\lambda
\tag{R-93292.1}
\]

has positive-definite autocorrelation

\[
 \mathscr A(u)=e^{i\lambda u},
\tag{R-93292.2}
\]

and is realized by

\[
 C(t)=e^{i\lambda t}.
\tag{R-93292.3}
\]

Nevertheless

\[
 \Re C(t)=\cos(\lambda t)
\tag{R-93292.4}
\]

takes both signs and attains its maximum at isolated prescribed phases.
Arbitrarily many positive atoms give the same obstruction with high coherent
spikes.

Therefore

\[
\boxed{
 \text{positive spectral measure}
 +\text{finite mean square}
 \not\Longrightarrow
 c_q\Re\mathfrak C_{q,m}(t)\le\mathcal R_m(q,t)
 \text{ pointwise}.
}
\tag{R-93292.5}

`L-93293` is a genuine carrier-average theorem, but `SCID_PL` still requires
carrier-specific signed arithmetic or a new local consumer. Neither PSD nor
block cardinality crosses that quantifier.
