# Validation and publication scope

The accepting code uses Python's standard library, integer arithmetic and
Fractions. It makes no network request and imports no repository theorem.
Normal and optimized executions reproduce CHECKS.json byte for byte.

## Complete declared finite tests

- Fifteen quadratic grid/jet configurations: d=-3,-1,2,5,13, with three
  full rectangles each. Every row, evaluation point and derivative column
  is retained. The matrices have 12, 15 or 32 rows. Exact Gram determinants
  are positive and satisfy Hadamard; hashes of their full integer values
  are recorded. Eighteen actual inert-prime reductions reconstruct every
  transformed coordinate by two algebraic paths and check the complete
  normalized Gram determinant identity. This is not a large-conductor test.
- Forty exact Sylvester determinants for z^m-a, 1<=m<=8, a=-2,-1,0,1,2.
- Fifteen full rational Hermite matrices, nodes 0,...,N-1 for 2<=N<=6 and
  1<=J<=3, agree with the confluent Vandermonde formula.
- All R=1,...,32, S=1,...,10 and p=2,3,5,7,11 are checked for the floor,
  layer and polynomial valuation-template formulas and their rational
  normalized lower bound. Complete declared half-integer ramp parameters
  test the second-difference identity, including every endpoint.
- Balanced parameter checks at R=2^64,2^80,2^96,2^128 with six declared D
  values use exact root/ceiling inequalities and rational log(2) enclosures.
  These are finite checks of formulas, not a proof of all-R asymptotics.
- Full ordinary-integer divisor desieving through N=128 agrees at every
  relevant prime with the complete prime-power and lcm formulas. The exact
  rational factorial quotient is independently multiplied through N=32.
- Exact rational checks retain the continuum, integer-to-real correction,
  zero multiplicity and common-zero cancellation. Collapsed-grid, arbitrary
  slack and phase-invariance controls reject tempting source-free inferences.

Most individual predicates are repeated coordinate equalities and divisibility
checks within these few complete grids. The total in CHECKS.json is not a
count of independent mathematical results or actual L-function examples.
No L-values, zero census, infinite prime sum, numerical real-zero gap, or
native Hecke-family moment is evaluated.

## Seven actually executed corrupted optimized processes

Each altered process must return 1 at its specified mathematical gate, not
merely encounter an arbitrary crash:

| Corruption | Required rejecting gate |
| --- | --- |
| Hasse rather than ordinary derivatives | ordinary_derivatives |
| Missing factor two in Gram valuation template | valuation_template |
| Absolute rather than signed Mobius weights | primitive_integer |
| Delete prime powers above the first | primitive_integer |
| Wrong one-sided continuum | one_sided_continuum |
| Delete common-zero cancellation | common_zero_residue |
| Delete zero multiplicity | zero_multiplicity |

`python -B replay.py` authenticates all ten named payloads, reruns both
positive modes, and executes all seven controls as separate subprocesses.
A fresh ZIP extraction is replayed with the unchanged supplied PDF bound
by its optional `--pdf` argument. No timed-out execution is counted as a pass.
The original PDF is in the conversation bundle, not the Git text import.

## What has not been validated

Finite exact checking does not verify the resultant rank lemma on arbitrary
complex points, the infinite prime comparison, the analytic Laplace/Hadamard
transfer, or OPEN-PD. The manuscript proves the first three at their stated
scope; they await independent review. OPEN-PD is explicitly unproved.
There is no independent mathematical referee, second research agent, Lean
build, comparator, remote CI or repository-wide validator result here.

The source checkpoint is `ae24603c7b6b002b8e50fefb01d8ca2e12dbc3fd`, draft
PR #993. The continuation changes only this new standalone directory; the
source transcription and IMPORT.md remain unchanged. SHA256SUMS seals the
final local payload. A separate publication receipt records the actual final
commit and remote identities, rather than inserting a circular self-hash.
