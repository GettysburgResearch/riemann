# T-91740 — Corrected Target-Lorenz native-root proposal after compact AVLT closure

Claim ID: `T-91740`  
Status: **PROVED CONDITIONAL COMPOSITION / TWO EXPLICIT GATES**  
Created: 2026-08-15  
New inputs: `L-91780--L-91784`  
Retained inputs: `L-91720`, `L-91362`, `L-91375`, `L-91377--L-91380`, `T-91313--T-91314`  
RH status: **unproved**

`L-91781` closes every stopped-leaf row margin with `py<166000`. The remaining
leafwise arithmetic theorem is

\[
 \Theta_j(p,y)\ge0
 \qquad(py\ge166000,\ 2\le j\le66).
\tag{T-91740.1}
\]

Call this theorem `Tail-AVLT`. `L-91782` supplies its leading parity reserve,
but does not prove (T-91740.1).

The second gate is the live source-owned native allocation (`ANRL`): one finite
source/channel coefficient table must place current, recursive child, stop,
collar, mismatch, omission, taper, shared port and unused slack inside the
native ordinary/detail capacities. `L-91783` proves that once those local
identities use one common coefficient vector, their root sum is exact and
nonduplicating.

Under `Tail-AVLT + ANRL`, every leaf has the common Target-Lorenz row bonus, all
ordinary/detail identities use one source ledger, and the recursive child mass
is below `1/8`. `L-91784` then gives native weighted slack

\[
 \mathcal D(X)=O(\log X)=o(\log^2X).
\]

The retained one-sided endpoint consumer would then provide the proposed RH
implication. This last sentence is conditional: neither live gate nor RH is
promoted here.

```text
compact AVLT py<166000                    PROVED
Tail-AVLT py>=166000                      OPEN
formal source-Fubini                      PROVED
live ANRL allocation                      OPEN
native slack recurrence                   PROVED CONDITIONAL
full endpoint implication                 CONDITIONAL
Riemann Hypothesis                        UNPROVEN
```
