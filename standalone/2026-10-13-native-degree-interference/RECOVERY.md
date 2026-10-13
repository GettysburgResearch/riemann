# Publication recovery

The twelve files in `../2026-10-13-native-matching-geometry/` are the unchanged
previously supplied matching-geometry packet. Its old README, manifest,
PUBLISHING and validation labels "not pushed" describe its historical creation
state. The present repository deposit supersedes that status, not its proposed
and unreviewed mathematical scope.

Recovered source commit: `8f5d93e6bd488ca3c2360f0a27e03c3f4d8bb1cd`.
Sole parent: `377f548cab8759399aca80ed3188c495667d562a` (#942).
Root tree: `8327d20634536561064ea1c10e66bf421cdf2dec`.
Recovered packet subtree: `0bda7e3860b387d02d3e8d4d570168f096c0d878`.

Live GitHub tree read-back returned all twelve expected blob identities and
sizes, including the original MANIFEST.json. Local SHA-256 and Git-blob checks
match all eleven manifest payloads and the manifest itself. Fresh ordinary
and optimized executions of both `verify.py` and `calibrate.py` reproduce
their respective recorded JSON files byte for byte.

An initial attempt to create the tree by local hashes failed because the new
blobs had not yet been uploaded. The failure did not create a commit. Uploading
the actual contents and reusing only the already resident helper corrected
that transport issue. The successful recovered commit is identified above.

The succeeding degree/phase packet adds new proposed work in a separate
directory. It does not alter or newly certify the recovered proof. The final
branch/head and draft PR are recorded in the PR description and delivery
receipt, not fabricated in advance in this source file.
