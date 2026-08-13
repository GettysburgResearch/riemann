# R-91650 — PR #431 scope corrections remain binding

Claim ID: `R-91650`  
Status: **EXACT MATHEMATICAL REFUTATION**  
Created: 2026-08-13  
RH status: **unproved**

## Causal support

The atom

\[
K_a(d;p,y)=d^{-1/2}[a\sqrt{py/d}-3]\mathbf1_{d\le py}
-p^{-1/2}d^{-1/2}[a\sqrt{y/d}-3]\mathbf1_{d\le y}
\]

must retain both support indicators. At `(t,p,y)=(79,83,1)`, the positive
squarefree integers `85,86,87` satisfy `e<=t+8` but `e>py`; their true
contributions vanish. Hence the historical untruncated prefix identity is false.

## Hidden branch

For `r=p^{-1/2}`, the pure reserve hidden branch has target and score `(2r,r^2)`,
while an `r`-scaled canonical child has `(2r,r)`. Since `r-r^2>0`, the branch is
not that child plus a positive score-superordinate remainder.

## Signed packet loss

A source restriction of mass fraction `theta` need not have deficit at most
`theta` times the parent deficit. The recursion must use the actual child packet
deficit.

## Current rows

A vanishing inherited child row does not prove positivity or bounded debt for
the remaining current row.

These statements refute historical `T-91304`, not the Riemann Hypothesis.