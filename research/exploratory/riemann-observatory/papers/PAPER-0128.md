# PAPER-0128 — Conjectures for the integral moments and ratios of \(L\)-functions over function fields

| Field | Value |
|---|---|
| Authors | Andrade, J. C.; Keating, J. P. |
| Year / stratum | 2014 / S5 |
| Venue | J. Number Theory 142, 102-148 (2014). |
| Identifiers | zbMATH [1318.11083](https://zbmath.org/?q=an:1318.11083) · DOI [10.1016/j.jnt.2014.02.019](https://doi.org/10.1016/j.jnt.2014.02.019) · arXiv [1407.3099](https://arxiv.org/abs/1407.3099) |
| MSC | 11G20, 11M50, 14G10 |
| Families | B, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1407.3099 |
| Selection | score 3.8808, in-pool citations 28, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Extend the Conrey-Farmer-Keating-Rubinstein-Snaith (CFKRS) recipe for integral moments, and the Conrey-Farmer-Zirnbauer ratios recipe, to the symplectic family of quadratic Dirichlet L-functions L(s,chi_D) over F_q[x], D in H_{2g+1,q} (monic squarefree, degree 2g+1), with q fixed and g->infinity. Equivalently, the family of zeta numerators of genus-g hyperelliptic curves y^2=D(x). The paper then derives explicit lower-order moment formulas and the one-level density from the ratios conjecture.

**Historical motivation.** Katz-Sarnak studies q->infinity at fixed genus; the g->infinity at fixed q regime is the true analogue of the number-field limit (conductor to infinity, fixed ground field). CFKRS-type conjectures give full polynomial lower-order terms for number-field moments; testing them over F_q[x] is attractive because RH is a theorem there and exact computation is possible.

### Main results

- **THM-PAPER-0128-1** (Conjecture 5 (Sec. 3, eqs. 3.1-3.6), conjecture (heuristic, CFKRS recipe), scope: conditional; Section 3, eqs (3.3)-(3.6); recipe in Section 4). Let $q$ be odd and fixed, $X(s)=q^{-1/2+s}$, $X_D(s)=|D|^{1/2-s}X(s)$ (so $L(s,\chi_D)=X_D(s)L(1-s,\chi_D)$ for $D\in\mathcal H_{2g+1,q}$). Then for fixed integer $k\ge1$, as $g\to\infty$: $\sum_{D\in\mathcal H_{2g+1,q}}L(\tfrac12,\chi_D)^k=\sum_{D}Q_k(\log_q|D|)(1+o(1))$, where $Q_k$ is a polynomial of degree $k(k+1)/2$ given by the $k$-fold residue $Q_k(x)=\frac{(-1)^{k(k-1)/2}2^k}{k!}\frac{1}{(2\pi i)^k}\oint\!\cdots\!\oint \frac{G(z_1,\dots,z_k)\Delta(z_1^2,\dots,z_k^2)^2}{\prod_j z_j^{2k-1}}q^{\frac x2\sum_j z_j}\,dz_1\cdots dz_k$, with $G=A(\tfrac12;z)\prod_j X(\tfrac12+z_j)^{-1/2}\prod_{i\le j}\zeta_A(1+z_i+z_j)$, $\zeta_A(s)=(1-q^{1-s})^{-1}$, and $A(\tfrac12;z)$ the Euler product (3.6) over monic irreducible $P$ (absolutely convergent for $|\Re z_j|<\tfrac12$). *Conditional on:* unproved CFKRS recipe (stated in Sec. 4 as used 'without rigorous justification in each step').
- **THM-PAPER-0128-2** (Remark 3 / Sec 5.1, consistency check with a theorem, scope: asymptotic; Sec. 5.1). For $k=1$ the conjecture reduces to $Q_1(x)=ax+b$ and coincides with the first-moment theorem of Andrade-Keating [AK] (imported, unconditional result for $\sum_{D\in\mathcal H_{2g+1,q}}L(1/2,\chi_D)$ with main term of size $|D|\log_q|D|/\zeta_A(2)$ times a constant; the explicit constant was not independently verified by me).
- **THM-PAPER-0128-3** (Sec 5.2, eqs (5.18)-(5.23), conjecture (specialization of Conj. 5), scope: conditional; Sec. 5.2). Second moment: $\sum_{D}L(\tfrac12,\chi_D)^2=\sum_D Q_2(\log_q|D|)(1+o(1))$ with $Q_2$ cubic, leading term involving $A(\tfrac12;0,0)=\prod_P\bigl(1-\frac{4|P|^2-3|P|+1}{|P|^4+|P|^3}\bigr)$ (function-field analogue of Jutila's constant (1.14)). *Conditional on:* Conjecture 5.
- **THM-PAPER-0128-4** (Sec 5.3, eqs (5.24)-(5.28), conjecture (specialization), scope: conditional; Sec. 5.3 (eq. 5.27 writes A(1/2;0,0) where A(1/2;0,0,0) is meant: typo)). Third moment leading order: $\sum_{D\in\mathcal H_{2g+1,q}}L(\tfrac12,\chi_D)^3\sim\frac{1}{2880\,\zeta_A(2)}A(\tfrac12;0,0,0)\,|D|(\log_q|D|)^6$, with $A(\tfrac12;0,0,0)=\prod_P\bigl(1-\frac{12|P|^5-23|P|^4+23|P|^3-15|P|^2+6|P|-1}{|P|^6(|P|+1)}\bigr)$, matching the shape of Soundararajan's number-field constant (1.15). The coefficient list was obtained by Mathematica (5.26). *Conditional on:* Conjecture 5.
- **THM-PAPER-0128-5** (Theorem 1 (eq. 5.29), theorem (conditional on Conjecture 5), scope: conditional; Sec. 5.4, eq. (5.29); proof via Lemma 5 (follows Keating-Odgers [KO])). Assuming Conjecture 5, for each fixed $k\in\mathbb N$, as $g\to\infty$: $\sum_{D\in\mathcal H_{2g+1,q}}L(\tfrac12,\chi_D)^k\sim\frac{|D|}{\zeta_A(2)}(\log_q|D|)^{k(k+1)/2}A(\tfrac12;0,\dots,0)\prod_{j=1}^k\frac{j!}{(2j)!}$. (For k=3, $\prod j!/(2j)!=1/2880$, consistent with 5.27.) *Conditional on:* Conjecture 5.
- **THM-PAPER-0128-6** (Conjecture 6 (3.7-3.9) and Conjecture 7 (6.34), conjecture (ratios, CFZ recipe), scope: conditional; Sec. 3 (3.7)-(3.11); Sec. 6.2 (6.34)). For $\Re\alpha_k,\Re\gamma_m>0$ (with the usual size restrictions): $\sum_{D\in\mathcal H_{2g+1,q}}\prod_{k=1}^K L(\tfrac12+\alpha_k,\chi_D)\big/\prod_{m=1}^Q L(\tfrac12+\gamma_m,\chi_D)=\sum_D\sum_{\epsilon\in\{\pm1\}^K}|D|^{\frac12\sum_k(\epsilon_k\alpha_k-\alpha_k)}\prod_k X(\tfrac12+\tfrac{\alpha_k-\epsilon_k\alpha_k}{2})\,Y(\epsilon\alpha;\gamma)A_D(\epsilon\alpha;\gamma)+o(|D|)$ with $Y$ the $\zeta_A$-ratio (3.9) and $A_D$ the Euler product (3.8). Conjecture 7 is the equivalent K-fold contour-integral form over $|z_i|=1$ with kernel $\Delta(z^2)^2\prod z_k/\prod_{j,k}(z_k-\alpha_j)(z_k+\alpha_j)$. *Conditional on:* unproved CFZ recipe.
- **THM-PAPER-0128-7** (Conjecture 8 (7.2-7.3), conjecture (K=Q=1 ratios), scope: conditional; Sec. 7, eqs (7.2)-(7.3)). For $-\tfrac14<\Re\alpha<\tfrac14$, $\tfrac1{\log|D|}\ll\Re\gamma<\tfrac14$, $\Im\alpha,\Im\gamma\ll_\varepsilon|D|^{1-\varepsilon}$: $\sum_D\frac{L(\frac12+\alpha,\chi_D)}{L(\frac12+\gamma,\chi_D)}=\sum_D\Bigl(\frac{\zeta_A(1+2\alpha)}{\zeta_A(1+\alpha+\gamma)}A_D(\alpha;\gamma)+|D|^{-\alpha}X(\tfrac12+\alpha)\frac{\zeta_A(1-2\alpha)}{\zeta_A(1-\alpha+\gamma)}A_D(-\alpha;\gamma)\Bigr)+o(|D|)$. *Conditional on:* Conjecture 6 / ratios recipe.
- **THM-PAPER-0128-8** (Theorems 2 and 3 (7.9-7.17, 7.17), theorem (conditional on Conj. 8), scope: conditional; Sec. 7, Theorems 2, 3). Theorem 2: under Conj. 8, $\sum_D L'/L(\tfrac12+r,\chi_D)=\sum_D\bigl[\frac{\zeta_A'}{\zeta_A}(1+2r)+A_D'(r;r)-(\log q)|D|^{-r}X(\tfrac12+r)\zeta_A(1-2r)A_D(-r;r)\bigr]$ (error o(|D|)). Theorem 3: for even periodic nice test function $f$ the one-level density $S_1(f)=\sum_D\sum_{\gamma_D}f(\gamma_D)=\frac1{2\pi}\int_{-\pi/\log q}^{\pi/\log q}f(t)\sum_D\bigl[\log|D|+\frac{X'}{X}\text{-term}+2\frac{\zeta_A'}{\zeta_A}(1+2it)+A_D'(it;it)-(\log q)|D|^{-it}X(\tfrac12+it)\zeta_A(1-2it)A_D(-it;it)\bigr]dt+o(|D|)$ (precise form eq. 7.17), with $A_D(r;r)=1$ and the explicit $A_D'(r;r)=\sum_P\frac{\log|P|}{(|P|^{1+2r}-1)(|P|+1)}$. *Conditional on:* Conjecture 8.

### Key definitions

- H_{2g+1,q}: squarefree monic polynomials of degree 2g+1 over F_q, with #H=(q-1)q^{2g}
- chi_D(f)=(D/f) quadratic residue symbol on F_q[x]
- L(u,chi_D)=L(q^{-s},chi_D); for odd degree equals L*(u,chi_D), a polynomial of degree 2g with functional equation L*(u)=(qu^2)^g L*(1/(qu))
- zeta_A(s)=1/(1-q^{1-s})
- A(1/2;z), A_D(alpha;gamma): arithmetic Euler-product factors

### Principal lemmas

- **THM-PAPER-0128-L1** (Lemma 5 (eqs 5.30-5.31); Sec. 5.4). Let $F$ be symmetric in $k$ variables, regular near 0, and $f$ have a simple pole of residue 1 at $0$, otherwise analytic nearby. With $K(|D|;w)=\sum_{\epsilon_j=\pm1}e^{\frac12\log|D|\sum\epsilon_jw_j}F(\epsilon w)\prod_{i\le j}f(\epsilon_iw_i+\epsilon_jw_j)$ and $I(|D|,k;0)$ its value at $w=0$: $I(|D|,k;0)\sim(\tfrac12\log|D|)^{k(k+1)/2}F(0,\dots,0)2^{k(k+1)/2}\prod_{j=1}^k\frac{j!}{(2j)!}$. — *Role:* Extracts the leading coefficient of the k-th moment conjecture; imported-style computation following Keating-Odgers [KO] and CFKRS Lemma 2.5.2

### Proof architecture

No theorem about the family is proved unconditionally in the paper. (1) Setup: for squarefree monic D of degree 2g+1, L(u,chi_D) is the numerator P_C(u) of the zeta function of y^2=D(x); RH (Weil) is known; functional equation L(s,chi_D)=X_D(s)L(1-s,chi_D) with X(s)=q^{-1/2+s}; ensemble averages via Moebius sieve over A^2|D (2.29). (2) Recipe (Sec. 4): insert shifts alpha_j, use the approximate functional equation (a polynomial of degree 2g so it is a finite exact identity with a sum over 2^k sign patterns), average the n-sums over D keeping only the 'diagonal' squares (the arithmetical factor A as Euler product, and zeta_A factors from the polar structure), then sum over sign choices and rewrite as the k-fold contour integral; send shifts to 0. Each step is unjustified, and the whole is checked against RMT (Sp(2g)) analogies and known results (k=1 theorem [AK]). (3) Moments Sec. 5: evaluate residues for k=1,2,3 (k=3 by Mathematica), then general k leading term via Lemma 5 (Theorem 1). (4) Ratios Sec. 6: same recipe with the Euler product A_D and Y-factor, converted to contour form (Conj. 7). (5) Sec. 7: differentiate Conj. 8 at alpha=gamma=r to get L'/L averages, then the explicit-formula-type integral to get one-level density (Theorem 3).

Dependency edges: CAND-01731 → CFKRS (Conrey-Farmer-Keating-Rubinstein-Snaith, Proc. LMS 2005) (adapts recipe); CAND-01731 → Conrey-Farmer-Zirnbauer ratios conjecture (adapts recipe); CAND-01731 → Andrade-Keating first moment theorem [AK] (consistency check (k=1)); CAND-01731 → Keating-Snaith (CMP 2000) symplectic moments (RMT analogue / leading-order agreement)

**Imported results.** Weil: Riemann hypothesis for curves over finite fields (eq 2.4); Rosen, Number Theory in Function Fields: Prop. 4.3, 14.6, 17.7 (polynomial nature, functional equation, identification with Artin L-function); Andrade-Keating (AK): first moment theorem for the hyperelliptic ensemble; CFKRS Lemma 2.5.2 (symmetrization lemma for sums over sign patterns); Keating-Odgers [KO] for the leading-order computation; Keating-Snaith conjectures 1,2; Jutila (1.11),(1.13); Soundararajan (1.15)

**Techniques.** CFKRS recipe adapted to F_q[x]; approximate functional equation as exact finite identity (polynomial L-function); Moebius sieving of squarefree polynomials; multi-variable contour integral / residue calculus with Vandermonde-squared kernel; Euler-product arithmetic factors A(1/2;z); ratios conjecture and differentiation to get L'/L; Random-matrix analogy with USp(2g)

## Context and interpretation

**Importance and obstacle overcome.** First systematic transfer of the full CFKRS/CFZ recipe (including all lower-order terms and ratios) to function fields with fixed q, g->infinity. Obstacle: absence of unconditional moment results beyond k=1 in this regime, and the need to adapt the recipe to the exactly-finite approximate functional equation and to the arithmetic of F_q[x]. Key payoff is a precise, testable prediction: the polynomial Q_k and the one-level density with lower-order terms.

**Relation to prior work.** Function-field analogue of CFKRS (number-field quadratic Dirichlet moments, Conjecture 3 here) and of Keating-Snaith symplectic moment conjecture; the leading coefficient agrees with the shape of Jutila (k=1,2) and Soundararajan (k=3). Builds on Andrade-Keating [AK] (k=1 theorem, and later work on k=2 by Florea is not in this paper).

**Limitations and open questions.** All main results are conditional on unproved heuristics. Remark 2 in the paper notes that the original CFKRS error term O(|d|^{-1/2+eps}) is believed to fail (extraneous lower-order terms, Diaconu-Goldfeld-Hoffstein, k>=3), so Conj. 5 is stated only with o(1) error. Sizes of the o(|D|) and the allowed ranges of alpha, gamma in the ratios conjectures are not justified. Not addressed: other families (cubic, non-hyperelliptic), proofs of the second or third moment, uniformity in q.

## Research potential

- **Hypotheses that might be weakened.** The error term o(1) in Conj. 5 could be replaced by an explicit conjectured secondary term of size |D|^{-1/2} or q^{-g/3}-type (cf. Remark 2 and the later Diaconu-Goldfeld-Hoffstein / Florea refinement): the paper's recipe cannot see such terms. The restriction to q odd and prime-degree-free squarefree D of odd degree 2g+1 could be relaxed to even degree (extra trivial zero, eq. 2.18).
- **Generalizations.** Apply the same recipe to L(s,chi_D)-families of other symmetry type (unitary: Dirichlet characters of F_q[x] mod a fixed polynomial; orthogonal: quadratic twists of elliptic-curve L-functions over F_q(t)), and to ratios of derivatives or mollified moments.
- **Candidate connections.** Because RH holds for these L-functions, Q_k(log_q|D|) can be compared to the USp(2g) moments of characteristic polynomials; any discrepancy for k>=3 against exact counting (computable for small g,q by enumerating D) bears on the recipe, hence on the Riemann Observatory's 'family identity versus extraction' distinction. The one-level density formula (Thm 3) is a testable lower-order correction to the Katz-Sarnak density.
- **Reusable lemmas.** Lemma 5 and eq. (4.61)/(5.30-5.33) give a self-contained leading-coefficient extraction for any symplectic-type k-th moment conjecture.
- **Possible experiments.** For q=3,5,7 and g up to ~8-10 enumerate H_{2g+1,q}, compute sum L(1/2,chi_D)^k (k=2,3) exactly via polynomial point counts, and fit against Q_k(log_q|D|) with the Euler product A truncated; check whether residuals follow the Remark-2 secondary terms.
- **Risks / barriers.** Fixed-q, g->infinity is not accessible by Deligne equidistribution (that handles q->infinity), so no route to a proof of k>=2; the recipe is heuristic and its agreement with data is evidence only, not for any statement about zeta zeros over Q.

## Audit notes (Level 1 reader)

Typo at eq. (5.27): A(1/2;0,0,0) written as A(1/2;0,0). Eq (5.26) contains duplicated terms (e.g. '3A222223' listed twice and 'A11112' vs 'A111112'-style indexing) in the OCR text, probably transcription issues; not checked. Theorem 1 and Sec 5.3 are conditional on Conjecture 5 despite being labeled 'Theorem'. Introduction writes (1.16) with factor in terms of k(k+1)/2 and a_{k,Sp}; not checked against Keating-Snaith. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01731`; harvest queries: msc_11M50.
- Triage decision: include — Moment/ratio conjectures in function fields, where RH is a theorem.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
