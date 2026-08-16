# Exact-head review regression for PRs #519, #523 and #520

Run:

```bash
python3 verify.py --output results/verification.json
```

Expected verdict:

```text
PASS_PR519_PR523_PR520_EXACT_HEAD_REVIEW_ALGEBRA
```

Proof object:

```text
46b1e17e3e989a79fe9bd4e3d4bb3e6169672f923eb256625f7c8a6caedf0f8b
```

The checker verifies exact finite algebra:

- `G1=3K`, `W1=3F`, and `A1=3A`;
- Vaughan's `+,+,-,+` identity;
- the strict grouped coefficient `a_U(q)=sum_(d|q,d>U) mu(d)`;
- the cubic third-difference endpoint inversion;
- the phase-lock translation and critical conjugation coefficients;
- the exact counterexample to the global arbitrary-Delta envelope;
- fixed-order exponent cancellation.

It does not prove balanced Type II, growing-order Hermite estimates, the
terminal-pair theorem or RH.
