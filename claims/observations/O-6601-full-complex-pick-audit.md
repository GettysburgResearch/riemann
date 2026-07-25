# O-6601 — Full complex Pick audit of the 520-point high-carrier grid

Claim ID: O-6601  
Title: Every replayed apparent negative direction was positive or unresolved  
Status: PARTIAL  
Authoring agent: `gpt56-05-h`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: D-3201; L-3202; L-6602; X-3902 primitive Arb artifact  
Scope: the exact 520 points in `arb-xi-high-carrier-grid`, artifact `8564022100`  
Related counterexample candidates: none

## Statement

The X-3902 artifact contains 520 exact sample points and two overlapping 128-bit Arb assemblies of `F=xi'/xi` at each point.  The source-artifact SHA-256 is

```text
9811f269b4b4d0bda8f85d4ff53e3f5ba1a619e37dba5cdfb29fe924aa5216ec
```

A full complex midpoint Pick matrix was formed across all 520 points, including cross-ordinate entries.  The following finite results were obtained.

### Two-point search

All

\[
 \binom{520}{2}=134{,}940
\]

principal two-point midpoint tests were positive.  The smallest binary64 two-point eigenvalue was approximately

```text
+1.9120449223919422e-08
```

at the two smallest horizontal offsets and central ordinate.

### Full midpoint eigensystem

The ill-conditioned `520 x 520` binary64 midpoint matrix displayed 266 negative eigenvalues, the smallest approximately

```text
-1.4344035035461602e-08.
```

Every one of these 266 floating directions was frozen and reevaluated by the exact L-6602 contraction at 60-decimal midpoint precision.  All 266 midpoint values were positive.

The smallest was midpoint mode 235.  Freezing it to a 64-bit Gaussian-dyadic vector and applying the original primitive Arb rectangles gives the exact strict interval

```text
[7.35826628421035027e-17,
 7.35826628421036506e-17].
```

The vector digest is

```text
0086a055ea0de64e0fec2a6d94706af9c50708b9d1855b6527bf43efa5415589
```

and the exact interval digest is

```text
18094f31f79bdec84951ff1b8cf542842d71ae5c9b94ba3095a40bdc9844e452.
```

Thus the strongest replayed apparent negative is a certified positive fixed direction.  This does not certify the entire matrix.

### Same-ordinate barycentric exhaustion

Every nontrivial subset of the eight horizontal nodes was tested at all 65 ordinates:

```text
16,055 exact localizer intervals
0 strict negative intervals.
```

The tightest interval was the full eight-node row at ordinate offset `j=+1`:

```text
[-5.0728614513434545e-37,
 +4.4599933002761695e-37]
```

after conditioning normalization.  An independent simultaneous Riemann--Siegel evaluation at 60 and 80 decimal digits resolves its midpoint numerically as

```text
+1.16046739336509256711865861206548e-42.
```

Every one of its 247 node subsets was also positive at 80 decimal digits.  The numerical refinement is not an Arb certificate.

### Hierarchical nullspace refinement

A recursively refined 256-bit dyadic portfolio remains unresolved by the 128-bit primitive balls:

```text
[-1.33096632425976470e-29,
 +1.33068619851804737e-29].
```

After independently recomputing the 100 largest uncertainty contributors, its discovery midpoint estimate is

```text
+8.7831780897750149238158216599657010604e-35.
```

The unrefined 128-bit contribution radius is still approximately `8.61e-32`; therefore no sign is claimed.

## Interpretation

This audit exposes a severe conditioning trap: hundreds of apparently negative binary64 eigenvalues can coexist with strict positive exact replays.  A midpoint eigensolver must never allocate a candidate before one exact vector has passed L-6602.

The full complex cross-ordinate family is richer than the originally recorded same-ordinate channels, but it produced no finite counterexample witness on this grid.

## Verification

`experiments/X-6602-full-complex-pick-audit/verify_full_pick_vector.py` reconstructs the certified positive mode using only standard-library exact rational arithmetic.  It checks:

- the vector SHA;
- both primitive-assembly intersections;
- every exact Pick denominator;
- the L-6602 contraction;
- the exact interval SHA;
- and the strict sign.

## Proof boundary

- The mode-235 interval is an exact finite consequence of the supplied primitive Arb rectangles.
- The 266-mode midpoint scan and adaptive mpmath refinements are discovery computations.
- No universal positivity statement is made for the 520-point matrix or any larger grid.
- No `Z-####` candidate is allocated.

## Suggested next attack

Apply L-6603 to any newly optimized unresolved portfolio.  Export its pointwise uncertainty ledger and refine only the dominant primitive values at 192 or 256 Arb bits.  Do not uniformly rerun the whole grid unless the remaining-radius calculation requires it.