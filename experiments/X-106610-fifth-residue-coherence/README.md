# X-106610 — Fifth-residue coherence replay

Run:

```bash
python3 experiments/X-106610-fifth-residue-coherence/verify.py \
  --output experiments/X-106610-fifth-residue-coherence/results/verification.json
```

The replay uses exact `Fraction` arithmetic. It checks the finite
sign-transition theorem, coherence and projective-edge inequalities, exact
\(90\%\) constants, and the \(c+\cos\) firewall. It does not evaluate Xi,
replay the fixed-order \(R_5\) theorem, or prove either analytic residue gate.
