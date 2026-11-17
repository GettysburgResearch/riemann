# PAPER-0126 — The scaling Hamiltonian

| Field | Value |
|---|---|
| Authors | Connes, Alain; Consani, Caterina |
| Year / stratum | 2021 / S6 |
| Venue | J. Oper. Theory 85, No. 1, 259-276 (2021). |
| Identifiers | zbMATH [1524.11171](https://zbmath.org/?q=an:1524.11171) · DOI [10.7900/jot.2019oct30.2265](https://doi.org/10.7900/jot.2019oct30.2265) · arXiv [1910.14368](https://arxiv.org/abs/1910.14368) |
| MSC | 11M55, 46L87, 58B34 |
| Families | D |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/1910.14368 |
| Selection | score 3.9195, in-pool citations 2, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** How does the Berry-Keating Hamiltonian $H=pq$ relate to Connes' spectral realization (absorption spectrum) of the zeta zeros, where does X.-J. Li's attempted proof of Weil positivity fail, and can a semi-local operator-theoretic framework prove Weil positivity (formulated as Conjecture 4.1)?

**Historical motivation.** Berry-Keating H=xp, Connes 1999 spectral realization, Li's 2019-style attempt at Weil positivity via Sonine spaces; the authors' return to analysis after pursuing algebraic geometry (Scaling Site).

### Main results

- **THM-PAPER-0126-1** (Section 1 (qualitative), expository/heuristic, scope: asymptotic; Introduction, Section 1). The scaling action of $\mathbb R_+^*$ on $L^2(\mathbb R)$ quantizes $H=PQ$ (with $x\partial_x+\frac12$ as unitary generator, $H=2\pi pq$ with the number-theoretic Fourier normalization); passing from the absorption spectrum of [10] to the emission spectrum of Berry-Keating does not introduce a semi-classical mismatch, the cutoff of Berry-Keating is equivalent semiclassically to removing the 'white light', and the minus sign survives in the Maslov phases (statement of aims in the Introduction; computations in Sect. 1 not verified here).
- **THM-PAPER-0126-2** (Lemma 2.4 (recalled), imported theorem (Connes 1999, Connes-Marcolli), scope: finite; Introduction / Sect. 2.2, Lemma 2.4 (recalled, not read in detail)). The trace of the scaling action on $L^2(X_S)$, $X_S=\mathbb A_S/\mathbb Q_S^*$, for a finite set $S\ni\infty$ of places of Q, is given by the local terms of the Riemann-Weil explicit formula (semi-local trace formula).
- **THM-PAPER-0126-3** (Lemma 3.4, lemma (native), scope: global; Sect. 3, Lemma 3.4). Let $H$ be a Hilbert space, $u$ unitary, $F=2P-1$ with $P$ an orthogonal projection, $d^-u=[F,u]$. The following are equivalent: (i) $Pu^*(1-P)uP=-\frac12u^{-1}d^-u$; (ii) $u^{-1}d^-u\le0$; (iii) $Pu=PuP$.
- **THM-PAPER-0126-4** (Corollary 3.5, corollary, scope: global; Sect. 3, Cor 3.5). In the one-variable quantized calculus, the equivalent conditions of Lemma 3.4 hold iff $u^*$ is an inner function in the sense of Beurling.
- **THM-PAPER-0126-5** (Eq. (3.3)-(3.4) and discussion, computation, scope: global; Sect. 3, eqs (3.3)-(3.4) and following text). At a prime $p$, $u_p(s)=\frac{1-p^{-(1-z)}}{1-p^{-z}}$, $z=\frac12+is$ (modulus 1 on the critical line) has poles at $z\in\frac{2\pi i}{\log p}\mathbb Z$ (so is meromorphic, not holomorphic, in the left half plane) and is unbounded on the right half plane ($\sim -p^{z-1}$ as $z\to\infty$ real). At the archimedean place $u_\infty(s)=\phi(\frac12+is)$, $\phi(z)=\frac{\pi^{-z/2}\Gamma(z/2)}{\pi^{-(1-z)/2}\Gamma((1-z)/2)}$, holomorphic in $\mathrm{Re}z\ge\frac12$ but unbounded there (e.g. $\phi(20)=\frac{1856156927625}{8\pi^{20}}\approx26.4562$). Hence no $u_v^*$ is inner and Li's direct approach cannot work.
- **THM-PAPER-0126-6** (Fact 3.6, proposition (negative result), scope: finite; Sect. 3, Fact 3.6 (eq 3.1 at line ~612 of extracted text)). The inequality (3.1), $\sum_{\mathbb Q_S^*}|1-w|\,h(w)\,d^*w\le0$-type semi-local positivity (here with $h=h_1\star h_2$, $h_2(w)=h_1(w^{-1})$) does not hold in general: for $S=\{\infty\}$ it would force $i u_\infty^{-1}u_\infty'$ to have constant sign, i.e. the Riemann-Siegel angle $\theta$ (where $u_\infty(s)=e^{2i\theta(s)}$) to be monotonic, which is false.
- **THM-PAPER-0126-7** (Conjecture 4.1, conjecture, scope: conditional; Sect. 4, Conjecture 4.1). The semi-local operator theoretic framework with $S:=\{\infty\}\cup\{p\mid p<q\}$ suffices to prove the Weil inequality for all test functions with support in the interval $(q^{-1/2},q^{1/2})$, where Weil positivity is $h=h_1\star h_2$ with $h_1$ satisfying the two conditions $\int_0^\infty h_1(x)x^{\pm1/2}d^*x=0$ (eq. 4.1).
- **THM-PAPER-0126-8** (Section 4.1 (Poisson formula, eqs 4.2-4.8), heuristic/construction, scope: local; Sect. 4.1, eqs (4.2)-(4.8)). Heuristically, the Poisson formula $E(\mathcal F_{e_{\mathbb R}}f)(x)=E(f)(x^{-1})$, $E(f)(x)=|x|^{1/2}\sum_{n>0}f(nx)$, shows that in Fourier (Mellin) variables $E$ is multiplication by $\zeta(\frac12-is)$ and the composite $I\circ\mathcal F$ is multiplication by $u(s)=\zeta(\frac12-is)/\zeta(\frac12+is)$, the ratio (3.4) of archimedean local factors; semi-locally $\sum_{M_S}m^{-1/2+is}=\zeta(\frac12-is)\prod_{p\in S}(1-p^{-1/2+is})$. Kahane's construction of elements of the Sonine space: $D(\Pi)$, $\Pi=\sum\delta_n$, with $D(f)(x)=x^2f''(x)+2xf'(x)$ (symmetric under Fourier), has range in $\{f(0)=\hat f(0)=0\}$.

### Key definitions

- quantized differential $d^-f=[H,f]$ with $H=2\mathcal F^{-1}1_P\mathcal F-1$ (eq. 2.9-2.10)
- semi-local adele class space $X_S=\mathbb A_S/\mathbb Q_S^*$, $\mathbb Q_S^*=\{\pm p_1^{n_1}\cdots p_k^{n_k}\}$
- ratio of local factors $u_v$ on the critical line (3.3)-(3.4)
- Sonine space
- Weil positivity (3.1)

### Principal lemmas

- **THM-PAPER-0126-L1** (Lemma 3.4; Sect. 3, Lemma 3.4). Equivalence of (i) $Pu^*(1-P)uP=-\frac12u^{-1}d^-u$, (ii) $u^{-1}d^-u\le0$, (iii) $Pu=PuP$. — *Role:* Gives the precise criterion (u* inner, Beurling) under which a Li-type positivity argument works; used to show it fails.
- **THM-PAPER-0126-L2** (Lemma 2.2; Sect. 2.2, Lemma 2.2 (recalled from [10,12])). For $\alpha=\prod_{v\in S}\alpha_v$, the Fourier transform $\mathcal F_\alpha$ on $\mathcal S(\mathbb A_S)$ extends uniquely to a unitary operator on $L^2(X_S)$. — *Role:* Hilbert-space set-up for the semi-local framework.
- **THM-PAPER-0126-L3** (Lemma 2.3; Sect. 2-4, Lemma 2.3 (recalled)). Semi-local sums over $M_S$ (positive integers prime to $S$) reduce, for the trivial character, to $\zeta(\frac12-is)\prod_{p\in S}(1-p^{-1/2+is})$ (referred to in Sect. 4.1). — *Role:* Explains the appearance of local-factor ratios via the Poisson formula.

### Proof architecture

Expository/programmatic. Sect. 1 relates the scaling action on L^2(R) to H=PQ and compares absorption vs emission spectra (Figures 1-5 and Maslov phase remark). Sect. 2 recalls the semi-local trace formula and the quantized differential d^-f=[H,f]. Sect. 3 translates X.-J. Li's attempt into the criterion (u^{-1}d^-u<=0) and shows by Lemma 3.4/Cor 3.5 it would hold iff u* inner; checks via explicit local factors (3.3)-(3.4) that u_v* is not inner, and Fact 3.6 (Riemann-Siegel angle not monotonic) that inequality (3.1) is false for S={infty}. Sect. 4 states Conjecture 4.1 and discusses Poisson formula and Sonine space (Kahane's construction). Imports: Connes 1999 trace formula, Weil's criterion, Bombieri's compact-support reduction [4].

Dependency edges: CAND-02189 → Connes 1999 semi-local trace formula (builds_on); CAND-01965 → CAND-02189 (builds_on); CAND-02188 → CAND-02189 (builds_on)

**Imported results.** Connes 1999 semi-local trace formula (Lemma 2.4); Weil's criterion for RH via explicit formula negativity; Bombieri / Yoshida-type compact support reduction ([4], [5]); Kahane's construction of Sonine space elements ([8]); Riemann-Siegel theta function and u_infty = e^{2 i theta} ([12] Ch. II Lemma 2.20)

**Techniques.** quantized calculus (commutator with the sign operator F=2P-1); Beurling inner functions / Hardy spaces of half-planes; semi-local trace formula; Poisson summation; Riemann-Siegel theta function; semiclassical Weyl-law heuristics

## Context and interpretation

**Importance and obstacle overcome.** Clarifies why the Berry-Keating 'emission' picture and Connes' 'absorption' picture are consistent semiclassically, and gives a clean criterion (Lemma 3.4/Cor 3.5) explaining exactly why Li's attempt cannot work: unimodular local ratio functions are not inner. Poses the operator-theoretic conjecture that later motivated CAND-01965 and CAND-02188.

**Relation to prior work.** Builds on Connes 1999 and Connes-Marcolli book; critique of X.-J. Li's attempt; reconciles with Berry-Keating [1,2]. Followed by CAND-01965 (Weil positivity archimedean) and CAND-02188 (quasi-inner functions).

**Limitations and open questions.** The paper proves no new positivity result; Conjecture 4.1 (semi-local framework proves Weil's inequality for test functions with support in (q^{-1/2},q^{1/2})) is open at the time (later partially addressed in CAND-01965 for q=2 and single archimedean place). The authors note any such approach must respect the global Poisson formula normalizing principal values at primes in S (a naive truncation to a finite set of primes ignores this). Fact 3.6 shows the unrestricted inequality (3.1) is false, so support restrictions are essential.

**Ideas in remarks/appendices/abandoned paths.** Remark 4.2: $\Delta_2=D_u^2-D_u$ (adjoint of the Sonine-producing operator) provides the tropical structure of the Scaling Site per [14] eq. (1); the Poisson formula seen as the conceptual reason for Kahane's Sonine functions (Sect. 4.1).

## Research potential

- **Hypotheses that might be weakened.** Conjecture 4.1's support window (q^{-1/2},q^{1/2}) and the vanishing conditions (4.1): can the window be extended using structure of Sonine space elements built from Kahane's D(Pi)?
- **Generalizations.** Criterion Lemma 3.4 holds for any unitary u and projection P; apply it to other modulated groups (Def 2.1 extension), to L-functions with characters, and to number fields via the semi-local adele class spaces.
- **Candidate connections.** Beurling inner functions and de Branges spaces; Riemann-Siegel theta monotonicity (Fact 3.6) and local counting of zeros; Kahane's Sonine functions D(Pi) and the Poisson summation formula.
- **Reusable lemmas.** Lemma 3.4 (three-way equivalence), Corollary 3.5 (inner iff), explicit unboundedness check phi(20) (eq. after 3.4) as a minimal counterexample to innerness.
- **Possible experiments.** Numerically construct elements of the semi-local Sonine space via D=Du^2+Du applied to the Poisson distribution smoothed with a small support function; test numerically the sign of Weil functional on S={inf,2,3} for test functions supported in (q^{-1/2},q^{1/2}) with q=5 to probe Conjecture 4.1; verify non-monotonicity of theta and the quantity i u^{-1}u' on the critical line to illustrate Fact 3.6.
- **Risks / barriers.** Conjecture 4.1 is essentially a positivity statement of Weil type for larger and larger supports; ignoring the global Poisson normalization of principal values (as in Li's approach) breaks the argument; Fact 3.6 shows positivity cannot hold without support restrictions.

## Audit notes (Level 1 reader)

Fact 3.6 as stated refers to inequality (3.1) written in the extracted text as '\sum_{Q^*}|1-w|h(w)d^*u<=0' (line 612); the sum/integral notation looks garbled in extraction, so the exact form of (3.1) should be verified against the original; Section 1 semiclassical computations and Sect. 4.2 were not read, so the claims about Maslov phases are reported from the introduction only.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02189`; harvest queries: kw_RH_any, kw_trace_formula_zeta, kw_weil_positivity, kw_zeta_zeros, arxiv_berry_keating, arxiv_connes_rh, arxiv_rh_abs, arxiv_weil_explicit, arxiv_zeta_zeros.
- Triage decision: include — Connes-Consani on scaling Hamiltonian linking Berry-Keating and spectral realization.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
