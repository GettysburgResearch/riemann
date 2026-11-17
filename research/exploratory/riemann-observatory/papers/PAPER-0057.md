# PAPER-0057 — An explicit region without zeros for the Riemann \(\zeta\) function.

*Original title:* Une région explicite sans zéros pour la fonction \(\zeta\) de Riemann.

| Field | Value |
|---|---|
| Authors | Kadiri, Habiba |
| Year / stratum | 2005 / S5 |
| Venue | Acta Arith. 117, No. 4, 303-339 (2005). |
| Identifiers | zbMATH [1101.11029](https://zbmath.org/?q=an:1101.11029) · DOI [10.4064/aa117-4-1](https://doi.org/10.4064/aa117-4-1) · arXiv [math/0401238](https://arxiv.org/abs/math/0401238) |
| MSC | 11M06, 11M26 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — arXiv:math/0401238v1 |
| Selection | score 4.5506, in-pool citations 24, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Give an explicit zero-free region $\Re s\ge1-1/(R_0\log|\Im s|)$, $|\Im s|\ge2$, for the Riemann zeta function with the smallest possible explicit $R_0$.

**Historical motivation.** Explicit versions of the de la Vallee Poussin zero-free region R_0=34.82 (1899) were improved by Rosser to 19, Rosser-Schoenfeld to 17.516 then 9.6459, Ford to 8.463. Explicit constants feed explicit error terms for the prime number theorem and psi(x), theta(x) estimates.

### Main results

- **THM-PAPER-0057-1** (Theoreme 1.1 (Principal), theorem, scope: global; Sec 1, p.2). $\zeta(s)\ne0$ for $\Re s\ge1-\dfrac{1}{R_0\log|\Im s|}$ with $|\Im s|\ge2$, where $R_0=5.70176$ (arXiv v1 and its abstract). The published Acta Arith. version is recalled (by the triage field, unverified here) as $R_0=5.69693$. *Conditional on:* numerical zero verification to height 3.3e9 imported as a hypothesis for zeros below that height.
- **THM-PAPER-0057-2** (Remark after Thm 1.1, remark, scope: asymptotic; Sec 1, p.3). The region is wider than the Ford-Vinogradov region (with $R_1=57.54$) up to $|\Im s|<e^{9402.562}$; the method generalizes to Dirichlet L-functions (author's reference [8]).

### Key definitions

- $\varrho=\beta+i\gamma$ nontrivial zero
- $\eta=1-\beta_0$
- Laplace transform $\tilde F(X,Y)=\int_0^de^{-(X+iY)t}f(t)dt$
- $D(z)=\tilde F(z)-\kappa\tilde F(z+\delta)$
- $R_0$: constant in zero-free region

### Principal lemmas

- **THM-PAPER-0057-L1** (Prop 2.1; Sec 2.1, eq (4)-(5)). Weil-type explicit formula for $\Re\sum_n\Lambda(n)n^{-s}g(\log n)$ in terms of the Laplace transform $\tilde F$ of $f*f$-type weight $F$, involving the sum over all zeros $\sum_{\varrho}\Re D(s-\varrho)$, with $D=\tilde F-\kappa\tilde F(\cdot+\delta)$. — *Role:* Expresses the prime-side positive quantity as an integral/gamma term minus a sum over zeros.
- **THM-PAPER-0057-L2** (Hypotheses (H1), (H2); Sec 2). Weight $f\in C^2([0,d])$ with support in $[0,d)$ and $f(d)=f'(0)=f'(d)=f''(d)=0$; Laplace transform $\tilde F(X,Y)\ge0$ for $X\ge0$. Weight built from Heath-Brown's compactly supported function $h_\theta$ times Stechkin's $1-\kappa e^{-\delta x}$. — *Role:* Positivity of zero-sum terms.
- **THM-PAPER-0057-L3** (Lemme 4.1 (Stechkin 1970); Sec 4). For $\sigma>1$, $\tau=(1+\sqrt{1+4\sigma^2})/2$: $\Re\!\left[\frac1{\sigma-1+\beta+i y}\right]\!+\!\ldots-\frac1{\sqrt5}\ldots\ge0$ (exact form garbled in extracted text), the symmetric-zero positivity trick. — *Role:* Imported; generalized in the paper to $\Re\tilde F(s-\varrho)+\Re\tilde F(s+1-\varrho)\ge0$ for $\Re(s-\varrho)>0$ (Sec 2.4).
- **THM-PAPER-0057-L4** (Props 2.2-2.5; Sec 2.3-2.5, eqs (8)-(9)). Bounds: gamma-factor term $\le\frac A2(1-\kappa)g_1(\theta)\eta\log\gamma_0+C_1(\eta)$; pole term $\le a_0\tilde F(\sigma-1,0)+C_2(\eta)$; zeros beyond $\gamma\ge\gamma_0+t_0$ contribute $\ge a_1\tilde F(\sigma-\beta_0,0)-C_3(\eta)$; $\Delta_2$ term $\le C_4(\eta)$. Constants such as $C(\eta)=\alpha_1\eta+\alpha_2\eta^2+\alpha_3\eta^3$ with $\alpha_2=344602.439$, $\alpha_3=5799250.773$ (as extracted). — *Role:* Make each piece explicit, yielding cubic polynomial in eta whose sign gives the zero-free condition.
- **THM-PAPER-0057-L5** (Trig polynomial; Sec 2.3). Degree-4 non-negative cosine polynomial $\sum_{k=0}^4a_k\cos k\theta$ (a_4=1, a_1=18.63362, a_2=11.4517, A=sum a_k=35.78532), a variant of Rosser-Schoenfeld's, positive by a product form $(\cdot+\cos y)^2(0.265+\cos y)^2$. — *Role:* Final positivity argument giving the 3-1-cos inequality analogue.
- **THM-PAPER-0057-L6** (Iteration table; end of Sec 2). Parameters $(r,R)$, $\eta_0$, $\kappa$, $\delta$ iterated to a fixed point: $R_0\mapsto5.974849,5.730454,5.704873,5.702090,5.701785,5.701753$ ending at $R_0=5.70175$ stated, announced rounded to 5.70176 with precision $10^{-5}$. — *Role:* Numerical fixed-point optimization of the constant; $\kappa_0=0.4389$, $\delta_0=0.6208$.

### Proof architecture

Use a Weil-type explicit formula with a smooth compactly supported weight g(log n) that is the product of Heath-Brown's weight (support compact, positive Laplace transform) and Stechkin's 1-kappa e^{-delta x}. Positivity of Re of prime sum with trigonometric polynomial a_k cos(k gamma_0 log n) gives an inequality (7) that must hold; assuming a zero beta_0+i gamma_0 near the line 1, each term is bounded explicitly: gamma term (Prop 2.2, Stirling, uses digamma bounds), pole term (Prop 2.3), the far-zero sum (Prop 2.5/4.4, needs lower bound), remainder (Prop 2.4). Positivity of the sum over non-nearby zeros uses a generalized Stechkin lemma. The result is a cubic C(eta) in eta=1-beta_0 times log gamma_0 which must be negative; the least R_0 follows by iterating the parameters. Zeros up to T_0=3.3e9 are excluded by numerical verification (Wedeniwski), entering via the constants (eta_0 and gamma_0 > T_0 lower bound).

Dependency edges: Theorem 1.1 → Props 2.1-2.5 (uses); Props 2.2-2.5 → Lemmas 3.2-3.6, 4.1-4.7 (proved by); Theorem 1.1 → RH verification height 3.3e9 (depends on)

**Imported results.** Rosser (1939) and Rosser-Schoenfeld (1962, 1975): R_0=19, 17.516, 9.645908801; Stechkin 1970 Lemma 2; Heath-Brown 1992 (compactly supported weight, Lemma 7.5); Wedeniwski / van de Lune-te Riele-Winter verification of RH to T_0=3.3e9; Ford 2002 (R_0=8.463 and Vinogradov-Korobov region with R_1=57.54); Weil explicit formulas

**Techniques.** Weil explicit formula with smoothed weights; Heath-Brown/Stechkin weight product; non-negative trigonometric polynomial of degree 4; generalization of Stechkin's symmetric-zero positivity lemma; explicit bounds on digamma; numerical fixed-point iteration of parameters

## Context and interpretation

**Importance and obstacle overcome.** First substantial drop below Ford's 8.463 to about 5.70 for the classical-type region, by combining two smooth-weight ideas and exploiting the ability to take Re s <= 1 thanks to compact support, a weakened positivity condition and a cubic optimization. Obstacle: obtaining fully explicit constants for each term with numerical zero verification. The region is unconditional; it does not approach RH.

**Relation to prior work.** Builds on Rosser-Schoenfeld, Stechkin, Heath-Brown and Ford. Compared with Ford's Vinogradov-Korobov-type region, this classical region is wider for |Im s| < e^{9402.562}. Generalization to Dirichlet L-functions is in the author's separate work.

**Limitations and open questions.** Region only of de la Vallee Poussin type (width 1/log), unconditional but far from RH. The explicit constant depends on numerical verification height T_0=3.3e9 (improved later by others). The final constant in arXiv v1 is 5.70176; the published version improved to 5.69693 (recollection by triage, not verified here). Further reduction seems to require new weights or better gamma/zeta bounds.

**Ideas in remarks/appendices/abandoned paths.** Sec 2.2: restricting to s with Re s <= 1 is possible because g has compact support; Sec 2: weakening Re G(z)>=0 to Re G(s-rho)+Re G(s+1-rho)>=0 via symmetry of zeros; the optimization by iterating (r,R) pairs to a common fixed point.

## Research potential

- **Hypotheses that might be weakened.** Dependence on T_0: raising the verified height lowers R_0 slightly (eta_0 and gamma_0 > T_0 enter Props 2.2-2.5); sensitivity could be quantified by rerunning the iteration table with a larger T_0.
- **Generalizations.** Dirichlet L-functions (author [8]); Dedekind zeta functions; zero-free regions for other families in the archive's L-function programme.
- **Candidate connections.** Explicit zero-free regions feed explicit bounds for psi(x)-x, for Robin-type inequalities, and for Mobius/Mertens bounds as in Ng CAND-01212 (unconditional Ivic bound uses the Vinogradov-Korobov region).
- **Reusable lemmas.** Generalized Stechkin lemma Re F(s-rho)+Re F(s+1-rho)>=0; the explicit-formula/weight machinery and the cubic C(eta) criterion.
- **Possible experiments.** Reproduce the iteration table for R_0 (parameters eta_0, kappa, delta) with interval arithmetic and the explicit constants C_1..C_4; check sensitivity to T_0 and to alternate degree-4 trigonometric polynomials.
- **Risks / barriers.** A proof-producing computation would need directed rounding for the constants listed (alpha_2, alpha_3 printed to 3 decimals), and the final R_0 differs between arXiv v1 and the journal, so provenance of the constant must be pinned to a version.

## Audit notes (Level 1 reader)

Version discrepancy: arXiv v1 (and its Resume) states R_0=5.70176 whereas the triage field recalls 5.69693 for the published Acta Arith. version; the paper's own text thanks the referee for an optimization of the Rosser-Schoenfeld polynomial and of theta which improves the final result, so the arXiv v1 constant may be pre-referee. Garbled extraction of Sec 2-4 means individual numerical constants (e.g., C_1(eta) <= -2718.913 eta, alpha_1) were not verified. The iteration table rounds 5.701752890 to 5.70175 in the text and then the Theorem states 5.70176 (rounding up for safety, presumably).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01238`; harvest queries: kw_zero_free, msc_11M06, msc_11M26.
- Triage decision: include — Widely cited explicit zero-free region.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
