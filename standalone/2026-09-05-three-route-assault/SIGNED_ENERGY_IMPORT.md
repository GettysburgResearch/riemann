# Attached signed-energy attempt: publication handoff

The separately prepared [signed-energy packet](pass4-signed-energy-attempt/README.md)
is now deposited on PR #793. Its seven files are byte-for-byte copies of the
author's attachment, `riemann-pr793-pass4-attempt.zip`. The archive SHA-256 is
`dcbc0ac035051ececc061ef8a9b279c0378e3028a2d794941f3270f8567833cc`.

The attachment was prepared against `bfb66e07f7e38306dbcb916911332a591efce917`
and proposed the directory name `pass4/`. By import time, commit
`a4366436a248102f86f0d692366ca705cad3fca9` had published a different, independent
prime-tail/cutoff packet at that path. Both contributions are retained.
Only the attached packet's containing directory is renamed to
`pass4-signed-energy-attempt/`; its proofs, checker, results, and manifest
are unchanged. References to local-only publication in its README and
VALIDATION.json describe the original handoff, not the later import.

Import replay: 706 bounded exact controls and ten unit/rejection tests pass
in both ordinary and optimized Python; the original SHA256SUMS entries
match. This is a publication and replay check, not an independent review
of the analytic proofs or a promotion of their scientific status. RH
remains unproved. No earlier packet is modified.
