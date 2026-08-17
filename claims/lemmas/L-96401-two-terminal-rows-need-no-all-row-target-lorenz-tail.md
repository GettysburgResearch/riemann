# L-96401 — The terminal factor-67 compiler is sufficient in rows 2 and 3

Claim ID: `L-96401`  
Status: **PROPOSED COMPLETE TWO-ROW TERMINAL THEOREM — REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: exact compact factor-67 Hall source; directed scalar source bounds; single-endpoint row/score monotonicity  
RH status: **unproved**

For a terminal fibre, put

\[
T(z)=4z-3,\qquad S(z)=5z-3,
\qquad z=\sqrt{x/k}.
\]

The Hall transport is target-exact and score-superordinate.  For `j=2,3`,
define

\[
\phi_j(Y)=\frac{Q_Y(j)}{5\sqrt Y-3}.
\]

Direct differentiation on each activation interval gives

\[
\phi_j'(Y)\ge0
\qquad(Y\ge j,\ j=2,3).
\tag{L-96401.1}
\]

At an activation point the entering component has value zero and a
nonnegative one-sided derivative, so the inequality is global.

Every terminal Hall edge is no-upward in source index, hence its positive
endpoint is at least its negative endpoint.  Equation (L-96401.1) therefore
gives nonnegative transported row gain.  The unmatched source is positive and
the literal score surplus is nonnegative.  Consequently the terminal output
satisfies (L-96400.2) for rows 2 and 3.

This theorem deliberately does not claim the complete 65-row Target–Lorenz
tail.  It uses only the two rows needed by the fixed-row Mellin consumer.
The forced `q=2` score obstruction remains binding: the row bonus has no
declared-score packet coordinate.
