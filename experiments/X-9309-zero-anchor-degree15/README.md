# X-9309 — Zero-anchor degree-15 direct-xi decision

This experiment adjoins the exact critical-line node

```text
x = 0,
u = x^2 = 0
```

to PR #103's sixteen-node direct-completed-xi table at the exact ordinate

```text
20225875608343133989267 / 2^32
```

(the retained atomized minimum at shift `483/1024`).

## Mathematical reduction

The old table has directed response moments

```text
a_0,...,a_14
```

from PR #112. L-9311 proves that the zero-anchored moments satisfy

```text
b_(k+1) = a_k,  0 <= k <= 14.
```

Only `b_0` is new. It is the directed response-`1` barycentric contraction on
all seventeen nodes.

For degree at most 15, the full half-line nonnegative response cone is decided
by

```text
H0 = (b_(i+j))     0 <= i,j <= 7
H1 = (b_(i+j+1))   0 <= i,j <= 7.
```

The second matrix is exactly the already-certified old degree-14 `H0`. The
first has the block form

```text
[ b0  v^T ]
[ v    A  ]
```

and is decided by the Schur threshold

```text
theta = v^T A^-1 v.
```

If `b0 < theta`, the exact polynomial

```text
q(y) = 1 - (A^-1 v)_0 y - ... - (A^-1 v)_6 y^7
```

gives the finite nonnegative response witness `P=q^2`.

## Proof-producing pipeline

1. Generate the reviewed PR #103 direct-xi source at the exact ordinate.
2. Apply a guarded patch that emits only `x=0`.
3. Evaluate at 512 and 640 bits with FLINT/Arb.
4. Require the 640-bit rectangle to be contained in the 512-bit rectangle.
5. Require the critical-line modulus-square lower endpoint to be positive.
6. Reuse the exact atomized count windows and sixteen old point rectangles.
7. Enclose every logarithm with an exact rational positive-tail series.
8. Accumulate the extremely ill-conditioned `b0` contraction with directed
   finite-decimal arithmetic.
9. Build exact rational midpoint and radius Hankel matrices.
10. Either certify a negative Schur polynomial or prove both matrices positive
    with exact rational LDL and a complete interval-box moat.

## Expected numerical scale

Ordinary 200-digit reconnaissance, which is not used by the checker, suggests
approximately

```text
b0                 451708942.5161826304...
Schur threshold    451708930.0045504368...
midpoint gap              12.5116321936...
```

The gap is positive but the barycentric contraction loses roughly 120 decimal
digits. This is why ordinary midpoint arithmetic is explicitly excluded from
the certificate.

## Reproduction

The GitHub workflow is

```text
.github/workflows/x9309-zero-anchor-degree15.yml
```

and the branch-push trigger is

```text
agent/gpt56-01-o/93-run-zero-anchor
```

The retained result will be committed under

```text
experiments/X-9309-zero-anchor-degree15/results/
```

with a complete SHA-256 ledger.

## Verdicts

```text
CERTIFIED_NEGATIVE_ZERO_ANCHOR_WITNESS
CERTIFIED_POSITIVE_FULL_DEGREE15_ZERO_ANCHORED_CONE
UNRESOLVED_ZERO_ANCHOR_CONE
```

A negative verdict is an RH-disproof nomination subject to independent
completed-xi reproduction and review of the inherited analytic/count gates. A
positive verdict closes only this exact ordinate, atomized count profile,
seventeen-node table, and degree bound.
