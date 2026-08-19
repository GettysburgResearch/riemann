# M-99120 — Hostile review protocol for the two-sort row resolvent

A reviewer should check, in order:

1. the local identity is stated in actual component rows, not in target/score
   metadata;
2. the child map acts only on the positive source sort;
3. the Hall row bonus has no child coordinate;
4. endpoint descent makes the child map nilpotent at every fixed root endpoint;
5. direct integration is performed before any optional cubature;
6. the one cubature preserves all live row coordinates and provenance-label
   masses simultaneously;
7. ordinary `q` and `4q` rows are formed before radix-four detail;
8. omission and thinning are applied once to the resolved row;
9. the physical score is evaluated only after resolution;
10. no claimed RH status is inferred from the finite algebraic checker.

The smallest falsifier is a single component-row coordinate for which
`E != J+ET`. If such a coordinate exists, the application fails. The abstract
resolvent theorem itself remains valid.
