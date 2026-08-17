# T-97200 publication recovery

This packet repairs the missing publication reported after PR #559 and records the
strongest statement that survives the parity audit in PR #561 and the scalar
hardening in PR #564.

```text
base PR:       #564
base SHA:      c74fe9bd7fd284718f4dcef8328af07e553d9d90
compared PR:   #559 @ 88d97adef8a42c5baf2f52c2c259a4ef536bdfdd
binding audit: #561 @ db9bdc63c855c6ddf664b763d748f8155a6a2c67
branch:        research/gpt56-pro/97200-parity-covariant-atomwise-recovery
```

The load-bearing correction is exact: rough placement preserves activation and
coefficient magnitude but contributes one channel swap per rough prime. Thus the
atomwise equality in `L-97001.7` must retain the cumulative history parity.

The packet does **not** claim unconditional scalar positivity or RH. It replaces
the invalid leafwise promotion with one source-complete finite-dimensional
producer, `GPHT*`, and records the equivalent all-depth scalar frontier from PR
#564 (`TFPE/ACBI`).
