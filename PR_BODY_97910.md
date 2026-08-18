## Factor-67 complete cube and two sharpened large-prime frontiers

This add-only successor is published on the current head of PR #590:

```text
publication base: 4f1283c67f0d4a4b504badd4c4113ba227521162
scientific freeze: 223f11259b3e7134f78d6492795e6e94caca8be3
```

The two intervening commits add only an archival PDF and its one-shot publisher;
they do not alter the frozen scientific input. The supplied route has been
re-identified from `97900-97902` to `97910-97912` because those identifiers were
already occupied in the live repository.

It proves the complete all-depth small-prime Euler cube positive through every
fixed cutoff

```text
Z=c (log X log log X)^2,  c<1/4,
```

rather than only `Z=(log X)^(1/4)`.

Two complementary exact reductions then survive:

1. the largest-prime owner strip `p>X exp(-H)` is negligible relative to the
   cube for every `H=o(sqrt(log X/log Z))`;
2. after separating the deterministic positive Euler main, every nonconstant
   error history with rough product at most `X^(1-delta)` is power-saving, so
   the remaining product-boundary error has child scale below `X^delta`.

The packet explicitly does not identify these two scales or intersect the two
localizations without proof. The remaining one-sided gates are `ESBLP67` and
`AFPBR67`. RH remains unproved.

PR #596 and PR #598 provide alternative open localizations of the same live
factor-67 boundary. They do not prove `ESBLP67` or `AFPBR67`, and none of these
routes revives the refuted `LAPBR67` residual-positivity mechanism.

### Replay

```bash
python3 experiments/X-97910-near-critical-factor67/verify.py
sha256sum -c T97910_FACTOR67_PRODUCT_BOUNDARY_SHA256SUMS
```

Expected:

```text
PASS_X97910_NEAR_CRITICAL_FACTOR67_ALGEBRA
```

### Publication deviations from the supplied two-route bundle

- only the independent factor-67 route is published in this PR;
- claim and experiment IDs are collision-only re-identifications;
- replay output is explicitly UTF-8/LF-stable across platforms;
- publication locks and checksums are added;
- no mathematical statement or proof prose is otherwise changed.
