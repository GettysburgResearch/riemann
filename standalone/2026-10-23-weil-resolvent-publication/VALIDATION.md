# Fresh publication checks, 23 October 2026

This is a recovery and integrity check, not a new analytic review.

- The delivered structural ZIP was safely extracted: exactly 48 regular files,
  775,673 bytes, no unsafe paths or symbolic links. Its SHA-256 is
  `5c6d42a85a6dbe1bd329a5ab67609776356f0262d7ad14dcac4be9cc30252dd5`.
- The deterministic TAR.XZ is 194,964 bytes, SHA-256
  `8185bfe6f9a5e2899cae78083a2d9e232f7b723d02a76eb88fb6116c0db03646`.
  All 25 part sizes and Git blob identities match the local byte inventory.
- `restore.py` succeeds in isolated ordinary and optimized Python. A fresh
  restoration reproduced every original file byte-for-byte.
- In optimized Python, an existing output directory is rejected with
  `output already exists`; a deliberately damaged final part is rejected with
  `part hash mismatch`. Neither control is counted from a generic crash.
- The restored structural `verify.py --manifest` passes in isolated ordinary
  and optimized Python, with identical output: 19 manifested files and seven
  finite algebra groups. Its report explicitly says `analytic_certification: false`.
- The earlier report packet's 26 manifested payload digests were checked. The
  three reports are unchanged parts of that original packet.
- The three browsing copies match their corresponding archived originals exactly.

The seven structural groups are zero-division Gram identity, rank-one PSD
update, generic-positive-matrix counterexample, prime-power census through 64,
theta-kernel normalization, bottom-space division regression, and the
near-null/negative-spectrum control.

The original numerical experiment reports, independent-assembly numerical
cross-check and historical mutation campaigns are preserved. They were not
rerun in this publication pass. No new source-paper reconstruction, independent
agent/human analytic review, proof-assistant check, repository-wide validation
or remote CI run is asserted.

Binary publication is authenticated by the returned Git blob identities and
the complete remote tree, not by a claimed UTF-8 fetch of the archive parts.
