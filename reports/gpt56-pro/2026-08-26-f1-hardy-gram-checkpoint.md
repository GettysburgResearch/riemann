# F1 Hardy–Gram and signed near-collision checkpoint

The requested checkpoint-four commit is present remotely and remains in the
ancestry of PR #730.  The first two checkpoints of this ownership pass proved
the Boolean/Wick F1 square and then discretized the reflection-Hodge variation
to one scalar Hardy sequence.

This checkpoint isolates the strongest elementary Hilbert-space route to that
sequence and proves the exact obstruction to closing it source-blindly.

1. Weighted Cauchy turns the Hardy `l1` gate into the sufficient square gate
   `F1GRAM105480` with only the constant harmonic mass `log 2 + O(1/M)`.
2. The logarithmic `L2` mass of every integer cell has an exact closed formula
   and is uniformly equivalent to the two endpoint squares.
3. The endpoint jump-square ledger is `M^(-1+o(1))`, so continuous `L2` and the
   discrete endpoint square are equivalent at the frozen source convention.
4. The discrete square is one exact positive-semidefinite Gram supported only
   on physical ratios between `1/8` and `8`.
5. Its diagonal is subpower.  Thus `F1GRAM105480` is equivalent to the positive
   part of one signed distinct-product off-diagonal `F1HCNC105481`.
6. Full Mellin--Plancherel identifies the same square with a compact weighted
   Nyman norm of the literal physical source polynomial.
7. The concurrent PR #719 spectral advance is absorbed: critical conjugation
   identifies the Gram with a strictly positive fixed weight times the modulus
   square of one normal-ordered analytic source square.  A Beta-weighted
   half-source fourth moment is a valid stronger sufficient gate.
8. An explicit all-positive critical packet has unit coefficient energy but
   Gram energy at least `cM`.  Universal Schur, Bessel, Hodge, or diagonal
   bounds are therefore impossible at physical-collapse scope.
9. The remaining estimate must use the signed least-prime Calderon difference,
   connected Kummer incidence, Wick-centered family cancellation, or an
   equivalent source-specific near-collision theorem.

The latest frozen heads are

```text
PR #730  74a4f6dcad0eabdc98c954ce0e7b46d39875cf32
PR #719  e56c981e2d0639a988f8f54aa362724eb00d9131
PR #751  98af0db6ec7f77d6333a77a3dac53c4698852f43
```

Replay:

```text
PASS_T105480_F1_HARDY_GRAM
proof_object_sha256=421243172d0f8069a7f4b8969265d99c01dab8df45ac16251357f57fa801e15d
finite_checks=185819
hostile_mutations=16
```

`F1FOURTH105483`, `F1ASQ2_105483`, `F1HCNC105481`, `F1GRAM105480`,
`F1HARDY105470`, `BCI102990`, and RH remain
open.
