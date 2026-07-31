# X-15608 — Off-line/excess-quantum regression

This standard-library-only verifier checks the finite diagonal model behind
`L-15622`.

The retained control uses

```text
G=3, alpha=1/10, t=1/2, Gamma=1,
D=diag(29/10,29/10,13/5,1).
```

The first two coordinates form the declared near-radical packet and satisfy
`A=GI-D <= alpha`. The third coordinate is one additional direction strictly
below `t`.

Exactly,

```text
theta                  2
threshold gap eta      1/2
clipped diagonal       9/10, 9/10, 3/5, 0
clipped trace          12/5
packet requirement     9/5
clipped excess         3/5
one-mode quantum       1/2
```

Hence the extra low direction forces strict failure of the robust gate:

```text
3/5 > 1/2.
```

Run:

```bash
python3 verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
```

The experiment verifies finite rational arithmetic only. The Riemann-specific
content of `L-15622` is the localization of an off-line Xi-cardinal direction
and its asymptotic orthogonality to the exact radical packet.
