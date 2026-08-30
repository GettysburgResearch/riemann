# PFR-T9 — complex Gamma filters give finite-horizon soft localization

Claim ID: `PFR-T9`  
Status: **PROVED EXACT SOURCE FORMULA AND LEAKAGE BOUND**  
Depends on: `PFR-T4`, `PFR-T5`, `PFR-R2`, `PFR-R3`  
RH status: **unproved**

For `q=a+iT`, `a>1/2`, integer `m>=2`, define

\[
R_{q,m}(t)=\sum_\rho
\frac{e^{(\rho-1/2)t}}
{(q-(\rho-1/2))^m}.
\]

It has an absolutely convergent source formula over prime powers and the
archimedean modes, displayed in `CONTINUATION_108320.md`.

For target half-width `w`, guard width `W`, put

\[
D_{in}^2=(a+1/2)^2+w^2,
\qquad
D_{out}^2=(a-1/2)^2+W^2.
\]

If `D_out>D_in`, the normalized multiplier

\[
H(\lambda)=\left(\frac{D_{in}}{a+iT-\lambda}\right)^m
\]

has magnitude at least one on `|Im(lambda)-T|<=w` and at most
`(D_in/D_out)^m` on `|Im(lambda)-T|>=W`.

If `C_out` is the total absolute exterior coefficient mass, then on every
finite horizon `[0,L]`,

\[
\|e^{-\sigma t}R_{out}\|_{L^2(0,L)}
\le C_{out}\Phi(1/2-\sigma,L),
\]

with `Phi(x,L)^2=int_0^L exp(2xt)dt`.  This is a leakage certificate, not a
local zero theorem; an in-band lower frame bound remains open.
