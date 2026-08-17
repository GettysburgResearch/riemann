# M-97400 — Hostile reconstruction protocol

Review in this order.

1. Freeze PR #566 at `2407b4ffe5024a2e3898922cf0b722d5cf69e496`, PR #574 at `74fba7f3e55fa9a53d1eb814e5067f5011ef5e86`, and PR #575 at `265c481ebd02807ab7d9a95cb0cf905a22c1876f`.
2. Recompute the canonical `Q_Y(2),Q_Y(3)` formulas and the positive `5:3` unsieved dictionary.
3. Expand every literal squarefree source atom into `d|P_61` and ordered rough history; check activation, magnitude, parity and first ownership.
4. Verify the formal causal coefficient cancellation atom by atom, including every `r_i lambda_i` child.
5. Confirm that no oriented child is observed as a positive row.
6. Reproduce the odd-history witness `X=61841`, history `(67)`, terminal `(71,13)` and its target gap greater than 17.
7. Check that PR #574’s TP2/Cauchy–Binet theorem does not imply total target capacity.
8. Check R-97300 before every use of scalar exactness; reject any lift to two rows.
9. Construct the exact finite completed-parity atom table for one endpoint, including target-active scalar-zero atoms and both activation sides.
10. Recompute the fractional-knapsack Lorenz optimum and one-parameter dual.
11. Search for an exact finite separator at any failed endpoint. A single separator refutes uniform CPSL67.
12. Independently reconstruct the compact and MPFR terminal certificate and preserve its canonical-orientation scope.
13. Recompute the scalar Mellin transform, especially the `k^(-s-1/2)` factor and `6/s^2` unit term.
14. Verify positive-axis removability, arbitrary-multiplicity pole survival, and Landau’s hypotheses after `X=e^t`.
15. Confirm that no finite scan, zero-density estimate, Mertens bound, endpoint benchmark bridge or RH-equivalent cancellation estimate is imported.

Immediate falsifiers:

```text
duplicate owner;
missing source atom or activation side;
changed k^(-1/2) coefficient;
leafwise canonical Hall after odd history;
TP2 promoted to global target capacity;
scalar exactness promoted to two rows;
omission of target-active scalar-zero atoms;
wrong Mellin scaling power;
finite replay promoted to CPSL67;
hidden assumption of eventual scalar positivity.
```

If CPSL67 is infeasible at a finite endpoint, publish the exact dual threshold and separator. If diagnostics remain feasible, do not promote them to a universal proof; search for a uniform invariant controlling the Lorenz envelope.
