# R-98800 — A Hall row bonus cannot be a complete positive exact-score packet

Claim ID: `R-98800`
Status: **EXACT REFUTATION / BINDING TYPE FIREWALL**
Frozen target: PR #499 `L-91820` at `99d3983b57f82941131caa8d9c36e4947f1179a0`
RH status: **not involved**

At the compact fibre `x=2`, the unique target Hall edge transports the negative
occurrence `o=2` to the positive occurrence `e=1`.  Put

\[
 z_k=\sqrt{x/k},\qquad T_k=4z_k-3,\qquad S_k=5z_k-3.
\]

The declared score per unit target is

\[
 g(z)=\frac{5z-3}{4z-3},\qquad
 g'(z)=-\frac3{(4z-3)^2}<0.
\]

Since `z_e=sqrt(2)>z_o=1`, the edge correction is

\[
\boxed{
 g(\sqrt2)-g(1)
 =\frac{3(1-\sqrt2)}{4\sqrt2-3}<0.
}
\]

Thus a nonzero edge cannot simultaneously be

```text
target-null;
positive in a target/score/row cone;
nonnegative in every component row;
exact in the declared-score coordinate.
```

The exact surviving statement is weaker and sufficient for the new route:

```text
target: exact residual identity;
score:  residual source is superordinate;
rows:   residual row plus a nonnegative edge-owned Hall bonus is exact.
```

Accordingly every successor must type the bonus as a **score-free physical-row
object**, not as a positive source packet.  Any mutation which assigns a
declared score to the bonus, gives it target mass, or exports it to a recursive
child is rejected.
