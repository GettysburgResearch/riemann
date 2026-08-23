# L-105075 — Quantitative converse-Rolle: Sum w_k <= 1.4457 explicit (first discharge of T-105060(d)'s hypothesis), the end-to-end constant is honest-vacuous, and the rung-0 blocker is IRREDUCIBLE for pointwise compression

Claim ID: `L-105075`
Status: **PROVED (Theorem Q1: explicit Sum w_k; Theorem Q3: irreducibility of the
rung-0 self-reference for the pointwise-compression method; Theorem Q4: harmonic-tail
obstruction) — Theorem Q2's end-to-end constant 4.5692 is PROVED CONDITIONAL on
D_res = 0 and is HONESTLY VACUOUS (13.95x worse than the trivial baseline) — the
Conrey rate alpha_m = 1 + O(m^{-2}) is pinned with citation (literature-transcribed,
in-container verification of the printed rate) — RH NOT ADDRESSED**
Created: 2026-08-23
Agent: claude (external reviewer lane; final-pass lane B1)
Depends on: `T-105060` (master corollary; §6 conditionality), `L-105064` (weight
compression; sup-3 sharpness family), `L-105063` (A' = max(6,2k); 16/15 extremal),
`L-105066` (rung density), `L-105067` (cluster cap), `L-105062` §6 (Zeta23 0.6725
baseline), Z23-UPSTREAM ledger row.
External-classical (NEW numeric import, transcribed from the papers, flags kept):
J. B. Conrey, "Zeros of derivatives of Riemann's xi-function on the critical line",
J. Number Theory 16 (1983) 49–74: alpha_0 > 0.3658, alpha_1 > 0.8137,
alpha_2 > 0.9584, alpha_3 > 0.9873, alpha_4 > 0.9948, alpha_5 > 0.9970, and
**alpha_m = 1 + O(m^{-2})** (printed as log F_m(1) <= m^{-2}, p. 73); companion II,
J. Number Theory 17 (1983) 71–75: beta_1 > 0.7869 .. beta_5 > 0.9863 (on-line AND
simple), beta_m = 1 + O(m^{-1}). No post-1983 improvement to the m^{-2} rate found.
Repo previously carried only the qualitative kappa_k -> 1.
Replay: `experiments/X-105075-quantitative-converse-rolle/` (B1.md; rate_check.py,
census_check.py; conrey_I_full.txt, conrey_II_full.txt = extracted sources;
FAILURES.md F1–F7).
RH status: **unproved, not addressed**

## 1. Statement

**Theorem Q1 (Sum w_k explicit — discharges T-105060(d)'s `Sum w_k < infinity`).**
With the Zeta23 import: `Sum_k w_k <= 1.4457` (import-free: 3.3158), via L-105064's
W6 + the Conrey values + tail `(3/2) Sum_{k>=6} 1/(k^2-1) = 0.275`. (Transcription
flags: C_Conrey = 1 normalization; m_0 unspecified in the printed rate.)

**Theorem Q2 (end-to-end, conditional on D_res = 0 on R-C1'/R-C2).**
`1 - kappa_0 <= 4.5692`, attained at optimal truncation K = 0 of
`1 - kappa_0 <= (1 - c_{K+1}) + Sum_{k<=K} max(6,2k) (3/(2 c_k))(1 - c_k)`.
HONEST COMPARISON: 4.5692 > 1, and > 0.3275 = 1 - 0.6725 by 13.95x — the machine's
output is strictly worse than the trivial bound riding its own Zeta23 input. Even at
forced-minimal constants (A' = 16/15) the bound is 0.9655, still 2.95x above trivial.
NOT a new proportion record; deposited because an explicit vacuous constant plus the
two theorems below is the honest quantitative content of the converse-Rolle machine
as built.

**Theorem Q3 (irreducibility of the rung-0 blocker).** Any pricing scheme of the
deposited type — pointwise weight `omega <= C_omega`, per-gap cap `extra <= A' W`,
proportion floor `kappa_0 >= c_0` — has rung-0 coefficient
`theta_0 = A' C_omega/(2 c_0)`. The deposited sharpness certificates FORCE
`C_omega >= 3` (L-105064 §2 sup-3 family) and `A' >= 16/15` (L-105063 §3 extremal,
40 dps), so `theta_0 >= 8/5 > 1` for EVERY admissible constant assignment: the
fixed-point restructure has negative left coefficient always. Stronger: even
deleting rung 0 entirely, the k = 1 term alone is
`(16/15)(3/(2·0.8137))(0.1863) = 0.3663 > 0.3275` — the method cannot beat the
trivial baseline at ANY constants consistent with the deposits (it would need
alpha_1 > 0.8301, not in the literature). The exits are distributional:
average-omega statistics or T-105065's [H3] repulsion — named, not claimed.

**Theorem Q4 (tail obstruction).** With `A'_k = max(6,2k)` and the m^{-2} rate the
master majorant's k-th term is ~3C/k — harmonic divergence; convergence of the
END-TO-END chain needs rho > 2 in `1 - kappa_k <= C/k^rho`, unavailable. (Q1's sum
converges because w_k prices (1 - alpha_{k+1}) WITHOUT the A'_k factor; the
divergence is a property of the pricing loop, not of the defect sum.)

## 2. Proof / verification

B1.md (the quantified chain, all four theorems); rate_check.py (mpmath dps 40 —
every constant; machine re-derivation of Conrey's F_m(1): `m^2 log F_m(1)`
increases 0.289 -> ~0.524 over m = 2..4000, always < 1 — the printed m^{-2} rate
confirmed and intrinsically not improvable from his mollifier at R = 1);
census_check.py (X-105061 cross-check: defect ledger X_0 = X_1 = X_2 = 0,
R = 269/269/270/269 — D_res = 0 and W_k = 0 for T <= 500).

## 3. Honest residual (and refuted routes)

- The density-zero route for the residual regimes is REFUTED (FAILURES F3):
  residual clusters are deep pairs, near-real for typical gaps — exactly the
  statistic L-105066 D3 cannot count; the exceptional-gap count IS the missing
  [H3] input. Global conservation pricing is circular (F4); L-105067's 16W cap
  worsens theta_0 to 35.7 (F5). D_res stays an explicit hypothesis.
- What would make the machine non-vacuous, precisely: (i) average-omega
  distributional pricing replacing sup-3, or (ii) [H3]-type repulsion, or
  (iii) alpha_1 > 0.8301. Each named with its consumer.

## 4. Falsifiers

An error in the Conrey transcription (check against conrey_I_full.txt /
conrey_II_full.txt and the cited PDFs); a pricing scheme of the stated type with
theta_0 < 1 (would contradict Q3 — check its C_omega against the sup-3 family and
its A' against the 16/15 extremal first); convergence of Sum k·(1 - alpha_k) under
the printed rate (contradicts Q4's harmonic bound).
