# L-91414 — Shift-eight row-debt localization

Status: **PROVED EXACT REDUCTION**. RH remains unproved.

For a score-Hall flow `t_(o,e)` with `e<=o+8`, the row excess of the positive residual over the signed row is
\[
\sum_{o,e}t_{o,e}[q(o)-q(e)],
\qquad q=K_R/K_S.
\]
Adverse terms have `e>o`.

If `o>y`, both nodes are outer. By `L-91410`,
\[
q(o)-q(e)=\sum_{k=o}^{e-1}[q(k)-q(k+1)],
\]
a sum of at most eight adjacent outer increments.

If `o<=y<e`, then
\[
y-8<o<=y<e<=y+8.
\]
If `e<=y`, both nodes lie in the fixed set `1<=d<=67`.

Thus every adverse shift-eight edge is either an adjacent outer telescope or belongs to one fixed interface table on nodes at most `75`. A completion by endpoint butterflies needs only one adjacent outer kernel and one finite interface certificate; no unbounded child-active monotonicity is needed.
