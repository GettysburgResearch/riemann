# Repaired P61 bias and exact factor-67 source-interface firewalls

This standalone packet proves one new global arithmetic theorem and gives two
exact statement-to-use refutations.

## The finite theorem

For the complete P61 `5:3` annular scalar `F` and its unsigned source mass `M`,

\[
0\le F\le M\quad(1\le x<67),
\]
\[
\frac1{42}M\le F\le\frac18M\quad(x\ge67).
\]

The proof is the exact coefficient reduction and directed finite-plus-analytic
tail in `L-97400`. The old lower constant `1/40` is false at `x=184`.

## Why this does not yet prove RH

A genuine parity-contractive root identity with child mass `H<M/8` would close,
because
\[
\frac1{42}(M-H)-\frac16H
=\frac{1-8H/M}{42}M>0.
\]

PR #565 does not supply that identity. It imports a same-channel source
restriction and consumes a swapped-channel subtraction while still assigning
the canonical P61 marginals. PR #566 places the child inside a reserve and
then uses the scalar of the disjoint Hall complement as though it dominated the
reserve.

The exact remaining problem is a source-complete parity current for the actual
rough Möbius root. RH remains unproved.
