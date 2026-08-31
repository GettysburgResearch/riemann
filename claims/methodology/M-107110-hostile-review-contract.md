# M-107110 — Hostile review contract for the stationary annular frontier

Review `L-107110--L-107112` and `T-107110` fail-closed.

Required checks:

1. Verify the same-band measure `(1-|log_q(m/n)|)_+` with all endpoint
   conventions; no probabilistic independence is used.
2. Check that the maximum over `Y<=X` remains present in the zero-abscissa
   theorem. Endpoint-only energy is not substituted for the maximal prefix.
3. Keep the q-free Möbius and literal beta sources distinct until the exact
   finite q-adic inverse is applied.
4. Verify that the shallow estimate is absolute only because the triangular
   kernel forces `q^-1<=a/b<=q`.
5. Check that `d>Y/R` really implies both primitive factors are `<R`.
6. Do not replace the assembled signed sum over common cores by a positive
   square for every core.
7. Treat the Vinogradov--Korobov and classical zero-abscissa theorems as
   source-locked analytic inputs, not as finite replay outputs.
8. Do not promote the rational proxy-weight core fixture to the analytic
   half-weight theorem; it verifies reindexing only.
9. Require a separate proof of the high-primitive estimate in
   `T-107110.4`. It is not supplied by coarea or by the polylogarithmic range
   removal.

Automatic rejection conditions:

```text
drop the outer maximum;
change the detector after a hypothetical zero;
absolute-value the common-core sum before interference;
count the finite replay as a Möbius estimate;
claim a new zero-free half-plane from the inherited VK bound;
claim RH.
```