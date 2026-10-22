# Publication recovery: Weil resolvents and the three research reports

23 October 2026. **Publication only; no new mathematical approval.**

This directory publishes the exact 48-file structural-continuation delivery:
20 Weil-resolvent research files, the earlier 27-file report-led packet
(including the three original reports), and its one-file delivery notice.
All original bytes and historical qualifications are preserved.

**No new zero-free boundary or RH proof is claimed.** The component arguments
remain proposed research. The source-specific spectral identification and
cofinal convergence remain open. Publication, finite algebra and file integrity
are not independent analytic certification.

## Read the core arguments

Byte-identical browsing copies are provided for the [structural proof](browse/PROOF.md),
[theta residual and full tails](browse/THETA_RESIDUAL.md), and
[convergence argument and missing estimate](browse/CONVERGENCE.md).
The complete original source list, self-review, numerical reports, code,
report audit, route ledger and original uploads are in the archive.

## Restore the complete delivery

The 48 originals are stored in **25 binary archive parts**, not as 48 individually
browsable files. The archive is 194,964 bytes; the originals total 775,673 bytes.
Part numbering is deliberately nonconsecutive; use the exact order in
[ARCHIVE.json](ARCHIVE.json). [ORIGINALS.json](ORIGINALS.json) records every
original path, size and SHA-256.

From this directory, using Python 3.9 or newer:

```sh
python -I -S -B restore.py
python -I -S -B restore.py --output /path/to/new-directory
```

The first command verifies only. The second restores the original `standalone/`
paths under a new directory and refuses an existing destination. The script uses
only the standard library, verifies all parts and the pinned complete archive,
checks every file, rejects unsafe paths and links, and executes no research code.

After restoration:

```sh
cd /path/to/new-directory/standalone/2026-10-22-weil-resolvent-selection
python -I -S -B verify.py --manifest
python -I -S -B -O verify.py --manifest
```

## Publication and scope

The historical NOT PUSHED/read-only statements inside the preserved documents
refer to the earlier delivery and are superseded by this publication notice only.
Their mathematical status, source qualifications and archived experimental
results are unchanged. The old report errors remain separately audited; the
original reports have not been silently corrected.

This publication is on its own research branch based on
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`. It does not change the existing
inverse-moment PR #1014, any inherited file, main, or integrated scientific status.
No merge is requested by this recovery. See [VALIDATION.md](VALIDATION.md) for
exactly what was freshly run and what was not.
