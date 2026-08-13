# L-91662 — One-sided endpoint upper bounds are sufficient

Claim ID: `L-91662`
Status: **PROVED EXACT CONCLUSION LEMMA**
Created: 2026-08-13
Depends on: `L-91660`, `T-90011`

The endpoint bridge gives

\[
F_\Lambda(X)\le\Delta_X(\mathcal N_X).
\]

If the packet construction proves

\[
\Delta_X(\mathcal N_X)\le K,
\]

then

\[
\limsup_{X\to\infty}
\frac{F_\Lambda(X)}{\log^2X}\le0.
\]

The threshold form of `T-90011` requires only

\[
\limsup_{X\to\infty}
\frac{F_\Lambda(X)}{\log^2X}
<\frac{-1-\zeta(1/2)}4.
\]

The right side is strictly positive.  Hence a uniform upper bound for the native
packet deficit already satisfies the threshold.  No lower bound for
`F_Lambda` and no two-sided `O(1)` assertion are used.
