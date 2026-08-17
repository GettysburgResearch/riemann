# R-96500 — The frozen Target–Lorenz certificate does not by itself prove positivity of every component row

Claim ID: `R-96500`  
Status: **EXACT SCOPE CORRECTION; TWO-ROW CERTIFIED RANGE RETAINED**  
Created: 2026-08-17  
Frozen parent: PR #550 at `20646a78c3e8843001cb49ea0c9741f6d0d446f7`  
RH status: **unproved**

## 1. Certified row range

The compact and MPFR-directed Target–Lorenz theorem imported by PR #550 proves
the terminal leaf inequalities in the declared range

\[
 2\le j\le66.
\]

That range is more than sufficient for the two conclusion-producing rows
`j=2,3`.

## 2. Why the all-row sentence is not automatic

A terminal causal leaf has parent/child form

\[
 Q_{py/d}-p^{-1/2}Q_{y/d},
 \qquad p\ge67,
 \qquad 1\le y<67,
 \qquad d\mid P_{61}.
\]

Although the child term vanishes above row `66`, the parent term
`Q_(py/d)` can have support far above row `66`.  Therefore the statement

```text
rows above 66 are absent from a terminal P61 leaf
```

is not a consequence of triangular support.  An all-row theorem would require
an additional frontier argument in those parent rows.

This packet does not supply or use such an argument.

## 3. Corrected scope

The projective source identity is consumed only through

\[
 \operatorname{Obs}_2,
 \qquad
 \operatorname{Obs}_3,
\]

and through their positive scalar combination

\[
 5\operatorname{Obs}_2+3\operatorname{Obs}_3.
\]

Every one of these coordinates lies inside the exact certified terminal range.
Consequently this correction retracts the unnecessary full-row overreach while
leaving the proposed two-row route intact.

```text
terminal rows 2 and 3                      CERTIFIED RANGE
terminal rows 4 through 66                 CERTIFIED RANGE / NOT NEEDED
terminal parent rows above 66              NOT ESTABLISHED HERE
full-row positivity claim in PR #550       SUPERSEDED BY TWO-ROW SCOPE
two-row projective route                   LIVE
Riemann Hypothesis                         UNPROVED
```
