# R-105201 — CRDB is a zero-count ledger, not a low-order producer

Claim ID: `R-105201`  
Status: **BINDING SCOPE CORRECTION**  
Created: 2026-08-23  
Depends on: `L-104500--L-104501`, `L-104522`, `L-105203`  
RH status: **unproved**

The natural-scale high-derivative results do not estimate the actual low-order
Levinson obstruction.  This can be seen exactly, without a countermodel.

Let

\[
F_j=\Xi^{(j)}
\]

on one regular conjugation-symmetric rectangle.  Retain the notation of
`L-105203`:

```text
O_j       off-real zeros of F_j in the rectangle;
R_j       real zeros of F_(j+1) on the real slice;
E_j       wrong extrema of F_j;
B_j       the two real endpoint defects;
W_j       N_Omega(F_j)-N_Omega(F_(j+1));
C_j       critical-residue coherence.
```

The exact reverse-Rolle and complex-transport identities give

\[
O_j-O_{j+1}
=2E_j+B_j+W_j-1.
\tag{R-105201.1}
\]

Hence

\[
\boxed{
\sum_{j=0}^{r-1}(B_j+W_j-1)
=O_0-O_r-2\sum_{j=0}^{r-1}E_j.
}
\tag{R-105201.2}
\]

The winding terms telescope because

\[
\sum_{j<r}W_j
=N_\Omega(F_0)-N_\Omega(F_r).
\tag{R-105201.3}
\]

Now define the upper ledger used in `CRDB105200`,

\[
\mathcal D_r
=O_r
+2\sum_{j<r}R_j(1-\mathfrak C_j)
+\sum_{j<r}(B_j+W_j-1).
\tag{R-105201.4}
\]

Since `L-105203.1` proves

\[
E_j\le R_j(1-\mathfrak C_j),
\]

put

\[
S_j=R_j(1-\mathfrak C_j)-E_j\ge0.
\]

Substitution of (R-105201.2) into (R-105201.4) gives the exact identity

\[
\boxed{
\mathcal D_r
=O_0+2\sum_{j<r}S_j.
}
\tag{R-105201.5}
\]

Thus `CRDB105200 < 2` is a correct sufficient condition, but its left side
already contains the unknown off-real zero count `O_0`, plus nonnegative
coherence slack.  The high-derivative entry only removes `O_r`; it does not
estimate (R-105201.2), the fixed low-order residues, or the continued
horizontal argument which determines them.

## Binding consequence

The following interpretation is withdrawn:

```text
high-tail residue coherence
  -> a nearly closed cumulative low-order budget.
```

The correct interpretation is:

```text
high-tail residue coherence
  -> an explicit terminal condition at derivative order r;

actual low-order descent
  -> still requires an independent Levinson/Hermite-Biehler boundary theorem
     or a direct exclusion of the last wrong-extremum event.
```

The useful exact identities in `L-105203` remain valid.  What is rejected is
counting the ledger itself as progress on its low-order input.

```text
high derivative terminal term O_r            CLOSED ON NATURAL BOXES
identity D_r=O_0+nonnegative slack            PROVED EXACT
CRDB as independent arithmetic producer       FALSE
low-order horizontal argument / last defect   OPEN
Riemann Hypothesis                             UNPROVED
```
