# X-20701 — Directed actual-zeta conditional-frame ladder

This is the first non-synthetic production consumer of PR #206.

At every retained integer cutoff it constructs the cutoff-free D-0001/X-0001
Weil block, including every prime power, the complete pole block, and the
cutoff-free archimedean block. The first two critical-line zeta zeros supply the
first and conditional second frames. A standard-library `Fraction` consumer
reconstructs the graph kernel, selected frame, joint corrected residual, Schur
floor, and triangular metric endpoint.

The immutable producer and consumer source blobs are:

```text
arb_producer.py  85bec1e106ba4a0b2cdabb363e0fcb0dc5bdc7b2
verify.py        a774ce8e7d7adc4be64d2f197fd1e419130e7eb4
source commit    34d8391395d1e08ae986bf5c1c10439f90f9cb57
```

They were initially written through the connector's default-branch contents
endpoint by mistake. The workflow materializes those immutable blobs by commit
and verifies their Git hashes before execution; the accidental default-branch
copies have been removed. The source commit remains immutable repository
history and is used only after exact blob-hash verification.

The support ladder is

```text
5, 10, 20, 50, 100, 200,
500, 1000, 2000, 5000, 10000, 100000.
```

The same frozen integer directions are replayed at 256 and 384 Arb bits, with
primitive interval containment required.

## Scope

These are actual zeta-data certificates for complete finite D-0001 test blocks.
They are not yet the complete augmented Suzuki low packets required by T-14302.
A positive fixed-`N=1` support ladder is a calibration and a genuine finite
result, not a proof of RH.
