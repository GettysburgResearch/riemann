# Recover the distinct eighteen-file tilted-numerator packet

Status: byte-preserved archival recovery only. This is not another new 49/54 theorem, independent review, or acceptance of the archived mathematics.

The user correctly identified that PR #969 already published a proposed 49/54 composition. Its eight-file packet at 6542781188469e8a23dadf9d419b3d5cf4d11de7 differs from the eighteen-file user-delivered riemann-tilted-numerator-20261018.zip. The latter's exact directory tree was not available at its computed Git object identity when checked. This recovery preserves all eighteen original files without overwriting #969 or combining their claims as independent improvements.

The four binary parts concatenate, in numerical order, to one deterministic tar.xz. It contains every original file unchanged, including proof notes, full certificates, checkers, manifest, and historical publication qualifications. This is archived-source recovery, not eighteen separately browsable plain files.

- Combined archive SHA-256: e2161170738aece61d4b4ae50b33c69ea3af9a308d963e4f1815b975081bd860.
- Combined archive size: 28444 bytes.
- Exact recovered source directory Git tree: 41b9a88ffefc1bef154f5c6ea7d62fce5dd73c72.
- Original source directory: standalone/2026-10-18-tilted-numerator-strip/.
- Original scientific base: #968, 14f544fb4293ffb59942ff8d345ab9d6da67025c.
- Recovery base: #969, 6542781188469e8a23dadf9d419b3d5cf4d11de7.

Run:

    python standalone/2026-10-18-tilted-packet-recovery/restore.py --output /path/to/new/tilted-numerator-strip

The restore script refuses an existing destination, authenticates the archive and exact eighteen regular-file names, verifies the complete Git tree and original SHA-256/length/blob manifest, and executes no recovered code. To replay after inspecting the recovered code, run its replay.py explicitly.

Fresh validation in this recovery pass: the original complete replay.py succeeded, matching all four ordinary/optimized summary/detailed reports and all eleven optimized negative-control outcomes. All seventeen manifest payloads match. These are finite bookkeeping checks, not certification of the source-qualified analytic theorem. The four uploaded binary blob hashes match the locally generated parts.

Historical NOT PUSHED labels remain unchanged. This README supersedes only their publication status. Original failed-source-access and same-author review qualifications remain applicable. No inherited proof, another contributor's branch, main, or integrated scientific status is modified.
