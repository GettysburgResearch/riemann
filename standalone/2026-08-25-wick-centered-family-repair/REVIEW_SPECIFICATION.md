# Review specification — T-106140 Wick-centered family repair

Review the new packet in this order:

1. `R-106131`: verify
   \[
   \sum_{\eta\ {\rm even}}w_q(\eta)=q-1
   \]
   and reconstruct the one- and two-conductor atomic ledgers.
2. Confirm that the earlier `L-106112` and `L-106121` diagonal estimates pay
   only the principal and principal--principal channels.
3. `L-106131`: reconstruct the sign-pair operator identity
   \[
   qI-J
   =
   \frac{q+1}{q-1}J
   +
   q\left(I-\frac{2}{q-1}J\right),
   \]
   its tensor product, and the channel-by-channel normal ordering.
4. Verify that the nonprincipal constant background is retained and that all
   collision variables are the complete physical squareclasses `Pc^2`,
   `Qd^2`.
5. `L-106132`: verify
   \[
   h\star h=\mu_{\rm sf},\quad
   b_U=(a_U\star h)^{\star2},
   \]
   and the least-prime cutoff recurrence.
6. `T-106140`: reconstruct
   \[
   \mathfrak A^\circ
   =
   \mathfrak P^\circ+\mathfrak K^\circ
   \]
   after the global source-dual sum.
7. Check the principal-only atomic bound and the implication from the
   principal bilateral moment to `BCI102990`.
8. Decide whether either `WCADD106140` or `WCKUM106140` follows from an
   existing theorem. Do not replace a global signed conductor sum by
   fibrewise absolute values.

A rejection must identify the first false equation or unsupported source
normalization. The current classification is:

```text
atomic-ledger correction                accepted internally;
Wick-centered operator identity         exact;
Boolean half-source identity            exact;
principal atomic diagonal               subpower;
WCADD106140                              open;
WCKUM106140                              open;
BCI102990 / RH                           open.
```
