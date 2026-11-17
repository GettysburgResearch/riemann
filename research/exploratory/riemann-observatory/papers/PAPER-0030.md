# PAPER-0030 — On the distribution of primes.

*Original title:* Sur la distribution des nombres premiers.

| Field | Value |
|---|---|
| Authors | von Koch, H. |
| Year / stratum | 1900 / S1 |
| Venue | Acta Math. 24, 159-182 (1900). |
| Identifiers | zbMATH [31.0201.02](https://zbmath.org/?q=an:31.0201.02) · DOI [10.1007/BF02403071](https://doi.org/10.1007/BF02403071) |
| MSC | 11M26, 11N05 |
| Families | A, C |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://zenodo.org/api/records/2347595/files/article.pdf/content |
| Selection | score 4.5913, in-pool citations 37, seed lists 2, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Give an elementary route from Euler's product formula (using the discontinuity factor lim_{s->infty}(1-e^{-x s})... ) to explicit formulas for the Chebyshev function psi(x), Mangoldt's function and Riemann's f(x)=sum pi(x^{1/k})/k, and use it to prove rigorously the result foreseen by Riemann: assuming all non-trivial zeros have real part 1/2, pi(x)-Li(x) is O(x^{1/2+epsilon}), then sharpened in a note to O(sqrt(x) log x).

**Historical motivation.** Riemann (1859) asserted without proof that pi(x)-Li(x) is of lower order under RH; von Mangoldt proved Riemann's explicit formula rigorously in 1895 and de la Vallee-Poussin gave an explicit formula for f(x) in 1899. Koch (invited talk at ICM 1900) gave the first proof of the conditional error term, one of the first results linking RH to the size of the prime counting error.

### Main results

- **THM-PAPER-0030-1** (Theorem of section 7 (psi version), theorem, scope: asymptotic; Section 7, p. 179). Assume \mathrm{Re}\,\rho=1/2 for every non-trivial zero \rho of \zeta. Then \psi(x)-x\to \ldots, more precisely \psi(x)-x+\log 2\pi-\ldots is O(x^{1/2+\varepsilon}) for every \varepsilon>0: the difference tends to zero after dividing by x and is of order at most that of x^{1/2+\varepsilon}. (Printed statement: 'la difference psi(x)-x (+ log 2 pi ...) tend vers zero pour x=oo et cette difference est un infiniment petit d'un ordre de petitesse au moins egal a celui de x^{a}... a>1/2'.)
- **THM-PAPER-0030-2** (Theorem of section 7 (theta version), corollary, scope: asymptotic; Section 7, pp. 179-180). Under RH, \theta(x)-x = O(x^{1/2+\varepsilon}) for every \varepsilon>0 (since \psi(x)-\theta(x)=O(\sqrt x)); the difference \theta(x)/x\to 1 at a rate at least that of x^{-1/2+\varepsilon}.
- **THM-PAPER-0030-3** (Theorem of section 7 (final form, p. 181), theorem, scope: asymptotic; Section 7, p. 181). If every non-trivial zero has real part 1/2, then F(x)=\pi(x)=\mathrm{Li}(x)+\eta(x), where |\eta(x)|\le K_\varepsilon\,x^{1/2+\varepsilon} for every \varepsilon>0 (K_\varepsilon depends only on \varepsilon). Proof: combine the estimate for \psi (via the Mangoldt-de la Vallee-Poussin formula (57) for f(x)) with f(x)-F(x)=O(\sqrt x).
- **THM-PAPER-0030-4** (Note additionnelle, p. 182, theorem, scope: asymptotic; Note additionnelle, p. 182). Under RH: |\psi(x)-x|<B\,e^{2\sqrt{\ldots}}\ldots precisely |\psi(x)-x|<B\sqrt x(\log x)^2 for all x (OCR: 'B e^{2}(log x)^2 sqrt x'), and |f(x)-\mathrm{Li}(x)|<K\log x\,\sqrt x. Hence \pi(x)=\mathrm{Li}(x)+O(\sqrt x\,\log x) with an effectively computable constant. Proof uses von Mangoldt's estimate \sum_{\rho}|{\rho}|^{-1-a}-type bound (via de la Vallee-Poussin, loc. cit. p. 42) with optimal parameter a=2/\log x.
- **THM-PAPER-0030-5** (Formula (9) of section 1 / (14) of section 2 / (16), theorem, scope: global; Sections 1-2, eqs. (9), (14), (16)). New representations: f(x)=\frac12(\ldots)+\lim_{s\to\infty}\sum_{\nu\ge1}\frac{(-1)^{\nu-1}x^{\nu s}}{\nu}\log\zeta(\nu s) type formulae; \psi(x)=\omega-\lim_{s\to\infty}\sum_{\nu\ge1}(-1)^{\nu-1}x^{\nu s}Z(\nu s), with Z=\zeta'/\zeta, and the analogue for \Lambda(x,r)=\sum_{n\le x}n^{-r}L(n) (r real), valid for all real r. Here \omega=\log p if x=p^k, else 0 (the OCR reads e^{-1}\log p: half-weight convention at prime powers).

### Principal lemmas

- **THM-PAPER-0030-L1** (Section 1, eq. (A)-(6); Introduction eq. (A), Section 1). For x>0: \lim_{s\to\infty}(1-e^{-x s}\ldots)^{\ldots}=0 or 1 according as x<1 or x>1 (smooth step as discontinuity factor); this replaces Riemann's use of the Perron-type integral (B). — *Role:* Elementary device replacing contour integration; the whole paper rests on it to convert Euler's product identity into formulas for f(x), psi(x).
- **THM-PAPER-0030-L2** (Section 3 (recalled facts); Section 3, eqs. (17)-(20)). Hadamard's product: with H(s)=\xi-type entire function of order 1, \prod_{\mathrm{Im}\rho>0}(1-s/\rho)(1-s/\bar\rho) converges absolutely and represents H up to a constant; consequently \zeta'/\zeta(s) has the partial fraction expansion (20) over \rho and the trivial zeros -2n. — *Role:* Imported (Riemann, Hadamard 1893): needed to evaluate the series of section 4.
- **THM-PAPER-0030-L3** (Section 4, eqs. (24)-(35); Section 4). Define P(x,s,a)=\sum_{\nu\ge1}(-1)^{\nu-1}x^{\nu s}/(\nu s+a)\ldots; it is entire in x, meromorphic in a; P(x,s,a)=\ldots\int_0^x(1-e^{-y^s})y^{a-1}\,dy\ldots with explicit bounds, e.g. \int_0^x s y^{2n+s-1}e^{-y^s}dy<1-e^{-x^s}-x^s e^{-x^s}. — *Role:* Allows interchange of sums and yields absolutely convergent double series, giving the expansion (25) of \Psi(x,s) as main term plus sums over trivial and non-trivial zeros.
- **THM-PAPER-0030-L4** (Section 5, eqs. (44)-(46); Section 5). As s\to\infty, \sum_n s/(2n(s+2n))=O(\log s) and, if \mathrm{Re}\rho=1/2, \sum_\rho s/(\rho(s-\rho))=O(s^{\alpha}) for every \alpha>0 (in fact O(s^{1/2+\varepsilon})-type bound after using \sum|\rho|^{-1-\varepsilon}<\infty). — *Role:* Growth of the zero sums in the explicit formula with parameter s.
- **THM-PAPER-0030-L5** (Section 6, eqs. (47)-(50); Section 6). For x=n+1/2 and s>2x\log x (so s large), the difference between \Psi(x,s) and \psi(x) stays bounded and, for s=x^{2}, tends rapidly to 0: \Psi(x,s)=\psi(x)+\Delta with |\Delta|<\ldots (via Mertens's remark and S_2<x^s\sum\ldots). — *Role:* Passage from the s-regularised function \Psi(x,s) to the true Chebyshev function; this is where truncation s=x^{a}(x^{2}) enters.

### Proof architecture

1. Euler's formula log zeta(s)=sum p^{-s}+... rewritten with s->nu s and multiplied by (-1)^{nu-1}x^{nu s}/nu, summed over nu; letting s->infinity with the smooth discontinuity factor (1-e^{-x s...}) gives new formulae for f(x), psi(x), Lambda(x,r) as limits (sections 1-2). 2. Insert the Hadamard-product partial fraction expansion of zeta'/zeta (section 3) into the formula for the regularised psi (section 4), exchange sums, and bound the elementary function P(x,s,a) (eq. (26)-(35)). 3. Estimate series over trivial and non-trivial zeros as s->infty (section 5), using sum|rho|^{-1-eps}<infinity. 4. For x=n+1/2 compare the regularised and true psi (section 6) and choose s=x^{(1+eps)}-type; get psi(x)-x=O(x^{1/2+eps}) under RH (section 7). 5. Transfer to f(x) via de la Vallee-Poussin's formula (57) and to pi(x) via f(x)-F(x)=O(sqrt x). 6. Note: using von Mangoldt's bound on sum_rho |rho|^{-1-a}, optimise a=2/log x to get O(sqrt x log x) for pi(x)-Li(x). Imported: Riemann's formula and functional equation, Hadamard product, von Mangoldt zero counting, de la Vallee-Poussin (1899) formula for f(x).

**Techniques.** Euler product with regularising step function; exchange of absolutely convergent double sums; Hadamard product / partial fractions of zeta'/zeta; explicit formula without contour integration; truncation at s=x^a with optimisation in a; Mertens remark for comparing psi and theta

## Context and interpretation

**Importance and obstacle overcome.** First rigorous proof of Riemann's heuristic claim that under RH the error in the prime counting function is of order x^{1/2+eps} (sharpened to sqrt(x) log x), after von Mangoldt and de la Vallee-Poussin supplied explicit formulae. The conclusion is the classical conditional bound that, with the converse direction, yields the equivalence of RH with pi(x)=Li(x)+O(sqrt x log x). Obstacle overcome: justify interchange of limits and sums without Perron's formula by an elementary regularisation.

**Relation to prior work.** Follows Riemann (1859), Hadamard (1893, 1896), von Mangoldt (J. reine angew. Math. 114, 119), de la Vallee-Poussin (Mem. couronnes 1899, pp. 42, 60-61), Mertens (Crelle 78), Chebyshev's psi function; explicitly says it gives easier proofs than known ones; the added note takes bounds on sum |rho|^{-1-a} from de la Vallee-Poussin.

**Limitations and open questions.** The paper proves only RH => bound, i.e. one direction; the converse (bound => RH) is not in this paper. Only the one-sided statement with sqrt(x) log x in the added note. The constants are not computed explicitly (footnote: 'il serait facile d'assigner une valeur numerique'). The method, based on interchange of limits, loses factors compared with the later Perron-integral argument.

## Research potential

- **Hypotheses that might be weakened.** The only hypothesis is Re rho=1/2 entering through sum_rho |rho|^{-1-a} and the factor x^{rho}; assuming instead Re rho<=Theta with Theta in (1/2,1) gives pi(x)-Li(x)=O(x^{Theta}log x) (the same proof with |x^rho|<=x^Theta), the route to zero-density-based estimates. The regularising parameter s in P(x,s,a) could be optimised separately from the von Mangoldt-based optimisation a=2/log x.
- **Generalizations.** The factor (1-e^{-x s}) device and formulas (9),(14),(16) for Lambda(x,r)=sum_{n<=x} n^{-r}L(n) extend to Dirichlet series/L-functions; the formula valid for all real r gives a one-parameter family of explicit formulae (potential comparison with weighted prime sums used in Robin-type inequalities).
- **Candidate connections.** Combined with de la Vallee-Poussin 1899 (CAND-00005) it forms the pair (unconditional exp(-c sqrt log x), conditional sqrt x log x); with Littlewood 1914 (CAND-00161) it forms the pair (conditional upper bound, unconditional Omega-result) for pi(x)-Li(x); Lagarias-style Robin inequality equivalences use the same explicit formulas.
- **Reusable lemmas.** Section 4 bounds for P(x,s,a) and eq. (35) are self-contained explicit estimates that can be re-run with exact constants; Section 6 comparison psi vs. Psi at x=n+1/2.
- **Possible experiments.** Make Koch's constants explicit: implement P(x,s,a) and Psi(x,s) at s=x^2 and verify numerically that Psi(x,s)-psi(x)->0 for x=n+1/2 as claimed (eqs. (48)-(50)) and compare to the true psi.
- **Risks / barriers.** The method is inherently conditional on RH; the converse (obtaining RH from sqrt-type error) requires a Mellin/Landau argument not present here. No unconditional gain over de la Vallee-Poussin.

## Audit notes (Level 1 reader)

The triage statement 'RH is equivalent to pi(x)=Li(x)+O(sqrt(x) log x)' overstates this paper: only the implication RH => bound is proved here (the converse is classical but is not in this paper). The paper states that Riemann's assumption Re rho=1/2 is not yet proved (footnote p. 175 citing Jensen). The 'additional note' (p. 182) is added after the paper was in press and gives the sqrt(x) log x bound with only a sketch (relies on von Mangoldt via de la Vallee-Poussin p. 42). OCR scrambled displays (e.g. exponents in (55) and the form of the final remainder), so exact displayed constants are given as stated in the text rather than from displays.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00002`; harvest queries: msc_11M26, msc_11N05.
- Triage decision: include — Von Koch's 1901 theorem: RH is equivalent to the sharp error term in the PNT.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
