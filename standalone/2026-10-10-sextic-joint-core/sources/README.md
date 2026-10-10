# Exact adjacent source snapshots

These two files are verbatim copies from GettysburgResearch/riemann PR #914, frozen commit `0cc0428fedbbfc340044c7451b3d392c1da9a103`:

- [A2_COMPLETION.md](pr914/A2_COMPLETION.md), source path `standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md`.
- [CONDUCTOR_SECTORS.md](pr914/CONDUCTOR_SECTORS.md), source path `standalone/2026-10-10-sextic-moment-conductor-core/CONDUCTOR_SECTORS.md`.

[MANIFEST.json](MANIFEST.json) records byte lengths, SHA-256 hashes, source commit and Git blob identities. Each copy was compared directly with the corresponding Git object. Relative links inside these verbatim sources retain their original source-directory meaning; this folder is a two-file dependency snapshot, not the full PR #914 packet. The complete original packet remains available [at its exact commit](https://github.com/GettysburgResearch/riemann/tree/0cc0428fedbbfc340044c7451b3d392c1da9a103/standalone/2026-10-10-sextic-moment-conductor-core).

The complementary #915 packet is already present in this branch's ancestry at `9959364671f89b86f3992ec5ed5e19f804eb607b`, under `standalone/2026-10-10-sextic-critical-core`. It is not duplicated or modified. All source and review limitations of both packets remain in force.

The verbatim A2 source contains one original form-feed byte (`0x0c`, zero-based byte offset 13449) before `rac` in equation (5.2). It is preserved for byte identity. The new interface proof derives its scale quotient directly from the separate child definitions (4.3), giving `A_t B_t = AB / ((Nc)^3 (Nd)^3 (Ne)^4)` and the normalized scalar in its equation (3.5); it does not depend on interpreting the malformed typesetting command. Authored files contain no such control bytes.
