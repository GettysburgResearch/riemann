# Pass-three dependency lock report

All frozen sources and the combined rehearsal use the committed toolchain and
manifest without `lake update`.

- `formal/lean-toolchain` content SHA-256:
  `0d3c76ccd8772d8bcbe207241421a760312b71a6aa82f84194391fdf5cb026d6`
- `formal/lake-manifest.json` content SHA-256:
  `6be307e0de2294f99ce68e80903cd4cc88e77b6797c853c67be5cd9f6a1db453`
- Lean toolchain: `leanprover/lean4:v4.33.0-rc2`
- Locked Mathlib prefix: `51e6992e`
- Locked Zeta23 prefix: `cec57f91`

The combined run restored the committed dependency cache and explicitly built
four pinned Zeta23 recovery targets before the aggregate build. Dependency
sidecar files were checked against the green C cache and were byte-identical.

An earlier disposable run encountered a transient private-sidecar/resource
failure. It did not change the manifest or source worktree. The final exact
runner cleared dependency resolution and all downstream gates.

Verdict: `PASS`.
