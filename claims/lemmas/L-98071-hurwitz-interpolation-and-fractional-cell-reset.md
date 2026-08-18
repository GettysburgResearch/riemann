# L-98071 — Hurwitz interpolation isolates the fractional-cell reset

Claim ID: `L-98071`  
Status: **PROVED EXACT IDENTITY**  
RH status: **not assumed**

Define
\[
\mathscr E(y)=3+2\zeta(1/2)-2\zeta(1/2,y+1)-4\sqrt y.
\]
At every integer `N`, `mathscr E(N)=e_N` from `L-98070`.

If `N=floor(y)`, the actual activation sawtooth
\[
E(y)=2\sum_{m\le y}m^{-1/2}-4\sqrt y+3
\]
satisfies
\[
D(y):=\mathscr E(y)-E(y)
=
2\left[\zeta(1/2,N+1)-\zeta(1/2,y+1)\right]
=
\int_N^y\zeta(3/2,u+1)\,du.
\]
Therefore
\[
D(N)=0,\qquad 0<D(y)<2/\sqrt{N+1}\quad(N<y<N+1).
\]

The target root is therefore the smooth interpolation minus one explicit
positive fractional-cell reset, `E(y)=mathscr E(y)-D(y)`. This is a structural
decomposition, not a sign proof for the Möbius projection.
