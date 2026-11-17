# PAPER-0031 — Moments of zeta and correlations of divisor-sums. IV

| Field | Value |
|---|---|
| Authors | Conrey, Brian; Keating, Jonathan P. |
| Year / stratum | 2016 / S6 |
| Venue | Res. Number Theory 2, Paper No. 24, 24 p. (2016). |
| Identifiers | zbMATH [1411.11074](https://zbmath.org/?q=an:1411.11074) · DOI [10.1007/s40993-016-0056-4](https://doi.org/10.1007/s40993-016-0056-4) · arXiv [1603.06893](https://arxiv.org/abs/1603.06893) |
| MSC | 11M06, 11M26 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/1603.06893 |
| Selection | score 4.5911, in-pool citations 21, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Within the Conrey-Keating program of deriving all lower-order terms of the 2k-th shifted moments of zeta from long Dirichlet polynomials and divisor correlations (circle-method viewpoint of Bogomolny-Keating), treat the first genuine Type II sums: prove that a convolution of two shifted divisor sums reproduces exactly the 2-swap terms predicted by the CFKRS recipe for the mean square of a Dirichlet polynomial of length X with T^2<<X<<T^3 and generalized divisor coefficients.

**Historical motivation.** Conrey-Keating programme to derive the CFKRS recipe for moments of zeta by number-theoretic means (shifted divisor sums) rather than random matrix theory; builds on Bogomolny-Keating's heuristics and the 2-swap special case of CK2.

### Main results

- **THM-PAPER-0031-1** (Theorem 1 (analytic version of general shifted divisor sum, from CK3), theorem, scope: asymptotic; Section 2, p.6). $\operatorname*{Res}_{w=1-\alpha,\,z=1-\beta}\sum_{q\ge1}\mu(q)\sum_{d\ge1}d^{z+w-1}\zeta(w+z-1)D_A\!\left(w,e(-\tfrac1{qd})\right)D_B\!\left(z,e(-\tfrac1{qd})\right)=\mathcal B(A'\cup\{-\beta\},B'\cup\{-\alpha\})$, with $A'=A\setminus\{\alpha\}$, $B'=B\setminus\{\beta\}$. (Restated from CK3; follows from an identity in Sec. 3 of CK3 and the singular-part result of Conrey-Gonek [CG].)
- **THM-PAPER-0031-2** (Theorem 2 (convolution identity, key theorem), theorem, scope: asymptotic; Section 2, p.6; proved Sections 10-11). $\operatorname*{Res}_{\substack{w_1=1-\alpha_1,z_1=1-\beta_1\\w_2=1-\alpha_2,z_2=1-\beta_2}}\ \zeta(w_1+z_1-1)\zeta(w_2+z_2-1)\sum_{(M,N)=1}\sum_{q_1,q_2,d_1,d_2}\frac{\mu(q_1)\mu(q_2)d_1^{z_1+w_1-1}d_2^{z_2+w_2-1}}{M^{z_1+w_2-1}N^{w_1+z_2-1}}\,D_{A_1}\!\big(w_1,e(-\tfrac N{q_1d_1})\big)D_{A_2}\!\big(w_2,e(-\tfrac M{q_2d_2})\big)D_{B_1}\!\big(z_1,e(-\tfrac M{q_1d_1})\big)D_{B_2}\!\big(z_2,e(-\tfrac N{q_2d_2})\big)=\mathcal B(A''\cup\{-\beta_1,-\beta_2\},B''\cup\{-\alpha_1,-\alpha_2\})$ (display partially garbled in extracted text; the exponents of M, N and the exact placement of d_i,q_i must be read from the PDF), with $A''=A\setminus\{\alpha_1,\alpha_2\}$ (A=A_1 u A_2 split), B'' analogous.
- **THM-PAPER-0031-3** (Section 9 (Conclusion), claim, scope: conditional; Sections 1 and 9). Both the Perron/recipe computation and the convolution of shifted divisor correlations give the same asymptotic formula (with power savings, modulo the correlation conjecture used) for the mean square of a Dirichlet polynomial of length X, T^2<<X<<T^3, with coefficients a general divisor function tau_A, tau_B; all main terms agree with the CFKRS recipe including the leading term of Keating-Snaith. *Conditional on:* Conjecture 1 (meromorphic continuation and residue formula for shifted divisor correlations S_{A,B}(s,h), from CK3).
- **THM-PAPER-0031-4** (Lemma 1 (formal combinatorial identity), lemma, scope: finite; Section 10, p.17-18). For four functions a,A,b,B: $F(a,A;b,B)+F(A,a;B,b)=C(A\star b,a\star B)+C(a,A)C(b,B)$, where $F(a,A;b,B)=\sum_{K,L,M}a(K)A(K+M)b(L)B(L+M)X^{K+L+M}$ and $C(a,b)=\sum_{r\ge0}a(r)b(r)X^r$.

### Key definitions

- Shifted moment I^psi_{A,B}(T)=int psi(t/T) prod_{alpha in A} zeta(s+alpha) prod_{beta in B} zeta(1-s+beta) dt
- Generalized divisor function tau_A with sum tau_A(n)n^{-s}=prod_{alpha in A}zeta(s+alpha)
- B(A,B)=sum tau_A(n)tau_B(n)/n = A(A,B)Z(A,B), Z(A,B)=prod zeta(1+alpha+beta)
- Swaps: subsets U subset A, V subset B with |U|=|V|
- Type I (one swap) and Type II (two swaps) sums
- Ramanujan sum r_q(h)

### Principal lemmas

- **THM-PAPER-0031-L1** (Lemma 1; Section 10, p.17-18). $F(a,A;b,B)+F(A,a;B,b)=C(A\star b,a\star B)+C(a,A)C(b,B)$ (formal identity of power series). — *Role:* Converts the p-adic local factor of the circle-method sum into the C-function of the recipe; proved by integrating over theta with Y=X e(theta) and an inclusion-exclusion on r>R, s>S
- **THM-PAPER-0031-L2** (Reformulation 11.1; Section 11.1, p.22-23). Need to show $\sum_{\min(M,N)=0}X^{-M(\gamma+\beta)-N(\alpha+\delta)}\Sigma_1(M,N)\Sigma_2(M,N)X^{M+N}=(1-X^{1-\alpha-\beta})(1-X^{1-\gamma-\delta})\,C(A\cup C\cup\{-\beta,-\delta\},B\cup D\cup\{-\alpha,-\gamma\})$ with explicit sums Sigma_1, Sigma_2. — *Role:* The local (prime-power) identity whose verification proves Theorem 2
- **THM-PAPER-0031-L3** (Section 3 setup; Section 3, p.6-7). Splitting A=A_1 u A_2, B=B_1 u B_2 so tau_A=tau_{A_1}*tau_{A_2}, tau_B=tau_{B_1}*tau_{B_2}; Farey dissection of [0,1] with fractions M/N, 1<=M<=N<=Q, and h_1=m_1N-n_1M, h_2=m_2M-n_2N giving m_1m_2-n_1n_2 = h_1m_2M+h_2m_1N-h_1h_2 over MN, so the off-diagonal sum becomes a double sum over shifted divisor sums. — *Role:* Discrete circle method: decomposes the 4-variable off-diagonal sum O_II into products of two shifted correlations (*_1): m_1N-n_1M=h_1 and (*_2): m_2M-n_2N=h_2
- **THM-PAPER-0031-L4** (Section 4 (h_2=0 semi-diagonal); Sections 4-6). If h_2=0 then m_2=N l, n_2=M l with l integer; the h_1 sum reduces to a single shifted divisor correlation <tau_A(m)tau_B(n)>_{(*)} given by the delta-method formula (4), with explicit arithmetic factors G_A, G_B and Z(A)=prod zeta(1+a). — *Role:* Semi-diagonal terms feed the main-term count and match recipe terms with one swap per side
- **THM-PAPER-0031-L5** (Section 8 (Automorphisms); Section 8, p.14-16). Each term arising from the recipe is produced 2^{k+l} times by the circle-method decomposition where |A|=k, |B|=l, one for each decomposition of m=m_1m_2, n=n_1n_2 into divisors; this equals the number of ways the recipe term arises from decompositions of A and B, so overcounting cancels and each recipe term appears once. — *Role:* Explains multiplicity bookkeeping: correct normalization of the Type II convolution

### Proof architecture

Write the long Dirichlet polynomial moment I^psi_{A,B}(T;X) as sum over m,n<=X of tau_A(m)tau_B(n) psi-hat((T/2pi)log(m/n))/sqrt(mn). Diagonal m=n gives 0-swap terms; off-diagonal split into Type I (one swap, a single shifted divisor sum, treated in CK1-CK3) and Type II (two swaps, X>T^2), where one factors tau_A, tau_B as convolutions and applies a Farey/circle-method decomposition with parameter Q so that m_1/n_1 ~ M/N ~ n_2/m_2 to turn the sum into products of two shifted correlations tau_{A_1}(m_1)tau_{B_1}(n_1) with m_1N-n_1M=h_1 and tau_{A_2}(m_2)tau_{B_2}(n_2) with m_2M-n_2N=h_2. The semi-diagonal case h_2=0 is computed explicitly (Sections 4-6) using the delta-method formula for the average of a shifted divisor correlation. Heuristic derivation of the general identity in Sections 7-9, including the automorphism count that removes overcounting. Rigorous proof of Theorem 2 as an identity between residues/arithmetical Euler-product factors in Sections 10-11, proved prime-by-prime by recasting as an identity of power series in X (Lemma 1 and Section 11 reformulation). Theorem 1 imported from CK3 and Conrey-Gonek. The evaluation of the shifted divisor correlations themselves is conjectural (Conjecture 1 of CK3), so the paper establishes agreement of two conjectural/heuristic evaluations, not an unconditional moment asymptotic.

**Imported results.** Goldston-Gonek mean value theorem for long Dirichlet polynomials; Conrey-Gonek: singular part of D_A(s,e(a/q)) (reference [CG]); Identity at the end of Section 3 of CK3; Bogomolny-Keating off-diagonal method; CFKRS recipe (Conrey-Farmer-Keating-Rubinstein-Snaith)

**Techniques.** Approximation of zeta^k by long Dirichlet polynomial (Goldston-Gonek mean values); Bogomolny-Keating off-diagonal terms viewed as a multi-dimensional Hardy-Littlewood circle method; Farey dissection with convolution of shifted divisor sums; Delta-method heuristic for shifted divisor correlations and Ramanujan sums; Residue calculus with generalized divisor functions tau_A and Euler products A(A,B); Formal power-series identities per prime (inclusion-exclusion, Lemma 1); Automorphism / multiplicity counting of divisor decompositions

## Context and interpretation

**Importance and obstacle overcome.** Provides a number-theoretic (non-random-matrix) route to all lower-order terms of shifted zeta moments and shows the CFKRS recipe is reproduced by an independent arithmetic computation for 2 swaps. The obstacle is the proliferation of off-diagonal terms with product structure (m_1m_2 - n_1n_2 = h), handled by the new M,N circle-method splitting into two linked shifted divisor problems; the algebraic miracle is the equality with the recipe's B function.

**Relation to prior work.** Part 4 of Conrey-Keating series: CK1 (0 swaps), CK2 (special 2 swaps), CK3 (1 swap in general), CK4 (general 2 swaps, this paper). Agrees with CFKRS recipe and Keating-Snaith leading term. Uses Goldston-Gonek and Conrey-Gonek.

**Limitations and open questions.** Only 2 swaps (X>T^2 case up to X<<T^3), not general X. The formula rests on the correlation conjecture (Conjecture 1 of CK3); no unconditional proof of the shifted-divisor asymptotics beyond what is known. The identity is verified; the actual asymptotic with power saving is stated conditional on the correlation input. Next paper in the series (announced) treats arbitrary length. Does not give any unconditional lower bound or new information on zeros.

## Research potential

- **Hypotheses that might be weakened.** Dependence on Conjecture 1 (shifted divisor-correlation pole structure): replacing it by a proven (even with power-saving restricted) correlation input, e.g. results of Deshouillers-Iwaniec / Duke-Friedlander-Iwaniec on quadratic divisor problem, would give unconditional partial moment results in a restricted range of X.
- **Generalizations.** 3-swap and higher (completely general X), cases with shifts A,B of larger size, and moments of L-functions of other families (Dirichlet, quadratic characters) via same circle-method structure; the identity could be formalized in a computer algebra system for arbitrary k.
- **Candidate connections.** Moments of zeta and extreme/large values: the CFKRS recipe feeds conjectures on max|zeta(1/2+it)| (Lindelof-type) and thus on zero spacing; also relates to Heap-Radziwill-Soundararajan style sharp upper bounds on moments. Not directly connected to RH: moment asymptotics do not imply zero location.
- **Reusable lemmas.** Lemma 1 (formal identity F(a,A;b,B)+F(A,a;B,b)=C(A*b,a*B)+C(a,A)C(b,B)) is a clean reusable algebraic lemma; the delta-method formula (4) for <tau_A(m)tau_B(n)> over m N - n M = h.
- **Possible experiments.** Numerically verify Theorem 2 by computing both sides for small shift sets (|A|=|B|=2,3) with random small shifts, truncating the sum over M,N and d_i,q_i, e.g., test the local identity of Section 11.1 for random alpha,beta,gamma,delta in a power series check to order X^40. Also compare numerical mean square of tau_k-Dirichlet polynomials of length T^{2.5} against the recipe prediction.
- **Risks / barriers.** The shifted divisor problem lacks power-saving asymptotics for long convolutions; the paper delivers agreement of conjectural evaluations, not proof of moment asymptotics. Dependence on large X>T^2 where Dirichlet polynomial approximation of zeta^k fails for k large.

## Audit notes (Level 1 reader)

Extracted text garbles the displays of Theorem 2 and the formulas in Sections 4-6 (exponent placement); statements here must be checked against the PDF. The abstract/intro claim 'formula we obtain is in complete agreement with ... the recipe' holds for the identity (Theorem 2), but the conclusion's phrase 'asymptotic formula with power savings' depends on Conjecture 1 from CK3, which is not restated as a hypothesis in the abstract. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01799`; harvest queries: kw_moments_zeta, msc_11M06, msc_11M26, arxiv_critical_line, arxiv_moments_zeta.
- Triage decision: include — Divisor-correlation approach to moments of zeta, Type II sums.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
