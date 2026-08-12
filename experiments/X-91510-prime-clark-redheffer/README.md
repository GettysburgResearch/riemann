# X-91510 — Prime Clark–Redheffer replay

This finite replay supports `L-91510`, `L-91511`, and the normal-form part of
`T-91510`.

It checks:

- the local Euler Julia identity `|m|^2+|d|^2=1`;
- exact equality between Julia detail energy and parity-Cayley dissipation;
- the Redheffer / hyperbolic-addition formula for a finite product;
- the coefficient-one cascade defect telescope;
- positivity of a finite Herglotz kernel at four interior nodes;
- exact resonance return at `z=1`, where every local detail vanishes and the
  transmitted product remains one.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_PRIME_CLARK_REDHEFFER
```

Selected values:

```text
max local Julia error             1.11e-15
max dissipation error             1.11e-15
max Redheffer error               4.45e-16
max cascade telescope error       2.01e-15
Herglotz kernel minimum eigenvalue 9.354e-4
```

The replay proves only finite algebra and numerical kernel positivity for the
selected factors. It does not prove the completed gamma/pole interconnection,
PDWT, CPPD, or RH.
