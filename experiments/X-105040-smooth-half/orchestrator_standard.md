# T-105040 orchestrator cross-check standard (derived before lane results)

1. H-expansion: H(Y) = 4 sqrt Y + zeta(1/2) log Y + zeta'(1/2) + E(Y);
   constant identified as zeta'(1/2) = -3.92264613921 (numeric convergence
   -3.92264877 / -3.92264622 / -3.92264614 at Y = 1e3/1e4/1e5).

2. Q log-coefficient: kappa_j = C_j zeta(1/2) + A_j j^{-1/2}
   - B_j (j+1)^{-1/2} - C_j sum_{m<=j+1} m^{-1/2};
   kappa_2 = -1.6234912156, kappa_3 = -0.5935699813.

3. Saturated margins (x >= ~(j+2) P_61): the sqrt-x layers cancel exactly
   (greedy sliver row mass vs G's leading term); the log-slope is
   alpha_j = kappa_j * B^s_theta, with B^s_theta = B^s_inf - S_sliv,
   S_sliv = (4/3) M_sc^sat + B^s_inf; measured M_sc^sat = 13.9039,
   B^s_inf = +0.002214 => B^s_theta = -18.53853;
   alpha_2 = 30.097146 (measured slope 30.097172),
   alpha_3 = 11.003917 (measured 11.003936) — 7-digit agreement; residuals
   consistent with O(1/log x) finite-difference corrections.

4. Saturation table (40 dps, expansion-based greedy over the full 2^18
   lattice): M2/M3/Msc = 1471.166/538.700/13.9039 at 1e26;
   1609.769/589.375/13.9039 at 1e28; 1748.371/640.050/13.9039 at 1e30;
   2025.576/741.400/13.9039 at 1e34. Sliver: 130941 evens, top threshold
   1110, x-independent. B^s_inf = +0.002214.

Lanes must reproduce (2)-(4) independently; discrepancies escalate to the
orchestrator before any deposit.
