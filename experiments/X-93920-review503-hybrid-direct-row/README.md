# X-93920 — Review-503-safe anchored/Volterra direct-row regression

This lightweight exact checker validates the new successor's **interfaces and constants**:

- the mandatory negative witness `(67,15,1005,14)` remains strictly negative;
- `p_1005(14)`, `p_15(14)`, and the direct `x=2` Volterra row contribution are positive;
- `L-91763` and `T-92910` are forbidden;
- no derivative-fibre causal generator, rough-lift parent, bulk quantizer, exported child, or auxiliary port is allowed;
- ordinary `q` and `4q` are observed on one row before detail;
- small columns are retained;
- the moving-anchor, relative-mismatch, thinning, and `<3457` native-cost constants pass exact arithmetic checks;
- genealogy is frozen exactly.

It does **not** replay the 51-million-event directed Target–Lorenz campaign, the retained-cell analytic estimate, or the Mellin–Landau endpoint consumer. It does not prove RH.

```bash
python3 verify.py certificates/control.json --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
```
