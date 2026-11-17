# PAPER-0026 — Trace formula in noncommutative geometry and the zeros of the Riemann zeta function

| Field | Value |
|---|---|
| Authors | Connes, Alain |
| Year / stratum | 1999 / S4 |
| Venue | Sel. Math., New Ser. 5, No. 1, 29-106 (1999). |
| Identifiers | zbMATH [0945.11015](https://zbmath.org/?q=an:0945.11015) · DOI [10.1007/s000290050042](https://doi.org/10.1007/s000290050042) · arXiv [math/9811068](https://arxiv.org/abs/math/9811068) |
| MSC | 11M55, 11M26, 11R56, 11F72, 58J50, 58J90 |
| Families | D |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/math/9811068 |
| Selection | score 4.5996, in-pool citations 80, seed lists 0, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Give a spectral (absorption-spectrum) interpretation of the critical zeros of Hecke L-functions on the adele class space X=A/k^* and a trace formula for the idele class group C_k acting on L^2(X), such that validity of the global trace formula is equivalent to RH for all L-functions with Grossencharakter (via Weil positivity).

**Historical motivation.** Polya-Hilbert program; Selberg trace formula analogy; sign of fluctuation term (quantum chaos, Berry/Keating) suggests absorption rather than emission spectrum; Frobenius/Lefschetz formula analogy for characteristic p, space X as geometric object on which C_k acts like Weil group.

### Main results

- **THM-PAPER-0026-1** (Theorem 1 (Sect. III), theorem, scope: global; Sect. III, p.13). Let $\chi\in\hat{C_{k,1}}$ (character of the norm-one idele classes), $\delta>1$, $H_\chi$ the Sobolev-type Hilbert space $L^2_{\delta,\chi}(X)_0$ and $D_\chi$ the generator of the action $W_\chi$ of $N\simeq \mathbb R_+^*$ (or $q^{\mathbb Z}$). Then $D_\chi$ has discrete spectrum, $\mathrm{Sp}\,D_\chi\subset i\mathbb R$ is exactly the set of $\rho\in i\mathbb R$ with $L(\tilde\chi,\tfrac12+\rho)=0$, where $\tilde\chi$ is the unique extension of $\chi$ to $C_k$ trivial on $N$; multiplicity of $\rho$ is the largest integer $n<\frac{1+\delta}{2}$ with $n\le$ multiplicity of $\tfrac12+\rho$ as a zero of $L$.
- **THM-PAPER-0026-2** (Corollary 2 (Sect. III), corollary, scope: global; Sect. III, p.14). For Schwartz $h\in S(C_k)$ the operator $W(h)=\int W(g)h(g)d^*g$ on $H$ is trace class and $\mathrm{Trace}\,W(h)=\sum_{L(\tilde\chi,\frac12+\rho)=0,\ \rho\in i\mathbb R/N^\perp}\hat h(\tilde\chi,\rho)$ with $\hat h(\tilde\chi,\rho)=\int_{C_k}h(u)\tilde\chi(u)|u|^\rho d^*u$, multiplicity as in Thm 1.
- **THM-PAPER-0026-3** (Theorem 3 (Sect. V), theorem, scope: asymptotic; Sect. V, p.~25-30). Let $K$ be a local field with basic character $\alpha$, $h\in S(K^*)$ compactly supported, $R_\Lambda=\hat P_\Lambda P_\Lambda$ (infrared cutoff $P_\Lambda$ = indicator of $|x|\le\Lambda$, ultraviolet cutoff $\hat P_\Lambda=FP_\Lambda F^{-1}$). Then $R_\Lambda U(h)$ is trace class and as $\Lambda\to\infty$: $\mathrm{Trace}(R_\Lambda U(h))=2h(1)\log'\Lambda+\int'\frac{h(u^{-1})}{|1-u|}d^*u+o(1)$, where $\int'$ is the principal value determined by the unique distribution on $K$ agreeing with $du/|1-u|$ off $u=1$ whose Fourier transform vanishes at 1.
- **THM-PAPER-0026-4** (Theorem 4 (Sect. VII), theorem, scope: asymptotic; Sect. VII, p.~35). S-local trace formula: for finite set $S$ of places, $X_S=\prod_{v\in S}k_v/O_S^*$, $h\in S(C_S)$ compactly supported, $\mathrm{Trace}(R_\Lambda U(h))=2h(1)\log'\Lambda+\sum_{v\in S}\int'_{k_v^*}\frac{h(u^{-1})}{|1-u|}d^*u+o(1)$ as $\Lambda\to\infty$.
- **THM-PAPER-0026-5** (Equation (16) / Corollary 2 of Sect. VIII (global trace formula, conjectural), conjecture, scope: asymptotic; Sect. VIII, p.41-42). With $Q_\Lambda$ the orthogonal projection of $L^2(X)$ onto span of $f\in S(A)$ with $f,\hat f$ vanishing for $|x|>\Lambda$ (trivial $\delta=0$): $\mathrm{Trace}(Q_\Lambda U(h))=2h(1)\log'\Lambda+\sum_v\int'_{k_v^*}\frac{h(u^{-1})}{|1-u|}d^*u+o(1)$ for all compactly supported $h\in S(C_k)$. Proved only for $h$ supported in $C_{k,1}$; open in general. *Conditional on:* unproved global trace formula (16).
- **THM-PAPER-0026-6** (Theorem 5 (Sect. VIII), theorem, scope: global; Sect. VIII, p.42-44). Let $k$ be a global field of POSITIVE characteristic and $Q_\Lambda$ as above. For compactly supported $h\in S(C_k)$ the following are equivalent: (a) the trace formula (16) holds as $\Lambda\to\infty$; (b) all L-functions with Grossencharakter on $k$ satisfy RH.
- **THM-PAPER-0026-7** (Theorem 6 (Appendix II), theorem, scope: global; Appendix II, p.77-78). Weil explicit formula rewritten: for $h\in S(C_k)$ compactly supported, $\hat h(0)+\hat h(1)-\sum_{L(\mathcal X,\rho)=0,\,0<\mathrm{Re}\rho<1}\hat h(\mathcal X,\rho)=\sum_v\int'_{k_v^*}\frac{h(u^{-1})}{|1-u|}d^*u$ with principal value normalized by $\alpha_v$ as in Thm V.3.

### Key definitions

- X=A_k/k^* adele class space
- C_k=GL_1(A)/GL_1(k) idele class group; N=range of |.|
- L^2_{\delta,\chi}(X)_0 Sobolev space (delta>1)
- Weil distribution \Delta=\log|d^{-1}|\delta_1+D-\sum_v D_v
- cutoff projections R_\Lambda=\hat P_\Lambda P_\Lambda, Q_\Lambda

### Principal lemmas

- **THM-PAPER-0026-L1** (Lemma 3 (Sect. VIII); Sect. VIII, p.44). $\lim_{\Lambda\to\infty}\Delta_\Lambda=\Delta_\infty$, $\Delta_\infty(f)=\sum_{L(\tilde\chi,\frac12+\rho)=0,\rho\in B/N^\perp}N(\tilde\chi,\tfrac12+\rho)\int_{z\in i\mathbb R}\hat f(\tilde\chi,z)d\mu_\rho(z)$ with $B=\{|\mathrm{Re}\rho|<1/2\}$ and $\mu_\rho$ the harmonic measure of $\rho$ w.r.t. $i\mathbb R$ (Dirac mass if $\rho\in i\mathbb R$). — *Role:* Computes the limiting Weil distribution from zeros without hypothesis; key to b)=>a) (positive char.): off-line zeros enter via harmonic measure, so $\Delta_\infty$ is positive iff RH.
- **THM-PAPER-0026-L2** (Equations (18)-(25) (Sect. VIII, unlabeled); Sect. VIII, p.42-43). $E(f)(g)=|g|^{1/2}\sum_{q\in k^*}f(qg)$ is a surjective isometry $L^2(X)_0\to L^2(C_k)$ intertwining $U(a)$ with $|a|^{1/2}V(a)$; $E(B_{\Lambda,0})\subset S_\Lambda$ so $Q'_{\Lambda,0}\le S_\Lambda$ and $\Delta_\Lambda(f)=\mathrm{Trace}((S_\Lambda-Q'_{\Lambda,0})V(f))$ is of positive type. — *Role:* Source of positivity: difference of two projections with one dominating the other gives a positive-type distribution; limit is Weil distribution, hence a)=>b) via Weil's positivity criterion.
- **THM-PAPER-0026-L3** (Lemma 1 (Sect. VII); Sect. VII-VIII, p.41). B_Lambda subspaces stabilize quickly in S; natural map L^2(X_S)->L^2(X_{S'}) maps B_Lambda^S onto B_Lambda^{S'} (statement as paraphrased in Sect. VIII), giving S-independent global cutoff. — *Role:* Allows S-independent global formulation of cutoff and of trace formula.

### Proof architecture

(1) Sect. III: Sobolev spaces L^2_delta(X)_0 on X=A/k^*; map E identifies L^2(X)_0 with L^2(C_k); critical zeros appear as point spectrum of generator D of the R_+^* action as absorption spectrum (Thm 1), trace in Cor 2; delta needed to make absorption spectrum a point spectrum. (2) Formal trace computation gives Weil distribution (Sect. VI). (3) Rigorous local trace formula: Thm 3 (one local field) and Thm 4 (finite S) via cutoff R_Lambda=P^_Lambda P_Lambda, analysis of conditionally convergent principal values. (4) Sect. VIII: delta eliminated by working with delta=0 and cutoff Q_Lambda; the difference S_Lambda - Q_Lambda gives positive-type distribution Delta_Lambda; global trace formula (16) is equivalent to RH (Thm 5, shown only for positive characteristic, remark extends to number fields); b)=>a) uses explicit formula plus Lemma 3 and finite-dimensional linear-algebra computation (subspace of l^2(Z) cut out by evanescence conditions at zeros). Weil explicit formula (Thm 6) is imported/checked in Appendix II.

**Imported results.** Weil's explicit formula and Weil positivity criterion (Weil 1952/1972; [W1],[W3]); RH for function fields (Weil); Tate thesis / functional equation and analytic continuation of Hecke L-functions; Bruhat/Schwartz function space theory, Poisson summation on adeles

**Techniques.** adele class space and idele class group representation; Tate/Weil explicit formula as trace formula; Sobolev-type function spaces and absorption spectrum; principal-value distributions via Fourier transform vanishing at 1; cutoff projections P_Lambda, Fourier-conjugate projection; Weil positivity criterion for RH; harmonic measure to treat off-line zeros as resonances; positive-type distributions from nested projections

## Context and interpretation

**Importance and obstacle overcome.** Overcomes the two defects of Connes' earlier preprint: the formal trace computation (made rigorous in local and S-local cases) and the unnatural parameter delta (eliminated in Sect. VIII). Remaining obstacle: the global trace formula (16) for arbitrary h, equivalent to RH, is not proved; so RH is reformulated, not proved.

**Relation to prior work.** Builds on Weil's explicit formulas and positivity criterion, Tate thesis, Connes' preliminary Bost-Connes/Hilbert-space paper [Co], Selberg trace formula; later developed by Meyer (CAND-01282), Connes-Consani-Marcolli, Connes-Consani semilocal trace formula.

**Limitations and open questions.** Global trace formula (16) open; Theorem 5 stated and proven only in positive characteristic (a theorem there already), number-field case only explained as an extension (Sect. VIII, from line ~2138 of text: 'how the above results extend to number fields') and equivalence to GRH asserted heuristically/conditional on trace formula; proof of Thm 1 uses delta>1; no unitary/self-adjoint operator for all zeros (off-line zeros appear only as resonances).

## Research potential

- **Hypotheses that might be weakened.** Trace formula (16) is required for all compactly supported h; test whether it suffices for h of the form f*f^sharp (Weil positivity cone) or for h supported in a neighborhood of 1; known for h supported on C_{k,1}.
- **Generalizations.** Extend Thm 4 from finite S to growing S with uniform error control in S; analogue for L-functions of automorphic representations (GL_n) by replacing C_k with GL_n adele classes.
- **Candidate connections.** Weil positivity (Li/Bombieri-Lagarias criteria), Meyer's virtual representation (CAND-01282), CCM endomotive spectral realization (CAND-01520), semilocal trace formula of Connes-Consani, de Branges spaces (CAND-01512).
- **Reusable lemmas.** Lemma 3 (harmonic-measure formula for limiting distribution) and the finite-dimensional lemma on Trace((S_N-E_N)V(f)); eq. (18)-(25) positive-type construction as template for any positivity-from-projection-domination argument.
- **Possible experiments.** Numerically compute Trace((S_Lambda-Q_Lambda)V(f)) for Q with k=Q, S={infty,2,3}, truncated to finite Lambda, and compare with explicit-formula side for test functions h; check the o(1) rate; function-field toy model (Thm 5) can be verified exactly on small genus.
- **Risks / barriers.** Proving (16) globally is as hard as RH; error terms in S-local theorem not uniform in S; off-line zeros contribute through harmonic measure so positivity needs sharper analysis.

## Audit notes (Level 1 reader)

Introduction says (global trace formula) 'equivalent to the Riemann Hypothesis for all L-functions with Grossencharakter', but Theorem 5 as stated is for positive characteristic only, where RH is known; the number-field equivalence is only discussed in Sect. VIII after the proof (around text line 2138). Not a gap per se but readers should not cite Thm 5 for number fields. Text extraction garbled math in places; exact page numbers approximate.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00726`; harvest queries: kw_RH_any, kw_trace_formula_zeta, kw_zeta_zeros, msc_11M26, arxiv_explicit_formula, arxiv_rh_abs, arxiv_zeta_zeros.
- Triage decision: include — Connes' noncommutative geometry spectral interpretation of zeros.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
