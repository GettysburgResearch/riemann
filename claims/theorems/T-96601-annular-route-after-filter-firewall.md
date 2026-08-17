# T-96601 — The annular route now requires arithmetic quadrature, not a one-sign shift filter

Claim ID: `T-96601`  
Status: **CORRECTED CONDITIONAL FRONTIER**  
Created: 2026-08-17  
RH status: **unproved**

PR #551 proves that the factor-four discrepancy

\[
\mathfrak A_2(X)=F_\Lambda(X)-2F_\Lambda(X/2)+F_\Lambda(X/4)
\]

is supported on `[X/4,X]` and has the zero-safe multiplier `(1-2^{-s})^2`.
`R-96600` proves that no finite zero-safe shift filter can make the underlying positive-source Green kernel nonzero and one-signed.

Therefore the honest producer remains the arithmetic estimate

\[
\boxed{\mathfrak A_2(X)=O(\log^B(2X))}
\tag{T-96601.1}
\]

for some fixed `B`, or an equivalent nonlinear/matrix domination of the atomic prime-power quadrature by its deterministic cell density. The compact annulus and pole survival are retained; the source-blind one-sign shortcut is closed.
