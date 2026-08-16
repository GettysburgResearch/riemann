# L-94021 — The outer fibre has an exact positive two-channel realization

Claim ID: `L-94021`
Status: **PROVED DIRECTED FINITE-WINDOW THEOREM**
Created: 2026-08-16
Depends on: `L-91107`, `L-91760/L-91761`; two-channel identity of `L-94020`
Replay: `X-94020-live-endpoint-source`
RH status: **unproved**

For `1<=x<67`, no rough prime can occur in the endpoint fibre.  Define the
signed equality and reserve residuals

\[
 L_E(x)=\sum_{k\le x}
 \frac{\mu(k)}{
  \sqrt k
 }
 (2\sqrt{x/k}-1),
\]

\[
 L_R(x)=\sum_{k\le x}
 \frac{
  \mu(k)
 }{\sqrt k}
 (\sqrt{x/k}-1).
\tag{L-94021.1}
\]

On each cell `N<=x<N+1`, both are affine in `sqrt(x)`.  Their minima are
therefore attained at the appropriate one-sided cell endpoint.  Exact rational
square-root enclosures over all 66 cells give

\[
 \boxed{L_E(x)>0.318,}
\tag{L-94021.2}
\]

and

\[
 \boxed{L_R(x)\ge0,}
\tag{L-94021.3}
\]

with equality in (L-94021.3) only at the initial endpoint `x=1`.

At fixed endpoint parameter `s`, all Möbius colours multiply one common
Volterra feature row.  Couple positive and negative colours separately in the
`E` and `R` channels by the complete rank-one transport.  The residual masses
are exactly `L_E(x)` and `L_R(x)`, so the resulting outer fibre is positive.
The exact identities

\[
 T=E+2R,
 \qquad
 S=2E+R
\]

show that the same occurrence coefficient carries target and score, while the
`E` channel alone carries the component row and all ordinary observations.

Thus the full endpoint region `1<=X/s<67` has a concrete positive source and
physical realization.  No causal difference of two Volterra fibres, rough
lift, exported child, or auxiliary port is used.
