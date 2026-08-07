# Integration handoff — Green–dipole Skorokhod carry sharpness

Branch:

```text
agent/gpt56-pro/260-green-dipole-skorokhod
```

Issue: #260

## Review order

1. `claims/lemmas/L-26202-green-skorokhod-contact-debt.md`
2. `experiments/X-26201-green-dipole-skorokhod/verify.py`
3. `claims/lemmas/L-26201-mobius-poisson-carry-correction.md`
4. `claims/lemmas/L-26203-parabolic-green-obstacle-debt.md`
5. PR #240 `L-23820/L-23821/L-23822`
6. `claims/theorems/T-26201-green-dipole-sharpness-implies-rh.md`
7. `claims/methodology/M-26201-green-dipole-skorokhod-full-proposal.md`
8. `claims/observations/O-26201-green-skorokhod-reconnaissance.md`
9. exact certificate, result, tests, and reconnaissance JSON
10. full report

## Source boundary

The branch is stacked on PR #248's exact parabolic/divisor-gradient geometry.
It imports but does not copy PR #240's current Green neutralization and
two-moment balayage.

## Promotion boundary

Do not promote `GDS`, `CCD`, the prime-ramp asymptotic, or RH without a new
reviewed proof of the contact-cell descent. Finite double-precision rows are
reconnaissance only.
