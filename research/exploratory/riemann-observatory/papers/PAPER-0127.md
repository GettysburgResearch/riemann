# PAPER-0127 — An effective universality theorem for the Riemann zeta function

| Field | Value |
|---|---|
| Authors | Lamzouri, Youness; Lester, Stephen; Radziwill, Maksym |
| Year / stratum | 2018 / S6 |
| Venue | Comment. Math. Helv. 93, No. 4, 709-736 (2018). |
| Identifiers | zbMATH [1414.11101](https://zbmath.org/?q=an:1414.11101) · DOI [10.4171/CMH/448](https://doi.org/10.4171/CMH/448) · arXiv [1611.10325](https://arxiv.org/abs/1611.10325) |
| MSC | 11M06 |
| Families | B, F |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1611.10325 |
| Selection | score 3.8847, in-pool citations 8, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Give the first effective version of Voronin's universality theorem for zeta: a rate of convergence, as T tends to infinity, of the t-measure of {t in [T,2T]: max_{|z|<=r}|zeta(3/4+it+z)-f(z)|<eps} to the corresponding probability for the random Euler product zeta(3/4+z,X).

**Historical motivation.** Voronin's proof (Pecherskii rearrangement) and Bagchi's probabilistic proof give only a positive lower density or an ineffective limit. Good and Garunkstis gave explicit lower bounds for the density, but no asymptotic with an error term.

### Main results

- **THM-PAPER-0127-1** (Theorem 1.1, theorem, scope: asymptotic; Sec. 1, Theorem 1.1). Let $0<r<1/4$, $f$ non-vanishing continuous on $|z|\le (r+1/4)/2$ and holomorphic in the interior, and $\omega$ real-valued $C^1$ with compact support. Then $\frac1T\int_T^{2T}\omega\big(\max_{|z|\le r}|\zeta(\tfrac34+it+z)-f(z)|\big)dt=\mathbb E\,\omega\big(\max_{|z|\le r}|\zeta(\tfrac34+z,X)-f(z)|\big)+O\big((\log T)^{-\frac{3/4-r}{11}+o(1)}\big)$, implied constant depending on $f,\omega,r$.
- **THM-PAPER-0127-2** (Remark after Thm 1.1, corollary (conditional on regularity of limit law), scope: asymptotic; Sec. 1 after Thm 1.1). If $Y_{r,f}=\max_{|z|\le r}|\zeta(\tfrac34+z,X)-f(z)|$ is absolutely continuous, then for fixed $\varepsilon>0$: $\frac1T\mathrm{meas}\{t\in[T,2T]:\max|\zeta(\tfrac34+it+z)-f(z)|<\varepsilon\}=\mathbb P(Y_{r,f}<\varepsilon+O((\log T)^{-(3/4-r)/11+o(1)}))$. *Conditional on:* absolute continuity of Y_{r,f}.
- **THM-PAPER-0127-3** (Proposition 2.1, proposition, scope: asymptotic; Sec. 2, Prop 2.1 (proved in Sec. 4)). For fixed $0<r<1/4$ there are $b_1,b_2,b_3>0$ depending only on $r$ such that with $\sigma(r)=3/4-r$: $\mathbb P_T\big(\max_{|z|\le r}|\zeta'(\tfrac34+it+z)|>e^V\big)\ll\exp\big(-b_1V^{\frac1{1-\sigma(r)}}(\log V)^{\frac{\sigma(r)}{1-\sigma(r)}}\big)$ uniformly for $b_2<V\le b_3(\log T)^{1-\sigma}/\log\log T$.
- **THM-PAPER-0127-4** (Proposition 2.2, proposition, scope: global; Sec. 2, Prop 2.2). Same tail bound for the random model: $\mathbb P(\max_{|z|\le r}|\zeta'(\tfrac34+z,X)|>e^V)\ll\exp(-b_1V^{1/(1-\sigma(r))}(\log V)^{\sigma(r)/(1-\sigma(r))})$ for all $V>b_2$.
- **THM-PAPER-0127-5** (Theorem 2.1, theorem, scope: asymptotic; Sec. 2, Thm 2.1 (proved in Sec. 5)). Fix $1/2<\sigma_0<1$; $s_j,r_j$ in $\sigma_0<\mathrm{Re}<1$, $|\mathrm{Im}|\le T^{(\sigma_0-1/2)/4}$. There are $c_3,c_4,c_5>0$ and $E(T)\subset[T,2T]$ with $\mathrm{meas}\,E(T)\ll T^{1-c_3}$ such that for $k,\ell\le c_4\log T/\log\log T$: $\frac1T\int_{[T,2T]\setminus E(T)}\prod_{j\le k}\log\zeta(s_j+it)\prod_{j\le\ell}\overline{\log\zeta(r_j+it)}\,dt=\mathbb E[\prod\log\zeta(s_j,X)\prod\overline{\log\zeta(r_j,X)}]+O(T^{-c_5})$ (the displayed integrand in the text uses $\log\zeta(r_j-it)$, i.e. conjugates).
- **THM-PAPER-0127-6** (Theorem 2.2, theorem, scope: asymptotic; Sec. 2, Thm 2.2 (proved in Sec. 6)). Fix $1/2<\sigma<1$, $J\le(\log T)^\sigma$, $s_j$ with $\min\mathrm{Re}\,s_j=\sigma$, $\max|\mathrm{Im}\,s_j|<T^{(\sigma-1/2)/4}$. There are $c_1(\sigma),c_2(\sigma)>0$ such that for $\max|u_j|,\max|v_j|\le c_1(\sigma)(\log T)^\sigma/J$: $\Phi_T(u,v)=\Phi_{rand}(u,v)+O(\exp(-c_2(\sigma)\log T/\log\log T))$, with $\Phi$ the joint characteristic functions of $(\mathrm{Re},\mathrm{Im})\log\zeta(s_j+it)$ resp. $\log\zeta(s_j,X)$.
- **THM-PAPER-0127-7** (Theorem 2.3, theorem, scope: asymptotic; Sec. 2, Thm 2.3 (proved in Sec. 7, via Beurling-Selberg functions)). Let $1/2<\sigma=\min\mathrm{Re}\,s_j\le\max\mathrm{Re}\,s_j<1$, $\max|\mathrm{Im}\,s_j|<T^{(\sigma-1/2)/4}$, $J\le(\log T)^{\sigma/2}$. Then the rectangle discrepancy $D_T(s_1,\dots,s_J)=\sup_{R_j}|\mathbb P_T(\log\zeta(s_j+it)\in R_j\forall j)-\mathbb P(\log\zeta(s_j,X)\in R_j\forall j)|\ll J^2/(\log T)^\sigma$.
- **THM-PAPER-0127-8** (Proposition 3.1, proposition, scope: asymptotic; Sec. 3, Prop 3.1). For $0<r<1/4$, $J\le(\log T)^{(3/4-r)/7}$, $|z_j|\le r$: $|\mathbb P_T(\max_{j\le J}|\zeta(\tfrac34+it+z_j)-f(z_j)|\le u)-\mathbb P(\max_j|\zeta(\tfrac34+z_j,X)-f(z_j)|\le u)|\ll u\,(J\log\log T)^{6/5}/(\log T)^{(3/4-r)/5}$.

### Key definitions

- zeta(s,X)=prod_p (1-X(p)p^{-s})^{-1} with X(p) iid uniform on unit circle, extended multiplicatively with E X(n)conj(X(m))=1_{n=m}
- P_T uniform probability on [T,2T]
- discrepancy D_T over products of axis-parallel rectangles
- Phi_T, Phi_rand joint characteristic functions

### Principal lemmas

- **THM-PAPER-0127-L1** (Lemma 4.1; Sec. 4). Statement concerns $0<r<1/4$, $\delta=(1/4-r)/4$, $y\le\log T$ (Dirichlet-polynomial approximation setup for zeta' near sigma=3/4-r); exact statement not extracted. — *Role:* Input to Prop 2.1: controls max of zeta' via short Euler/Dirichlet polynomial plus zero-density to exclude zeros.
- **THM-PAPER-0127-L2** (Lemma 4.2 (Lemma 1 of [4]); Sec. 4). Imported approximation of log zeta(s) by a Dirichlet polynomial over primes up to y for y>=2, |t|>=y+3 (outside a zero-free rectangle). — *Role:* Standard Selberg/Granville-Soundararajan-style approximation used for both Prop 2.1 and moments.
- **THM-PAPER-0127-L3** (Lemma 5.3; Sec. 5). Exceptional set $E(T)\subset[T,2T]$ of measure $\ll T^{1-c}$ outside which zeta has no zeros in relevant rectangles around $s_j+it$ (zero-density input). — *Role:* Allows log zeta to be defined and approximated, and gives Theorem 2.1 away from E(T).
- **THM-PAPER-0127-L4** (Lemma 7.1; Sec. 7). $|F_I(x)|\le1$ for the Beurling-Selberg Fourier-side test functions $F_I$. — *Role:* Bounds in the discrepancy argument converting characteristic function closeness (Thm 2.2) to rectangle discrepancy (Thm 2.3).
- **THM-PAPER-0127-L5** (Reduction via maximum modulus, (3.1); Sec. 3). $\max_j|\zeta(\tfrac34+it+z_j)-f(z_j)|\le\max_{|z|\le r}|\cdots|\le\max_j\max_{z\in D_j}|\cdots|$ with $D_j$ discs of radius eps covering $|z|=r$, $J\asymp1/\varepsilon$. — *Role:* Reduces the sup over a disc to finitely many (growing with T) shifts; derivative bound (Prop 2.1) shows the two sides agree off a small set.

### Proof architecture

(1) Maximum modulus principle reduces to the circle |z|=r; cover it by J ~ small power of log T discs, and use Prop 2.1 (tail bound for max|zeta'|, with zero-density estimates to avoid zeros) to replace the sup on each disc by the value at the center, outside a set of small measure; same for the random model via Prop 2.2. (2) Reduce to comparing the distribution of the vector (log zeta(3/4+it+z_j))_{j<=J} with (log zeta(3/4+z_j,X))_j: moments (Thm 2.1, Dirichlet polynomial approximation of log zeta plus mean values, off an exceptional set from zero-density), then characteristic functions (Thm 2.2), then rectangle discrepancy via Beurling-Selberg majorants/minorants (Thm 2.3). (3) Prop 3.1: cover the region U_j={|e^w-f(z_j)|<=u,|Im w|<=loglogT} by eps-squares, use absolute continuity of log zeta(s,X) (Jessen-Wintner) to bound boundary squares, and optimize eps to get the logarithmic saving. Theorem 1.1 follows by smoothing with omega. Imported: zero density near sigma=1, Jessen-Wintner, bound on arg zeta tails (Lamzouri [9]).

Dependency edges: CAND-02263 → CAND-01610 (effective refinement of the universality theory surveyed there (Sec. 16))

**Imported results.** Voronin 1975; Bagchi 1981 (random Euler product); Jessen-Wintner theorem on absolute continuity of log zeta(s,X); Zero-density estimates N(sigma,T); Lamzouri [9] distribution of arg zeta / Remark 1 (large values of |arg|); Kolmogorov three-series theorem

**Techniques.** Maximum modulus principle; covering by growing number of discs; tail bounds for max |zeta'| in measure; moments of log zeta shifts with number of factors ~ log T/loglog T; Fourier/characteristic function comparison; Beurling-Selberg extremal functions; Jessen-Wintner absolute continuity; zero-density estimates

## Context and interpretation

**Importance and obstacle overcome.** First rate of convergence in universality: error (log T)^{-(3/4-r)/11+o(1)}, matching the shape of Bagchi's limit law. Obstacle: replacing the sup over a continuum of shifts by finitely many points needed a large-deviation tail for max |zeta'| (Prop 2.1) uniform in a range growing with T, and moments of up to log T/loglog T shifts.

**Relation to prior work.** Alternative to Bagchi's functional limit theorem; generalizes Lamzouri's one-dimensional discrepancy bound (J=1 case, Thm 1.1 of their ref [10]). Authors state that the method extends to Selberg class / GL_n L-functions using zero-density near 1 and Ramanujan bounds, and to families in the conductor aspect (cf. Kowalski GL2 universality).

**Limitations and open questions.** Rate only logarithmic; true rate unknown. Cannot show Y_{r,f} has no atoms, so the measure statement for fixed eps is conditional on absolute continuity (conjectured). Restricted to 0<r<1/4 and the line 3/4; the limit law itself (support) comes from Bagchi, not re-proved. Does not touch RH.

## Research potential

- **Hypotheses that might be weakened.** The restriction r<1/4 and center 3/4 comes from sigma(r)=3/4-r>1/2 requirements and zero-density exponent; a stronger zero-density estimate (e.g. under Lindelof) would widen the disc and improve the exponent 1/11.
- **Generalizations.** Replace zeta by Selberg class elements or Dirichlet L-functions with uniform conductor control; effective joint universality; effective strong recurrence statements relevant to Bagchi's RH criterion (CAND-01610 Thm 20).
- **Candidate connections.** Absolute continuity of Y_{r,f}: a regularity theorem for the law of sup norms of random analytic functions could upgrade Thm 1.1 to a fixed-eps measure statement. Connection to large-value/tail estimates for zeta' (Prop 2.1) and to moment computations of log zeta shifts (Thm 2.1), reusable in Selberg-type CLT work.
- **Reusable lemmas.** Prop 2.1/2.2 (tail of max|zeta'| in a disc, deterministic and random); Theorem 2.3 (J-dimensional discrepancy J^2/(log T)^sigma for J<=(log T)^{sigma/2}).
- **Possible experiments.** Numerically compare empirical distribution of max over |z|=r of |zeta(3/4+it+z)-f(z)| for t in [T,2T] with Monte Carlo of the random Euler product for T up to 1e6-1e8 to see the actual convergence rate against (log T)^{-0.1}; test discrepancy bound J^2/(log T)^sigma for small J.
- **Risks / barriers.** Logarithmic barrier from moment range k<=c log T/loglog T; going to power saving would need beyond-Dirichlet-polynomial control of log zeta. Result is unconditional but says nothing about zeros, hence no direct RH consequence.

## Audit notes (Level 1 reader)

Theorem 2.1 as extracted: second product written log zeta(r_j - it) in the text (extraction shows 'rj - it'), presumably denotes conjugate-type shift; minor notational point at Sec. 2 Thm 2.1. Prop 2.1 and Theorem 2.2 reuse sigma for both sigma(r)=3/4-r and an independent sigma; harmless. Otherwise none noticed in inspected portion (proofs in Secs. 4-7 not audited).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02263`; harvest queries: msc_11M06, arxiv_universality_zeta.
- Triage decision: include — Effective universality with quantitative bounds on approximation.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
