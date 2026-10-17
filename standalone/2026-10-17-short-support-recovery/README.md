# Lossless recovery of the previously unpushed short-support packet

Status: publication recovery, not independent mathematical approval.

The four binary `archive.part01` through `archive.part04` concatenate to one
XZ-compressed TAR containing all THIRTEEN ORIGINAL FILES of the delivered
`riemann-short-support-theta-20261017.zip` source packet, unchanged. The
outer ZIP's duplicate patch and transport receipt are not source files and
are not inside this repacked archive. This is an archived-source recovery,
not a claim that thirteen plain files were separately added to this branch.

Run, from this directory:

    python recover.py ../2026-10-17-short-support-theta --replay

The destination must not already exist. The script authenticates every part,
the combined archive, all original payload hashes and the exact thirteen-file
Git tree before writing. It rejects unsafe paths and never overwrites existing
research. `--replay` executes the original manifest and both normal/optimized
checkers and compares their entire output with the archived CHECKS.json.

Original source tree: `a80cb7e2404e0f6835c47017597b6acbeb9cb264`.
Original source base: #959, `7b845294207d96b883c1fa95028663082267804f`.
Combined archive SHA256:
`966fc4099801404d5f5922614e687c18c5c383028d3fd5d5b59a88250abddf57`.

All original historical NOT PUSHED labels, proofs, scripts, manifests, test
outputs and mutation records are preserved. This notice supersedes only the
publication status. Original manifest plus normal/optimized checker replay
passed freshly during recovery. Historical mutation generation was not newly
rerun. No mathematical referee, full-repository CI or Lean build is claimed.

The new selected-fourth-density packet is separate. It cites the recovered
REFLECTED_MOMENT.md for short support and improves the density/contour argument;
it does not silently modify the old 91/100 statement.
