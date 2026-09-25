# Publication pass 1 — 25 September 2026

Status: PROPOSED mathematics and exact finite certificates; not independently reviewed or integrated.

User authorized publication and continuing research after the preceding chat-only pass. The nine files in the supplied `riemann_arithmetic_boundary_20260925.zip` are preserved byte-for-byte. Their historical statements that no repository changes were made describe the original pass, not this publication. This publisher note is a separate addition.

Base: `GettysburgResearch/riemann` main at `f99d9e3908dde4865377c75d9ca051c1f545bf4f`, tree `8bddd12122e8a772683c9ed0b37dbcb945036893`.
Branch: `research/relative-arithmetic-boundary-20260925`.
All changes are confined to a new standalone directory. Main, other contributors' branches, canonical statuses, and workflows are untouched.

## Fresh replay

All eight SHA256SUMS entries passed after extracting the supplied archive. The following complete commands succeeded on the current Linux container:

```sh
python -I -S -B check.py --output replay.json
cmp results.json replay.json
python -I -S -B completion_certificate.py --check completion_receipt.json
python -I -S -B -O check.py --output replay_optimized.json
cmp results.json replay_optimized.json
python -I -S -B -O completion_certificate.py --check completion_receipt.json
```

Both algebra outputs were byte-identical to the archived receipt. Both completion replays included the optional full small-completion scout and reconstructed the complete stored receipt. No full repository validator, CI, Lean build, or independent mathematical review was run.

## Load-bearing claims

Review RESEARCH.md Sections 3–5, especially the uniform resonance inequalities and the distinction between the preserved native head and artificial completion tail. The finite checks authenticate the stated arithmetic, not the analytic arguments or an unbounded native upper estimate.

## Continuation

New mathematics belongs in a separate pass-2 directory. Do not silently upgrade the first pass to a full comparison theorem, a native asymptotic gain, or an RH proof.
