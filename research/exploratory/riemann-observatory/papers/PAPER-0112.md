# PAPER-0112 — The \(n\)-level correlations of zeros of the zeta function

| Field | Value |
|---|---|
| Authors | Rudnick, Zeév; Sarnak, Peter |
| Year / stratum | 1994 / S4 |
| Venue | C. R. Acad. Sci., Paris, Sér. I 319, No. 10, 1027-1032 (1994). |
| Identifiers | zbMATH [0837.11047](https://zbmath.org/?q=an:0837.11047) |
| MSC | 11M06 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://www.math.tau.ac.il/~rudnick/papers/RudnickSarnakCRAS1994.pdf |
| Selection | score 4.1597, in-pool citations 10, seed lists 0, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** For the normalized zeros of zeta, \tilde\gamma_j=(\gamma_j\log\gamma_j)/2\pi, do the n-level correlations R_n agree with Dyson's GUE determinant W_n(x)=\det K(x_i-x_j), K(x)=\sin\pi x/\pi x, at least for test functions whose Fourier transform has restricted support? Announcement of the Duke paper (CAND-00720); also states the extension to principal GL(m) L-functions.

**Historical motivation.** Montgomery 1973 pair correlation and Odlyzko's numerics supported the GUE hypothesis; Hejhal had just done n=3. This Note extends the theory to all n with a uniform method.

### Main results

- **THM-PAPER-0112-1** (Theorem 1.1 (smoothed n-level correlations, unconditional), theorem, scope: asymptotic; Section 1, Theorem 1.1 (p. 1030)). Let f satisfy TF1 (symmetric), TF2 ($f(x+t(1,\dots,1))=f(x)$) and TF3 (rapid decay on $\sum x_j=0$), with $\hat f$ supported in $\sum_{j}|\xi_j|<2$. Let $g\in C_c^\infty(\mathbb R)$, $h(r)=\int g(u)e^{iru}du$. Then as $T\to\infty$, $R_n(T,f,h)=\sum^{\ne}_{j_1..j_n}h(\gamma_{j_1}/T)\cdots h(\gamma_{j_n}/T)f(\tfrac L{2\pi}\gamma_{j_1},\dots,\tfrac L{2\pi}\gamma_{j_n})\sim \frac{1}{2\pi}T\log T\int h(r)^n dr\int_{\mathbb R^n}f(x)W_n(x)\delta(\tfrac{x_1+\dots+x_n}{n})dx$, with $L=\log T$ (formula reconstructed; displayed equation lost in OCR). No RH assumed (sums over zeros with complex ordinates).
- **THM-PAPER-0112-2** (Theorem 1.2 (n-level correlations of the zeros, under RH), theorem, scope: asymptotic; Section 1, Theorem 1.2 and Remark 2 (p. 1030)). Assume RH. For f with TF1-3 and $\mathrm{supp}\,\hat f\subset\{\sum|\xi_j|<2\}$, $R_n(B_N,f)\to\int_{\mathbb R^n}f(x)W_n(x)\delta(\tfrac{x_1+\dots+x_n}n)dx$ as $N\to\infty$ (GUE n-level correlations). n=2 is Montgomery's theorem; n=3 is announced by Hejhal in different form. *Conditional on:* RH.
- **THM-PAPER-0112-3** (Remark 3 (GL(m) extension), announcement, scope: asymptotic; Section 1, Remark 3). The same GUE n-level correlation holds for principal L-functions of cuspidal automorphic representations of GL(m)/Q (proof deferred to the Duke paper, with support restriction $\sum|\xi_j|<2/m$ there). *Conditional on:* RH for Theorem 1.2-type unsmoothed version.

### Key definitions

- n-level correlation sum $R_n(B_N,f)=\frac{n!}{N}\sum_{S\subset B_N,|S|=n}f(S)$
- test function conditions TF1-3
- smoothed correlation $R_n(T,f,h)$
- $W_n(x)=\det(K(x_i-x_j))$

### Principal lemmas

- **THM-PAPER-0112-L1** (Smooth explicit formula (2.1); Section 2). Smoothed Riemann explicit formula relating $\sum_\rho h(\gamma)$ to sums over prime powers $\Lambda(n)n^{-1/2}g(\pm\log n)$. — *Role:* Converts n-fold sums over zeros into n-fold sums over primes; avoids RH in Theorem 1.1.
- **THM-PAPER-0112-L2** (Proposition 2.1 (combinatorial sieving, partitions); Section 2, p. 1031-1032). Identity relating the all-indices sums $C_F$ (variables in a block of a set partition identified) via Moebius inversion on the partition lattice to the GUE determinant's Fourier transform; precise formula lost in OCR. — *Role:* Passes from unrestricted sum $C_n$ (over all indices) to distinct-index sum $R_n$.
- **THM-PAPER-0112-L3** (Proposition 2.2 (identity of piecewise linear functions); Section 2, p. 1032). Identity coupling the pairing structure of the prime sums (diagonal pairs) with the cycle structure of the determinant defining $W_n$; proved by Spitzer's combinatorial lemma. — *Role:* Core combinatorial step producing the sine-kernel determinant from primes.

### Proof architecture

Smooth explicit formula turns the n-point zero sum into a sum over n-tuples of primes; multiplying out, the main term (lengthy computation using $\sum|\xi_j|<2$) comes from diagonal pairings (prime-power coincidences $n_i=n_j$ via unique factorization), giving $C_n(f,T)\sim N\int \hat f C_O$. Combinatorial sieving over set partitions removes the diagonal-index terms to pass to distinct indices, and Prop 2.2 (via Spitzer) identifies the result with $\hat W_n$. Theorem 1.2 follows from 1.1 by approximating indicator cutoffs under RH. Only an outline is given; full details deferred to the Duke paper.

Dependency edges: CAND-00864 → CAND-00720 (announcement of; full proofs and GL(m) generalization there); CAND-00864 → CAND-00743 (n=3 case independently treated by Hejhal; cited in Remark 2); CAND-00750 → CAND-00864 (Bogomolny-Keating heuristic extends beyond support restriction (acknowledged in Remark 1))

**Imported results.** Montgomery pair correlation (n=2) as the special case; Dyson's determinantal formula for GUE correlations (J. Math. Phys. 3, 1962); Spitzer 1956 combinatorial lemma, Trans. AMS 82

**Techniques.** smooth explicit formula; diagonal pairing of prime sums; Moebius inversion on partition lattice; Spitzer's combinatorial lemma (cyclic rotation of random walks); Fourier analysis of Dyson's determinant

## Context and interpretation

**Importance and obstacle overcome.** First all-n verification of GUE statistics for zeta zeros in a limited range. Obstacle: showing that the determinantal structure of GUE emerges from sums over primes; solved by the diagonal-pairing combinatorics plus Spitzer.

**Relation to prior work.** Generalizes Montgomery (n=2) and Hejhal (n=3, preprint, RH, different form). Bogomolny-Keating are acknowledged as having a heuristic (via Hardy-Littlewood) beyond the support restriction. Companion/successor: full proof in Duke 81 (1996).

**Limitations and open questions.** Support restriction $\sum|\xi_j|<2$ is not removed (conjecturally unnecessary); only a statement about smoothed/Fourier-restricted statistics, no information on nearest-neighbour spacings (needs unrestricted support); note gives only outline.

**Ideas in remarks/appendices/abandoned paths.** Remark 2 notes Theorem 1.1 avoids RH by working with smooth h, a point reused to treat L-functions without RH.

## Research potential

- **Hypotheses that might be weakened.** The support condition $\sum|\xi_j|<2$ is the barrier; beyond it off-diagonal terms (Hardy-Littlewood-type prime correlations) contribute equally. Extending needs Hardy-Littlewood tuples (as in Bogomolny-Keating) or averaged versions.
- **Generalizations.** GL(m), families; already announced.
- **Candidate connections.** Pair-correlation-based statements about simple zeros / small gaps (Montgomery-Odlyzko type) use only n=2; n>2 gives higher-order constraints on gap structure but remains inside the Fourier-restricted regime.
- **Reusable lemmas.** Prop 2.1 and 2.2 (partition-lattice Moebius inversion and Spitzer identity) are reusable for any problem that needs distinct-index sieving from all-index sums.
- **Possible experiments.** Numerically evaluate $R_n(T,f,h)$ for n=3,4 with Fourier support inside and outside $\sum|\xi|<2$ on Odlyzko's zero tables to see onset of deviations from the diagonal prediction.
- **Risks / barriers.** Does not imply RH (RH enters as an assumption for Thm 1.2); the result is local/statistical and cannot decide global functionals.

## Audit notes (Level 1 reader)

OCR of the displayed formulas is missing in the inspected text, so exact normalization in Theorems 1.1/1.2 was reconstructed from the Duke paper; no inconsistencies noticed in readable portions.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00864`; harvest queries: kw_RH_any, kw_pair_correlation, msc_11M06.
- Triage decision: include — Landmark n-level correlation result for zeros.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
