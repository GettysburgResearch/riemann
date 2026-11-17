# PAPER-0078 — On Riemann's function \(\zeta(s)\) and the number of primes under a given bound.

*Original title:* Sur la fonction \(\zeta(s)\) de Riemann et le nombre des nombres premiers inférieurs à une limite donnée.

| Field | Value |
|---|---|
| Authors | de la Vallée-Poussin, Ch. J. |
| Year / stratum | 1899 / S1 |
| Venue | Belg. Mém. 59, 74 p. (1899). |
| Identifiers | zbMATH [30.0193.03](https://zbmath.org/?q=an:30.0193.03) |
| MSC | 11N05, 11M06, 11M26 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://archive.org/download/memoirescouronnesetautrinoc59/memoirescouronnesetautrinoc59_djvu.txt |
| Selection | score 4.4537, in-pool citations 23, seed lists 2, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Prove, for Riemann's zeta function, a quantitative zero-free region of the form 1-Re(rho) >= c/log(Im rho) near the line Re s=1 (with explicit constants), and use it together with von Mangoldt's explicit formula to obtain the prime number theorem with a remainder term, i.e. pi(x)=Li(x)+O(x e^{-c sqrt(log x)}). Explicit constants are tracked throughout (rho=0.03282..., later 0.034666..., eta=47.886).

**Historical motivation.** Following Hadamard's and the author's 1896 proofs that zeta has no zeros on Re s=1 (giving the PNT qualitatively), and von Mangoldt's 1895/1897 proof of Riemann's formula for pi(x), the question was to make the PNT quantitative. The memoir was submitted to the Belgian Academy in 1898 and reported on by Mansion; constants were recomputed before publication in 1899.

### Main results

- **THM-PAPER-0078-1** (No. 17 Theoreme (Chap. I), theorem, scope: global; Chap. I, n. 17 (pp. ~21-23 of the memoir)). The function \zeta(s) has no non-trivial zero \rho=\alpha+i\beta with \alpha\neq 1/2 unless |\beta|>28.558 (a preliminary, weak statement; the strategy is to rule out zeros near Re s=1 for large height). Wording of the source: zeta(s) has no imaginary root a+bi with a different from 1 [sic OCR; context is a zero-free region] unless |b| exceeds 28.558. The exact formulation could not be recovered from the garbled OCR.
- **THM-PAPER-0078-2** (No. 31 Theoreme (Chap. II, eq. (54)), theorem, scope: global; Chap. II, n. 31 (p. ~40)). For \beta>514 (later improved to \beta>105 in n. 78), every zero \rho=\alpha+i\beta of \zeta satisfies a bound of the form 1-\alpha \ge \rho_0/(\log\beta + \eta_0) with explicit constants \rho_0=0.03282\ldots, \eta_0=4.49737\ldots (garbled OCR: the displayed inequality reads like "\log \beta - 3.506" in the denominator; treat the exact shape of the denominator as unverified). This is the quantitative zero-free region c/\log t.
- **THM-PAPER-0078-3** (No. 78 Theoreme (note at end of memoir, n. 71-78), theorem, scope: global; n. 78 (pp. ~73-74)). Improved constants: for \beta>105 the same inequality holds with \rho_0=0.034666\ldots and \eta_0=47.886\ldots (the OCR reads "\rho = 0.034666..., \eta = 47.886 ... pour \beta > 105").
- **THM-PAPER-0078-4** (Chap. IV, n. 59 (psi/theta remainder), theorem, scope: asymptotic; Chap. IV, n. 59-61). For the Chebyshev-type function (the OCR text is the end of Chap. IV before Chap. V) the remainder r satisfies r\to 0 as x\to\infty, with order at least that of \sqrt{\rho\log x}\,e^{-\sqrt{\rho\log x}}, where \rho=0.03282\ldots, i.e. \psi(x)=x+O\big(x\,\sqrt{\log x}\,e^{-\sqrt{\rho\log x}}\big)-type relative error. The exact form of the displayed formula is garbled.
- **THM-PAPER-0078-5** (Chap. V theorem (n. 65 end), theorem, scope: asymptotic; Chap. V, n. 62-65). Let F(x)=\pi(x) denote the number of primes <x. Then F(x)=\mathrm{Li}(x)+O\!\big(x\,e^{-c\sqrt{\log x}}\big)-type: the error relative to Li(x) tends to zero at a rate at least that of \sqrt{\rho'\log x}\,e^{-\sqrt{\rho'\log x}}\cdot x (exact constant and form garbled). The proof transfers the result for f(x)=\sum_k \pi(x^{1/k})/k to F(x) via f(x)-F(x)=O(\sqrt x) (OCR: f(sqrt x)<sqrt x). Li(x) is the principal term of F(x).

### Principal lemmas

- **THM-PAPER-0078-L1** (Equation (3) (log-derivative identity); Chap. I-II, eq. (3), (25)). For Re s>1, \zeta'(s)/\zeta(s)=-\sum_p \log p/(p^s-1) and the Hadamard product representation / partial fractions of -\zeta'/\zeta in terms of zeros, used to extract real parts (Chap. I, eq. (3), (25)) — *Role:* Starting identity: taking real parts with s=u+it, u slightly above 1, turns the sum over zeros into a positive quantity; a trigonometric positivity (1+cos-type) argument then bounds Re rho from above.
- **THM-PAPER-0078-L2** (Chap. I, n. 5-16 (integral representation (7) and its real part); Chap. I, n. 6-16). Explicit evaluation of \Re\sum_\rho 1/(s-\rho) and of \Re\,\zeta'/\zeta in terms of Gamma-function terms with numerical constants (e.g. 0.046192). — *Role:* Quantitative upper bounds for the contribution of trivial factor and pole, giving inequality (24).
- **THM-PAPER-0078-L3** (Chap. II, n. 18-31 (inequality (25) onward); Chap. II, n. 22-31; parameters in n. 71). For u close to 1 from above and t>12 real, an inequality combining zeta'/zeta(u+it) and the zero sum with a trigonometric polynomial 1+cos kappa t, yielding the real part of rho bounded away from 1 by c/log beta. — *Role:* Core zero-free region mechanism (positivity of 3+4cos+cos2 in modern phrasing; the memoir uses a different, more elaborate auxiliary polynomial with parameters h, m).
- **THM-PAPER-0078-L4** (Chap. III, n. 33-43; Chap. III). Bounds for sums over zeros such as \sum_\rho 1/|\rho| and \sum_\rho 1/|\rho|^2 and tail sums over \beta>b, using von Mangoldt's zero counting (imported) and the Chap. II inequality. — *Role:* Controls the zero sum in the explicit formula of Chap. IV-V.
- **THM-PAPER-0078-L5** (Chap. V n. 62-65 (formula (9) for f(x)); Chap. V, n. 65). f(x)=\mathrm{Li}(x)-\sum_\rho(\ldots)+\text{(integrals)} with f(x)=\sum_k \pi(x^{1/k})/k, an Euler-Mascheroni-free explicit formula obtained by integrating the log-derivative identity. — *Role:* Turns the zero-free region estimates into an estimate for pi(x).

### Proof architecture

Two-part memoir. Part I (Chaps. I-II): starting from the Euler-product log-derivative and the Hadamard product/partial fractions of zeta'/zeta, take real parts at s=u+it with u->1+; bound the sum over zeros by positivity of a suitable trigonometric polynomial, getting first a crude statement (no zeros with real part differing from 1... only at heights >28.558, n.17), then an explicit inequality 1-Re(rho) >= rho0/(log beta+eta0) for beta large (n.31, n.78). Part II (Chaps. III-V): estimate sums over zeros using von Mangoldt's zero-density/counting results; plug into an explicit formula for f(x)=sum pi(x^{1/k})/k and for the Chebyshev function, optimise the truncation, and obtain remainder O(x*exp(-c sqrt(log x))). Imported: von Mangoldt's formula and zero counting N(T)~(T/2pi)log T (Crelle 114, 119); Hadamard product theorem; Euler formulae.

**Techniques.** real part of logarithmic derivative of zeta; trigonometric-polynomial positivity trick with extended parameters; Hadamard factorization / partial fractions over zeros; von Mangoldt explicit formula; explicit numerical constants; optimisation of truncation height to balance zero-sum and tail

## Context and interpretation

**Importance and obstacle overcome.** First published proof (simultaneously with Hadamard 1896) of the prime number theorem and the first quantitative zero-free region of type 1-sigma >= c/log t, giving the first prime number theorem with a remainder term better than any power of log x. Obstacle overcome: moving from the qualitative statement 'no zero on Re s=1' to a uniform lower bound for the distance 1-Re(rho) via explicit positivity/real-part estimates, and keeping all constants explicit so that remainder terms are effective.

**Relation to prior work.** Builds on Chebyshev (bounds), Riemann (1859), Hadamard (1893 product theorem), von Mangoldt (explicit formula and N(T)), the author's own 1896 Annales Soc. Sci. Bruxelles papers, and runs parallel to Hadamard (Bull. SMF 1896). Directly used by von Koch (Acta Math. 24, 1900/01), who cites it (pp. 60-61 of the memoir) for the explicit formula for f(x) and for the von Mangoldt-derived bound on sums over zeros.

**Limitations and open questions.** The zero-free region is only of width c/log t, which is not enough to say anything about Re rho=1/2. Remainder is exp(-c sqrt(log x)), far from the sqrt(x) log x conditional on RH (von Koch). Constants are explicit but tiny (rho0 about 0.035). Does not give a zero-free region at heights below 105 or 514, so small zeros are not treated.

## Research potential

- **Hypotheses that might be weakened.** The positivity trick uses 1+cos(kt) type polynomials with Re at u slightly above 1; replacing it by a general nonnegative trigonometric polynomial with the optimal degree is exactly the later 3+4cos+cos2 de la Vallee-Poussin argument; the memoir's explicit constants (rho0=0.034666) could be rerun with modern explicit bounds (Kadiri, Mossinghoff-Trudgian) as a computational test of how much of the 1899 argument is intrinsic.
- **Generalizations.** The mechanism (positive trig polynomial plus real part of log derivative) extends to Dirichlet L-functions and Dedekind zeta (Landau-Page); the Chap. II inequality is the prototype of zero-free regions for L-function families and for Rankin-Selberg convolutions.
- **Candidate connections.** With Koch (CAND-00002) it brackets the unconditional exp(-c sqrt(log x)) error versus conditional sqrt(x) log x error; relevant to any RH approach that needs an effective zero-free region as input (e.g. Robin-type inequalities with explicit prime-counting error, Lagarias-type equivalences).
- **Reusable lemmas.** Chap. II inequality (25) with parameters (h,m) in n. 71 and the explicit sums in Chap. III as an auditable explicit-constants lemma; Chap. V reduction from f(x) to F(x) via f(x)-F(x)=O(sqrt x).
- **Possible experiments.** Re-derive the memoir's constants rho0=0.03282 and 0.034666, eta0=47.886 symbolically (rational arithmetic) to verify the stated numbers; compute what zero-free constant the same auxiliary polynomial yields when the sum over small zeros is checked against Platt's zero lists.
- **Risks / barriers.** The method cannot approach Re s=1/2: any method of this type is limited to c/log t because the pole at s=1 and the Euler product only give positivity near Re s=1.

## Audit notes (Level 1 reader)

The OCR (Internet Archive djvu of the Belgian academy volume, Google-digitised) is badly garbled in formulas, so exact displayed inequalities (n.17, n.31, n.59, n.65, n.78) were not recoverable and are given in hedged form; do not cite the exact denominator shape from this record. The no. 17 theorem text as OCRed says 'a diffère de 1/2'[sic] in the OCR; the actual wording is probably 'a diffère de 1'. The footnote on n.78 notes a numerical error in the 5th decimal of rho in the manuscript submitted to Mansion. The triage description (pi(x)=Li(x)+O(x exp(-c sqrt(log x)))) is consistent with the intro/Chap. V statements as read, but the memoir states it as an order-of-smallness claim, not with the O-notation.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00005`; harvest queries: msc_11M06, msc_11M26, msc_11N05.
- Triage decision: include — De la Vallee Poussin 1899: first zero-free region and PNT with error term.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
