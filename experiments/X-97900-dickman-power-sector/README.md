# X-97900 — Dickman power-sector replay

The verifier checks exact source/exposure identities and performs a finite
numerical reconnaissance of the power-sector asymptotic. The analytic theorem
is proved in `L-97900/L-97901`; the finite run is not its proof.

```bash
python3 verify.py --limit 1000000 --output results/verification.json
```

Expected classification:

```text
PASS_T97900_DICKMAN_POWER_SECTOR_LOCALIZATION
```

The retained result explicitly records that full `CSHT67`, root `RBLPTE67`,
`SPCC67`, and RH are not proved.
