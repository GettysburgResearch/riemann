# L-102735 — Every dyadic physical horizon reduces to four one-octave radial problems

Claim ID: `L-102735`  
Status: **PROVED EXACT SOURCE-LOCALIZATION THEOREM**  
Created: 2026-08-23  
Depends on: `L-102732--L-102734`  
RH status: **not assumed**

Fix a physical logarithmic horizon

\[
 Y\le X\le2Y.
\]

A centered filtered source atom at product `n` can contribute only if

\[
 1\le X/n\le8.
\]

Therefore every contributing source product lies in

\[
 \boxed{Y/8\le n\le2Y.}
 \tag{L-102735.1}
\]

Partition this interval into four exact source octaves:

\[
 [Y/8,Y/4),
 \quad
 [Y/4,Y/2),
 \quad
 [Y/2,Y),
 \quad
 [Y,2Y].
 \tag{L-102735.2}
\]

Let `v_j=(A_j,B_j,C_j)` be the carrier-subtracted filtered disk triple from the
`j`-th source octave.  The complete triple is

\[
 v=\sum_{j=0}^3v_j.
\]

By the subadditivity of `L-102733`,

\[
 \boxed{
 \mathfrak R(v)
 \le
 \sum_{j=0}^3\mathfrak R(v_j).
 }
 \tag{L-102735.3}
\]

Thus no separate cross-octave S-lemma reserve or physical occupancy estimate is
needed: the four source pieces are recombined through the same sublinear gauge.

Each `v_j` is a one-octave source packet and therefore enjoys the strict
contraction constant

\[
 \kappa_8<0.689
\]

from `L-102734`.

Define

```text
ORSC102735:
  uniformly for each of the four source octaves on every dyadic physical
  horizon, the integrated centered radial cost is Y^o(1).
```

Then

\[
 \boxed{
 \mathrm{ORSC}_{102735}
 \Longrightarrow
 \mathrm{RSC}_{102760}.
 }
 \tag{L-102735.4}
\]

The global filter/occupancy problem has therefore been reduced to one literal
source octave at a time.  The remaining arithmetic difficulty is internal to a
single octave; it is not interaction among infinitely many scale blocks.