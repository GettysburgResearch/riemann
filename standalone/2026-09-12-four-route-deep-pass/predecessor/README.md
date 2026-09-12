# Frozen BHH26 recurrence source

`bhh26-check.py` is an **unmodified byte copy** of:

- Repository: Gettysburg Research / riemann.
- PR: #860, explicit-cutoff variant.
- Commit: `e1a782cffaafbc9cc228273ed94ce63ae0407632`.
- Original path: `standalone/2026-09-10-astra-branching-high-height/check.py`.
- SHA256: `c50a582fcb298dd17971e4f8969bdf39b78d3edc2862321c22faf8ce7fecb97d`.

The source is distributed under the original repository's MIT License,
copyright (c) 2026 Gettysburg Research contributors. `LICENSE` is an unmodified
copy from that same commit (SHA256
`b73bb0e2318088e194a54dfb09c23ed0321c1b3d5c1f07258ad5876bf3aa16c1`).

The consumer `../height-cutoffs.py` checks the literal source bytes against
its pinned SHA256 **before compiling or executing them**. It then calls the
full rational `threshold_records` recurrence. The predecessor's standalone
packet-inventory CLI is not invoked: its neighboring historical files are not
vendored and are not needed by this consumer. Only standard-library imports
are used.

The directory's `.gitattributes` disables line-ending conversion, preserving
the authenticated bytes across Git checkouts. Reproduction needs neither Git
nor the historical commit's objects. Source commit/path/hash fields and every
mathematical result in `height-cutoffs.json` remain unchanged.

The hash pins an identified source file; it does not independently validate
its mathematics or authenticate a jointly replaced consumer and manifest.

## Packaged reproduction check

On 2026-09-13, both `python -I -S -B height-cutoffs.py` and
`python -I -S -B -O height-cutoffs.py`, run from the enclosing packet,
reconstructed depths 0 through 8 successfully. A separate run from outside
the repository, with `subprocess.check_output` prohibited, also succeeded.
An actual changed-byte source in a temporary fixture was rejected for the
SHA256 mismatch before its appended executable statement could run; it
produced no result receipt. The temporary target was checked inside the
explicit assessment directory before cleanup.

The regenerated `height-cutoffs.json` was compared with the original receipt
in `assessment-20260912-four-route-deep/`: the parsed content and literal bytes
were identical. There were no mathematical, provenance-field, or receipt
differences. Printed floating ratios remain approximate displays of the exact
rational ratios retained in that unchanged receipt.
