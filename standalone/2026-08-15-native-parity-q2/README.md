# Native parity / `q=2` factor-67 review front door

Base: PR #500 at `d73c1e7a1a482cac31581211a84db43cc34c824e`.  
Frozen comparison: PR #496 at `96f8a6b3cc3d474217633e16d4caa490a0aae518`.  
Proposal: `T-92920`.  
Status: candidate-complete on frozen inputs; RH remains unproved.

## Review order

1. `R-92920` — exact conditional `q=2` separator and withdrawal.
2. `L-92920` — paired native/rough bifurcation.
3. `L-92921` — oriented physical coupling.
4. `L-92922` — all-column feasibility and `q=2` mutation test.
5. `L-92923` — native cost below `60989`.
6. `T-92920` — endpoint composition.
7. `X-92920`, manifests and lock.

The decisive question is whether the rough-prime swap survives until actual
physical child placement.  An uncoloured output row is not enough.
