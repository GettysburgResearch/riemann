# Review handoff — directed hardening of PR #497

## Freeze

```text
repository:       gfreund123/riemann
controlling PR:   #497
base branch:      research/gpt56-pro/93600-target-lorenz-complete-successor
base head:        bd2a3c32ab50d8a8cec39c4b51ccd63349b23a74
origin PR #468:   9e2ae6d26a7920055e1f11327dc0ddeb7b855c61
successor branch: research/gpt56-pro/93780-target-lorenz-directed-hardening
UTC cutoff:       2026-08-15T19:09:43Z
```

**RH remains unproved.** The successor is a hardening layer over PR #497, not a
second publication of the unpublished `93420` packet.

## Review order

```text
R-93780 and the 93420-vs-497 TSV;
L-93780 and check_zeta.py;
L-93781, directed_tail.cpp and the full 65-row replay;
L-93782 and the compact/tail control lock;
L-93783 and the exact typed-leaf replay;
L-93784 all-column compiler;
L-93785 direct native cost;
T-93780 and T-93781;
integration lock and endpoint dependency pins.
```

## What is new

```text
PR #497 adopted as controlling proposal;
no duplicate 93420 theorem paths;
directed zeta-half and derivative primitives;
directed sqrt/log evaluation of all 51,118,080 tail events;
finite directed row-66 extremality certificate;
exact half-open compact/tail join;
explicit typed leaf (positive source nu, current-only row bonus B,
  score surplus sigma);
complete leaf owner label and one common coefficient vector;
transitive endpoint dependency pins;
correction of four stale nonnormative SHAs in the PR #497 lock.
```

## Immediate falsifiers

Reject at the first failure of:

```text
the Hurwitz B2 remainder bounds or directed zeta intervals;
hardware fenv directed rounding under the published compiler flags;
one event interval or final-tail persistence polynomial crossing zero;
row-65 lower bound failing to separate from the row-66 boundary upper;
compact L-91781 not covering every real x<166000;
one source occurrence lacking a unique label;
B being used as positive source or exported to a child;
different Target-Lorenz coefficients across target, score or rows;
a full child capacity replacing an actual internal child response;
a signed comparison entering the positive source ledger;
one omitted q<K physical column;
nonzero exported recursion or root port;
direct native Y4 charge >=61000;
wrong endpoint orientation or an RH-bearing benchmark bridge.
```

## Replay

Quick:

```bash
python3 experiments/X-93780-target-lorenz-directed-tail/verify.py \
  --output /tmp/x93780.json
python3 experiments/X-93781-target-lorenz-typed-ledger/verify.py \
  --output /tmp/x93781.json
```

Full tail reconstruction:

```bash
python3 experiments/X-93780-target-lorenz-directed-tail/verify.py \
  --full --workers 4 --output /tmp/x93780-full.json
```

The full replay is intentionally expensive. It reruns every row rather than
trusting the retained aggregate.
