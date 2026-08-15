# R-91860 — A target-null Hall bonus is a positive row channel, not a complete target/score packet

Claim ID: `R-91860`  
Status: **PROVED EXACT TYPE-SEPARATION / SUPERSESSION FIREWALL**  
Created: 2026-08-15  
Frozen predecessor: PR #499 at `99d3983b57f82941131caa8d9c36e4947f1179a0`  
Comparison: PR #500 at `d73c1e7a1a482cac31581211a84db43cc34c824e`; review PR #501 at `2f58a65097206c4b80142cead52282161302d10c`  
RH status: **unproved**

## 1. Forced compact Hall edge

At the admissible root fibre `x=2`, the positive Möbius target node is `e=1` and the negative node is `o=2`. The no-upward target Hall transport is forced to use the nonzero edge

\[
 o=2\longrightarrow e=1.
\]

For `z=sqrt(x/k)`, target and declared score per source unit are

\[
 T(z)=4z-3,\qquad S(z)=5z-3,
\]

so score per target unit is

\[
 g(z)=\frac{5z-3}{4z-3},\qquad
 g'(z)=-\frac3{(4z-3)^2}<0.
\]

Here `z_e=sqrt(2)` and `z_o=1`. Hence

\[
 g(z_e)-g(z_o)
 =\frac{3(1-\sqrt2)}{4\sqrt2-3}<0.
\tag{R-91860.1}
\]

## 2. Exact consequence

For a Hall edge of target mass `t_(o,e)`, the exact declared-score edge correction is

\[
 t_{o,e}\left(\frac{S(e)}{T(e)}-\frac{S(o)}{T(o)}\right).
\]

Equation (R-91860.1) makes this correction strictly negative on the forced edge. Therefore a nonzero Hall edge cannot simultaneously be

```text
target-null;
positive in a complete target/declared-score/component-row packet cone;
nonnegative in every component row;
and exact in declared score.
```

The promotion in frozen `L-91820.3--.4/.8` is false at that complete-packet scope.

## 3. What survives

The following statements remain exact.

1. The Hall residual is a genuine positive target-bearing source packet.
2. It is target-exact and declared-score superordinate:
   \[
   S(c)\ge S(E)-S(O).
   \]
3. The component-row difference is a target-null coefficientwise nonnegative row
   \[
   B_j=\sum_{o,e}t_{o,e}
   \left[\frac{R_j(e)}{T(e)}-\frac{R_j(o)}{T(o)}\right]\ge0.
   \]
4. The row bonus is current-generation only. It has Hall-edge provenance but no target-bearing source mass and no inherited declared-score coordinate.
5. Its literal physical score, computed from the nonnegative row itself, is nonnegative.

Thus the correct codomain is two-sorted:

```text
positive complete source packets
    plus
nonnegative current physical rows.
```

The Hall residual belongs to the first sort. The Hall bonus belongs to the second.

## 4. Supersession boundary

This refutation does not modify PR #499. It supersedes only the complete-packet interpretation of the bonus. The all-column response-complement and endpoint-consumer arguments may be reused after one realized row is rebuilt with the row bonus routed through a direct row channel.

```text
complete target-null Hall packet             FALSE
positive target-bearing residual source      EXACT
nonnegative target-null component-row bonus  EXACT
score superordination of residual source     EXACT
bonus rough ownership / child recursion       FORBIDDEN
Riemann Hypothesis                            UNPROVEN
```
