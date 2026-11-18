# PAPER-0079 — Highly composite numbers. Annotated by Jean-Louis Nicolas and Guy Robin

| Field | Value |
|---|---|
| Authors | Ramanujan, Srinivasa |
| Year / stratum | 1997 / S4 |
| Venue | Ramanujan J. 1, No. 2, 119-153 (1997). |
| Identifiers | zbMATH [0917.11043](https://zbmath.org/?q=an:0917.11043) · DOI [10.1023/A:1009764017495](https://doi.org/10.1023/A:1009764017495) |
| MSC | 11N25, 11-03, 11M26, 01A60, 11N56 |
| Families | C |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/1211.6944 |
| Selection | score 4.4409, in-pool citations 20, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** basis: partial. Ramanujan's unpublished HCN Part 2 asks for the maximal order of sigma_{-s}(n) = sum_{d|n} d^{-s} using generalized (superior) highly composite numbers, and what that gives under RH. Nicolas and Robin annotated and corrected the text.

**Historical motivation.** Part 2 was suppressed in 1915 for paper shortage; rediscovered by Berndt and Nicolas at the 1987 Urbana-Champaign conference; published in 1997 in Ramanujan J. 1.

### Main results

- **THM-PAPER-0079-1** (Ramanujan's Theorem (as formulated by Nicolas-Robin in Note 71; quoted in arXiv:1211.6944 section 1), theorem (conditional), scope: asymptotic; HCN Part 2, p. 133 and formula (382), Note 71; second-hand via arXiv:1211.6944 section 1). If RH holds, then for $n_0$ large enough, $n>n_0\Rightarrow \sigma(n)/n< e^{\gamma}\log\log n$. The proof uses $\limsup_{n\to\infty}(\sigma_{-1}(n)-e^\gamma\log\log n)\sqrt{\log n}\le -e^\gamma(2\sqrt2-4-\gamma+\log 4\pi)=-1.393\ldots<0$, which is the corrected form of Ramanujan's formula (382). *Conditional on:* RH.
- **THM-PAPER-0079-2** (Ramanujan's bound for 1/2<s<1 (second-hand), theorem (conditional), scope: asymptotic; as quoted in arXiv:1211.6944 section 1). Under RH, for $1/2<s<1$ and all sufficiently large $n$: $\sigma_{-s}(n)\le|\zeta(s)|\exp\Bigl\{\mathrm{Li}((\log n)^{1-s})-\frac{2s(2^{2s-1}-1)(\log n)^{1/2-s}}{(2s-1)\log\log n}-\frac{s}{\log\log n}\sum_\rho\frac{(\log n)^{\rho-s}}{\rho(\rho-s)}+O\bigl(\frac{(\log n)^{1/2-s}}{(\log\log n)^2}\bigr)\Bigr\}$. This is the survey's transcription, and the exact constants were not checked against the paper. *Conditional on:* RH.
- **THM-PAPER-0079-3** (Robin's Theorem (imported, not in this paper), imported theorem, scope: global; survey section 1). RH holds iff $\sigma(n)<e^\gamma n\log\log n$ for all $n>5040$. It is the Robin 1984 theorem that the annotations cite.

### Key definitions

- sigma_{-s}
- generalized highly composite number
- generalized superior highly composite number

### Principal lemmas

- **THM-PAPER-0079-L1** (Definition of generalized (superior) highly composite number; via survey, section 1). $N$ is generalized highly composite if $\sigma_{-s}(N')<\sigma_{-s}(N)$ for all $N'<N$. It is generalized superior if $\sigma_{-s}(N)/N^\varepsilon\ge\sigma_{-s}(N')/N'^\varepsilon$ for $N'<N$ and $>$ for $N'>N$. At $s=1$ these are superabundant and colossally abundant numbers. — *Role:* extremal family on which sigma_{-s} is controlled
- **THM-PAPER-0079-L2** (Prime factorization of generalized SHCN; via survey, section 1). With $x_r^{\varepsilon}=\frac{1-x_r^{-s(r+1)}}{1-x_r^{-sr}}$, one has $N=\prod_{r\le R}e^{\vartheta(x_r)}$ and $\sigma_{-s}(N)=\prod_r\prod_{p\le x_r}\frac{1-p^{-s(r+1)}}{1-p^{-sr}}$. — *Role:* reduces the estimate of sigma_{-s}(N) to sums over primes up to x_r
- **THM-PAPER-0079-L3** (Prime sum estimate (Ramanujan p.133); via survey, section 1). $\sum_{p\le x}\frac{\log p}{p^s-1}$ is expressed through $\int (x-\vartheta(x))\,dx$-type integrals, using the explicit formula $x-\vartheta(x)=\sqrt x+x^{1/2}\cdot\ldots+\sum_\rho x^\rho/\rho+\ldots$. This is where RH enters. — *Role:* input of RH

### Proof architecture

From the survey only: (1) extremal numbers with a parametric factorization; (2) an estimate of sigma_{-s} on them via sums of log p/(p^s-1); (3) the explicit formula, with RH controlling the zero sum; (4) deduction for all n, then s to 1. Nicolas found a sign error in Ramanujan's manuscript that had hidden Robin's equivalence.

Dependency edges: CAND-00778 → Robin 1984 (annotations cite as proving the equivalence at n0=5040)

**Imported results.** Mertens' theorem; explicit formula for theta(x); Robin 1984 (J. Math. Pures Appl.)

**Techniques.** generalized colossally abundant (superior highly composite) numbers; explicit formula for theta(x) under RH; Mertens-type estimates

## Context and interpretation

**Importance and obstacle overcome.** It shows that Ramanujan had an RH-conditional form of the Gronwall/Robin bound for sigma, and the annotations correct a sign error that had obscured the link with Robin's criterion. This is second-hand.

**Relation to prior work.** Continues HCN Part 1 (Proc. LMS 1915); anticipates Robin (1984) in spirit, but Robin was independent.

**Limitations and open questions.** Under RH the bound is only for n>n0 with n0 not explicit. The equivalence at n0=5040 is Robin's theorem, not Ramanujan's. The 1997 text itself was not seen.

**Ideas in remarks/appendices/abandoned paths.** The text contains Ramanujan's sections on s in (0,1), not examined here.

## Research potential

- **Hypotheses that might be weakened.** Check whether a one-sided zero-free region instead of RH gives an unconditional-in-region version of the corrected formula (382).
- **Generalizations.** Parameter s in (1/2,1): the sigma_{-s} analogue of Robin's criterion. See also Caveney-Nicolas-Sondow GA1/GA2 reformulations.
- **Candidate connections.** Robin-type criteria (Lagarias, sigma(n)<=H_n+exp(H_n)log H_n) and Nicolas' phi criterion.
- **Reusable lemmas.** Parametric factorization of generalized SHCN.
- **Possible experiments.** Numerically verify the constant 2sqrt2-4-gamma+log 4pi and the corrected formula (382) on colossally abundant numbers with 1e3 to 1e6 prime factors.
- **Risks / barriers.** The explicit formula needs RH for the error term. Without RH, only a conditional exponent in sigma_{-s} follows.

## Audit notes (Level 1 reader)

The survey records an error of sign in Ramanujan's manuscript (corrected by Nicolas-Robin). The 1997 text itself was not inspected.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00778`; harvest queries: msc_11M26, msc_11N56_rh.
- Triage decision: include — Ramanujan's highly composite numbers, with RH-conditional bounds underlying Robin.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
