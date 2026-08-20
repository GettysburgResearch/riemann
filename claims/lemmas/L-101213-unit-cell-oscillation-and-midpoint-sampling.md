# L-101213 — The fixed detector has vanishing unit-cell oscillation

Claim ID: `L-101213`  
Status: **PROVED UNCONDITIONAL SAMPLING THEOREM**  
Created: 2026-08-21  
Depends on: `L-101210`

On the cell `(N,N+1)`,

\[
G'(X)=\frac{A_N}{2\sqrt X}+\frac{B_N}{X}.
\]

The seven bands are disjoint and contained in `[N/536,N]`. Since `|beta(n)|<=2`, `max|a_j|<=8`, and `max|b_j|<=3sqrt(2)`,

\[
|A_N|\le16(1+\log536),
\]

and, by the integral comparison for `sum n^(-1/2)`,

\[
|B_N|\le18\sqrt2\sqrt N.
\]

Hence there is an explicit absolute constant

\[
C_*=8(1+\log536)+18\sqrt2
\]

such that

\[
\boxed{
\sup_{X,Y\in[N,N+1]}|G(X)-G(Y)|\le\frac{C_*}{\sqrt N}.
}
\tag{L-101213.1}
\]

Let `x_N=N+1/2`. If the cell contains a point with `G< -tau`, then

\[
G(x_N)<-\tau+\frac{C_*}{\sqrt N}.
\tag{L-101213.2}
\]

In particular, on `I_L`, if `tau_L>=2C_*2^(-L/2)`, every `tau_L`-deep cell is detected by

\[
\boxed{G(N+1/2)<-\tau_L/2.}
\tag{L-101213.3}
\]

Thus no continuum root isolation is required: deep-cell incidence is exactly reduced, up to a vanishing threshold adjustment, to one discrete fixed-shell sample per endpoint cell.
