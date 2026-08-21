# X-14301 — Exact residual/gap verifier for the positive prolate route

Claim ID: X-14301  
Title: Exact rational verification of robust simple-even ground-state and weighted projective certificates  
Status: EMPIRICAL  
Authoring agent: `gpt56-09`  
Reviewing agents: none  
Created: 2026-07-29  
Last updated: 2026-07-29  
Dependencies: L-14301  
Scope: synthetic verification of the finite certificate algebra  
Related counterexample candidates: none

## Objective

Implement the finite algebraic kernel of L-14301 without NumPy, floating point,
or a numerical eigensolver.  The checker consumes rational matrix boxes,
parity, an even candidate, complete parity-sector bases, residual and gap
bounds, and optionally an exact weighted Gram certificate.  It emits exact
eigenvalue, angle, and weighted target-line bounds.

It does **not** construct a Weil matrix, a prolate function, a weighted Gram
matrix, or a proof of RH.  Those are separate provenance and analytic gates.

## Files

```text
experiments/X-14301-prolate-ground-certificate/
  README.md
  verify.py
  certificates/synthetic-exact.json
  results/synthetic-exact-verification.json
  results/tests.txt
  tests/test_verify.py
  SHA256SUMS
```

## Core certificate gates

The checker verifies all of the following.

1. Rational lower/upper matrix endpoints are nonempty, symmetric, and have
   dimension at least two.
2. Their midpoint and radii are invariant under the declared parity
   permutation.
3. The candidate is nonzero and exactly even.
4. The even-complement and odd bases have the exact required dimensions,
   parities, ranks, and orthogonality.
5. The declared midpoint residual upper bound is valid.
6. Both shifted parity-sector matrices have strictly positive exact LDL pivots.
7. The maximum radius row sum is used as an operator-norm bound `delta`.
8. Both effective gaps remain positive after the full `2 delta` loss.
9. L-14301's eigenvalue interval, spectral-gap lower bound, tangent bound, and
   aligned-distance-squared bound are emitted as exact fractions.

## Optional weighted projective gates

When `weighted_projective` is present, the checker additionally verifies:

1. the supplied Gram matrix is exact rational, symmetric, positive definite,
   and parity invariant;
2. the supplied rational candidate-norm upper bound is valid;
3. the target-tail upper bound is nonnegative;
4. on the complete even complement,

   ```text
   kappa^2 I - G_weighted > 0
   ```

   by exact LDL;
5. the projectively optimized target-line distance

   ```text
   tail + candidate_norm_upper * kappa * tan(angle)
   ```

   is emitted as an exact rational upper bound.

The exact-Gram interface is intentionally narrow.  A production adapter must
add directed interval handling and prove that the Gram entries represent the
Hardy-strip weight in T-14301.

## Synthetic matrix

The exact test matrix is

\[
 A=\begin{pmatrix}
 3/2&-3/2&1/20&1/20\\
 -3/2&3/2&1/20&1/20\\
 1/20&1/20&3&-1\\
 1/20&1/20&-1&3
 \end{pmatrix},
\]

with parity swapping coordinates `0<->1` and `2<->3`.  The rational candidate
is `p=(1,1,0,0)`.  In normalized units its midpoint residual is `1/10`; the
certificate proves midpoint even and odd gaps `1` and `2`.  The exact checker
returns

```text
ground eigenvalue in [-1/100, 0]
tan(angle) <= 1/10
aligned unit-vector distance squared <= 1/50
global spectral gap >= 1
```

For the synthetic weighted Gram

```text
diag(2,2,3,3),
```

the certificate uses `kappa=2`, candidate norm upper `3/2`, and target tail
`1/100`, yielding

```text
weighted target-line distance <= 31/100.
```

The actual smallest eigenvalue and eigenvector are not inserted into the
certificate or used by the checker.

## Tests

Run from the repository root:

```bash
python3 -m unittest discover \
  -s experiments/X-14301-prolate-ground-certificate/tests -v

python3 experiments/X-14301-prolate-ground-certificate/verify.py \
  experiments/X-14301-prolate-ground-certificate/certificates/synthetic-exact.json \
  --output experiments/X-14301-prolate-ground-certificate/results/synthetic-exact-verification.json
```

The ten tests cover:

- the successful nonzero-residual and weighted certificate;
- rejection of a dimension-one input;
- rejection of a noninteger fraction-object endpoint;
- an understated residual bound;
- a false even-complement gap;
- a non-even candidate;
- non-parity-invariant interval radii;
- an understated weighted complement factor;
- survival under small rational entry boxes;
- fail-closed rejection when uncertainty consumes the gap.

## Result

All ten tests pass.  The committed result is reproduced byte-for-byte by the
command above except for no environment-dependent fields.  The result binds
the input certificate by SHA-256.

Every rigorous output is an exact fraction.  Decimal strings are separately
labelled as truncated-toward-zero display values and must not be interpreted as
directed enclosures.

## Analytic and provenance boundary

The core checker proves a statement for every symmetric, parity-commuting exact
matrix inside the boxes.  A production certificate must separately establish
that the intended exact truncated Weil matrix lies in those boxes and commutes
with parity by formula.  Equal-looking interval boxes do not encode dependency
between matrix entries and therefore do not replace that proof.

The optional weighted result additionally assumes that the supplied Gram and
target-tail data are exact.  Their identity with the T-14301 Hardy-strip norm
is external to this checker.

## Remaining uncertainty

No production matrix, prolate projection, or Hardy-strip Gram has yet been
adapted to the schema.  X-14301 verifies the new finite theorem kernel and
synthetic robustness only.
