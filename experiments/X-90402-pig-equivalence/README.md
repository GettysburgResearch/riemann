# X-90402 — compact innovation / PIG equivalence algebra

Status: **FINITE EXACT COEFFICIENT REGRESSION — NOT AN RH PROOF**  
Related theorem: `T-90404`

Run:

```bash
python3 experiments/X-90402-pig-equivalence/verify.py
```

Expected verdict:

```text
PASS_X_90402_PIG_EQUIVALENCE_ALGEBRA
```

The script uses exact integer/Fraction arithmetic and formal `log p` basis vectors to check through a declared finite cutoff:

1. the coefficient formula for `b_4`;
2. `1*b_4 = epsilon - 3 sum_(r>=1) delta_(4^r)`;
3. the compact-current prefix identity
   `1*q_circ = (epsilon-4 delta_4)*Lambda + 4 log(4) delta_4`;
4. the aligned filtered-Chebyshev carry formula;
5. `L_(4n,4j)(delta_4*b_4)=L_(n,j)(b_4)`.

It does not formalize the classical implication `RH => psi(x)=x+O(sqrt(x)log^2x)`, the physical block measure, `T-90302`, PIG, or RH.
