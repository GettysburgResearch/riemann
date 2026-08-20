# R-100600 — Positive mixing of the shifted-square homotopy cannot remove both defects

Claim ID: `R-100600`
Status: **PROVED EXACT METHOD FIREWALL**
RH status: **unproved**

For the exact homotopy of PR #688/L-100400,

\[
\mathcal E_2(X)
=X(1+c)^2 A_c(X)+(3-c)X I_c(X)+P_c(X),
\qquad -1\le c\le0,
\]
where the atomic coefficient `(1+c)^2` is nonnegative and vanishes only at `c=-1`, while the pre-activation collar `P_c` vanishes identically only at `c=0` (`lambda_0=1`).

Let `dnu(c)` be any nonzero positive measure on `[-1,0]`. If the averaged atomic contribution vanishes for every source, then

\[
\int_{-1}^0(1+c)^2d\nu(c)=0,
\]
forcing `nu` to be supported at `c=-1`. But at `c=-1`, `lambda_c=16/9>1`, so the collar is generally nonzero (and is explicitly negative on retained finite fixtures in PR #688).

Conversely, making the collar vanish identically by positive mixing forces support at `c=0`, where the atomic coefficient is one.

Therefore no positive convex mixture of the exact shifted-square identities can simultaneously eliminate the atom and collar while preserving positivity. Any successful use of the homotopy must estimate at least one of the two defects or introduce a genuinely signed cancellation with an independent positivity mechanism.
