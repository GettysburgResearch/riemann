# O-90005 — dBN zero-dynamics: stall theorem for the Coulomb/window schema and the verification cost law

Claim ID: `O-90005` (provisional range; allocate at registry)
Status: **PROVED_SKETCH (stall theorem, scoped) + PROVED (literature pins, verified verbatim) — adversarially reviewed this session**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`, Strike A prong A3
Date: 2026-08-09
Scope: caps ONE schema of zero-side arguments (Coulomb pair-death with window-count statistics); not every conceivable zero-side argument. No RH claim.

## 1. Setting (all pins verified against arXiv sources)

Backward heat \(\partial_tH=-\partial_{zz}H\) (Rodgers–Tao, citing Csordas–Smith–Varga); zero dynamics \(\partial_tx_k=2\sum_{j\ne k}'1/(x_k-x_j)\); a complex pair \(a\pm ib\) dies (reaches the real axis) at a rate governed by the Coulomb field of the neighbouring real zeros. Per-pair death bound (Lemma A3.1, PROVED_SKETCH with named caveats: window persistence along the flow, collision handling, sup attainment): with real zeros of local gap structure \(G\) near height \(x\), the pair dies by time \(\le\) an explicit function of \((G,b)\); the endpoint-minimization step was strengthened on review to an exact superadditivity \(\varphi(s_1)+\varphi(s_2)\ge\varphi(s_1+s_2)\).

## 2. Stall theorem (the deliverable)

**Even with perfect one-point statistics** (RH+GUE-grade local density, error \(e=0\)), the Lyapunov rate of this schema is capped by Coulomb geometry times density: \(\kappa\le L/4\pi\) with \(L=\log(T_{\mathrm{ver}}/4\pi)\). At the current frontier \(T_{\mathrm{ver}}=6\cdot10^{12}\): \(L=26.9\), death time \(\ge0.340\) (Trudgian-grade constants: 0.398) — versus Polymath 15's analytic 0.20 at the same frontier. Reaching \(\Lambda\le0.19\) via dynamics+statistics needs \(L\approx112\), i.e. verification height \(\sim10^{49}\); \(\Lambda\le0.1\)-class needs \(\sim10^{94}\). **The dynamics schema is strictly dominated by the existing analytic architecture at every attainable height.**

## 3. The plug-in trap (proved conditionality)

Montgomery pair correlation — the statistic one imagines feeding the flow — is **RH-conditional** (pinned verbatim from Rodgers–Tao: "results of Montgomery who determined *on the Riemann Hypothesis* the pair correlation measure … against band-limited functions"; the CGGGH gap result likewise). RT may use such inputs only inside their reductio (assuming \(\Lambda<0\), which implies RH). The statistic the death-ODE actually consumes is a one-point/window-count quantity; no unconditional version strong enough for any \(\delta>0\) improvement was found, and §2 shows even the perfect version stalls.

## 4. Cost law (companion to R-90002)

\(\Lambda\le t+y_0^2/2\) is achievable by the existing (prime-free) architecture iff \(t\log(2H_v/4\pi)\gtrsim c\approx4.5\): today \(t^*\approx0.166\) (⟹ Λ≤0.20 ✓); \(t=0.1\) needs \(H_v\sim10^{20}\); \(t=0.05\sim10^{38}\); \(t\to0\) is superexponential. Polymath 15's own heuristic ("Λ ≤ O(1/log T) … without a major breakthrough on the Riemann Hypothesis", pinned verbatim) is the informal statement; Lemma A3.1 is a rigorous one-sided half of it.

## 5. Campaign consequence

Combined with R-90002 (prime-side entrance closed) and L-90002 (the deepened moat has no consumer), the dBN lane offers the campaign no attack surface beyond computation. Recorded so no future wave re-enters it with a renamed schema.

Artifacts: `scratchpad/adv_a3_check.py` (independent exact polynomial backward-heat simulator: ODE match to 7 digits, death-time sandwich 0.208 ≤ 0.3347 ≤ 0.405 verified); prong report in session workflow journal.
