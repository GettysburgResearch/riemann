# X-99700 — Adaptive logarithmic-owner hierarchy replay

Run:

```bash
python3 verify.py --output results/verification.json
```

Expected:

```text
PASS_T99700_ADAPTIVE_LOG_OWNER_HIERARCHY
a83e49b28ba44fec4bdf51581f4a2158d6525d056d039ab116439d139b6b9cff
```

The replay checks:

- the exact 5:3 unsieved completion `a=q*1`;
- 3,500 generalized-von-Mangoldt nonnegativity fixtures;
- 3,500 exact identities `q*ell_k=a*Lambda_k`;
- fixed-order duplicate-67 counterexamples for grades 1 through 6;
- 10,000 exact `beta*g=epsilon` convolution values;
- 9,999 logarithmic-owner and minus-one eigenfunction identities;
- zero owner variance on 6,082 squarefree native histories;
- positive owner variance where the duplicate-67 exponent creates genuine mixing.

The replay deliberately records:

```text
fixed_order_closure_proved=false
phase_adaptive_carleson_proved=false
rh_established=false
```
