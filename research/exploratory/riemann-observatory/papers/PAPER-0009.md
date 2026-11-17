# PAPER-0009 — On the distribution of zeros of the function \(\zeta(s)\) and its arithmetical consequences

*Original title:* Sur la distribution des zéros de la fonction \(\zeta(s)\) et ses conséquences arithmétiques.

| Field | Value |
|---|---|
| Authors | Hadamard, J. |
| Year / stratum | 1896 / S1 |
| Venue | Bull. Soc. Math. Fr. 24, 199-220 (1896). |
| Identifiers | zbMATH [27.0154.01](https://zbmath.org/?q=an:27.0154.01) · DOI [10.24033/bsmf.545](https://doi.org/10.24033/bsmf.545) |
| MSC | 11M06, 11M26, 11N05 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://www.numdam.org/item/10.24033/bsmf.545.pdf |
| Selection | score 4.6143, in-pool citations 51, seed lists 1, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Prove that zeta(s) has no zero on the line Re s=1 (and the same for Dirichlet L-series), and deduce from the product representation of the entire function xi (Hadamard 1893) that the sum of logarithms of primes up to x is asymptotic to x (Halphen's statement), including in an arithmetic progression.

**Historical motivation.** Riemann 1859 conjectured the explicit formula; Stieltjes (1885) announced zeros all on Re s=1/2 without published proof; Cahen 1894 gave a proof of theta(x)~x relying on Stieltjes's claim; Hadamard repairs it by a different route. Results were announced to the Academie des sciences on 22 June 1896.

### Main results

- **THM-PAPER-0009-1** (n.1-4, theorem, scope: global; nos. 1-4, pp.199-202). \zeta(1+it)\neq0 for every real t\neq0 (i.e. \zeta has no zeros on the line \Re s=1; at t=0 it has the simple pole).
- **THM-PAPER-0009-2** (n.5, theorem, scope: global; no. 5 pp.202-203). Generalisation of nonvanishing: any function f(s) holomorphic except for a simple pole, uniform on the line \Re s=1, and with \log f(s)=\sum a_n n^{-s} with all a_n \ge 0 for \Re s>1 is non-zero on \Re s=1; likewise a product over an arbitrary split of the primes into two classes provided it is holomorphic on the line (the 'exception: possibly at s=1'). Example: Schlomilch's function \sum\frac{1}{(2n+1)^s}\ldots.
- **THM-PAPER-0009-3** (n.6-10, theorem, scope: global; nos. 6-10 pp.203-210). Dirichlet series L_\chi(s) with periodic coefficients (combinations of the Hurwitz-Cahen functions) are entire of genus 1 with \sim R\log R zeros in |s|<R (apart from the pole); under the Lipschitz conditions (k\ge3, x odd, etc.) L_\chi(1-s) is related to \overline{L_\chi(s)} by an exponential-trigonometric factor, hence all complex zeros lie in the strip 0\le\Re s\le1 and are symmetric about \Re s=1/2; extended to all Dirichlet series L (n.9 remarks 1-3). Also L_\chi(1+it)\neq0 by the same positivity argument, using Dirichlet's fundamental equation n.10. *Conditional on:* Lipschitz's functional equation (imported), Hurwitz 1882, Cahen 1894 (imported).
- **THM-PAPER-0009-4** (n.11, theorem, scope: asymptotic; no. 11 pp.210-211). For a>1 let N_a(x) be the number of primes in (x, x^a)... As s\to1^+, \sum\log\frac1{p}\ldots gives: for any \epsilon>0, infinitely often N_x>(1-\epsilon)... and infinitely often N_x<(1+\epsilon)...; hence if \sum_{p\le x}\log p/x has a limit, it is 1. Hadamard remarks this is the same type as Poincare's inequalities (extension to complex primes) and Tchebycheff.
- **THM-PAPER-0009-5** (n.12-18, theorem, scope: asymptotic; nos. 12-18 pp.211-218; final statements (21)-(22) p.218). For \mu>1 (and \mu=2 as the key case), \sum_{p<x}(\log p)\log^{\mu-1}(x/p)=(1+o(1))\,x\cdot c_\mu (the normalisation by \Gamma(\mu) from the Riesz-type kernel \frac1{2\pi i}\int_{(a)}x^z z^{-\mu}dz=\log^{\mu-1}x/\Gamma(\mu) is dropped in the OCR, but the paper says 'asymptotic to x'); in particular, with \mu=2, \sum_{p<x}\log p\log(x/p)\sim x; and deducing, by differencing x and x(1+h) and dividing by \log(1+h): \theta(x)=\sum_{p<x}\log p\sim x (Halphen's theorem), equivalently the prime number theorem \pi(x)\sim x/\log x by Tchebycheff. *Conditional on:* Hadamard 1893 product representation (imported).
- **THM-PAPER-0009-6** (n.19, theorem, scope: asymptotic; no. 19 pp.218-219). For (k,m)=1, \sum_{q\le x,\ q\equiv m\,(k)}\log q\sim x/\varphi(k) (the primes in a given residue class mod k have logarithmic density 1/\varphi(k)); the analogous Cahen-type integral with L-series gives it. Authors remarks that the general equation 'for mu in the Riesz weighted form' cannot apparently be deduced from this endpoint case, and error terms are asked about.
- **THM-PAPER-0009-7** (n.20, remark, scope: conditional; no. 20 p.219). The same method (non-vanishing on Re s=1 from the positive-coefficient log and the Weber/Meyer series) applies to quadratic-form L-series of Weber and Meyer; for negative determinant a formula of Weber already supplies the needed analytic continuation and genus. *Conditional on:* uniformity of the Weber and Meyer series (not proved here).

### Key definitions

- S_n, P_n: partial sums over the first n primes of p^{-s} and p^{-s}cos(t log p); S'_n,P'_n, S''_n,P''_n for the class of primes with t log p within angle a of 2k\pi
- \rho_n=S'_n/S_n
- L_\chi(s): Dirichlet series with periodic coefficients mod k (Hurwitz-Cahen)
- genus of an entire function as in Hadamard 1893

### Principal lemmas

- **THM-PAPER-0009-L1** (n.2-4 (the Hadamard trick); nos. 2-4 pp.200-202). If \zeta(1+it_0)=0 then \sum_p p^{-s}\cos(t_0\log p)\to-\infty like \log(s-1) as s\to1^+. Split primes into those with t_0\log p within angle a of 2k\pi... (class 1) and the rest. The ratio \rho_n=S'_n/S_n of the partial sums must tend to 1 as s\to1; then replacing t by 2t_0 forces Q_n\ge\theta' S_n with \theta'=\rho\cos2a-(1-\rho)>0 for suitable a, so that \Re\log\zeta(s+2it_0)\to+\infty which would make 1+2it_0 a pole of \zeta, a contradiction. — *Role:* Core of the nonvanishing proof; uses only positivity of coefficients of \log\zeta and the double-angle identity 1+\cos\theta... (equivalent to Mertens' 3-4-1 inequality in angle form)
- **THM-PAPER-0009-L2** (n.6; no. 6 pp.203-205). The Hurwitz-Cahen functions are entire (apart from s=1) of genus 1, with the number of zeros in |s|<R of order R\log R, by the contour representation (8) and Hadamard's genus theorems applied to the entire integral factor (coefficient comparison with \Gamma's integral). — *Role:* Gives convergence of \sum 1/|\alpha|^{1+\epsilon} needed to separate finitely many zeros and bound the rest
- **THM-PAPER-0009-L3** (n.14-16 (contour deformation); nos. 14-16 pp.213-216). Choose horizontal lines at heights between consecutive zero ordinates with gap \ge cA(A-1)/ (K\lambda); on these \left|\frac{\zeta'(z)}{\zeta(z)}\right|\le K'\log z_0 (from the partial fraction expansion (20) over zeros \alpha and trivial poles \beta and the zero count \le K\lambda A^{3\lambda}); the integrals over those horizontal segments tend to 0. — *Role:* Replaces von Mangoldt-type zero-counting/zero-free information by a self-contained estimate valid whenever the genus is known
- **THM-PAPER-0009-L4** (n.16; no. 16 pp.216-217). After shifting contours, the residue at z=1 is -x; the residues at zeros not among the first M have total modulus < \epsilon x (tail of the convergent series \sum 1/|\alpha|^{a}), and the remaining contour integral is o(x). — *Role:* Yields \sum_{p<x}\log p\log^{\mu-1}(x/p)\sim x

### Proof architecture

(i) Elementary-positivity proof that \zeta(1+it)\neq0 using only that \log\zeta is a Dirichlet series with positive coefficients and a simple pole at s=1 (nos. 2-5). (ii) Extension to periodic Dirichlet series (Hurwitz-Cahen functions) with genus 1 and functional equations (nos. 6-10). (iii) Replace Cahen's argument (which relied on Stieltjes's unproved Re=1/2 claim) by a Riesz-type integral \frac1{2\pi i}\int\frac{\zeta'(z)}{\zeta(z)}\frac{x^z}{z^\mu}dz, contour shifted left using Hadamard's 1893 genus bound and the nonvanishing on Re z=1 so that finitely many zeros need separate treatment; residue at z=1 gives x (nos. 12-16). (iv) Weighted sum asymptotic to x converted into \theta(x)\sim x by differencing at x and x(1+h) and monotonicity (nos. 17-18). (v) Same for progressions (no. 19). Imported: Hadamard 1893 (genus/product), Hurwitz 1882 and Cahen thesis 1894 for L-functions, Lipschitz functional equation, Dirichlet's fundamental equation.

Dependency edges: CAND-00001 → CAND-00019 (uses genus-1 product for xi and the Hadamard factorisation); CAND-00001 → CAND-00003 (independent simultaneous proof of zeta(1+it)!=0 and PNT (Nota p.220)); CAND-00001 → CAND-00004 (compares with Mangoldt's zero distribution; avoids it)

**Imported results.** Hadamard 1893 genus and product for xi; Hurwitz 1882, Z. Math. Phys. 27, 86-101; Cahen thesis 1894 (Ann. ENS (3) 11): analytic continuation of Hurwitz-type functions; Lipschitz, J. Reine Angew. Math. 105: functional equation of L-series; Dirichlet's fundamental equation; Bachmann, Analytische Zahlentheorie, for Weber/Meyer series

**Techniques.** Positivity of Dirichlet coefficients of log zeta; Double-angle trick (1+cos 2a... ) / equivalent of 3-4-1 inequality; Riesz-type kernel x^z/z^mu; Contour deformation controlled by genus; Differencing to pass from weighted sums to theta(x)

## Context and interpretation

**Importance and obstacle overcome.** Closes the gap that kept the prime number theorem out of reach: non-vanishing of zeta on Re s=1 together with the Hadamard product gives the PNT (equivalent to Halphen's theta(x)~x). The obstacle: the positivity trick only works at finitely many points; one needs to transfer it into a contour-shift argument without having a zero-free strip, which is why Hadamard controls tail zeros by the convergence of sum 1/|alpha|^{a} and chooses horizontal lines between zeros. Independent (simultaneous) with de la Vallee Poussin (see Nota p.220).

**Relation to prior work.** Builds on Hadamard 1893 (genus), Cahen (1894 thesis; contour technique), Hurwitz 1882, Lipschitz, Mangoldt 1895 (comparison; Hadamard notes his method avoids the zero count), Tchebycheff, Poincare's inequalities for complex primes. Simultaneous independent with de la Vallee Poussin 1896.

**Limitations and open questions.** Only an asymptotic equivalence, no error term (Hadamard asks, no. 19, what the weighted equation says about the size of the error). The proof of nonvanishing uses only the pole/positivity structure, but the passage to \theta(x)\sim x uses the genus theory for each family of L-series (done for \zeta, Dirichlet L; quadratic forms only announced). Does not prove Stieltjes's/Riemann's claim of zeros on Re s=1/2 ('Nous sommes bien loin d'avoir demontre l'assertion de Riemann-Stieltjes'; not even excluded zeros accumulating towards Re s=1).

**Ideas in remarks/appendices/abandoned paths.** (1) no. 5: the non-vanishing proof applies to any 'two-class' product over primes holomorphic on the line, a prototype for abstract positivity arguments (Landau, Mertens trick) in the Selberg class. (2) no. 19: Hadamard queries whether the Riesz-weighted equation for general mu contains more precise information on the error term than the endpoint mu=1 case, an early pointer to Riesz means for error terms. (3) no. 11 Tchebycheff-type inequalities from s->1 behaviour alone. (4) no. 20: the method for Weber/Meyer series for quadratic forms.

## Research potential

- **Hypotheses that might be weakened.** Only positivity of the Dirichlet coefficients of log f and holomorphy on the line are used (n.5): applies to any L-function with Euler product positive log-coefficients; the hypothesis 'known genus' in the contour step could be replaced by a zero-density/log-derivative bound (Landau-type) to remove genus theory entirely.
- **Generalizations.** Selberg class members and automorphic L-functions (Rankin-Selberg positivity of log coefficients) give nonvanishing on Re s=1; the Riesz kernel with real mu (nos. 12-18) is a natural family for Tauberian-free proofs of PNT in arithmetic semigroups.
- **Candidate connections.** The 3-4-1 / double-angle trick is the origin of de la Vallee Poussin/Mertens positivity (1+cos)^2>=0, and of positivity-based zero-free regions (Landau's lemma), and of the Siegel zero problem in the one-real-character case.
- **Reusable lemmas.** The angle-class argument (nos. 3-4): a clean lemma stating that if a Dirichlet series with non-negative coefficients log-derivative has a pole of order m at s=1 then it cannot also have a zero at 1+it_0 of order beyond m/2, in its original form without Mertens' inequality.
- **Possible experiments.** Quantify Hadamard's argument: compute the explicit lower bound on |zeta(1+it)| that follows from the angle-class argument versus the classical 3-4-1 argument, to see which gives a better zero-free region constant; numerically test the Riesz-weighted asymptotics sum_{p<x} log p log(x/p) ~ x at x up to 10^9 and look at the secondary oscillation from the first zero gamma_1=14.1347 (relative size x^{-1/2}).
- **Risks / barriers.** By itself the method yields only o(x) error with no explicit rate; passing to zero-free regions of classical shape needs de la Vallee Poussin's 1899 refinement; nothing here touches the critical-line location of zeros so no direct route to RH.

## Audit notes (Level 1 reader)

OCR garbles most formulas (e.g. eq.(4), (5), (19), (21), (22)); the exact weights in the Riesz sum of nos. 13-17 (exponent mu vs mu-1, Gamma normalisation) are reconstructed from the integral (17) and the text; the paper itself states 'asymptotic to x'. No mathematical error noticed in the portion read. Hadamard himself flags (no. 11) that his result does not exclude zeros accumulating towards Re s=1 and that the general-mu equation does not seem to imply the endpoint. The proof in no. 4 requires a < pi/2-ish constraint 1>rho>1/(1+cos 2a); consistent.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00001`; harvest queries: msc_11M06, msc_11M26, msc_11N05.
- Triage decision: include — Hadamard's 1896 proof of the prime number theorem via nonvanishing of zeta on Re s=1.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
