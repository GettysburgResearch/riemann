# T-97200 publication recovery handoff

```text
base PR:       #564
base branch:   research/gpt56-pro/97120-single-scalar-parity-julia-hardening
base SHA:      c74fe9bd7fd284718f4dcef8328af07e553d9d90
head branch:   research/gpt56-pro/97200-parity-covariant-atomwise-recovery
comparison:    PR #559 @ 88d97adef8a42c5baf2f52c2c259a4ef536bdfdd
binding audit: PR #561 @ db9bdc63c855c6ddf664b763d748f8155a6a2c67
```

The missing earlier publication is replaced by an add-only recovery. It makes
one exact correction to `L-97001.7`: the terminal owner must carry the complete
rough-history channel swap. It then records the strongest honest source-complete
successor, `GPHT*`, and connects it to PR #564's `TFPE/ACBI` frontier.

The packet does not claim a proof of `GPHT*`, `TFPE`, `ACBI`, scalar positivity,
or RH.
