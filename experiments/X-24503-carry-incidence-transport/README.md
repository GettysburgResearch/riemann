# X-24503 — Exact carry incidence-transport replay

Status: `EXACT_RATIONAL / SYNTHETIC FINITE REGRESSION`  
Issue: #245

Run

```bash
python experiments/X-24503-carry-incidence-transport/verify.py
```

The standard-library checker uses integers and `fractions.Fraction` only. It
verifies:

1. the carry second-difference identity of `L-24501`;
2. constant `b`-block endpoint-incidence transport from `L-24520`;
3. pure two-row transport between ordinary-prime endpoints;
4. the exact telescoping objective ratio `B/A`;
5. the reversed `q+1` sign and corrected `q` sign from `R-24503`;
6. termination and feasibility of the descending algorithm `L-24519`;
7. its exact triangular recurrence on randomized rational controls.

The checker validates finite algebra only. It does not evaluate logarithms,
prime-ramp asymptotics, Lagarias's imported theorem, or RH.
