# Full native RH attack: a tested Euler construction, not a completed proof

This packet leaves the auxiliary graph sequence and tests a concrete candidate
for the original full arithmetic residual. **The candidate fails. RH and the
source-specific subpower upper bound remain unproved.**

- [REASSESSMENT.md](REASSESSMENT.md) records the live cross-route reading and the
  attempted end-to-end argument. Coverage is selected, not repository-wide review.
- [PROOF.md](PROOF.md) supplies the exact growing Mobius-prefix candidate, all
  three normalization conditions, and the unconditional sharp asymptotic
  `log(1+E(p_Y)) ~ 4 sqrt(Y)/log(Y)` for its COMPLETE physical norm.
- [SOURCE_LOCK.json](SOURCE_LOCK.json) pins the inspected repository sources and
  classical inputs; [VALIDATION.md](VALIDATION.md) records what was executed.

The asymptotic is a proposed component theorem with a complete paper proof.
It is not a positive RH-strength estimate, a new zero-free region, or a theorem
about the optimized residual. The old graph results and all predecessor sources
are unchanged. Ordinary PNT is used; RH is not used.

Replay the bounded algebra (standard library only):

```sh
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
sha256sum -c SHA256SUMS
```

Those commands authenticate finite coefficient identities and the sealed files.
They do not machine-prove PNT, Fourier Plancherel, or the analytic asymptotic.
No new minimum or full residual value is computed by the checker.
