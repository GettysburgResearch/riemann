# PAPER-0152 — Über zwei Arten von Faktorenfolgen in der Theorie der algebraischen Gleichungen.

| Field | Value |
|---|---|
| Authors | Pólya, G.; Schur, I. |
| Year / stratum | 1914 / S2 |
| Venue | J. Reine Angew. Math. 144, 89-113 (1914). |
| Identifiers | zbMATH [45.0176.01](https://zbmath.org/?q=an:45.0176.01) |
| MSC | 30C15, 26C10 |
| Families | C, F |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://gdz.sub.uni-goettingen.de/id/PPN243919689_0144 (page OCR via https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0144/00000093 to 00000118; Crelle 144, pp. 89-113) |
| Selection | score 2.0381, in-pool citations 17, seed lists 2, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Characterize real sequences (gamma_k) acting on real polynomials by $\sum a_kx^k\mapsto\sum\gamma_ka_kx^k$ that preserve real-rootedness ('Faktorenfolgen'): of the first kind (preserve real-rootedness of all real-rooted polynomials), and of the second kind (preserve real-rootedness when the input is real-rooted with all roots of the same sign). Link these to entire functions of genus 0 and 1 with real zeros.

**Historical motivation.** Laguerre's multiplier sequences (e.g. q^{k^2}) preserve real-rootedness; Polya and Schur turn this into a complete characterization linking to the structure of entire functions of genus 0 and 1, the setting in which the Riemann xi function's real-zero (RH) question is formulated.

### Main results

- **THM-PAPER-0152-1** (Definitions (introduction, p. 89-90), definition, scope: finite; Introduction, eqs (1)-(3)). A real sequence $(\alpha_k)_{k\ge0}$ is a Faktorenfolge of the first kind if for every polynomial $\sum_{k\le n}a_kx^k$ with only real roots, $\sum_{k\le n}\alpha_ka_kx^k$ has only real roots. A sequence $(\beta_k)$ is of the second kind (as written in the paper's terminology: sequences such that the transformation preserves real-rootedness) when it does so for polynomials with all real roots of the same sign (positive-root-only class, the paper states it with the weaker hypothesis on the input and conclusion 'no imaginary root'). Constants count as real-rooted polynomials. Examples attributed to Laguerre: $1,q,q^4,q^9,\dots$ ($|q|\le1$ in the paper's notation for the squares-exponent sequence) are of the first kind; $\cos\vartheta,\cos(\vartheta+\delta),\cos(\vartheta+2\delta),\dots$ are of the second kind. First kind implies second kind; the converse fails (e.g. the cosine sequence unless $\delta$ is a multiple of $\pi$).
- **THM-PAPER-0152-2** (Sec. 3, Satz I (algebraic criterion), theorem, scope: global; Sec. 3, Satz I (p. 100-101)). A real sequence $(\alpha_k)_{k\ge0}$ is a Faktorenfolge of the first kind iff for every $n\ge1$ the polynomial $\sum_{k=0}^n\binom nk\alpha_kx^k$ has only real roots, all of the same sign. [Paper's formulation: 'dann und nur dann ... wenn alle Gleichungen (11.) $\alpha_0+\binom n1\alpha_1x+\dots+\alpha_nx^n=0$ lauter reelle Wurzeln von gleichem Vorzeichen besitzen'.]
- **THM-PAPER-0152-3** (Sec. 3, Satz II, theorem, scope: global; Sec. 3, Satz II). A real sequence $(\beta_k)$ is a Faktorenfolge of the second kind iff for all $n$ the polynomial $\sum_{k=0}^n\binom nk\beta_kx^k$ has only real roots (eq. 12).
- **THM-PAPER-0152-4** (Sec. 4, Satz I (transcendental criterion), the 'Polya-Schur theorem', theorem, scope: global; Sec. 4 (Satz I and II, p. 102-105); definitions of Types I, II in Sec. 2, formulas (I.), (II.)). A real sequence $(\alpha_k)$ is a Faktorenfolge of the first kind iff the power series $\Phi(x)=\sum_{k\ge0}\alpha_k x^k/k!$ converges everywhere and is an entire function of type I, i.e. $\Phi(x)=Cx^me^{\gamma x}\prod_\nu(1+r_\nu x)$ (or with $x\to-x$) with $\gamma\ge0$, $r_\nu\ge0$, $\sum r_\nu<\infty$ (all zeros real and of one sign). Analogously for the second kind: iff $\Phi(x)=\sum\beta_kx^k/k!$ is entire of type II: $\Phi(x)=Cx^me^{-\gamma x^2+\delta x}\prod(1+\delta_\nu x)e^{-\delta_\nu x}$ with $\gamma\ge0$, $\delta_\nu$ real, $\sum\delta_\nu^2<\infty$ (Laguerre-Polya class).
- **THM-PAPER-0152-5** (Sec. 2, Satz I and Satz II, theorem, scope: global; Sec. 2, Satz I-II (pp. 94-98, proof of II to p. 100)). A power series with real coefficients is an entire function of type I (resp. type II) iff it is the uniform limit on some disc $|x|<\rho$ of real polynomials with only real zeros of one sign (resp. only real zeros). In particular, uniform limits on compact sets (even on a small disc) of real-rooted polynomials are in the Laguerre-Polya class (this was known to Laguerre in the same-sign case; the authors give the first proofs with convergence on a mere disc).
- **THM-PAPER-0152-6** (Sec. 1 (elementary properties), Satz I-IV, elementary properties, scope: global; Sec. 1, pp. 94-97). (I) In a first-kind sequence the nonzero terms form a single contiguous block with either all sign changes or all sign persistences. (II) In a second-kind sequence, if two adjacent terms vanish then all earlier or all later terms vanish; an isolated zero has neighbors of opposite sign. (III) For both kinds: $\alpha_\nu^2\ge\alpha_{\nu-1}\alpha_{\nu+1}$-type (Turan-type log-concavity inequality) (statement partially garbled in OCR). (IV) Composition (termwise product) of two first-kind sequences is first-kind; first-kind composed with second-kind is second-kind (this uses Schur's Kompositionssatz from the companion paper 'A.', Crelle 144, pp. 75-88).
- **THM-PAPER-0152-7** (Sec. 6, Satz I-III (applications), corollaries, scope: global; Sec. 6, pp. 108-113). If $\Phi$ is entire of type I (resp. II), so is $\Phi'$ (known, via Laguerre); applications to functions of genus 0 and 1; (III) an entire function of the second kind whose nonzero Taylor coefficients are all positive is of the first kind, of the form $e^{\gamma x}\prod(1+r_\nu x)$ with $r_\nu\ge0$.

### Key definitions

- Faktorenfolge erster/zweiter Art (multiplier sequence of the first/second kind)
- Type I function: Cx^m e^{gamma x} prod(1+r x), r>=0, sum r<infinity
- Type II function: Cx^m e^{-gamma x^2+delta x} prod(1+delta_nu x)e^{-delta_nu x}, sum delta_nu^2<infinity (Laguerre-Polya class)

### Principal lemmas

- **THM-PAPER-0152-L1** (Schur's Kompositionssatz (companion paper 'A.', imported); Schur, A., Crelle 144, 75-88). If $f(x)=\sum_{k\le n}a_kx^k$ has only real zeros of one sign and $g(x)=\sum b_kx^k$ has only real zeros, then the Hadamard-type composition $\sum a_kb_k x^k$ has only real zeros (precise hypotheses as in A.; not read by me). — *Role:* Engine of Sec. 1 Satz IV and of the sufficiency direction of Sec. 3
- **THM-PAPER-0152-L2** (Sec. 3, Satz I proof; Sec. 3, pp. 100-101 (proof partly read)). Sufficiency proceeds from Sum binom(n,k) alpha_k x^k real-rooted for all n, plus Satz V of Sec. 1 and the Laguerre theorem that uniform limits of real-rooted polynomials are real-rooted entire functions, to deduce real-rootedness of the transformed polynomial. — *Role:* Reduction of the multiplier property to a condition on the binomial transforms

### Proof architecture

Necessity direction: take the real-rooted polynomial (1+x)^n; the transformed polynomial is sum binom(n,k) alpha_k x^k, hence real-rooted (same-sign by Sec 1 Satz I). Sufficiency (Sec. 3): by Schur's composition theorem and a limit process, real-rootedness of all binomial transforms yields a first-kind sequence. Sec. 4 passes to entire functions: sum binom(n,k) alpha_k (x/n)^k -> sum alpha_k x^k/k! uniformly on discs, so by Sec. 2 (Laguerre-Polya theorem, with uniform convergence on a disc sufficing) the limit is of Type I; conversely approximate a Type I function by polynomials with real zeros of the same sign. Sec. 6 uses the equivalence to rederive and extend classical facts on entire functions of genus 0 and 1.

Dependency edges: CAND-00276 → Schur composition theorem (Crelle 144, 75-88) (depends on); CAND-00276 → CAND-00293 (Polya 1926 xi representation) (supplies Laguerre-Polya class / real-zero preservation tools used for xi); CAND-00276 → de Bruijn 1950 and Newman 1976 (Lambda constant) (later developments using heat-flow / Fourier transforms in the Laguerre-Polya class)

**Imported results.** Schur, Kompositionssatz, Crelle 144 (1914), 75-88 (companion paper A.); Laguerre, Oeuvres vol. I pp. 31-35, 199-206 (examples; limit of real-rooted polynomials); Biehler theorem on zeros of derived polynomials; Borel for entire function genus statements; Jensen

**Techniques.** composition (Hadamard-product-type) theorems for polynomials with real roots; limits of real-rooted polynomials and Laguerre-Polya class; binomial-transform criteria; Turan-type inequalities for coefficients; equivalence between algebraic (polynomial) and transcendental (entire function) criteria

## Context and interpretation

**Importance and obstacle overcome.** Complete classification of multiplier sequences, which gives the Laguerre-Polya class its algebraic characterization. For RH: the xi function in the variable t is RH iff Xi is in the Laguerre-Polya class; this paper gives the polynomial/approximation tools (uniform limits of real-rooted polynomials, multiplier sequences) used in the de Bruijn-Newman and Jensen-polynomial program. Obstacle: obtaining a necessary-and-sufficient test (not just examples); overcome with the binomial transform plus Schur composition.

**Relation to prior work.** Systematizes Laguerre's examples; builds on Schur's composition theorem; adds new proofs that uniform convergence on a disc suffices for the limit of real-rooted polynomials to be Laguerre-Polya.

**Limitations and open questions.** Characterization holds for sequences acting on the monomial basis; it does not give a test for a specific entire function (e.g. Xi) to be in LP, apart from the Jensen-polynomial route (binomial transform of Taylor coefficients). Later literature (Craven-Csordas) extends to other bases. Not discussed in the paper: RH.

## Research potential

- **Hypotheses that might be weakened.** Type II requires only real zeros with sum delta_nu^2 < infinity; the key RH-relevant hypothesis is that the Taylor coefficients of Xi(sqrt(z)) satisfy the Jensen-polynomial real-rootedness of all degrees and shifts (Polya's criterion). Weaken: asymptotic hyperbolicity of Jensen polynomials (Griffin-Ono-Rolen-Zagier) establishes only local/fixed degree results.
- **Generalizations.** Replace monomial basis by Hermite basis (Craven-Csordas), or add sign conditions for the second-kind classification; apply the binomial-transform criterion to the Taylor coefficients of Xi: RH iff for all n and shifts d the Jensen polynomials J^{d,n} are real-rooted (a statement derived from the Sec. 3 criterion).
- **Candidate connections.** Combine with Newman's Lambda: multiplier sequences exp(-lambda k^2) (Laguerre example q^{k^2}) preserve real-rootedness, which is exactly the heat-flow monotonicity; check that H_t for t>=0 is obtained by composing with the first-kind sequence e^{-t k^2} in Taylor-coefficient space of the Fourier transform, a clean algebraic derivation of 'Lambda>=0 monotone direction'.
- **Reusable lemmas.** Sec. 2 Satz I/II (uniform limits on a disc of real-rooted polynomials) is the standard closure lemma for the Laguerre-Polya class in RH work.
- **Possible experiments.** Compute binomial transforms of the Taylor coefficients of Xi (or of Phi(u) moments) at high precision and test real-rootedness for n up to 100 with certified root isolation; classify which sequences arising from Xi Taylor/moment coefficients lie in first versus second kind.
- **Risks / barriers.** Finite checks of Jensen polynomials give no information about RH globally; the criterion needs all n.

## Audit notes (Level 1 reader)

OCR garbles formula details (e.g. Sec. 1 Satz III inequality, exact normalization 'first/second kind' in the introduction); I did not verify the statement of the Sec. 4 Type II representation against a clean copy. The paper's definition of second kind is quoted with a hypothesis on input (roots of one sign) that is also how the criterion (12) is stated; whether the literal paper convention (input same-sign, conclusion real) matches the commonly cited 'multiplier sequence of the second kind' needs re-checking in the facsimile. The headline modern Polya-Schur statement (multiplier sequence iff Laguerre-Polya generating function) is in Sec. 4 Satz I-II as read. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00276`; harvest queries: citation_expansion.
- Triage decision: include — Polya-Schur multiplier sequences; basis for Laguerre-Polya theory.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
