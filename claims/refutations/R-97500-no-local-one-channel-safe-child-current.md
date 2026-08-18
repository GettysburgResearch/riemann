# R-97500 — A safe-child contraction cannot have a universal local positive one-channel current

Claim ID: `R-97500`  
Status: **PROVED EXACT TWO-NODE SEPARATOR AND ALL-DEPTH NO-GO**  
Created: 2026-08-18  
Depends on: `L-97500`  
RH status: **unproved**

Take the two-node raw recursion

\[
 f_0+r f_1=0,
 \qquad f_1=1,
 \qquad 0\le t<r.
\]

The unique raw scalar is `f=(-r,1)`. The exact current for the contracted
recursion `f_0+t f_1=g_0` is

\[
 \boxed{g_0=t-r<0.} \tag{R-97500.1}
\]

Therefore no coefficientwise nonnegative one-channel current map can, for all
positive local data, replace a raw edge `r` by a smaller safe edge `t` while
preserving the exact parity-resummed scalar.

For factor 67 the raw edge is `r=p^(-1/2)`. The safe child used in the hazard
budget is `t=alpha=lambda r`, with `0<=lambda<1`; hence `t<r` whenever the edge
is active. The separator applies before any analytic estimate.

More strongly, (L-97500.6) shows that every finite-depth local replacement
misses a nonzero coefficient on a sufficiently long chain. The missing current
is necessarily global in rough-history depth unless the contracted and raw
operators coincide.

This refutes only a **source-local one-channel** contracted current. It does not
refute an arithmetic nonlocal Hall transport, a two-channel parity state, or the
Riemann Hypothesis.
