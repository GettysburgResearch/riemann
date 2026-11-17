# PAPER-0133 — More than one third of zeros of Riemann's zeta-function are on \(\sigma=1/2\)

| Field | Value |
|---|---|
| Authors | Levinson, Norman |
| Year / stratum | 1974 / S3 |
| Venue | Adv. Math. 13, 383-436 (1974). |
| Identifiers | zbMATH [0281.10017](https://zbmath.org/?q=an:0281.10017) · DOI [10.1016/0001-8708(74)90074-7](https://doi.org/10.1016/0001-8708(74)90074-7) |
| MSC | 11M06 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Levinson.pdf (copy of Adv. Math. 13 (1974) 383-436; DOI 10.1016/0001-8708(74)90074-7) |
| Selection | score 3.6183, in-pool citations 87, seed lists 4, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Show that a positive proportion, indeed more than 1/3, of the zeros of zeta(s) lie on sigma=1/2, improving Selberg's unspecified positive constant c, by a method that bounds the variation of the argument of an auxiliary function G(s) built from zeta and zeta' rather than by Hardy-Littlewood sign-change counting.

**Historical motivation.** Hardy-Littlewood (1921) proved N_0(T)>cT, Selberg (1942) proved N_0(T)>cN(T) with an effectively computable but tiny c using a non-negative mollifier. Levinson sought an effective proportion by tracking the argument of an auxiliary function rather than sign changes of Z(t).

### Main results

- **THM-PAPER-0133-1** (Theorem (p. 384), theorem, scope: asymptotic; Section 1, p. 384; proof in Section 15, pp. 433-435). Let L=\log(T/2\pi) and U=T/L^{10}. For all sufficiently large T, N_0(T+U)-N_0(T)>\tfrac13\,[N(T+U)-N(T)], where N_0(T) counts zeros of \zeta(1/2+it) with 0<t\le T and N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T) counts all zeros in 0<\sigma<1,0<t<T. The proof actually yields the lower bound 0.34\,UL/(2\pi).
- **THM-PAPER-0133-2** (Corollary (p. 384, due to H. L. Montgomery), corollary, scope: asymptotic; p. 384; proof at end of Section 15). If m denotes the multiplicity of a zero of \zeta on \sigma=1/2, then \sum (m-1) over zeros with 1/2+iT\le \rho\le 1/2+i(T+U) is bounded by N_G(D)<0.329\,UL/(2\pi) (from (15.4)); hence \sum_{m\ge2} m is a small multiple (<~ 2 times that) of UL. The constants in the printed statement are garbled in OCR ('C(m-1)<G log g').
- **THM-PAPER-0133-3** (Eq. (1.12), key intermediate result, scope: asymptotic; Section 1, (1.9)-(1.12)). With G(s)=\zeta(s)+\frac{\zeta'(s)}{f'(s)+f'(1-s)} and D the rectangle with vertices 1/2+iT, 3+iT, 3+i(T+U), 1/2+i(T+U): \arg G(1/2+it)\big|_T^{T+U}=-2\pi N_G(D)+O(L), where N_G(D) is the number of zeros of G in D.
- **THM-PAPER-0133-4** (Eqs (15.1)-(15.4), key computation, scope: asymptotic; Section 15, pp. 433-434). With y=T^{1/2}/L^{20}, mollifier \psi (Dirichlet polynomial of length y built from the Mobius function with smoothing weights, defined in (2.3)-(2.4)), a=1/2-R/L and R fixed: \int_T^{T+U}|\psi G(a+it)|^2dt=U\,F(R)+O(U\log^5L/L), with F(R)=e^{2R}(\cdots) (explicit expression (15.1)). For R=1.3: F(1.3)<2.3502, giving (1/2-a)\,2\pi N_G(D)<0.4275\,U, i.e. 2\pi N_G(D)<0.329\,UL.

### Key definitions

- h(s)=\pi^{-s/2}\Gamma(s/2), f=\log h, \chi(s)=h(1-s)/h(s)
- G(s)=\zeta(s)+\zeta'(s)/[f'(s)+f'(1-s)]
- L=\log(T/2\pi), U=T/L^{10}, y=T^{1/2}/L^{20}
- \psi(s): mollifier (2.3)-(2.4)
- N_G(D): number of zeros of G in D

### Principal lemmas

- **THM-PAPER-0133-L1** (Eq. (1.6)-(1.9); Section 1). Zeros of \zeta(1/2+it) occur where \arg\{h(s)\,[\,(f'(s)+f'(1-s))\zeta(s)+\zeta'(s)\,]\}\equiv\pi/2\ (\mathrm{mod}\ \pi) on \sigma=1/2 (h(s)=\pi^{-s/2}\Gamma(s/2)); so it suffices to control the argument change of G(s) on the half line. — *Role:* Converts zero counting for zeta on the critical line into winding of G; argument change on the line is dominated by zeros of G in D.
- **THM-PAPER-0133-L2** (Littlewood's lemma, eq. (2.2); (2.5)-(2.6); Section 2). For F analytic in D_a, \int_T^{T+U}\log|F(a+it)|dt-\int_T^{T+U}\log|F(3+it)|dt+\int_a^3\arg F(\sigma+i(T+U))d\sigma-\int_a^3\arg F(\sigma+iT)d\sigma=2\pi\sum\mathrm{dist}; applied to \psi G with concavity \int\log|\psi G|\le \frac U2\log(\frac1U\int|\psi G|^2). — *Role:* Bounds N_G(D) by a mollified mean square of G on the line sigma=a slightly left of 1/2; the mollifier flattens |zeta| to make Jensen sharp.
- **THM-PAPER-0133-L3** (Eq. (2.16)-(2.20); Section 2). Via the Riemann-Siegel formula, G(\sigma+it)=H(\sigma+it)+H_1(t) with H_1(t)=O(t^{-1/4}) and H=\ldots built from g_1,g_2,g_3 (sums over n<(t/2\pi)^{1/2}) and \chi_1(t); then \int|\psi G|^2=\int|\psi H|^2+O(U^{1/2})+\ldots — *Role:* Reduces the mean square to Dirichlet polynomials of length ~T^{1/2}.
- **THM-PAPER-0133-L4** (Lemma 3.2; Section 3, p. 391). For 1\le A_1,A_2\le T^{1/2}, (A_1,A_2)=1, off-diagonal sum over j_1,j_2 with A_1j_1\ne A_2j_2 satisfies a bound <100\,T^{1-2a}\log T (precise form (3.2) garbled). — *Role:* Off-diagonal (Montgomery-Vaughan-type) control in the mean square.
- **THM-PAPER-0133-L5** (Lemmas 3.3-3.5; Section 3). Lemma 3.4: \int_A^B\exp[it\log(t/ye)](t/2\pi)^{1/2-a}dt=(2\pi)^a y^{1-a}e^{-iy+\pi i/4}+E(y) for A<y<B<A+A/\log A (analogue of Selberg 1942 Lemma 2); Lemma 3.5 handles the same for m=1,2. — *Role:* Stationary-phase evaluation of the main oscillatory integrals arising from the Riemann-Siegel main sum.
- **THM-PAPER-0133-L6** (Lemmas 3.6-3.7; Section 3, pp. 395-397). Lemma 3.6: \sum_{k|k_1,k_2}\ldots with k=(k_1,k_2): \sum k/(k_1k_2)\ldots=O(\log^3 y). Lemma 3.7: lattice-point count \sum_{(n,m)\in K}f(n,m)=\iint_K f\,du\,dv+\mathcal J with explicit error for a region in the first quadrant (Euler-Maclaurin in two variables). — *Role:* Combinatorial and lattice tools for evaluating the double sums over mollifier coefficients.
- **THM-PAPER-0133-L7** (Lemmas 3.8-3.13; Section 3, pp. 398-). Lemma 3.8 (Mobius inversion of g(m)=\sum_{r|m}\mu(r)f(rm)-type); Lemma 3.9: for large squarefree j, \sum_{p|j}\frac{\log p}{p}=O(\log\log j); Lemma 3.11: J(x)=\sum_{r\le x}\mu^2(r)\prod_{p|r}f(p)/r \cdots=\prod_p(1+\tfrac{1}{p}\ldots)(1-\tfrac1p)\log x+O(1) for f(p)=1+O(p^{-c}); Lemmas 3.12-3.13 variants. — *Role:* Evaluation of the arithmetic sums (singular series) that give the explicit value F(R).
- **THM-PAPER-0133-L8** (Section 15, (15.5)-(15.8); pp. 434-435). If zeta has a zero of multiplicity m on sigma=1/2 then G has one of multiplicity m-1; each zero of G on the line gives a zero of zeta of one higher multiplicity; counting the argument variation of G on intervals between indentations at the N_1' zeros on the line gives at least UL/(2\pi)\cdot(1-2\cdot0.329)>0.34\,UL/(2\pi) zeros of zeta on the line. — *Role:* Final bookkeeping from argument variation of G to the count N_0 (including zeros of G on the line and multiplicity).

### Proof architecture

Section 1: reduce zeros of zeta on sigma=1/2 to argument variation of G(s)=zeta+zeta'/(f'(s)+f'(1-s)); bound arg change on the right and horizontal sides, so the line contributes -2pi N_G(D)+O(L). Section 2: Littlewood's lemma applied to mollified psi*G with concavity of log reduces N_G(D) to the mean square of psi*G on sigma=a=1/2-R/L, evaluated via the Riemann-Siegel formula, giving G=H+H_1. Section 3: arithmetic lemmas (Selberg-style). Sections 4-14: long evaluation of the diagonal/off-diagonal integrals I_ij and sums S_0,S_1,S_2,K_0,K_1,K_2 (derived with Mobius-sum/lattice-point lemmas) -- analysis analogous to Selberg 1942. Section 15: assemble to F(R); choose R=1.3 giving N_G(D)<0.329UL/2pi and conclude >1/3 of zeros on the line. Imported: Riemann-Siegel formula, Stirling, Littlewood's lemma, Jensen, Selberg's lemmas.

Dependency edges: CAND-00409 → Selberg 1942 mollifier lemmas (borrows); CAND-00409 → Riemann-Siegel formula (imports); CAND-00409 → Littlewood lemma (imports)

**Imported results.** Riemann-Siegel formula (Siegel 1932; Titchmarsh Sec. 2.10); Stirling formula for Gamma; Littlewood's lemma (Titchmarsh Sec. 9.9) and Jensen's theorem (Sec. 9.4); Selberg 1942 (Skr. Norske Vid. Akad. Oslo no. 10) lemmas for the mollifier evaluation; Levinson 1973 'Remarks on a formula of Riemann' (J. Math. Anal. Appl. 41) for Riemann-Siegel details; Levinson 1968 sieve-sum evaluation (J. Math. Anal. Appl. 22)

**Techniques.** Argument principle / change of argument of auxiliary function G=zeta+zeta'/(f'+f'); Littlewood's lemma with mollifier; Riemann-Siegel formula; Mollification by Mobius-type Dirichlet polynomial of length T^{1/2}/L^{20}; Mean square of Dirichlet polynomial with off-diagonal bound; Optimization over R (a=1/2-R/L)

## Context and interpretation

**Importance and obstacle overcome.** Gave the first large explicit proportion (>34%) of zeros on the line, introducing the mollified argument-principle method on zeta+zeta'/(...) that Conrey's 2/5 and later improvements build on. The obstacle was to convert a global argument-change into a count using mollified second moments in very short intervals (length T/L^10), where off-diagonal terms must be controlled, with sufficiently flat |psi G|^2 so that Jensen loses little.

**Relation to prior work.** Replaces Hardy-Littlewood/Siegel sign-change counting and Selberg's mollified sign-change method (which gave unspecified c) by an argument-variation method; borrows Selberg's arithmetic lemmas and mollifier idea. Announced in PNAS 71 (1974) 1013-1015. Improved by Conrey (2/5, 1989) and later authors.

**Limitations and open questions.** Unconditional proportion only; says nothing about the remaining zeros. Proportion 1/3 limited by the mollifier length theta=1/2 (y=T^{1/2-}) and the choice of G; no simplicity statement in the main theorem (corollary only bounds multiplicities). Interval length T/L^10, short intervals of this type only.

## Research potential

- **Hypotheses that might be weakened.** Mollifier length exponent 1/2 (extension to theta>1/2 is where Conrey/Bui-Conrey-Young gain); the form of G (higher derivatives: Conrey's use of zeta'' etc.).
- **Generalizations.** Levinson's method for Dirichlet L-functions, Selberg-class / GL(2) twists (e.g. arXiv:2511.06109, 2607.00282 found in search); proportion of simple zeros via the Corollary.
- **Candidate connections.** The N_G(D) bound is a mollified-Jensen inequality; an optimal-mollifier calculus (Feng, Bui-Conrey-Young) reduces to a quadratic form, a candidate experimental target; relation to Atkinson's off-diagonal analysis (CAND-00078) and Montgomery-Vaughan Lemma 3.2-type bounds (CAND-00336).
- **Reusable lemmas.** Lemmas 3.7 (2D lattice-point with derivative errors) and 3.9-3.13 (sums over squarefree j of f(p) with f(p)=1+O(p^-c)) are reusable arithmetic lemmas for mollifier sums.
- **Possible experiments.** Reproduce F(R) numerically (formula (15.1) is garbled in OCR; reconstruct from the Conrey-style formula) and compute the optimizing R and the resulting proportion 1-2*0.329~0.342 to validate; test mollified second moment of G numerically at T~10^6.
- **Risks / barriers.** Proportion results are local-in-density statements; they do not constrain existence of zeros off the line or any global RH functional. Method has an inherent ceiling (about 0.41 after all improvements) unless a new idea appears.

## Audit notes (Level 1 reader)

Several displayed formulas in the OCR are corrupted: the explicit F(R) in (15.1), the mollifier definition (2.4), the Corollary's constants, and Lemma 3.2's exact bound form. The Theorem's inequality uses N_0 whose multiplicity convention is not defined in Section 1; the proof counts with multiplicity. The proof of the Theorem is stated 'for large T'; also the statement is for the specific window U=T/L^10, not a full-interval asymptotic (a dyadic/chaining summation is implicit when passing to N_0(T)>(1/3)N(T)).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00409`; harvest queries: msc_11M06.
- Triage decision: include — Landmark: Levinson's one-third of zeros on the critical line.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
