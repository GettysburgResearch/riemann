# PAPER-0085 — The Riemann hypothesis

| Field | Value |
|---|---|
| Authors | Bombieri, Enrico |
| Year / stratum | 2006 / S5 |
| Venue | Carlson, J. (ed.) et al., The millennium prize problems. Providence, RI: American Mathematical Society (AMS); Cambridge, MA: Clay Mathematics Institute (ISBN 0-8218-3679-X/hbk). 107-124 (2006). |
| Identifiers | zbMATH [1194.11001](https://zbmath.org/?q=an:1194.11001) |
| MSC | 11-01, 11M26 |
| Families | A, C |
| Work type | survey |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf |
| Selection | score 4.3728, in-pool citations 11, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Official Clay Millennium statement of the Riemann hypothesis (nontrivial zeros of zeta lie on Re s = 1/2), with a survey of its history, significance, numerical and theoretical evidence, the function-field analogue, Weil's explicit formula and positivity criterion, and open questions on a cohomological or spectral approach.

**Historical motivation.** Official statement for the Clay Millennium Prize problem, tracing the line from Euler, Gauss and Chebyshev through Riemann (1859), Hadamard and de la Vallee Poussin, Hasse, Weil and Deligne.

### Main results

- **THM-PAPER-0085-1** (Sect. I, Riemann hypothesis, problem statement, scope: global; Sect. I). The nontrivial zeros of \zeta(s) have real part 1/2; equivalently all zeros of \xi(t)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s), s=\tfrac12+it, are real.
- **THM-PAPER-0085-2** (Sect. II, equivalent form, equivalence (cited, classical), scope: asymptotic; Sect. II p.4). RH is equivalent to \pi(x)=\mathrm{Li}(x)+O(\sqrt x\log x); Littlewood: \pi(x)-\mathrm{Li}(x) changes sign with size at least \mathrm{Li}(\sqrt x)\log\log\log x.
- **THM-PAPER-0085-3** (Sect. III, numerics, computational evidence (cited), scope: finite; Sect. III pp.5-6). van de Lune-te Riele-Winter: the first 1.5 billion zeros are simple and on the line (T about 5x10^8). Odlyzko: more than 3x10^8 zeros at heights near 2x10^20 satisfy RH. A planned interval is [10^22,10^22+10^10].
- **THM-PAPER-0085-4** (Sect. III, density and proportion, theorems (cited), scope: asymptotic; Sect. III p.6). N(\alpha,T)=O(T) (Bohr-Landau 1914); N(\alpha,T)=O(T^{4\alpha(1-\alpha)+\epsilon}) (Carlson 1920); Ingham exponent 3(1-\alpha)/(2-\alpha) for 1/2<\alpha<=3/4; more than 40 percent of nontrivial zeros are simple and on the line (Selberg, Levinson, Conrey).
- **THM-PAPER-0085-5** (Sect. IV, survey of theorem (cited), scope: global; Sect. IV pp.6-8). For a smooth projective curve C over F_q, Z(t,C) is rational with numerator of degree 2g and its zeros have |t|=q^{-1/2}. This is Hasse (g=1, 1934) and Weil (general g, 1940s), generalized by Deligne to varieties; the proof uses the index theorem for surfaces (Severi 1906).
- **THM-PAPER-0085-6** (Sect. V, Explicit Formula, formula (cited, Weil 1952), scope: global; Sect. V p.8). For f in the class W (continuous, piecewise C^1, f=O(x^\delta) at 0, O(x^{-1-\delta}) at infinity, Mellin transform \hat f(s)=\int_0^\infty f(x)x^s dx/x): \hat f(0)-\sum_\rho\hat f(\rho)+\hat f(1)=\sum_n\Lambda(n)[f(n)+\tfrac1n f(\tfrac1n)]+(\log 4\pi+\gamma)f(1)+\int_1^\infty[f(x)+\tfrac1x f(\tfrac1x)-\tfrac2x f(1)]\frac{x\,dx}{x^2-1}, with the zero sum taken as \lim_{T\to\infty}\sum_{|\mathrm{Im}\rho|<T}.
- **THM-PAPER-0085-7** (Sect. V, Weil positivity, equivalence (cited, Weil), scope: global; Sect. V p.9). RH is equivalent to a sign condition (negativity) of the right-hand side of the explicit formula for all f(x)=\int_0^\infty g(xy)g(y)dy with g in W and \int_0^\infty g(x)dx/x=\int_0^\infty g(x)dx=0. In the function-field case this is the index theorem for surfaces.

### Key definitions

- \xi(t)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s), s=1/2+it
- class W of admissible test functions
- explicit formula with \Lambda(n) and the (log 4\pi+\gamma) term
- Zeta function Z(t,C) of a curve over F_q

### Principal lemmas

- **THM-PAPER-0085-L1** (Algebraic Index Theorem; Sect. V p.9). For a nonsingular projective surface X over an algebraically closed field, the self-intersection form (D.D) on divisors of degree 0 for a projective embedding is negative semidefinite (Severi 1906; Hodge in characteristic 0). — *Role:* Geometric source of positivity in the function-field Riemann hypothesis, offered as the model for a hoped-for general index theorem.

### Proof architecture

No proof of RH is offered. Expository structure: statement; history from Euler and Chebyshev to Riemann's explicit formula; consequences of RH and GRH for primes, Chebotarev, cubic forms (Hooley) and Miller's primality test; evidence (numerics, zero-density, proportion on the line, function fields); Weil's explicit formula and positivity criterion with its geometric counterpart; random matrix and Hilbert-Polya remarks; closing questions about a cohomology theory, an analogue of Frobenius, and an index theorem for the classical case. Imported results include Hasse, Weil, Deligne, Severi, and the Weil explicit formula.

Dependency edges: CAND-01333 → CAND-01219 (Weil positivity viewpoint that Li coefficients realize)

**Imported results.** Explicit formula and positivity criterion (Weil 1952); Hasse 1934 and Weil 1940s RH for curves; Deligne, La conjecture de Weil I, II; Severi 1906 algebraic index theorem; Bohr-Landau, Carlson and Ingham zero density theorems; Selberg, Levinson and Conrey on the proportion of zeros on the line; van de Lune-te Riele-Winter and Odlyzko zero computations; Montgomery, Rudnick-Sarnak and Katz-Sarnak pair correlation

**Techniques.** Explicit formula (Riemann-Weil); Weil positivity / Hilbert space index; Rational zeta function of curves over finite fields; Zero verification via Cauchy integral and sign changes of xi(t); Random matrix universality (Montgomery-Odlyzko, Rudnick-Sarnak, Katz-Sarnak)

## Context and interpretation

**Importance and obstacle overcome.** It is the canonical authoritative statement of the problem, with the statement of Weil's explicit formula in the exact normalization used in the Clay problem and a clear formulation of the parallel between RH and the Weil conjectures via positivity. It does not overcome any obstacle. It frames the open problem.

**Relation to prior work.** Survey. Cites Edwards, Landau, Titchmarsh (revised by Heath-Brown), Iwaniec-Sarnak on L-functions, Weil (1952), Katz-Sarnak, and Connes, Deninger and Haran.

**Limitations and open questions.** All the closing questions are open: is there a global cohomological theory and a Frobenius analogue; is there an index theorem implying RH; and what is the situation for L-functions with no geometric origin (Maass), where the text says 'entirely new ideas may be needed'. Bombieri's 40 percent and numerics statements date from 2000 and have been superseded (Feng, Bui-Conrey-Young, Platt-Trudgian).

## Research potential

- **Hypotheses that might be weakened.** Not applicable as a survey. For the Weil positivity statement, the test function class W could be varied to see which subclass already gives an equivalent criterion, as in the Li test functions of Bombieri-Lagarias.
- **Generalizations.** The problem statement extends to global L-functions and the Selberg class, where the Mellin explicit formula is used.
- **Candidate connections.** Li coefficients as Weil positivity on specific test functions (see CAND-01219); Hilbert-Polya and random matrix remarks; Connes's adelic trace formula approach [Conn]; Deninger [Den]; Haran [Hara].
- **Reusable lemmas.** The normalized explicit formula with class W and the zero sum convention lim_{T} sum_{|Im rho|<T} is a reusable reference for sign and normalization checks of local computations in the archive.
- **Possible experiments.** Verify numerically the displayed explicit formula for explicit test functions (e.g. Gaussians in log x) and confirm the sign convention of the positivity criterion against Weil's formulation; compare with the Li-coefficient normalization.
- **Risks / barriers.** As the survey says, the function field proof uses geometry (Frobenius, cohomology, index theorem) with no known number field counterpart. Any program based on the analogy must produce an index theorem for the arithmetic of Spec Z.

## Audit notes (Level 1 reader)

Basis for the record: the Clay-hosted PDF of the problem description, which appears to be the same text as the AMS chapter but pagination was not verified. Sign convention in the Weil positivity statement (negativity of the right-hand side) is stated loosely in the text; the displayed extraction of the explicit formula has some garbled symbols from pdftotext (the sum signs), so the formula above is reconstructed from the standard form. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01333`; harvest queries: kw_RH_any, msc_11M26.
- Triage decision: include — Bombieri's Clay problem description of RH, standard reference.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
