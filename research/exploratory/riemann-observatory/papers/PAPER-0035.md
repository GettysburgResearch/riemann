# PAPER-0035 — On Artin's conjecture

| Field | Value |
|---|---|
| Authors | Hooley, Christopher |
| Year / stratum | 1967 / S3 |
| Venue | J. Reine Angew. Math. 225, 209-220 (1967). |
| Identifiers | zbMATH [0221.10048](https://zbmath.org/?q=an:0221.10048) · DOI [10.1515/crll.1967.225.209](https://doi.org/10.1515/crll.1967.225.209) |
| MSC | 11N69, 11R42, 11M26 |
| Families | A, E |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://gdz.sub.uni-goettingen.de/id/PPN243919689_0225 (Goettingen Digitization Centre scan of J. reine angew. Math. 225; article PDF https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0225/LOG_0016.pdf; read via page images) |
| Selection | score 4.5833, in-pool citations 81, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Assuming the extended Riemann hypothesis for Dedekind zeta functions of the Kummer fields Q(b^{1/k_1}, 1^{1/k}), prove Artin's primitive-root conjecture (infinitely many primes p for which a given non-square a != -1 is a primitive root) together with an asymptotic formula for N_a(x) with the Heilbronn-corrected density.

### Main results

- **THM-PAPER-0035-1** (Theorem (Section 7), part (a), case a_1 \not\equiv 1 \pmod 4, theorem (conditional), scope: conditional; Section 7, p. 219-220). Assume the extended Riemann hypothesis for the Dedekind zeta function of every Galois field Q(b^{1/k_1}, \zeta_k) with k square-free and k_1 | k. Let a be a nonzero integer, not \pm 1 and not a perfect square; N_a(x) is the number of primes p\le x for which a is a primitive root mod p; a_1 is the square-free part of a; h is the largest integer such that a is a perfect h-th power; C(h)=\prod_{q|h}(1-\tfrac{1}{q-1})\prod_{q\nmid h}(1-\tfrac{1}{q(q-1)}). If a_1\not\equiv 1 \pmod 4 then N_a(x)=C(h)\,\frac{x}{\log x}+O\!\left(\frac{x\log\log x}{\log^2 x}\right) as x\to\infty. *Conditional on:* Extended Riemann hypothesis for Dedekind zeta functions of the fields Q(b^{1/k_1}, 1^{1/k}), k squarefree, k_1|k.
- **THM-PAPER-0035-2** (Theorem (Section 7), part (a), case a_1 \equiv 1 \pmod 4, theorem (conditional), scope: conditional; Section 7, p. 220). Under the same hypothesis, if a_1\equiv 1 \pmod 4 then N_a(x)=C(h)\Big(1-\mu(|a_1|)\prod_{q|h,\,q|a_1}\frac{1}{q-2}\prod_{q\nmid h,\,q|a_1}\frac{1}{q^2-q-1}\Big)\frac{x}{\log x}+O\!\left(\frac{x\log\log x}{\log^2 x}\right). *Conditional on:* same extended RH hypothesis.
- **THM-PAPER-0035-3** (Theorem (Section 7), part (b), corollary (conditional), scope: conditional; Section 7, p. 220; positivity of A(a) at p. 219 after (32)). Under the same hypothesis, if a is neither \pm 1 nor a perfect square then there are infinitely many primes p for which a is a primitive root modulo p. This follows because the density constant A(a) is strictly positive. *Conditional on:* same extended RH hypothesis.
- **THM-PAPER-0035-4** (Equation (4) and (3), unconditional estimate, scope: asymptotic; Section 3, pp. 211-212). Without any hypothesis, with \xi_1=\tfrac16\log x, \xi_2=x^{1/2}\log^{-2}x, \xi_3=x^{1/2}\log x: N_a(x)=N_a(x,\xi_1)+O\{M_a(x,\xi_1,\xi_2)\}+O\!\left(\frac{x\log\log x}{\log^2 x}\right), where M_a(x,\xi_2,\xi_3)=O(x\log\log x/\log^2x) by Brun's method and Mertens, and M_a(x,\xi_3,x-1)=O(x/\log^2 x).
- **THM-PAPER-0035-5** (Equation (33), estimate (conditional), scope: conditional; Section 6, p. 219). M_a(x,\xi_1,\xi_2)\le\sum_{\xi_1<q\le\xi_2}\Big(\frac{\operatorname{li}x}{q(q-1)}+O(x^{1/2}\log x)\Big)=O\!\left(\frac{x}{\log^2x}\right), using the conditional prime-ideal-type estimate (28) (stated in Section 5; not read in detail). *Conditional on:* extended RH for the Kummer fields.

### Principal lemmas

- **THM-PAPER-0035-L1** (Criterion in Section 3; Section 3, p. 210-211). For p\nmid a, a is a primitive root mod p iff there is no prime q | p-1 for which a is a q-th power residue mod p; this gives the sieve N_a(x)=N_a(x,x-1) and the Legendre-type inclusion-exclusion (5) N_a(x,\xi_1)=\sum_{l'}\mu(l')P_a(x,l'). — *Role:* Reduces the problem to counting primes splitting completely in Kummer fields.
- **THM-PAPER-0035-L2** (Section 4 (equations (8)-(11)); Section 4, pp. 212-213). The primes counted by P_a(x,k) are exactly those p\nmid ak that split completely in G=Q(a^{1/k_1}, 1^{1/k}), with k_1=k/(h,k); [G:Q]=\varphi(k)[G:Z]\text{ where }[G:Z]\mid k_1 and in fact [G:Z]=k_1 or k_1/2 (the latter only if k is even), using that subfields of abelian Z are abelian. — *Role:* Gives the degree n(k) of the Kummer extension so that the prime ideal theorem under GRH produces P_a(x,k)=\mathrm{li}\,x/n(k)+O(\sqrt x\log x\cdot\ldots).
- **THM-PAPER-0035-L3** (Equation (3) and Section 3, last term; p. 211-212). For primes q>x^{1/2}\log x, p\le x with R(q,p), p divides \prod_{m<x^{1/2}\log^{-1}x}(a^{2m}-1), giving M_a(x,\xi_3,x-1)<\frac{2\log|a|}{\log 2}\sum_{m<x^{1/2}\log^{-1}x} m=O(x/\log^2x), with no hypothesis. — *Role:* Handles large q unconditionally by a size argument on the product.
- **THM-PAPER-0035-L4** (Equations (18)-(24), (21)-(23); Section 5, pp. 215-216). Uniform-in-field polynomial bounds: |\Delta|\le k^{A_2 n(k)}, and |(s-1)\zeta_G(s)|\le\{k(|t|+2)\}^{A_8 n} on -3/2\le\sigma\le 11/2, obtained from the functional equation, Stirling and Phragmen-Lindelof; 1/|(s-1)\zeta(s)|\le A_3^n at \sigma=2. — *Role:* Supplies the explicit dependence on the field degree n(k) needed to apply the explicit formula for \psi(x,k) under GRH uniformly in k up to x^{1/3}-type ranges.
- **THM-PAPER-0035-L5** (Equations (30)-(32); Section 6, p. 219). Evaluation of A(a)=\sum_{k\ge1}\mu(k)(h,k)\,\varepsilon(k)/(k\varphi(k))-type series: A(a)=C(h) if a_1\not\equiv1 mod 4, and A(a)=C(h)(1-\mu(|a_1|)\prod_{q|h,q|a_1}(q-2)^{-1}\prod_{q\nmid h,q|a_1}(q^2-q-1)^{-1}) if a_1\equiv1 mod 4; A(a)>0 always. — *Role:* Computes the Artin constant (Heilbronn-corrected) and proves positivity.

### Proof architecture

Section 3: sieve with thresholds \xi_1=\tfrac16\log x, \xi_2=x^{1/2}\log^{-2}x, \xi_3=x^{1/2}\log x. Small q (\le \xi_1) are handled by Legendre inclusion-exclusion into counts P_a(x,l') of primes splitting totally in Kummer fields; middle range \xi_1<q\le\xi_2 uses GRH-conditional counts and Mertens; range \xi_2<q\le\xi_3 uses a Brun sieve upper bound on primes p\equiv1 mod q; and q>\xi_3 is handled by the product (a^{2m}-1) divisibility argument with no hypothesis. Section 4 identifies P_a(x,k) with prime splitting in G=Q(a^{1/k_1},1^{1/k}) and computes [G:Q]. Section 5 proves explicit-formula bounds for \psi(x,k) uniform in k using the growth bounds (20)-(24) and the zero-counting statement, which under the extended RH gives P_a(x,k)=\mathrm{li}\,x/n(k)+O(x^{1/2}\log x) uniformly for k\le x^{1/3}-type ranges (from (6) and (33); the exact statement (28) was not read). Section 6 sums over l' to get N_a(x,\xi_1)=A(a)\,x/\log x+O(\cdot), computes A(a), and bounds M_a(x,\xi_1,\xi_2) by (33). Section 7 assembles via (4), (29), (30), (32), (33). Imported: Dedekind zeta analytic properties (Landau, Satz 154, 171, 197, 199), Brun's sieve, Mertens, prime ideal theorem/explicit formula under GRH.

**Techniques.** Sieve in prime ranges with three thresholds; Kummer-field splitting criterion (Dedekind); explicit formula for prime ideals under GRH uniform in field degree; Brun's sieve; Phragmen-Lindeloef bounds for Dedekind zeta; Euler-product evaluation of the Artin constant

## Context and interpretation

**Importance and obstacle overcome.** First proof of Artin's conjecture and of the Artin density (Heilbronn-corrected) under GRH, resolving the discrepancy with Lehmer's numerical data. The obstacle is that primes q up to p-1 appear in the criterion, while GRH controls only q up to about \sqrt x/\log^2 x; Hooley closes the gap with the Brun-sieve and product-divisibility estimates for large q, which cost no hypothesis.

**Relation to prior work.** 

**Limitations and open questions.** Conditional on a very strong GRH for infinitely many Kummer fields (extended RH for all Q(b^{1/k_1},1^{1/k})); footnote 2 (p. 210) notes that weaker hypotheses (a smaller set of zeta functions) suffice, especially for an existence theorem. The conjecture for a fixed a remains open unconditionally (as of this paper). No unconditional result, and no explicit statement of how a single failure of GRH would change the argument.

## Research potential

- **Hypotheses that might be weakened.** The extended RH for all Q(b^{1/k_1},1^{1/k}), k squarefree: only fields with k\le x^{1/3}-type conductor (see (6)) enter, and footnote 2 hints at a restricted family; this was later developed in Gupta-Murty and Heath-Brown (unconditional for all but two primes) and Murty-Srinivasan. A concrete question is to determine which finite window of k the GRH input is used on, by tracking (6) and (28).
- **Generalizations.** Primes for which two integers are simultaneously primitive roots, and the least primitive root (stated in the closing remark, p. 220); function-field analogue (Bilharz, cited in the introduction); elliptic curve analogues (Lang-Trotter style).
- **Candidate connections.** Direct example of a conditional-on-GRH asymptotic where the error term O(x loglog x/log^2 x) comes from the unconditional large-q treatment rather than GRH. This is a model for 'RH-dependent versus RH-independent ranges' for any RH-consequence analysis in the Observatory.
- **Reusable lemmas.** The three-range sieve decomposition (3)-(4) and the unconditional bound (3) for q>x^{1/2}\log x are reusable for any primitive-root or order-in-(Z/p)^* problem.
- **Possible experiments.** Compute N_a(x) for several a (e.g. a=2,3,5,10, and a with a_1\equiv1 mod 4 such as a=5) up to 10^9 and compare with C(h) and the a_1\equiv1 mod 4 correction; this tests the constant in Theorem (a), not GRH itself.
- **Risks / barriers.** Statement (28) and Section 5 were not read, so the exact conductor range and GRH usage are inferred from (6), (33) and the introduction. The theorem is conditional, so it is not evidence for RH. At most it shows RH has arithmetic consequences.

## Audit notes (Level 1 reader)

None noticed in inspected portion. Sections 5 (middle) and 6 (first part) were not read page by page; the precise form of estimate (28) is therefore unrecorded.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00328`; harvest queries: kw_RH_any, msc_11M26.
- Triage decision: include — Hooley proves Artin's primitive root conjecture under GRH, a canonical GRH application.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
