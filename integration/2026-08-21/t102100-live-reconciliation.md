# T102100 live reconciliation

Two parallel results landed after the first T102100 commit.

1. PR #701 proves the stronger pointwise cubic interval range `A<e`.  It
   supersedes T102100's `A<e^(16/17)` as the current widest interval theorem;
   the exact `17/16` Harnack certificate remains independent valid mathematics.
2. PR #702 reduces the one-field Vaughan energy to `HCNC103100`, a signed
   shrinking-window near-collision estimate.  `L-102106/T-102110` prove that
   this estimate controls both carrier-free PR #697 channels simultaneously.

Current implication:

```text
HCNC103100 -> CFBB102100 -> RH.
```

`HCNC103100`, `CFBB102100`, and RH remain unproved.
