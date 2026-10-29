# Combining two source faces without losing uniformity

Status: proposed source-interface lemma, unreviewed. No new zero-free region is proved. The external source claims below have not been independently reviewed or rebuilt.

Exact sources: `GTimG/QuasiRiemannTracker` PR [#93](https://github.com/GTimG/QuasiRiemannTracker/pull/93), head `70c4d642c4c6263a09bf0f3930a74e2aa7c99f00`, and PR [#94](https://github.com/GTimG/QuasiRiemannTracker/pull/94), head `e5a82f72d8ff39a3cc1ad044e6acd727e77a3fc4`. At these heads the shared interface is `QRH.Record1252270103Source.GlobalSource` in Collet's `Record1252270103Source/Core/Contract.lean`, with quantifier order in `Record12518109Existence/UniformSource.lean` and the literal estimate in `Record12518109Source/InitialMoment.lean`. This note uses those exact contracts as hypotheses, not a blanket claim that the corresponding submitted proofs are correct.

## Domain geometry

Write `G(B,lambda,c)` for a global face. For nonnegative `m1,m2,s` and `lambda`, its admitted domain is exactly

```
s <= c M,       m1 + m2 + lambda s <= B M.
```

This is `globalFace_admissible_iff` in the cited source, including the implied individual plain bounds. For two faces with the same cap and nonnegative slopes, their union is the exact piecewise-affine region

```
s <= c M,       m1 + m2 <= max(B1 M-lambda1 s, B2 M-lambda2 s).
```

This equality is elementary and requires no convexification. In particular any convex-combination face `G(t B1+(1-t) B2, t lambda1+(1-t) lambda2,c)`, `0<=t<=1`, lies inside the union. It need not be a subface of either original face globally.

## Literal uniformity interface

Assume `G(B1,lambda1,c)` and `G(B2,lambda2,c)`, each in the exact `UniformUnitFaceSource` sense and on the same character, root, coefficient and profile objects. The source bound extends to the union above with the original quantifier order:

1. For fixed `epsilon>0`, obtain each early mesh and take their minimum before choosing any finite slot type or moving data. The source's `UnitFaceSource.mono_mesh` supplies both bounds on that mesh.
2. For each fixed ambient slot type, ray data, profile window, characters and fixed masks, obtain each source's degree, finite seminorm-control set, positive constant and eventual threshold. Choose the maximum degree, the union of the two finite control sets, the maximum of the two constants, and intersect the two eventual ranges. The source's profile control is nonnegative and monotone under inclusion; the diagonal control is nonnegative, and the height base is at least one. Thus each estimate has the common enlarged right-hand side.
3. Only after these fixed choices are made, examine the live `M,m1,m2,s`. For a point in the union, at least one of the two original admissibility inequalities holds; invoke that original source bound at that point. The selection of the bound is per live point, with no change to the slot dictionary, masks, profiles or energy.

This proves the union statement and the convex-combination corollary from the two hypotheses. It is a paper-level derivation from the cited interface, not a Lean compilation or independent verification of either source. All threshold and constants may still depend on the fixed data in precisely the source's permitted way.

## Proposed PR93/PR94 splice

Under their shared hypothesis `51/100 <= HeckeZeroSupremum.beta`, PR93 and PR94 supply the following claimed count faces, each with cap `1/10`:

```
PR93: (B,lambda) = (19452098647453/20000000000000, 4230401/2000000)
PR94: (B,lambda) = (96232839/100000000,             3853/2000)
```

The PR93 affine budget is larger for `0<=s/M<205530847453/3774010000000 = 0.0544595397078969...`; PR94 is larger above that crossing. Both live in the original domain `0<=s/M<=1/10`. The midpoint face, supplied by the preceding union argument but by neither global inclusion alone, has

```
(B,lambda) = (38698666447453/40000000000000, 8083401/4000000).
```

Likewise, the claimed physical faces with cap `1/10` are

```
PR93: (B,lambda) = (3945996453113/4000000000000, 4603201/2000000)
PR94: (B,lambda) = (49283557/50000000,           4503/2000),
```

with crossing `3311893113/200402000000 = 0.0165262478069081...`. A midpoint face has `(B,lambda) = (7888681013113/8000000000000, 9106201/4000000)`.

These faces cross, so neither original full global domain contains the other. A new return should keep each relevant physical and count window in whichever original face is valid; it may also choose any convex-combination face. In particular, a source-union result by itself does not bound the nonprincipal return, establish a better exponent, or justify replacing a restricted marked-count theorem with a broader one. Full admission guards, source identities and a rigorous continuum return certificate must still be checked. Exploratory numerical comparisons performed independently so far have not shown a meaningful improvement at the sampled bottleneck.
