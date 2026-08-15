# L-93605 — The Target-Lorenz native `Y_4` deficit is below `61000`

Claim ID: `L-93605`  
Status: **PROPOSED COMPLETE DIRECT NATIVE-COST THEOREM — REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-91378`, `L-93604`, `L-19885`, elementary Chebyshev bound `J_Lambda(X)<16 log(2) sqrt(X)`  
Replay: `X-93601-target-lorenz-native-endpoint`  
RH status: **unproved**

For the row of `L-93604`, put

\[
\delta_X
=\langle Y_4,r_X\rangle
=J_\Lambda(X)-\mathcal H(d_X).
\]

The two-ledger construction gives the explicit inequality

\[
\begin{aligned}
\delta_X\le{}&(1-\tau_K)J_\Lambda(X)\\
&+\mathcal H(o_X^{\rm bot})+\mathcal H(o_X^{\rm top})\\
&+\sum_qY_4(q)
 \bigl(|e_X^{\rm nonterm}(q)|+|e_X^{\rm term}(q)|\bigr).
\end{aligned}
\tag{L-93605.1}
\]

The first line and omissions are costs of positive source operations. The last
line prices signed observation errors by absolute value. No signed vector is
called positive source.

Using the exact sparse support estimates

\[
\sum_q\frac{Y_4(q)}{q^{3/2}}<11,
\qquad
\sum_{q\le X}\frac{Y_4(q)}q
\le3+2L+2L^2,
\quad L=\log(2X),
\tag{L-93605.2}
\]

and the frozen all-column/terminal estimates, the named charges are

```text
square-root thinning     <12012
nonterminal comparison   <4        (X>=10^12)
terminal comparison      <4452*11 = 48972
positive omissions       <1
root port / large-X base  0
```

Therefore

\[
\boxed{
0\le J_\Lambda(X)-\mathcal H(d_X)
<12012+4+48972+1
=60989<61000.
}
\tag{L-93605.3}
\]

In particular

\[
\delta_X=O(1)=o(\log^2X).
\]

The estimate contains no occurrence of a pre-RH bound for
`J_Lambda(X)-4sqrt(X)` and exports no recursive native-slack term.
