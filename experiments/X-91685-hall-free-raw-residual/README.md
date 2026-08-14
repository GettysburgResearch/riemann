# X-91685 — Hall-free raw-residual algebra replay

This checker authenticates the **new local composition algebra** and the hostile-leaf normalization. It does not independently reproduce the large imported directed certificates or the root interface.

## Run

```bash
cd experiments/X-91685-hall-free-raw-residual
python3 verify.py --json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_HALL_FREE_RAW_RESIDUAL_ALGEBRA
```

## What is checked

- exact current-plus-child identity on formal rational ledgers;
- inherited/frontier partition and terminal support logic;
- `D_(P61,y)=c_y` for every integer terminal endpoint `1<=y<67`;
- exact positivity of the rational theorem margins;
- 80-digit diagnostic reconstruction of the hostile leaf `(p,y)=(67,13)` in all rows `2,...,871`;
- equality of the row-66 value with the earlier joint-flow replay;
- local content hashes and dependency-lock structure.

The checker does not prove the imported global `L-91364` theorem, the PR #468 rough-reservoir identity, `NRSLI/NRCT`, the root correction bound, or RH.
