# PAPER-0040 — Numerical computations concerning the GRH

| Field | Value |
|---|---|
| Authors | Platt, David J. |
| Year / stratum | 2016 / S6 |
| Venue | Math. Comput. 85, No. 302, 3009-3027 (2016). |
| Identifiers | zbMATH [1345.11064](https://zbmath.org/?q=an:1345.11064) · DOI [10.1090/mcom/3077](https://doi.org/10.1090/mcom/3077) · arXiv [1305.3087](https://arxiv.org/abs/1305.3087) |
| MSC | 11M26, 11M06, 11P32 |
| Families | B, E |
| Work type | computation_report |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1305.3087 |
| Selection | score 4.5776, in-pool citations 18, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Rigorously verify the Generalised Riemann Hypothesis for Dirichlet L-functions of primitive characters up to large modulus and height, by designing two new rigorous (interval-arithmetic) algorithms, one for large q (DFT over characters of Hurwitz-zeta lattice) and one for small q (Booker's Fourier method specialised to Dirichlet L-functions).

**Historical motivation.** Rumely's numerical GRH verification; the need for large rigorous GRH checks for ternary Goldbach (Helfgott); Odlyzko-Schonhage fast zeta evaluation; Booker's algorithm for rigorous L-function computation.

### Main results

- **THM-PAPER-0040-1** (Theorem 7.1, theorem (computational), scope: computational; Section 7, p.14). GRH holds for Dirichlet L-functions of primitive character modulus $q\le 400{,}000$ up to height $t_0=\max\big(\tfrac{10^8}{q},\tfrac{7.5\cdot10^7}{q}+200\big)$ for even $q$ and $t_0=\max\big(\tfrac{10^8}{q},\tfrac{3.75\cdot10^7}{q}+200\big)$ for odd $q$, i.e. every zero of $L_\chi(s)$ with $|\Im s|\le t_0$ and $0<\Re s<1$ lies on $\Re s=1/2$. Checked 29,565,923,837 L-functions, isolating about $3.8\cdot10^{13}$ zeros (excluding those used in Turing's method).
- **THM-PAPER-0040-2** (Theorem 7.2, theorem (computational), scope: computational; Section 7, p.15). For every Dirichlet L-function of primitive character of modulus $q\le2{,}000{,}000$, $L_\chi(1/2)\ne0$ (checked for 739,151,526,102 primitive characters; 438,152 double-precision-interval straddles of zero were resolved by interval Euler-Maclaurin, the final 20 using MPFI at 100 bits).
- **THM-PAPER-0040-3** (Lemma 4.1, lemma (algorithmic), scope: computational; Section 4). For $q\ge3$ and given $\varphi(q)$ complex values $a(n)$, $n\in[1,q-1]$, $(n,q)=1$, the sums $\sum_{n=1}^{q-1}a(n)\chi(n)$ can be computed for all $\varphi(q)$ characters $\chi$ in $O(\varphi(q)\log q)$ time and $O(\varphi(q))$ space (via CRT decomposition of $U(\mathbb Z/q)$ and FFT incl. Bluestein for prime lengths).
- **THM-PAPER-0040-4** (Theorem 3.1 (Booker) / Theorem 3.2 / Theorem 3.3 (Rumely), imported theorems (Turing method), scope: computational; Section 3). Booker: for an L-function of degree $r$ with Euler product, $N(t)=\Phi(t)+S(t)$ gives the net zero count in $[t_1,t_2)$. Theorem 3.2 (integrated form): $N_\chi(t_0)$ expressed via $\frac{1}{h\pi}\big[2h+\frac{2ht_0+h^2}{2}\log\frac q\pi+2\int\Im\log\Gamma(\frac{1/2+a_\chi+it}2)dt-\ldots\big]$ with error integrals of $S_\chi$. Rumely (Thm 3.3): for $t_0>50$, $h>0$, $|\int_{t_0}^{t_0+h}S_\chi(t)dt|\le1.8397+0.1242\log\frac{q(t_0+h)}{2\pi}$; Trudgian's constants (2.17618, 0.0679955), optimised for $qt_0\approx10^8$, are noted.
- **THM-PAPER-0040-5** (Theorem 6.1 / Theorem 6.2 / Lemmas 6.3-6.7, rigorous up-sampling, scope: computational; Section 6). Whittaker-Shannon sampling theorem and Weiss's error bound used to rigorously up-sample $\Lambda_\chi$ from coarse samples (step 5/64 of mean zero spacing about 1/5 density) to the sign-change test, with explicit tail/aliasing error bounds (Lemmas 6.3-6.7); not read in full detail.

### Key definitions

- Primitive Dirichlet character, parity $a_\chi\in\{0,1\}$
- Completed L-function $\Lambda_\chi(t)$, real for suitable $\epsilon_\chi$
- $S_\chi(t)=\frac1\pi\Im\int_\infty^{1/2}\frac{L'_\chi}{L_\chi}(\sigma+it)d\sigma$
- DFT definition (Definition 2.1) and Fourier transform normalisation $F(x)=\frac1{2\pi}\int f(t)e^{-ixt}dt$

### Principal lemmas

- **THM-PAPER-0040-L1** (Lemma 4.1; Section 4). FFT computation of $\sum a(n)\chi(n)$ over all characters mod $q$ in $O(\varphi(q)\log q)$ time. — *Role:* Core of the large-q algorithm: all $L_\chi(s)$ computed simultaneously through Hurwitz zeta $\zeta(s,a/q)$ lattice (Lemma 4.2 Taylor expansion).
- **THM-PAPER-0040-L2** (Lemma 4.2; Section 4). For $s\notin\mathbb Z_{\le0}$, $\alpha\in(0,1]$, $|\delta|<\alpha$: Taylor/Euler-Maclaurin-type expansion of $\zeta(s,\alpha+\delta)$ about $\alpha$ (statement only skimmed). — *Role:* Allows a precomputed lattice of $\zeta(1/2+it+c,r/D)$ to supply all $a/q$ values by interpolation.
- **THM-PAPER-0040-L3** (Lemma 5.4 (Booker); Section 5). Decay/aliasing estimate for the Fourier transform of the completed L-function with parameter $\eta\in(-1,1)$, $\delta=\frac\pi2(1-|\eta|)$ (Lemma 5.6 of Booker specialised). — *Role:* Rigorous truncation error in the small-q algorithm.
- **THM-PAPER-0040-L4** (Lemmas 5.1-5.3, 5.5, 5.6; Section 5). Bounds for the Fourier-side gamma factors and error terms of the rigorous computation of $\hat F_{e/o}(x,\chi)$ and of $L_\chi$ on vertical lines (Lemma 5.3 gives bound on $L_\chi$); not read in detail. — *Role:* Error control for the rigorous DFT approximation.
- **THM-PAPER-0040-L5** (Lemmas 6.3-6.7; Section 6). Explicit bounds converting the discrete DFT output to guaranteed enclosures of $\Lambda_\chi(t)$ (including the Weiss band-limited error term and the final combined bound). — *Role:* Final rigorous enclosure used for sign-change counting.

### Proof architecture

Zeros on the line are certified by sign changes of the real-valued completed function Lambda_chi(t)=eps_chi (q/pi)^{it/2} Gamma((1+a+it)/2) exp(pi t/4) L_chi(1/2+it) (exp(pi t/4) factor counteracts Gamma decay). Total number of zeros in a rectangle is obtained from Turing's method (Booker's Thm 3.1/3.2, with Rumely/Trudgian's bound on integrals of S_chi): if the number of sign changes found on [0,t0] equals the Turing-method count, no zeros are off the line. Two algorithms compute Lambda_chi on a grid of sampling step ~ 5/64... (5 times the mean density): (a) large q: for each fixed q express L_chi(s)=q^{-s} sum_a chi(a) zeta(s,a/q), compute Hurwitz zeta values by a precomputed lattice for rational points in a Taylor expansion (Lemma 4.2), then evaluate all characters mod q simultaneously with an FFT over U(Z/q) (Lemma 4.1) - O(phi(q) log q) per t; (b) small q: Booker's method specialised: sample Fourier transform F-hat on a lattice, aliasing sums via DFT (Theorem 2.2, Poisson-type), giving samples of Lambda_chi on a fine grid with rigorous truncation error (Lemmas 5.x). Rigorous up-sampling (Section 6) uses Whittaker-Shannon (Thm 6.1) plus Weiss's error bound (Thm 6.2) to obtain enclosures between samples. Section 7: grid steps 5/64 of... then up-sample by 8, then 32, 128, 512; remaining 0.0003% of L-functions are resolved with interval-arithmetic Euler-Maclaurin (double precision, occasionally MPFI at 100 bits), handling indeterminate-sign cases, sign-uncertainty at the centre, and mis-bracketed Turing counts. Arithmetic: floating-point with rigorous error bounds in double precision (interval arithmetic) and MPFI for fallback; Sections 5.1-6 error-term derivations were not verified line by line.

Dependency edges: CAND-01805 → Booker 2006 (rigorous L-function algorithm) (specialises); CAND-01805 → Rumely 1993 (extends); CAND-01805 → Helfgott ternary Goldbach (supports (numerical input))

**Imported results.** Booker 2006: Theorem 3.1 (Turing's method for general L-functions), Lemma 5.4/5.6 (Fourier decay estimates); Rumely 1993, Theorem 2: bound for the integral of S_chi (Theorem 3.3); Trudgian 2011: improved Turing constants; Whittaker-Shannon sampling theorem and Weiss's error estimate (Theorems 6.1, 6.2); Bluestein FFT algorithm

**Techniques.** Turing's method (Booker, Rumely, Trudgian); FFT/DFT on characters via CRT (including Bluestein for prime lengths); Hurwitz zeta lattice with Taylor expansion; Booker's rigorous Fourier-transform algorithm for L-functions; Whittaker-Shannon sampling with Weiss's rigorous error bound; interval arithmetic (double precision, MPFI 100 bits) with Euler-Maclaurin fallback; massive parallel computation (about 400,000 core hours)

## Context and interpretation

**Importance and obstacle overcome.** Extends Rumely's 1993 GRH verification (q<=13 to height 1e4, about 1e7 zeros) by roughly 6 orders of magnitude in zeros (3.8e13 zeros), sufficient to support Helfgott's proof of ternary Goldbach (explicit-formula/minor-arc input). Obstacle: computing all phi(q) L-functions per modulus at heights up to 1e8/q for large q; solved by the DFT-over-characters trick combined with a Hurwitz-zeta lattice reused across q.

**Relation to prior work.** Builds on Rumely (1993; Turing method bound Theorem 3.3), Trudgian (improved Turing constants), Booker (Artin's conjecture, Turing's method and the Riemann hypothesis, Experiment. Math. 2006; Thm 3.1, Lemma 5.4), Odlyzko-Schonhage and Gourdon (zeta zeros to 1e13).

**Limitations and open questions.** Finite verification (primitive characters, modulus <= 400,000, height max(1e8/q, ...)): no information on larger q or heights, no global GRH evidence; Theorem 7.2 only shows L(1/2,chi) != 0 for q <= 2e6. Execution is by floating-point sampling at density ~5x mean zero density with rigorous interval enclosures; the computation relies on software run on clusters (ECC memory used for the small-q algorithm for q <= ~10,000 and large-q algorithm beyond; so not every modulus was run twice). The paper does not publish the raw computed data. Non-primitive characters are not treated (they follow from primitive ones for the associated L-function up to Euler factors, standard but not discussed here as far as read).

## Research potential

- **Hypotheses that might be weakened.** The height max(1e8/q, 7.5e7/q+200) is determined by the computational budget, not by method limits; the primitivity condition could be extended to ranges of imprimitive characters (follows from primitive-factor). Repeating with independent implementation at the 5x density would remove the single-run dependence for large q.
- **Generalizations.** Rigorous verification for higher-degree L-functions (GL(2) modular forms, Dedekind zeta) via Booker's framework (Theorem 3.1 is stated for degree r); verifying GRH in rectangles of different aspect q by t trade-off (t0 ~ 1e8/q suggests a norm 'q*t0 <= 1e8').
- **Candidate connections.** Locality/complement theorem question (see AGENTS.md boundaries): this result is a finite certificate per (q,t0) and must not be used as global evidence; combine with explicit-formula Goldbach-type minor-arc bounds (Helfgott) and with zero-density estimates; compare against exceptional-character (Siegel zero) exclusions for q<=4e5 (L(1/2,chi)!=0 up to 2e6 is a distinct statement).
- **Reusable lemmas.** Lemma 4.1 (FFT over characters of U(Z/q)) is reusable for any character-sum evaluation (e.g. checking Gauss/Jacobi sums, computing L(1,chi) for all chi mod q); Theorem 3.2 (integrated Turing counting formula) for any degree-1 family.
- **Possible experiments.** Reproduce a small slice: q<=200, t0=1e4, with an independent interval-arithmetic implementation (e.g. Arb) and the Turing count test to audit the pipeline end-to-end; measure the proportion of L-functions needing the high-precision fallback (reported about 0.0003%).
- **Risks / barriers.** Completeness of coverage (every primitive character mod every q<=400000 checked?) depends on bookkeeping and cluster runs, not on a theorem; artifact data not published in the paper, so no independent replay of the primitive data is possible from the source alone; interval arithmetic claims rely on the author's implementation (double-precision intervals plus MPFI).

## Audit notes (Level 1 reader)

Heights: the abstract and Theorem 7.1 formulas agree. The text states the sampling step as 5/64 'representing a sampling rate of about 5 times the expected zero density' (extraction of the fraction was garbled; I did not verify the 5/64 value). The paper counts 29,565,923,837 L-functions; I did not independently verify that this equals the number of primitive characters up to 4e5. Sections 5.1-6 error lemmas not verified line by line. 'Zeros isolated 3.8e13 (not counting those used in Turing's method)' is the author's count. No other issue noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01805`; harvest queries: kw_GRH, kw_RH_any, msc_11M06, msc_11M26, arxiv_rh_abs.
- Triage decision: include — Rigorous GRH verification for Dirichlet L-functions up to modulus 400000.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
