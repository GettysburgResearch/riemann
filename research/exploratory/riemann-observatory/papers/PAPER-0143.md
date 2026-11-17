# PAPER-0143 — Sur la distribution des nombres premiers.

| Field | Value |
|---|---|
| Authors | Littlewood, J. E. |
| Year / stratum | 1914 / S2 |
| Venue | C. R. 158, 1869-1872 (1914). |
| Identifiers | zbMATH [45.0305.01](https://zbmath.org/?q=an:45.0305.01) |
| MSC |  |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://archive.org/download/comptes-rendus-hebdomadaires-academie-des-sciences_1914-06-22_158_25/comptes-rendus-hebdomadaires-academie-des-sciences_1914-06-22_158_25_djvu.txt |
| Selection | score 2.481, in-pool citations 73, seed lists 2, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Narrow the gap between Schmidt's Omega result for pi(x)-Li(x) and the upper bound O(sqrt(x) log x) under RH, by proving (assuming RH, otherwise known) that psi(x)-x and pi(x)-Li(x) both change sign and attain size at least K sqrt(x) log log log x (resp. divided by log x) for arbitrarily large x. The note announces results with a sketch of proof (Kronecker + a lemma on a Dirichlet-type series).

**Historical motivation.** Schmidt (1903) proved pi(x)-Li(x) changes sign infinitely often with size at least sqrt x / log x; Gauss's numerical observation that Li(x)>pi(x) for small x suggested the opposite. Littlewood used Kronecker's theorem (previously exploited by Bohr for Dirichlet series) to prove that pi(x)-Li(x) takes both signs and to sharpen the Omega estimate.

### Main results

- **THM-PAPER-0143-1** (Eq. (1)-(3) of the Note, theorem, scope: asymptotic; CR 158 (1914), p. 1869, section 1). Schmidt proved \psi(x)-x=\Omega_\pm(\sqrt x) (i.e. there is K>0 with |\ldots|>K\sqrt x for arbitrarily large x, eq. (1)); under RH \psi(x)-x=O(\sqrt x\log^2 x) and \pi(x)-\mathrm{Li}(x)=O(\sqrt x\log x) (eq. (2), as printed: O(sqrt(x) log x)). Littlewood announces: \psi(x)-x=\Omega_\pm\big(\sqrt x\,\log\log\log x\big), \pi(x)-\mathrm{Li}(x)=\Omega_\pm\big(\sqrt x\log\log\log x/\log x\big), i.e. for arbitrarily large x each difference exceeds K\sqrt x\log\log\log x (resp. divided by \log x) in absolute value (eq. (3): K\,\sqrt{x}\,\log\log\log x/\log x). He proves the statement assuming RH ('Dans le cas contraire, on sait deja plus').
- **THM-PAPER-0143-2** (Section 2 Lemma, lemma, scope: asymptotic; Section 2, p. 1870). Let \eta_0>0 and S(\ldots)=\sum (\ldots) an almost periodic-type sum over zeros \rho=1/2+i\gamma_n; there exist values of the variable such that the real part of the sum exceeds a given bound with positive density, so that the extremal oscillation of the trigonometric series \sum\ldots can be forced to be at least \log\log\log-large by a quantitative Kronecker choice of arguments. (Statement is largely garbled in OCR: it asserts existence of values for which two inequalities hold simultaneously.)

### Principal lemmas

- **THM-PAPER-0143-L1** (Section 2 (Lemme); Section 2, pp. 1870-1871). For a positive number n_0, a sum S(\ldots)=\sum_n(\ldots)\ldots of the oscillating form \sum e^{i\gamma_n\log x}/\rho_n weighted over zeta zeros takes, for suitable arguments, values larger than a stated positive quantity; the first inequality is proved by an elementary argument using formula (9) as \varepsilon\to0, the second by a Kronecker-theorem argument (as used by H. Bohr in Dirichlet series). — *Role:* Core of the Omega result: converts the zero sum into an oscillating series with arbitrary phases; log log log x is the growth of the 'effective number of independent oscillations' obtainable from the zeros.
- **THM-PAPER-0143-L2** (Section 3 (the closing contradiction); Section 3, pp. 1871-1872). Using Kronecker's theorem (as exploited by Bohr), choose T such that \|\gamma_n T/2\pi\|<\ldots simultaneously for finitely many n (x_n=\|x-[x]\| distance to nearest integer); with (6),(7) a curve C: \sigma=\xi(n) (positive, continuous, decreasing) exists on which the Dirichlet-type function is bounded uniformly in the domain 0\le\xi\le\xi(n); a contradiction with the lemma of section 2 (extended to this domain) shows the assumed one-sided bound is false. — *Role:* Argument by contradiction giving the sign changes and the size sqrt(x) log log log x.

### Proof architecture

Section 1 states the problem relative to Schmidt's (1) and the RH upper bound (2) and announces (3), proved assuming RH (otherwise zeros off the line already give more). Writes n=log x and a Mellin-type transform of the series with parameters (5)-(8). Section 2: a lemma on a sum over zeros with a positive-density set of arguments; one inequality by an elementary argument as epsilon->0, the other via Kronecker. Section 3: Kronecker's theorem (T with ||gamma_n T /2 pi|| small) used to align phases; existence of a contour C in the s-plane where the auxiliary function g(z)=O(1), with contradiction against the lemma. Imported: Schmidt 1903 Omega result, Kronecker theorem (via H. Bohr), von Mangoldt explicit formula, Landau results on zeros.

**Techniques.** Kronecker's theorem on simultaneous approximation of the zero ordinates (via Bohr); Phragmen-Lindelof-type contour argument; oscillation of trigonometric sums over zeta zeros; proof by contradiction on the hypothesised bound; explicit-formula reduction of pi(x)-Li(x) to psi(x)-x

## Context and interpretation

**Importance and obstacle overcome.** Shows that the Riemann-hypothesis bound O(sqrt x log x) is nearly sharp: pi(x)-Li(x) is not o(sqrt x/log x * logloglog x) and changes sign infinitely often, resolving Gauss's observation in the opposite direction (Li(x)>pi(x) for all computed x) up to Littlewood's theorem of sign changes of pi(x)-Li(x) (no explicit x). Obstacle overcome: producing arbitrarily large simultaneous oscillation of infinitely many cosine terms e^{i gamma log x} of the explicit formula using Kronecker's theorem when the gamma are not known to be rationally independent.

**Relation to prior work.** Improves Schmidt (Math. Ann. 57, 1903: Omega_pm(sqrt x / log x...)), complements the RH upper bound of von Koch (CAND-00002); announced as a sketch whose full proof appeared with Hardy in Acta Math. 41 (1918); builds on Bohr's use of Kronecker and on Landau's theory of zeros.

**Limitations and open questions.** Only a sketch in a 4-page Comptes Rendus note (no details of the lemma; the full proof was given later in Acta Math. 41 (1918, Hardy-Littlewood) and in Littlewood's own papers). The sharper Omega_pm(sqrt x log log log x) was subsequently improved/shown near optimal conditional on RH (Montgomery 1980 conjectured sqrt x (loglog logx)^2 growth, Gonek-Montgomery). The proof assumes RH for the main statement.

## Research potential

- **Hypotheses that might be weakened.** RH is assumed to place all zeros at 1/2+i gamma_n; replacing it by a one-sided region sigma<=Theta would give Omega_pm(x^{Theta}...) statements; the Kronecker step uses only finitely many gamma_n at a time, so a version with only partial independence (e.g., under linear independence of the gammas replaced by weaker conditions) is a natural weakening.
- **Generalizations.** Same method gives Omega_pm for Dirichlet L-functions (prime races, Chebyshev's bias) and for primes in arithmetic progressions; log log log x arises from the amount of Kronecker control, replaced by (log log log x)^2 under strong conjectures (Montgomery).
- **Candidate connections.** With Koch (CAND-00002) it gives the pair (RH upper bound sqrt x log x, Omega bound sqrt x logloglog x/ log x): the gap is exactly the 'log x / logloglog x' region studied by Montgomery's conjecture and the Gonek-Montgomery results; connected to Robin-type inequalities via the same error term for theta and psi; and to the Rubinstein-Sarnak prime race framework.
- **Reusable lemmas.** The Kronecker/Bohr step as a template for forcing large oscillation of sum over zeros with a quantitative T; the contour-C contradiction argument.
- **Possible experiments.** Compute the explicit formula partial sum sum_{|gamma|<=Gamma} x^{i gamma}/rho for x in a range up to e^{10^4} with the first 10^5 zeros and observe the size of max/min versus sqrt x logloglog x (sanity on the claimed size).
- **Risks / barriers.** The result is an Omega bound, so it cannot be turned into an upper bound; improvement beyond logloglog needs strong independence hypotheses on the zeta zeros (Montgomery's loglog/ logloglog conjecture).

## Audit notes (Level 1 reader)

OCR for formulas (3)-(9) is almost unreadable; the displayed inequality labelled (3) in the OCR (Omega statement for psi) and the text 'Je vais demontrer (4)' show a numbering inconsistency in the OCR/printing (the announced inequality is called (3) in the display but (4) in the text). The triage description matches the statements read, but the precise form of the K constant and logs in eq. (3) could not be verified from the OCR. The proof is only sketched; the full arguments are not in this note. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00161`; harvest queries: citation_expansion.
- Triage decision: include — Littlewood's proof that pi(x)-Li(x) changes sign infinitely often.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
