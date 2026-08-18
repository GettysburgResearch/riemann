# L-98070 — Integer Euler discrepancy is a strict Hausdorff moment sequence

Claim ID: `L-98070`  
Status: **PROVED EXACT ANALYTIC THEOREM**  
RH status: **not assumed**

Define
\[
e_N=2\sum_{m\le N}m^{-1/2}-4\sqrt N+3,\qquad
e_\infty=3+2\zeta(1/2)>0.
\]

Direct algebra gives
\[
e_N-e_{N+1}
=
\frac{2}{\sqrt{N+1}(\sqrt{N+1}+\sqrt N)^2}>0.
\]

Using
\[
n^{-1/2}=\frac1{\sqrt\pi}\int_0^\infty e^{-nt}t^{-1/2}dt
\]
and summing the geometric tail yields
\[
e_N=e_\infty+\frac2{\sqrt\pi}\int_0^\infty
e^{-Nt}\frac{1-(1+t)e^{-t}}{(1-e^{-t})t^{3/2}}dt.
\]
The density is strictly positive because `e^t>1+t`.

With `x=e^{-t}` this is
\[
e_N=e_\infty+\int_0^1x^N\,d\nu(x),\qquad d\nu\ge0.
\]
Thus `(e_N)` is a strict Hausdorff moment sequence. In particular every
alternating finite difference has the Hausdorff sign and every Hankel and
`[0,1]` localizing matrix is positive semidefinite.
