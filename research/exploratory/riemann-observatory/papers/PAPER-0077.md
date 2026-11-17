# PAPER-0077 — On Riemann's study ``Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse''. (On the number of primes less than a given bound.)

*Original title:* Zu Riemann's Abhandlung ``Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse''.

| Field | Value |
|---|---|
| Authors | von Mangoldt, H. |
| Year / stratum | 1895 / S1 |
| Venue | J. für Math. CXIV, 255-305 (1895). |
| Identifiers | zbMATH [26.0215.03](https://zbmath.org/?q=an:26.0215.03) |
| MSC | 11M06, 11M26, 11N05 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://gdz.sub.uni-goettingen.de/id/PPN243919689_0114 (GDZ OCR of J. reine angew. Math. 114 (1895), images 261-311 = pp. 255-305, fetched via gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0114/<image>; EuDML record eudml.org/doc/148949) |
| Selection | score 4.4537, in-pool citations 23, seed lists 0, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Using Hadamard's 1893 product representation of xi, (1) make Riemann's 1859 asymptotic formula for the number N of zeros with real part (in Riemann's xi(t) normalisation) between 0 and h rigorous with an explicit error bound, and (2) prove convergence (with Riemann's ordering) of the infinite series \sum_{\nu}\{li(x^{\rho})\} and thus justify the analytic expressions for the prime-power counting function; asks whether Riemann's other assertions (all zeros real) hold, left open.

**Historical motivation.** After 34 years of no rigorous progress on Riemann's 1859 memoir ('zum ersten mal seit beinahe 34 Jahren ein wirklicher Fortschritt'), Hadamard's 1893 result made a rigorous treatment possible; von Mangoldt announced results in the Berlin Academy Sitzungsberichte of 19 July 1894. Piltz's 1884 Habilitationsschrift (pp.33-36,42-43) contained partial ideas on the convergence argument, acknowledged on p.257.

### Main results

- **THM-PAPER-0077-1** (Introduction: zero-counting theorem (Endergebniss), theorem, scope: global; Introduction p.256; proved in Part I (pp.257-280), eq.(2)-(4),(17)-(18), numerics p.264 (h=12, h<=53 bounds)). Let \xi(t) be Riemann's function with zeros \alpha_\nu (Re > 0 normalisation; zeros of the t-variable). For real h>0 let N(h) be the number of zeros with real part in (0,h]. Then N(h)=0 for h \le 12, and for h>12 \left| N(h)-\Big(\frac{h}{2\pi}\log\frac{h}{2\pi}-\frac{h}{2\pi}\Big)\right| < 0.34\,\log h\,+\,2.58 (the constants and exact form read from OCR: '0,34 l h + 2,58'; the main term is Riemann's h/2\pi\cdot\log(h/2\pi) - h/2\pi).
- **THM-PAPER-0077-2** (Part I, density corollary, corollary, scope: asymptotic; p.277 (after eq.(20)-(21))). If k=k(h)\to\infty with k of higher order than \log h and lower order than h, the number of zeros with real part between h and h+k is k\,\frac{1}{2\pi}\log\frac{h}{2\pi}+o(k); so the density of zeros at height h grows like \frac1{2\pi}\log\frac h{2\pi}.
- **THM-PAPER-0077-3** (Part I, first-root remark, theorem, scope: finite; Part I pp.264-266, p.277). \xi(t)=0 has at least one root whose real part lies in (0,53]; all roots have real part (absolute) greater than 12. (Shown by the numerical evaluation of the argument-increase \Phi from the Riemann-Siegel-type formula for \xi.)
- **THM-PAPER-0077-4** (Part I, product theorem (eq.(1)), theorem, scope: global; p.258). \xi(t)=\xi(0)\prod_{\nu}(1-t^2/\alpha_\nu^2), the product converging unconditionally, restated from Hadamard 1893 Part III with zeros counted by multiplicity and ordered by non-decreasing real part. (imported, not new.) *Conditional on:* Hadamard 1893 (imported).
- **THM-PAPER-0077-5** (Part II: convergence theorem, theorem, scope: global; Part II, p.285 (theorem on ordering and convergence), proof pp.285-292). For the zeros \alpha_\nu of \xi ordered by non-decreasing real part, the series \sum_\nu \frac{1}{\alpha_\nu}\,W_\nu(x,r) (the terms of the analytic expression of the weighted prime-power function f(x,r)=\sum_{p^m\le x}\ldots L(n)\,n^{-r}-type) converges for every real r and all real positive x, and for x>1 its sum is given by the explicit expression with the contributions \frac{x^{1-r}}{r-1}, \sum_n\frac{x^{-2n-r}}{2n(r+2n)} and the Euler constant (eq.(46)-(55); formula p.285 'Satz').
- **THM-PAPER-0077-6** (Part II, Riemann's series corollary, corollary, scope: global; Introduction pp.256-257; p.292). The infinite series \sum_\rho\{ li(x^{\rho})+li(x^{1-\rho})\} in Riemann's memoir converges with the arrangement indicated by Riemann (zeros ordered by absolute imaginary part) and has the sum Riemann stated; so Riemann's assertions are confirmed in all essentials. (stated in the introduction p.256 and consequence of p.292 Satz.)
- **THM-PAPER-0077-7** (Closing remarks (p.304), remark, scope: conditional; pp.304-305). If it were shown that all roots \alpha_\nu are real, or merely that Im \alpha_\nu lies in a strip narrower than (-i/2,+i/2), then asymptotic laws follow, e.g. \lim_{x\to\infty}\theta(x)/x=1 (sum of logs of primes up to x); the argument of Cahen for \theta(x)\sim x is rejected as not rigorous (existence of a rectangle with required properties not shown; would fail if zeros accumulated near Re s=1). Mangoldt notes this before Hadamard 1896/de la Vallee Poussin 1896 proved nonvanishing on Re s=1. *Conditional on:* narrower strip for zeros (not proved here).

### Key definitions

- \alpha_\nu: zeros of \xi(t) with positive real part, with multiplicity, ordered by non-decreasing real part
- L(n)=\log p if n=p^a, else 0 (von Mangoldt function, defined p.278)
- f(x,r): weighted prime-power function combining L(n)n^{-r} over n<=x (exact definition at p.278, OCR unclear)
- Abweichung (argument/deviation) of a function along a path: increase of the argument

### Principal lemmas

- **THM-PAPER-0077-L1** (Part I, inequalities (2)-(4) (argument principle by angles); pp.258-260). Move t along the segment a-i\eta to b-i\eta (all zeros lie in the Riemann strip |Im t|<1/2); each zero seen from t rotates positively, hence for the sum S of the angles subtending the path from the zeros with real part in [a,b] one has S \le \Phi (\Phi = increase of the argument of \xi) and S \ge A\arctan(\cdot), giving upper bounds for the count A. — *Role:* Converts the argument increase of \xi (explicit via Stirling and the functional equation) into a count of zeros by a geometric positivity argument that does not need non-vanishing on the critical line
- **THM-PAPER-0077-L2** (Part I, eq.(5) onwards (bound for \Phi); pp.260-266). From the Gamma-factor representation \xi(t)=\Pi(\tfrac{s}{2}-1)(s-1)\pi^{-s/2}\zeta(s) and Stirling's formula, \Phi = h\log(h/2\pi)\cdot\tfrac12 - \ldots with explicit remainder bounds; the zeta part contributes a bounded argument along Re s=1+\delta by absolute convergence of the Euler product. — *Role:* Evaluates the main term and controls the error with explicit numerical constants
- **THM-PAPER-0077-L3** (Part I, sums over zeros: Satz 1)-3) (pp.267-272); pp.267-272). Counting lemmas bounding the number of zeros in sub-intervals and the sum \sum\arctan\frac{\cdot}{h-\beta_\nu}, used to bootstrap sharper bounds (Satz 1: no zero in a first sub-interval; Satz 2: upper bound on the number of zeros in the second; Satz 3 proved p.272). — *Role:* Iterative sharpening from O(h\log h) to the full asymptotic with explicit error
- **THM-PAPER-0077-L4** (Part II, Hulfssatz block (p.278-281); pp.278-285). Weighted Perron integral for the von Mangoldt function L(n): for a+r>1, x>1 define L(n)=\log p if n=p^a, else 0; integrate -\zeta'(s+r)/\zeta(s+r)\cdot x^{s}/s... over Re s=a, |Im s|\le h, then shift contours using the product formula to get the sum over zeros plus the 'trivial' terms \sum_n \frac{x^{-2n}}{2n(r+2n)}. — *Role:* Origin of the explicit formula for the weighted prime-power sum
- **THM-PAPER-0077-L5** (Part II, eq.(55)/(58); p.292-293, p.304). For r=1: \sum_\nu \frac{\sin(\alpha_\nu\log x)}{\alpha_\nu}\,(\ldots) converges for every x>0 when terms are ordered with growing index, and for x>1 equals an explicit elementary expression; eq.(58) yields \theta(x)/x\to1 under the conditional narrower-strip hypothesis. — *Role:* Connects the explicit formula with Riemann's trigonometric series

### Proof architecture

Section I (zero distribution): from Hadamard's product for xi and the functional equation, count zeros via argument principle by moving t along horizontal segments within the strip |Im|<1/2 and using that every zero subtends a positive angle; Stirling gives the argument increase with explicit constants; an iterative sharpening with Satz 1-3 yields the main term plus error 0.34 log h+2.58. Section II (series): the Perron-type integral for the weighted von Mangoldt sum f(x,r) is contour-shifted using xi's product and the Gamma-factor expansion; convergence of the zero-sum is proved by estimating partial sums with the counts from Section I (zeros per unit height ~ log h/2pi) and the oscillating integrals, giving convergence when ordering by non-decreasing real part and an explicit closed form. Imported: Hadamard's 1893 genus-zero product; Riemann's integral representations and functional equation; Stirling's formula. No assumption of the Riemann hypothesis; conclusion on theta(x)/x->1 is stated only as conditional on a zero-free region (later supplied by Hadamard and de la Vallee Poussin 1896).

Dependency edges: CAND-00004 → CAND-00019 (imports genus-zero product representation of xi); CAND-00001 → CAND-00004 (Hadamard 1896 cites von Mangoldt's zero counts for Sum 1/|alpha|^(1+eps) convergence and notes his own method avoids it); CAND-00004 → Piltz 1884 (partial anticipation acknowledged); CAND-00004 → Cahen 1893 (criticizes the proof of theta(x)~x as non-rigorous)

**Imported results.** Hadamard 1893: genus zero of xi and product representation (J. Math. Pures Appl. (4) 9, 171-215); Riemann 1859 integral representations and functional equation; Stirling formula; Riemann: all zeros of xi lie in the strip |Im t|<1/2 (proved by Riemann's representations as stated on p.258)

**Techniques.** Argument principle via positive angle subtended by zeros; Stirling formula with explicit constants; Perron-type contour integral for L(n)/n^s with parameter r; Euler-Maclaurin / absolute convergence of Euler product on Re s>1; Explicit numerics for finite checks (h=12, h<=53)

## Context and interpretation

**Importance and obstacle overcome.** First rigorous proof of Riemann's two main analytic claims about zeros: the asymptotic count N(T) ~ (T/2pi) log(T/2pi e) with explicit error O(log T), and the convergence and value of the explicit-formula series. Obstacle: absence of a product over zeros before Hadamard 1893 and the need to control conditionally convergent sums over zeros (ordering matters). Mangoldt's positivity-of-angles argument yields the zero count without any knowledge of where zeros sit within the strip, and the ordering-by-real-part theorem gives the convergence. Introduces the von Mangoldt function L(n) and the explicit-formula technology that underlies everything later (Landau 1908, prime number theorem with remainder, Weil's explicit formulas, Montgomery pair correlation).

**Relation to prior work.** Depends on Riemann 1859 (formulas, functional equation), Hadamard 1893 (product representation), Piltz 1884 (partial anticipation of convergence ideas), Cahen 1893 (rejected as non-rigorous at p.304), Hadamard's earlier remark (no. 36-37 of his memoir) that the zero count is of order h log h; Mangoldt determines the coefficient 1/2pi and the second term. A previous note by Jensen (C. R. 104, 1887) sketched a route to 'all zeros have real part greater than 6.561 (and 8.4)', consistent with the bound 12 here.

**Limitations and open questions.** The rigorous explicit formula (final closed forms for psi(x)) as usually quoted today is credited to this memoir, but from the part I read the proved results are the weighted-sum expressions f(x,r) (all real r) and the convergence theorem; the pure psi(x)=x-\sum_\rho x^\rho/\rho-... form is the case obtained from them, which I did not verify line by line. The paper does not prove that all zeros are real (explicitly 'bleibt unerledigt'), nor non-vanishing on Re s=1 (so theta(x)\sim x remains conditional here). The count N(h) is stated in Riemann's real-normalisation (zeros of \xi(t) with Re t>0, i.e. Re\alpha=\gamma); a literal reading gives the form given above but the OCR garbles the error term, so the 0.34/2.58 constants should be re-read from the scan.

**Ideas in remarks/appendices/abandoned paths.** The geometric positivity argument (angles subtended by zeros along a horizontal path) gives a lower bound for the zero counting function in terms of the argument increase, independent of any location hypothesis on zeros; it is a template for zero-counting in zero-free-strip-agnostic settings (zeta-like functions with only strip localisation). Also the remark p.304 that localisation of the imaginary parts of alpha_nu in a strip narrower than |Im|<1/2 would already give theta(x)~x is an early statement of the zero-free-region to prime-counting implication, in Riemann's xi(t) normalisation (Re s=1 zero-free is equivalent to Im alpha<1/2).

## Research potential

- **Hypotheses that might be weakened.** The positivity-of-angles lemma needs only that all zeros lie in the closed strip |Im t|<=1/2 (a localisation) and that the path avoids the strip; for L-functions and Selberg-class members the same lemma gives counts under the functional equation and strip localisation alone. The ordering hypothesis (non-decreasing real part) in the convergence theorem could be tested for weakening to pairing alpha and -alpha-bar.
- **Generalizations.** Same scheme gives explicit formulas with explicit error for Dirichlet L-functions (done later by Landau) and Dedekind zeta; for the Selberg class, generalised zero counts with degree d replace h/2pi log(h/2pi) by (d h/2pi)log(...) plus conductor terms.
- **Candidate connections.** Explicit-constant zero counting (Rosser, Trudgian, Platt-Trudgian) is the modern descendant of eq.(2)-(4); the explicit 0.34 log h+2.58 style bound could be compared with the Backlund bound 0.137 log T+0.443 loglog T+4.35 to track how much the original positivity method loses, informing computational RH verification (certified zero count). Connect the closing remark p.304 (narrow strip implies theta~x) to quantitative zero-free-region-to-error-term transfers.
- **Reusable lemmas.** The angle-sum lemma (S<=Phi, S>=A arctan) and its use to bound zero counts from argument increase.
- **Possible experiments.** Recompute N(h) and the true error h/(2pi)log(h/(2pi)) - h/(2pi) - N(h) for h up to 10^4 using verified zeros and compare to 0.34 log h + 2.58 to check the stated constants (decode them from the scan first); check the 'no zero with real part <=12' and 'a zero in (0,53]' statements (first zero at 14.134... in gamma, consistent).
- **Risks / barriers.** Conclusions here are consequences of the product plus functional equation; they cannot settle the position of zeros on the critical line, and the convergence ordering is delicate (conditional convergence). The memoir is partly rendered obsolete by Landau's simplifications, so value is historical plus ideas, not stronger statements.

## Audit notes (Level 1 reader)

OCR (GDZ Fraktur-era) mangles nearly all formulas, so the exact error constants (0.34, 2.58) and the exact forms of eq.(2)-(4), (46), (55) in the statements above are reconstructed and flagged, not verified; the paper's Crelle numbering is also self-consistent only up to OCR noise. Triage description 'Rigorous proof of Riemann's formula for the prime counting function and psi(x) as a sum over nontrivial zeros' is only partly supported by my reading: I verified the zero-counting theorem, the convergence theorem for the weighted series f(x,r), and the explicit statement in the introduction that Riemann's series sum_{rho}{li(x^rho)+...} converges to the stated value; I did not verify the pure psi(x) formula as a corollary. On p.304 von Mangoldt explicitly states that theta(x)/x->1 is NOT proved here (conditional on a narrower strip).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00004`; harvest queries: kw_RH_any, msc_11M06, msc_11M26, msc_11N05.
- Triage decision: include — Von Mangoldt's 1895 proof of Riemann's explicit formula for psi(x).
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
