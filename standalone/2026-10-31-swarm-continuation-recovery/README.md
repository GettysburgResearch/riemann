# Recovered continuation packet — 31 October 2026

This directory publishes the 39-file research packet recovered from the saved Library artifact `riemann-swarm-continuation-20261031.zip`. The interrupted remote branch contained only its parent, `11b4f6612275955a1fddb5c53f67dc21124783f8` (PR #1026). The original proposed tree and a sampled original blob were absent when checked.

## Lossless recovery format

All 39 original payload files are stored byte-for-byte in a deterministic tar.xz archive, split into eight binary parts. They are **not individually browsable until restored**. `restore.py` verifies each part, the entire archive, exact membership, all 38 original manifest entries, and their SHA256 and Git blob hashes. The manifest itself is covered by the archive hash. No restored code is executed.

From the repository root:

```sh
python3 standalone/2026-10-31-swarm-continuation-recovery/restore.py
python3 standalone/2026-10-31-swarm-continuation-recovery/restore.py --output standalone/2026-10-31-swarm-continuation
```

The output directory must not already exist. The restored parent-relative dependencies are present on the base branch. Original publication-status documents are historical records and have intentionally not been rewritten.

Archive: 79,868 bytes; SHA256 `eaf3fb5fe828e33974f2bab471647576083b4917154ecfe5f7acf219929566cd`.

## What was recovered

- A proposed Laguerre support-window theorem and an obstruction to the old absolute anchor budget.
- A cofinal Bessel approximation and limiting companion/residue analysis.
- A cosine-phase version of the native discrete approximation criterion.
- Exact full-complex-disk Bessel certificates at `(a,M)=(10,50)` and `(20,100)`, energy radius 500.
- Proof notes, original reviews, source provenance, scripts, and recorded results.

Read the restored `README.md`, `CLAIMS.md`, and `COORDINATOR_REVIEW.md` first. This recovery does not newly certify every analytic argument. It does not establish RH or an improved zero-free region.

## Fresh validation during recovery

All original manifest checks passed. Six programs were rerun locally: the anchor checker, companion structure checker, native cosine checker, local-gate adversarial controls, and both Bessel disk certificates. All returned zero and all six parsed JSON outputs matched the archived results exactly. The two disk certificate replays took approximately 70 and 138 seconds respectively. Floating-point exploratory probes were not included in these six exact replays.

The restorer was tested by bytewise comparison of all 39 output files, rejection of a flipped part byte, path traversal checks, and refusal to overwrite an existing output directory.

No new parallel research agents were launched during recovery. Prior agent-review documents remain historical provenance, not a claim of fresh independent review. The publication tree differs from the original proposed raw-file tree because this publication uses a lossless archive. Existing repository files are unchanged.
