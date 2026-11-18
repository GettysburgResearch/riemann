# PAPER-0101 — Aspects of the screw function corresponding to the Riemann zeta-function

| Field | Value |
|---|---|
| Authors | Suzuki, Masatoshi |
| Year / stratum | 2023 / S6 |
| Venue | J. Lond. Math. Soc., II. Ser. 108, No. 4, 1448-1487 (2023). |
| Identifiers | zbMATH [1536.11133](https://zbmath.org/?q=an:1536.11133) · DOI [10.1112/jlms.12785](https://doi.org/10.1112/jlms.12785) · arXiv [2206.03682](https://arxiv.org/abs/2206.03682) |
| MSC | 11M26, 42A82, 47G10 |
| Families | C, D |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/2206.03682 |
| Selection | score 4.312, in-pool citations 5, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Define an explicit real function Psi(t) (built from von Mangoldt sum plus gamma-factor terms) whose negative -Psi is a Krein screw function iff RH; derive Weil-positivity, Yoshida non-degeneracy, Hankel-moment, boundedness, pointwise positivity and Li-coefficient reformulations of RH, plus unconditional partial results.

**Historical motivation.** Krein's screw lines; Weil's positivity criterion, Li's criterion, Yoshida and Bombieri non-degeneracy; seeks an analytic-operator formulation on ordinary L^2 spaces with continuous kernel.

### Main results

- **THM-PAPER-0101-1** (Theorem 1.1, unconditional theorem, scope: global; Sec.1, Thm 1.1; proof Sec.2). With $\Psi(t)=4(e^{t/2}+e^{-t/2}-2)-\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n)+\big(\frac{\Gamma'}{\Gamma}(\tfrac14)\tfrac t2-t\log\pi\big)\cdot$(precise form (1.1) incl. $\tfrac14(C-e^{-t/2}\Phi(e^{-2t},2,\tfrac14))$, $C=\pi^2+8G$): (1) $\int_0^\infty\Psi(t)e^{izt}dt=-z^{-2}\,\frac{\xi'}{\xi}(\tfrac12-iz)$ for $\Im z>1/2$; (2) $\Psi(t)=\sum_\gamma\frac{1-\cos\gamma t}{\gamma^2}$ over zeros of $\xi(1/2-iz)$ with multiplicity; (3) $\Psi(t)\ll\exp(t/2-c\sqrt t)$. (Formula (1.1) transcribed from source, paper should be consulted for exact constants.)
- **THM-PAPER-0101-2** (Theorem 1.2, equivalence, scope: global; Sec.1 (proof via Lagarias 1999 and Krein-Langer Satz 5.9)). RH holds iff $g=-\Psi$ is a screw function on $\mathbb R$ (Krein class $G_\infty$): $g$ even, continuous and $G_g(t,u)=g(t-u)-g(t)-g(-u)+g(0)$ non-negative definite.
- **THM-PAPER-0101-3** (Theorem 1.3, equivalence, scope: global; Sec.1; proof Sec.3 (Weil distribution)). RH holds iff $\langle\phi,\phi\rangle_{G_g,a}=\iint G_g(t,u)\phi(u)\overline{\phi(t)}dudt\ge0$ for all $\phi\in C_0(a)=\{\phi\in C_c^\infty,\ \mathrm{supp}\subset[-a,a],\int\phi=0\}$ and every $0<a<\infty$; under RH the form is positive definite on $L^2(-a,a)$.
- **THM-PAPER-0101-4** (Theorem 1.4, equivalence, scope: global; Sec.1; proved Sec.5 using Thms 4.1-4.3). RH holds iff the form is non-degenerate on $L^2(-a,a)$ for every $0<a<\infty$, i.e. the integral operator $G_g[a]$ has no zero eigenvalue for every $a$.
- **THM-PAPER-0101-5** (Theorem 1.5, unconditional theorem, scope: finite; Sec.1; proof Sec.6). For each $0<a<\infty$, $G_g[a]$ is trace class, with $\mathrm{Tr}\,G_g[a]=\int_{-a}^aG_g(t,t)dt$.
- **THM-PAPER-0101-6** (Theorems 1.6, 1.7, equivalence, scope: global; Sec.1; proofs Sec.7). RH iff $\Psi(t)=O(1)$ on $[0,\infty)$ (Thm 1.6); RH iff $\Psi(t)\ge0$ for all $t$, and then $\Psi(t)>0$ for $t\ne0$ (Thm 1.7). $\Psi\notin L^1\cup L^2$ unconditionally.
- **THM-PAPER-0101-7** (Theorem 1.8 / Theorem 8.1, equivalence + identity, scope: global; Sec.1; Sec.7.3; Sec.8). With $\mu_n=\int_0^\infty4^{-1}e^{-t/2}\Psi(t)t^ndt$ and Hankel matrices $\Delta_n=(\mu_{i+j})$, $\Delta_n^{(1)}=(\mu_{i+j+1})$: RH iff $\det\Delta_n\ge0$ and $\det\Delta_n^{(1)}\ge0$ for all $n$ (Stieltjes moment problem). Li coefficients: $\lambda_1=\mu_0$, $\lambda_2=6\mu_0-\mu_1$, $\lambda_3=19\mu_0-7\mu_1+\tfrac12\mu_2$, general formula (8.2) for $n\ge4$ with inverse.
- **THM-PAPER-0101-8** (Theorems 4.1, 4.2, 4.3, 6.1, 11.1, unconditional partial results, scope: local; Sec.4, 6, 11). 4.1: exists $t_0>\log2$ with $\Psi>0$ on $(0,t_0)$. 4.2: exists $a_0>0$ with $G_g$ positive definite on $L^2(-a,a)$ for $0<a<a_0$ (so $g|_{[-2a,2a]}\in G_a$). 4.3: for $a_0,\mu>0$ exists N with $\langle\phi,\phi\rangle\ge\mu\int|\Phi_1(\phi,z)|^2dz$ on $K_{N,0}(a)$. 6.1: if RH false, exists $a_0>0$ and nonzero $(w_\gamma)$ with $\sum w_\gamma(e^{i\gamma t}-1)/\gamma^2=0$ on $(-a_0,a_0)$. 11.1: for $\omega\in\mathbb R$, $\xi(s)\ne0$ for $\Re s>1/2+\omega$ iff $\Psi_\omega(t)\ge0$ for all $t\ge t_0$ for some $t_0>0$.

### Key definitions

- Psi(t) in (1.1), g=-Psi
- screw function class G_a (Krein) and kernel G_g
- hermitian form <.,.>_{G_g,a} on C_0(a)
- moments mu_n (1.13)
- Q_xi(z)=i(xi'/xi)(1/2-iz)
- variants Psi_omega (11.1)

### Principal lemmas

- **THM-PAPER-0101-L1** (Krein-Langer Satz 5.9 (imported); Sec.1). Bijection between screw functions $g\in G_\infty$, $g(0)=0$, and Nevanlinna Q with $Q(iy)/y\to0$ via $\int_0^\infty g e^{izt}dt=-iz^{-2}Q(z)$. — *Role:* Engine of Thm 1.2.
- **THM-PAPER-0101-L2** (Lagarias 1999 (imported); Sec.1). RH iff $\Im\,i(\xi'/\xi)(1/2-iz)>0$ for $\Im z>0$. — *Role:* Shows Q_xi is Nevanlinna iff RH.
- **THM-PAPER-0101-L3** (Proposition 2.1; Sec.2). Estimate used for Theorem 1.1(3): bound with $c>0$ on Psi (Vinogradov-Korobov-type zero-free region). — *Role:* Gives absolute convergence of moments mu_n.
- **THM-PAPER-0101-L4** (Lemma 2.1; Sec.2). Statement about entire functions of exponential type used in the Weil-distribution/Paley-Wiener step. — *Role:* Technical for Sec.3.
- **THM-PAPER-0101-L5** (Proposition 3.1; Sec.3). Characterization on the space C(a) relating Weil distribution to the screw-function form. — *Role:* Bridge for Thm 1.3.

### Proof architecture

Compute Laplace transform of Psi from explicit formula (Sec.2.1), giving $-z^{-2}\xi'/\xi$. Combine Lagarias positivity with Krein-Langer correspondence to get Thm 1.2; positivity of the kernel is exactly positivity of the Weil distribution (Sec.3, Bombieri-Lagarias), giving Thm 1.3. Non-degeneracy (Thm 1.4) via Yoshida/Bombieri strategy using local positivity (Thm 4.2) and a coercive lower bound (Thm 4.3); trace class (Thm 1.5) via kernel regularity. Thm 1.6-1.8 from Laplace-transform Tauberian (Widder) arguments plus Stieltjes moment theory; Sec.8 explicit linear relation to Li coefficients; Sec.9 Krein string ('Zeta string'); Sec.10 mean-periodicity.

**Imported results.** Krein-Langer Satz 5.9 (screw functions vs Nevanlinna); Lagarias 1999 positivity of xi'/xi; Weil / Bombieri-Lagarias positivity; Yoshida 1992 non-degeneracy criterion; Widder Laplace transform theory; Fesenko-Ricotta-Suzuki mean-periodicity

**Techniques.** Krein screw functions / Nevanlinna (Pick) class; Weil positivity / Weil explicit formula; Laplace transform and Widder positivity; Stieltjes moment problem and Hankel determinants; Hilbert-Schmidt/trace class operators, Mercer theorem; Hadamard product and Paley-Wiener

## Context and interpretation

**Importance and obstacle overcome.** Packages RH as pointwise positivity of the single explicit function Psi(t) (zero-free formula with primes), and unifies Weil, Li, Hankel and Stieltjes criteria; replaces distributional Weil form by continuous-kernel integral operator on L^2. Obstacle: no unconditional positivity beyond small t; the equivalences are reformulations.

**Relation to prior work.** Builds on Lagarias 1999, Krein-Langer, Bombieri 2000, Yoshida, Li 1997, Bombieri-Lagarias 1999; Suzuki's own later papers extend to Selberg class (CAND-02381).

**Limitations and open questions.** Positivity of Psi(t) proven only on (0,t_0), t_0>log 2 (numerical help), and Gg positive definite only for small a. Full RH requires Psi>=0 for all t, which is equivalent to RH. Whether non-degeneracy (Thm 1.4) can be proved for large a is open.

## Research potential

- **Hypotheses that might be weakened.** Theorem 11.1 needs only Psi_omega>=0 for t>=t_0 (eventual positivity): attack zero-free regions of width omega via asymptotics of Psi_omega; Thm 1.7 pointwise positivity on a finite window already gives local positivity.
- **Generalizations.** Extension to Selberg class done in CAND-02381; remains for Thm 1.4 (non-degeneracy) in S^flat and for Hecke/automorphic L-functions and Dedekind zeta.
- **Candidate connections.** Hankel determinants of mu_n vs Li coefficients (Thm 8.1) give a Stieltjes-moment equivalent suitable for rigorous numerics; connects to Krein string / de Branges spaces (Zeta string, Kotani) and to mean-periodicity (Fesenko-Ricotta-Suzuki).
- **Reusable lemmas.** Formula (1.1)/(1.3) as zero-free formula for Psi; explicit Li-moment transformation (8.1)-(8.2); Theorem 4.3 coercive bound.
- **Possible experiments.** Compute Psi(t) from primes (or zeros) for t up to ~ log(10^{15}) and verify Psi>=0 and the smallest eigenvalues of Gg[a] for moderate a; compute Hankel determinants det Delta_n, det Delta_n^(1) in high precision (interval arithmetic) to see growth/sign for n<=100; test Psi_omega positivity for omega slightly negative to detect first zeros of Re part.
- **Risks / barriers.** All equivalences are circular reformulations; finite checks of Psi>=0 give local evidence only and cannot decide RH (Psi(t) is needed for all t; terms oscillate with e^{t/2} cancellation). Hankel determinant numerics suffer severe ill-conditioning.

## Audit notes (Level 1 reader)

Intro formula (1.1) as extracted is garbled by text conversion; the transcription of its gamma-factor term in my main_results should be verified against the PDF. Introduction notes Gg(t,t)=2Psi(t); Thm 1.7 sign (g=-Psi) consistent. No genuine inconsistencies noticed in inspected portion (Sec.3,5,7,9,10 proofs not read in detail).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01970`; harvest queries: kw_RH_any, kw_weil_positivity, msc_11M26, arxiv_li_criterion, arxiv_rh_abs, arxiv_weil_explicit.
- Triage decision: include — Screw function framework giving equivalent conditions to RH.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
