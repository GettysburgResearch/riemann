# T-97620 publication recovery note

This branch republishes the exact authored files recovered from
`t97200-exact-annular-bias-source-no-go.zip` (download SHA-256
`d592df72f3bb47c3788cf3247faa491c5d091d5d753c5b49b3a7596a47efc24a`)
under a collision-free `97620` namespace.

The eight gzip certificate streams are byte-for-byte unchanged and contain
1,167,388 lines in total. The packet omits `verification.raw.json`,
`verification.448.raw.json`, `build_and_replay.sh`, and `src/mpfr_min.h`, which
the retained metadata/source identifies as inputs to a complete from-source
regeneration. Those files were not reconstructed or invented. The included
verifier therefore checks the retained streams, their exact hashes and line
counts, the final proof-object record, and hostile mutations only.

The only scientific-text repair is the mechanical replacement of one isolated
carriage-return byte in `PROOF.md` by the intended LaTeX token `\\rm`.

Scientific status: the scalar theorem and no-go theorem are retained; the
Riemann Hypothesis remains unproved.
