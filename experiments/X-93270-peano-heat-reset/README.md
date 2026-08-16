# X-93270 Peano/heat reset

Lightweight exact regression for the 93270 research-reset packet.

It checks:

1. the Peano curvature polynomial and double Mellin zero;
2. the complete factor-64 piecewise expansion;
3. exact nonnegativity certificates for every support cell;
4. the positive logarithmic convolution constant;
5. the centered-cubic positive Mellin smoothing identity;
6. the First-Hermite Gaussian Fourier polynomial;
7. real-axis noncancellation conditions;
8. the positive-source curvature countermodel;
9. the absolute Gaussian depth firewall;
10. hostile mutations.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_93270_PEANO_HEAT_RESET
```

The replay proves finite algebra only. It does not prove `SID_0`, `SID_H`, the analytic RH equivalences, or RH.
