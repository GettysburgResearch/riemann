# X-90009 — Final deficit theorem artifacts (Stage 2 gate + Stage 3 closure)

Consumer: claims/theorems/T-90009-final-deficit-theorem.md

- `stage2_gate.py` — the GO/NO-GO gate: shell normal form at z=2 (Prop-1 residuals vs floors),
  moat constant -0.9025 at z=2, Mobius coordinates + identity check (1.4e-12 at 1e6), kernel
  masses/envelopes, random-f shell second moments (exact fiber identity + samples), supply/demand
  curves. Run: `python3 stage2_gate.py small|mid|big` (~15 s each).
- `stage3_final.py` — closure computations:
  (A) exact mu shells T^s_{X_j}(2), chain 2^20 -> 2^7 (floors exact); telescope identity to 1.7e-12;
      all 13 shells negative, sum of positive parts = 0; consecutive correlation +0.996.
  (B) class-H moments at X0=2^17 (10 shells): kernel telescope pointwise (2.3e-13); exact
      mean/covariance via fiber sums g_j(d)=sum_a c^(j)(d a^2); consecutive fluctuation correlation
      +0.999..1.000; SD(signed total)=1.741 sqrt(X0) = sum_j SD(shell_j); sqrt(E total^2)=3.073 sqrt(X0);
      30-sample check.
  (C) pretender distances: min over real chi mod q<=12 times n^{it}, |t|<=60 (grid 0.05) of
      D^2(f chibar, n^{it}; X0); lambda M=1.357; 25 random f in [1.19,1.38]; joint witness
      (seed 90009 #2): total = -7.49 sqrt(X0) with M=1.398.
  (D) deficit arithmetic with Hall's optimal kappa([-1,1]) = 0.32867416320 (GS Decay Ex.1).
  Run: `python3 stage3_final.py all` (~15 s).
- `stage3_final.log` — canonical log of the committed run.

Pinned sources: arXiv:1706.03755 (GHS sharp Halasz), arXiv:math/9911246 (GS Decay: Hall's theorem,
kappa optimality, Example 1 m=2), arXiv:1203.0596 (Koukoulopoulos).
