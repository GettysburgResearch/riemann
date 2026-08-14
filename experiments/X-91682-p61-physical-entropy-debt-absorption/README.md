# X-91682 — `P_61` physical-entropy debt absorption

This replay supports `L-91682`.

It checks, with exact `Fraction` arithmetic and outward rational square-root/logarithm enclosures:

- a nine-prime-power lower packet proving `R(67)>23/2`;
- `sqrt(41/67)<4/5`, `sqrt(67)<33/4`, and `log(67)<9/2`;
- the exact positive derivative margin `1402/5025`;
- the complete-block declared-score coefficient `4/3`;
- the Boolean `P_61` entropy-density classification and von-Mangoldt domination through `n=4489`.

Run:

```bash
cd experiments/X-91682-p61-physical-entropy-debt-absorption
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_P61_PHYSICAL_ENTROPY_DEBT_ABSORPTION
```

The replay certifies the finite and scalar gates. It uses, but does not re-prove, the published explicit Chebyshev bound `psi(x)>=0.9x` for `x>=41`. It does not certify the target/row determinants, the finite causal profile corridor, the root equality realization, or RH.
