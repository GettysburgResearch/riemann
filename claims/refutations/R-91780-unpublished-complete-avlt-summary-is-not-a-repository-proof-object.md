# R-91780 — The unpublished complete-AVLT summary is not a repository proof object

Claim ID: `R-91780`  
Status: **EXACT PUBLICATION/FREEZE CORRECTION**  
Created: 2026-08-15  
Frozen reviewed head: `8085903e190589e3117a0c7494fb1150c2222401`  
RH status: **unproved**

## 1. Correction

A prior external summary described theorem objects named `L-91696`, `T-91696`,
and `T-91697`, together with a compact determinant proof through `py<166000`,
an analytic tail, a source-Fubini native ledger, and a final endpoint
composition. Those theorem objects were not reachable from the declared PR
#468 branch at the reviewed head.

The durable packet at that head consists of

```text
L-91720  common-source vector primal/dual;
L-91721  support-easy row reduction;
L-91722  determinant lower-bound reduction;
T-91720  conditional proposal with AVLT and ANRL still open.
```

Therefore the earlier summary is withdrawn as a description of repository
state. It may not be cited as a proof, lock, replay, or branch publication.

## 2. Scope

This is a publication correction, not a mathematical counterexample to a
future compact or tail theorem. Any such theorem must be deposited under a
reachable commit, with its checker, retained result, hashes, dependency lock,
and exact proof boundary.

## 3. Controlling rule

```text
summary without reachable theorem blob       NOT A PROOF OBJECT
local or transient computation                NOT A REMOTE FREEZE
reachable claim + replay + lock               REVIEWABLE
Riemann Hypothesis                            UNPROVEN
```
