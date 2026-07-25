# X-6601 — Exact dual-cone search on the proof-grade Arb `xi'/xi` table

Experiment ID: X-6601  
Status: exact rational replay of externally produced directed balls; no RH candidate  
Agent: `gpt56-06-d`  
Issue: #66  
Date: 2026-07-25  
Related claims: D-3201, L-3201, L-3202, L-3901--L-3904, L-4701--L-4703, D-5701, L-5701, L-5702, L-6601

## Question

Can all existing proof-grade value-only `xi'/xi` localizers be placed over one canonical primitive feature table and combined into an exact rational conic portfolio with a strictly negative robust endpoint and positive feature-repair moat?

## Canonical feature table

The primitive feature at horizontal node `x_k` and ordinate block `T_j` is

\[
 R_{j,k}=\operatorname{Re}\frac{\xi'}{\xi}
 \left(\frac12+x_k+iT_j\right).
\]

The exact grid is

```text
T_j = 20225875608343121406355 / 2^32 + j/32,
-32 <= j <= 32,

x_k in {2^-17,2^-15,2^-13,2^-11,2^-10,2^-9,2^-7,2^-5}.
```

There are 65 ordinate blocks, eight features per block, and 520 primitive features in total. Each feature is enclosed once by intersecting the two rigorous PR #56 assemblies:

1. differentiate the completed `xi` product and divide by `xi`;
2. assemble the corrected completion terms plus `zeta'/zeta`.

Repeated use of one `R_{j,k}` never creates independent uncertainty.

## Immutable source artifacts

### Baseline table

- GitHub Actions artifact: `arb-xi-high-carrier-grid`;
- artifact digest:
  `sha256:9811f269b4b4d0bda8f85d4ff53e3f5ba1a619e37dba5cdfb29fe924aa5216ec`;
- certificate SHA-256:
  `10025d3c3b50b24f0b39c9981664131644fc58ad0a59fd8606f1d96d9b3e02c2`;
- directed precision: 128 bits;
- exact points: 520.

The original PR #56 checker certified all 2,275 imported channels nonnegative. X-6601 generated a materially larger library and found 51 exact feasible anchors immediately. Fourteen blocks were too close to rank deficiency at 128 bits and were escalated rather than classified from their midpoints.

### Ambiguous-block escalation

- GitHub Actions artifact: `arb-xi-ambiguous-pick-batch`;
- artifact digest:
  `sha256:646ff50e6191d68700bc3bb9a2ad21010241f51ad384d9ee36078a55d6f857a3`;
- certificate SHA-256:
  `bc9bf349864fa65257a195538404e20a9e49891d18e2e55faeb44505b85d618f`;
- PR #56 verification SHA-256:
  `317049ea8390df76927685d4b2398e3abf6a411eebcdf81f69765b0622e9e558`;
- directed precision: 192 bits;
- exact points: 112, covering precisely the fourteen baseline anchor failures.

## Localizer library over one table

For every ordinate block, `analyze_feature_cone.py` reconstructs exact rational coefficients for:

1. **scalar passivity** — eight rows `R_k>=0`;
2. **all pairwise two-channel rows** — every `A` and `B`/secant row;
3. **complete-Bernstein divided differences** — every node subset of size at least three with its exact alternating orientation;
4. **barycentric Pick product rows** — every node subset of size at least two;
5. **ordinary same-height Pick matrix** — the full rational midpoint matrix and exact `LDL^T` pivots;
6. **matched-pole Pick vectors** — explicit rational model-cell rows whenever the universal Pick anchor is not already available;
7. **cross-Loewner total-positivity controls** — every minor on disjoint increasing row and column lists through order four, the maximal possible order for eight nodes.

A full positive-definite Pick anchor is stronger than enumerating candidate vectors: it proves nonnegativity of every exact real Pick direction, every matched-pole construction, and every exact finite PSD Gram multiplier at that feature point.

The jet-only differential and shifted-Stieltjes matrices of PR #43 are not silently fabricated from value samples. The derivative-free secant, divided-difference, barycentric Pick, ordinary Pick, and cross-Loewner replacements from PRs #48 and #52 are included. A future jet table is a genuinely larger feature space.

## Exact algorithm

For each block:

1. intersect both primitive directed intervals;
2. choose the exact rational midpoint of each intersection as an anchor nominee;
3. replay 530 normalized affine rows using exact fractions;
4. construct the full exact rational Pick matrix and compute exact `LDL^T` pivots;
5. enumerate 1,106 exact cross-Loewner minors;
6. declare a feasible anchor only when every check is nonnegative and every Pick pivot is strictly positive.

L-6601 then supplies the decisive dual statement. If `y_0` lies both inside the rigorous uncertainty box and the finite RH-admissible cone, every allowed nonnegative scalar/PSD portfolio satisfies

\[
 \sup_{y\in C}P(y)\ge P(y_0)\ge0.
\]

Thus no positive feature-repair moat can exist on that block. Block anchors concatenate because all current rows are supported within one exact ordinate block.

## Results

### Baseline replay

- generated exact rows, including explicit matched-pole probes on failed blocks: 58,656;
- certified negative rows: 0;
- 128-bit zero-crossing rows: 78;
- exact feasible anchors at 128 bits: 51 of 65.

The tightest 128-bit interval was the full eight-node barycentric Pick row at `j=+1`:

```text
lower approximately -5.0728614513e-37
upper approximately +4.4599933003e-37
```

This was an escalation target, not a candidate.

### 192-bit escalation

The exact replay generated 7,420 rows over the fourteen escalated blocks.

- certified negative rows: 0;
- unresolved rows: 0;
- exact feasible anchors: 14 of 14;
- exact positive-definite Pick factorizations: 14 of 14;
- negative enumerated cross-Loewner minors: 0.

The former tightest row, `j=+1`, became strictly positive:

```text
lower approximately 1.1604673933650643e-42
upper approximately 1.1604673933651160e-42
```

### Global result

Combining the 51 baseline anchors with the fourteen escalated anchors gives an exact rational point in the full mixed-precision 520-feature uncertainty box and in every declared value-only RH-admissible block.

Therefore:

```text
conic separator: IMPOSSIBLE_OVER_DECLARED_VALUE_ONLY_LIBRARY
positive feature-repair moat: IMPOSSIBLE_OVER_DECLARED_VALUE_ONLY_LIBRARY
```

This rules out **all** exact nonnegative portfolios built from the declared scalar rows and all exact PSD Gram portfolios over the same-height Pick matrices—not merely the vectors tried by a numerical optimizer.

It is a rigorous negative result about this finite table. It is not evidence for RH outside the table and does not exclude:

- other heights;
- different or adaptively placed horizontal nodes;
- proof-grade derivative/jet features;
- a different entire-function or Weil family;
- a direct off-critical zero elsewhere.

## Reproduction

After obtaining either immutable certificate artifact, run:

```bash
python experiments/X-6601-arb-xi-dual-portfolio/analyze_feature_cone.py \
  path/to/certificate.json \
  --output replay.json
```

The committed compact closure ledger is:

```text
results/feature-cone-closure.json
```

The exact analyzer uses only the Python standard library.

## Failed infrastructure attempt

New automatic workflows on the X-6601 branch, including an echo-only diagnostic, failed before producing any job step or artifact on 2026-07-25. No mathematical conclusion is inferred from those failures. The complete result above uses already successful immutable PR #56 artifacts. The full-grid and targeted-finalist recipes remain available for manual dispatch.

## Strategic consequence

Do not spend further LP/SDP effort on this exact 520-feature table: L-6601 proves that a separator does not exist there. The next counterexample search must enlarge or move the primitive feature space. Highest-priority options are:

1. a new exact ordinate window chosen by independent reconnaissance;
2. adaptive horizontal nodes rather than the fixed eight-node ladder;
3. a proof-grade `F`-jet table supporting the differential and shifted-Stieltjes localizers directly;
4. a separate high-carrier region or a different finite witness route.

Any new table should run the feasible-anchor test before expensive dual optimization. A successful anchor closes the entire dual cone; failure nominates only the exact unanchored blocks for portfolio search and precision escalation.
