# Barrier after allowing every existing ChainF50 face

This is an exact arithmetic limitation of a specified PR94 scalar return, not a zero-free theorem or a limitation on a different analytic source or detector. The executable check parses all 130 triples from pinned `ChainF50/Chain.lean`, SHA-256 `ab1fc1b2303404bf57fa2d978ea6b3d7ea3b77e689fc59ff40b50f99e8824570`.

Retain the PR94 `BoundsN` range `873/1000 < theta` and `793/1000 < h < 806/1000`, its relations `ell=11/3-4 theta`, `kappa=2 theta-1`, and its row exponent formula. Take the available return point `d=h, delta=223/500, p=1/2`. Give the scheme an optimistic enlargement: allow all 130 global triples as potential count faces, ignoring their admissibility windows; allow any real marked cap on each capped face, subject only to its necessary upper plain-length inequality; and allow the physical capacity to equal the largest unlimited conductor line among all 130 faces. Drop the positive row fee. These relaxations do not assert any new source theorem or Lean transport.

Under these rules the required row inequality already fails whenever

```
theta <= 803672422246031/919671258000000
       = 0.8738692388775632...
```

At the fixed point, the least uncapped count among all faces is the source-129 value `137478360780643/225606975000000`. The separate exact check `../2026-10-29-arvi-return/check_chain_point.py` shows that for each of the 130 faces, optimising the capped formula over all real caps with only its relaxed necessary plain-length guard has this same face's uncapped count as its infimum. This also covers the capped physical count formula because it has the same algebra with a different source triple. Lowering the uncapped face's B, as in weakC7, can only increase its count: the count denominator is independent of B and its numerator has strictly negative derivative in B. The old count is larger on `kappa > 373/500`, checked in `../2026-10-29-arvi-return/independent_obstruction.py`. Therefore the count envelope is at least the displayed source-129 value even under these enlargements.

For each physical triple `(B, Lambda)`, the actual capacity is at most `(B h-4 ell)/Lambda`. Replace it by that unlimited line and replace the count by the lower bound above. The resulting row exponent minus theta is affine in theta and h. The accompanying checker verifies that both slopes are strictly negative for every one of the 130 triples, and that at `h=806/1000` and the displayed theta every one of the 130 gaps is nonnegative, with equality only for `source_66`. Thus for the actual strict inequality `h<806/1000`, every line yields a positive gap. Even the pointwise best line fails there.

Compared with PR94's claimed `0.87387234`, this leaves at most about `3.10113e-6` improvement in the specified geometry and formulas. The previous fixed-source-64 barrier was `0.8738692733793095`; admitting all 130 physical faces improves that obstruction by about `3.45e-8`. This numerical limitation is compatible with potentially useful gains elsewhere in the `(delta,p)` domain, but those gains cannot overcome this one point without changing the count estimate, physical source face, row formula, or geometry.

Reproduce the physical calculation with:

```sh
python research/exploratory/2026-10-29-chain-face-envelope/check_physical_obstruction.py --chain /workspace/scratch/pr94-prepared/submission/src/Submissions/arvi_density/ChainF50/Chain.lean
```

The face checker and comparison are exact rational calculations, independent of floating-point scans; they are not Lean certificates. Source 66 is separately established by the existing chain under the same global hypothesis, and it dominates the source-64 unlimited line throughout the retuned physical shell `19/25 <= d <= 0.8059900001`. Actual PR94 `PhysicalSchedule` uses one globally chosen physical pair, and the `physicalB` and `physicalLambda` constants are shared with the capP count branch; using a different physical pair there requires disentangling those dependencies and rechecking all schedule and count-window certificates. A shell-dependent face envelope would require additional source transport. None of these wiring changes has been carried out here.
