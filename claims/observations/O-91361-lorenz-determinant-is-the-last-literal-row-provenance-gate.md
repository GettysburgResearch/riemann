# O-91361 — One full Lorenz determinant is the last literal row-provenance gate in the causal factor-54 route

Claim ID: `O-91361`  
Status: **CURRENT SYNTHESIS / PROPOSED RESOLUTION PATH**  
Created: 2026-08-13  
RH status: **unproved**

The exact nonduplicating packet budget of `L-91355` reduces every rough generation to:

```text
survival and current causal packets: total parent coefficient at most one;
canonical contracted children: total coefficient below one eighth.
```

The true causal target/score Hall theorem supplies a positive score-Lorenz residual source. `L-91360` proves that, for every row, causal row mass per score unit decreases with the source node. `L-91358` shows that literal row subordination is then equivalent to the single full-packet determinant

\[
\boxed{
\mathscr D_j(p,y)
=E_R^{(j)}(p,y)O_S(p,y)
 -E_S(p,y)O_R^{(j)}(p,y)
\ge0,
}
\]

for

\[
p\ge67,\qquad1\le y\le67,\qquad2\le j\le66.
\]

If this determinant holds, the Lorenz residual is one hereditary positive source which is score-exact and target-subordinate, while

\[
\text{signed arithmetic row}
=	ext{residual-source row}+	ext{positive target-null row bonus}.
\]

The literal entropy surplus theorem on PR #437 then applies to the complete row, including the bonus. Together with the nested same-index physical embedding and the one-use finite collar/port ledger, the packet-valued consumer gives

\[
\mathfrak L_X
\le\frac18\sup_{Y\le c_0X+C_0}\mathfrak L_Y+O(1),
\]

and hence an `o(log^2 X)` loss bound.

Thus the strongest factor-54 proposal now has one explicit first open sign:

```text
causal row/score ratio ordering             CLOSED / L-91360
source nonduplication and child mass <1/8  CLOSED / L-91355
literal one-prime entropy surplus           CLOSED ON PR #437
full Lorenz determinant D_j(p,y)>=0         OPEN / FINITE-ANALYTIC
row provenance after determinant            IMMEDIATE / L-91358
full factor-54 composition                  PROPOSED
Riemann Hypothesis                          UNPROVED
```

Numerical reconnaissance is not a proof object. A production theorem must use directed cells or an analytic determinant factorization and must preserve the causal support cutoffs.
