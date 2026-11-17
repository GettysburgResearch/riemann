# PAPER-0094 — On Robin's inequality

| Field | Value |
|---|---|
| Authors | Luca, Florian; Solé, Patrick |
| Year / stratum | 2025 / S7 |
| Venue | Integers 25, Paper No. A8, 7 p. (2025). |
| Identifiers | zbMATH [1581.11103](https://zbmath.org/?q=an:1581.11103) · DOI [10.5281/zenodo.14907242](https://doi.org/10.5281/zenodo.14907242) |
| MSC | 11N56, 11A25 |
| Families | C |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://doi.org/10.5281/zenodo.14907242 (PDF z8.pdf, Integers 25 (2025) #A8) |
| Selection | score 4.3142, in-pool citations 1, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** How sparse is the set of n>7! violating Robin's inequality sigma(n)<e^gamma n log log n (a finite set under RH)? Give explicit unconditional upper bounds for NR(x)=#{7!<n<=x: sigma(n)>=e^gamma n log log n}.

**Historical motivation.** Robin's criterion; many partial results prove Robin for subclasses (odd, squarefree, k-free for k up to 21, sums of two squares) of density <1; asks whether exceptional set has density 0, answered qualitatively by Wojtowicz 2007.

### Main results

- **THM-PAPER-0094-1** (Theorem 1, theorem (unconditional), scope: asymptotic; Sec.2, Thm 1). For $x\ge3$, $\#NR(x)=O\big(x/\log\log x\big)$ where $NR(x)=\{7!<n\le x:\sigma(n)\ge e^\gamma n\log\log n\}$.
- **THM-PAPER-0094-2** (Theorem 2, theorem (unconditional), scope: asymptotic; Sec.2, Thm 2). For $x\ge3$, $\#NR(x)=O\big(x/\sqrt{\log x}\big)$.
- **THM-PAPER-0094-3** (Remark 1, unproved remark, scope: asymptotic; Sec.2 after Thm 2). The exponent 1/2 on log can be improved to $e^\gamma-1-\epsilon$ for any $\epsilon>0$, $x>x(\epsilon)$ (stated without proof).
- **THM-PAPER-0094-4** (Theorem 3, theorem (unconditional), scope: asymptotic; Sec.2, Thm 3). For every $\epsilon>0$ and $x>x(\epsilon)$, $\#NR(x)=O(x^{\epsilon})$. Hence $NR$ has density 0 with power-saving counting function (improving Wojtowicz 2007, which gave density 0 without bound).

### Key definitions

- NR(x)
- sigma, tau, phi, omega arithmetic functions
- P1,P2,P3 splitting of n/phi(n)

### Principal lemmas

- **THM-PAPER-0094-L1** (Proof of Thm 1; Sec.2). $\sum_{n\le x}\sigma(n)/n=\frac{\pi^2}{6}x+O(\log x)$; Markov-type bound on dyadic intervals [x/2,x]. — *Role:* Chebyshev/Markov argument giving 1/loglog x saving.
- **THM-PAPER-0094-L2** (Proof of Thm 2; Sec.2). If $n\in[x/2,x]$ has $\tau(n)<(\log x)^{1.5}$ then $\sigma(n)/n<2+1.5\log\log x<1.78\log\log(x/2)<e^\gamma\log\log n$ for $x>10^{600}$; so $NR(x)\cap[x/2,x]\subset\{\tau(n)\ge(\log x)^{1.5}\}$, with $\sum\tau(n)=x\log x+O(x)$. — *Role:* Divisor-function Markov bound.
- **THM-PAPER-0094-L3** (Proof of Thm 3, key step; Sec.2). If $n\in NR(x)\cap[x/2,x]$ then $\sigma(n)/n\le n/\varphi(n)$ forces $-\log P_2(n,x)=O(\exp(-a(\log\log x)^{3/5}(\log\log\log x)^{-1/5}))$, so n misses at most $m\ll\log x/\exp((\log\log x)^{1/2})$ primes below $\log x$, hence $Q_P=\prod_{p\le\log x,p\notin P}p$ divides n with $Q_P=x^{1+o(1)}$. — *Role:* Structural characterization: exceptions are x^{o(1)}-many (choices of P times cofactor n_1=x^{o(1)}).
- **THM-PAPER-0094-L4** (Vinogradov 1963 Mertens remainder (imported); Sec.2). $\prod_{p\le y}(1-1/p)=\frac{e^{-\gamma}}{\log y}(1+O(\exp(-a(\log y)^{3/5}(\log\log y)^{-1/5})))$ (applied at $y=\log x$). — *Role:* Supplies precision to match e^gamma loglog x.

### Proof architecture

Dyadic decomposition n in [x/2,x], summing x/2^k contributions. Thm 1: first moment of sigma(n)/n. Thm 2: second route via divisor-count threshold. Thm 3: Robin violators must have n/phi(n) nearly maximal; factor n/phi(n) over primes <=log x, Vinogradov-Korobov strength Mertens (error exp(-a(loglog x)^{3/5}...)) forces n to contain almost all primes up to log x (all but m << log x/exp(sqrt(loglog x)) of them); count subsets and cofactors giving x^{o(1)} possibilities per dyadic block.

**Imported results.** Vinogradov 1963 (Mertens remainder); Prime number theorem with classical error; Robin 1984 equivalence (RH iff Robin's inequality for n>7!); Wojtowicz 2007 (density 0)

**Techniques.** Markov/Chebyshev first-moment inequalities; dyadic decomposition; n/phi(n) bound for sigma(n)/n; Mertens product with Vinogradov-Korobov error; combinatorial counting of missing-prime sets (Stirling); omega(n)<2 log n/loglog n

## Context and interpretation

**Importance and obstacle overcome.** Unconditional x^{epsilon} counting function for the exceptional set to Robin's inequality, explicit and via the n/phi(n) Mertens trick; obstacle was getting beyond logarithmic savings by exploiting the very strong (Vinogradov-Korobov) Mertens remainder at height log x.

**Relation to prior work.** Quantifies Wojtowicz (2007) density-0 result; complements the k-free-integer partial verifications of Robin's inequality (Choie et al., Solé-Planat, Broughan-Trudgian, Morrill-Platt, Axler).

**Limitations and open questions.** Counting bound x^epsilon with ineffective x(epsilon); does not narrow location of potential counterexamples or give any unconditional Robin for a new infinite class beyond density 0. Remark 1 improvement unproved in the paper. Open: explicit power of log in Thm 3 structure (e.g. exceptions are numbers divisible by nearly all primes up to log x).

## Research potential

- **Hypotheses that might be weakened.** Replace log x threshold in Thm 3 by a larger y (e.g., y=(log x)^A) to sharpen the structure n divisible by almost all primes <= y; exponent in (7) uses a 3/5 Vinogradov-Korobov zero-free region: any better zero-free region sharpens m and the bound on x^{o(1)}.
- **Generalizations.** The same method applies to Nicolas' criterion (phi(n)/n loglog n inequality) and to Robin-type inequalities for other arithmetic functions (e.g., psi, Dedekind function, sigma_k via Lagarias-type criterion).
- **Candidate connections.** Structural result (violators are highly divisible, n=Q_P n_1 with n_1=x^{o(1)}) is exactly the colossally abundant regime; connects to Robin arithmetic programme: combine with Nicolas/Robin lower bounds for colossally abundant numbers and Axler/Morrill-Platt 21-free results to restrict where a counterexample can live.
- **Reusable lemmas.** The factorization sigma(n)/n <= n/phi(n)=P1^{-1}P2P3^{-1} and the missing-prime counting step (7) as a template for sparse-set bounds.
- **Possible experiments.** Compute NR-type sets for relaxed constants (sigma(n)/(n loglog n) >= e^gamma - delta) up to 10^{12} and compare empirical counts to x^{o(1)} predictions; enumerate n < 10^{10} with n/phi(n)>= e^gamma loglog n (e.g. via exhaustive search of n divisible by all primes up to y) to check structural claim Q_P | n.
- **Risks / barriers.** Method yields only upper density bounds; cannot decide RH since any counterexample could be among the x^{o(1)} exceptional n; the power-saving is limited by x^{o(1)} choices and not by finer arithmetic. No explicit x(epsilon).

## Audit notes (Level 1 reader)

Proof of Thm 3 steps look plausible as read: the bound on log P3 uses ω(n) < 2 log n/loglog n so n has at most that many prime factors above log x, whose reciprocals sum is bounded by that over primes in (log x, 4 log x) (stated '(3+o(1)) log x/loglog x primes' there, correct asymptotically but 'primes in (log x, 4 log x)' count requires PNT in short ranges at scale log x; fine). In Thm 2 proof the bound S1<1+1.5 loglog x is correct; threshold 10^{600} is needed and checked loosely. Remark 1 (exponent e^gamma-1-eps) has no proof in text. The source accessed is the Zenodo PDF, fully text-extracted. none else noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02415`; harvest queries: kw_RH_any, kw_robin, msc_11N56_rh.
- Triage decision: include — Recent work on Robin's inequality, a central RH equivalent.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
