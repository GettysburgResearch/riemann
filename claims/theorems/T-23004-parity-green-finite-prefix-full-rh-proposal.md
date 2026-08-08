# T-23004 — Superseded polylogarithmic parity–Green proposal

Claim ID: `T-23004`  
Title: Historical finite-prefix parity–Green proposal  
Status: **SUPERSEDED / LOAD-BEARING CONDITION REFUTED BY `R-23008`**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-08  
Frozen historical version: commit `a0d5a627bd2d4e799eddf7c795df77083a3618ff`  
Replacement: `T-23005-critical-order-factor-five-transition-rh-proposal.md`

## 1. Historical proposal

The frozen version proposed a finite-prefix inequality with condition number

\[
K_R\le C(\log R)^A
\]

and only a constant additive defect. Combined with the digital Sobolev tail, it
would have yielded a strict lower-scale recurrence and RH.

## 2. Exact disposition

`R-23008` proves that the prefix symbol at a zeta zero `rho=beta+i gamma`
satisfies

\[
|A_R(\rho)|\ll_\rho (1+\log R)R^{-\beta}.
\]

At a critical-line zero this forces inverse scale at least

\[
R/(\log R)^{O(1)},
\]

unless the mode is placed in an explicit tempered defect channel. Therefore the
polylogarithmic conditioning in the frozen `PGC(R)` is incompatible with the
known critical-line spectrum.

The following components of the frozen proposal remain valid at their declared
scopes:

```text
all-ratio shell transfer;
positive digital comb identities;
parity/carry compact dipole;
exact dyadic Green path block;
digital recurrence;
H1-to-L2 tail bound.
```

The load-bearing `PGC(R)` and the deduction using its polylogarithmic rate are
not available.

## 3. Correct replacement

`T-23005` uses the sharp critical threshold

\[
K_R=R^{1+o(1)}
\]

and an explicit tempered channel. It combines the independent-frequency block,
parity-paired finite reconstruction, and factor-five carry Schur reserve. Its
sole open theorem is the production physical-to-carry source transference
`CF5TC(R)`.

## 4. Status boundary

```text
T-23004 historical algebraic front end   RETAINED
polylogarithmic PGC(R)                    REFUTED
T-23004 as an RH proof                    WITHDRAWN
T-23005 critical-order replacement        ACTIVE CONDITIONAL PROPOSAL
Riemann Hypothesis                        UNPROVED
```
