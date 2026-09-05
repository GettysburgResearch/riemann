# T-90006 — GFEP as exact flow feasibility: min-cut = exit-pixel family (harmonic collapse), no threshold cuts, and the pixel wall

Claim ID: `T-90006` (provisional range; allocate at registry)
Status: **DUALITY THEOREMS PROVED (complete proofs below); binding-family/renewal/margin structure NUMERICAL_ONLY; wall renamed exactly (§6) — no RH claim**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`, final dispatch Prong G1
Date: 2026-08-09
Extends: `L-28001` (spine), `T-90003`, `T-90005`; consumes their exact definitions unchanged
Scope: exact finite LP/flow formalization of GFEP per (X,n); numerics at X ≤ 10^5

## 0. Setup (fixed throughout)

Fix \(X\ge4\), \(n\ge2\). Window \(W=[n,\min(2n,X+1))\cap\mathbb Z\), nodes \(V=[n,X]\cap\mathbb Z\), far nodes \(F=[2n,X]\cap\mathbb Z\). Children of \(m\): \(a_2=\lfloor m/2\rfloor,\ b_2=m-a_2,\ a_3=\lceil m/3\rceil,\ b_3=m-a_3\); kernel \(Q(m,c)=\tfrac c{2m}\cdot\mathrm{mult}\), row-stochastic; every child \(<m\) (strict descent). Source \(S(m)=mR_X(m)\). Discrete Laplacian \(L:\mathbb R^V\to\mathbb R^F\),
\[(Lh)(m)=h(m)-\sum_{c\ \mathrm{child},\,c\ge n}Q(m,c)\,h(c),\qquad m\in F,\]
(children \(<n\) dropped = absorbed at 0: the overshoot kill). Certificate cone \(\mathcal C_n=\{h\in\mathbb R^V:h\ge0,\ Lh=0\}\). Pixels \(H_p(m)=E_n(m,p)\) (L-28001.10), \(p\in W\).

## 1. Lemma 1 (pixel basis / harmonic collapse) — PROVED

\(\mathcal C_n\) is a simplicial cone with extreme rays exactly \(\{H_p\}_{p\in W}\); every \(h\in\mathcal C_n\) is \(h=\sum_{p\in W}h(p)H_p\), i.e. a dual potential is determined by its window values.

*Proof.* First-step decomposition of the first-entrance event at \(m\in F\): a child \(c<n\) means \(Z_{\tau_n}=c\notin W\), contributing 0; a child \(c\in W\) means \(Z_{\tau_n}=c\), contributing \(\delta_{c,p}=H_p(c)\); a child \(c\in F\) continues. Hence \(LH_p=0\), and \(H_p\ge0\), so \(H_p\in\mathcal C_n\). Conversely \(L\) is triangular for the descending order: row \(m\) involves \(h(m)\) and \(h\) at children \(<m\). Ascending back-substitution determines \(h\) on \(F\) uniquely from \(h|_W\); \(h\) and \(\sum_p h(p)H_p\) satisfy the same recursion with the same window data, hence coincide. Restriction \(h\mapsto h|_W\) is thus a linear isomorphism \(\mathcal C_n\cong\mathbb R^W_{\ge0}\). ∎

## 2. Lemma 2 (Green pairing) — PROVED

Let \(g\) be the canonical far flow: \(g(m)=S(m)+\sum_{m'\in F}g(m')Q(m',m)\), \(m\in F\) (finite descending recursion; this is `full_G` of T-90005's gate, n-independent above \(2n\)). Then for **every** \(h\in\mathbb R^V\):
\[\sum_{m\in V}S(m)h(m)=\sum_{p\in W}\Sigma_{X,n}(p)\,h(p)+\sum_{m\in F}g(m)\,(Lh)(m).\]

*Proof.* By definition of first-entrance delivery, \(S(m')+\sum_{m\in F}g(m)Q(m,m')=\Sigma_{X,n}(m')\) for \(m'\in W\), and \(=g(m')\) for \(m'\in F\). Pair with \(h\) and regroup the double sum by parent \(m\):
\(\sum_{m'\ge n}h(m')\sum_m g(m)Q(m,m')=\sum_{m\in F}g(m)[h(m)-(Lh)(m)]\). ∎

Corollaries (exact): \(h\in\mathcal C_n\Rightarrow\langle S,h\rangle=\sum_p\Sigma(p)h(p)\); with \(h=H_p\): \(\langle S,H_p\rangle=\Sigma_{X,n}(p)\); with \(h=h_n\in\mathcal C_n\) (hitting potential): L-28001.12 re-derived — the strong-Markov identity **is** the conic decomposition \(h_n=\sum_p h_n(p)H_p\) into extreme rays. With \(h\equiv1\): the capture identity \(\sum_{m\ge n}S(m)=\sum_p\Sigma(p)+\sum_F g(m)\,\mathbb P_m(Z_1<n)\) (measured capture \(\approx0.883\), cf. leak \(\ge5/6\), T-90005 §4). All verified to \(\le6\cdot10^{-17}\).

## 3. Theorem A (exact LP duality; min-cut = min exit pixel) — PROVED

Consider the proportional-routing flow LP
\[(P_n):\quad\max_{y\in\mathbb R^F,\,t\in\mathbb R}t\ \ \text{s.t.}\ \ s(m'):=S(m')+\!\!\sum_{m\in F}y(m)Q(m,m')-y(m')\mathbf1_{m'\in F}\ \ge\ t\,\mathbf1_{m'\in W}\quad(m'\in V).\]
(\(y(m)\) = throughput routed through internal node \(m\), split in the fixed proportions \(Q\); \(s\) = node surplus. The only routing freedom in this network is the per-node scalar — arc ratios are frozen.) Then:

1. \(\operatorname{val}(P_n)=\min_{p\in W}\Sigma_{X,n}(p)\), attained by the canonical flow \(y=g\) (which has \(s=0\) on \(F\): the network is everywhere-saturated, mirroring the all-tight carry-LP primal of O-90004 §4).
2. The optimal dual solutions are exactly the mixtures \(\sum_{p\in\arg\min}\alpha_pH_p\), \(\alpha\) a probability vector: **the separating potentials collapse to exit pixels** (Martin boundary), by Lemma 1.
3. GFEP\((n)\iff\operatorname{val}(P_n)\ge0\iff\) the surplus system \(\{s\ge0\}\) is feasible.

*Proof.* Upper bound: for feasible \((y,t)\) and any \(p\), substitute \(S=s-Q^Ty+y\mathbf1_F\) into \(\langle S,H_p\rangle\) and regroup as in Lemma 2: \(\langle S,H_p\rangle=\langle s,H_p\rangle+\sum_F y\,(LH_p)=\langle s,H_p\rangle\ge t\,H_p(p)=t\), using \(LH_p=0\), \(s\ge t\) on \(W\) (where \(H_p=\delta_p\)), \(s\ge0\) on \(F\), \(H_p\ge0\). So \(t\le\min_p\Sigma(p)\); \(y=g\) attains it. Duality: the dual of \((P_n)\) is \(\min\langle S,h\rangle\) over \(h\ge0\), \(Lh=0\) (rows of \(y\) free), \(\sum_{p\in W}h(p)=1\) (row of \(t\)); by Lemma 1 its feasible set is the simplex \(\{\sum\alpha_pH_p\}\) with objective \(\sum\alpha_p\Sigma(p)\). (3) is immediate. ∎

Machine verification (scipy/HiGHS, `g1_lp.py`): at \(X=3000\), \(n\in\{100,149,271\}\): \(t^*=\min_p\Sigma\) to \(6\cdot10^{-17}\); the solver's dual vector equals \(H_{p^*}\) with \(\|\cdot\|_\infty\le5.6\cdot10^{-17}\), support exactly \(\{p^*\}\).

## 4. Theorem B (threshold cuts do not exist in this network) — PROVED

For \(h=\mathbf1_{[k,X]}\): \((Lh)(m)=\mathbb P_m(Z_1<k)\ge0\), strictly \(>0\) for \(m\in[k,2k)\cap F\) — threshold indicators are strictly **superharmonic**, never harmonic, hence never certificates. By Lemma 2 their cut value \(\sum_{m\ge k}S(m)=\sum_{p\ge k}\Sigma(p)+\sum_Fg(m)\mathbb P_m(Z_1<k)\) (= L-28001.8) contains the transported far mass \(g\) — evaluating a threshold cut presupposes the full unknown flow. Consequently: **the certificate cone of the GFEP network is exhausted by the exit-pixel family; no threshold/dyadic min-cut criterion exists.** The cut structure lives on the Martin (exit) boundary, not on scale thresholds — the structural reason no size-style reduction can emerge from the flow recast, consistent with the fence map (T-90005 §3, O-90004 §3). ∎

## 5. Structure of the binding cuts — NUMERICAL_ONLY (scripts `g1_scan.py`, `g1_families.py`, `g1_split.py`)

Exhaustive over \(n\in[8,X/10]\) at \(X=3000,10^4\) (1286 scales), spot-log-spaced at \(10^5\):

- **Binding families.** \(p^*\in\{n\}\) (≈38%), odd interior (≈55%), \(2n-1\) (≈7%); even interior binds once in 1286 scales (\(X{=}10^4,n{=}106,p^*{=}140\), margin gap 2.6%). Mechanism (deterministic parent-inventory depletion): bottom pixel has 5 far parents \(\{2n,2n{+}1,3n,3n{-}1,3n{-}2\}\) (its \(2p{-}1\)- and \(b_3\)-parents fall inside \(W\)), odd pixels 7, even pixels 8 (extra \(b_3\)-parent \(3p/2{+}1\)) — less inflow ⇒ binds.
- **Renewal profile of the pixel potentials.** Log-steps \(\{\log2\ (\frac12),\log\frac32\ (\frac13),\log3\ (\frac16)\}\), mean \(\bar\mu=\frac16\log2+\frac12\log3=0.664837\). Renewal overshoot predicts \(H_p(m)\approx\kappa(p/n)/(\bar\mu p)\) for \(m\gg n\) with \(\kappa=\frac23\) on \(\theta\in(1,\frac43)\), \(1\) on \((\frac43,2)\): measured \(0.60\!-\!0.70\) vs \(0.98\!-\!1.20\), jump located exactly at \(p=\lceil 4n/3\rceil\) (PROVED_SKETCH via non-lattice renewal; constants NUMERICAL_ONLY). Pointwise the potentials are arithmetically rough (cv \(\approx2\!-\!3\) over \(m\in[X/2,X]\)) — renewal holds in mean only.
- **Margin law and the Möbius regressor.** \(\sqrt n\min_p\Sigma\approx0.38(\log(X/n)+2)\) (R² 0.91–0.92 across \(X=3000..10^5\), extending T-90005 §4). Adding the signed H2-remainder \((4{+}L)M_K-A_K\) (\(K=X/n\) or \(X/2n\)) as a regressor improves R² by \(<3\cdot10^{-4}\): the margin's mean is transport-geometric, not the global Möbius remainder.
- **Razor's edge, localized.** At the binding pixel, \(\sqrt n\,\Sigma(p^*)\) = (window self-source, negative, \(-0.3..-1.9\)) + (far inflow, \(+1.8..+4.6\)); fluctuation across \(n\) is carried by the inflow (corr \(0.958\)) and anticorrelated with the self-source (\(-0.842\)): both sides are Möbius flows; the cut value is their razor-edge difference.

## 6. The wall, renamed exactly — WALL_RENAMED (deliverable)

By Theorem A and Lemma 2, with T-90003 Lemma 1's exact source form:
\[\boxed{\ \text{GFEP-full}\iff\ \forall X,\ \forall n\le X/20,\ \min_{p\in W}\ \langle S_X,H^{(n)}_p\rangle\ \ge\ 0,\qquad \langle S_X,H^{(n)}_p\rangle=X^{-1/2}\!\!\sum_{m=n}^{X}\!H^{(n)}_p(m)\,m\!\!\int_{m/X}^{(m+1)/X}\!\!\!t^{-3/2}\,C_{\lfloor1/t\rfloor}(\log\tfrac1t)\,dt\ }\]
(the range \(n>X/20\) is proved, T-90005 §2; GFEP-full ⇒ RH by the exact chain map, T-90005 §1). The min-cut **family** is deterministic — finitely many explicitly computable harmonic pixels per scale, with structured binding subfamily (§5) — but every deep cut **value** at \(n=o(X)\) pairs the full Möbius cell sequence \(C_N\), \(N\) up to \(X/n\) unbounded, against deterministic harmonic measure; by T-90003 §3 even the uniform sign pattern of those cells is RH-hard, and by T-90005 §3 no majorant evaluates the pairing. The min-cut condition is therefore **the Möbius-tail one-sidedness renamed**: "the discrete harmonic measure of every exit pixel integrates the Möbius carry flow nonnegatively." Feasibility does **not** close in the deterministic sector; what the recast contributes is exactness — the sharpest necessary subfamily being the five-parent bottom-pixel sequence
\[\Sigma_{X,n}(n)=nR_X(n)+\tfrac12g(2n)+\tfrac n{2(2n+1)}g(2n{+}1)+\!\!\sum_{m\in\{3n,3n-1,3n-2\},\,m\le X}\!\!g(m)\,\tfrac n{2m}\ \ge\ 0\]
(weight \(\tfrac12\) at \(2n\) from child multiplicity 2; verified exactly),
an exact three-term-scale recursion in which the entire RH difficulty of GFEP is (empirically ≈38% of scales, and necessarily) already present.

## 7. Artifacts

`experiments/X-90004-gfep-certificates/g1_flow.py` (Σ/pixel/hitting kernels + identity checks vs T-90005 certified minimum 4.826247 at (1960,196,391): exact), `g1_lp.py` (HiGHS LP + dual extraction), `g1_scan.py`, `g1_families.py`, `g1_split.py`. All identities verified to \(\le10^{-16}\) relative.
