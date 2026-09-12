# Sharp nonlocal energy: remove optimization ambiguity, not the RH premise

**PROPOSED component proofs; independent mathematical/code review required.**
RH and the native dimension-asymptotic upper bound remain open.

Read [PROOF.md](PROOF.md), especially Sections 2, 4--6 and 8. This is a new,
add-only continuation of the similarity-energy packet #881, frozen at
`ab663f7d8020a62e1d8eedaf7d963d0eca3efe50`.

For the unchanged theta centered antiderivative K, the proposed sharp identity is

    inf_(S bounded invertible) ||SKS^-1||_HS^2 = mu2 + 8 Delta_Xi.

The proof uses classical compact triangularization, retaining continuous nest
directions, all nonzero multiplicities, and quasinilpotent energy. Its similarities
need not converge or have uniformly bounded condition numbers. This removes
possible extra requirements beyond RH, but DOES NOT evaluate the right side.

The COMPLETE finite-block energy includes A, both coupling Grams BB* and C*C,
and the remaining block's full HS norm. It is geodesically convex. Adding
`lambda Tr(G+G^-1-2I)` makes it coercive and strictly geodesically convex, hence
uniquely minimized. The manuscript gives a global gradient-residual bracket
for this finite minimum, computable without a matrix square root once its
complete primitive matrix data are enclosed.

Take the first d orthonormal theta polynomials and lambda=2^-d. Their unique
regularized minima form one decreasing source-defined sequence m_d with

    m_d -> mu2 + 8 Delta_Xi.

The open task is m_d->mu2. A finite optimizer's stopping error is NOT its error
from the infinite limit. No new complete theta-energy integral, native minimizing
matrix, dimension rate, or numerical zero is certified in this packet.

Exact controls include full/complement block identities, geodesic derivatives,
strong-convexity constants, global scalar optimizer brackets, finite nest scaling,
and a COMPLETE continuous Volterra kernel calculation. A normal real matrix
with eigenvalues off the imaginary axis prevents conflating normality with RH.

## Replay

From this directory, with Python 3 and no third-party package:

```sh
python -I -S -B check.py --check results.json
python -I -S -B -O check.py --check results.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

All accepting decisions regenerate the bounded result, use exact rational
arithmetic and strict typed JSON, and authenticate the local packet inventory.
They do not prove the infinite theorems or authenticate a freshly computed theta
primitive. A resealed missing-coupling or gradient mutation is rejected by
separate exact matrix formulas, not only by checksums.

See [VALIDATION.md](VALIDATION.md) for precisely executed scopes and omissions,
and [SOURCES.json](SOURCES.json) for frozen sources and reading depths.
Do not promote this draft into canonical mathematics merely because its tests pass.
