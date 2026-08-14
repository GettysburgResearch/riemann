# X-91143 — Euler shell recovery and firewalls

Replay:

```bash
python3 experiments/X-91143-euler-shell-recovery/verify.py
```

Expected verdict:

```text
PASS_EULER_SHELL_RECOVERY_AND_FIREWALL
```

The script uses standard-library exact `Fraction` arithmetic and directed
square-root/logarithm intervals for the shell-profile counterexample.  The
finite density and entropy loops are regression checks for the exact analytic
formulas in the companion claims.

It does not certify Hereditary Typed Entry, CFFP, or RH.
