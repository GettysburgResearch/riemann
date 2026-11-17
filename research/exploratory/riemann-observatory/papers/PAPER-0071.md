# PAPER-0071 — On two conjectures in the theory of numbers

| Field | Value |
|---|---|
| Authors | Ingham, A. E. |
| Year / stratum | 1942 / S2 |
| Venue | Am. J. Math. 64, 313-319 (1942). |
| Identifiers | zbMATH [0063.02974](https://zbmath.org/?q=an:0063.02974) · DOI [10.2307/2371685](https://doi.org/10.2307/2371685) |
| MSC | 11M26 |
| Families | C, G |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1942.Ingham.pdf |
| Selection | score 4.4905, in-pool citations 33, seed lists 3, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** If Mertens' conjecture |M(x)|<x^{1/2} or Polya's conjecture L(x)<=0 (or any of four one-sided x^{1/2} bounds) were true, what would follow about the zeros of zeta? Answer: RH, simple zeros, and a linear dependence among the imaginary parts.

**Historical motivation.** Stieltjes-Mertens (|M(x)|<x^{1/2}, verified by von Sterneck to 5e6), Polya 1919 (L(x)<=0 verified to 1,500, extended to 20,000 by Gupta 1940); analogy with Littlewood's disproof of pi(x)<li(x).

### Main results

- **THM-PAPER-0071-1** (Theorem A, theorem (conditional), scope: asymptotic; sec. 1 Theorem A p.314; proof sec. 3 pp.318-319). Let $M(x)=\sum_{n\le x}\mu(n)$, $L(x)=\sum_{n\le x}\lambda(n)$. If the positive ordinates $\gamma_1<\gamma_2<\dots$ of the distinct zeros $\tfrac12+i\gamma_n$ of $\zeta$ (assumed all on $\sigma=1/2$ and simple, otherwise the conclusion is classical) satisfy no linear relation $\sum c_n\gamma_n=0$ ($c_n\in\mathbb Z$ not all 0), or only finitely many independent such relations, then $\limsup x^{-1/2}M(x)=+\infty$, $\liminf x^{-1/2}M(x)=-\infty$, $\limsup x^{-1/2}L(x)=+\infty$, $\liminf x^{-1/2}L(x)=-\infty$. *Conditional on:* LI (finite relation-rank) hypothesis on zero ordinates.
- **THM-PAPER-0071-2** (Corollary in sec. 1 / start of sec. 3, corollary (classical part, proved for completeness), scope: asymptotic; pp.313-314; proof pp.318-319). If any one of $M(x)<Kx^{1/2}$, $M(x)>-Kx^{1/2}$, $L(x)<Kx^{1/2}$, $L(x)>-Kx^{1/2}$ holds for all large $x$ (for some constant K), then RH holds and all zeros of $\zeta$ are simple; hence the Mertens conjecture $|M(x)|<x^{1/2}$ and Polya's $L(x)\le0$ (x>=2) each imply RH and simple zeros. Combined with Theorem A: either they fail or the ordinates are linearly dependent over $\mathbb Q$ (infinitely many independent relations).
- **THM-PAPER-0071-3** (Theorem 1, theorem (Tauberian/Laplace-integral), scope: asymptotic; p.314-316, eqs (4)-(9)). Let $F(s)=\int_0^\infty A(u)e^{-su}du$ ($A$ locally integrable, convergent for $\sigma>\sigma_1>0$) and $A^*(u)=\sum_{-N}^Na_ne^{i\gamma_nu}$ ($\gamma_{-n}=-\gamma_n$, real trigonometric polynomial) with $F^*(s)=\int_0^\infty A^*e^{-su}du$ ($\sigma>0$). If $F-F^*$ is regular (or continuous with regular interior) on $\sigma\ge0,\ |t|\le T$, then $\varliminf A(u)\ge\varliminf A^*_T(u)$ and $\varlimsup A(u)\le\varlimsup A_T^*(u)$... (inequality (5) in source: $\underline\lim A^*_T\le\underline\lim A\le\overline\lim A\le\overline\lim A_T^*$) where $A_T^*(u)=a_0+\sum_{0<|\gamma_n|<T}(1-|\gamma_n|/T)a_ne^{i\gamma_nu}$ (Fejer-weighted truncation).
- **THM-PAPER-0071-4** (Theorem 2, theorem (conditional on RH), scope: asymptotic; p.316-318, eq.(10)). Assume all complex zeros of $\zeta$ are simple and on $\sigma=1/2$: $\tfrac12+i\gamma_n$, $\gamma_{-n}=-\gamma_n$, $0<\gamma_1<\gamma_2<\dots$. Let $\alpha_n$ be the residue at $s=i\gamma_n$ of $F(s)=\dfrac1{(\tfrac12+s)\zeta(\tfrac12+s)}$ (case (i), Mobius) or $\dfrac{\zeta(1+2s)}{(\tfrac12+s)\zeta(\tfrac12+s)}$ (case (ii), Liouville). Then $\sum_{n}|\alpha_n|$ diverges (indeed $\sum_{0<\gamma_n<T}|\alpha_n|\gg\log T$ along a sequence $T_m\to\infty$). *Conditional on:* RH, simplicity of zeros.

### Key definitions

- $M(x)=\sum_{n\le x}\mu(n)$, $L(x)=\sum_{n\le x}\lambda(n)$
- $\gamma_n$: ordinates of zeros
- linear independence of the $\gamma_n$ over $\mathbb Q$ (LI)

### Principal lemmas

- **THM-PAPER-0071-L1** (Theorem 1 proof; pp.315-316). Wiener-type smoothing: with Fejer kernel $K_T(v)=T[\sin(Tv/2)/(Tv/2)]^2\ge0$ and Landau's theorem on Laplace transforms of one-signed functions (regularity on positive real axis gives convergence for $\sigma>0$), the Riemann-Lebesgue lemma gives $\int A(u)K(u-\omega)du=\int A^*(u)K(u-\omega)du+o(1)$. — *Role:* Passes from analytic data of F to limits of A.
- **THM-PAPER-0071-L2** (Kronecker step eq.(12); p.319). If $\gamma_n$ ($0<\gamma_n<T$) are linearly independent over $\mathbb Q$ then $\overline\lim_{u\to\infty}A^*_T(u)=a_0+2\sum_{0<\gamma_n<T}(1-\gamma_n/T)|a_n|$ by Kronecker's theorem, and $\ge 2\sum_{0<\gamma_n<T/2}|a_n|/2$. — *Role:* Gives arbitrarily large limsup as $T\to\infty$ by Theorem 2.
- **THM-PAPER-0071-L3** (sec. 3 first part; p.318). If $A-A(u)\ge0$ for $u>0$ (one-sided bound), Landau's theorem makes $G(s)=\int(A-A(u))e^{-su}du$ regular for $\sigma>0$ so $F(s)$ has no singularities in $\sigma>0$ (no zeta zero off 1/2) and no multiple pole on $\sigma=0$. — *Role:* Shows one-sided Mertens/Polya-type bounds imply RH and simple zeros.

### Proof architecture

Set $A(u)=M(e^u)e^{-u/2}$ or $L(e^u)e^{-u/2}$ so that $F(s)=\int A(u)e^{-su}du$ equals $1/((\tfrac12+s)\zeta(\tfrac12+s))$ or the Liouville analogue; poles at $i\gamma_n$ with residues $\alpha_n$. (1) One-sided bound + Landau theorem => RH and simple zeros. (2) Under RH+simplicity, Theorem 2 (contour integral of $(T+is)^k F(s)$ over a rectangle, using $1/\zeta$ polynomial-in-T bound on a sequence $T_m$ from Titchmarsh Thm 18) shows $\sum|\alpha_n|=\infty$. (3) Theorem 1 (Wiener/Fejer smoothing) reduces $\limsup A$ to limsup of a trigonometric polynomial. (4) Kronecker's theorem under LI makes the trig polynomial's limsup $\ge 2\sum_{\gamma<T/2}|\alpha_n|\to\infty$.

**Imported results.** Landau's theorem on Laplace transforms of one-signed functions; Kronecker's theorem on simultaneous diophantine approximation; Riemann-Lebesgue lemma; Titchmarsh (1930) Theorem 18 p.26: exists sequence T_m with 1/zeta bounded by T^epsilon-type growth; Wiener Tauberian technique; Heilbronn's theorem h(D)=1 for finitely many D

**Techniques.** Laplace transform positivity (Landau); Wiener-style Tauberian smoothing with Fejer kernel; Riemann-Lebesgue lemma; Kronecker's simultaneous approximation theorem; contour integration with sup bounds on 1/zeta along special heights

## Context and interpretation

**Importance and obstacle overcome.** Shows Mertens and Polya conjectures are unlikely (would require infinitely many linear relations among zeros), foreshadowing Odlyzko-te Riele's 1985 disproof of Mertens and Haselgrove's 1958 disproof of Polya. Obstacle: obtaining unboundedness of $M(x)x^{-1/2}$ from LI without Phragmen-Lindelof or explicit formulae, via Wiener Tauberian technique + Kronecker's theorem instead of Dirichlet approximation.

**Relation to prior work.** Modelled on Littlewood 1914; cites von Sterneck tables, Polya's relation of L(m)=0 with class numbers h(-p)=1, Heilbronn's theorem. Later: Haselgrove 1958 (Polya false), Odlyzko-te Riele 1985 (Mertens false), Ng 2004 (LI-based limsup/liminf of M(x)/sqrt(x) bounds), Humphries 2013.

**Limitations and open questions.** Ingham notes LI could be relaxed to finitely many relations but 'no obvious way of replacing it by anything essentially easier to verify'. The linear independence is unproven for zeta (LI is a hypothesis, not a theorem); thus the conclusion is conditional.

**Ideas in remarks/appendices/abandoned paths.** Remark after Theorem A: LI could be relaxed to finitely many relations (stated); the proof for finitely many relations uses Kronecker for gamma_n beyond the last relation gamma_m. Also the observation that sign change of L(x) is forced by lambda(n)=+-1 (Polya's argument that L can only change sign through 0) used for Polya's class-number connection.

## Research potential

- **Hypotheses that might be weakened.** LI could be replaced by a quantitative weak version (e.g., Q-rank of ordinates up to T grows like T log T) to obtain explicit growth lower bounds for limsup M(x)/sqrt(x) (as in Ng, Humphries); Theorem 2's divergence of sum|alpha_n| could be sharpened to a rate (sum_{gamma<T}|alpha_n| ~ log^? T) conditional on Gonek-Hejhal.
- **Generalizations.** The Laplace-Tauberian + Kronecker argument applies to partial sums of mu*chi or Liouville-type functions for L(s,chi); to prime counting error terms (Rubinstein-Sarnak, Chebyshev bias) where LI is used.
- **Candidate connections.** Odlyzko-te Riele disproof (LLL) showing M(x)/sqrt(x) exceeds 1; Gonek-Hejhal conjecture sum 1/|zeta'(rho)|^2 ~ T; Pintz 1987 effective version; Pólya-type L(x)>0 values at 906150257; connect to CAND on Rubinstein-Sarnak LI.
- **Reusable lemmas.** Theorem 1 (Wiener/Fejer comparison of A with a trigonometric polynomial) and Theorem 2 (divergence of sum|alpha_n| for residues of 1/zeta); the Landau-theorem step proving one-sided bounds imply RH+simple zeros.
- **Possible experiments.** Compute alpha_n = 1/((1/2+i gamma_n) zeta'(1/2+i gamma_n)) for first 1e5 zeros and test growth of partial sums of |alpha_n| (Theorem 2) and of the Fejer-weighted truncation sup; compute max of M(x)/sqrt(x) at large x via explicit formula to study LI-implied unboundedness.
- **Risks / barriers.** LI is an open conjecture; disproof of Mertens (1985) shows conclusion ('not bounded by 1') unconditionally for the constant 1 but unboundedness of M(x)/sqrt(x) remains open (Ng conjecture of size (log log log x)^{5/4}); numerical computation cannot decide limsup = infinity.

## Audit notes (Level 1 reader)

OCR garbling of the JSTOR scan; lines around p.313-314 truncated. Triage summary slightly under-states: Theorem A is conditional on LI (not the truth of Mertens/Polya), and Mertens/Polya themselves imply RH+simple zeros (classical). In Theorem 2, 'Sum |alpha_n| divergent' is derived from $2\pi i S_k(T)\sim iT^k\log T$, i.e. sum over 0<gamma<T of |alpha_n| is at least log T; no gap noticed. In eq.(12) the printed constant factors are garbled by OCR (stated $a_0+2\sum(1-\gamma_n/T)|a_n|$ vs the bound by $2\sum_{\gamma<T/2}|a_n|/2$). Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00065`; harvest queries: kw_RH_any, msc_11M26.
- Triage decision: include — Ingham 1942 showing Mertens and Polya conjectures imply linear dependence of zero ordinates.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
