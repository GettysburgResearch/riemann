# X-103110 — Quarter-power owner-collapse audit

This lightweight replay authenticates the correction to the historical
quarter-power closure proposal.

It verifies:

```text
arbitrary-cutoff Boolean Vaughan identity;
exact cutoff-transfer identity;
source-blind owner-collapse amplification countermodel;
fixed-owner/support statements remain distinct from coherent physical collapse;
QPTI103112, BCI102990, and RH are not marked proved.
```

Run:

```bash
python3 experiments/X-103110-quarter-power-owner-collapse-audit/verify.py \
  --output /tmp/x103110.json
cmp /tmp/x103110.json \
  experiments/X-103110-quarter-power-owner-collapse-audit/results/verification.json
```

Retained verdict:

```text
PASS_T103110_QUARTER_POWER_OWNER_COLLAPSE_AUDIT
1326dcc1ad0146d630ee1c3ce944fe9986b96b565ee4d7d0c1ea244123916ea5
```

The replay does not prove an arithmetic physical-restriction theorem or RH.
