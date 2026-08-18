# X-97500 — Exact raw/contracted resolvent replay

Run:

```bash
python3 verify.py
```

Expected:

```text
PASS_T97500_RAW_CONTRACTED_RESOLVENT_AND_TWO_CHANNEL_SOURCE_REPAIR
5cd6ea67db8bb335c3d349917ff2b7d739fba83a99231efac27939ae5eb3e9b0
```

The checker uses exact rational arithmetic. It proves finite algebra and
mutation firewalls only. It does not prove `NCBI67`, scalar positivity, or RH.
