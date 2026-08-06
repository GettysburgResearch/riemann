# X-21501 — Exact finite prime-pair Gram energy

This experiment is the finite algebra consumer for `L-21502`.

It verifies, with Python integers and `fractions.Fraction`, that a compact
piecewise-constant window and finitely many weighted logarithmic atoms satisfy

```text
integral |sum a_n G(x-u_n)|^2 dx
=
sum_(m,n) a_m a_n integral G(x-u_m)G(x-u_n) dx.
```

The checker reconstructs:

- every shifted-overlap kernel entry;
- the direct piecewise signal energy;
- the pairwise Gram energy;
- diagonal and off-diagonal contributions;
- one canonical proof-object digest.

The retained synthetic control is

```text
kernel = [[2,   1/2,    0],
          [1/2,   2, -1/2],
          [0,   -1/2,    2]]

energy       29
diagonal     28
off-diagonal  1
```

Proof-object SHA-256:

```text
75fb476e2abec4ea872e01069e6944781dc0e949d7f048c75dc17bc27dca6834
```

Seven central and mutation tests are committed.

## Reproduction

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

## Production boundary

This control uses rational synthetic atom locations. A production block for the
actual `L-21501` window must add:

1. a complete prime-power manifest;
2. directed enclosures for every `log n` location;
3. exact piecewise-cubic integration for the triangular window;
4. source and manifest digests;
5. a scale sequence used to test candidate global energy inequalities.

A finite block, however large, does not prove the subexponential cofinal bound
of `T-21501`.
