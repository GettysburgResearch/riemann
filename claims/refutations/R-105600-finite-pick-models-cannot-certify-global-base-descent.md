# R-105600 — Finite Pick models cannot certify global downward-base descent

Claim ID: `R-105600`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-24  
Depends on: `L-105601`  
RH status: **not assumed**

Let

\[
f(z)=\alpha z+\beta+
\sum_{j=1}^Nw_j
\left({1\over t_j-z}-{t_j\over1+t_j^2}\right),
\qquad
\alpha\ge0,\quad w_j>0,\quad t_j\in\mathbb R,
\]

be a nonconstant rational Pick function. Fix a downward displacement
`delta>0` and a physical scale `h>delta`. Put `y=h-delta` and

\[
\mathcal C_h^{[\delta]}(a)
={1\over2}
\left[h\Re f'(a+iy)-\Im f(a+iy)\right].
\]

The exact kernel of `L-105601` gives

\[
\mathcal C_h^{[\delta]}(a)
={\alpha\delta\over2}
+{1\over2}\sum_jw_j
{\delta(a-t_j)^2-(2h-\delta)y^2
 \over((a-t_j)^2+y^2)^2}.
\]

If `alpha>0`, the first term is already a fixed positive obstruction at
spatial infinity. If `alpha=0`, let `M=sum_jw_j>0`. Expanding at infinity,

\[
\boxed{
\mathcal C_h^{[\delta]}(a)
={\delta M\over2a^2}+O(|a|^{-3})>0
}
\]

for all sufficiently large `|a|`.

Thus no finite atomic Herglotz measure, rational Pick function, or fixed-degree
real-rooted polynomial model can satisfy the globally nonpositive lower-base
microscope after any nonzero downward shift.

The obstruction does **not** refute the Xi programme. Xi has an infinite,
translation-dense critical/source measure whose remote mass may interact with
the long positive tail of the signed descent kernel. It proves that any
successful descent theorem must use that infinite arithmetic structure. A
finite fixture, finite truncation with uncontrolled tail, or compactly
supported model cannot be promoted to the global spatial-escape statement.

```text
finite polynomial/rational model -> global base descent    REFUTED
infinite Xi reciprocal-source descent                       OPEN
Riemann Hypothesis                                          UNPROVEN
```
