# GitHub publication review for Observatory checkpoint 14

Place this exploratory deposit under `standalone/2026-11-18-riemann-observatory-checkpoint14/` on its own branch targeting `main`. Existing standalone research packets support the path. Preserve the ZIP byte for byte and the exact ZIP member hierarchy under `archive/riemann-observatory/`. Keep post-seal QA, local verification, and publishable Drive verification in separate package-level receipts; the original ZIP must stay immutable. Preserve third-party LICENSE and NOTICE files. The raw Drive response contains file and parent identifiers, destination URLs, and unverified sharing metadata. Review those outside the sealed package for public safety and prefer a factual transfer receipt with filenames, hashes, method, and visibility/readback limits over raw connector responses where link disclosure is unnecessary. Preserve the released checkpoint identity; the superseded unshipped quantifier diagnostic represents a distinct staging artifact.

Use a package-level README as the only new navigation. Link in review order to the archive START_HERE, Round 17 report, specific threshold and common-sequence adjudications, final synthesis HTML/PDF, immutable ZIP/sidecar, and QA/reproduction notes. The exploratory header should state status, scope, exact source/dependencies, actual tests, and smallest remaining gap. Keep root front doors, CURRENT_RESULTS, canonical registries, formal track, and integration records intact. Leave #1030 untouched as a separately scoped exploration.

Open a regular reviewable PR once archive QA and branch publication pass. The exploration is a complete checkpoint deposit with open mathematical questions, and the repository welcomes that contribution without requiring a draft. Use exploratory/archive language and include the finite, local, and conditional scopes. Treat Observatory record IDs as scoped archive references. A draft is reasonable only for unfinished publication work. No PR template was present. Include full exact base SHA and full pushed head SHA in the PR body, together with status, load-bearing files and IDs, finite/global boundary and RH relation, dependencies, arithmetic classes from computation receipts, commands and outcomes, known gaps and omitted replays, and preferred review order. Do not embed the head SHA in the commit it names. The local and remote main observed during review were both `f99d9e3908dde4865377c75d9ca051c1f545bf4f`; recheck while publishing and verify PR base/head/URL after creation. No exact-SHA independent mathematical review is implied by a sealed-artifact QA receipt.

## Reproduction and staged verification

`(cd artifacts && sha256sum -c riemann-observatory-checkpoint14.zip.sha256)` and the archived `scripts/validate_sealed_checkpoint.py` passed on the supplied files, including all 24 receipt code pins and independent comparison with the standalone HTML/PDF in /workspace/artifacts. The ZIP SHA-256 is `9f1dcab0d244f667e90cdf712eea15c6f07b8141c1adaee7569f26774c57a198`, size 21,554,391 bytes, and there are 2,888 ZIP members including the distribution manifest. The maximum extracted member is 13,448,721 bytes. GitHub can store both the sealed ZIP and extracted tree via ordinary Git blobs.

From the package directory, `(cd artifacts && sha256sum -c riemann-observatory-checkpoint14.zip.sha256)` and the following standard-library command validate the ZIP and archived renders. To match the pre-publication replay append one `--code-pin RESULT=SOURCE` per entry in the sealed validation receipt.

```bash
archive=archive/riemann-observatory
python3 -B "$archive/scripts/validate_sealed_checkpoint.py" artifacts/riemann-observatory-checkpoint14.zip \
  --checkpoint 14 --bytes 21554391 \
  --sha256 9f1dcab0d244f667e90cdf712eea15c6f07b8141c1adaee7569f26774c57a198 \
  --pdf "$archive/final_synthesis/synthesis.pdf" \
  --html "$archive/final_synthesis/synthesis.html"
```

Before pushing compare the exact staged or committed archive path set with ZIP names and every staged or committed Git blob with its ZIP member bytes. Verify the committed ZIP and sidecar similarly, including omissions from ignore rules and byte transformations. Check the scope of the staged diff and whitespace on newly authored navigation/receipt text. Preserve inherited whitespace in sealed files rather than changing archival bytes. Do structural `validate_archive.py` only in a disposable copy, as it overwrites `quality/validation.json`. Full integration/rebuild commands in the archived continuation are future-work instructions. The formal workflow does not cover this path. The bounded integration workflow may trigger through `*.md` on main-targeting PRs, depending on GitHub path evaluation and changed-file limits; its outcome provides baseline repository assurance. The sealed validator authenticates transport and archive consistency, with mathematical and source review limits described by the archive.

## Final package path clarification

The recipe above uses the final package artifact filenames. The portable package-level entry point is `python3 -B verify_checkpoint.py`; add `--git-ref HEAD` to compare the committed archive, ZIP and sidecar blobs byte for byte. The independent final review confirmed the wrapper links, frozen counts, mathematical scope and post-seal receipt byte preservation, and found no apparent credentials or private personal information in the added receipts. This supporting note is a publication-layout adaptation of the original review, not a sealed archive member.
