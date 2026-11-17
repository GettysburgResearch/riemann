# PAPER-0038 — Nonnegative trigonometric polynomials and a zero-free region for the Riemann zeta-function

| Field | Value |
|---|---|
| Authors | Mossinghoff, Michael J.; Trudgian, Timothy S. |
| Year / stratum | 2015 / S5 |
| Venue | J. Number Theory 157, 329-349 (2015). |
| Identifiers | zbMATH [1334.11070](https://zbmath.org/?q=an:1334.11070) · DOI [10.1016/j.jnt.2015.05.010](https://doi.org/10.1016/j.jnt.2015.05.010) · arXiv [1410.3926](https://arxiv.org/abs/1410.3926) |
| MSC | 11M26, 42A05, 11Y35 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1410.3926 |
| Selection | score 4.5825, in-pool citations 34, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Reduce the constant R_0 in the explicit classical zero-free region $\sigma>1-1/(R_0\log|t|)$ of zeta, by improving Kadiri's method with better nonnegative trigonometric polynomials (found by simulated annealing) and a sharper treatment of the error term.

**Historical motivation.** Classical zero-free region from de la Vallee Poussin (R_0=30.47) improved through Westphal, Rosser-Schoenfeld, Stechkin, Kondratev, Ford, Kadiri (5.69693). Landau's 1908 problem on V is the surrogate for the best constant obtainable from this method.

### Main results

- **THM-PAPER-0038-1** (Theorem 1, theorem, scope: computational; Sec 1 p.3; proof by Kadiri's method with computed parameters, Sec 3 and Sec 6). $\zeta(\sigma+it)\ne0$ for $|t|\ge2$ and $\sigma>1-\frac{1}{5.573412\,\log|t|}$. This is the largest known zero-free region in the critical strip for $3.06\cdot10^{10}<|t|<\exp(10151.5)$. *Conditional on:* numerical verification of RH to height 3.06e10 (imported), validity of the numerical optimization step (finite computation).
- **THM-PAPER-0038-2** (Theorem 2, theorem, scope: computational; Sec 1 p.3; upper bound from the degree-40 polynomial F_40 (V_40<34.488992000856), Sec 6). Let $P_n$ be the set of even trigonometric polynomials $f_n(\varphi)=\sum_{k=0}^n a_k\cos k\varphi\ge0$ with $a_k\ge0$ and $a_1>a_0$, and $V=\lim_{n\to\infty}\inf_{f_n\in P_n}\frac{f_n(0)-a_0}{(\sqrt{a_1}-\sqrt{a_0})^2}$. Then $34.468305<V<34.4889920009$ (previously $34.468305<V<34.5035864$).
- **THM-PAPER-0038-3** (Corollary 1, corollary, scope: global; Sec 7). With $\epsilon_0(x)=\sqrt{8/(17\pi)}\,X^{1/2}e^{-X}$, $X=\sqrt{(\log x)/R}$, $R=6.315$: $|\theta(x)-x|\le x\epsilon_0(x)$ for $x\ge149$ and $|\psi(x)-x|\le x\epsilon_0(x)$ for $x\ge23$ (replacing 6.455 by 6.315 in Trudgian's earlier result). *Conditional on:* Theorem 1 converted to the form sigma>=1-1/(6.315 log|t/17|), t>=24 via [19].
- **THM-PAPER-0038-4** (Corollary 2, corollary, scope: global; Sec 7). For $x\ge229$: $|\pi(x)-\mathrm{li}(x)|\le0.2593\,\frac{x}{(\log x)^{3/4}}\exp\left(-\sqrt{\frac{\log x}{6.315}}\right)$. *Conditional on:* numerical bound theta(t)<t for t<1.39e17.

### Key definitions

- Classical zero-free region sigma>1-1/(R_0 log|t|)
- P_n: even nonnegative trig polynomials sum a_k cos k phi with a_k>=0, a_1>a_0
- Landau V_n=inf (f_n(0)-a_0)/(sqrt a_1 - sqrt a_0)^2, V=lim V_n

### Principal lemmas

- **THM-PAPER-0038-L1** (Eq. (2.2)-(3.1); Sec 2 and Sec 3). Kadiri's inequality $R_0\le\frac{A\,g_1(\theta)(1-\kappa)}{2(K(w,\theta)-C(\eta))}$ with $A=f_n(0)-a_0$, $g_1(\theta)=\sec^2\theta(3-\theta\tan\theta-3\theta\cot\theta)$, $K(w,\theta)=\int_0^{d_1(\theta)}(a_1e^{-u}-a_0)h_\theta(u)e^{wu}du$; improved to $R_0\le\frac A2 g_1(\theta)(1-\kappa)\min_{0<\eta_1\le\eta_0}\max\{1/K(w_1,\theta),1/(K(w_0,\theta)-C(\eta_1))\}$. — *Role:* Master bound; the new parameter eta_1 retains some of the error term to gain a better constant.
- **THM-PAPER-0038-L2** (Table 5 / F_16; Sec 3, Table 5 in Sec 6). Explicit degree-16 nonnegative even trigonometric polynomial with a_k>=0, a_1>a_0, nonnegativity guaranteed by the construction method. — *Role:* Main source of the improvement (together with the error-term saving, about 93.6% of the improvement; remaining 6.4% from larger T_0).
- **THM-PAPER-0038-L3** (Sec 6 fit; Sec 6). Empirical: the attainable constant is well approximated by $R_0=5.4912+2.0185/\log T_0$, suggesting limited further gain from larger T_0. — *Role:* Heuristic fitted trend (not a theorem).

### Proof architecture

Suppose a zero beta_0+i gamma_0 lies just outside the established region. Use a nonnegative trig polynomial f_n in the Mertens-type argument 3+4cos+cos2 generalization, with Kadiri's explicit formula for log-derivative of zeta applied at points n gamma_0 shifted, test function h_theta, and a lower bound K(w,theta) on the main term with an error term C(eta)=C_1+...+C_4 and delta/kappa parameters. This yields a bound on R_0. Iterate (with r<R_0<R shrinking) until the numerical fixed point is reached. Parameters: T_0=3.06e10, t_0=1e5, theta=1.85573, r=5, R=5.7 start, tolerance Delta=1e-6, outer improvement v=5e-7; convergence in about seven rounds to 5.5734118005.

Dependency edges: CAND-01216 → Kadiri 2005 (R_0=5.69693) (improves); CAND-01216 → Platt/other RH verification to 3.06e10 (uses as input); CAND-01216 → Arestov-Kondratev 1990 (V bounds) (improves upper bound of)

**Imported results.** Kadiri, Acta Arith. 117 (2005) 303-339 (the method and inequality (2.2)); RH verified to height 3.06e10 (ref [10]); Arestov-Kondratev (1990): 34.468305<V<34.5035864 (lower bound used in Theorem 2); Ford (2002) explicit Vinogradov-Korobov region; theta(t)<t for t<1.39e17 (ref [11]); Trudgian's earlier work [19] for conversion to log|t/17| form

**Techniques.** Nonnegative trigonometric polynomials (de la Vallee Poussin type argument); Kadiri's explicit method for zero-free regions; Simulated annealing for polynomial search; Explicit error-term bookkeeping; Landau's extremal quantity V_n

## Context and interpretation

**Importance and obstacle overcome.** Gives the best explicit classical zero-free region for medium heights, which feeds explicit prime number theorem bounds. The obstacle is that the polynomial search is a hard optimization problem whose surrogate (Landau V_n) is not the true objective; the authors note that better V_n does not always give better R_0 (best at n=12 in Table 4, with R_0<5.57422 after local tuning).

**Relation to prior work.** Same framework as Kadiri; new element is a polynomial of degree 16 (and exploration up to degree 40 for V), error term analysis with a new parameter eta_1, and T_0 updated from 3.33e9 to 3.06e10. R_0 improves from 5.69693 to 5.573412.

**Limitations and open questions.** Region is the classical form (not Vinogradov-Korobov) and is the best only for 3.06e10<|t|<exp(10151.5). The fit R_0~5.4912+2.0185/log T_0 suggests the method is near its limit. Whether a better surrogate than V_n exists is open. The proof is computer-assisted with floating-point parameters.

**Ideas in remarks/appendices/abandoned paths.** Sec 6 fitted formula R_0=5.4912+2.0185/log T_0 and remark about the equivalent form sigma>=1-1/(R log(t/B)); Sec 7 remarks on updating Faber-Kadiri and Ramare.

## Research potential

- **Hypotheses that might be weakened.** The input T_0=3.06e10 could be updated to the current RH verification height (Platt-Trudgian ~3e12), which by the fitted law moves R_0 only slightly (about 5.49+2.02/log T_0).
- **Generalizations.** Apply the same method to Dirichlet L-functions and Dedekind zeta functions (explicit zero-free regions) with the new trig polynomials.
- **Candidate connections.** Optimize directly against the Kadiri objective R_0(f_n) instead of Landau's surrogate V_n; explicit form sigma>=1-1/(R log(t/B)) (Sec 7 remark) for B>1 would improve Corollaries 1-2.
- **Reusable lemmas.** Coefficient tables for F_16, F_40; the framework of the min-max over eta_1 in (3.1).
- **Possible experiments.** Re-run the Table 3 iteration with exact (interval) arithmetic to certify the 5.573412 claim; direct simulated annealing on the R_0 objective at n=12.
- **Risks / barriers.** This is not a statement about RH. The classical region shrinks to the 1-line as t->infinity; the method cannot approach sigma=1/2.

## Audit notes (Level 1 reader)

Reliance on floating-point computation of R_0 with convergence tolerance 1e-6 and a binary search on eta_1 with tolerance 1e-3; the paper does not state interval/rounding-controlled arithmetic (rounding contract), so Theorem 1 as stated is a computational result with an unaudited arithmetic class. Table 4 R_0 values are not monotone in n (n=12 best), consistent with the remark in the text. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01216`; harvest queries: kw_zero_free, msc_11M26, msc_11Y35, arxiv_zero_free.
- Triage decision: include — Best explicit zero-free region in a large intermediate range.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
