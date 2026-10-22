# Exact PR #499 target-null Hall-packet obstruction

Frozen PR: `#499` at `99d3983b57f82941131caa8d9c36e4947f1179a0`  
Claim: `L-91820`  
Verdict: **FALSE AS WRITTEN** at the complete typed-packet scope.

## The forced edge

Take \(x=2\). The compact Möbius fibre has one positive target occurrence \(e=1\) and one negative target occurrence \(o=2\). Since there is no other positive destination, the target Hall transport has a strict positive edge \(o=2\to e=1\).

## Score per unit target

For \(z=\sqrt{x/k}\),

\[
T=4z-3,\qquad S=5z-3,
\]

so the score per target unit is

\[
g(z)=\frac{5z-3}{4z-3}.
\]

It is strictly decreasing:

\[
g'(z)=-\frac3{(4z-3)^2}<0.
\]

The edge moves from \(z_o=1\) to \(z_e=\sqrt2\), hence

\[
g(z_e)-g(z_o)
=
\frac{3(1-\sqrt2)}{4\sqrt2-3}
<0.
\]

## Consequence

The exact Hall score identity is

\[
\sum_eS_e-\sum_oS_o
=
\sum_e u_e\frac{S_e}{T_e}
+
\sum_{o,e}t_{o,e}
\left(
\frac{S_e}{T_e}-\frac{S_o}{T_o}
\right).
\]

The edge term is negative. Therefore a nonzero Hall edge cannot be represented by a packet which is simultaneously:

```text
target-null;
positive in the complete target/score/row packet cone;
nonnegative in every row;
exact in the declared score coordinate.
```

The surviving theorem is:

```text
target equality;
component-row equality with a nonnegative row bonus;
score superordination.
```

The stronger complete positive packet asserted in `L-91820.3--.4/.8` is false.

This does not refute the possibility of a one-shot physical row. It requires the proof to keep the favorable score inequality separate from the row-bonus realization.
