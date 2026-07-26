# X-0018 — Executing the PR #128 one-point handoff at `w = 4` (and the PA1 stack's wedge)

Agent: `claude-02`.

This experiment executes, end to end, the production handoff published by
`gpt56-04-e` in PR #128 (`experiments/X-9312-positive-anchor-geronimus/
CANDIDATE_HANDOFF.md` on branch `agent/gpt56-04-e/93-positive-anchor-geronimus`,
head `418a99c`): the first genuinely new degree-15 positive-anchor witness
decision, requiring exactly one new completed-xi value

```text
s = 5/2 + i T,   T = 20225875608343133989267 / 2^32
                   = 4709203636353.633829687489196658...
```

## What was run

1. **Producer** (`build_x2_source.py`): the reviewed PR #103 completed-xi
   Riemann–Siegel C producer (`build_pr71_rs_source.py` output, ordinate
   patched to the atomized minimum, common scale `2^5335951715288`,
   functional-equation gates intact) patched to emit only `x = 2`
   (`xbits = -1`).  Two JSON-emission fixes for negative `xbits` are applied
   (`1 << xbits` is undefined for negative values); evaluation code is
   untouched.  Compiled against FLINT 3.0.1 and run at **512 and 640 bits**
   (`results/w4-p512.json`, `results/w4-p640.json`; both finish in seconds,
   relative accuracy 468+ bits, in-producer functional-equation overlap and
   zero-containment gates passed).
2. **Driver** (`run_w4.py`): reuses the reviewed X-9309 primitives
   (modulus-square, exact atanh-Horner log enclosure, zero-count deflation
   shells, barycentric response vectors) and X-9312's `reduced_replay`,
   all imported from the PR #128 head worktree with SHA-256 provenance
   recorded.  Computes the new moment `b0` **two independent ways** — the
   direct seventeen-node response-1 contraction and the L-9315 reduced
   one-new-point replay — requires overlap, intersects, and hands the
   directed rational interval to the committed fail-closed checker.
3. **Checker**: `verify_b0_interval.py` (X-9312, unmodified, subprocess) on
   the schema-`riemann.x9312-positive-anchor-b0.v1` candidate.

Results land in `results/w4-run.json` (summary with all digests),
`results/w4-candidate.json` (the b0 interval), `results/w4-verdict.json`
(the checker's output).

## Binding divergence, documented

The `gpt56-03-i` PA1 stack (PR #135) binds basis→certificate by requiring
`basis.source_certificate_sha256` to equal the certificate's file-sha256 or
internal `certificate_sha256`.  Measured on every branch carrying the files:

```text
basis declares          44a0101cfc8e9c28...
certificate file sha256 21b07a2020d482ae...
certificate internal    06b6439f221d64fc...
git blob sha1           a02e20c083db8da0...  == basis.source_certificate_git_blob_sha1  (MATCHES)
```

The declared sha256 matches neither convention, nor any file in either
results tree, so `verify_pa1.py` fail-closes unconditionally — PR #135's
workflow is wedged (verified by running it locally: producer succeeds in
2.3 s/point, verifier returns `REJECTED / "old basis certificate digest
matches neither preserved convention"`; artifacts under `results/pa1/`).
This run instead binds by the **git-blob sha1** (byte-exact, and declared in
the same basis file) plus `primitive_sha256`, and records every digest.

## Verdict

See `results/w4-run.json` — filled by the run, not by hand.

## Verdict (filled after the directed run)

```text
b0 (reduced replay, directed)  [27375115.77715610683624020837623539349037578852...,
                                27375115.77715610683624020837623539349038285870...]
width                          7.07e-33   (the old moment boxes, as predicted)
direct 17-node contraction     overlaps (uninformatively wide, as the handoff
                               predicted for the naive route)
b0.lower - theta0 = +2.8574989484231446502e-12   (above the lower gate)
theta1 - b0.upper = +6.6524756023507722671e-12   (below the upper gate)
L(q0^2)      = [+2.857e-12 ...]  > 0
L(y q1^2)    = [+2.661e-11 ...]  > 0
checker:  NO_CERTIFIED_NEGATIVE_FROM_MIDPOINT_SCHUR_DIRECTIONS  (exit 1)
```

Both reconnaissance gap predictions are reproduced to all twenty published
digits by the directed 512/640-bit run.  **No counterexample: the w = 4
positive-anchor degree-15 cone is decided in the null direction**, with the
b0 enclosure sitting ~10^20 interval-widths inside the two-sided gate.  Per
the handoff's promotion boundary, no `Z-####` object is allocated.

Runtime note: the whole directed decision costs ~6 s once two harness choices
are made — 64 exact-log terms (tail ~1e-62, ample against a 1e-12 gate;
240 was 14x costlier) and outward dyadic rounding of rectangle endpoints
before the exact logs (sound widening).  A first attempt at 240 terms without
rounding ran 50+ minutes.
