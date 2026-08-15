# L-92923 — The native parity-coupling slack has direct `Y_4` cost below `60989`

Claim ID: `L-92923`  
Status: **CANDIDATE-COMPLETE DIRECT NATIVE-COST COMPILATION ON FROZEN ESTIMATES — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Primary inputs: `L-91378`, `L-91756`, `L-91853`, `L-92922`  
RH status: **unproved**

Let

\[
 r_X=\Omega_X-\Xi(d_X)\ge0
\]

be the actual external slack from `L-92922`.  The oriented source compiler adds
no new error class.  Hall transport, paired orientation, causal splitting,
actual child placement and label erasure are exact before the one global
quantizer.

The complete cost ledger is therefore

\[
\begin{array}{c|r}
\text{class}&\text{strict upper bound}\\ \hline
\text{common square-root thinning}&12012\\
\text{nonterminal signed comparison}&4\\
\text{terminal signed comparison}&48972\\
\text{positive bottom/top omissions}&1\\
\text{port / large-X base}&0
\end{array}
\]

and hence

\[
 \boxed{
 0\le
 \langle Y_4,r_X\rangle
 =J_\Lambda(X)-\mathcal H(d_X)
 <12012+4+48972+1
 =60989.
 }
\tag{L-92923.1}
\]

The signed comparison is paid by direct absolute `Y_4` domination.  Positive
omissions are paid as source.  No target-mass theorem is applied to a signed
vector.

Relative to PR #496, there is no additional `6039/8` terminal-child payment:
every **actual oriented** child is already a physical colour of the single row.
Relative to PR #500, the numerical ledger is unchanged, but the native
normalization is now certified by the paired orientation compiler.

No estimate of `J_Lambda(X)-4sqrt(X)` is used.

```text
native slack nonnegative                       L-92922
rough-lift mutation                             rejected
source/observation ledgers                      separate
actual internal children                       fully realized
exported child family                           empty
native deficit                                  <60989
Riemann Hypothesis                              unproved
```
