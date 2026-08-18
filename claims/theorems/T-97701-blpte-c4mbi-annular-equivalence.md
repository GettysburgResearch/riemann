# T-97701 - Root BLPTE67, C4MBI67 and annular scalar positivity are identical

Claim ID: `T-97701`  
Status: **PROVED EXACT EQUIVALENCE; SIGN OPEN**  
Created: 2026-08-18  
Depends on: `L-97700`, `L-97701`, `L-97702`, `L-97703`  
RH status: **unproved**

At the root endpoint, write `BLPTE67(X)` for the exact inequality from
`L-97701`

\[
\mathfrak T_Z(X)\le U_Z(X)-\mathfrak I_Z(X).
\tag{T-97701.1}
\]

The largest-prime Bellman identity is

\[
U_{\rm full}(X)=U_Z(X)-\mathfrak I_Z(X)-\mathfrak T_Z(X).
\tag{T-97701.2}
\]

By construction of the normalized root scalar,

\[
U_{\rm full}(X)=\frac{\mathcal A_X}{\sqrt X}.
\tag{T-97701.3}
\]

Therefore, pointwise in every root endpoint `X>0`,

\[
\boxed{
\mathrm{BLPTE67}(X)
\iff U_{\rm full}(X)\ge0
\iff \mathcal A_X\ge0
\iff \mathrm{C4MBI67}(X).
}
\tag{T-97701.4}
\]

This has two consequences.

1. `BLPTE67` is not a source-blind auxiliary estimate weaker than the producer;
   at root scope it is exactly the producer sign in Bellman coordinates.
2. The exact remaining arithmetic statement can be written either as the
   four-band Mertens inequality of `L-97702` or the prime-Möbius owner inequality
   of `L-97703`.

The existing Mellin-Landau consumer proves

\[
\left[\mathcal A_X\ge0\text{ eventually}\right]
\Longrightarrow \mathrm{RH}.
\]

Hence a proof of `C4MBI67` would finish this lane.  No proof of that sign is
contained in T-97701, and RH remains unproved.

## Exact boundary

```text
BLPTE67(X) <=> U_full(X)>=0                PROVED EXACT AT ROOT
U_full(X)=A_X/sqrt(X)                      PROVED EXACT
A_X>=0 <=> C4MBI67(X)                      PROVED EXACT
prime-Mobius owner decomposition           PROVED EXACT
source-blind unsigned Type-II closure      REFUTED AS A MECHANISM
C4MBI67 sign                               OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVED
```
