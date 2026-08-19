# Research synthesis — the SHARP row-kernel frame

## Why the latest score routes must be discarded

PR #635 proves that a row cannot simultaneously be near-native in ordinary
capacity and carry a literal score `4sqrt(X)-O(1)`. PR #638 then shows that the
continuum inverse used to justify that score has a rank-two nullspace and
unrecorded activation atoms.

The clean response is not another score calibration. The fixed-row
Mellin--Landau consumer needs only coefficientwise positivity of one component
row.

## The eureka

The SHARP target is an exact positive primitive for every component row:

\[
 Q_Y(j)=\int_1^Y(4\sqrt{Y/t}-3)\kappa_j(t)\,dt/t,
 \qquad \kappa_j(t)>0.
\]

The kernel is explicit and elementary. Its positivity reduces to one base
inequality and the exact increasing sequence

\[
 \Delta_{j,N+1}-\Delta_{j,N}>0,
 \qquad
 4(N+1)^3-(2N+1)^2(N+2)=3N+2.
\]

This aligns the row with the exact target Hall source. It also fixes every
boundary mode at the finite source level, so the second-order Volterra frame is
unnecessary.

## Stress tests

- Replacing the SHARP target by `2sqrt(y)-1` fails the Hall prefix at
  `t=13`, `x=67`.
- Replacing the exponent `3/2` in the kernel destroys the exact logarithmic
  integral.
- Dropping the negative `m=j+1` coefficient breaks the Mellin symbol.
- Treating the Hall bonus as recursive violates source ownership.
- Using the score shortcut contradicts the ordinary-response lock.
- Using the old FRONTIER-CHAIN imports a known false finite transport.

## Status

This packet is the strongest short component-row candidate visible in the
current repository. It removes the score, all-column, terminal, port,
prime-square, and rank-two frame interfaces. It remains a proposed proof until
the compact Hall/profile, causal common-parent tree, and fixed-row analytic
consumer are independently reconstructed.
