# PAPER-0008 — Small values of the Euler function and the Riemann hypothesis

| Field | Value |
|---|---|
| Authors | Nicolas, Jean-Louis |
| Year / stratum | 2012 / S5 |
| Venue | Acta Arith. 155, No. 3, 311-321 (2012). |
| Identifiers | zbMATH [1272.11109](https://zbmath.org/?q=an:1272.11109) · DOI [10.4064/aa155-3-7](https://doi.org/10.4064/aa155-3-7) · arXiv [1202.0729](https://arxiv.org/abs/1202.0729) |
| MSC | 11N37, 11M26, 11N56 |
| Families | C |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1202.0729 |
| Selection | score 4.6179, in-pool citations 10, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Quantify Nicolas's 1983 equivalence (RH iff N_k/phi(N_k) > e^gamma loglog N_k for all k) by sharp two-sided bounds, under RH, for c(n)=(n/phi(n)-e^gamma loglog n) sqrt(log n), and show that failure of RH makes c(N_k) unbounded above and below.

**Historical motivation.** Rosser-Schoenfeld (1962) asked whether n/phi(n)>e^gamma loglog n occurs infinitely often; Nicolas (1983) answered yes and proved the primorial RH equivalence. This 2012 paper (for Schinzel's 75th birthday) makes the equivalence quantitative at the sqrt(log n) scale.

### Main results

- **THM-PAPER-0008-1** (Theorem 1.1 (1.4), theorem, scope: asymptotic; Section 1, Thm 1.1; proof in Section 4). Assume RH. Then $\limsup_{n\to\infty} c(n)=e^{\gamma}(2+\beta)=3.6444150964\ldots$, where $c(n)=\big(\frac{n}{\varphi(n)}-e^\gamma\log\log n\big)\sqrt{\log n}$ and $\beta=\sum_\rho \frac1{\rho(1-\rho)}=2+\gamma-\log\pi-2\log2=0.0461914179\ldots$ *Conditional on:* RH.
- **THM-PAPER-0008-2** (Theorem 1.1 (1.5), theorem, scope: conditional; Thm 1.1, proof Section 4). Under RH, for all $n\ge N_{120569}=2\cdot3\cdots1591883$, $c(n)<e^\gamma(2+\beta)$. *Conditional on:* RH, Maple 30-digit computation of c(N_k) for k<=50847534 (pi(10^9)).
- **THM-PAPER-0008-3** (Theorem 1.1 (1.6), theorem, scope: conditional; Thm 1.1). Under RH, for all $n\ge2$, $c(n)\le c(N_{66})=c(2\cdot3\cdots317)=4.0628356921\ldots$ *Conditional on:* RH, same computation.
- **THM-PAPER-0008-4** (Theorem 1.1 (1.7), theorem, scope: conditional; Thm 1.1; proof via (3.4) and computation). Under RH, for all $k\ge1$, $c(N_k)\ge c(N_1)=c(2)=2.2085892614\ldots$ *Conditional on:* RH.
- **THM-PAPER-0008-5** (Corollary 1.1, corollary, scope: asymptotic; Section 1, after (1.10)). Each of the four assertions (1.4)-(1.7) is equivalent to RH. If RH fails, $\liminf c(n)=-\infty$ and $\limsup c(n)=+\infty$ (via $\log f(x)=\Omega_\pm(x^{-b})$, some $0<b<1/2$, imported from Nicolas 1983 Th.3(c)).
- **THM-PAPER-0008-6** (Proposition 2.1, proposition, scope: conditional; Section 2, Prop 2.1). Under RH, for $x\ge x_0=10^9$, with $f(x)=e^\gamma\log\theta(x)\prod_{p\le x}(1-1/p)$ and $W(x)=\sum_\rho x^{i\Im\rho}/(\rho(1-\rho))$: $-\frac{2+W(x)}{\sqrt x\log x}+\frac{0.055}{\sqrt x\log^2x}\le\log f(x)\le-\frac{2+W(x)}{\sqrt x\log x}+\frac{2.062}{\sqrt x\log^2 x}$, and corresponding bounds (2.17) for $1/f(x)-1$. *Conditional on:* RH.
- **THM-PAPER-0008-7** (Proposition 3.1, proposition, scope: conditional; Section 3, Prop 3.1). Under RH, if $10^9\le p_k\le x<p_{k+1}$ then $e^\gamma(2+W(x))-\frac{3.7}{\log x}\le c(N_k)\le e^\gamma(2+W(x))-\frac{0.07}{\log x}$; in particular $c(N_k)\le e^\gamma(2+\beta)-0.07/\log x$ and $c(N_k)\ge e^\gamma(2-\beta)-3.7/\log x$. *Conditional on:* RH.
- **THM-PAPER-0008-8** (Section 4 remarks, remark/open, scope: asymptotic; end of Section 4). It is not known whether $\liminf W(x)=-\beta$; via Landau one only gets $\liminf W\le -1/(\rho_1(1-\rho_1))=-0.00499\ldots$. Challenges posed: find largest M<N_{k_1+1} with $c(M)\ge e^\gamma(2+\beta)$ ($k_1=120568$), and all n<N_{k_1+1} with c(n)>e^\gamma(2+\beta); and, if RH fails, bound the first k>k_0 with c(N_k) outside the range.

### Key definitions

- $N_k=\prod_{j\le k}p_j$ primorial
- $c(n)=(n/\varphi(n)-e^\gamma\log\log n)\sqrt{\log n}$
- $f(x)=e^\gamma\log\theta(x)\prod_{p\le x}(1-1/p)$, so for $p_k\le x<p_{k+1}$: $f(x)=e^\gamma\log\log(N_k)\,N_k/\varphi(N_k)$ inverse-style identity as in text
- $\beta=\sum_\rho 1/(\rho(1-\rho))$ (Edwards p.159), $|W(x)|\le\beta$ under RH
- $K(x),J(x),F_z(x)$ integrals (1.15)-(1.17) of $S(t)=\theta(t)-t$, $R(t)=\psi(t)-t$ against $1/\log t+1/\log^2t$

### Principal lemmas

- **THM-PAPER-0008-L1** (Lemma 2.1 (=Prop.1 of Nicolas 1983); Section 2). For $x\ge121$: $K(x)-\frac{S^2(x)}{x^2\log x}\le\log f(x)\le K(x)+\frac1{2(x-1)}$. — *Role:* Reduces log f to the integral K of theta-error
- **THM-PAPER-0008-L2** (Lemma 2.2; Section 2). For $\Re z<1$, $F_z(x)=\frac{x^{z-1}}{(1-z)\log x}+r_z(x)$; if $\Re z=1/2$, $|r_z(x)|\le\frac{1}{|1-z|\sqrt x\log^2x}(1+\frac4{\log x})$; explicit bounds (2.4) for z=1/2 and (2.5) for z=1/3. — *Role:* Explicit evaluation of zero contributions in the explicit formula
- **THM-PAPER-0008-L3** (Lemma 2.3; Section 2). Explicit monotonicity of $H(x)=1+\sum_{k=4}^{\kappa}x^{1/k-1/3}$ for $x\ge2^j,j\ge9$ and $L(x)=\sum_{k=2}^\kappa T(x^{1/k})/x^{1/3}$ for $x\ge 2^j, j\ge35$. — *Role:* Technical input for Lemma 2.4
- **THM-PAPER-0008-L4** (Lemma 2.4; Section 2). Under RH, $\psi(x)-\theta(x)\ge\sqrt x$ for $x\ge121$, and for $x\ge1$: $(\psi(x)-\theta(x)-\sqrt x)/x^{1/3}\le1.332768\ldots\le4/3$ (the latter unconditional in origin: Robin 1984 Lemma 3; here reproved). — *Role:* Controls $J-K$, i.e. prime-power contribution
- **THM-PAPER-0008-L5** (Lemma 2.5; Section 2). Under RH for $x>1$: $J(x)=-\frac{W(x)}{\sqrt x\log x}-J_1(x)-J_2(x)$ with $0<J_1\le\frac{\log2\pi}{x\log x}$, $|J_2|\le\frac{\beta}{\sqrt x\log^2x}(1+4/\log x)$. — *Role:* Explicit-formula expression of J in terms of the oscillating sum W
- **THM-PAPER-0008-L6** (Lemma 3.1; Section 3). If $n\ge2$ and either $\omega(n)=k$ or $N_k\le n<N_{k+1}$ then $c(n)\le c(N_k)$. — *Role:* Reduces sup over n to primorials (monotone-in-n argument with Rosser-Schoenfeld (1.1))

### Proof architecture

Section 2: Nicolas's inequality (Lemma 2.1) bounds log f via K(x); J-K controlled by Lemma 2.4 (prime powers) and Cor 2.1; J expressed through the explicit formula under RH (Lemma 2.5), leaving the oscillating term W(x)/(sqrt(x) log x) with |W|<=beta. Prop 2.1 gives explicit two-sided bounds for log f and 1/f-1 for x>=10^9. Section 3: Lemma 3.1 reduces c(n) to c(N_k); Prop 3.1 converts f to c(N_k) using (1.14) and Schoenfeld's RH bound (1.12) for theta. Section 4: limsup W(x)=beta by Dirichlet/Kronecker pigeonhole argument (imported, Ellison-Mendes France / Hardy-Wright); for k<=pi(10^9) c(N_k) computed numerically in Maple (30 digits), for k>pi(10^9) Prop 3.1 gives the bounds; equivalence with RH from Omega_+- of log f when RH fails.

Dependency edges: CAND-01199 → Nicolas 1983 J. Number Theory 17 (sharpens/refines); CAND-01199 → Robin 1984 (J. Math. Pures Appl. 63) (uses Lemma 3 / parallel sigma(n) criterion); CAND-01199 → Schoenfeld 1976 (imports explicit RH bound for theta)

**Imported results.** Nicolas 1983 (J. Number Theory 17): RH iff N_k/phi(N_k)>e^gamma loglog N_k for all k; Prop.1 (Lemma 2.1), Prop.2, Th.3(c) Omega_+- statement; Schoenfeld 1976 (6.3): |theta(x)-x|<= sqrt(x) log^2 x/(8 pi) for x>=599 under RH; Dusart: theta(x)<x for x<=8e11; Rosser-Schoenfeld 1962: Th.10 (theta>=0.84x), Th.15 (n/phi(n)<=e^gamma loglog n+2.51/loglog n); Landau 1903 limsup n/(phi(n) loglog n)=e^gamma; limsup W(x)=beta via pigeonhole (Nicolas 1983 p.383)

**Techniques.** explicit formula for psi/theta under RH; partial summation and integral representations K,J,F_z; Schoenfeld explicit RH bound |theta(x)-x|<=sqrt(x) log^2 x/(8 pi); pigeonhole/Kronecker for limsup of W; finite computation up to 10^9 primes; monotonicity reduction to primorials

## Context and interpretation

**Importance and obstacle overcome.** Turns a qualitative sign-criterion into an exact asymptotic constant: under RH the second-order term of n/phi(n)-e^gamma loglog n at primorials is governed by the oscillating sum W(x), with sup exactly e^gamma(2+beta); the obstacle was making the explicit-formula analysis effective enough (x_0=10^9) to leave a finite computable range, and getting four new RH-equivalent statements (1.4)-(1.7).

**Relation to prior work.** 

**Limitations and open questions.** Whether liminf W(x)=-beta is unknown (only liminf W<=-0.00499); lim inf c(N_k) not determined. Conditional on RH for all quantitative bounds; (1.5),(1.6) rely on a non-certified 30-digit Maple computation up to k=50,847,534 (author says 'we may think the first ten are correct'). Open challenges: largest M<N_{120569} with c(M)>=e^gamma(2+beta); all such n; effective threshold k if RH fails.

## Research potential

- **Hypotheses that might be weakened.** Prop 3.1 and Lemma 2.5 use RH only through zero-sum bounds |W|<=beta and Schoenfeld's theta bound; one could replace RH by a zero-free-region/density hypothesis (zeros with real part <=1/2+delta) to obtain quantitative failure-detection windows, answering the author's final question (bound on first k witnessing failure) in terms of a hypothetical zero rho0 with beta0>1/2.
- **Generalizations.** Same scheme should treat the sigma-analogue (Robin, sigma(n)/(n loglog n)) at superabundant/colossally abundant numbers and Dedekind-psi, giving analogous limsup constant e^gamma(2+beta) with different lower-order terms; also general primorial-type products over primes in progressions (GRH for L(s,chi)) replacing beta by sum 1/(rho(1-rho)) over L-zeros.
- **Candidate connections.** W(x)=sum x^{i gamma}/(rho(1-rho)) is an almost-periodic function of log x; its liminf question (liminf W=-beta?) is a Kronecker/linear-independence-of-ordinates problem and links to Ingham-type oscillation arguments (Mertens, Pintz); also to Robin-Nicolas programme in PROGRAMMES.md (Robin arithmetic).
- **Reusable lemmas.** Lemma 3.1 (c(n)<=c(N_k) via omega(n) or size) and Lemma 2.4 (psi-theta>=sqrt x, explicit) are reusable; Lemma 2.2 gives explicit bounds for F_z, reusable for any explicit-formula-with-1/log weights.
- **Possible experiments.** Recompute c(N_k) for k<=pi(10^9) with interval arithmetic to certify (1.5)-(1.7) and the value k_1=120568; compute W(x) numerically with first ~10^4 zeros to estimate liminf W and test whether -beta is approached; search n<N_{120569} for c(n)>=e^gamma(2+beta) as the author's challenge.
- **Risks / barriers.** Without RH the bounds are vacuous (Omega_+- from a hypothetical off-line zero gives no effective k); liminf W requires independence of zero ordinates, unproven; finite computation is not certified.

## Audit notes (Level 1 reader)

Computation behind (1.5)-(1.7) for k<=k_0 uses 30-digit Maple floating point, not interval arithmetic (Section 4, p.10-11); the paper says 'we may think that the first ten are correct'. This is not a rigorously certified finite check; the reported margins (c(N_k1)=3.6444180 vs threshold 3.6444151) are ~3e-6 so rely on ~10 digits. Equivalence statements in Corollary 1.1 rely on unconditional Omega_+- result of Nicolas 1983 Th.3(c) (imported, not reproved). Text extraction loses the exponent in W(x) definition (1.18); otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01199`; harvest queries: kw_RH_any, msc_11M26, msc_11N56_rh, arxiv_rh_abs, arxiv_rh_ti.
- Triage decision: include — Refinement of Robin-type criteria via small values of phi on primorials.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
