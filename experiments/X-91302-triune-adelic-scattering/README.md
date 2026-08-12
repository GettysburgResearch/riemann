# X-91302 — Triune Adelic Scattering finite-algebra replay

This standard-library/SymPy replay checks only exact algebraic components of
the proposal:

1. the phase-locked `Q_*` local factorization;
2. the period-16 finite-DFT eigenpacket and four moments;
3. the Cayley Schur/positive-real congruence;
4. a finite conservative-colligation optical identity;
5. a finite resolvent/DtN identity;
6. the log-odds Sturm–Liouville equation and first-order flux equations;
7. the Brownian two-copy symmetrization identity;
8. an exact PR #398-style control with a negative two-point target Pick
   determinant.

It does not evaluate zeta and does not prove `AOT_a`, innerness, the renewal
integral, or RH.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```
