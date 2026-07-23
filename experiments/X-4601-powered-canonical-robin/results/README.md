# X-4601 committed results

The complete production terminal stream is deterministic but generated. It is
not committed because the repository protocol prefers compact proof manifests
and regeneration scripts over reproducible bulk output.

Committed release anchors:

- `production-manifest.json` — exact endpoint, parameters, counts, source
  fingerprints, internal certificate digest, terminal digest, and both
  uncompressed and deterministic-gzip hashes;
- `verification.json` — the independently written traversal replay output;
- `parameter-ladder.json` — fail-closed replacement-precision replay;
- `mode-comparison.json` — exact powered-versus-separate production comparison;
- `runtime.txt`, `tests.txt`, and `SHA256SUMS`.

Regenerate the full certificate by following the commands in the experiment
README, then compare all hashes and summaries with the committed manifest before
accepting the replay.
