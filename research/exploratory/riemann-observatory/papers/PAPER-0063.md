# PAPER-0063 — Analogues of the Robin-Lagarias criteria for the Riemann hypothesis

| Field | Value |
|---|---|
| Authors | Washington, Lawrence C.; Yang, Ambrose |
| Year / stratum | 2021 / S6 |
| Venue | Int. J. Number Theory 17, No. 4, 843-870 (2021). |
| Identifiers | zbMATH [1472.11236](https://zbmath.org/?q=an:1472.11236) · DOI [10.1142/S1793042121500111](https://doi.org/10.1142/S1793042121500111) · arXiv [2008.04787](https://arxiv.org/abs/2008.04787) |
| MSC | 11M26, 11A25 |
| Families | C |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/2008.04787 |
| Selection | score 4.5146, in-pool citations 4, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Can Robin's criterion sigma(n) < e^gamma n loglog n and Lagarias's criterion be replaced by criteria restricted to odd integers with the constant e^gamma/2, and how do the prime factorization and squarefreeness of n affect Robin's inequality?

**Historical motivation.** Robin (1984) and Lagarias (2002) give arithmetic equivalents of RH. Robin's 1983 modular analogues showed that f_{4,1} exceeds its limsup infinitely often while f_{4,3} does not (under GRH for Q(i)). The authors asked what the interplay does for odd n, where limsup is e^gamma/2.

### Main results

- **THM-PAPER-0063-1** (Theorem 1.2 = Theorem 3.6, theorem, scope: global; Sec 1, Sec 3). RH is equivalent to: $\sigma(n)/(n\log\log n)<e^{\gamma}/2$ for all odd $n\ge c_0=18565284664427130919514350125=3^4\cdot5^3\cdot7^2\cdot11\cdot13\cdots67$.
- **THM-PAPER-0063-2** (Theorem 1.3 = Theorem 4.6, theorem, scope: global; Sec 1, Sec 4). RH is equivalent to $\sigma(n)\le \frac{3n}{\log n}+\exp(H_n')\log H_n'$ for all odd $n\ge3$, where $H_n'=2H_n-H_{2n}=\sum_{k=1}^{n}1/k-\sum_{k=n+1}^{2n}1/k\cdot(-1)\ldots$, as defined by $H_n'=2\sum_{k\le n}1/k-\sum_{k\le 2n}1/k$.
- **THM-PAPER-0063-3** (Theorem 5.1, theorem, scope: global; Sec 5.1). Unconditionally, odd squarefree $n\ge4849845$ satisfy $\sigma(n)/(n\log\log n)<e^{\gamma}/2$.
- **THM-PAPER-0063-4** (Proposition 5.3, proposition, scope: asymptotic; Sec 5.1). As n runs through odd squarefree integers, $\limsup \sigma(n)/(n\log\log n)= 4e^{\gamma}/\pi^{2}$ (read from the text extraction).
- **THM-PAPER-0063-5** (Theorem 5.4, theorem, scope: global; Sec 5.3). If $n=2^k m$ with $m$ odd squarefree and $n\ge841$, then Robin's inequality $\sigma(n)<e^{\gamma}n\log\log n$ holds, unconditionally. This extends the Chandee-type/Choie et al. result for squarefree n>30.
- **THM-PAPER-0063-6** (Corollary 5.7 / Prop 5.11, corollary, scope: global; Sec 5.4). If p does not divide n, then $f(p^k n)<f(n)$ under an explicit condition relating $\log n$ and $p^k$ (Thm 5.6, so that the exponent of 2 maximizing $f(2^m n)$ is determined by the equation $(\log xn)(\log\log xn)-2x+1=0$ with $x=2^k$). Prop 5.11 shows the optimal k increases with n.

### Principal lemmas

- **THM-PAPER-0063-L1** (Lemma 2.2 (from Alaoglu-Erdos); Sec 2). For $0<\epsilon\le -1+\log_3 4$, odd colossally abundant numbers are $N=\prod_{p\ge3}p^{\alpha_p(\epsilon)}$ with $\alpha_p(\epsilon)=\lfloor\log(p^{1+\epsilon}-1)-\log(p-1))/\log p\rfloor-1$ (for 1+eps exponents as in (2.1)). — *Role:* explicit parametrisation of odd CA numbers, the extremal set
- **THM-PAPER-0063-L2** (Lemma 3.2 / 3.3; Sec 3). For odd CA N with parameters $x_1>x_2$: if $x_2\ge347$ then $\log N>\theta_0(x_1)+0.998x_2$; if $x_1\ge120409$ then $\log\log N>\log\theta(x_1)\exp(0.99154\,x_2/(x_1\log x_1))$. — *Role:* effective Chebyshev-type estimates controlling log log N
- **THM-PAPER-0063-L3** (Lemma 3.4; Sec 3). If an odd n violates the odd analogue of Robin's inequality and $N\le n\le N'$ are consecutive odd CA numbers, then N or N' violates it. — *Role:* reduces the verification to odd colossally abundant numbers (as in Robin's [13, Sec 3, Prop 1])
- **THM-PAPER-0063-L4** (Proposition 3.5; Sec 3). Assuming RH, $\sigma(n)/(n\log\log n)<e^\gamma/2$ for all odd $n\ge c_0$; verified by computer for odd CA numbers with $61<x_1<120409$ (actually up to $x_1\le10^6$) and analytically for $x_1\ge120409$ using Robin-style explicit bounds on theta(x) under RH. — *Role:* forward direction of Thm 1.2
- **THM-PAPER-0063-L5** (Lemma 4.4 / Lemma 4.5; Sec 4). 4.4: assuming RH, if odd n violates the Lagarias-analogue and $N_1\le n\le N_2$ with $N_1\ge490$ consecutive odd CA, then N_1 or N_2 violates it. 4.5: if RH is false there are $0<\beta<1/2$, $C>0$ with $\sigma(N)\ge \frac{e^\gamma}{2}N\log\log N+CN\log\log N/(\log N)^\beta$ for infinitely many odd CA N. — *Role:* reduction and the reverse direction for the Lagarias analogue

### Proof architecture

Forward direction: use Lemma 3.4 to reduce to odd colossally abundant numbers. Check them by computer up to x1 < 120409 and analytically beyond (Lemmas 3.1-3.3 giving Chebyshev-type bounds under RH). The cutoff c_0 is the least odd CA number past the last violator N = 3^4 5^3 7^2 11...61. Reverse direction: if RH fails then by Robin f(M)>e^gamma infinitely often for even CA M=2^k N, and a bound sigma(2^k)/2^k<2 gives sigma(N)/(N loglog N)>e^gamma/2 for large N, contradicting the hypothesis. The Lagarias analogue is the same with Lemma 4.4/4.5, by mimicking Lagarias's proof. Section 5 treats squarefree n and general factorization via multiplicativity.

**Imported results.** Robin 1984 (RH iff sigma(n)<e^gamma n loglog n, n>5040) [13]; Robin 1983 (sup-limits over arithmetic progressions mod 4, Thm 1.1) [14]; Lagarias 2002 (sigma(n)<=H_n+exp(H_n)log H_n) [10]; Alaoglu-Erdos 1944 (CA numbers) [1]; Robin's p. 205 result f(M)=e^gamma(1+Omega_pm((log M)^{-beta})) if RH false; Explicit Chebyshev bounds under RH (Schoenfeld type)

**Techniques.** colossally abundant numbers (Alaoglu-Erdos); Robin's explicit bounds on theta(x) under RH; computer verification of finitely many odd CA numbers; reduction from all n to CA numbers; multiplicativity of sigma and Mertens-type products

## Context and interpretation

**Importance and obstacle overcome.** Gives a verified-finite-check reformulation of RH using odd numbers only, with a sharper constant, and clarifies why the two competing classes (1 mod 4 and 3 mod 4 primes) cause a large cutoff. The obstacle was handling odd CA numbers, where the exponent of 2 is missing, and finite check up to x1<120409.

**Relation to prior work.** Odd-integer analogues of Robin [13] and Lagarias [10], extending Robin's [14] progression analysis, and squarefree results of Choie-Lichiardopol-Moree-Sole and Moree's remarks on the constants.

**Limitations and open questions.** The forward direction of the odd criterion still uses RH, so it is an equivalence and unconditional only in the reverse. The proof of equivalence is not new in spirit (Robin 1984 transposed to odd integers), and c_0 is huge. Whether the same holds with other constants or for other residue classes is open. Section 5 results are unconditional but only for restricted n (squarefree or 2^k times squarefree).

## Research potential

- **Hypotheses that might be weakened.** Replace odd by integers coprime to a fixed finite set of primes S, with constant e^gamma prod_{p in S}(1-1/p); the proof shape (reduce to CA numbers coprime to S) seems to carry over.
- **Generalizations.** Analogues for sigma_k, for the Dedekind psi function, or for the Nicolas-type phi-version restricted to odd integers. Sharpen c_0 via the actual last odd violator.
- **Candidate connections.** Robin arithmetic programme: the 'Robin-Lagarias' cut-offs plus Robin's explicit-bound tools tie into the signed native/Mobius cancellation programme through the explicit psi(x) error under RH.
- **Reusable lemmas.** Lemma 3.4 and Lemma 4.4 (reduction to odd CA numbers) and Lemma 3.2-3.3 (explicit log N bounds).
- **Possible experiments.** Recompute the violators of f(n)<e^gamma/2 among odd CA numbers up to x1=10^6 with interval arithmetic to check c_0 and the stated last violator 3^4 5^3 7^2 11...61; test whether the odd-CA ladder matches Robin's even one.
- **Risks / barriers.** Finite computations are not a substitute for the analytic step; also the equivalence relies on the Robin 1984 trichotomy, so nothing here bypasses RH.

## Audit notes (Level 1 reader)

Read from lossy text. Prop 5.3 constant read as 4e^gamma/pi^2 should be checked against the PDF. Prop 3.5 depends on a computer check (Sec 6, not replayed) with ordinary floating point, and the paper does not state a rounding contract or provide certified arithmetic; the correctness of c_0 relies on that. Theorem 1.3 definition of H_n' text-extracted as 2H_n-H_{2n}; consistent. No computational artifact or hash is bound to the check.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01842`; harvest queries: kw_RH_any, kw_robin, msc_11M26, arxiv_rh_abs, arxiv_rh_ti, arxiv_robin.
- Triage decision: include — New equivalents of Robin/Lagarias type criteria.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
