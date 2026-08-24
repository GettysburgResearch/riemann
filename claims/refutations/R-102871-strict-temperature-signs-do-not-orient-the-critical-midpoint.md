# R-102871 — Strict-temperature signs do not orient the critical midpoint

Claim ID: `R-102871`  
Status: **PROVED PHASE-TRANSITION FIREWALL**  
Created: 2026-08-24  
Depends on: `L-102895--L-102897`  
RH status: **not assumed**

The unconditional signs

\[
\mathscr S_t(X)<0\quad(t<1/2),
\qquad
\mathscr S_t(X)>0\quad(t>1/2)
\]

hold with \(t\) fixed and \(X\) sufficiently large.  They do not determine the
sign at \(t=1/2\).

Indeed, for each large \(X\), the exact transition occurs at
\(\vartheta(X)\), not a priori at \(1/2\).  Both possibilities

\[
\vartheta(X)>1/2
\quad\text{and}\quad
\vartheta(X)<1/2
\]

are compatible with every fixed strict-temperature sign, because
\(\vartheta(X)-1/2\to0\).

A scalar model already shows the logical obstruction.  For arbitrary
\(b_X=o(1)\),

\[
F_X(t)=t-\frac12-b_X
\]

is negative at every fixed \(t<1/2\) and positive at every fixed \(t>1/2\) for
large \(X\), while

\[
F_X(1/2)=-b_X
\]

has either sign.

In the arithmetic family the displacement is exponentially localized, but
`L-102897` proves that its positive part is exactly the RH-bearing midpoint
negative mass.  Consequently none of the following is sufficient:

```text
eventual positivity of one strict half-source;
eventual signs on both fixed sides of t=1/2;
the existence of a transition zero converging to 1/2;
a finite scan of the temperature polynomial.
```

A valid closure must control the orientation or positive drift of the exact
critical-temperature zero.
