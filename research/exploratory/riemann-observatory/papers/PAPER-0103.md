# PAPER-0103 — Higher correlations and the alternative hypothesis

| Field | Value |
|---|---|
| Authors | Lagarias, Jeffrey C.; Rodgers, Brad |
| Year / stratum | 2020 / S6 |
| Venue | Q. J. Math. 71, No. 1, 257-280 (2020). |
| Identifiers | zbMATH [1439.11216](https://zbmath.org/?q=an:1439.11216) · DOI [10.1093/qmathj/haz043](https://doi.org/10.1093/qmathj/haz043) · arXiv [1905.12123](https://arxiv.org/abs/1905.12123) |
| MSC | 11M26, 11M50 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1905.12123 |
| Selection | score 4.312, in-pool citations 5, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Can the Alternative Hypothesis (AH: normalized consecutive spacings of zeta zeros lie within o(1) of half-integers) be ruled out by the currently proved band-limited n-level correlations (Montgomery n=2, Hejhal n=3, Rudnick-Sarnak n>=3, all under RH)? Answer: no. They build an explicit AH-compatible point process (a randomly translated 1/2-discrete sine process on (1/2)Z) matching those correlations exactly, and a deterministic sequence in (1/2)Z with the same property.

**Historical motivation.** The Alternative Hypothesis (Conrey-Ghosh-Gonek, Baluyot, Farmer-Gonek-Lee) is a model in which gaps are never smaller than about 1/2, hence it would imply no Landau-Siegel zeros and a strong form of non-GUE rigidity. Because the pair-correlation theorem of Montgomery only reaches |xi|<1 where K_Alt and K_GUE agree, it was known AH is compatible with pair correlation; the question was whether the higher correlations (Hejhal, Rudnick-Sarnak) add enough information.

### Main results

- **THM-PAPER-0103-1** (Theorem 3.1, theorem (counterexample to the sufficiency of known correlations), scope: asymptotic; Section 3, p.4; proof Section 5.2). There exists a deterministic sequence $\{c_j\}_{j\in\mathbb Z}\subset\mathbb R$ with $c_{j+1}-c_j\in\{\tfrac12,1,\tfrac32,2,\dots\}$ for all $j$, such that for every $\varphi\in\mathcal S(\mathbb R)$, $\lim_{T\to\infty}\frac1T\int_T^{2T}\sum_j\varphi(c_j-t)\,dt=\int_{\mathbb R}\varphi$, and for every $n\ge2$ and every $\eta\in\mathcal K_n$, $\lim_{T\to\infty}\frac1T\int_T^{2T}\sum^{\ne}_{j_1,\dots,j_n}\eta(c_{j_1}-t,\dots,c_{j_n}-t)\,dt=\int_{\mathbb R^n}\eta(x)\det_{1\le i,j\le n}[S(x_i-x_j)]\,d^nx$, where $S(x)=\sin(\pi x)/(\pi x)$ and $\mathcal K_n=\{\eta\in\mathcal S(\mathbb R^n):\operatorname{supp}\hat\eta\subset\{\xi:\xi_1+\dots+\xi_n\ne0\ \text{or}\ |\xi_1|+\dots+|\xi_n|<2\}\}$.
- **THM-PAPER-0103-2** (Theorem 4.7 (AH point process), theorem, scope: global; Section 4.5, pp.9-10; full-generality n-point formula in Remark 4.8, eq. (18)). Let $(w_j)$ be the $\tfrac12$-discrete sine process on $\tfrac12\mathbb Z$ and $\omega\sim U[0,\tfrac12)$ independent. Then $(\tilde w_j)=(w_j-\omega)$ is a simple, $\mathbb R$-translation-invariant point process, all pairwise distances lie in $\{\tfrac12,1,\tfrac32,\dots\}$, and for all $n\ge1$ and all $\eta\in\mathcal K_n$, $\mathbb E\sum^{\ne}\eta(\tilde w_{j_1},\dots,\tilde w_{j_n})=\int\eta\det[S(x_i-x_j)]\,d^nx$.
- **THM-PAPER-0103-3** (Lemma 4.6, lemma (band-limited agreement), scope: asymptotic; Section 4.4, pp.7-8). Let $(w_j)$ be the $a$-discrete sine process, $0<a\le\tfrac12$. For $n\ge1$ and $\eta\in\mathcal S(\mathbb R^n)$ with $\operatorname{supp}\hat\eta\subset[-\tfrac1{2a},\tfrac1{2a}]^n$: $\mathbb E\sum^{\ne}\eta(w_{j_1},\dots,w_{j_n})=\int\eta\det[S(x_i-x_j)]\,d^nx$.
- **THM-PAPER-0103-4** (Proposition 4.3, proposition (existence), scope: global; Section 4.3 p.6; proof in Appendix A via Macchi's theorem (Thm A.1)). For each $0<a\le1$ there is a point process on $a\mathbb Z$ with $\mathbb E\sum^{\ne}\varphi(w_{j_1},\dots,w_{j_n})=a^n\sum_{k\in(a\mathbb Z)^n}\varphi(k)\det[S(k_i-k_j)]$ for all $n\ge1$, $\varphi\in C_c(\mathbb R^n)$. Existence fails for $a>1$ (Remark A.3).
- **THM-PAPER-0103-5** (Theorem 5.3 / Lemma 5.2, theorem (ergodic transfer), scope: asymptotic; Section 5, pp.10-11). The sequence $X_\ell=(w_j-\ell/2)$ of shifts of the $\tfrac12$-discrete sine process is stationary and ergodic (Lemma 5.2, proved in Appendix A.2 from Theorem A.4). Hence almost surely, for all $n\ge1$ and all $\varphi\in\mathcal S(\mathbb R^n)$: $\lim_N\frac1N\sum_{\ell<N}\sum^{\ne}\varphi(w_{j_1}-\ell/2,\dots,w_{j_n}-\ell/2)=(1/2)^n\sum_{k\in(\frac12\mathbb Z)^n}\varphi(k)\det[S(k_i-k_j)]$.
- **THM-PAPER-0103-6** (Proposition 4.4, proposition, scope: global; Section 4.3, p.6). For $0<a\le1$ the $a$-discrete sine process is simple (a.s. no point has multiplicity >1), proved from the vanishing of the 2x2 determinant on the diagonal.
- **THM-PAPER-0103-7** (Theorem B.1 (stated), theorem (gap probabilities), scope: global; Appendix B, p.~20+; referenced in Section 3). Closed-form gap probabilities for the AH point process, equal to those of the 1/2-discrete sine process (Section 3 statement; derived via the determinantal gap-probability tool Theorem B.2). Exact formula not extracted in this reading.

### Key definitions

- Normalized zeros $\tilde\gamma_j=\gamma_j\log|\gamma_j|/(2\pi)$
- GUE Hypothesis (Conj. 2.1) with sine-kernel determinants
- Alternative Hypothesis (Conj. 2.2): $\tilde\gamma_{j+1}-\tilde\gamma_j=h_j+o(1)$, $h_j\in\{\tfrac12,1,\tfrac32,\dots\}$
- Form factors $K_{Alt}(\xi)=\delta_0+2|\xi|$ on $[-1,1]$ extended periodically vs $K_{GUE}=\delta+\min(|\xi|,1)$
- a-discrete sine process; AH point process $(w_j-\omega)$
- Band-limited class $\mathcal K_n$

### Principal lemmas

- **THM-PAPER-0103-L1** (Step 1 inside Lemma 4.6 (eq. 13); p.7-8). The sine determinant $\det[S(x_i-x_j)]$ has no Fourier frequencies outside $[-1,1]^n$: for $g\in\mathcal S(\mathbb R^n)$ with $\hat g=0$ on $[-1,1]^n$, $\int g\det[S(x_i-x_j)]=0$. Proof: expand determinant over permutations, use $S=\widehat{1_{[-1/2,1/2]}}$, so frequencies are $\xi_i-\xi_{\sigma^{-1}(i)}$ with modulus <=1. — *Role:* Makes the Poisson-summation identity hold exactly (all aliases k in (a^{-1}Z)^n\{0} fall outside the support) for a<=1/2.
- **THM-PAPER-0103-L2** (Decomposition K_n subset I_n + J_n (proof of Thm 4.7); p.9-10). $I_n=\{\eta:\operatorname{supp}\hat\eta\subset\{\sum\xi_i\ne0\}\}$ and $J_n=\{\eta:\operatorname{supp}\hat\eta\subset[-1,1]^n\}$; $\mathcal K_n\subset I_n+J_n$. On $I_n$ both sides vanish because $\int\eta(x-t\mathbf 1)dt=0$ and the sine determinant is translation-invariant; on $J_n$ Lemma 4.6 plus averaging over the random shift gives equality. — *Role:* Reduces the full Rudnick-Sarnak support region to the two cases that can be handled; this is where the random translation omega is used.
- **THM-PAPER-0103-L3** (Lemma 4.1; p.5-6). A point process is determined by its correlation functions when these satisfy the stated growth condition (cites Lemma 4.2.6 of Hough-Krishnapur-Peres-Virag). — *Role:* Gives uniqueness, used to prove translation invariance of the discrete sine process (Prop. 4.5).
- **THM-PAPER-0103-L4** (Proposition 4.5; p.7). The $a$-discrete sine process is invariant under translations by $a\mathbb Z$. — *Role:* Needed for stationarity in the ergodic argument and for R-invariance after random shift.
- **THM-PAPER-0103-L5** (Remark A.3; Appendix A, ~p.18). For a>1 the operator K with kernel S on a Z no longer satisfies 0<=K<=1, so no determinantal process exists; the range a<=1 is sharp. — *Role:* Shows that the lattice-spacing a=1/2 construction is not improvable to a>1 by this route.

### Proof architecture

(1) Existence of the a-discrete sine process on aZ with correlation determinants of the sinc kernel via Macchi's theorem (operator with kernel S restricted to aZ has spectrum in [0,1] iff a<=1); simplicity and aZ-translation invariance. (2) Lemma 4.6: for eta band-limited to [-1/(2a),1/(2a)]^n, Poisson summation on (aZ)^n against eta*det[S] collapses to the n-fold integral because det[S] has Fourier support in [-1,1]^n. This forces a<=1/2 (a=1/2 used). (3) Random shift omega~U[0,1/2) yields R-invariance; split K_n into I_n (trivial, sum xi nonzero) and J_n (Lemma 4.6), giving Theorem 4.7. (4) Ergodicity of the shift sequence (Appendix A.2, Theorem A.4 on translation-invariant determinantal processes on aZ) plus Birkhoff, with a countable-dense-set argument for simultaneous validity over all n and phi in S(R^n), gives a single deterministic configuration (Theorem 5.3), then averaging over t in [0,1/2) and converting N/2-averages to T..2T averages yields Theorem 3.1. Imported: Macchi's theorem, ergodic theorem, HKPV uniqueness lemma, and (for context only) Theorem 2.4 of Montgomery/Hejhal/Rudnick-Sarnak.

Dependency edges: CAND-01989 → Montgomery 1973 pair correlation (shows the n=2 band-limited theorem cannot exclude AH); CAND-01989 → Hejhal 1994 triple correlation / Rudnick-Sarnak 1996 n-level (shows these band-limited results are all consistent with AH); CAND-01989 → Tao 2019 blog/note (independent, via CUE and symmetric functions) (parallel independent result); CAND-01989 → Farmer-Gonek-Lee (zeros of xi') (proposed route to disprove AH; paper notes xi' spacings as an alternative); CAND-01989 → Lagarias-Rodgers companion paper [20] (general a,B bandlimited matching) (extension announced)

**Imported results.** Macchi (1975) characterization of determinantal processes with kernel 0<=K<=1 (Theorem A.1); Hough-Krishnapur-Peres-Virag, Lemma 4.2.6 (uniqueness from correlation functions); Birkhoff ergodic theorem (Billingsley 28.4); Montgomery 1973, Hejhal 1994, Rudnick-Sarnak 1996 band-limited correlation theorem (Theorem 2.4, under RH) - used only to define the target class K_n; Kuna-Lebowitz-Speer realizability framework (context)

**Techniques.** determinantal point processes (Macchi existence criterion); Poisson summation on lattices; Fourier support analysis of the sine-kernel determinant; random translation to restore R-invariance; Birkhoff ergodic theorem for point-process shifts and density argument in l^1; pair/higher-order form factor comparison (K_Alt vs K_GUE)

## Context and interpretation

**Importance and obstacle overcome.** Shows that a natural route to proving a spacing result (excluding AH by correlations known under RH) is blocked: no argument that uses only the proved band-limited n-level correlations (supp of Fourier transform in {sum xi != 0} or {sum|xi|<2}) can rule out AH. The obstacle overcome is realizability: producing a genuine lattice-supported process whose correlations equal sine-determinants against the whole class, which works because the sine determinant has Fourier support in [-1,1]^n and lattice spacing 1/2 aliases only at frequency 2.

**Relation to prior work.** Complements Baluyot (form factor under AH), Farmer-Gonek-Lee (xi' spacing), Carneiro et al. and Goldston-Turnage-Butterbaugh (small-gap results using pair correlation) and Kuna-Lebowitz-Speer (realizability). Independent of and parallel to Tao's construction via finite CUE. Does not touch RH itself: it is a barrier result showing which hypotheses are insufficient.

**Limitations and open questions.** The sequence {c_j} is non-explicit (existence via ergodic theorem). Uniqueness of the AH process among processes on (1/2)Z with these correlations is open (paper expects non-uniqueness; asks as in Question A.5 of Aistleitner et al. type reference [1]). Open: optimal band-limit B for a general lattice aZ (companion paper); a process matching the Sodin process Si_0 for zeros of xi'; whether extending Theorem 2.4 to the closed region |xi|_1<=2 or beyond sum|xi|<2 would exclude AH. Nothing here says anything about zeros of zeta themselves, only about sufficiency of known correlation data.

**Ideas in remarks/appendices/abandoned paths.** Remark 4.8 gives all n-point correlations of the AH process against all Schwartz test functions (not just K_n), a concrete non-GUE target for testing future higher-correlation theorems. Section 6 asks the same band-limited matching for the process Si_0 of Sodin modelling xi' zeros under RH+GUE. Appendix B computes the exact gap distribution of the AH process (usable as a null model for spacing statistics).

## Research potential

- **Hypotheses that might be weakened.** Lemma 4.6 needs only band limit 1/(2a) with a<=1/2; any result extending Rudnick-Sarnak beyond sum|xi_i|<2 (e.g. to the boundary, or n=2 beyond |alpha|<1 unconditionally in a narrow range) would, by the same Poisson-summation obstruction, immediately start to exclude the a=1/2 lattice. The threshold 2 in Theorem 2.4 is exactly the aliasing frequency 1/a=2 of this construction.
- **Generalizations.** Replace the sine kernel by Bessel/Airy/other determinantal kernels to treat symplectic/orthogonal families (Katz-Sarnak) with the analogue of AH; replace (1/2)Z by general lattices aZ with a<1/2 or non-lattice quasi-crystals; build processes with spacings in a set like {1/2,1,3/2,...} but also matching n-point correlation beyond K_n by relaxing translation invariance.
- **Candidate connections.** Pair with Carneiro-Chandee-Chirre-Milinovich (CAND-01897) and Baluyot et al. (CAND-02364): the small-gap/simple-zero results via pair correlation are sharp barriers relative to AH; the 0.606894 small-gap constant and lim inf <=0.50412 are near the AH value 1/2, so any improvement toward 1/2 interacts directly with this counterexample. Link to the Rodgers-Tao de Bruijn-Newman Lambda>=0 argument via zeta-zero statistics under heat flow, and to Farmer-Gonek-Lee xi' spacing as a candidate discriminating statistic.
- **Reusable lemmas.** Lemma 4.6 (Poisson summation with Fourier-support of sine determinants) is reusable for any test-function-restricted comparison of lattice vs continuous determinantal processes; the I_n+J_n decomposition is reusable for any translation-averaged statistic; Theorem 5.3's density trick gives a deterministic sequence from any ergodic discrete process.
- **Possible experiments.** Numerically sample the 1/2-discrete sine process (via Macchi/L-ensemble sampling on a finite window of (1/2)Z) and compare its empirical 2-, 3-, 4-level form factors with Odlyzko zeta-zero data at heights ~10^22 to quantify how far beyond K_n the AH process diverges; compute the first test functions with supp of Fourier transform just outside the Rudnick-Sarnak region that separate AH from GUE and estimate the minimal such region.
- **Risks / barriers.** This is a negative/obstruction result; it cannot by itself contribute to RH. Any correlation-based exclusion of AH must use test functions outside K_n, which requires input beyond RH-conditional Montgomery/Rudnick-Sarnak methods (e.g. Landau-Siegel zero considerations, or xi' spacings).

## Audit notes (Level 1 reader)

none noticed in inspected portion. Minor: Lemma 4.6's footnote 7 handles the a=1/2 boundary only for Schwartz eta by noting eta-hat vanishes on the boundary of [-1,1]^n; the final step of Section 5.2 (equivalence (25) of N/2-averages with T..2T averages) is stated with 'We omit the details'. The proof that K_n is contained in I_n + J_n is asserted without an explicit partition-of-unity argument.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01989`; harvest queries: kw_pair_correlation, kw_zeta_zeros, msc_11M26, msc_11M50, arxiv_pair_corr, arxiv_zeta_zeros.
- Triage decision: include — Higher correlations and the alternative hypothesis, ruling out Montgomery-type exotic spacing.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
