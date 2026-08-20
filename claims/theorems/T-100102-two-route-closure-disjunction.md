# T-100102 — The original two-route closure disjunction is withdrawn

Claim ID: `T-100102`  
Status: **WITHDRAWN AFTER HOSTILE CONSISTENCY CHECK**  
Created: 2026-08-20  
Corrected: 2026-08-20 by `T-100103`  
Depends on: `T-100100--T-100103`; `R-100103`  
RH status: **unproved**

The original statement advertised

\[
\mathrm{DCE100100}\lor\mathrm{QPET100101}
\Longrightarrow RH.
\]

The formal implication from either premise was true, but the resulting
"two-route" interpretation was misleading.

- `L-100103` proves that every DCE edge inequality is exactly nonnegativity of
  the predecessor critical state. DCE remains open and conclusion-bearing.
- `R-100103` proves that QPET asks for a liminf strictly below `A_k^*`, while
  the unconditional completion corridor forces the liminf to be at least
  `A_k^*`. QPET is false as stated.

Thus there is no live disjunction of two independent producers. The corrected
normative statement is

\[
\boxed{
\mathrm{DCE100100}\Longrightarrow RH,
}
\]

with DCE explicitly recognized as the target state sign rather than an
upstream maximum-principle theorem. The finite-completion programme retains its
unconditional corridor and pole-amplification theorems only.

```text
DCE100100                       OPEN / CONCLUSION-BEARING
QPET100101                      REFUTED
original two-route disjunction  WITHDRAWN
Riemann Hypothesis              UNPROVED
```
