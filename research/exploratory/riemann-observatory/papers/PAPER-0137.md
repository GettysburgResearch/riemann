# PAPER-0137 — Study of the properties of entire functions and in particular of a function considered by Riemann.

*Original title:* Étude sur les propriétés des fonctions entières et en particulier d'une fonction considérée par Riemann.

| Field | Value |
|---|---|
| Authors | Hadamard, J. |
| Year / stratum | 1893 / S1 |
| Venue | Journ. de Math. (4) IX, 171-215 (1893). |
| Identifiers | zbMATH [25.0698.03](https://zbmath.org/?q=an:25.0698.03) |
| MSC | 30D99, 11M06 |
| Families | A, F |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://www.numdam.org/item/JMPA_1893_4_9__171_0.pdf |
| Selection | score 3.1841, in-pool citations 7, seed lists 3, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** How are the growth, the genus and the zero distribution of an entire function related to the decay of its Taylor coefficients, and does this give a rigorous proof that Riemann's entire function xi(x), regarded as a function of x^2, has genus zero (so that it equals a constant times a canonical product over its zeros with no exponential factor)?

**Historical motivation.** Poincare 1883 proved: finite genus implies coefficients decay like (m!)^{-1/lambda}; Hadamard completes with the converse; Riemann 1859 needed genus 0 of xi as a gap; Hadamard states he proceeds toward the question 'Riemann function' as an application in Part III. This is the first rigorous step toward the prime number theorem.

### Main results

- **THM-PAPER-0137-1** (Introduction goal (converse of Poincare), theorem, scope: global; Introduction p.172; conclusion of Part II no. 33 (as stated: 'la reciproque du theoreme de M. Poincare est donc bien etablie pour lambda non entier'); statement paraphrased from garbled OCR). If F(x)=\sum a_m x^m is entire and |a_m| \le (m!)^{-1/\lambda} (up to epsilon-adjusted form), then F has genus < \lambda in general; the doubtful case is \lambda = E+1 an integer, where genus can be E or E+1. Hadamard states: coefficient of x^m smaller than 1/(m!)^{1/\lambda}-type bound implies genus at most E, E+1 being the least integer exceeding \lambda.
- **THM-PAPER-0137-2** (Part I, no. 6 (growth from coefficients), theorem, scope: global; Part I, no. 6 (pp. ~176-179)). If |a_m| \le 1/e^{\varphi(m)} with \varphi increasing with m and \varphi(m)/m increasing (after regularising by a convex minorant), then for every \epsilon>0 the maximum modulus satisfies F(x) < A\,x^{\epsilon}e^{\psi(x)}-type bound where \psi is the inverse function of \varphi; i.e. coefficient decay controls growth. Exact displayed form of the bound could not be read in the OCR.
- **THM-PAPER-0137-3** (Part I, no. 9-11 (inverse direction), theorem, scope: global; Part I, no. 9 (p. ~178)). Conversely, from a growth law for F one recovers a coefficient-decay law via Poincare's auxiliary function \Phi(x)=\int_0^\infty e^{-t}F(tx)\,dt generalised to \Phi(x)=\int e^{-\Psi(t)}F(tx)\,dt for general positive increasing \Psi.
- **THM-PAPER-0137-4** (Part II, nos. 21-27 (zeros from coefficients), theorem, scope: asymptotic; Part II, nos. 21-27). Using the limsup determinants of Hadamard's 1892 'Essai sur l'etude des fonctions donnees par leur developpement de Taylor', the successive zeros of an entire function are expressed through its Taylor coefficients; under a regular decay a_m ~ 1/(m!)^{1/\lambda}-type hypothesis this gives the law of distribution of zeros.
- **THM-PAPER-0137-5** (Part II, no. 18, theorem, scope: global; Part II, no. 18). Picard's theorem (an entire function omits at most one value) is re-derived for all entire functions satisfying the coefficient condition (8), hence for all functions of finite genus.
- **THM-PAPER-0137-6** (Part III, no. 33 (examples), corollary, scope: global; Part II no. 33). \sin(\pi x)/(\pi x)=\prod(1-x^2/n^2) with no exponential factor follows from genus zero of the function of x^2 deduced from the Taylor development (a proof that avoids the special argument needed after Weierstrass).
- **THM-PAPER-0137-7** (Part III, no. 37 (final proposition), theorem, scope: global; Part III, nos. 34-38 (pp. 210-215); concluding proposition 'La fonction xi(x) (consideree comme fonction de x^2) est de genre zero'). Let \xi(x)=\tfrac12\int ... (Riemann's entire function, defined via \Psi(t)=\sum_{n\ge1}e^{-n^2\pi t}, \xi(x)=\int_1^\infty \Psi(t)\,t^{-3/4}\cos(\tfrac x2\log t)\,dt-type formula (45)-(46)). Considered as a function of x^2, \xi has genus zero; hence \xi(x)=\xi(0)\prod_\alpha(1-x^2/\alpha^2) with no exponential factor. Derived from the coefficient bound of the Taylor expansion in x^2 (condition (8) with exponent \alpha=2-\epsilon, hence \lambda=\tfrac12+\epsilon) combined with the converse-Poincare result.

### Key definitions

- Genus of an entire function: F=e^{Q}\prod E_p(x/a_n) with Q polynomial of degree <= E and all primary factors of degree E
- limsup of sequence 'limite superieure' used as regularity notion; 'tend regulierement'
- Condition (8): coefficient bound |a_m| <= (m!)^{-1/\lambda} type with regular decay
- xi(x): Riemann's function of x^2 defined via integral (45)-(46)

### Principal lemmas

- **THM-PAPER-0137-L1** (no. 6-8 (convex envelope); nos. 5-8). For a coefficient bound |a_m|<=e^{-\varphi(m)}, one may replace \varphi by a function with \varphi(m)/m increasing; for such \varphi, b_{m_0}=m_0(m_0+1)[\varphi(m_0+1)-\varphi(m_0)]-\ldots is increasing and unbounded, and \varphi(m)\ge m^{\lambda'} type growth for any \lambda'>1 slightly above 1 in the relevant normalisation. — *Role:* Regularisation step so that the maximum-term argument of no. 6 applies
- **THM-PAPER-0137-L2** (no. 12-15 (exp(G(x)) functions); nos. 12-15). For F=e^{G(x)} with G entire, |F| is controlled by Re G; coefficient formula a_m=\frac1{\pi R^m}\int_0^{2\pi}P(Re^{i\theta})\cos m\theta\,d\theta for the real part P of an entire function; if P grows at most polynomially then G is a polynomial of bounded degree. — *Role:* Shows the exponential factor in the Weierstrass product has degree <= E, i.e. G polynomial of degree at most the genus; key to ruling out exp factor
- **THM-PAPER-0137-L3** (nos. 28-29 (determination of genus); nos. 28-33). For F with coefficients of order (m!)^{-1/\lambda}, \lambda not an integer, applying the e^{G} analysis to the associated auxiliary function shows G is a polynomial of degree at most E, so F is of genus E, where E+1 is the least integer exceeding \lambda. — *Role:* Delivers the converse of Poincare's theorem (genus vs coefficient decay) in the non-integer case
- **THM-PAPER-0137-L4** (no. 36 (reduction of Psi); nos. 35-36). In the series for \xi in x^2 one may replace \Psi(t) by its first term e^{-\pi t}, drop the factor t^{-3/4}, and observes \log t < \epsilon t^{\,\cdot} for large t, producing Taylor coefficients a_m of size below (m!)^{-(2-\epsilon)}-type in the variable x^2... (exponent reconstructed; OCR garbled). — *Role:* Computes the coefficient decay of xi needed for the genus argument

### Proof architecture

Part I establishes the direct and converse link between coefficient decay (a_m <= exp(-phi(m)) with phi(m)/m increasing) and growth of F via a maximum-term argument and the Poincare auxiliary function Phi. Part II studies F = e^{G(x)} by analysing the real part of an entire function through Fourier coefficients on circles, and uses the limsup/determinant formulas of the 1892 Essai to relate Taylor coefficients to zeros; this yields the converse of Poincare's theorem for non-integral lambda (no. 33) and Picard's theorem for finite genus. Part III is the application: Riemann's xi, written as an entire function of x^2 via the integral representation, has Taylor coefficients bounded by order (m!)^{-2+eps}, hence order less than 1 in x^2, hence genus 0 by Part II, which gives the canonical product without exponential factor. Imported: Weierstrass factorisation theorem, Poincare's 1883 theorem (genus finite implies coefficient decay), Riemann's integral representation of xi. This product is exactly what later feeds the explicit formula (von Mangoldt 1895) and Hadamard 1896/de la Vallee Poussin 1896.

Dependency edges: CAND-00019 → CAND-00004 (supplies genus-zero product (eq.(1)) used by von Mangoldt 1895); CAND-00019 → CAND-00001 (product representation and zero-distribution inputs cited by Hadamard 1896 (genus 1 of related functions, Sigma 1/|a|^{1+eps} convergence)); CAND-00019 → Riemann 1859 (fills the unproved genus claim for xi)

**Imported results.** Weierstrass factorization theorem; Poincare, Sur les fonctions entieres, Bull. SMF 11 (1883): finite genus gives decay of Taylor coefficients; Riemann 1859 integral representation of xi; Hadamard, Essai sur l'etude des fonctions donnees par leur developpement de Taylor, J. Math. Pures Appl. (4) 8 (1892)

**Techniques.** Maximum-term / Taylor coefficient estimates; Poincare auxiliary function Phi(x)=int e^{-t}F(tx)dt; Cauchy coefficient formula for real parts of entire functions; limsup determinant formulas for zeros (Hadamard 1892); Weierstrass canonical products; Regularisation by convex envelopes

## Context and interpretation

**Importance and obstacle overcome.** Riemann's 1859 memoir asserted without adequate proof that xi, as a function of x^2, has genus zero (infinite product over zeros) and that the number of zeros in |Im|<T is ~ T/2pi log T/2pi e; the product representation is the gate to the explicit formula and to the prime number theorem. The obstacle was that Weierstrass's theorem alone gives a product times e^{G(x)} with unknown entire G; Hadamard proved G constant by controlling order via Taylor coefficients. Introduces what is now called the Hadamard factorization theorem, which is the basis of every later zero-theoretic argument in RH (de Bruijn-Newman, Laguerre-Polya class, xi-geometry).

**Relation to prior work.** Builds on Weierstrass (canonical products), Poincare (1883, genus/coefficients, Picard theorem), Laguerre (genus theory) and Hadamard's own 1892 Essai (Taylor coefficients and zeros). Fills the gap in Riemann 1859 (genus of xi).

**Limitations and open questions.** The paper settles genus zero of xi(x) in x^2 and thus order <= 1 (in s). It does NOT prove Riemann's conjecture that all zeros are real (in the xi(t) normalisation), nor the asymptotic count of zeros (that is von Mangoldt 1895, using this paper), nor non-vanishing on Re s=1 (Hadamard 1896). The integer-lambda case of the Poincare converse is left open ('il y a doute'; genus E or E+1), as is the question whether genus is preserved under differentiation or linear combination (only: genus E to genus at most E+1 in general).

**Ideas in remarks/appendices/abandoned paths.** Part II no. 21-27: formulas for successive zeros from Taylor determinants (ratios of Hankel-like determinants of coefficients with limsup) could be revisited for xi using its explicit moment-type coefficients (Taylor/Hankel structure of the Riemann Xi coefficients, Polya Jensen polynomials). Not exploited in the paper itself.

## Research potential

- **Hypotheses that might be weakened.** The condition 'phi(m)/m increasing' (convex regularisation) and the integer-lambda gap: the paper cannot decide genus E vs E+1 when lambda is an integer; for xi, lambda=1/2 (non-integer) so no problem, but for xi-like Dirichlet series products with order exactly 1 in s the doubtful case would arise.
- **Generalizations.** The Taylor-coefficient-to-genus argument can be applied to the Xi-type functions attached to L-functions and Epstein/Selberg-class members (order 1 in s, order 1/2 in the square variable) and to Jensen-polynomial coefficient sequences (Polya, Griffin-Ono-Rolen-Zagier hyperbolicity of Jensen polynomials) where decay of Taylor coefficients of Xi at 0 is exactly Hadamard's input.
- **Candidate connections.** Link the limsup-determinant zero formulas (Part II, nos. 21-27) to Hankel/Turan-type determinant tests on the Taylor coefficients of Xi (Laguerre-Polya class characterisation by Turan inequalities).
- **Reusable lemmas.** Cauchy-coefficient formula for the real part of an entire function and the resulting 'G polynomial of degree <= E' lemma (nos. 12-15) is a clean reusable statement for exponential factors of canonical products.
- **Possible experiments.** Compute Taylor coefficients of Xi(sqrt(z)) to high precision, fit phi(m)=-log a_m, and verify numerically that a_m (m!)^{2-eps}... stays bounded as required by condition (8); compare the Hadamard determinant zero estimates with actual first zeros (14.134...) to see the quality of Part II.
- **Risks / barriers.** Genus zero / order <1 in x^2 carries no information about the real-ness of zeros; it is the first, not the last, hypothesis. A purely Taylor-coefficient route to RH would need Laguerre-Polya membership, which is equivalent to RH for Xi and not accessible from decay information alone.

## Audit notes (Level 1 reader)

OCR of the Numdam scan is heavily garbled, so exact exponents in the statements of nos. 6, 28-33, 36 could not be read reliably; the statements above are paraphrased and flagged. The paper counts two sections labelled 'no. 15' and several numbering duplications (e.g. 'no. 15' appears twice, '21' twice in OCR) which may be OCR artefacts or the original's typographic numbering. Hadamard himself flags the integer-lambda case as doubtful (no. 33). Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00019`; harvest queries: msc_11M06.
- Triage decision: include — Hadamard's factorization theory of entire functions applied to xi.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
