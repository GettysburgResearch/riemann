# PAPER-0082 — Exponential sums with multiplicative coefficients

| Field | Value |
|---|---|
| Authors | Montgomery, H. L.; Vaughan, R. C. |
| Year / stratum | 1977 / S3 |
| Venue | Invent. Math. 43, 69-82 (1977). |
| Identifiers | zbMATH [0362.10036](https://zbmath.org/?q=an:0362.10036) · DOI [10.1007/BF01390204](https://doi.org/10.1007/BF01390204) |
| MSC | 11N37, 11L03 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — http://gdz.sub.uni-goettingen.de/gdzocr/PPN356556735_0043/ (GDZ OCR of pages 75-90, Inventiones Math. 43 (1977) 69-82; DOI 10.1007/BF01390204; EuDML record https://eudml.org/doc/142508) |
| Selection | score 4.4221, in-pool citations 25, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Obtain a sharp bound, uniform over the class F of multiplicative f with |f(p)|<=A and sum_{n<=N}|f(n)|^2<=A N, for S(alpha)=sum_{n<=N}f(n)e(n alpha), improving Daboussi's loglog-saving, and deduce a conditional (GRH) improvement of the Polya-Vinogradov inequality.

**Historical motivation.** Daboussi's theorem gave a uniform but weak saving (loglog)^{-1/2} for multiplicative f; Montgomery-Vaughan aim for the Vinogradov-type saving (log N)^{-1}(up to loglog powers) and use it as the minor-arc input to improve Polya-Vinogradov under GRH.

### Main results

- **THM-PAPER-0082-1** (Theorem 1, theorem, scope: asymptotic; Section 1, eq. (6), p. 70; proved in Sections 2-5). Let A\ge1 be fixed and \mathcal F the class of multiplicative f with |f(p)|\le A for all primes p and \sum_{n\le N}|f(n)|^2\le A N for all N (eq. (1)). If q\le N and (a,q)=1 then, uniformly for f\in\mathcal F, S(a/q)\ll_A N\Big\{(\log 2N)^{-1}+\varphi(q)^{-1/2}+(q/N)^{1/2}\big(\log(2N/q)\big)^{3/2}\Big\}. (Exponent of the last log read from the proof, (10).)
- **THM-PAPER-0082-2** (Corollary 1, corollary, scope: asymptotic; Section 1, p. 70; proof Section 6). If |\alpha-a/q|\le q^{-2}, (a,q)=1 and 2\le R\le q\le N/R, then S(\alpha)\ll_A N/\log N+N R^{-1/2}(\log R)^{3/2}, uniformly for f\in\mathcal F (form reconstructed from (22) and the proof in Section 6; OCR of the display is corrupted).
- **THM-PAPER-0082-3** (Corollary 2, corollary, scope: asymptotic; Section 1, p. 70; proof Section 6, p. 77). For almost all real \alpha, and for all real irrational algebraic \alpha, S(\alpha)\ll_{A,\alpha} N(\log\log N)^{3/2}/\log N-type bound (N>N_0(\alpha)), uniformly in f\in\mathcal F; the printed display is OCR-corrupted, and the form here is reconstructed from the proof which takes R of size (\log N)^2.
- **THM-PAPER-0082-4** (Section 7 propositions (i)-(iii), sharpness examples, scope: finite; Section 7, p. 78). (i) For every real \alpha and N\ge2 there is a totally multiplicative f with |f(n)|\le1 and |S(\alpha)|\gg N/\log N. (ii) If q\le N^{...}, (a,q)=1 there is f (a primitive character mod q or induced) with |S(a/q)|\gg N q^{-1/2}. (iii) If N(\log N)^{-?}\le Q\le N there exist \alpha,q,f with Q/3\cdot... \le q\le Q, (a,q)=1, |S(a/q)|\gg (N q)^{1/2}\cdot... [as in the paper; precise ranges garbled]. In all three f is totally multiplicative with |f(n)|\le1.
- **THM-PAPER-0082-5** (Theorem 2, conditional theorem, scope: conditional; Section 1, p. 70; proof Sections 8-9, pp. 78-81). Assume the Grand Riemann Hypothesis (no Dirichlet L(s,\chi) has a zero with \Re\rho>1/2). Then for every non-principal character \chi modulo q and every x, \sum_{n\le x}\chi(n)\ll q^{1/2}\log\log q. *Conditional on:* Grand Riemann Hypothesis.

### Key definitions

- Class F_A: multiplicative f, |f(p)|<=A, sum_{n<=N}|f(n)|^2<=A N for all N
- S(alpha)=sum_{n<=N} f(n)e(n alpha), e(x)=exp(2 pi i x)
- GRH: no L(s,chi) has a zero with Re rho>1/2

### Principal lemmas

- **THM-PAPER-0082-L1** (Fundamental estimate (16), Section 4; p. 74-76). For disjoint rectangles \mathcal R(k)=I(k)\times J(k) in (0,Q]\times(0,M], with Q''\le2Q', |I|\le X, |J|\le Y... and (a,q)=1,\ q\le XY: \Big|\sum_k\sum_{(p,n)\in\mathcal R(k)}f(p)f(n)e(pna/q)\log p\Big|\ll M Q\{(\log2Q)^{-?}+\ldots\}\text{, i.e. } \ll MQ\big\{(XY)^{-1/2}\ldots+\varphi(q)^{-1/2}\ldots\big\}\ (\text{exact form of (16) garbled}). — *Role:* Core bilinear (type I/II) estimate: Cauchy-Schwarz over n, smoothing weight, then a sieve upper bound for prime pairs (p,p+h) and a bound on sum min(Y,||h a/q||^{-1}) using divisor-type sums.
- **THM-PAPER-0082-L2** (Reduction in Section 2, eqs (8)-(10); p. 71-73). Using \log n=\sum_{m|n}\Lambda(m), it suffices to show \sum_{mn\le N}f(m)f(n)\Lambda(m)e(mna/q)\ll N+N\varphi(q)^{-1/2}\log N+(Nq)^{1/2}(\log 2N/q)^{3/2}\log N; replacing f(mn) by f(m)f(n) costs O(N) by (1),(4),(9); prime-power m=p^k, k\ge2 contribute O(N). — *Role:* Reduces the claim to a bilinear sum over primes p times n, i.e. a Vinogradov-type bilinear form.
- **THM-PAPER-0082-L3** (Section 3 partition; p. 73-74). Partition the region pn\le N into dyadic rectangles \mathcal R_i and iteratively placed rectangles \mathcal R_{i,j,k} of the form (P,P']\times(N',N''] with P'-P\ge1, N''-N'\ge1 and (P''-P)(N''-N')>q; leftover regions are bounded crudely using Brun-Titchmarsh and Cauchy, giving \ll N+(Nq)^{1/2}(\log 2N/q)^{3/2}\log N. — *Role:* Geometry of the bilinear decomposition and treatment of boundary regions.
- **THM-PAPER-0082-L4** (Lemma 1 (Polya); Section 8, p. 79). For a primitive character \chi mod q, q>1: \sum_{n\le x}\chi(n)=\frac{\tau(\chi)}{2\pi i}\sum_{1\le|h|\le q}\bar\chi(h)h^{-1}(1-e(-hx/q))+O(1)+O(q^{1/2}\log q\cdot q^{-1}\ldots) (printed error garbled). — *Role:* Fourier expansion converting the character sum to exponential sums with the multiplicative coefficient \bar\chi(h)/h.
- **THM-PAPER-0082-L5** (Lemma 2; Section 8, p. 79-80). Let \chi be non-principal mod k, L(s,\chi)\ne0 for \Re s>1/2, (\log k)^{10}\le y\le k, x\le k. Then \sum_{n\le x}\chi(n)=\sum_{n\le x,\ n\in S(y)}\chi(n)+O(xy^{-1/2}(\log k)^{c}) where S(y) is the set of n with all prime factors \le y (exponents garbled). — *Role:* GRH-derived smoothing: character sums equal sums over y-smooth numbers up to small error; proved by contour integration with M(s,\chi)=\prod_{p\le y}(1-\chi(p)p^{-s})^{-1} and N=L/M.
- **THM-PAPER-0082-L6** (Section 9 (proof of Theorem 2); p. 80-81). Via Dirichlet approximation: if r>(\log u)^{?}, Corollary 1 gives S(\alpha,u)\ll u/\log u; if r\le(\log u)^{?}, Lemma 2 (applied to \psi\chi mod qr/d) reduces to y-smooth sums, whence \sum_{n\le u}\chi(n)e(n\alpha)\ll u/\log u+\sum_{n\in S}1; summation by parts gives \sum_n\chi(n)e(n\alpha)/n\ll\log\log q; with Littlewood's L(1,\chi)\ll\log\log q under GRH, Theorem 2 follows from Lemma 1. — *Role:* Combines major arcs (GRH, Lemma 2) with minor arcs (Theorem 1/Corollary 1).

### Proof architecture

Theorem 1: (i) reduce S(a/q) via log n=sum Lambda to a bilinear sum over (p,n) with weights f(p)f(n); (ii) replace f(mn) by f(m)f(n) (error O(N) using (1)); (iii) partition the hyperbolic region pn<=N into rectangles; (iv) on each rectangle apply Cauchy-Schwarz in n (using only the L^2 bound (1) on f) and a smoothing weight, leading to a sum over prime pairs p,p' with ||(p-p')na/q||; (v) bound pairs (p,p+h) by sieve upper bound and sum min(Y,||h a/q||^{-1}) by arithmetic (divisor-sum) estimates -> (16); (vi) sum over rectangles (Brun-Titchmarsh for the thin strips) giving (6). Corollaries via Dirichlet approximation and partial summation/ Abel transform (21); Corollary 2 via Khintchine/Liouville. Theorem 2: Polya Fourier expansion (Lemma 1) + major arcs via GRH (Lemma 2 smooth numbers, Littlewood's L(1,chi) bound) + minor arcs via Corollary 1. Imported: Brun-Titchmarsh [Halberstam-Richert Thm 3.?], sieve estimate for prime pairs [H-R Thm 3.11], Davenport Ch.19 for GRH bound on sum chi(p)p^{-s}, Littlewood 1928 L(1,chi) under GRH, Dirichlet/Khintchine/Liouville theorems.

Dependency edges: CAND-00336 → Daboussi 1975 (Asterisque 24-25) (improves); CAND-00336 → Polya-Vinogradov inequality (conditional improvement under GRH); CAND-00336 → Brun-Titchmarsh inequality (imports); CAND-00336 → Littlewood 1928 L(1,chi) under GRH (imports)

**Imported results.** Daboussi (1975) and Daboussi-Delange (1974): bound S(alpha)<<N(loglogN)^{-1/2} under q-conditions (motivating); Davenport 1937 and Vinogradov: S(alpha)<<N(logN)^{-A} for the Mobius function (mentioned); Polya (1918)/Vinogradov (1919): sum chi(n)<<q^{1/2}log q; Brun-Titchmarsh inequality (Halberstam-Richert 1974, Thm 7/3.?); Sieve estimate for pairs of primes (Halberstam-Richert Thm 3.11); Littlewood (1928): L(1,chi)<<loglog q under GRH; Davenport, Multiplicative Number Theory, Sec. 19; Khintchine theorem (Hardy-Wright Thm 198), Liouville (Thm 191), Paley (1932) for sharpness of Theorem 2

**Techniques.** Vinogradov bilinear (type II) method with L^2 information only on f; Cauchy-Schwarz with smoothing; Sieve upper bound for prime pairs p,p+h; Brun-Titchmarsh; Rectangle partition of pn<=N; Dirichlet approximation / minor-major arcs; GRH-smooth-number approximation of character sums

## Context and interpretation

**Importance and obstacle overcome.** Shows that multiplicativity plus L^2-boundedness suffices for N/log N-type cancellation, matching Vinogradov's prime sum case up to log factors and showing sharpness (Section 7: f can reach N/log N). Theorem 2 (GRH => q^{1/2} loglog q) is the best-possible-up-to-constants improvement matching Paley's Omega result. Obstacle: no information on f(p) beyond |f(p)|<=A; handled by using f only through L^2 and reducing to bilinear sums where the sieve bound for p,p+h replaces equidistribution input.

**Relation to prior work.** Strengthens Daboussi's (1975) uniform bound; generalizes Vinogradov/Davenport minor-arc estimates for primes and Mobius to all multiplicative f; the conditional Polya-Vinogradov improvement follows Paley and Littlewood, authors note that the maximum over x is not typically so large (to be shown elsewhere).

**Limitations and open questions.** Theorem 2 conditional on GRH; Theorem 1 loses (log)^{3/2} and does not beat N/log N for the general class (and (i) shows this is sharp). Does not reach the Mobius-specific saving (log N)^{-A} unconditionally; Corollary 2 only for 'typical' alpha.

## Research potential

- **Hypotheses that might be weakened.** Assumption |f(p)|<=A and the L^2 condition (1) could be weakened to a weighted L^2 condition (as in Granville-Soundararajan pretentious setting); the exponent 3/2 of log may be improvable.
- **Generalizations.** Montgomery-Vaughan with prime-twisted weights; to number-field / function-field settings; Theorem 2 analogue for Selberg-class twists. The bilinear reduction is reusable for sums of mu(n)e(n alpha) under RH, relevant to signed native/Mobius cancellation programmes.
- **Candidate connections.** Mobius case f=mu: under RH, the same structure with Lemma 2-type smoothing can give sharper minor arc bounds; Corollary 1 gives a uniform input for Mertens-type sums twisted by e(n alpha). Link to Levinson-type mollifier mean squares (CAND-00409) through large-sieve flavored off-diagonal control.
- **Reusable lemmas.** Fundamental estimate (16) and Lemma 2 (GRH smoothing of character sums to y-smooth numbers) are reusable.
- **Possible experiments.** Compute max_{alpha} |sum_{n<=N} mu(n)e(n alpha)| for N up to 10^7 and compare with N/log N and N R^{-1/2}(log R)^{3/2}; for f in the extremal families (i),(ii), verify the claimed lower bounds numerically.
- **Risks / barriers.** Does not address zero locations; Theorem 2 is conditional on GRH and yields no information toward RH itself. Uniformity over the class F necessarily prevents saving beyond N/log N (Prop. (i)).

## Audit notes (Level 1 reader)

OCR (GDZ) corrupts exponents throughout: exact forms of (6), (16), Corollary 1-2 displays and Section 7 ranges are partly reconstructed from the proof (flagged). One apparent notational inconsistency in the text: Theorem 2 is labelled 'Theorem !' and Corollary 2 'Corollary !' (OCR). Nothing else noticed in inspected portion; the proof is elementary and appears internally consistent at the level read.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00336`; harvest queries: kw_RH_any, citation_expansion.
- Triage decision: include — Montgomery-Vaughan on exponential sums with multiplicative coefficients, Moebius cancellation.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
