# Session report — Issue #66 proof-grade Arb `xi'/xi` dual portfolios

Agent: `gpt56-06-d`  
Issue: #66  
Branch: `agent/gpt56-06-d/66-arb-xi-dual-portfolio`  
Stacked base: draft PR #56  
Date: 2026-07-25  
Status: exact finite-table obstruction; no RH counterexample candidate

## Starting hypothesis

The proof-grade Issue #39 feature table might contain no individually negative imported channel but still admit a rational conic portfolio whose shared primitive uncertainties cancel, producing a strictly negative robust endpoint and positive feature-repair moat.

The intended route was:

1. import the immutable Arb primitive table;
2. express every existing value-only `xi'/xi` localizer over one feature-ID system;
3. contract shared primitive coefficients before widening;
4. search scalar and PSD dual portfolios;
5. exact-replay every nominee;
6. promote only a strict negative surviving all logical and implementation gates.

## Artifact recovery

Two successful PR #56 workflow artifacts were recovered and bound by digest.

### Full 128-bit table

- artifact digest:
  `9811f269b4b4d0bda8f85d4ff53e3f5ba1a619e37dba5cdfb29fe924aa5216ec`;
- certificate digest:
  `10025d3c3b50b24f0b39c9981664131644fc58ad0a59fd8606f1d96d9b3e02c2`;
- exact points: 520;
- exact blocks: 65;
- primitive horizontal nodes per block: eight.

### 192-bit ambiguous-block batch

- artifact digest:
  `646ff50e6191d68700bc3bb9a2ad21010241f51ad384d9ee36078a55d6f857a3`;
- certificate digest:
  `bc9bf349864fa65257a195538404e20a9e49891d18e2e55faeb44505b85d618f`;
- original verification digest:
  `317049ea8390df76927685d4b2398e3abf6a411eebcdf81f69765b0622e9e558`;
- exact points: 112;
- exact blocks: the fourteen baseline blocks whose rational midpoint Pick matrices were too close to rank deficiency at 128 bits.

## Canonical feature semantics

At each ordinate block, one primitive coordinate is assigned to each exact real interval

\[
 R_k=\operatorname{Re}(\xi'/\xi)(1/2+x_k+iT).
\]

The coordinate is the intersection of the two PR #56 directed assemblies. Every row reuses that one feature. No repeated occurrence is treated as independent.

The current table is value-only. Jet-only differential and shifted-Stieltjes matrices are explicitly outside its feature space. Their derivative-free secant, divided-difference, barycentric Pick, ordinary Pick, and Loewner replacements are included.

## Localizer expansion

For each eight-node block, X-6601 reconstructs:

- 8 scalar rows;
- 56 pairwise A/B rows;
- 219 alternating divided-difference rows;
- 247 barycentric Pick rows;
- one full 8x8 Pick matrix whose PSD cone contains every fixed vector and every finite PSD Gram multiplier;
- 1,106 cross-Loewner minors;
- explicit matched-pole rows on rational model cells whenever the full midpoint Pick matrix is not already positive definite.

The ordinary affine row count is 530 per block and 34,450 over all 65 blocks. The Pick PSD factorization is not a finite vector sample: one exact positive-definite factorization closes every exact real fixed direction and every exact finite PSD Gram portfolio at that anchor.

## New lemma: feasible-anchor obstruction

L-6601 records the exact dual obstruction.

If one rational point `y0` lies inside the rigorous primitive enclosure and satisfies every declared scalar row and PSD matrix constraint, then every nonnegative scalar/PSD portfolio `P` obeys

\[
 \sup_C P\ge P(y_0)\ge0.
\]

Consequently, no robustly negative portfolio and no positive feature-repair moat exists on that table. This is stronger than failure of one LP or SDP search.

The block form is especially useful. Since every current row is supported at one ordinate, anchors concatenate. Any possible cross-height portfolio is also obstructed once every block is anchored.

## Baseline exact replay

The 128-bit table produced:

```text
height blocks                         65
exact rows evaluated              58,656
certified negative rows                0
zero-crossing rows                    78
exact feasible anchors                51
unanchored blocks                     14
```

The extra row count above 34,450 came from explicit matched-pole probes on the fourteen blocks where the universal Pick anchor had not yet been established.

The tightest row was the eight-node barycentric Pick row at `j=+1`:

```text
lower approximately -5.0728614513434545e-37
upper approximately +4.4599933002761695e-37
```

It was preserved as an escalation target, not called negative.

## 192-bit exact escalation

The existing PR #56 ambiguous batch covered precisely the fourteen failed blocks. X-6601 ignored its originally selected vectors and rebuilt the complete localizer library from the primitive rectangles.

Result:

```text
height blocks                         14
exact rows evaluated               7,420
certified negative rows                0
zero-crossing rows                     0
exact feasible anchors                14
negative cross-Loewner minors           0
```

The former tightest `j=+1` barycentric row became

```text
lower approximately 1.1604673933650643e-42
upper approximately 1.1604673933651160e-42
```

strictly positive by an enormous interval-separation factor relative to its 192-bit width.

## Exact global conclusion

The 51 baseline anchors and fourteen escalated anchors concatenate into one rational point inside the mixed-precision product enclosure and every declared value-only RH-admissible block.

Therefore:

```text
NO EXACT ROBUST CONIC SEPARATOR EXISTS ON THE CURRENT TABLE.
NO POSITIVE FEATURE-REPAIR MOAT EXISTS ON THE CURRENT TABLE.
```

This statement covers:

- every nonnegative rational scalar portfolio of generated rows;
- every exact fixed Pick direction;
- every barycentric or matched-pole Pick direction;
- every exact finite PSD Gram multiplier for the same-height Pick matrices;
- every cross-height aggregation of those block-supported constraints.

It is not a proof of RH, not evidence about untested heights, and not a statement about a future jet table or different node placement.

## Counterexample status

No counterexample was found. No `Z-####` candidate is allocated.

The request for a positive feature-repair moat on the current table is not merely unanswered: L-6601 plus the exact global anchor proves it is impossible. Continuing to optimize portfolios on this unchanged table would be mathematically wasted work.

## Failed infrastructure

Three new branch workflows—the full 256-bit grid, targeted barycentric finalists, and an echo-only diagnostic—failed before publishing any job step or artifact. Since even the diagnostic failed, no sign or implementation conclusion is drawn. Automatic triggers were removed from the full-grid recipe to prevent infrastructure failures from following every research commit.

The mathematical result does not depend on those failed workflows; it uses already successful immutable PR #56 artifacts.

## Files added

- `claims/lemmas/L-6601-feasible-anchor-obstructs-dual-witness.md`
- `experiments/X-6601-arb-xi-dual-portfolio/analyze_feature_cone.py`
- `experiments/X-6601-arb-xi-dual-portfolio/README.md`
- `experiments/X-6601-arb-xi-dual-portfolio/results/feature-cone-closure.json`
- `experiments/X-6601-arb-xi-dual-portfolio/results/feature-cone-192-escalation-summary.json`
- manual FLINT escalation workflows and a preserved generator
- integration patch
- this report

## Claims affected

- L-6601 — new, `PROPOSED`.
- X-6601 — exact rational replay of directed Arb artifacts; no candidate.

No parent claim is promoted.

## Main adversarial targets

1. Reconstruct every row-count formula and coefficient orientation.
2. Independently audit the rational `LDL^T` implementation and the strict-positive-pivot criterion.
3. Check all 1,106 per-block cross-Loewner index pairs and determinant signs.
4. Verify artifact and certificate digests against the GitHub Actions records.
5. Confirm that the mixed-precision product enclosure legitimately uses 128-bit boxes on 51 blocks and 192-bit boxes on fourteen blocks.
6. Attack the semantic feature-ID map for accidental duplication.
7. Confirm that every portfolio currently contemplated is block-supported and lies in the scalar/PSD dual cone covered by L-6601.
8. Preserve the exclusion of jet-only rows from the value-only table.

## Recommended next attack

The finite cone itself says what must change. Move or enlarge the primitive table before further dual optimization.

Highest-priority options:

1. proof-grade adaptive horizontal nodes around reconnaissance-nominated displacement scales;
2. a new exact ordinate window, not a denser replay of the closed window;
3. proof-grade `F` jets so the differential and shifted-Stieltjes constraints become genuine additional coordinates;
4. a second high-carrier basin or a different finite witness route.

Every new table should begin with the exact feasible-anchor test. If an anchor exists, the complete dual cone is closed immediately. Only unanchored blocks should receive LP/SDP search and precision escalation.

## Organizational improvement

Add **feasible-anchor replay before dual search** to the project protocol. Primal feasibility can rule out an entire infinite family of dual certificates with one small exact object. This is the correct complement to the uncertainty-closer role introduced by PR #50.
