# T-90004 — The Q4 gate decompiled: a ψ-window three-point criterion strictly between Montgomery and RH

Claim ID: `T-90004` (provisional range; allocate at registry)
Status: **DECOMPILATION + CONSUMER PROVED (adversarially reviewed this session, hostile re-derivation of the Landau/multiplier arrow); GATE ITSELF OPEN — STRICTLY STRONGER THAN RH; UNCONDITIONAL ROUTE CLOSED BY CALIBRATION**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`, final-pass Thrust 1 (3 prongs + adversarial review) — building on and repairing the `gpt56-sol` Q4 wave (PRs #339–#350)
Date: 2026-08-09
Repairs/extends: `L-90010`, `O-90011` (PR #350 branch `agent/gpt56-sol/346-odd-source-carry-repair`); confirms the PR #346 `L-34406` bug and the `R-90009` repair
Scope: exact identities + one proved implication; **no unconditional claim; RH remains unproved**

## 1. The decompilation (the wave's key object, made transparent — proved, 3 lines)

The Q4 "compact current" is not a Möbius window. With \(\psi_*(x)=\sum_{a\ge0}\psi_{\rm odd}(\lfloor x/2^a\rfloor)\):
\[
Q(e)=\psi_*(n)-\psi_*(j)-\psi_*(k),\qquad
\boxed{\,I_2(e)=\psi_{\rm odd}(2n)-\psi_{\rm odd}(2j)-\psi_{\rm odd}(2k)\ \ \text{exactly}.}
\]
(Proof: universal prefix law \(\mathcal L_e(f)=C_f(n)-C_f(j)-C_f(k)\) + \((\mathbf1*q_{\rm odd})(d)=\Lambda_{\rm odd}(\mathrm{oddpart}\,d)\) + the dyadic telescope. Verified exactly on 60 random rows; equivalent to the \(E=\psi-x\) form \(I_2=E(2n)-E(2j)-E(2k)-\log2\cdot Y_{\rm odd}(e)\) with \(Y_{\rm odd}=O(\log n)\) — note: **not** bounded; \(Y(2m,m)=-\lfloor\log_2m\rfloor\).) The reserve is RH-blind Stirling: \(\Delta_2R=6H(\alpha)\,n\log n+4\log2\cdot v_2\binom nj H(\alpha)n+O_\eta(n)\) (leading constant **6H**, not 4H), positive on balanced cones.

## 2. The consumer (proved; hostilely re-derived in review)

**Eventual-form gate ⇒ RH.** If \(|I_2(e)|^2\le C\,\Delta_2R(e)\) for all sufficiently large balanced rows — even only on the single ray \(j=\lceil n/2\rceil\), even with any constant \(C\), even weakened to \(|I_2|\ll n^{\theta}\mathrm{polylog}\) — then every zeta zero has \(\Re\rho\le\theta\). Mechanism: \(D(x)=\psi_{\rm odd}(2x)-2\psi_{\rm odd}(x)\) has Mellin transform \(\frac{2^s-2}{s}\bigl(-\zeta_{\rm odd}'/\zeta_{\rm odd}\bigr)(s)\); the multiplier vanishes on \(0<\Re s<1\) only if \(|2^\rho|=2\), i.e. \(\Re\rho=1\), excluded **unconditionally** by de la Vallée Poussin — no hidden RH input; Landau's oscillation theorem finishes. (Review re-derived the multiplier algebra including the \(\Delta_4\) factorization \((2^s-2)^2(2^s+2)\), boundary terms, and integer→real interpolation.)

**Quantifier warning (load-bearing).** As worded in `O-90011.1`, "cofinally" — by the repo's own glossary (`RESULTS_INDEX.md`: "extending through an unbounded sequence") — is the *frequent* reading, under which the gate is **vacuous**: with an off-line zero, phase-null rows satisfy it infinitely often. All RH content sits in the **eventual-for-all** quantifier. The gate must be restated in eventual form before any consumption.

## 3. Where the gate sits (proved placements)

- **RH does not imply the gate**: RH gives \(|I_2|^2\ll n\log^4n\), missing the \(n\log n\) budget by \(\log^3n\). Montgomery-class refinements imply it with limsup ratio 0. **The gate sits strictly between Montgomery and RH** — it may be false even if RH is true.
- **The unconditional route is dead**: the prefix law transmutes \(\mu\log\) into \(-\Lambda\) (the O-90004 duality); \(I_2\) is a ψ-window, for which Vinogradov–Korobov gives only \(n^{1-o(1)}\), and any unconditional \(n^{1-\delta}\) bound is equivalent to a zero-free strip (calibration theorem, T-90001 §5).
- **The per-cell/moat route is structurally closed**: \(\Delta_2R-|I_2|^2\) carries signed off-diagonal prime-pair terms \(\Lambda\Lambda'\) to which the moat cone is blind (L-90003), matching the wave's own generic-PSD no-go (`L-34403`).
- **Margins are a small-n artifact**: dyadic-block max ratio decays \(0.62\ (n\le100)\to\sim0.13\ (2\cdot10^4)\to0.055\) (sampled to \(10^6\)); records without the \(n\ge20\) floor: 0.624 at (16,8), Δ₄ 0.680 at (13,8). The √-normalized diagonal fluctuation does **not** decay (ψ-type), so the decay reflects the \(\log n\) reserve growth, not vanishing arithmetic content.

## 4. Verified repairs and hazards (service to the Q4 wave)

`R-90009` confirmed: \(Y_{\rm odd}(n,j)=C_2(n)-C_2(j)-C_2(n-j)\), \(Y_{\rm odd}(10,3)=-1\) vs the bugged `L-34406` value 3 (hand-checked); \((\varepsilon-\delta_2)*b_{\rm odd}=\mu\) with \(\mathcal L_{2e}(\mu)=-1\) exact; the chain recurrence and curvature identity verified (the curvature identity is definitional storage — its positivity upper-bounds nothing, as `L-90010` itself states; the odd-lane recurrence is *neutral*: delayed coefficient 2 squares to the exact scale loss 4 — no contraction). **Hazards:** claim-ID collisions (two disjoint `L-344xx` sets on PR #345 vs #346; two disjoint `L-340xx` sets on PR #341 vs #342); branch `…-v2` is stale (tip = bugged PR #346 tip; the real repair is on `-v1` at `eef62a72`).

## 5. Net assessment

The Q4 wave's true product — visible after decompilation — is a **new, clean, RH-sufficient three-point ψ-window criterion with a two-line multiplier consumer**, joining the equivalence family at Montgomery strength. It is not a proof lane: stronger than RH, unconditionally out of reach by calibration, numerically unprobeable (weak-Mertens window). Its value is (i) the sharpest statement yet of what a *stronger-than-RH* elementary gate looks like in this repo, (ii) the consumer's multiplier trick (unconditional de la Vallée Poussin anchor), reusable, and (iii) closing the "is Q4 the crack?" question decisively so no further credits chase it.

Artifacts: `experiments/X-90006-q4-decompilation/` (scan/identity scripts incl. the reviewer's `rev_verify.py`); full prong reports in workflow journal `wf_d204d825-c30`.
