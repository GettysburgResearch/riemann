# T-90003 — GFEP holds for all n > X/10; the uniform bottom sign pattern is RH-hard

Claim ID: `T-90003` (provisional range; allocate at registry)
Status: **PROVED (with two certified finite gates; adversarially reviewed this session — one ε-constant repaired and re-certified, one scope line added per review)**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`, Strike B prong B1 + adversarial review
Date: 2026-08-09
Extends/repairs: `T-28001`/`L-28001`/`L-28002` (branch `research/gpt56-sol-280-global-fragmentation-spine`), `O-90002`
Scope: proves GFEP on \(n>X/10\) (all \(X\ge4\)); proves the open core is exactly \(n=o(X)\); no RH claim

## 1. Cell calculus for the critical source (Lemma 1, proved)

\(U_X(m)=X^{-1/2}\tilde U(m/X)\) with \(\tilde U(\theta)=\sum_{k\le1/\theta}\mu(k)(k\theta)^{-1/2}\log\frac1{k\theta}\), and **exactly**
\[
R_X(m)=X^{-1/2}\int_{m/X}^{(m+1)/X}t^{-3/2}\,C_{\lfloor1/t\rfloor}(\log\tfrac1t)\,dt,\qquad
C_N(L)=(1+\tfrac L2)M_N-\tfrac{A_N}2,
\]
\(M_N=\sum_{k\le N}\mu(k)/\sqrt k\), \(A_N=\sum_{k\le N}\mu(k)\log k/\sqrt k\). (Machine-verified to 1e-27 incl. knot-crossing windows.)

## 2. Sign structure (Lemma 2, proved)

\(C_N>0\) on cells \(N=1..4\) — e.g. \(C_2(L)=(1-\tfrac1{\sqrt2})(1+\tfrac L2)+\tfrac{\log2}{2\sqrt2}>0\) termwise — hence \(R_X(m)\ge0\) for \(\lceil X/5\rceil\le m\le X\) (`L-28002` independently re-proved; **repair**: its displayed \(C_2\) minimization is unnecessary and its slope claim is wrong-way; termwise positivity settles it). \(C_N<0\) on every cell \(N=5..40\) (88 certified endpoint enclosures + linearity in \(L\)): the **first proved negativity range** below the top fifth.

## 3. Landau fence (Theorem 3, proved — the deliverable's sharpest edge)

The uniform bottom pattern "\(R_X(m)\le0\) for all windows inside \((0,1/5]\), all \(X\)" (observed in every scan) **implies RH**: it forces \(D(t)=C_{\lfloor t\rfloor}(\log t)\le0\) for \(t\ge5\), whose exact transform is
\[
\int_1^\infty D(t)\,t^{-s-1}dt=\frac{2s+1}{2s^2\,\zeta(s+\tfrac12)},
\]
and Landau one-sidedness plus \(\zeta<0\) on the real segment \((\tfrac12,1)\) excludes off-line zeros. (Converse under RH additionally needs convergence of \(\sum\mu(k)/\sqrt k\) — open even under RH; the pattern is **RH-hard, not RH-equivalent**.) Consequence: the GFEP programme's "Layer-B" input is RH-hard at unbounded ratio; only fixed-ratio bands are elementary.

## 4. Top determinism (Theorem 4, proved, scoped to 2n ≥ X)

For \(2n\ge X\): \(\Sigma_{X,n}(p)=pR_X(p)\) **exactly**; the global minimum cell of all scans is the deterministic value \(\Sigma_{X,\lfloor X/2\rfloor}(X-1)=\sqrt{X-1}\log\frac X{X-1}\sim X^{-1/2}\). No \(\vartheta\)-errors exist anywhere in the top region (\(U\) is Möbius-free \(w\)-differences for \(m>X/3\)): **the \(X^{-1/2}\) tightness carries zero arithmetic sensitivity.** (Odd-\(X\) \(n=\lfloor X/2\rfloor\) has one extra positive far term; statement scoped to \(2n\ge X\).)

## 5. Main theorem (proved, with certified gates; ε-constant repaired on review)

**For every \(X\ge4\) and every \(n\) with \(X/10<n<\lceil X/5\rceil\), \(\Sigma_{X,n}(p)\ge0\) for all band \(p\); combined with §2, GFEP holds for ALL \(n>X/10\).** Proof: exact last-far-state decomposition \(\Sigma(p)=pR(p)+\sum_{m''\in\mathrm{Par}(p),\,m''\ge2n}G(m'')Q(m'',p)\) (verified independently to 8e-17; \(G\) is \(n\)-independent above \(2n\)); all far sources positive there (§2); a certified piecewise occupancy minorant \(\gamma\ge0\) on a knot-aligned grid over \([1/5,1]\) by descending induction on the always-present parents (\(Q(2m')=\tfrac12\) exact; \(Q(2m'+1)\ge\tfrac14-\tfrac5{4X_0}\) — **the repaired ε, valid uniformly for \(p>X/10\)**; 3-family \(\ge\tfrac16\) each); 600 certified band inequalities give \(\sqrt X\,\Sigma\ge0.832\) for \(X\ge2000\) (re-certified after the ε-fix); finite exact gate for \(X<2000\) (199,597 pairs, min \(\sqrt X\Sigma=2.790140\)). For \(p\ge\lceil X/5\rceil\): \(pR(p)\ge0\) (§2) and \(G\ge0\) close it directly (scope line added per review). **First proved GFEP region where positivity is carried entirely by recombined ancestry over a wholly negative diagonal — the Perron–Frobenius pattern validated at theorem level.**

## 6. Extension and the determinism boundary

Band 2 (\(n>X/20\)): float prototype clears with worst margin +1.51 — NUMERICAL_ONLY; the certified version needs honest \(Q\) upper bounds on negative-\(\gamma\) image cells (worked out, not certified). **Determinism boundary (proved):** \(\Sigma_{X,n}\) touches Möbius data only through \(C_N\), \(N\le X/n\); GFEP at \(n\ge\delta X\) is a finitely-many-cell deterministic inequality per fixed \(\delta\) — provable by this machinery — while uniformly in \(n\) it needs \(C_N\) at unbounded \(N\), where by §3 even the source *sign* is RH-hard. **The open core of GFEP is exactly \(n=o(X)\).**

## 7. Artifacts

`experiments/X-90004-gfep-certificates/`: `cells.py`, `exactR.py`, `certify.py`, `certified_band2_fixed.py` (the ε-repaired certificate, worst band margin 0.8326), `smallX.py`, `sigma_struct.py`, `adv_b_review.py` (independent review implementations). All re-run by the adversarial reviewer; every load-bearing identity independently re-implemented.
