# R-97400 — The `1/40` lower bias asserted in PR #565 is false

Claim ID: `R-97400`  
Status: **EXACT DIRECTED REFUTATION OF THE CONSTANT; POSITIVITY IS NOT REFUTED**  
Created: 2026-08-18  
Frozen target: PR #565 at `339e3367660f40c74795802a6f8170b15e19b13a`  
RH status: **unproved**

Let
\[
P=P_{61}=\prod_{p\le61}p,
\]
\[
H_x(n)=\min\!\left(\log4,\log\frac xn\right)_+,
\]
and let the positive `5:3` unsieved dictionary be
\[
q_*(2)=15,\qquad q_*(3)=6,\qquad q_*(4)=3,
\qquad q_*(m)=6\quad(m\ge5).
\]
Put
\[
A_*(x)=\sum_{m\ge2}\frac{q_*(m)}{\sqrt m}H_x(m),
\]
\[
F(x)=\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}A_*(x/d),
\qquad
M(x)=\sum_{d\mid P}\frac1{\sqrt d}A_*(x/d).
\]
PR #565 asserts
\[
F(x)\ge\frac1{40}M(x)\qquad(x\ge67).
\tag{R-97400.1}
\]

The 256-bit directed replay `X-97400` evaluates the exact integer endpoint
`x=184` and proves
\[
\boxed{
-18.114417591649673
<40F(184)-M(184)
<-18.114417591649601<0.
}
\tag{R-97400.2}
\]
Therefore (R-97400.1) is false.

The same proof object gives
\[
3.272741705897984
<42F(184)-M(184)
<3.272741705898060,
\]
so the failure is sharply between the constants `1/40` and `1/42`.  It does
not refute `F(x)>0`, the upper estimate `F(x)<=M(x)/8`, or the repaired lower
estimate proved in `L-97400`.
