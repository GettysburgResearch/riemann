# M-106550 — Hostile review contract for the 280-point pressure lift

Reject the packet if any of the following occurs.

1. The seven-gap certificate is treated as newly replayed; it is only imported
   from the exact source lock of `T-105210`.
2. The identity \(E(G_B)=E_{280}\) is used without unit diagonal.
3. More than one eigenvalue above \(2\) is allowed in the \(E<2\) branch.
4. The Cauchy--Schwarz constraint
   \[
   E-a^2\ge a^2/(m-1)
   \]
   is omitted.
5. The \(E\ge2\) branch is replaced by the old unit cap.
6. The nonnegative span variable is dropped before applying the monotonicity
   of \(\phi_m(E)-E\).
7. Convex pinching, offset averaging, or the coefficient
   \(279/140000\) is changed without a complete recount.
8. `external_arb_certificate_replayed`, `ninety_percent_established`, or
   `rh_established` is set true.
