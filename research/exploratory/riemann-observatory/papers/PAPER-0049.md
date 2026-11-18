# PAPER-0049 — Simple zeros of the Riemann zeta-function

| Field | Value |
|---|---|
| Authors | Conrey, J. B.; Ghosh, A.; Gonek, S. M. |
| Year / stratum | 1998 / S4 |
| Venue | Proc. Lond. Math. Soc., III. Ser. 76, No. 3, 497-522 (1998). |
| Identifiers | zbMATH [0907.11025](https://zbmath.org/?q=an:0907.11025) · DOI [10.1112/S0024611598000306](https://doi.org/10.1112/S0024611598000306) |
| MSC | 11M26, 11M06 |
| Families | B |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/simplezeros.pdf |
| Selection | score 4.5604, in-pool citations 38, seed lists 1, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** How large a proportion of the nontrivial zeros of zeta can be shown simple (and how many distinct) under RH, by a method independent of Montgomery's pair-correlation approach? Define C_s = liminf N_s(T)/N(T), C_d = liminf N_d(T)/N(T).

**Historical motivation.** Montgomery's pair correlation gave 2/3 simple zeros under RH; the authors seek a method not tied to the pair correlation constant $C_0$ (Section 1, eq (1.1)-(1.2), $C_d>1/6(5+2C_s-C_0)$).

### Main results

- **THM-PAPER-0049-1** (Theorem 1, theorem (conditional), scope: conditional; Section 1, p.498). Assume RH and the Generalized Lindel\"of Hypothesis (GLH: $L(\sigma+it,\chi)\ll_\epsilon (q(|t|+1))^\epsilon$ for $\sigma\ge 1/2$, $\chi$ mod $q$). Then $C_s>19/27$ and $C_d>5/6+1/81$ (the latter read from garbled OCR; reconstruct from source before citing). *Conditional on:* RH, GLH.
- **THM-PAPER-0049-2** (Theorem 2, theorem (conditional on GLH only), scope: asymptotic; Section 2, eqs (2.5)-(2.7)). Let $B(s)=\sum_{k\le y} b(k)k^{-s}$, $y=T^{v}$, $v<1/2$, $b(k)=\mu(k)P(\log(y/k)/\log y)$, $P$ real polynomial with $P(0)=0,P(1)=1$. Under GLH, $S_1=\sum_{\gamma\le T}B\zeta'(\rho)\sim(1/2+v)\int_0^1P\,dx\cdot \frac{T L^2}{2\pi}$ and $S_2=\sum_{\gamma\le T}B\zeta'(\rho)B\zeta'(1-\rho)\sim\lambda\frac{TL^3}{2\pi}$ with $\lambda=\frac13+v\left(\int_0^1P\right)^2... $ (exact form (2.7) garbled in OCR: involves $v$, $\int P$, $\int P^2$ and $\frac{1}{12 v}\int P'^2$), where $L=\log(T/2\pi)$. *Conditional on:* GLH.
- **THM-PAPER-0049-3** (Section 2 optimization, computation, scope: asymptotic; Section 2, p.500). Cauchy-Schwarz $\left|\sum_{\gamma\le T}B\zeta'(\rho)\right|^2\le N_s(T)\sum|B\zeta'(\rho)|^2$ together with RH ($S_2=\sum|B\zeta'(\rho)|^2$) gives $N_s/N\ge |S_1|^2/(N\cdot S_2)$; optimal $P(x)=-vx^2+(1+v)x$; letting $v\to1/2$ gives $S_1\sim\frac{19}{24}N L$-normalization and $S_2\sim\frac{57}{64}NL$-normalization, hence ratio $19/27$. *Conditional on:* RH, GLH.
- **THM-PAPER-0049-4** ((3.26),(3.27), proposition (mean values), scope: asymptotic; Section 3, p.504). Mean values $M_1,M_2$ of $\int|B F(1/2+it)|^2dt$ (with $F$ built from $\zeta$-derivative combinations, via Conrey's earlier machinery) are evaluated for $v<1/2$ (remark: valid for $v<4/7$ by Conrey [4], Levinson-type, 'two-fifths' mollifier work).
- **THM-PAPER-0049-5** (Remark after (2.7), heuristic, scope: asymptotic; Section 2, p.501). Averaging over all $t$ instead of zero ordinates suggests the method would give 3/4 of zeros simple (Levinson: $\int|GB|^2\sim\frac43TL^2$), but the zero-ordinate average differs slightly.

### Key definitions

- $N_s(T)$ = number of simple zeros with $0<\gamma\le T$; $N_d(T)$ distinct zeros
- $C_s=\liminf N_s/N$, $C_d=\liminf N_d/N$
- mollifier $B(s)=\sum_{k\le y}b(k)k^{-s}$, $b(k)=\mu(k)P(\log(y/k)/\log y)$
- GLH as stated in Section 1

### Principal lemmas

- **THM-PAPER-0049-L1** (Lemma 1; Section 4, p.505). Stationary-phase evaluation of $\frac1{2\pi i}\int_{c+i}^{c+iT}\chi(1-s)r^{-s}ds$: equals $e(-r)+E(r,c)$ for $r\le T/2\pi$, and $E(r,c)$ otherwise, with $E\ll T^{c-1/2}\cdot$(explicit factor). — *Role:* Gonek's lemma converting contour integrals with $\chi(1-s)$ into additive-character sums $e(-m/k)$
- **THM-PAPER-0049-L2** (Lemma 2; Sections 4-5, eq (5.4)-(5.5)). Dirichlet-series version of Lemma 1 for $A(s)=\sum a(n)n^{-s}$, giving $I_n=M_n+E_n$ with $E_n\ll T^{1/2}yL^7$ and $M_n=\sum_{k\le y}\sum_{m\le kT/2\pi}a_n(m)b(k)k^{-1}e(-m/k)$. — *Role:* Reduction of $I_1,I_2$ to sums with additive characters
- **THM-PAPER-0049-L3** (Lemma 4; Section 4). Perron's formula (standard). — *Role:* Handling the m-sum with analytic continuation of generating function $A_n(s;w,d)$
- **THM-PAPER-0049-L4** (Section 6; Section 6, eqs (6.1)-(6.4)). Small conductors $q$: $A_n(s;w,d)$ continued to the left of $\sigma=1$ via $L$-function factors; contribution negligible for $q>1$. — *Role:* Shows only principal character contributes to main term
- **THM-PAPER-0049-L5** (Section 7; Section 7, (7.1)-(7.10)). Large q: large sieve estimates with a Vaughan-type identity $A_n=H_n+I_n$ (parameters $u=x^2$, $v=T^{1/2}$) to bound sums over primitive characters. — *Role:* Uses GLH-type sixth-moment bounds; the technical heart
- **THM-PAPER-0049-L6** (Section 8 / Lemma A; Section 8, pp.519-522). Main-term evaluation: only $q=1$ (principal character, $\tau(\chi_0)=\mu(K)$) contributes, replacing $e(-m/k)$ by $\mu(K)/\varphi(K)$; uses $R_j(0)=R_j'(0)=0$ and a Conrey Lemma-10-style sum; yields the closed form for $\lambda$ in (2.7). Credited to a referee's simplification. — *Role:* Produces S_2 asymptotic

### Proof architecture

Mollify zeta' at zeros: $N_s\ge|\sum B\zeta'(\rho)|^2/\sum|B\zeta'(\rho)|^2$ (Cauchy). Evaluate $S_1,S_2$ by residues over a rectangle contour $C$ (sec 2), using functional equation $\zeta'(s)=-\chi(s)\zeta'(1-s)-(\chi'/\chi)\chi\zeta(1-s)$ to transform to line integrals; the right-hand sides give diagonal main terms; $M_1,M_2$ come from mean values on the critical line (Conrey mollifier machinery); the hard terms $I_1,I_2$ (integrals of $\chi(1-s)\cdot$ Dirichlet series) are evaluated via Gonek's lemma into $e(-m/k)$ sums, split by character conductor, with small conductors by analytic continuation, large conductors by large sieve + GLH, main terms from principal characters. RH enters only to replace $S_2=\sum|B\zeta'|^2$ (needs $1-\rho=\bar\rho$). Then optimize $P$ by calculus of variations.

Dependency edges: CAND-00742 → CAND-00748 (thematic only (both rely on pair-correlation-adjacent zero statistics); no formal dependency)

**Imported results.** Levinson mean value $\int|G B|^2\sim\frac43TL^2$ (Levinson 1974, Adv. Math.); Conrey, J. Number Theory 16 (1983) and 'More than two-fifths' (Crelle 1989): mollified mean values $M_1,M_2$ for $v<4/7$; Gonek, Invent. Math. 75 (1984): mean values of zeta and derivatives; Gonek lemma; Montgomery 1973, Montgomery-Taylor: RH-based simple-zero proportions 2/3 and 0.6725; Cheer-Goldston: 0.672753; Standard large-sieve inequalities (Gallagher, Bombieri), Shiu's Brun-Titchmarsh for multiplicative functions

**Techniques.** Mollifier at zeros of zeta (Levinson/Conrey type); Cauchy-Schwarz lower bound for number of simple zeros; Contour integration with functional equation; Gonek's lemma on $\int\chi(1-s)r^{-s}$; Additive characters to Dirichlet characters; Gauss sums; Large sieve and Vaughan-type identity; Calculus of variations for mollifier polynomial

## Context and interpretation

**Importance and obstacle overcome.** First lower bound on simple zeros exceeding Montgomery's pair-correlation bound; method independent of pair-correlation, using mollified $\zeta'$ at zeros. Obstacle: evaluating sums of $\zeta'(\rho)B$ over zeros requires handling off-diagonal terms through additive character sums and the large sieve.

**Relation to prior work.** Improves Montgomery (2/3), Montgomery-Taylor (0.6725), Cheer-Goldston (0.672753) at the cost of GLH; companion paper Conrey-Ghosh-Gonek 'Mean values of the Riemann zeta-function with application to the distribution of zeros' uses same methods and needs GLH.

**Limitations and open questions.** Result needs RH and GLH; the GLH was added after referee noted an omission (Remark after Theorem 1). Mollifier length restricted to $v<1/2$ (zero-ordinate sums), so 3/4 not reached; Bui-Heath-Brown (arXiv:1302.5018, per search snippet, not read) later removed GLH keeping 19/27 under RH. Does not give all zeros simple. Cheer-Goldston and Montgomery-Taylor 0.6725 (pair correlation) is weaker than 19/27=0.7037.

**Ideas in remarks/appendices/abandoned paths.** Section 2 Remark (p.501): comparison of zero-ordinate averages with all-$t$ averages (Levinson) predicts 3/4 as the natural limit; the discrepancy between the two averages is itself an object of interest (Section 2). Section 3: validity of (3.26),(3.27) for $v<4/7$.

## Research potential

- **Hypotheses that might be weakened.** GLH enters only through a sixth-moment upper bound for Dirichlet L-functions averaged over characters (Sections 6-7); replace with unconditional large-sieve/moment bounds (as done by Bui-Heath-Brown) or check what mean-sixth-moment is needed exactly. RH enters only at $S_2=\sum|B\zeta'(\rho)|^2$.
- **Generalizations.** Lengthen mollifier from $v<1/2$ toward $v<4/7$ (Conrey's range for $M_1,M_2$) to improve 19/27; apply to simple zeros of Dirichlet/automorphic L-functions; use (2.7) with other polynomials; 3/4 benchmark remark suggests ceiling of method.
- **Candidate connections.** Pair correlation (Montgomery) lower bound 0.6725; the ratios-conjecture computation of $\sum\zeta'(\rho)\ldots$ (Conrey-Snaith) could re-derive $S_1,S_2$ main terms heuristically at any mollifier length and test where off-diagonal terms enter.
- **Reusable lemmas.** Lemma 1/2 (Gonek) to evaluate any sum over zeros of $\chi(1-s)\times$Dirichlet polynomial; Section 8 main-term machinery.
- **Possible experiments.** Numerically evaluate $\sum_{\gamma\le T}B\zeta'(\rho)$ and $\sum|B\zeta'(\rho)|^2/N$ for explicit $P$, $v$ near 1/2 at large height (Odlyzko data) and compare to $19/24$, $57/64$ normalized predictions; check finite-T convergence.
- **Risks / barriers.** Any improvement beyond $v=1/2$ needs control of off-diagonal terms in $I_1,I_2$ not covered by GLH; Cauchy-Schwarz step loses information (cannot reach 1).

## Audit notes (Level 1 reader)

1) Triage summary says 'under RH, at least 19/27' and mentions an RH+pair-correlation higher bound; the paper's Theorem 1 requires RH AND GLH (and no pair-correlation hypothesis is used). Remark after Theorem 1 states the earlier version omitted GLH by mistake. 2) Extracted text has garbled mathematics (e.g. constant for $C_d$ and formula (2.7)); constants above reconstructed and flagged. 3) No other issues noticed in inspected portion (Sections 5-7 only skimmed).

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-00742`; harvest queries: kw_GRH, kw_RH_any, kw_pair_correlation, kw_zeta_zeros, msc_11M06, msc_11M26.
- Triage decision: include — Under RH and Lindelof-type hypotheses, proportions of simple zeros.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
