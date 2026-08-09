# L-90003 — c-monotonicity of the moat, the c-Gram, and the cone-blindness fence

Claim ID: `L-90003` (provisional range; allocate at registry)
Status: **B2.1–B2.3 PROVED; witness lemma PROVED (one constant corrected on review); cone fence PROVED_SKETCH (register as observation, not theorem) — adversarially reviewed this session**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`, Strike B prong B2 + adversarial review
Date: 2026-08-09
Dependencies: T-90001 §2 (Moat), L-90002 (Tilted Moat)
Scope: structure of the provable-positivity cone; no RH claim

## 1. c-monotone moat (proved)

For fixed \(\theta\): \(c\mapsto H_c(\theta)\) is continuous (piecewise-\(C^1\) in \(c\); continuity + a.e. derivative suffice), equals \(H(\theta)\) for \(c\le\theta\), and on \(c\in(\theta,1)\):
\[
\frac{d}{dc}H_c(\theta)=\frac{\theta^{3/2}}{c^2}J'(\theta/c)\ \ge\ 0,
\]
increasing to 0 as \(c\to1^-\). Two-parameter closure: \(H_{a,b}=\sqrt\theta\,(J(\theta/b)-J(\theta/a))\le0\) for \(a\le b\), with integral decomposition over extreme rays \((\theta^{3/2}/s^2)J'(\theta/s)\ge0\).

## 2. c-Gram (proved) — and why it cannot help

\(G_{ij}=-H_{\max(c_i,c_j)}(\theta)\) is PSD for every fixed \(\theta\): \(G_{ij}=\int\mathbf1_{c_i\le s}\mathbf1_{c_j\le s}\,d\nu_\theta\) with \(d\nu_\theta=-d_sH_s\ge0\) — an indicator Gram. Structural consequence: c-mixing with squared coefficients adds **no new extreme rays**, and the Gram's zero-response is a scalar multiple of \(\hat E(\rho)\), not a Hermitian square — unlike Weil-Gram forms it **cannot manufacture zero-side positivity**. (\(-H_{\min}\) is strongly indefinite: min eig ≈ −1.8.)

## 3. Telescope conservativity (proved) and the ladder decrement law (sketch)

\(\sum_jT^s_{X_j}(z)=T^r_{X_0}(z)-T^r_{X_J}(z)\) is definitional — the telescope is linear with ±1 coefficients and adds no sign content (O-90004 §3's averaging-circularity re-derived at calculus level). Depth-\(K\) truncated-Möbius ladders: \(V_K/\sqrt X-4=4m(K)\log X-4(l(K)+1)-16m(K)+\varepsilon\), \(|\varepsilon|\le0.062\) measured — the per-step decrement is elementary and computable, but X-uniform convergence to 4 is equivalent to \(m(K)\to0,\ l(K)\to-1\), each **PNT-equivalent**, and gap \(o(1)\) at depth \(K=X^{o(1)}\) forces \(m(K)=o(1/\log X)\): zero-free-region strength. The ladder's convergence driver is not elementary in the sense that matters.

## 4. Witness lemma (proved; constant corrected) and the cone fence (sketch)

There is a **positive, Chebyshev-admissible** measure \(d\tilde\vartheta=(1+R'(t))dt\), \(R(t)=\delta t\cos(\gamma\log t+\varphi)\), \(\gamma=\pi/\log2\), \(\delta=0.090\) (density ≥ 0.58), satisfying every profile/floor generator fact, whose bridge functional at \(z=2\) is driven to \(0.0149\sqrt X\) on a positive-density set of \(\log X\), while the profile term at \(z=2\) is \(O(1)\) — **corrected closed form** \(-2\sqrt2\,(1+\zeta(\tfrac12))\log c\approx-0.9025\) (the originally displayed \(2\sqrt2\log c\) was wrong; measured −0.9009). Consequence (fence, PROVED_SKETCH — the closure specification is informal): every inequality derivable from the generator set {Moat, Tilted Moat, Prop A, floor bounds} under {nonneg-nondecreasing-weight IBP, positive combination, c-mixing, dyadic telescope} is satisfied by \(\tilde\vartheta\), which violates WSTS-scale bounds — **the provable-positivity cone of the profile calculus cannot prove WSTS**. Register as a fence observation; a formal closure theorem would need the operation set pinned.

## 5. Three-crossing warning (numerical, independently confirmed — load-bearing for general-c work)

For \(c\in[0.44,0.47]\) the dyadic-difference profile \(E_c\) has **three** sign changes (θ ≈ 0.1395/0.1458/0.1519 at c = 0.45), versus a single crossing at \(c\in\{1/3,0.4,1/2\}\). Theorem S / T-90002 is unaffected (realized \(c=\lfloor X/2\rfloor/X\in[0.49,0.5)\)), but **any general-ratio telescope (e.g. 2/3-Mertens-mutation variants) must not assume single-crossing**. Recorded here so no future wave trips on it.

Artifacts: `scratchpad/b2_cfamily.py` (note: check-(4) printout shows max of \(-H_{a,b}\) with an inverted comment — the claim's orientation is right and is a 2-line consequence of J monotone; fix the print before reuse), `adv_b_review.py` (independent crossing/Mellin/identity checks).
