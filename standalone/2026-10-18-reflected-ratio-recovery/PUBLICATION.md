# Reflected-ratio packet: publication recovery

Status: byte-preserved publication of the previously delivered research packet. This is not a new mathematical result, independent review, acceptance of the proposed 19/21 consequence, or an RH proof.

The twelve original files from `riemann-reflected-ratio.zip` are published as individually readable files under `standalone/2026-10-18-reflected-ratio/`, unchanged. Their complete Git tree is `a9e1cbeca5b484870d5b511abb59cc75948a4160`, matching the tree reconstructed from the supplied archive. The historical NOT_PUSHED labels in the original README, manifest, draft description and validation record are preserved. This separate notice supersedes publication status only; every analytic qualification remains.

Base: PR #975, commit `edbc27b61208ccc7ee1fa99fa3f4e861f5a03452`.
Publication branch: `research/reflected-ratio-recovery-20261018`.

## Fresh recovery checks

The archive was safely extracted into a new local directory. Its `python replay.py` completed successfully: four normal/optimized summary and detailed reports matched the saved bytes; all eight separately executed corrupted models were rejected at their declared gates; all eleven manifested payloads matched their SHA-256 hashes and lengths. The full twelve-file Git tree also authenticates the unchanged manifest itself.

The stored Git tree returned by GitHub equals the locally reconstructed source tree. This checks the complete payload, not merely two proof files or the compact summary. Finite bookkeeping tests do not certify the analytic inputs or the proposed global theorem. No independent mathematical referee, Lean build, repository-wide validator or remote CI result is claimed.

## Reading and replay

Read [the ratio lemma](../2026-10-18-reflected-ratio/RATIO_LEMMA.md), [the full composition](../2026-10-18-reflected-ratio/COMPOSITION.md), and [the original source boundaries](../2026-10-18-reflected-ratio/SOURCES.md).

Run:

```sh
cd standalone/2026-10-18-reflected-ratio
python replay.py
```

Only new standalone paths are added. No prior proof, another contributor's branch, main, or integrated scientific-status statement is changed. Pushed research drafts are not the same as reviewed results merged into main. No work absent from the available conversation archives is claimed recovered.
