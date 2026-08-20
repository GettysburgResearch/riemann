# R-101212 — Splitting `B_N log X+C_N` into two global coordinates destroys an exact carrier cancellation

Claim ID: `R-101212`  
Status: **PROVED INTERFACE FIREWALL**  
Created: 2026-08-21  
Audits: `L-101212`

The identity

\[
G(X)=A_N\sqrt X+B_N\log X+C_N
\]

is exact. However, the last two terms arise sourcewise as

\[
\sum_n\frac{\beta(n)}{\sqrt n}
[b_j\log(X/n)+c_j],
\]

where `log(X/n)` is bounded by `log536` on the physical shell. Estimating
`B_N log X` and `C_N` separately introduces two potentially large global
`log X` carriers which cancel term by term in the physical observation.

Therefore the three separate deviation estimates in `T-101210` are a valid
sufficient condition but are not the preferred closure interface. The
carrier-preserving replacement is the midpoint sample of `L-101213`, or the
centered coordinate

\[
D_N=B_N\log(N+1/2)+C_N,
\]

with only the vanishing within-cell term
`B_N log(X/(N+1/2))` left over.
