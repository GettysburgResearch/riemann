# M-98070 — Hostile replay and publication protocol

1. Freeze PR #608 at `f362acf56bbbbd183976b6377fbe883193886e1a` and tree `33387b767da8a6c69d824f5bfee33c864d9cc299`.
2. Reject namespace `98060`; GitHub branch search confirms
   `agent/98060-curvature-cutoff-coboundary`.
3. Use collision-safe namespace `98070`.
4. Require exact replay plus mutation controls before publication.
5. Treat the legacy C++ `10^8` result as quarantined and incompatible with the
   current scanner unless its semantics are independently reconstructed and
   the full range is rerun.
6. Do not claim a successor PR exists until GitHub readback shows the new commit
   and PR.
7. Require `sha256sum -c T98070_CONTENT_SHA256SUMS`.
8. Require exact path/mode match against `T98070_PATH_MODE_MANIFEST.tsv`.
9. RH status must remain `UNPROVEN`.
