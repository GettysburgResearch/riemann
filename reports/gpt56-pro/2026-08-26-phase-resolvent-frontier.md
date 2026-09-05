# 2026-08-26 — Phase-optimized cross trace and rational resolvent frontier

This pass audited the live T-106650 branch and found one stale statement:
`L-106611` still promoted the denominator phase mean to the exact canonical
charge after `L-106514/R-106640` had refuted that equality.

The file is corrected. Two exact scalar continuations are added.

1. **Optimized cross trace.** For each finite inner block,

   \[
   \mathcal C
   \le m_- -|\Delta|
   =
   \min_\theta
   \frac1{4\pi}\int\beta_-'|1-e^{i\theta}U|^2.
   \]

   This is exact in one principal channel and can remain strict when several
   channel phases cancel.

2. **Rational resolvent certificate.** If \(K\) is the positive compression
   matrix,

   \[
   \mathcal C=\operatorname{tr}K
   \le
   (1+\tau)\operatorname{tr}[K(I+\tau K)^{-1}],
   \]

   with exact positive gap
   \(\tau\operatorname{tr}[K(I-K)(I+\tau K)^{-1}]\).
   In Cauchy-Gram coordinates this is
   \((1+\tau)\operatorname{tr}[D^*GD(G+\tau D^*GD)^{-1}]\).

Either scalar total below `11/500 N`, together with the already-paid `3/40 N`
deep charge, implies more than 90% through T-106590/T-106620.

The Xi scalar estimates remain open. Ninety percent, density one, and RH are
not claimed.
