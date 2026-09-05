# R-90002 — No one-sided prime-side certifier exists for the de Bruijn–Newman flow at t > 0

Claim ID: `R-90002` (provisional range; allocate at registry)
Status: **OBSTRUCTION THEOREMS — ADVERSARIALLY REVIEWED THIS SESSION (all literature imports verified against arXiv sources character-for-character)**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`, Strike A (3 prongs + adversarial review)
Date: 2026-08-09
Fence-map addition: closes the "feed arithmetic into the dBN flow via a one-sided tilted prime inequality" lane
Scope: structural impossibility results; no statement about verification-height-driven or two-sided/mollifier progress on Λ

## 1. Setting

\(H_t(z)=\int e^{tu^2}\Phi(u)\cos(zu)\,du\); RH ⟺ Λ=0 (Rodgers–Tao `1801.05914`: Λ≥0; Polymath 15 `1904.12438`: Λ≤0.22, improvable to 0.20 with Platt–Trudgian `2004.09765` height 3·10¹²). The Gaussian tilt multiplies log-scale-\(u\) data by \(e^{tu^2}\); a prime \(n\) sits at \(u=(\log n)/2\), so its tilt weight is \(b_n^t=e^{(t/4)\log^2n}\). Polymath 15's effective approximation (Thm 1.3, imported and verified verbatim): \(H_t/B_t=f_t+O_{\le}(e_A+e_B+e_{C_0})\) with \(f_t\) a Gaussian-tilted quasi-Dirichlet sum; errors relatively \(\sim\log^2x/x\) — never the obstruction.

## 2. Obstruction theorems

**O1 (no arithmetic object at t>0; proved, one line).** \(\sum_n\Lambda(n)b_n^t n^{-\sigma}\) diverges for every \(\sigma\) and every \(t>0\) (terms \(\to\infty\)); likewise every candidate Euler factor. Hence: no half-plane of convergence, no Landau abscissa, no exact explicit formula with compact prime windows, no Euler product for any convergent completion.

**O2 (truncation sign-flip; proved with exact formula).** Define tilted von Mangoldt \(\Lambda_t\) by \(\sum_{d|k}\Lambda_t(d)b^t_{k/d}=b_k^t\log k\). Then \(\Lambda_t(p)>0\), \(\Lambda_t(pq)=\log(pq)\,b_pb_q(e^{(t/2)\log p\log q}-1)>0\) (positivity numerically to \(k\le3000\); general \(k\) conjectured) — but for the *truncated* sum that actually approximates \(H_t\), composites \(k=pq\in(N,N^2]\) carry \(\Lambda^{(N)}_t(pq)=-b_pb_q\log(pq)<0\): positivity dies exactly at the truncation \(k=N+1\). Finite entire sums have no analytic-continuation boundary; **the one-sided tail Landau's theorem needs provably does not exist.**

**O3 (the gap is the classical wall, translated; verified with a convention fix).** Zero-freeness of \(H_t\) splits into \(x\le T_{\mathrm{ver}}\) (verification+flow/barrier) and \(x\ge e^{c/t}\) (mollified triangle inequality, prime-insensitive), \(c_{\mathrm{eff}}\approx4.46\) calibrated at Polymath 15's own barrier. In the gap, the parameter \(\delta=(t/4)\log(x/4\pi)\) sweeps exactly the absolute-convergence-vs-zero-free-strip wall of T-90001 §5, translated to \(x\)-scale \(e^{4\delta/t}\). (Height conventions: with \(c\) defined via \(\log(\bar X/4\pi)\), the \(t=0.1\) requirement is \(\sim10^{20}\), not \(10^{19}\); immaterial to the law.)

**O4 (heuristic, downgraded on review).** One-sided prime hypotheses appear not to be localizable to the finite window \([T_{\mathrm{ver}},e^{c/t}]\) where a bridge would act (analytic transforms of nonnegative data cannot vanish on open sets). Status: credible heuristic, NOT a proof; the fence stands on O1+O2+O3 alone.

**Cost law (verified modulo the O3 convention).** The salvaged conditional theorem (contrapositive of P15 Thm 1.3) gives \(\Lambda\le t+y_0^2/2\) iff a pointwise lower bound on the tilted sum holds over the gap window — achievable by the existing prime-free architecture iff the verification height \(H_v\) satisfies \(t\log(2H_v/4\pi)\gtrsim c\approx4.5\). Today \(t^*\approx0.166\) (consistent with Λ≤0.20); \(t=0.05\) needs \(H_v\sim10^{38}\); \(t\to0\) (RH) costs \(e^{c/t}\): **superexponential**. Polymath 15's own "Λ ≤ O(1/log T) without a major breakthrough on RH" heuristic paragraph (pinned verbatim) is the informal version.

## 3. What survives (see L-90002)

The deterministic half of the premise is TRUE and proved: the WSTS moat deepens monotonically along the flow (Tilted Moat Lemma). But the same analysis shows the tilt is a low-pass filter — the per-zero signal-to-moat ratio is \(t\)-invariant for ordinates \(\gamma\lesssim(t/2)\log X\) — so the deepened moat has no consumer. Two independent prongs hit the identical wall; that coincidence is the strongest evidence the wall is real.

## 4. Consequences for the campaign

The dBN lane's prime-side entrance is closed by theorem. What remains open in dBN-land: verification-height-driven progress (computational; next increment \(\sim10^{20}\)), and zero-side dynamics — for which see the stall theorem in O-90005 (the Coulomb/window schema is capped at death-time ≥ 0.34 at current heights even with perfect one-point statistics, and Montgomery pair correlation is RH-conditional, verified from source).

Artifacts: `scratchpad/p15-src/`, `rt-src/` (extracted arXiv sources), `tilt_log_coeffs.py`, `adv_a3_check.py` (independent backward-heat simulator, ODE match to 7 digits); full prong reports in session workflow journals.
