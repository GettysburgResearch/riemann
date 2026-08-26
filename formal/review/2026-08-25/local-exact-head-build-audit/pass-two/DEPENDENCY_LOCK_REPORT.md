# Pass-two dependency lock report

All pass-two source and diagnostic work uses the committed toolchain and manifest inherited from the exact bootstrap base.

| Item | Committed value |
|---|---|
| bootstrap/main base | `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f` |
| `formal/lean-toolchain` | `leanprover/lean4:v4.33.0-rc2` |
| committed toolchain content SHA-256 | `0d3c76ccd8772d8bcbe207241421a760312b71a6aa82f84194391fdf5cb026d6` |
| committed `formal/lake-manifest.json` content SHA-256 | `6be307e0de2294f99ce68e80903cd4cc88e77b6797c853c67be5cd9f6a1db453` |
| Mathlib revision | `51e6992efd06126df61a496bebf8f49482a4e129` |
| Zeta23 revision | `cec57f919ccf34e5fa5372b4ba332f7c848bbb6e` |

The remaining eight manifest package revisions also match the pass-one lock report. No source repair changes `formal/lean-toolchain` or `formal/lake-manifest.json`, and no `lake update` was run. Dependency cache access was serialized where it could mutate the shared cache. Windows CRLF checkout hashes are not substituted for committed Git-blob hashes.

Reviewer A remote `ae0887b8125601c98dc809cffe01c7f1c78bb998` and Reviewer B remote `6d42bbc31c81e7d6a03909e205b56f30f6f7b49a` retain these exact locks. Reviewer C remains at remote `b20ee9b3678e5d8fa32b04b156bc02cec782a97b`; its unpushed advisory work also leaves both lock files untouched.
