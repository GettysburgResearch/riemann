# X-15107 — Certified-zero cardinal residue checker

This standard-library-only checker replays the exact finite algebra of
`L-15122` and the conservative capture bound of `L-15123`.

The retained rational control uses nodes `(-1,0,1)`, target
`p=(3/8,1/4,3/8)`, and target roots `(-1/2,1/2)`. Two selected positive Cauchy
atoms sit exactly at the target roots with masses `2` and `3`. Two residual
atoms at `-2` and `2`, each of mass `1/10`, are subtracted into the residual
source and then reconstructed exactly.

The checker verifies:

- the target interpolation polynomial and the declared simple roots;
- the selected and residual source vectors;
- the exact cardinal quadrature identity;
- the residual and complete residue weights;
- the conservative root-capture lower bounds;
- reconstruction of the full matrix from its Cauchy rays;
- the target kernel and exact positive complement `LDL^T` pivots.

Run:

```bash
python3 verify.py certificates/selected-zero-pass.json
python3 -m unittest discover -s tests -v
```

The retained control is entirely synthetic rational algebra. It contains no
zeta zero, no prime sum, no directed transcendental producer, and no RH claim.
Its purpose is to test the proof consumer that a production implementation must
feed with certified zero balls, smooth-target root intervals, and the complete
prime-side residual source.
