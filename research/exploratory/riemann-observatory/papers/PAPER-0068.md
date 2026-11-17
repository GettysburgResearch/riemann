# PAPER-0068 — Screw functions of Dirichlet series in the extended Selberg class

| Field | Value |
|---|---|
| Authors | Suzuki, Masatoshi |
| Year / stratum | 2025 / S7 |
| Venue | Int. J. Number Theory 21, No. 8, 1815-1823 (2025). |
| Identifiers | zbMATH [1582.11098](https://zbmath.org/?q=an:1582.11098) · DOI [10.1142/S1793042125500885](https://doi.org/10.1142/S1793042125500885) · arXiv [2209.12832](https://arxiv.org/abs/2209.12832) |
| MSC | 11M26, 42A82 |
| Families | C, D |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/2209.12832 |
| Selection | score 4.4981, in-pool citations 2, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Extend Suzuki's screw function from zeta to any F in the extended Selberg class S^# and show GRH for F is equivalent to eventual non-negativity of Re(-g_F(t)); also give a zero-free formula (via Lerch transcendent) for F in the semi-extended class S^{#flat}.

**Historical motivation.** Generalizes pointwise positivity criterion for RH from zeta (Suzuki 2023, Thm 1.7) to Selberg class, in parallel to Weil/Li-type criteria extended by Smajlovic.

### Main results

- **THM-PAPER-0068-1** (Theorem 1.1, equivalence, scope: global; Sec.1; proof Sec.3.1). Let $F\in S^\#$ with no real zeros of $F(s)$ except possibly at $s=1/2$. Then GRH for F holds iff $\Re(-g_F(t))\ge0$ for all $t\ge t_0$ for some $t_0\ge0$, where $g_F(t)=-iB_Ft-\frac{m_0}{2}t^2+\sum_{\gamma\in\Gamma_F\setminus\{0\}}m_\gamma\frac{e^{-i\gamma t}-1}{\gamma^2}$.
- **THM-PAPER-0068-2** (Corollary 1.1, corollary, scope: conditional; Sec.1; Sec.3.2). Let $F\in S$ (Selberg class), $F(1)\ne0$, and $\Re(-g_F(t))\ge0$ for all $t\ge t_0$. Then there is $\delta>0$ with no zeros of F in $\Re s>1-\delta$. *Conditional on:* eventual nonnegativity of Re(-g_F).
- **THM-PAPER-0068-3** (Theorem 4.1, identity (unconditional), scope: global; Sec.4). For $F\in S^{\#\flat}$ (log-derivative has Dirichlet series $-F'/F=\sum_{n\ge2}c_F(n)n^{-s}$), $\Psi_F(t)=4m_F(e^{t/2}+e^{-t/2}-2)-\sum_{n\le e^t}\frac{c_F(n)}{\sqrt n}(t-\log n)+(\log Q+\sum_j\lambda_j\frac{\Gamma'}{\Gamma}(\frac{\lambda_j}2+\mu_j))t+\sum_j\ldots$ (Lerch-transcendent terms (4.2)) equals $-g_F(t)$ for all real $t$.
- **THM-PAPER-0068-4** (Theorem 5.1, equivalence, scope: global; Sec.5.1). For $F\in S^\#$: GRH for F iff $g_F$ is a screw function on $\mathbb R$ (even, with $g_F(t-u)-g_F(t)-g_F(-u)+g_F(0)$ non-negative definite kernel).
- **THM-PAPER-0068-5** (Sec.5.4 remark, conditional generalization, scope: global; Sec.5.4). For $F\in S^{\#\flat}$, GRH holds iff $\sum_{\gamma}\hat\phi(\gamma)\overline{\hat\phi(\gamma)}\ge0$ for all $\phi\in C_c^\infty(\mathbb R)$ (Weil-type positivity via Smajlovic's explicit formula/Li criterion), i.e. analog of Thm 1.3 in [10].

### Key definitions

- extended Selberg class S^# (axioms S1-S3)
- semi-extended class S^{#flat} (Euler sum condition S5')
- screw function g_F in (1.1)
- B_F real constant from (2.6)
- F^*(s)=conj F(conj s)

### Principal lemmas

- **THM-PAPER-0068-L1** (Eq. (3.2); Sec.3.1). $\int_0^\infty g_F(t)e^{izt}dt=z^{-2}\frac{\xi_F'}{\xi_F}(\tfrac12-iz)$ for $\Im z>1/2$. — *Role:* Laplace transform linking g_F to the log-derivative of xi_F.
- **THM-PAPER-0068-L2** (Eq. (3.4); Sec.3.1). $2\int_0^\infty\Re g_F(t)e^{izt}dt=z^{-2}\frac{\xi_F'F^*}{\xi_FF^*}(\tfrac12-iz)$, using $g_F(t)=g_{F^*}(t)$-type symmetry and $\xi_{F^*}(s)=\xi_F(\bar s)$. — *Role:* Passes to the real part so that Widder's theorem controls the abscissa of convergence.
- **THM-PAPER-0068-L3** (Widder Thm 5b, Ch. II (imported); Sec.3.1). If a Laplace transform of a real-valued function that is eventually of one sign converges, its abscissa is a singularity on the real axis. — *Role:* Gives that xi_F xi_{F*} has no zeros for Re s>max(sigma_0,1/2).
- **THM-PAPER-0068-L4** (Sec.2.2 Hadamard factorization (imported); Sec.2.2). xi_F(1/2-iz)=e^{A+Bz}z^{m_0}\prod(1-z/\gamma)^{m_\gamma}e^{m_\gamma z/\gamma}; B_F real; (2.5)-(2.6). — *Role:* Defines B_F and g_F.

### Proof architecture

Direction (GRH => Re(-g_F)>=0): zeros real, so Re(-g_F)=m_0t^2/2+sum m_gamma (1-cos gamma t)/gamma^2>=0. Converse: compute Laplace transform (3.2), symmetrize with F^*, use Widder Thm 5b to show abscissa of convergence of the transform of Re g_F is at most max(sigma_0-1/2,0), hence xi_F xi_{F*} nonvanishing for Re s>max(sigma_0,1/2); absence of real zeros (hypothesis) gives sigma_0 <=1/2.

**Imported results.** Widder, The Laplace Transform, Ch. II Thm 5b; Krein-Langer 2014 screw functions; Smajlovic 2010 (S^{#flat}, explicit formula, Li criterion for Selberg class); Suzuki, J. London Math. Soc. 2023 (CAND-01970); Bombieri 2000 Weil positivity

**Techniques.** Hadamard factorization, order one entire functions; Laplace transform / Widder Tauberian-type singularity theorem; Hurwitz-Lerch zeta transforms; Krein screw functions; symmetrization F -> F F^*

## Context and interpretation

**Importance and obstacle overcome.** Shows the eventual-sign criterion works for the whole extended Selberg class, provided real zeros are controlled (the symmetrization trick F F^* and Widder's theorem handle non-self-dual F). Gives a zero-free formula for g_F via Lerch transcendent when F has a Dirichlet series for log-derivative.

**Relation to prior work.** Direct sequel to Suzuki 2023 (CAND-01970); uses Smajlovic's S^{#flat}; analogue of Lagarias positivity and Li's criterion for Selberg class.

**Limitations and open questions.** Hypothesis excluding real zeros of F in (1/2, infinity) is essential for the converse (can fail for F in S^# outside S, which can have zeros with real part >1; Corollary 1.1 only gives a zero-free strip near 1 for F in S). Section 5.3 notes generalization of moment/Hankel Theorem 1.8 needs a zero-free region (e.g. F in S with classical zero-free region giving F'/F << log) to ensure convergence of moments. Non-degeneracy theorem 1.4 generalization not attempted.

## Research potential

- **Hypotheses that might be weakened.** The 'no real zeros except 1/2' hypothesis could be replaced by control of sigma_0 for the particular F (e.g., via the Euler product for F in S, which is used in Cor 1.1); eventual-positivity threshold t_0 is not quantified.
- **Generalizations.** Quantify t_0 for Dirichlet L-functions or cusp forms from the explicit zero-free formula in Thm 4.1; extend Hankel-moment criterion (Thm 1.8) to F in S given a Vinogradov-Korobov zero-free region.
- **Candidate connections.** Connects to Smajlovic's Li coefficients and to Weil positivity for Selberg class; with CAND-01970, gives a family-wise criterion testable on Dirichlet L-functions L(s,chi) uniformly in conductor, relevant to families programmes.
- **Reusable lemmas.** Eq. (3.4) real-part symmetrization and the Widder step as a generic template for 'eventual sign implies zero-free half-plane'.
- **Possible experiments.** For F=L(s,chi) with small conductor, evaluate Psi_F(t) from Theorem 4.1 using primes and Gamma-terms and check Re(-g_F)>=0 on t in [0,~log 10^{12}]; compare with theoretical lower bound from low-lying zeros.
- **Risks / barriers.** Eventual positivity is for t>=t_0 with t_0 uncontrolled, so numerical finite windows give no certificate; reformulation is equivalent to GRH, with no new input about zeros.

## Audit notes (Level 1 reader)

Proof of converse in Sec.3.1 concludes zero-freeness for xi_F xi_{F*} in Re s>max(sigma_0,1/2) and then GRH only 'if xi_F or xi_{F*} has no real zeros except 1/2' — consistent with the theorem's hypothesis. Corollary 1.1 notes failure for S^# minus S. none other noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02381`; harvest queries: kw_RH_any, kw_selberg_class, msc_11M26, arxiv_rh_abs, arxiv_selberg_class.
- Triage decision: include — Grand RH as nonpositivity of screw function, operator-theoretic criterion.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
