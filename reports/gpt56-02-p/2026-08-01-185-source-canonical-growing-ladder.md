# 2026-08-01 — Growing source-canonical direct-block emitter

## Advance

The production split is now canonical at every finite `N`.  In the unnormalised
even Fourier coordinates, the source-valid subspace is exactly the kernel of
`x0+2 sum xk`; its metric orthogonal complement is the all-ones source-corrector
vector.  This removes the fitted integer basis used in `X-18505`.

The new Arb producer enumerates all prime powers, emits complete cutoff-free
D-0001 matrices, and contracts them into the exact source split.  Frozen dyadic
Galerkin solves are included in the config.  The Fraction consumer independently
reconstructs all contractions, proves source-valid coercivity by interval LDL,
and tests the direct LMI.

## Reconnaissance

Nine growing levels through `(c,N)=(5000,10)` have ordinary Schur values between
`0.0825` and `0.0221`.  Their products with `log c` stay between `0.1717` and
`0.2022`, strongly nominating a `1/log c` quotient floor.  Source-valid
coercivity simultaneously falls to about `6e-49`, but 240-bit dyadic solves make
the corresponding residual penalty negligible relative to the proposed floor.

## Honest frontier

The immutable directed workflow decides the finite ladder.  It does not prove
that the same scaling law persists on an unbounded sequence.  The smallest exact
remaining obstruction is therefore no longer a data-format or solve problem:
it is a uniform arithmetic lower bound for the source-corrector Schur scalar,
with enough conditioning control to keep the source-valid block invertible.

No RH conclusion is claimed from the finite ladder.
