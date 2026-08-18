# PR #580 expanded-packet reconciliation

The first publication of this branch intentionally used a six-file remote-minimal front door:

```text
head: 106730b4d13230cf3028f18e5b8930591cc5053d
tree: 081d9aaccd6263c0ade1a6deadfbe301a18b86de
```

The supplied deterministic ZIP has SHA-256
`a171862e6845234e4e83feae9df60885250ec62a2c9fc73e7314721a5fa134d0`
and also carries the complete twenty-file scientific packet enumerated in
`gpt56-pro-95400-intended-files.txt`. This reconciliation publishes that
expanded packet on the same branch while retaining the minimal front door and
its exact history.

Only a transcription defect was repaired before publication: six tab-prefixed
`frac` tokens in the factorization of \(Q(S)\), duplicated between
`L-95400-safe-triple-annularization-of-the-focc-packet.md` and
`PROOF_PACKET.md`, were restored to twelve literal LaTeX `\tfrac` tokens.
No formula, theorem, proof status, numerical result, or scientific conclusion
was changed.

The expanded verifier and retained output replace their compressed
remote-minimal equivalents. Both certify the same verdict:

```text
PASS_X_95400_Q4_FOCC_ANNULAR_HARDENING
```

Scientific status is unchanged: the safe annularization, exact kernels,
decompositions, and closed sectors are retained; the separated coprime
Type-II theorem `SACF`, hence FOCC, OCHD, and RH, remain unproved.
