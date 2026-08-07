# X-15109 — Certified-zero frame plus complete residual checker

This standard-library-only checker replays the direct noncircular finite theorem
`L-15125/T-15108`.

The retained rational control uses:

```text
nodes                         (-1,0,1)
target                        (3/8,1/4,3/8)
selected Cauchy atoms         mass 2 at -1/2, mass 3 at 1/2
complete residual atoms       mass 1/10 at -2 and 2
metric                        I
selected frame floor g        15
selected residual ratio rho   0
complete residual radius      1/4
```

The checker verifies:

- exact positivity of the selected Cauchy frame above `g M` on `p^perp`;
- the coordinate-relative selected target residual;
- both LMIs `omega M +/- R >= 0` for the complete target-pinned residual;
- the strict scalar comparison `rho+omega<g`;
- the exact target kernel and final positive complement pivots.

Run:

```bash
python3 verify.py certificates/synthetic-pass.json
python3 -m unittest discover -s tests -v
```

The control is synthetic rational algebra. It contains no zeta ordinate,
completed-`Xi` evaluation, prime stream, or RH claim. A production producer must
supply the complete selected-zero Cauchy frame and the residual matrix obtained
from the full polar, archimedean, and all-prime-power source.
