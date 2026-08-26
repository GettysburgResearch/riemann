# T-106090 — Superseded Q-fixed least-discrepancy rough-tail frontier

Claim ID: `T-106090`  
Programme aliases: `LFAM1.LEAST_DISCREPANCY_REPAIR`, `LFAM2.ROUGH_TAIL_FAMILY_FRONTIER`, `STRESS.BOOLEAN_CORE_TRIANGULAR_MOMENT`  
Status: **SUPERSEDED BY `R-106110` AND `T-106110`; RETAINED AS THE ONE-SIDED CONSTRUCTION RECORD**  
Created: 2026-08-25  
Corrected: 2026-08-25  
Depends on: `L-106090--L-106093`; binding corrections `R-106090`, `R-106110`; replacement `T-106110`  
Programme issues: #743, #736, #737  
RH status: **unproved**

## Retained mathematics

This packet established the following exact and useful reductions:

```text
least-discrepancy orientation of every coprime two-sided Boolean pair;
strict roughness of the opposite reduced core;
nonzero Ramanujan phase at the least discrepancy prime;
fixed-Q even-character rough-tail family;
fixed-Q automatic long-core estimate;
left-anchor amplification before the family square.
```

Those statements remain valid and are inherited by `T-106110`.

## Binding correction

The first controlling moment froze the opposite semiprime owner product `Q`
and used external source-dual weight

\[
 g^2\ell Q.
\]

`R-106110` proves that the factor `Q` cancels the literal reciprocal owner
energy `1/Q`.  Hence a fixed-fibre bound leaves the number of admissible
opposite-owner fibres.  The former claim that the complete same-anchor
diagonal was subpower is withdrawn.

The physical source contains

\[
 \sum_Q z_Q
\]

before squaring.  The correct family amplitude must therefore contain the
complete `Q` sum before one Gauss square is taken.

## Correct replacement

`T-106110` defines

\[
 \mathcal Z_{g,\ell,\sigma,h}(t)
 =\sum_{\alpha,Q}
 \overline{A_\alpha(t)}B_{\alpha,Q,\sigma,h}(t)
\]

and the dual-amplified source moment with external weight

\[
 g^2\ell.
\]

It proves the exact conditional chain

\[
 \mathrm{DAPRO}_{106110}\wedge\mathrm{DAKUM}_{106110}
 \Longrightarrow
 \mathrm{BCI}_{102990}
 \Longrightarrow
 \mathrm{RH}.
\]

Both first premises remain open.

## Binding status

```text
least-discrepancy incidence and rough-tail geometry     RETAINED
fixed-Q local family                                    RETAINED
left-anchor amplification                               RETAINED
Q-fixed complete diagonal                               WITHDRAWN
LDRPCX/LDRNEX distinct-anchor-only frontier             SUPERSEDED
R-106110 opposite-owner fibre firewall                  BINDING
T-106110 dual-amplified frontier                        LIVE / OPEN
Riemann Hypothesis                                      UNPROVEN
```
