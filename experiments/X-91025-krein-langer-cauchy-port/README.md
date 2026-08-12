# X-91025 — Kreĭn–Langer Cauchy port decomposition

This exact finite replay checks:

- the product rule `K_(FG)=K_F+F conj(F) K_G`;
- the complete source = critical + stable + zero-port identity;
- the simple crossed-pole rank-one formula;
- the finite Takenaka–Malmquist port expansion;
- the one-pole control in which a positive source kernel coexists with a
  nonzero pole port and a cancelling negative critical kernel.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_KREIN_LANGER_CAUCHY_PORT_DECOMPOSITION
```

The replay proves finite rational-complex algebra only. It does not certify the
infinite xi Blaschke product, identify the arithmetic Hankel Stinespring kernel,
remove the zero ports, or prove RH.
