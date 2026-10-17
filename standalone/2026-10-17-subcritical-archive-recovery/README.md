# Byte-preserved recovery of the earlier thirteen-file 91/100 packet

This is RECOVERY, not a second announcement of the subcritical-scale idea.
The live #965 packet already proposes the same 91/100 boundary at commit
`d58e3282a9379b6ae165681bc2e21e4f9fd18c26`. It has ten files. The user-delivered
archive contains a distinct thirteen-file write-up, checker and source adapter,
which had not been published. The two versions are not byte-identical and are
not two independently accepted proofs. The direct raw-blob lookup of the old
PROOF.md returned 404 in this recovery session.

The four binary parts here concatenate into a deterministic tar.xz containing
exactly the ORIGINAL thirteen scientific packet files, without changes. Splitting
is purely transport; restore.py verifies the combined SHA-256, allows only the
thirteen named regular files, and refuses extraction into any existing path.
It does not run the recovered code. The ZIP's outer publication script, patch
and duplicate receipts are not scientific additions and are not mirrored here.

    python restore.py
    python restore.py --output /path/to/a/new/directory
    cd /path/to/a/new/directory
    python verify_manifest.py
    python verify.py
    python -O verify.py
    python run_mutations.py

The original NOT PUSHED labels, source limitations and proposed-theorem status
are deliberately unchanged. THIS notice supersedes only their publication label
for these thirteen files once the enclosing commit is reachable on GitHub.
It does not supersede their mathematical qualifications or assert recovery of
work from conversations not available in this session. No inherited #965 or #961
file, main, or integrated scientific-status statement is changed.

Fresh local recovery checks: the original manifest passes; both complete ordinary
and optimized verifier outputs equal the archived CHECKS.json byte-for-byte;
all eight separately executed optimized negative controls reproduce MUTATIONS.json.
The restored thirteen files were compared byte-for-byte with the uploaded packet.
These are publication and finite-bookkeeping checks, NOT analytic certification,
an external referee report, a Lean build, or repository-wide CI.

Provenance:
- user-delivered ZIP SHA-256:
  `f0cfa2e8780f544b0e4a11f6ef8adb3764bd793913a1cd598f9a3eaac97d00b4`
- combined tar.xz SHA-256:
  `b62d32003291be5b24d57d79232463d1853aed7a860668ecdc60753e22172c30`
- original proof Git blob: `7cccf97f3a9843fef2c5ce4d74f8476967e9fb79`
- original verifier Git blob: `6048cff9edd36ad87b9425b4d6c4b1d04fa7200c`
- scientific parent of the old packet: #961, `7bd275b44261fff93bb565a9342c44b7c66526f6`
- live continuation parent for this recovery: #965, `d58e3282a9379b6ae165681bc2e21e4f9fd18c26`.

For the readable current 91/100 proposal use
`../2026-10-17-subcritical-dedekind/PROOF.md`. Restore this archive to inspect the
historical alternative derivation. Future work should cite which one it uses.
