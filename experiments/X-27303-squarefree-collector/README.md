# X-27303 — Squarefree composite collector algebra

This standard-library checker validates the exact finite identities in
`L-27304`.

Run:

```bash
python verify.py --self-test --output results/exact-verification.json
```

The retained control uses the collector

```text
A=30=2*3*5,
B=43,
t=7/5.
```

It verifies:

- response `-t` on prime rows `2,3,5`;
- response `+t` on prime row `43`;
- zero response on every proper prime power through `43`;
- total prime-incidence compression `-2t`;
- the formal objective ratio `43/30`;
- five fail-closed mutations.

Retained verdict:

```text
PASS_EXACT_SQUAREFREE_COLLECTOR_ALGEBRA
```

Proof-object SHA-256:

```text
05097e2a74e36a917feb7911407cb30485c9b14a1ab0f497346973254ea11c03
```

This is exact finite algebra. It does not prove the all-scale Squarefree
Collector Lift or RH.
