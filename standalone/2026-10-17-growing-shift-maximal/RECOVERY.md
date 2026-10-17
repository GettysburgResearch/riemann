# Recovery checked before continuation

The two user-delivered pending packets were already recovered by PR #956 at
943d7714f81b97a75652ebc6e19990a88c917d4d. This pass did NOT create that recovery
commit, duplicate its directories, or strengthen the historical claims.

On 17 October 2026 this pass reconstructed both Git trees directly from the
mounted ZIP archives, including original manifests and publication labels:

- affine-cancellation: 11 files, tree 4af7d5a47b4e51a3414fd8aa06f8e5f2221c837e;
- mesoscopic-prime-exchange: 13 files, tree 13d3f1121d05f547e2067fe25103d4051e4b20cf.

Both identities match the published #956 recovery. The affine tree was also
read through the live GitHub Git-tree endpoint. All original theorem files
remain unchanged. The original extra recovery notice is retained on #956.

Fresh FULL ordinary and optimized Python runs were completed for BOTH exact
checkers. Each output is byte-identical to its archived RESULTS.json or
outputs/EXACT.json, respectively. The affine manifest verifier also passed.
Historical mutation and numerical reports were preserved, not relabeled as
freshly rerun. One attempted interactive process launch was unavailable in
this container; the four actual checker runs were executed as ordinary bounded
commands and completed successfully.

A newer recovery in #958 concerns different native norm-divisibility and
norm-fiber packets. It is not confused with these two ZIPs, and this pass does
not claim access to unprovided archives from other conversations.

No independent mathematical review, Lean build, or full-repository validation
is implied by archive identity and exact finite replay. The new mathematical
continuation, if published, is separately labeled in this directory.
