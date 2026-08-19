# L-99260 — Exact Radon–Nikodym child thinning repairs the SHARP common-parent source

Claim ID: `L-99260`  
Status: **PROVED EXACT SYNTHESIS OF THE PR #647 REPAIR**  
Created: 2026-08-20  
Depends on: `L-99240`, PR #647 `L-99250`  
RH status: **not assumed**

For a fixed row `j`, let

\[
 dM_Y^{(j)}(t)
 =\mathbf1_{t\le Y}T(Y/t)\kappa_j(t)\frac{dt}{t},
 \qquad T(y)=4\sqrt y-3.
\]

If `1<=Z<=Y`, the child is not the raw cutoff of the parent measure. The exact
map is

\[
 \boxed{
 R_{Z\mid Y}(t)
 =\mathbf1_{t\le Z}\frac{T(Z/t)}{T(Y/t)},
 \qquad
 dM_Z^{(j)}=R_{Z\mid Y}\,dM_Y^{(j)}.
 }
 \tag{L-99260.1}
\]

Since `T` is increasing,

\[
 0\le R_{Z\mid Y}\le1.
\]

The raw-cutoff mutation is exact. At `Y=16`, `Z=4`, `t=4`,

\[
 T(Y/t)=T(4)=5,
 \qquad
 T(Z/t)=T(1)=1,
\]

so the child density is one fifth of the raw parent cutoff density.

The RN derivatives satisfy the cocycle

\[
 \boxed{
 R_{W\mid Y}=R_{W\mid Z}R_{Z\mid Y}
 \qquad(1\le W\le Z\le Y),
 }
 \tag{L-99260.2}
\]

almost everywhere on `M_Y^(j)`. Consequently every finite child history can
be realized by multiplying one parent source by a single product of RN factors.

After normalization by target mass, the measures are monotone:

\[
 \frac{M_{Y_1}^{(j)}}{T(Y_1)}
 \le
 \frac{M_{Y_2}^{(j)}}{T(Y_2)}
 \qquad(Y_1\le Y_2).
\tag{L-99260.3}
\]

Thus one compact Hall target flow lifts to a positive matched row-source
difference. Random-key widths

\[
 \alpha_iR_{Z_i\mid Y}(t)
\]

produce disjoint child cylinders because `sum alpha_i<1/8`; their complement is
the exact positive current marginal.

This closes the endpoint-child ownership vulnerability of PR #642. It does
not identify the positive causal parent decomposition with the signed Möbius
Euler row; `R-99260` is binding at that separate interface.
