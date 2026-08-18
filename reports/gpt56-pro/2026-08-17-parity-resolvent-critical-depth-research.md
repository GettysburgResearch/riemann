# Parity resolvents, source thinning, and the critical adaptive-depth frontier

## Research choice

The highest-leverage task after PR #576 was to reconstruct the exact operator
used by PR #566. The repaired P61 constant is already strong enough
arithmetically; the unresolved issue is whether the proposed current is the
actual current of the cumulative-parity source.

## Main finding

The natural source and every thinned source are related by

\[
 (I+R)F=b,
 \qquad
 (I+A)F=g_A,
 \qquad
 g_A=b-(R-A)F.
\]

The term `(R-A)F` is an all-depth signed residual. It cannot be replaced by a
local reserve or by a scalar inequality on the reserve.

The M-matrix test is

\[
 g_A-A g_A=(I-A^2)F\ge0.
\]

For `A=R`, this is the depth-two current already certified negative. For a
contractive `A`, it is a new global residual theorem, not a consequence of the
P61 bias.

## Constructive repair attempt

The exact even-depth identity

\[
 C_L(A)=(I-A^L)F
\]

shows how adaptive depth could work. The source-mass depth based on
`sum p^-1/2` expands the whole tree asymptotically. The row-critical term
carries `1/p` per rough prime. A formal full-prime Euler product is not enough,
because it contains subsets whose product exceeds the endpoint. The repair
restricts to primes `p<=(log X)^(1/4)` and chooses an even Bonferroni depth from
their reciprocal sum. Every such source history is genuinely activated, the
exact P61 annular base is retained, and the aggregate nonhomogeneous error is
`X^o(1)` against a positive `sqrt(X)/log log X` main term. The resulting exact
positive depth is `O(log log log X)`.

This is the strongest new theorem in the packet. It isolates one sharper
obligation: control only the complementary current containing at least one
rough prime larger than `(log X)^(1/4)`. This is named `LAPBR67`.

## Portfolio effect

- PR #566 should not be reviewed as “M-matrix algebra plus one Hall margin.”
  Its source operator is the first issue.
- PR #569's adaptive idea is viable only after changing from source mass to
  critical row mass; its published source-weight depth is asymptotically full
  expansion.
- PR #576's `1/42` bias remains useful local input, but no local bias proves the
  residual current.
- The common Hall/Julia/frontier family is now pinned to a large-prime adaptive
  current; the exact small-prime cube is already positive.

## RH status

\[
 \boxed{\text{The Riemann Hypothesis remains unproved.}}
\]
