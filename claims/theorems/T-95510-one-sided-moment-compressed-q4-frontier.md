# T-95510 — One-sided, moment-compressed Q4 closure frontier

Claim ID: `T-95510`  
Status: **UNCONDITIONAL REDUCTION — PRODUCER OPEN**  
Created: 2026-08-18  
Frozen base: PR #580 at `812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05`  
RH status: **unproved**

The Q4 route can be sharpened in two independent ways.

1. Only an upper bound for the separated cross correlation is needed; its lower
   bound is automatic from `A^2>=0` and the polylogarithmic diagonal.
2. Subpower growth is enough.  The absolute polylogarithmic `SACF` theorem may
   be replaced by the one-sided condition

\[
 \mathcal S_{(\log2X)^B}(X)\le X^{o(1)}.
\]

3. On every exact band pair, the common-divisor kernel is a finite combination
   of fifteen squarefree power-log moments.  Those moments have the exact
   divisor expansion (L-95511.6).

Therefore the corrected conditional chain is

\[
 \boxed{
 \mathrm{UOSACF}
 \Longrightarrow
 \mathcal A(X)=X^{o(1)}
 \Longrightarrow
 \mathcal C_e(X)=X^{o(1)}
 \Longrightarrow
 \mathrm{RH}.
 }
\tag{T-95510.1}
\]

The packet does not prove `UOSACF`.  It removes the unnecessary lower-tail and
polylogarithmic burdens and exposes a finite moment-level target suitable for a
one-sided dispersion argument.

```text
safe annularization                         RETAINED
closed diagonal/near/large-gcd sectors      RETAINED
absolute polylog SACF                       OVERSTRONG FORMULATION
one-sided subpower UOSACF                   SUFFICIENT / OPEN
bandwise finite moment compression          PROVED EXACT
Riemann Hypothesis                          UNPROVEN
```
