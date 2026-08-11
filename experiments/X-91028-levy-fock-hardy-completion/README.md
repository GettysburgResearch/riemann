# X-91028 — Lévy–Fock–Hardy completion regression

This finite replay supports `L-91030`–`L-91033`, `T-91007`, and `R-91007`,
with main's `L-91028`, `L-91029`, and `T-91006` retained as upstream local
inputs.

It checks:

- the exact causal spectral-factor identity of `L-91026`;
- scale covariance `Psi_a(u)=Psi_1(u/a)`;
- the exact admissibility constant `(15/16) log 2`;
- the one-particle Fock identity `inner(v_(a,s),v_(a,t))=log Q_a(s+conj(t))` on a finite prime-power model;
- the radial Fock cocycle;
- the compound-Poisson boundary characteristic function;
- positivity of a finite coherent-state Fock Gram;
- positivity of a synthetic RH-side screw/wavelet Gram;
- equality of its diagonal with the one-Weil-square Cauchy residual;
- the removable bridge value `sqrt(378)/(16a)`;
- a finite polarization firewall showing that positive diagonal entries do not imply matrix positivity.

The replay uses synthetic real zero ordinates and finite prime-power truncations.  It does **not** evaluate the actual zeta screw Gram, prove the weighted form-core theorem, construct the conservative Fock/Hardy colligation, establish RH, or transfer any upstream Lean status.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_LEVY_FOCK_HARDY_COMPLETION
```
