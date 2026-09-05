# Lane D PLAN (density transfer + corollaries)
1. Read deposited context: T-105060, L-105061/62/63, laneB1/B3 notes.
2. Derive complex partial-fraction identity for Xi_k'/Xi_k off real axis (genus/order care).
3. Prove ATTRACTION LEMMA: zero of Xi_{k+1} at height >= eta needs Xi_k zero at height >= eta' nearby; quantify eta', d(eta).
4. Numeric check: synthetic ladders (planted high pairs) + real Xi_1/Xi_2 zeros via mpmath.
5. Assemble density transfer N_{k+1}(eta,T) <= C(eta) N_k(eta',T+1); base case Xi_0 via classical zero-density (EXTERNAL-CLASSICAL, literature-unverified).
6. Littlewood route (a): assess honestly whether it beats T log T; record outcome either way.
7. Deliverable 2: honest check whether census X_k=0 excludes off-line pairs — likely NO; document.
8. Deliverable 3: PR(delta,eps)-conditional theorem statement consuming lane-W interface; draft T-105065 + L-105066.
9. All numerics in laneD/*.py; derivations appended to DERIVATION.md in small chunks.
10. Final: STATEMENTS PROVED first; failures recorded honestly.

## Working identity (to verify then prove)
F = Xi_k, genus-0 square-variable Hadamard (L-105062 S1). For w = u+iv, v>0, F(w) != 0:
Im(F'/F)(w) ungroups absolutely (Sum 1/|w-zeta|^2 < inf). Pairing each real zero alone
and each conjugate pair (zeta_j = x_j+iy_j, conj):
pair net Im = 2v[(y_j^2 - v^2) - (u-x_j)^2] / (|w-zeta_j|^2 |w-conj zeta_j|^2).
At a zero w of Xi_{k+1} with F(w)!=0: Sum_pairs [above] = mv/|w|^2 + v Sum_real 1/|w-t_n|^2 > 0
=> SOME pair has (u-x_j)^2 + v^2 < y_j^2: w lies in the OPEN JENSEN DISK D((x_j,0), y_j).
This is Jensen's theorem (polynomials: Jensen 1913/Walsh 1920) extended to the ladder class.
Consequences: D2 rung transfer with log-loss; D3 o(T) via EXTERNAL Selberg density;
D4 verified-height propagation X -> X - k/2; D5 high pairs carry o(N_0) of W_k.

## FINAL STATUS (2026-08-23)
- D1 attraction/Jensen-disk lemma: PROVED (DERIVATION.md D0-D1). Numerics: 550+ poly configs
  + Xi-like plant (60dps) 0 violations; float64 incident recorded.
- D2 one-rung transfer, D2.0 unit-window: PROVED. D3 o(T) rung density: PROVED mod
  EXTERNAL Selberg/Carlson. D4 verified-height propagation (X -> X-k/2): PROVED.
- D5 weight localization (w_k carried by y_j < eta): PROVED mod EXTERNAL H-L gaps;
  D5.0 gap-doubling PROVED (3021 intervals numeric-clean).
- Littlewood route (a): assessed, yields only << T/eta; NOT completed; superseded by (b).
- Deliverable 2 exclusion form: VACUOUS (counterexample family; census extra-ledger
  excludes nothing about off-line zeros). Salvage = D4. Recorded in D6.
- Deliverable 3: T-105065 draft (conditional; hypotheses [H1]-[H4] pinned exactly);
  L-105066 draft. Both in this dir; repo read-only, nothing written to repo.
