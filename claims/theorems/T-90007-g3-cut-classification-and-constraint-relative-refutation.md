# T-90007 — G3 classification: every GFEP cut value is a Möbius-tail functional; positive-kernel form; constraint-relative refutation of structural closure

Claim ID: `T-90007` (provisional range; allocate at registry)
Status: **§1 CLASSIFICATION PROVED (complete finite algebra); §3 REFUTATION PROVED (finite certificates, two independent code paths, dps40); §2 kernel positivity NUMERICAL_ONLY/CONJECTURED; §4 calibration NUMERICAL_ONLY; net verdict WALL_RENAMED — no RH claim**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`, final dispatch Prong G3 (embedded skeptic)
Date: 2026-08-09
Extends/consumes: `T-90003` (source cell calculus), `T-90005` (§4 PNT-tie), `T-90006` (Lemmas 1–2, Theorems A–B) — definitions unchanged. Notation: \(W,F,V,Q,S,L,\mathcal C_n,H_p,g,\mathrm{Leak}_n\) as in T-90006 §0–2; \(m(y)=\sum_{k\le y}\mu(k)/k\), \(M_N,A_N,C_N\) as in T-90003 §1.

## 1. Theorem 1 (the τ dictionary; proved) — the pre-positioned classifier

Let \(\varepsilon:\{\text{squarefree }k\}\to\mathbb R\) be **arbitrary** (the true \(\mu\) is one instance) and let \(C^\varepsilon_N,M^\varepsilon_N,A^\varepsilon_N,m_\varepsilon\) be the corresponding tails.

**(a) Sign-universal PNT-tie.** With \(F(t,N):=\sqrt t\,[(4+\log\tfrac1t)M^\varepsilon_N-A^\varepsilon_N]\):
\[\tau_\varepsilon(\theta):=\int_\theta^1 t^{-1/2}C^\varepsilon_{\lfloor1/t\rfloor}(\log\tfrac1t)\,dt\;=\;4\,m_\varepsilon(1/\theta)-F(\theta,\lfloor1/\theta\rfloor).\]
*Proof.* \(\partial_t F(t,N)=t^{-1/2}C_N(\log\frac1t)\) (direct differentiation); at the knot \(t=1/N\), \(F(1/N,N-1)-F(1/N,N)=-4\varepsilon(N)/N\); telescope over cells from \(\theta\) to 1, with \(F(1,1)=4\varepsilon(1)\). ∎
So H2's finite form \(\tau=4m+B\) is **universal algebra with zero arithmetic content**: it constrains an adversarial source not at all; all arithmetic lives in the tail *values*.

**(b) Threshold evaluation.** For every \(k\): \(\langle S,\mathbf 1_{[k,X]}\rangle=\sum_{m\ge k}mR_X(m)=kU_X(k)+\sum_{m>k}U_X(m)\) (Abel; \(U_X(X{+}1)=0\)) and, splitting \(m=tX-\{tX\}\) in T-90003 §1's integral form,
\[\langle S,\mathbf 1_{[k,X]}\rangle=\sqrt X\,\tau_\mu(k/X)\;-\;X^{-1/2}\!\!\int_{k/X}^1\{tX\}\,t^{-3/2}C_{\lfloor1/t\rfloor}(\log\tfrac1t)\,dt,\]
with \(kU_X(k)=\sqrt{X\theta}\,[LM_K-A_K]\), \(K=\lfloor X/k\rfloor\): every piece an explicit finite Möbius-tail functional. ∎

**(c) Window-trace decomposition.** By T-90006 Lemma 2 with \(h\equiv1\): \(\sum_{p\in W}\Sigma(p)=\langle S,\mathbf 1_{[n,X]}\rangle-\mathrm{Leak}_n\). Hence for any certificate \(h\in\mathcal C_n\) with trace mean \(\bar h\) on \(W\):
\[\langle S,h\rangle=\bar h\Big[\sqrt X\,\tau_\mu(n/X)-(\text{sawtooth})-\mathrm{Leak}_n\Big]+\sum_{p\in W}(h(p)-\bar h)\,\Sigma(p).\]
**Classifier:** a constant-trace certificate evaluates to exactly the leak-corrected τ one-sidedness (the wall verbatim); any other trace adds a centered pairing against \(\Sigma\), which by T-90003 §6 needs \(C_N\) at unbounded \(N\le X/n\). T-90006's empirical optimal duals are Dirac traces \(H_{p^*}\) — the **maximal** disaggregation, farthest from the aggregate. ∎

**(d) Superharmonic correction.** \(\langle S,\mathbf 1_{[k,X]}\rangle-\sum_{p\ge k}\Sigma(p)=\sum_F g(m)\mathbb P_m(Z_1<k)\): threshold one-sidedness ⇔ τ one-sidedness **modulo \(g\ge0\)** — deep occupancy positivity, the original spine wall (L-28001 G-positivity). The circle closes: threshold ⇒ τ needs the spine wall; pixels avoid \(g\) but disaggregate to the razor's edge. ∎

Machine verification (`g3_classify.py`): (a) closed form vs cell-sum, (b) both forms vs direct sums, (c) capture split — all \(\le5\cdot10^{-39}\) at \((X,n)\in\{(300,12),(1000,20),(2000,20),(2000,63),(3000,100)\}\); measured \(g\ge0\) throughout; aggregate margins huge (e.g. \(+28.7\) at \((3000,100)\)) versus per-exit \(O(n^{-1/2}\log)\) — the difficulty is pure disaggregation (exit-uniformity).

## 2. Positive-kernel form (exact identity; positivity CONJECTURED)

Abel in \(m\) (\(G_p:=pW_p\) harmonic, T-90006): \(\Sigma_{X,n}(p)=\sum_{k\,\mathrm{sf}}\mu(k)\,c^{X,n}_p(k)\), \(c^{X,n}_p(k)=\sum_{m\ge n,\,mk\le X}dG_p(m)\,w_X(mk)\) — finite, transport-defined, \(\mu\)-free kernels. **Census: \(c\ge0\) at all 9,825 tested \((p,k)\) pairs** across \((X,n)\in\{(2000,20),(3000,25),(3000,15),(4000,20),(4000,15)\}\) (`g3_adv3.py`; representation cross-checked against the independent first-entrance flow to \(7\cdot10^{-14}\), and at dps40 spot points to \(10^{-40}\)). If \(c\ge0\) holds generally (CONJECTURED), per-exit GFEP is literally: **the Möbius sequence integrates nonnegatively against an explicit family of nonnegative kernels** — Möbius one-sidedness with no remainder.

## 3. Theorem 2 (constraint-relative refutation; proved by finite certificate)

Define the adversarial source: \(\varepsilon(k)=\mu(k)\) for \(k\le40\), \(\varepsilon(k)=-1\) for squarefree \(k\in(40,X/n]\). Then (dps30–40, two independent code paths — coefficient form and first-entrance flow — agreeing to \(10^{-8}\) rel.):

- \((X,n)=(2000,20)\): \(\min_p\Sigma^\varepsilon=-0.4712\) at \(p=20\); \((3000,25)\): \(-0.8139\) at \(p=25\). **GFEP fails.**
- The assignment satisfies **every proved constraint of the campaign**: exact \(\mu\) (hence all certified cell signs \(C_N\gtrless0\), \(N\le40\), T-90003 §2) on \(k\le40\); squarefree support; \(|\varepsilon|=1\); the chain/kernel untouched; and — verified exactly, 0/424 endpoint violations — **the full RH-hard Landau bottom pattern \(C^\varepsilon_N\le0\) for all \(N\in[5,X/n]\)** (`g3_patt_check.py`). LP over the pattern-constrained class equals the free minimum (constraints slack).

**Corollaries.** (i) No argument using only {chain structure + any certified prefix + the uniform bottom sign pattern} can prove GFEP at \(n=o(X)\): the pattern (itself RH-hard, T-90003 §3) does **not** imply GFEP — GFEP strictly requires tail-**magnitude** cancellation. (ii) Prefix-death: fixing true \(\mu\) on \(k\le K_0\) revives the refutation once \(X/n\gtrsim\tfrac32K_0\) (measured: \(K_0=80\), \(K_{\max}=120\) leaves \(+0.002\) — razor-marginal; \(K_0=60\), \(K_{\max}=120\): \(-0.294\)). (iii) Locality: 5 sign flips (the \(\mu=+1\) sites \(k\in\{46,51,55,57,58\}\) just above the certified line) kill \((3000,25)\); vulnerable exits are the bottom-of-window family \(p\in[n,\sim1.3n]\) (upper-window exits unbreakable at these depths) — matching and explaining T-90006 §5's binding families; any aggregated or generic-exit argument is pre-refuted by (i)+the §1(c) aggregate/per-exit gap. (iv) G2's injection hunt (`g2_injection.py`, `g2_final_checks.py`): free/node/row sorted-domination **all fail at true \(\mu\)** at every tested deep point (even cardinality \(\#B\le\#A\) fails); consistent — had any survived, it would have proven \(\Sigma^\varepsilon\ge0\), contradicting the certificate.

## 4. Calibration (NUMERICAL_ONLY): what closing the exact LP costs

Impose only \(|m_\varepsilon(N)|\le A/\sqrt N\) for \(N\in(40,X/n]\) (√-strength, Ingham-shape) plus the certified prefix. The exact per-exit LP then closes iff \(A\le A^*(X,n)\):
\(A^*=2.48\) (\(K_{\max}{=}100\)), \(2.19\) (120), \(1.46\) (200), \(1.39\) (200, deeper \(n\)), \(1.33\) (266) — **decreasing in depth**. Since \(\sqrt N\,|m(N)|=\Omega_\pm(c)\) with (under RH+LI) unbounded limsup, a uniform-\(A\) √-tail hypothesis is eventually false while the demanded \(A^*\) falls: the exact-flow route's residual demand is precisely a uniform √-scale Möbius-tail magnitude bound — the wall, with its constant now measured per depth. Open: whether richer true-constraint families (joint \(m,M,A\)-tails) stabilize \(A^*\); any such family is again a Möbius-magnitude statement.

## 5. Net statement (WALL_RENAMED, exact)

GFEP-full \(\iff\) \(\forall X,\,n\le X/20,\,p\in W:\ \sum_{k}\mu(k)\,c^{X,n}_p(k)\ge0\) with explicit computable kernels (nonnegative at every tested point). This family is **not** a consequence of the chain structure, any finite prefix of \(\mu\), or the full RH-hard sign pattern (§3 — finite counterexample certificates); its provability from √-strength tail magnitudes alone carries a constant budget \(A^*(depth)\) that decreases while the truth's \(\sqrt N|m(N)|\) recurrently spikes (§4). Combined with T-90006 §4 (no threshold cuts) and §1(d) (thresholds ⇔ τ only through \(g\ge0\) = the spine wall), every exit from the flow recast lands on the same object: **quantitative Möbius-tail cancellation at √-scale, per exit, at unbounded depth.** The renaming is now closed under: majorants (T-90005 §3), cones/spectra (O-90006), threshold cuts (T-90006 §4), sign-pattern hypotheses and finite prefixes (here).

## 6. Artifacts

`experiments/X-90004-gfep-certificates/`: `g3_classify.py` (Theorem 1 verification), `g3_adv.py` (adversarial LP + independent flow recheck), `g3_adv2.py` (prefix scan, sparse adversary, RH-tail LP), `g3_adv3.py` (kernel census, \(A^*\) bisection, five-parent identity — exact incl. at T-90005's certified minimum (1960,196)), `g3_patt_check.py` (0/424 pattern-endpoint violations, exact).
