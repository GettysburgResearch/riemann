# T-97240 full-packet publication recovery

This publication repair promotes the exact deterministic packet supplied by
the author onto PR #569. The existing ten-file remote publication was a
condensed reconstruction of the same new adaptive parity-Hall route, not a
reproduction of PR #561. Its combined lemma remains in the branch as an
additional front door, while the packet's five separately reviewable lemmas,
PDF, review specification, experiment ledger, handoff, and claim-status files
are now present.

Where an authored packet path already existed, the packet bytes are
controlling; the pre-recovery variants remain recoverable from Git history.
The generic packet `PR_BODY.md` is published as `PR_BODY_97240.md` because the
branch inherits an unrelated root `PR_BODY.md`. The live checksum ledger
changes only that path label; the exact original ledger is retained under
`integration/2026-08-17/t97240-original-author-packet/`.

```text
frozen base PR:       #561
frozen base commit:   db9bdc63c855c6ddf664b763d748f8155a6a2c67
pre-recovery PR head: 3bcafc5aacaf46f2e1beea43ed647cd7fb661892
packet ZIP bytes:     294638
packet ZIP SHA-256:   593867357b1adc4c4a4217e6c2b2b6b27f83ddb98ef9237527f34a268fcf3883
replay verdict:       PASS_T97240_GLOBAL_PARITY_HALL_SCALAR_JULIA_REDUCTION
proof-object SHA-256: 2cc5a62c6d85ac486382649ec2f87818ced52ab4cd47f1cc30f2eeb13d79d6b6
scientific status:    GABPT open / RH-bearing; conditional consumer proved
RH established:       false
```

This recovery changes publication completeness and provenance only. It does
not add or alter mathematical reasoning.
