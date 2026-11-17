# PAPER-0118 — Sur l'hypothèse de Riemann.

| Field | Value |
|---|---|
| Authors | Riesz, M. |
| Year / stratum | 1916 / S2 |
| Venue | Acta Math. 40, 185-190 (1916). |
| Identifiers | zbMATH [46.0497.03](https://zbmath.org/?q=an:46.0497.03) · DOI [10.1007/BF02418544](https://doi.org/10.1007/BF02418544) |
| MSC | 11M26 |
| Families | C |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://mwolf.pracownicy.uksw.edu.pl/Riesz_translation.pdf |
| Selection | score 4.0905, in-pool citations 16, seed lists 2, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Give a necessary and sufficient growth condition on an explicit entire function F(x) (Riesz function) equivalent to RH, via a Mellin transform representation of Gamma(1-s/2)/zeta(s).

**Historical motivation.** Following Littlewood 1912 and Landau 1909 on bounds for 1/zeta, M(x)=O(x^{1/2+eps}) type equivalences; Riesz seeks a function-theoretic reformulation.

### Main results

- **THM-PAPER-0118-1** (Eq. (1) (sec. 2), identity (representation), scope: global; sec. 2, eqs. (1),(2)). With $C_k=\sum_{n\ge1}n^{-2k}=\zeta(2k)$ and $F(x)=\sum_{k\ge1}\frac{(-1)^{k+1}x^k}{C_k\,\Gamma(k)}$, one has $F(x)=\frac1{2i}\int_{a-i\infty}^{a+i\infty}\frac{x^z}{\zeta(2z)\Gamma(z)\sin(\pi z)}\,dz$ for $a$ in a fixed range with $a\ge 1/2$ (garbled in translation; unconditionally valid at $a=1/2$ up to $1$), absolutely/uniformly convergent for $-\pi/2+\delta\le\arg x\le\pi/2-\delta$ (sign of angle range garbled in translation).
- **THM-PAPER-0118-2** (Eq. (3), theorem (unconditional), scope: asymptotic; sec. 2). $F(x)=o(x^{1/2})$ as $x\to\infty$ uniformly in an angle $|\arg x|\le \pi/2-\delta$.
- **THM-PAPER-0118-3** (Eq. (5) (sec. 3), theorem (Mellin transform identity), scope: global; sec. 3, eqs. (4),(5)). For $\delta\le\Re s\le 2-\delta$ (strip given in translation as $z+\delta\le\Re s\le 2-\delta$, garbled, $1\ldots$ lower bound $\delta$ unconditional range $0<\Re s<2$ intersected with convergence) : $\dfrac{\Gamma(1-s/2)}{\zeta(s)}=\int_0^\infty x^{-(s/2+1)}F(x)\,dx$.
- **THM-PAPER-0118-4** (Eq. (6) / sec. 4 conclusion, theorem (equivalence), scope: global; sec. 4). RH holds iff for every $\delta>0$, $F(x)=O\big(x^{1/4+\delta}\big)$ as $x\to+\infty$ along the positive real axis.
- **THM-PAPER-0118-5** (remark in sec. 4, identity / remark, scope: global; sec. 4 end and sec. 5). $F(x)=\sum_{n\ge1}\mu(n)\frac{x}{n^2}e^{-x/n^2}$; also $\sum_{n\ge1}F(x/n^2)=xe^{-x}$.
- **THM-PAPER-0118-6** (sec. 4 remark, theorem (Phragmen-Lindelof reduction), scope: asymptotic; sec. 4). If $F(x)=O(x^{1/4+\delta})$ holds on some sector (half-plane-like angle) inside $|\arg x|<\pi/2$, it holds on the positive real axis; conversely (6) on the positive real axis implies it in any such angle.
- **THM-PAPER-0118-7** (sec. 5, theorem (zeros of F), scope: global; sec. 5 eqs. (7)-(9)). $F$ is entire of order 1 (exponential type 1, $|F(x)|<|x|e^{|x|}$), $F(x)/ (xe^{-x}\cdot)$-type limit $e^{x}F(-x)/x\to -1$ hmm (translation: $\lim e^{-x}F(-x)/x=-1$) as $x\to+\infty$; its zeros $\gamma_\nu$ satisfy $\sum|\gamma_\nu|^{-1-\epsilon}<\infty$ but $\sum|\gamma_\nu|^{-1}=\infty$; canonical form $F(x)=xe^{\gamma x}\prod(1-x/\gamma_\nu)e^{x/\gamma_\nu}$; $F$ has infinitely many non-real zeros and changes sign on $(0,\infty)$ at least once.

### Key definitions

- $F(x)=\sum_{k\ge1}(-1)^{k+1}x^k/(\zeta(2k)\,(k-1)!)$ (Riesz function)

### Principal lemmas

- **THM-PAPER-0118-L1** (sec. 3 inversion; sec. 3). Interchange of $\sum_n$ and $\int_0^\infty$ in $\zeta(s)\phi(s)=\sum_n\int x^{-(s/2+1)}F(x/n^2)dx$ is legitimate, using $|F(x/n^2)|<M(x/n^2)^a$ with $1/2<a<\Re s/2$. — *Role:* Gives Mellin identity (5).
- **THM-PAPER-0118-L2** (sec. 4 (Landau/Caratheodory); sec. 4, cites Landau Handbuch II p.870). Under RH, $1/\zeta(s)=O(|s|^r)$ for $\Re s\ge 1/2+\delta$, $r=r(\delta)$. — *Role:* Imported: lets one shift $a$ down to $1/4+\epsilon$ in (1), giving $F=O(x^{1/4+\epsilon})$ (necessity).
- **THM-PAPER-0118-L3** (sec. 5 Polya theorem; sec. 5). Entire $\Phi=\sum a_nx^n$ of the form (8) (genus<=1 with real/complex zero data) also has form (9) (all real zeros of one sign) iff one of the sequences $(a_n)$, $((-1)^na_n)$ has finitely many sign changes. — *Role:* Imported; shows F has infinitely many non-real zeros.

### Proof architecture

Contour representation (1) of F by residues at z=k of 1/(zeta(2z)Gamma(z) sin pi z). Unconditionally a=1/2 gives F=o(x^{1/2}); Mellin transform of F then equals Gamma(1-s/2)/zeta(s) on 0<Re s<2 (via sum over n of F(x/n^2)=x e^{-x}). Sufficiency: F=O(x^{1/4+delta}) makes the Mellin integral converge absolutely for Re s>1/2+delta, giving analytic continuation of Gamma(1-s/2)/zeta(s), hence no zeros of zeta there. Necessity: under RH, polynomial bound on 1/zeta (Landau-Caratheodory) lets contour be moved to a=1/4+epsilon. Sections 5-6 add structure of F (type one, genus-1 product, infinitely many nonreal zeros, sign change).

**Imported results.** Landau, Handbuch I pp.177-178: order of 1/zeta(s) near Re s=1; Landau Handbuch II p.870 (via Caratheodory): under RH 1/zeta(s)=O(|s|^r), Re s>=1/2+delta; Littlewood C. R. 29 Jan 1912: under RH zeta(s)=O(|s|^eps); Polya J. reine angew. Math. 145 (1915): sign changes and zero distribution of genus 0/1 entire functions; Phragmen-Lindelof; Hadamard/Poincare factorization

**Techniques.** Mellin transform; residues; Phragmen-Lindelof; Hadamard factorization

## Context and interpretation

**Importance and obstacle overcome.** First analytic equivalence of RH with growth of an explicit entire function (the Riesz function / Riesz criterion). Obstacle: converting a statement about a zero-free half-plane into a growth bound on a power series with zeta(2k) denominators, via Mellin duality with Gamma(1-s/2)/zeta(s).

**Relation to prior work.** Uses Landau Handbuch (1909) bound for 1/zeta; Littlewood (C. R. 1912) conditional bounds; Caratheodory theorem via Landau; Polya 1915. Reformulates the equivalent M(x)=O(x^{1/2+eps}) (Littlewood) in terms of an entire function (identity F(x)=sum mu(n)(x/n^2)e^{-x/n^2} makes link to M).

**Limitations and open questions.** Author states he cannot decide whether the criterion facilitates checking RH. Criterion is global (all x), not a finite test. Only the necessity direction needs imported RH-consequence (polynomial bound for 1/zeta).

**Ideas in remarks/appendices/abandoned paths.** sec. 4 last paragraph: method gives reciprocal of any Dirichlet series (not just zeta) as Mellin transform of an entire function; sec. 5: sign-change/zero structure of F (infinitely many nonreal zeros) as a function-theoretic side question; closing remark that F changes sign at least once on the positive axis (since F(x)=O(x^{1/4-delta}) is impossible).

## Research potential

- **Hypotheses that might be weakened.** Replace exponent 1/4 by quantitative form: RH with explicit error constants corresponds to x^{1/4} F(x) bounds (Riesz-type criteria of Baez-Duarte style with Mobius); the o(x^{1/2}) unconditional (3) could be sharpened using the best zero-free region to get a free unconditional bound e^{-c log^{3/5}}.
- **Generalizations.** The F(x)=sum mu(n)(x/n^2)e^{-x/n^2} identity generalizes to L(s,chi) (replace mu by mu*chi); dual Mellin pair Gamma(1-s/2)/zeta(s) generalizes to Dirichlet series with functional equation.
- **Candidate connections.** Link to Baez-Duarte and Nyman-Beurling (Riesz/Hardy-Littlewood criteria), Hardy-Littlewood 1918 criterion sum (-x)^k/(k! zeta(2k+1)); zero statistics of F (infinitely many nonreal zeros) connect to Polya-type questions and to the work of Titchmarsh on the Riesz function.
- **Reusable lemmas.** Mellin pair Gamma(1-s/2)/zeta(s) <-> F(x); the interchange-of-sum lemma (sec. 3); Polya sign-change theorem application (sec. 5).
- **Possible experiments.** Compute F(x) with mpmath for x up to 1e6 using the alternating series (needs large precision) or the Mobius series; fit growth exponents of x^{-1/4}F(x) and locate sign changes/zeros; test certified bounds on 1/4+delta exponent.
- **Risks / barriers.** Equivalence is global and gives no finite certificate; any numerical growth study is heuristic. Cancellation in the alternating series requires extremely high precision.

## Audit notes (Level 1 reader)

Basis: English translation not the original French. Translation garbles several formulae (range of a in (1) printed '1/4 <= a <= 1/2' vs. expected 1/2<=a<=1; angle ranges; the limit lim e^{-x}F(-x)/x; 'internal excitation'). Section 3 strip lower bound garbled ('z+delta'). In the Hadamard step the translation reads 'series sum 1/|gamma|^{1+eps} convergent' which is consistent. No actual error identified in logic of inspected portion; the necessity step relies on Landau-Caratheodory polynomial bound being applied to the shifted contour with uniform decay of 1/(Gamma(z) sin pi z) in vertical strips, not detailed. Triage statement consistent (up to overall sign (-1)^{k+1} vs (-1)^k, which equals sign convention of F).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00074`; harvest queries: kw_RH_any, msc_11M26.
- Triage decision: include — Riesz 1916 criterion for RH.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
