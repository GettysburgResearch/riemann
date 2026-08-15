# Review handoff — complete Target-Lorenz native-root successor

## Freeze

```text
repository:            gfreund123/riemann
origin PR:             #468
origin branch:         research/gpt56-pro/91381-euler-shell-recovery
origin head:           9e2ae6d26a7920055e1f11327dc0ddeb7b855c61
successor branch:      research/gpt56-pro/93600-target-lorenz-complete-successor
normative content:     9421eb45bcd10f0b7cdf4881a7adddbc295c8b64
main at cutoff:        9c7538559d7f56c2914b39aed5a1fb3fbf7ce131
UTC cutoff:            2026-08-15T14:20:57Z
```

## What this successor claims

The packet proposes a complete independent Target-Lorenz route:

```text
compact determinant py<166000          frozen directed exact
analytic/event tail py>=166000          new proposed complete certificate
complete all-parameter AVLT             proposed complete
concrete positive common parent         explicit formula
all-column native feasibility           proposed complete
native Y4 deficit                       <61000
endpoint-to-RH composition              frozen conditional
RH                                      unproved pending review
```

It does not wrap the root-Hall producers of PR #488/#489/#493/#494.

## Load-bearing order

```text
L-93600
L-93601 + X-93600
L-93602
R-93600
L-93603
L-93604
L-93605 + X-93601
T-93600
T-93601
```

Then reconstruct the frozen inputs in the exact order listed in
`t93601-target-lorenz-complete-successor-lock.json`.

## Decisive repairs from reviews #490--#492

1. Formula `L-93603.5` supplies an actual common parent from explicit positive
   endpoint and leaf measures.
2. Actual child responses remain internal colours; full child capacities are
   never promoted into the source identity.
3. Mismatch, collar and terminal vectors are a separate signed observation
   ledger.
4. Native slack is defined only after every physical column is feasible.
5. The recursive family and root-global port are both empty/zero.
6. The endpoint currency is `J_Lambda-H=<Y4,r>`, never the continuum benchmark
   bridge.

## Fresh replay

```bash
cd experiments/X-93600-target-lorenz-tail
python3 verify.py --output /tmp/x93600.json
cmp /tmp/x93600.json results/verification.json
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS

cd ../X-93601-target-lorenz-native-endpoint
python3 verify.py --output /tmp/x93601.json
cmp /tmp/x93601.json results/verification.json
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

## First falsifiers

```text
negative or unresolved tail cell;
incorrect compact/tail boundary;
rounding uncertainty exceeding the 0.78 reserve;
non-explicit leaf coefficient or duplicate owner;
different coefficients across physical coordinates;
signed error inserted into positive source;
full child capacity used instead of actual response;
omitted q<K column;
nonzero root port or exported recursion;
native cost >=61000;
wrong one-sided endpoint orientation.
```

A failure is a rejection of this proposal at the frozen SHA. Later work does
not retroactively repair it.
