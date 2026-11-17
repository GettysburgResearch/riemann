# PAPER-0044 — Analytical research on the theory of prime numbers

*Original title:* Recherches analytiques sur la théorie des nombres premiers.

| Field | Value |
|---|---|
| Authors | de la Vallée Poussin, Ch. J. |
| Year / stratum | 1896 / S1 |
| Venue | Brux. S. sc. 21 B, 183-256, 281-362, 363-397 (1896). |
| Identifiers | zbMATH [27.0155.03](https://zbmath.org/?q=an:27.0155.03) |
| MSC | 11M06, 11M20, 11M26, 11N05, 11N13, 11N32 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://archive.org/download/recherchesanaly00pousgoog/recherchesanaly00pousgoog_djvu.txt (Google-digitized Hayez 1897 offprint of Ann. Soc. Sci. Bruxelles 20B, 2nd part, 1896; bound with Parts II-IV) |
| Selection | score 4.5684, in-pool citations 36, seed lists 1, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Give an analytic theory of primes (Part I) via Riemann's zeta: prove rigorously that zeta(s) has no zeros of the form 1+beta i, and deduce asymptotic consequences for primes; then (Part II) extend to Dirichlet L-functions and primes in the progression Mx+N, and (Part III) to primes represented by quadratic forms of negative determinant (Part IV, 1898: positive determinant).

**Historical motivation.** Riemann 1859 and the Chebyshev bounds; Hadamard 1893 made the product over zeros rigorous; the PNT was open; both authors announced similar results in the same year with Hadamard's note (Bull. SMF, p.220 Nota) acknowledging de la Vallee Poussin's simultaneous independent work.

### Main results

- **THM-PAPER-0044-1** (Part I, ch. III-IV (stated aim, nos. 2, 42), theorem, scope: global; Part I, no. 2 (statement of object), nos. 31-42 (L+P theorems), proof in ch. III). \zeta(s) has no root of the form \rho=1+\beta i (\beta real, \beta\ne0); the proof is by contradiction: supposing such a root, the fundamental equation (no. 28/31) gives a function of y represented in two incompatible ways as a sum 'L+P' (a limit plus an almost-periodic / purely oscillatory part), contradicting uniqueness theorems II-V.
- **THM-PAPER-0044-2** (Part I, ch. IV (nos. 55-56, eq.(5),(9)), theorem, scope: asymptotic; Part I ch. IV, nos. 55-56 (pp. ~62-66 of the offprint), eq.(5)-(9)). From the fundamental equation with y\to\infty (the series over the zeros tends to zero because \Re(\rho-1)<0 for all zeros): \sum_{p}\ldots\int\ldots=y-\ldots+\epsilon_y and (eq.(9)) \int^y\!\sum_{p<x}\log p\,\frac{dx}{x}-type identity; changing y to (1+k)y and subtracting yields that the ratio \frac1y\sum_{p\le y}\log p tends to 1 (equivalent of Tchebycheff function \theta(y)\sim y), and hence \pi(x)\sim x/\log x (prime number theorem; the PNT statement itself I did not locate verbatim in the OCR).
- **THM-PAPER-0044-3** (Part I, ch. II, theorem, scope: global; Part I ch. II (nos. 13-18)). Functions \int\theta(x)e^{\ldots}x^{s}dx with \theta continuous bounded as x\to\infty and a>0 are entire of genus at most 1 in s (Theorem II, no. 16); consequently the auxiliary functions \varphi_1,\varphi_2 built from \psi_1(a,x)=\sum_n e^{-\pi(n+a)^2 x} are entire of genus 1, which supplies the zero-sum representation of \zeta'/\zeta.
- **THM-PAPER-0044-4** (Part II (title; ch. I-V), theorem, scope: asymptotic; Part II ch. IV §§2-3, ch. V (headings seen at OCR lines 5055, 5206); statements not read in detail). No Dirichlet L-function L(s,\chi) vanishes on \Re s=1 (Part II ch. IV §2 'Aucune fonction L(s,\chi) ne s'annule pour s=1+beta i'), whence the theorem of Dirichlet on primes in arithmetic progressions is re-proved (ch. IV §3), and the primes \equiv N (mod M) have asymptotic density 1/\varphi(M) (asymptotic form in ch. V).
- **THM-PAPER-0044-5** (Part III, theorem, scope: asymptotic; Part III (and Part IV of 1898 in the same bound volume)). Title-level: primes representable by a quadratic form of negative determinant have the asymptotic distribution expected (Part III); positive determinant in Part IV (1898). Exact statements not read.

### Key definitions

- \psi_1(a,x)=\sum_{n\in\mathbb Z}e^{-\pi(n+a)^2x}
- fonction Z_1(a,s), Z_2(a,s) Hurwitz-type zeta functions
- L+P: sum of a function tending to a limit (L) and a purely periodic (almost periodic) part (P)
- condition \theta (theta-type growth condition used for entire functions of genus 1)

### Principal lemmas

- **THM-PAPER-0044-L1** (Theorems I-V, nos. 36-41 (the 'L+P' calculus); nos. 31-42 (offprint pp. ~40-48)). A function \Phi(y)=L(y)+P(y) with L\to0 (limit part) and P purely periodic/almost periodic is uniquely decomposed; operations (multiplication by cos, change of y to ky, summation of the associated series) preserve the form and the periodic part carries the same trigonometric lines with the same coefficients (Theorems III-V). — *Role:* Replaces the 3-4-1 positivity argument by a uniqueness-of-almost-periodic-part argument: two contradictory expressions in the form L+P (from real and imaginary parts of the fundamental equation, nos. 34-42) refute \rho=1+\beta i
- **THM-PAPER-0044-L2** (no. 31, eq. of the 'equation fondamentale'; no. 28, no. 31, no. 32). For \Re\alpha>1: an exact identity expressing \frac{\zeta'}{\zeta}-weighted sums over primes via the sum over zeros \rho of terms e^{\rho y}/(\ldots), a constant, three rapidly decaying terms, and periodic terms \sum a_n\cos(\alpha_n y)+b_n\sin(\alpha_n y) arising from the pole at s=1 and zeros on \Re s=1. — *Role:* Source of the representation to which L+P theorems are applied
- **THM-PAPER-0044-L3** (no. 15 (general theorem on integrals); no. 14-15 (OCR line ~1204)). If \Re(\alpha+k_n) stays between two positive bounds, \sum|\cdot| converges and a further series converges, then the representation by partial fractions extends (general convergence theorem enabling the zero-sum expansion). — *Role:* Justifies the infinite partial-fraction sum for the logarithmic derivative

### Proof architecture

Part I: (ch. I) recall formulas: Euler product, analytic continuation via the elementary integral formula (2) for \Re s>0; (ch. II) analytic structure: \zeta via theta-type integrals, the auxiliary entire functions of genus <=1, partial fractions over zeros (Hadamard 1893 imported); (ch. III) 'L+P' calculus and the proof of \zeta(1+\beta i)\ne0 by deriving two contradictory L+P expansions; (ch. IV) from the fundamental equation as y\to\infty obtain \theta(y)\sim y and consequences. Part II: same architecture for L(s,\chi) (characters mod prime p then composite), then Dirichlet's theorem in an asymptotic form. Part III: quadratic forms via Z(s)-functions of Weber type. Imported: Riemann 1859, Hadamard 1893 (genus), Dirichlet, Hurwitz, Weber. Independent route from Hadamard 1896 (positivity trick), which is documented in Hadamard's Nota.

Dependency edges: CAND-00003 → CAND-00019 (imports genus-1 product for xi); CAND-00003 → CAND-00001 (independent simultaneous proof (mutual acknowledgement))

**Imported results.** Riemann 1859 functional equation and theta-integral representation; Hadamard 1893 (genus and product, cited in note p.1); Dirichlet's L-series and characters; Hurwitz function Z(a,s); Weber series for quadratic forms

**Techniques.** Almost-periodic (L+P) uniqueness calculus; Genus-1 partial-fraction expansion of zeta'/zeta over zeros; Fundamental equation y-integral identity (Mellin-like); Elementary Chebyshev-type differencing in y (1+k)y; Dirichlet characters and Gauss sums for the progression part

## Context and interpretation

**Importance and obstacle overcome.** Independent proof (simultaneous with Hadamard 1896) of the prime number theorem via non-vanishing of zeta on Re s=1, plus the first treatment of arithmetic progressions and quadratic forms with Riemann's analytic method. The obstacle: how to exclude zeros on the line Re s=1 when the Euler series no longer converges absolutely; solved by the L+P uniqueness argument. Establishes the 'analytic school' of prime number theory.

**Relation to prior work.** Uses Riemann 1859, Hadamard 1893, Mangoldt 1895 only lightly; distinguishes itself from Hadamard 1896 (positivity trick) by the L+P method; extends Dirichlet 1837-1840 and Weber/Meyer quadratic-form L-series.

**Limitations and open questions.** Only asymptotic equivalences (error o(.)); explicit error terms (de la Vallee Poussin 1899, zero-free region 1-c/log t) come later in a separate memoir. No statement about the critical line. My reading did not cover the proofs of Parts II-III or the middle of Part I, so quantitative content beyond the headings is not verified here.

**Ideas in remarks/appendices/abandoned paths.** The L+P (limit plus almost periodic) decomposition of functions of y and its uniqueness theorems anticipate Wiener's Tauberian theory and Bohr almost periodic function methods; applying the 'identification of oscillating parts' to prime-counting residuals could give quantitative lower bounds (Omega results). Not developed in this memoir.

## Research potential

- **Hypotheses that might be weakened.** The L+P method uses only Dirichlet-series positivity + genus 1; test whether it yields the zero-free region 1-c/log t by tracking quantities (it is known to give only a qualitative result here).
- **Generalizations.** Selberg-class L-functions and Rankin-Selberg convolutions; the uniqueness theorem for L+P expansions may adapt to Beurling generalized primes where Tauberian approaches are used.
- **Candidate connections.** Wiener-Ikehara Tauberian theorem and Bohr almost periodic functions; quantitative: connect to Landau's Omega theorems for psi(x)-x using the periodic part from zeros.
- **Reusable lemmas.** Uniqueness of the L+P decomposition (Theorems III-V) as a clean standalone statement about functions of the form (limit) + (trigonometric sums).
- **Possible experiments.** Numerically reconstruct the 'periodic part' P(y) from the first few hundred zeros and compare with actual (psi(e^y)-e^y)e^{-y/2} to illustrate the L+P decomposition; check when the L component vanishes in practice.
- **Risks / barriers.** Method is qualitative; no obvious route to RH since it uses only that nothing happens on Re=1.

## Audit notes (Level 1 reader)

Basis is partial: OCR copy is a 1897 Hayez offprint (bound with later Parts IV 1898), text is out-of-order and noisy; I did not read proofs in Parts II-III or most of Part I. The statements for Parts II-III are headings-level only and marked as such. Pagination refers to the offprint, not to Ann. Soc. Sci. Bruxelles 20B pp. 183-256, 281-362, 363-397. The triage note 'independent of Hadamard' is consistent with Hadamard's Nota (Bull. SMF p.220). Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00003`; harvest queries: msc_11M06, msc_11M20, msc_11M26, msc_11N05.
- Triage decision: include — De la Vallee Poussin's independent 1896 proof of the PNT, landmark.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
