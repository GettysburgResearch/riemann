# M-99210 — Hostile reconstruction contract for the component-row candidate

Review in this order:

1. Reconstruct the exact finite row `c_X(j)` directly from its Möbius sum.
2. Reconstruct the endpoint-frame identity and verify that its integrated output
   is `c_X`, not merely a target-equivalent or score-equivalent row.
3. Verify endpoint monotonicity of every canonical packet coordinate, including
   activation knots.
4. Rebuild the compact Hall flow and verify every matched row coordinate is
   nonnegative.
5. Check the exact source fraction `c=u_e/T_e`; reject independent child
   normalization.
6. Verify every random-key pushforward in the physical component rows.
7. Check one owner per rough occurrence and that the Hall bonus never recurses.
8. Verify finite endpoint descent and deterministic direct integration.
9. Independently derive the fixed-row Mellin formula and all initial convergence
   domains.
10. Recompute the large-`j` asymptotic of `P_j(rho)` and apply Landau only to
    the defining nonnegative Mellin integral.

Immediate falsifiers:

```text
endpoint frame outputs a row other than c_X;
one canonical component decreases with endpoint;
negative matched Hall component;
Hall bonus enters a child;
child row differs numerically before label pushforward;
one endpoint increment has two owners;
finite tree fails to reconstruct the signed compact fibre;
P_j(rho) cancels every sufficiently large row;
positive-real singularity omitted from the Mellin audit;
RH imported into the row producer.
```

The exact score identity is `H(c_X)=P_Lambda(X)`, not `4sqrt(X)`. Any review
using the superseded equality-score shortcut is reviewing a different and false
composition.
