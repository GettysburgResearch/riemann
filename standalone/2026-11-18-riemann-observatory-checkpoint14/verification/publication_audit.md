# Checkpoint 14 GitHub publication audit

**Disposition:** The immutable payload passes archive and distribution validation. I found no apparent credential or private personal data in the scanned material. The user authorized publication of the complete sealed distribution, including historical delivery metadata carried within it. The Drive sharing state remains unverified.

## Verified distribution

- Sealed ZIP `/workspace/checkpoints/checkpoint14_sealed.zip`, 21,554,391 bytes, SHA-256 `9f1dcab0d244f667e90cdf712eea15c6f07b8141c1adaee7569f26774c57a198`. Both local distribution ZIP copies have the same hash.
- The frozen staging directory matches all 2,888 members byte for byte. The distribution manifest lists and authenticates 2,887 payloads. It counts itself as the final member.
- The archived validator passed on the expected digest, path safety, distribution allowlist, file byte counts and hashes, structural checks, and exact comparison to the standalone synthesis PDF and HTML. No source staging, raw discovery responses, nested ZIPs, bytecode, unapproved PDFs, missing members, or extra members appeared.
- There are exactly six PDFs, all on the original output allowlist and all without PDF attachments. They are `final_synthesis/synthesis.pdf` and `experiments/results/{augmented_moment63_escape,prime_band_round11,probability_chains64,witness62_prefix_transition,witness62_weighted_criterion_phase}.pdf`.
- Total unpacked bytes 83,741,305. Largest individual file `corpus/candidates.jsonl` at 13,448,721 bytes. Zero files above either 50 MiB or 100 MiB.
- No symlinks. All ZIP entries carry mode 0600. The frozen directory has two regular files with executable bits, `experiments/code/replay_839_reference.sh` and `experiments/code/continue_formal_round2.sh`. Manifest digests authenticate bytes. Git records executable-bit differences independently.

## Public content review

- No provider token, private key, JWT, bearer token, credential assignment, authenticated URL, or signed-ticket URL patterns matched distributable text or extracted PDF text/metadata. Common hardcoded-token and private-key patterns also had no hits in binary tables, PNGs, or the SQLite archive. This was a pattern-based sweep.
- Three email-shaped hits are the same public upstream author credit inside the vendored 839 files. One hit in `scripts/prime84_cue_moment_window_check.py` is matrix operator syntax. Home-path matches were parts of public-literature URLs.
- Four historical operational Drive file/parent locators appear in 17 files matching `quality/checkpoints/*drive*.json` and in `quality/delivery.json`, `logs/director.md`, `scripts/write_live_checkpoint.py`, `scripts/write_round9_checkpoint.py`, and `scripts/write_round10_checkpoint.py`. Historical tool responses report access unverified, with sharing and permission fields unset. The locators identify Drive resources. Drive applies its existing access controls independently, and publishing the locators grants no Drive permissions. A distinct Drive source link in research provenance also occurs in the SQLite graph. The current checkpoint 14 Drive delivery receipt and raw responses were generated after the seal and fall outside the verified archive.
- The checkout's `CONTRIBUTING.md` requires publication-safe material and retention of third-party licenses and notices. The 839 vendor verifier and its three numerical input directories each contain MIT LICENSE and NOTICE files. The AF formal source Apache-2.0 LICENSE and NOTICE sit under `experiments/licenses/AF-formal-source/` and preserve upstream derived-code attribution. Keep all five pairs intact.

## Reproduce the archive check

From `/workspace`:

```sh
python -B checkpoints/checkpoint14/scripts/validate_sealed_checkpoint.py \
  checkpoints/checkpoint14_sealed.zip --checkpoint 14 \
  --sha256 9f1dcab0d244f667e90cdf712eea15c6f07b8141c1adaee7569f26774c57a198 \
  --bytes 21554391 --pdf artifacts/synthesis.pdf --html artifacts/synthesis.html
```

This publication audit covered artifact integrity and distribution content. It did not replay the mathematics or establish GitHub integration status.
