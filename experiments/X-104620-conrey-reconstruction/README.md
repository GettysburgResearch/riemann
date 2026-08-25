# X-104620 — Exact Conrey variational reconstruction replay

Run:

```bash
python3 verify.py results/verification.json
```

The verifier:

1. checks the admissibility identity `phi(x)+phi(1-x)=1`;
2. evaluates `Phi_m` and `Psi_m` as affine functions of `e^2`;
3. bounds `e^2`, square roots, hyperbolic cotangents and comparison
   exponentials by rational Taylor intervals;
4. proves the four inequalities in `L-104603`.

Expected verdict:

```text
PASS_T104620_CONREY_VARIATIONAL_RECONSTRUCTION
```

The replay does not prove Conrey's analytic mean-square theorem and does not
claim RH.
