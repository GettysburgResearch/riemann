# Hostile review specification — T-103010

Frozen predecessor:

```text
PR #719
ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc
```

Mandatory checks:

1. derive the explicit two-piece formula for `A(e^u)` from `(D-1/2)A=A_-`;
2. verify continuity and endpoint vanishing;
3. verify strict log-concavity on both pieces and the downward slope jump;
4. reconstruct the `TP_2` minor inequality with the correct order convention;
5. derive `A_-/A` and prove it is strictly decreasing;
6. verify the Wronskian sign including nonoverlapping supports;
7. expand the endpoint determinant and recover the literal source Plücker minor;
8. verify the monotone-ratio source criterion;
9. derive the autocorrelation identity `integral W=2C'`;
10. recompute `||a||_2^2=12 log 2-8` and the total budget `24 log 2-16`;
11. reproduce the two-atom source-order counterfixture;
12. confirm that `DORI103010`, `BCI102990`, and RH remain unproved.

Immediate falsifiers:

```text
reversing one of the TP2 order conventions;
using TP2 to orient an arbitrary signed source;
taking an absolute value before forming the source Pluecker minor;
claiming the finite replay proves the analytic theorem;
claiming order-concordant closure proves the inversion sector;
claiming RH from T-103010.
```
