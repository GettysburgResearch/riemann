# PAPER-0136 — On the distribution of the zeros of Riemann's function \(\xi(t)\).

*Original title:* Zur Verteilung der Nullstellen der Riemannschen Funktion \(\xi(t)\).

| Field | Value |
|---|---|
| Authors | v. Mangoldt, H. |
| Year / stratum | 1905 / S2 |
| Venue | Math. Ann. 60, 1-19 (1905). |
| Identifiers | zbMATH [36.0263.02](https://zbmath.org/?q=an:36.0263.02) · DOI [10.1007/BF01447494](https://doi.org/10.1007/BF01447494) |
| MSC | 11M26, 11M06 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://archive.org/download/sim_mathematische-annalen_1905_60/sim_mathematische-annalen_1905_60_djvu.txt |
| Selection | score 3.4952, in-pool citations 9, seed lists 2, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Prove an explicit-constant asymptotic for N(T), the number of zeros of Riemann's xi(t) with real part of t between 0 and T (i.e. zeros rho with 0<Im rho<=T in the modern normalisation), with error of order only log T, improving Mangoldt's earlier 1895 bound with an error of order (log T)^2.

**Historical motivation.** Riemann 1859 asserted the count of zeros up to T without proof; Mangoldt 1895 proved it with error O((log T)^2); this paper sharpens to O(log T) (Landau and later proofs by Backlund 1914 refine constants).

### Main results

- **THM-PAPER-0136-1** (Introductory statement (unnumbered), theorem, scope: asymptotic; Math. Ann. 60, p. 1 (introduction), proved on pp. 2-19). For $T>28.558$: $\left|N(T)-\left(\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}\right)\right|<0.43200\,\log T+1.91662\,\log\log T+13.07873$, where N(T) counts zeros of xi with Re t in (0,T) with multiplicity (OCR of the constants as read; the main term as in the 1905 claim N=(T/2pi)log(T/2pi)-T/2pi+O(log T)). The previous Mangoldt (1895, J. reine angew. Math. 114, p. 266) bound was $0.34(\log T)^2+1.35\log T+2.58$.

### Key definitions

- xi(t) = Riemann's function with zeta(s)=...xi((s-1/2)/i); zeros have real t in (-T,T) iff 1/2+it zeros
- N = number of zeros of xi(t) with real part of t between 0 and T, with multiplicity
- l = natural logarithm (footnote)

### Principal lemmas

- **THM-PAPER-0136-L1** (Eq. (1)-(4), Sec. 3, p. 3-5; pp. 2-5). Writing the change of arg of xi along the segments from -ia to T-ia to T, 2*pi*N equals twice the increment of the coefficient of i in log xi(t); the first segment's increment Theta_1(a,T) is computed from the Gamma-factor via Stieltjes' formula, giving Theta_1(a,T)=(T/2)log(T/2pi)-T/2+... with explicit remainders. — *Role:* Gamma-factor/Stirling part of the argument principle (explicit S-free part of N(T)).
- **THM-PAPER-0136-L2** (Eqs. (5)-(21), pp. 5-16; pp. 5-16). For the Dirichlet-series/zero part: counts of zeros in windows of length 2k are bounded using the positivity of the increment of the argument of each linear factor (1 - t/t_rho): the number of zeros in an interval of length 2k near height T is bounded by an expression M/(arctg(2k)...) in terms of the increment of the argument over the segment T..T+2k. — *Role:* Bounds the S(T)=arg zeta term (the log T order), by a window-counting device with parameter k.
- **THM-PAPER-0136-L3** (Eqs. (22)-(24), p. 16-17; p. 16-17). Optimisation in the free parameter k (called k): the minimiser satisfies $k^2\arctan(2k)$-type equation (22) with root k approx 0.675, giving the constant 0.432 in front of log T (zeta(3)=1.20206 used). — *Role:* Fixes the constants 0.43200, 1.91662, 13.07873.

### Proof architecture

Apply the argument principle to xi(t) on the rectangle with vertices -ia, T-ia, T, ... (a>1/2 arbitrary constant, T chosen to avoid zeros). Decompose the increment of the argument into the Gamma-factor part (computed exactly with Stieltjes' Stirling expansion) and the contribution from the factor of xi coming from zeta, i.e. the Dirichlet series part, which is estimated by the interval-counting argument using that arguments of each linear factor increase monotonically. A trace of positive terms is summed using absolute convergence; the bound on the number of zeros in short windows is optimised in the window half-length k, giving an O(log T) bound for S(T) with explicit constants valid for T>28.558.

Dependency edges: CAND-00089 → Mangoldt 1895 (improves); CAND-00089 → Riemann 1859 (completes proof of claim); CAND-00089 → Stieltjes 1889 Stirling expansion (imports)

**Imported results.** Riemann 1859 definition of xi(t) and relation with zeta (Monatsberichte p. 671); Stieltjes 1889 asymptotic expansion for log Gamma (J. math. pures appl. (4) 5, p. 431, formula (20); p. 433 formula (26)); Mangoldt 1895 (J. reine angew. Math. 114) positivity of argument increments and earlier N(T) bound; Hadamard product of xi

**Techniques.** argument principle; Stieltjes/Stirling expansion of log Gamma; Hadamard product of xi; monotonicity of argument of linear factors; window counting with free parameter and numerical optimisation

## Context and interpretation

**Importance and obstacle overcome.** Completes the proof of Riemann's 1859 asserted formula N(T)=(T/2pi)log(T/2pi)-T/2pi+O(log T) (Riemann's claim for the number of zeros), with an explicit error. The obstacle was Mangoldt's 1895 error term of order (log T)^2: the new idea is a more efficient counting of zeros in short windows via the monotone growth of arguments and an optimisation of the window length, which brings the error to order log T.

**Relation to prior work.** Improves Mangoldt 1895 (J. reine angew. Math. 114), from 0.34 (log T)^2 + 1.35 log T + 2.58 to 0.432 log T + 1.917 log log T + 13.08 for T>28.558.

**Limitations and open questions.** Unconditional but only gives the main term to O(log T): no information on arg zeta on the half-line in finer terms. No relation to RH beyond counting; modern explicit versions (Backlund, Rosser, Trudgian, Platt-Trudgian) are far sharper (O(log T) constants 0.11 or 0.1038). Basis for N(T) count was OCR-only so constants should be cross-checked against the printed page.

**Ideas in remarks/appendices/abandoned paths.** The parameter-optimised window device with k~0.675 (p. 16-17) as an early example of optimising a smoothing/window parameter in an explicit zero-counting bound.

## Research potential

- **Hypotheses that might be weakened.** The technique does not use RH; the threshold T>28.558 and the constants come from numerical optimisation which could be redone with modern zero data (known zeros up to 3e12) to give a sharp small-T explicit N(T).
- **Generalizations.** Window-counting / argument-increment method to Dirichlet L-functions and Dedekind zeta (counting zeros with explicit constants), cf. Rademacher, Trudgian explicit bounds for L(s,chi).
- **Candidate connections.** Provenance/history node: Mangoldt 1905 is the origin of the explicit Riemann-von Mangoldt formula that all later explicit zero-counting (Backlund 1914, Rosser 1941, Trudgian 2014) refines; connects to the Rosser-Schoenfeld explicit formula in CAND-02344 (inputs (8)-(9)).
- **Reusable lemmas.** The window-counting inequality for zeros in an interval of length 2k via the positive increment of arg of linear factors (pp. 11-16) is a reusable local-to-global counting device.
- **Possible experiments.** Verify the stated inequality numerically for T in [28.558, 10^4] using the actual zeros; re-optimise k with modern constants; compare with Backlund's 0.137 log T + 0.443 log log T + 4.350.
- **Risks / barriers.** Historical; the method's O(log T) cannot be improved without the S(T) improvements under RH (Littlewood O(log T/log log T)).

## Audit notes (Level 1 reader)

basis: partial OCR full text only. The OCR of page 1 and the key formulae (the printed numerical constants 0.43200, 1.91662, 13.07873, and 0.34/1.35/2.58 for the old bound) is noisy; the displayed main term formula was not legible in the OCR so it was filled from the well known statement of the result (title/zbMATH triage) and the structure of the proof (Theta_1 = (T/2)log(T/2pi)-T/2...). Exact placement of log vs log log terms in the final inequality should be checked against a clean scan.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00089`; harvest queries: msc_11M06, msc_11M26.
- Triage decision: include — Von Mangoldt 1905 proof of the zero-counting asymptotic.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
