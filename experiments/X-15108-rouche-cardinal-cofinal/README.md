# X-15108 — Rouché--cardinal finite-gate checker

This standard-library-only checker consumes the rational endpoint ledger of
`L-15124/T-15107`.

It verifies, for every paired target root and certified line zero:

- a strict Rouché boundary moat;
- a positive real-axis derivative floor;
- the induced node-coordinate displacement radius;
- lower and upper phase-mass bounds;
- a complete nonnegative cardinal-derivative matrix;
- a complete residual-residue radius;
- the strict positive arithmetic residue margin at boundary scalar `c=0`.

The retained synthetic control certifies

```text
Rouché slacks              9/10, 9/10
node displacements         1/100, 1/100
normalized loss            3/125, 19/1000
residue margins            244/125, 2943/1000
verdict                    CERTIFIED_ROUCHE_CARDINAL_ARITHMETIC_COMPLETION
```

Run:

```bash
python3 verify.py certificates/synthetic-pass.json
python3 -m unittest discover -s tests -v
```

The certificate is synthetic rational algebra. It contains no zeta ordinate,
completed-`Xi` ball, prime sum, or RH claim. Production transcendental backends
must emit the directed rational bounds consumed by this checker.
