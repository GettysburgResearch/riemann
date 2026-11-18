# PAPER-0036 — The de Bruijn-Newman constant is non-negative

| Field | Value |
|---|---|
| Authors | Rodgers, Brad; Tao, Terence |
| Year / stratum | 2020 / S6 |
| Venue | Forum Math. Pi 8, Paper No. e6, 62 p. (2020). |
| Identifiers | zbMATH [1454.11158](https://zbmath.org/?q=an:1454.11158) · DOI [10.1017/fmp.2020.6](https://doi.org/10.1017/fmp.2020.6) · arXiv [1801.05914](https://arxiv.org/abs/1801.05914) |
| MSC | 11M06 |
| Families | B, C, F |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1801.05914 |
| Selection | score 4.583, in-pool citations 19, seed lists 4, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Is the de Bruijn-Newman constant Lambda >= 0 (Newman's conjecture)? Equivalently, can RH be 'barely true' only: RH <=> Lambda <= 0, so the paper shows RH is equivalent to Lambda = 0.

**Historical motivation.** Newman (1976) conjectured Lambda>=0, saying that RH, if true, is 'barely so' (any perturbation of the heat flow backwards produces off-line zeros). Previous progress: Lehmer-pair based lower bounds (Csordas-Smith-Varga 1994 -4.4e-6; Odlyzko 2000; Saouter-Gourdon-Demichel 2011 -1.15e-11) approaching 0 numerically but never proving it.

### Main results

- **THM-PAPER-0036-1** (Theorem 1, theorem, scope: global; Sec.1, p.3). $\Lambda \ge 0$, where $H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du$, $\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})\exp(-\pi n^2e^{4u})$, and $\Lambda$ is the (Newman) constant with: all zeros of $H_t$ are real iff $t\ge\Lambda$.
- **THM-PAPER-0036-2** (Lemma 4, lemma, scope: asymptotic; Sec.2, p.8). For $z=x-i\kappa\log_+x$, $x\ge0$, $0\le\kappa\le C$, $\Lambda<t\le0$: $H_t(z)\ll\exp(-\pi x/8+O_C(\log_+^2x))$; and for $\kappa\ge C'$ (absolute) $H_t(z)=\exp(-\pi x/8+O_C(\log_+^2x))$ and $H_t'/H_t(z)=\frac i4\log\frac{iz}{4\pi}+O_C(\log_+x/x)$.
- **THM-PAPER-0036-3** (Theorem 9, theorem, scope: asymptotic; Sec.3, p.~18-20 (eq. 48,49)). For $\Lambda<t\le0$, $T>0$, $0\le\alpha\le C$: $N_t([0,T])=\Psi(T)+O(\log_+^2T)$ (Psi the Riemann-von Mangoldt main term $\frac{T}{4\pi}\log\frac{T}{4\pi}-\frac{T}{4\pi}$) and $N_t([T,T+\alpha\log_+T])=\frac{\alpha\log_+^2T}{4\pi}+o_{T\to\infty}(\log_+^2T)$ uniformly in alpha.
- **THM-PAPER-0036-4** (Theorem 11, theorem (quoted from Csordas-Smith-Varga), scope: local; Sec.4, eq.(56)). For $\Lambda<t\le0$ zeros $x_j(t)$ are simple, C^1 in t, and $\partial_tx_k(t)=2\sum'_{j\ne k}\frac1{x_k(t)-x_j(t)}$ (principal value sum).
- **THM-PAPER-0036-5** (Proposition 13, proposition, scope: asymptotic; Sec.4). For $j\in\mathbb Z^*$, $\Lambda/2\le t\le0$: $\max_{k\ne j}H_{jk}(t)\ll(\log_+^2j)\log_+\log_+j$, where $H_{jk}=\log\frac1{|x_j-x_k|}$-type gap quantity; i.e. $\log\frac1{x_{j+1}-x_j}\ll\log^2 j\log\log j$.
- **THM-PAPER-0036-6** (Theorem 17, theorem, scope: asymptotic; Sec.5, eq.(65), p.40). Integrated renormalized energy bound: $\int_{\Lambda/4}^0\tilde E_{[0.5T\log T,3T\log T]_{\mathbb Z^*}}(t)\,dt=o_{T\to\infty}(T\log^3_+T)$.
- **THM-PAPER-0036-7** (Proposition 26, proposition, scope: asymptotic; Sec.7, p.~57-59). Energy at time zero: $\tilde E_{[T\log T,2T\log T]_{\mathbb Z^*}}(0)=o_{T\to\infty}(T\log^3T)$. Consequence (eq. 93): $x_{j+1}(0)-x_j(0)=\frac{4\pi+o(1)}{\log T}$ for a proportion $1-o(1)$ of $j\in[T\log T,2T\log T]$, contradicting the Conrey-Ghosh-Goldston-Gonek-Heath-Brown small-gap theorem (proportion c(lambda)>0 of gaps <= lambda*4pi/log T for any lambda>0.77, under RH).

### Principal lemmas

- **THM-PAPER-0036-L1** (Lemma 6/7; Sec.2). Saddle point / Stirling-type control of the integral representation of H_t(x-iy) with y of size ~ log x. — *Role:* Provides Lemma 4 and thereby the Riemann-von Mangoldt-type counts for t<0.
- **THM-PAPER-0036-L2** (Lemma 14; Sec.4). Quantitative repulsion estimate for finite subsets K of zeros, extending Csordas-Smith-Varga Theorem 1 (finite-set log-gap bound). — *Role:* Gives Prop 13 lower bound on gaps, needed to define cutoff Hamiltonian H(t)=sum log 1/|x_j-x_k|.
- **THM-PAPER-0036-L3** (Proposition 15; Sec.4). Weak integrated energy bound: $\int_{\Lambda/2}^0\sum_{J\le j<k\le2J}E_{jk}(t)\,dt\ll J^2\log_+^{O(1)}J$. — *Role:* Justifies swapping derivative and infinite sum in the Hamiltonian/energy monotonicity formula.
- **THM-PAPER-0036-L4** (Lemma 16/18/19; Sec.5-6). Local (cutoff) versions of d/dt H = -4E and monotonicity (convexity) of renormalized energy, with error terms from spatial cutoffs. — *Role:* Core of the 'relaxation to local equilibrium' mechanism; feeds Thm 17.
- **THM-PAPER-0036-L5** (Lemma 20/21, Prop 22, Lemma 24, Cor 25; Sec.6). Long-range decay of pairwise interaction terms and absolute convergence of truncated energy functionals; bound H~_T(t)=O(delta_T log^3 T) on Lambda/4<=t<=0. — *Role:* Technical control of cutoff errors so the integrated energy bound closes.
- **THM-PAPER-0036-L6** (Proposition 27; Sec.7). Existence (by pigeonholing a la Bourgain) of a good interval I^0 within [0.8 T log T, 2.2 T log T] where dyadic-scale integrated energies are O~(1). — *Role:* Provides the localized initial control for energy propagation.
- **THM-PAPER-0036-L7** (Proposition 28; Sec.7). Energy propagation inequality: energy at t=0 on an interval is controlled by integrated energy at earlier times on slightly larger intervals. — *Role:* Transfers the integrated bound (Thm 17) to the time-zero bound (Prop 26).

### Proof architecture

Proof by contradiction: assume Lambda<0 (hence RH). (1) Sec.2: saddle-point/Stirling asymptotics of H_t(x-iy), y~log x (Lemma 4). (2) Sec.3: Riemann-von Mangoldt type zero counts for t in (Lambda,0] (Thm 9) and macroscopic location x_j(t)=xi_j+O(log xi_j) (Cor 10), valid down to scale log T (weaker than t=0). (3) Sec.4: import Csordas-Smith-Varga ODE d_t x_k = 2 sum' 1/(x_k-x_j) (Thm 11), prove quantitative gap lower bound (Prop 13, Lemma 14), view flow as gradient flow of log-gas Hamiltonian H(t) with d_t H=-4E, E convex-decreasing. (4) Sec.5-6: spatially cutoff, renormalized energy; derive integrated energy bound Thm 17 (o(T log^3 T)) via weak bound Prop 15 and Lemmas 16-25. (5) Sec.7: pigeonhole a good interval (Prop 27), propagate energy monotonicity (Prop 28) to get Prop 26 at t=0: zeta zeros are locally arithmetic-progression-like on average (gaps ~ 4pi/log T for almost all j). (6) Contradiction with Montgomery pair correlation / Conrey-Ghosh-Goldston-Gonek-Heath-Brown small-gap result. Imported results enter at Thm 11 (CSV), Stirling/Gamma asymptotics, Littlewood zero-count, and the final contradiction.

**Imported results.** Csordas-Smith-Varga 1994: zeros of H_t simple, avoid origin, evolve by ODE (56) for t in (Lambda,0] (Lemma 2.4, Cor 1, Thm 1); Newman 1976: existence of finite Lambda <= 1/2; Polya/de Bruijn monotonicity of real-rootedness in t; Riemann-von Mangoldt formula and Littlewood short-interval zero count at t=0; Conrey-Ghosh-Goldston-Gonek-Heath-Brown 1985 (On the distribution of gaps between zeros of the zeta-function): for lambda>0.77 a positive proportion of gaps <= lambda*2pi/log T (used under RH); Montgomery 1973 pair correlation (motivation); Bourgain 1999 pigeonhole trick

**Techniques.** backwards heat flow of xi on the Fourier side (de Bruijn-Newman family); Newton-type ODE for zero dynamics, log-gas Hamiltonian / gradient flow; saddle point method with Stirling approximation; renormalized local energies with spatial cutoffs and monotonicity formulae; pigeonholing / energy propagation (Bourgain); pair correlation / small gaps (Montgomery; Conrey-Ghosh-Goldston-Gonek-Heath-Brown) for the contradiction

## Context and interpretation

**Importance and obstacle overcome.** Settles Newman's conjecture unconditionally and shows RH <=> Lambda = 0, a quantitative 'RH is on the edge' statement: any strengthening of RH of heat-flow type must be sharp. Obstacle: the Lehmer-pair strategy needs arbitrarily good Lehmer pairs, which are not known to exist without GUE-type hypotheses. The authors replace it by a dynamical argument (local equilibrium of zero gas under backward flow) which only needs a positive-proportion small-gap theorem; the technical obstacle is lack of Dirichlet-series expansions for t<0, overcome by saddle point asymptotics at height ~ log x.

**Relation to prior work.** Builds directly on Csordas-Smith-Varga (repulsion of zeros, ODE for zeros, Lehmer-pair bounds). Mentions GUE-conditional sketch (blog 2018) superseded. Note-added: Dobner's alternative proof (Riemann-Siegel type) and the generalized Newman conjecture settled by simpler argument (Griffin-Ono-Rolen-Zagier / ref [12]) .

**Limitations and open questions.** Does not prove or disprove RH (only Lambda>=0, so RH <=> Lambda=0). Quantitative: no effective lower-bound mechanism beyond contradiction, no information on zeros of H_t for t<0 other than existence of non-real ones. The generalized Newman conjecture for other L-functions is not addressed (later done elsewhere). Open: strengthen to explicit structure of off-line zeros for t<0 (Dwars' numerical curves), rate of Lambda_{T}-type truncations, and any proof of Lambda <= 0.

## Research potential

- **Hypotheses that might be weakened.** The only arithmetic input at the end is a positive-proportion small-gap theorem (lambda>0.77, CGGGH-B) and Montgomery-type pair correlation; any statement showing that zeros are not locally equally spaced at a positive proportion of j suffices. The restriction t in (Lambda/4,0] with log^2 losses in Thm 9 (weaker than t=0) could be improved to remove the 'barely suffices' margin.
- **Generalizations.** Generalized Newman conjecture for L-functions in Selberg class / Dirichlet L-functions (the authors say it may extend; later proven by simpler route). Local-equilibrium-via-energy-monotonicity could be applied to other repulsive zero flows (heat flow on Maass/automorphic xi, Dyson Brownian motion-type analogues).
- **Candidate connections.** Dyson Brownian motion and log-gas gradient flows (beta=2 corresponds to coefficient 2/(x_k-x_j)); Hamiltonian energy E(t) as a potential monotone quantity for t>=0 side to attack RH (Lambda<=0) -- a forward heat-flow version would need control of zeros at t=0 itself; Lehmer-pair quality vs. pair correlation; Dobner Riemann-Siegel approach.
- **Reusable lemmas.** Lemma 4 (Ht asymptotics at height ~log x, uniform for t in (Lambda,0] and even for t>-C), Theorem 9 (zero counts for H_t), Prop 13/Lemma 14 (quantitative gap repulsion), Prop 28 (energy propagation), Thm 11 (zero ODE).
- **Possible experiments.** (a) Numerically integrate (56) from t=0 backwards starting from computed zeta zeros (Odlyzko tables) and track renormalized truncated energy E~(t) and gap statistics to test the mechanism quantitatively; (b) measure the Lambda-dependence of the constants in Prop 26 to see how fast a hypothetical Lambda<0 would be contradicted; (c) explore Dwars' deterministic curves of off-line zeros for t<0.
- **Risks / barriers.** The argument is intrinsically a lower-bound-for-Lambda argument; it does not produce any constraint in the direction Lambda<=0 (RH). t>0 side requires control at the critical t=0 where zero spacing is not accessible; constants/log-power losses are 'barely' enough, so pushing to explicit effective statements is hard.

## Audit notes (Level 1 reader)

none noticed in inspected portion (the PDF-extracted text header shows 'Forum of Mathematics, Pi (2021), vol. ???, e1, 61 pages' vs triage citation 'Paper No. e6, 62 p. (2020)'; bibliographic-only discrepancy. Detailed technical Lemmas 18-24 were not checked line by line.)

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01803`; harvest queries: kw_RH_any, kw_debruijn_newman, msc_11M06, arxiv_debruijn_newman, arxiv_pair_corr, arxiv_rh_abs, arxiv_zeta_zeros.
- Triage decision: include — Landmark proof of Newman's conjecture Lambda >= 0.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
