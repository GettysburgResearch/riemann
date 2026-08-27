# X-105324 — Localized temperature-flux replay

Run:

```bash
python -B experiments/X-105324-localized-temperature/verify.py \
  --output experiments/X-105324-localized-temperature/results/verification.json
```

Expected:

```text
PASS_X_105324_LOCALIZED_TEMPERATURE_FLUX
1df05430d5bb879d42e941a9fa7ee31a55c3bc752102a471c6f34e938ca2e4b0
RH_UNPROVEN
```

The replay performs 20 exact rational checks on complete polynomial windows:

- the zeroth, first and second logarithmic-derivative fluxes;
- exact local-temperature conservation in the zero-leakage global case;
- vanishing of the complete-window first-residue carrier leakage.

It does not prove a bound on an entire finite-window flux, canonical-product
passage, the Xi weighted winding budget, or RH.
