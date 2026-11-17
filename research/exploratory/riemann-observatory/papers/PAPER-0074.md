# PAPER-0074 — On a representation of the idele class group related to primes and zeros of \(L\)-functions

| Field | Value |
|---|---|
| Authors | Meyer, Ralf |
| Year / stratum | 2005 / S5 |
| Venue | Duke Math. J. 127, No. 3, 519-595 (2005). |
| Identifiers | zbMATH [1079.11044](https://zbmath.org/?q=an:1079.11044) · DOI [10.1215/S0012-7094-04-12734-4](https://doi.org/10.1215/S0012-7094-04-12734-4) · arXiv [math/0311468](https://arxiv.org/abs/math/0311468) |
| MSC | 11M26, 22D12, 43A35, 58B34 |
| Families | D, E |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/math/0311468 |
| Selection | score 4.4822, in-pool citations 16, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Construct a virtual representation pi=pi_+ - pi_- of the idele class group C_K of a global field on nuclear bornological spaces whose spectrum is the set of poles and zeros of the complete L-function and whose character equals the (raw) Weil distribution, thereby giving a spectral interpretation of the explicit formula that is not biased to the critical line.

**Historical motivation.** Connes' 1999 spectral interpretation singled out the critical line (zeros off the line appear as resonances) and left the global trace formula unproved; Meyer instead builds an unbiased representation capturing all zeros and poles equally, making the explicit formula a character identity and avoiding the unproved geometric computation.

### Main results

- **THM-PAPER-0074-1** (Theorem 5.8, theorem, scope: global; Sect. 5, Thm 5.8). The global difference representation $\pi$ of $C_K$ is smooth and summable and its character is the raw Weil distribution $W$: $W(f)=\chi_\pi(f)=\sum_{\omega\in\Omega(C_K)}\mathrm{mult}(\omega,\pi)\hat f(\omega)$, with uniform absolute convergence for $f$ in bounded subsets of $\mathcal D(C_K)$, where $W(f)=\sum_{v}\int'_{K_v^\times}\frac{f(x)|x|}{|1-x|}d^\times x-f(1)\ln D_K$.
- **THM-PAPER-0074-2** (Theorem 5.11, theorem, scope: global; Sect. 5, Thm 5.11). The spectrum of $\pi$ consists of the poles and zeros of $L_K:\Omega(C_K)\to\mathbb C$ (complete L-function as function of quasi-characters, $L_K(\chi|x|^s)=L(\chi,s)$) and $\mathrm{mult}(\omega,\pi)=\mathrm{ord}(\omega,L_K)$ for all $\omega$; poles appear in $\pi_+$ (2-dim, spec $\{1,|x|\}$), zeros in $\pi_-$.
- **THM-PAPER-0074-3** (Theorem 5.1, theorem, scope: global; Sect. 5 (Thm 5.1, proved via Sect. 4)). For $S$ sufficiently large there are natural isomorphisms $\mathbb C(1)\hat\otimes^L_{\mathcal D(K^\times)}\mathcal S(\mathbb A_K)^S\cong\mathbb C(1)\hat\otimes^L\mathcal S(\mathbb A_S)\cong T(C_S)$ in the derived category of smooth $\mathcal D(C_K)$-modules; in particular $H_+^S\cong T(C_S)$ and higher homology $H_n(K^\times,\mathcal S(\mathbb A_K))=0$ for $n\ge1$.
- **THM-PAPER-0074-4** (Theorem 6.3, theorem, scope: global; Sect. 6). Any $\chi\in\mathrm{spec}\,\pi_-$ satisfies $0<\mathrm{Re}\,\chi<1$ (no zeros on the boundary of the critical strip), via a reformulation of Deligne's abstract Hadamard-de la Vallee-Poussin argument with the Bohr compactification of $C_K$ and GNS construction.
- **THM-PAPER-0074-5** (Theorem 6.5, theorem, scope: asymptotic; Sect. 6, Thm 6.5). Generalized PNT: with $S$ large, prime ideals of $O_S$ viewed as a discrete subset of $C_S$, for open $A\subseteq C_S^1$ and $\pi_A(\xi)=\#\{$prime ideals in $A\times[1,\xi]\}$, $\pi_A(\xi)\approx\mathrm{vol}(A)\,\xi/\ln\xi$ as $\xi\to\infty$ (Chebotarev-type equidistribution).
- **THM-PAPER-0074-6** (Introduction (modified Weil distribution), proposition, scope: conditional; Sect. 1 p.2). The modified Weil distribution $f\mapsto\hat f(|x|^{-1/2})+\hat f(|x|^{1/2})-W(f|x|^{-1/2})=\chi_{\pi_-}(f|x|^{-1/2})$ is positive definite iff $\mathrm{spec}\,\pi_-\subset|x|^{1/2}\widehat{C_K}$, equivalent to GRH. Meyer does not prove positivity.

### Key definitions

- virtual representation pi=pi_+ (-) pi_-
- H_+=S(A_K)/K^x, H_-=S(C_K)_{]-inf,inf[}
- summable representation
- T(C_S)=S(C_S)_{]0,inf[} cap F(S(C_S)_{]-inf,1[})
- raw Weil distribution W
- modified Weil distribution

### Principal lemmas

- **THM-PAPER-0074-L1** (Lemma 3.3; Sect. 3). For $f\in\mathcal S(C_S)_{1/2}$ the operators $\int\lambda(f)T$ and $T\int\lambda(f)$ on $L^2(C_S)_{1/2}$ are uniformly nuclear and $\mathrm{tr}(\int\lambda(f)T)=\mathrm{tr}(T\int\lambda(f))=\tau(\mathcal F\partial(\mathcal F^*f))$ (local trace formula, essentially Connes'), where $T=M_\phi-\mathcal F M_\phi\mathcal F^*$. — *Role:* Local trace formula in Hilbert-space setting.
- **THM-PAPER-0074-L2** (Lemma 5.5; Sect. 5). $i_+(H_+)+i_-(H_-)=\{(f_0,f_1)\in\mathcal S(C_K)_{><}: f_0-f_1=c_0-c_1|x|^{-1}\}$; hence $\pi_+$ is 2-dimensional (consequence of Poisson summation). — *Role:* Identifies the poles $\{1,|x|\}$.
- **THM-PAPER-0074-L3** (Lemma 5.6; Sect. 5). For $\alpha>1$, $\int\lambda(f)(P_--P_+^S)$ and $(P_--P_+^S)\int\lambda(f)$ extend to uniformly nuclear operators $L^2(C_S)_\alpha\oplus L^2(C_S)_{1-\alpha}\to\mathcal S(C_K)_{><}$ for $f\in\mathcal D(C_S)$. — *Role:* Key estimate for summability of pi and trace computation using auxiliary operators P_pm.
- **THM-PAPER-0074-L4** (Lemma 4.2/4.3/Prop. 4.4, Thm 4.12; Sect. 4). Bornological extension and isocohomological properties of Bruhat-Schwartz algebras S(G); S(G) is isocohomological for every such G. — *Role:* Homological machinery used to prove S(A_K)/K^x ~ T(C_S).
- **THM-PAPER-0074-L5** (Theorems 2.5, 2.10, 2.12, 2.14; Sect. 2). Summable representations: character computable both spectrally (sum of eigenvalues) and traciallly; summability hereditary under smoothening, contragradients, subquotients. — *Role:* Abstract framework needed for trace = spectral sum.

### Proof architecture

Define H_+ = S(A_K)/K^x (coinvariants), H_- = S(C_K)_{]-inf,inf[}; embed both equivariantly into S(C_K)_{><} (omits critical strip) via i_+(f)=(Sigma f, J Sigma F f) and i_-(f)=(f,f); take pi_+=(H_++H_-)/H_-, pi_-=(H_++H_-)/H_+. Section 2 sets up nuclearity/summability on bornological spaces; Sect. 3-4 prove S-local trace formula (Connes-like) without Hilbert spaces; Sect. 5 proves summability and the character formula by combining the S-local trace formula with a global term from places outside S that annihilates a given f for S large; spectrum identified through functionals on H_-/(H_+ cap H_-) (Fourier-Laplace transform; the ideal H_+ cap H_- = holomorphic functions vanishing to order ord(omega,L) at zeros). Sect. 6 proves no zeros on boundary (Deligne's argument) and a PNT generalization from pi.

**Imported results.** Weil explicit formula (Weil 1952/1972) equals character equation identification; Poisson summation / Tate functional equation; Deligne's abstract Hadamard-de la Vallee-Poussin argument ([5], Weil II style); Bruhat's Schwartz-Bruhat function theory ([1]); Connes' local trace formula ([4], Thm VII.4)

**Techniques.** bornological vector spaces and nuclear/order-0 operators; summable representations, character of virtual representations; derived functors and isocohomological algebras; Tate-thesis style Fourier analysis on adeles/ideles; Poisson summation; Fourier-Laplace transform to holomorphic functions on Omega(C_K); Bohr compactification and GNS (Hadamard-de la Vallee-Poussin via Deligne)

## Context and interpretation

**Importance and obstacle overcome.** Provides a rigorous global construction (with all zeros/poles and rigorous trace formula) that Connes could only do S-locally, at the cost of losing any connection to RH. Obstacle overcome: global term from places outside S and non-unitarity (multiple/off-line zeros), handled by nuclear bornological spaces and virtual representation.

**Relation to prior work.** Motivated by Connes (CAND-00726); follows Tate's thesis and Deligne's argument; the S-local part is essentially equivalent to Connes' local trace formula; later work: Connes-Consani-Marcolli endomotives (CAND-01520).

**Limitations and open questions.** No connection to RH: the position of spec pi_- (positivity of modified Weil distribution) not controlled; Sect. 6 only gives 0<Re<1 and PNT, no bounds on vertical/horizontal zero position; pi not unitary. Geometric (Lefschetz) interpretation of the character as in Connes remains open.

## Research potential

- **Hypotheses that might be weakened.** Summability definition requires f in D(C_K) with compact support; one could test whether the same character formula holds for larger test-function classes (e.g. f with controlled growth) to reach Weil positivity cone f*f^sharp.
- **Generalizations.** Replace C_K by GL_n adele classes or by Artin-type L-functions with Hilbert/Banach completion of pi_-; analogue for Selberg zeta; relative version with Weil group.
- **Candidate connections.** Connes trace formula (CAND-00726), CCM Weil positivity section 5.4 (CAND-01520), de Branges spaces (CAND-01512): the decomposition H_+ ∩ H_- as ideal of holomorphic functions vanishing at zeros resembles de Branges-type subspace structure.
- **Reusable lemmas.** Lemma 5.5 (structure of H_++H_- via Poisson), Lemma 5.6 uniform nuclearity of P_- - P_+^S, and Theorem 6.3 abstract no-zeros-on-boundary argument as template.
- **Possible experiments.** For K=Q, discretize C_S with S={inf,2,3}, compute numerically the S-local trace tr(int lambda(f) T) for test f and compare to the explicit-formula local terms; verify convergence of W(f) as S grows.
- **Risks / barriers.** Positivity of pi_- character is exactly GRH; construction gives no handle on it. Heavy bornological machinery limits reuse.

## Audit notes (Level 1 reader)

Extraction rendered 'c' ligature missing (e.g. 'Introdu tion'), harmless. Intro says 'Given the Explicit Formula ... a geometric computation of the character in Connes' situation is equivalent to GRH'. Statement of Theorem 6.5 precise hypotheses on A not read. none noticed otherwise in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01282`; harvest queries: kw_GRH, kw_RH_any, kw_trace_formula_zeta, kw_zeta_zeros, msc_11M26, arxiv_explicit_formula, arxiv_weil_explicit.
- Triage decision: include — Spectral interpretation of zeros via idele class group representation.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
