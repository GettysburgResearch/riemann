# X-91009 — Vinogradov–Korobov annular Pick-ray replay

This finite scale replay accompanies `L-91009` and `T-91004`.

It checks only elementary algebra and asymptotic scale laws:

- the square-root lower bound on the expanding disc;
- penetration of the real Pick ray beyond `w=3/4`;
- penetration of the tangent-defect variable below `t=1/4`;
- the model ratio `eta_VK(T)^(-1)/log T -> 0`;
- positivity of the Catalan background at the moving boundary;
- transfer of the annular radius into the corresponding zero-depth threshold.

It does **not** prove the classical Vinogradov–Korobov logarithmic-derivative estimate, evaluate zeta, certify the analytic transfer theorem, or prove RH.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_VK_ANNULAR_PICK_RAY
```