# Cross-review light replay

Run:

```bash
python3 verify_cross_review.py
```

The replay checks only this delta packet's schemas, required verdicts, unique IDs, the exact rows-2/3 and fixed 5:3 polynomial factors, the declared Xi reserve-budget inequality, and the absence of any claim that RH is proved. It does not rerun high-zero verification, Q4 scans, Brownian campaigns, large matrix searches, or any historical heavy certificate.
