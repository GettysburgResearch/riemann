# Fixed rows 2 and 3

PR #652 supplies a fixed two-row detector family.

For the row numerators, write `a=2^{-z}`. The exact elimination used in the review is:

\[
P_2(z)=0
\quad\Longrightarrow\quad
3P_3(z)=-3(a-1)(a-2).
\]

When `Re(z)>0`, one has `|a|<1`, so neither `a=1` nor `a=2` is possible. Thus the two fixed numerators have no common zero in the open right half-plane.

This is a zero-safe analytic consumer. It does not prove that the literal native source supplies both fixed rows with eventual nonnegativity, subpower negative mass, or an admissible fixed holomorphic defect. That producer is the explicit open node `OPEN.ARITH.ROWS23_NATIVE`.
