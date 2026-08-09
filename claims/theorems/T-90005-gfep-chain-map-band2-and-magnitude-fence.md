# T-90005 — GFEP ⇒ RH chain map (exact), band-2 certification (n > X/20), and the magnitude-promoted Landau fence

Claim ID: `T-90005` (provisional range; allocate at registry)
Status: **CHAIN MAP PROVED; BAND-2 GATE CERTIFIED (adversarially re-run); DOMINANCE ROUTE REFUTED WITH PROOF; conditional-reduction salvage DOWNGRADED TO DEAD_END on review — RH REMAINS UNPROVED**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`, final-pass Thrust 2 (2 prongs + adversarial review with independent re-implementations)
Date: 2026-08-09
Extends: `T-90003`; repairs its band-1 occupancy minorant (missing third binary parent `2c−1`, `Q ≥ 1/4` exact — sound for occupancy states)
Scope: one proved implication chain, one certified extension, two proved impossibility results; no unconditional RH claim

## 1. The chain map (proved): GFEP-full ⇒ RH through exact algebra

\[
\text{GFEP}\ \Rightarrow\ A_X(n)\ge0\ \forall n\ \xRightarrow{\text{L-23811 exact column identity}}\ \text{BCT certificate, unused capacity }\Delta_X=0\text{ exactly}
\]
\[
\xRightarrow{\text{L-23814}}\ \sum_nA_X(n)\sqrt n=O(\log^2X)\ \xRightarrow{\text{L-23809 Dirichlet+Stirling}}\ \text{entropy packing}\ge4\sqrt X-O(\log^2X)
\]
\[
\xRightarrow{\text{L-23808 Kummer/Legendre}}\ \sum_{p^a\le X}\Lambda(p^a)p^{-a/2}\log\tfrac X{p^a}\ge4\sqrt X-O(\log^2X)\ \xRightarrow{\text{Landau (T-90001 §4 consumer)}}\ \text{RH}.
\]
Every arrow downstream of GFEP is finite exact algebra or elementary estimation except the final Landau transfer. **GFEP-full is therefore a second one-statement RH-sufficient hinge**, joining the one-scalar \([T^s(2)]_+\). Moreover: partial GFEP (any fixed band or \(n\ge X^\delta\)) feeds the chain **nothing** — the residual bottom-scale column load is uncontrolled without VK-invisible cancellation; the next gap after any band extension is always the same bottom one-sidedness.

## 2. Band-2 certificate (proved; adversarially re-run, full Q-inventory audited)

For all \(X\ge2000\), all \(X/20<n\le X/10\), all band \(p\): \(\sqrt X\,\Sigma_{X,n}(p)\ge1.3788\) (interval gate, uniform in X, honest Q upper bounds, sign-aware fluxes); exact finite gate \(20\le X\le1999\) over 9,999,990 triples, min \(\sqrt X\Sigma=4.826247\) at \((1960,196,391)\). Occupancy positivity certified through the first dead-zone octave (\(\gamma_B\ge2.69\) on \([1/10,1/5)\)). **GFEP now stands proved for all \(n>X/20\).** Treadmill corollary (sketch): each further band is certifiable (~+8.99 room for band 3) but buys one octave; by §3 the certified-margin route can never become uniform in \(n\).

## 3. The dominance refutation (proved) and the magnitude-promoted fence

The session's octave-race conjecture (branching \(2^g\) vs source \(2^{g/2}\)) was **mis-bookkept**: deep sources ride the same transport amplification \(2^{g-\nu}\) as top sources, so \(2^g\) cancels from every dominance inequality. What remains is resource \(\tau(2^{-g_0})=4m(2^{g_0})+B\)-term (a **Möbius tail**, geometric decay only under quasi-RH; even its **sign** is unknowable at VK strength) versus budget \(\sigma(g_0)\sim e^{-cg_0^\lambda}\), \(\lambda<1\): budget/resource \(\ge e^{0.3466\,g_0-cg_0^\lambda}\to\infty\) at every cutoff. **Fence (promoted from T-90003 §3):** no sign-free (magnitude-only) transport argument can prove GFEP below fixed ratio; closing the race requires \(M(x)\ll x^{1-\delta}\) — a zero-free half-plane. The review strengthened it further: **even RH-strength magnitude bounds do not close GFEP by majorants** — the truth at \(n=o(X)\) is a cancellation identity at the razor's edge (measured cumulative |neg|/pos margin climbs \(0.156\to0.804\to0.948\) toward \(\sim1.00\) as \(n\) descends; GFEP itself held at every tested point). The salvage "conditional reduction (GL)+(MD)" is **DEAD_END as stated** (review): the signed floor from two-sided occupancy alone goes negative from \(g_0\approx6\) (the true floor is carried by unstated cross-octave profile proportionality, correlations 0.93–0.998), and the rate arithmetic fails for every \(\delta\) (\(\delta<1/2\) unsatisfiable; \(\delta>1/2\) false by Ingham's \(m(y)=\Omega_\pm(y^{-1/2})\); \(\delta=1/2\) fails by ~16×). Sanity check that caught it: the claim plus §1 would have proven "zero-free half-plane ⇒ RH".

## 4. Gems retained

- **PNT-tie identity (proved, with the exact boundary term derived in review):** \(\int_0^1t^{-1/2}C_{\lfloor1/t\rfloor}(\log\tfrac1t)\,dt=4\sum_{k\ge1}\mu(k)/k=0\) exactly; finite form \(\tau(\theta)=4m(1/\theta)+B(\theta)\) with \(B(\theta)=-\sqrt\theta[(4+L)M_K-A_K]\) exact (the \(\Theta(\sqrt\theta L)\) size of \(B\) is **conditional** on \(M_K\asymp-c\), \(A_K=O(1)\) — open; flagged per review).
- **Leak accounting (proved):** first-entrance overshoot occurs only via the a3-child of \(m\in[2n,3n-3]\), weight \(\le1/6+1/(6n)\); window in-flow \(\ge5/6-o(1)\) of source mass above \(2n\) (measured 0.899).
- **Deep-margin scaling law (numerical):** \(\min_p\Sigma_{X,n}(p)\approx0.37\,n^{-1/2}(\log(X/n)+2)\), matching to ~10% across tested ranges — GFEP at \(n=o(X)\) is empirically true to Möbius-tail precision and unprovable by majorants: both facts now quantified.

## 5. Net assessment for the campaign

The pass's two thrusts converge on one statement: **both remaining hinges — the one-scalar \([T^s(2)]_+\) (T-90001/T-90002) and GFEP at \(n=o(X)\) (here) — are the same Möbius-tail one-sidedness at √-scale, now measured at the razor's edge.** No unconditional proposal exists; what exists is two independent one-statement gates, each with a fully proved exact consumer to RH, a certified deterministic frontier (\(n>X/20\); all \(z>Y\)), and impossibility theorems covering every majorant-, transport-, spectral-, flow-, and cone-shaped attack attempted by either model family. Artifacts: `experiments/X-90004-gfep-certificates/` (`certified_band2_gate.py`, `smallX_band2.py`, `race_octaves.py` + the reviewer's independent `rev2_indep.py`, `rev2_signedfloor.py` in scratchpad); journals `wf_f52d0745-0c5`.
