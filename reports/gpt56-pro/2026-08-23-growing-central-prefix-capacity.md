# Growing central-prefix capacity exclusion in the Xi derivative tail

Date: 2026-08-23  
Workspace: PR #729  
Scientific status: **RH unproved**

## Quantitative compact-scale theorem

The real-saddle law gives

\[
E|U/\omega_r-1|=O((r\omega_r)^{-1/2}).
\]

Therefore normalized odd/even Xi derivatives and their first two derivatives
are uniformly trigonometric on fixed-height strips of rescaled real length
`Y_r=o(sqrt(r omega_r))`. Every critical cell in such a strip is real and
simple, and its scaled residue is `-1+o(1)`.

## Tail capacity margin

The tangent and cotangent source measures have reciprocal-square atoms. After
deleting the first `J`, selecting `k` consecutive tail atoms and evaluating
the Vandermonde determinant gives

\[
\lambda_{\min}(R_{k,J}^{(a)})
\ge c_{k,a}J^{-3k(k-1)-2-2a}.
\]

A common exponent for both Stieltjes blocks is

\[
d_k=3k(k-1)+4.
\]

## Mesoscopic exclusion

For any

\[
0<\gamma_k<{1\over2(3k(k-1)+5)},
\]

put `J_r=floor(r^gamma_k)`. The normalized source and actual-prefix errors are
smaller than the model tail eigenvalue. Hence

\[
C_{k,r,J_r}^{(a)}<A_{k,r}^{(a)}
\]

for both blocks and all sufficiently high derivatives.

A fixed order capacity failure must therefore escape beyond a polynomially
growing central prefix. It cannot be caused by any fixed or sufficiently slow
growing collection of central trigonometric cells.

## Remaining obstruction

The theorem does not control the omitted critical tail. An abstract exact
matrix separator shows that a safe prefix can coexist with an overfilling
remote tail. The next analytic target is therefore a tail comparison, not more
local critical-cell analysis.

## Replay

```text
PASS_X_105390_GROWING_PREFIX_CAPACITY
200 exact rational checks
```

The replay verifies the reciprocal-square Gram determinants and exponent
balance. It does not replay the Xi analytic estimates or prove complete
capacity.

## Publication correction

The compact-cell theorem used here is the corrected `L-105387`; the malformed
`L-105386` draft is non-normative.
