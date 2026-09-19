# Publisher handoff

The RCB26 patch was applied as an additive continuation of PR #848 on top of
`617cfaca6130addd2d16bbce6af117a55aef761b`. Since the author's source snapshot
`9e4375952c87835c2f4f2cca10a996009e74a435`, that branch had added the separate
NSR26 resonance-stress packet; those nine files were preserved unchanged.
No combined mathematical acceptance is implied by sharing a branch.

All ten supplied SHA256SUMS entries match the restored original LF bytes.
The patch's eleven original files are retained without substantive changes.
Windows Git initially converted line endings during application; original LF
bytes were restored before committing. The accepting checks read equivalent
text and reproduced the author's canonical result.

[Fresh publisher replay](PUBLISHER_REPLAY.json): standard-library reconstruction
passed normally and with optimization; the nine-method unittest suite passed
in both modes on Windows/Python 3.12.10. This is a scoped packet replay, not
independent mathematical review. No optional NumPy scout, full-repository
validator, Lean build, or CI success is claimed. Authoring publication-failure
notes remain historical records; this handoff accompanies the publication.

RH and the native cross-block covariance gain remain open. Review the whole
argument in PROOF.md independently of these finite checks.
