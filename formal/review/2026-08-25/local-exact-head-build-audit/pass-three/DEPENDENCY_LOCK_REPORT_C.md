# Reviewer C dependency and source-lock report

- Original C head/tree: `b20ee9b3678e5d8fa32b04b156bc02cec782a97b` /
  `ed817c346294758ae1db773edba78d4527bace54`
- Repaired C head/tree: `381a5a98ade7c6bad7122e5182c2fc07332dc747` /
  `d048c21065d8f06e44a7166a426c8c0960d96117`
- Toolchain: `leanprover/lean4:v4.33.0-rc2`
- Toolchain SHA-256:
  `0d3c76ccd8772d8bcbe207241421a760312b71a6aa82f84194391fdf5cb026d6`
- Manifest SHA-256:
  `6be307e0de2294f99ce68e80903cd4cc88e77b6797c853c67be5cd9f6a1db453`
- Mathlib: `51e6992efd06126df61a496bebf8f49482a4e129`
- Zeta23: `cec57f919ccf34e5fa5372b4ba332f7c848bbb6e`

The lock files did not change and no `lake update` was run. Cache acquisition
exited 0 and restored 8,489 already-cached artifacts.

The LF-materialized external statement SHA-256 is
`2eb547a373c49f56fa4da97284534bc06ee9a71548121a2b15d337cb79832c73`.
Source-lock validation passes with 139 claims and the pinned Mathlib/Zeta23
revisions.

Verdict: `PASS`.
