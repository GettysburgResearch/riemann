# PAPER-0093 — High moments of the Riemann zeta-function

| Field | Value |
|---|---|
| Authors | Conrey, J. B.; Gonek, S. M. |
| Year / stratum | 2001 / S5 |
| Venue | Duke Math. J. 107, No. 3, 577-604 (2001). |
| Identifiers | zbMATH [1006.11048](https://zbmath.org/?q=an:1006.11048) · DOI [10.1215/S0012-7094-01-10737-0](https://doi.org/10.1215/S0012-7094-01-10737-0) · arXiv [math/9902162](https://arxiv.org/abs/math/9902162) |
| MSC | 11M06, 11M20 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — arXiv:math/9902162 (v1, 1 Feb 1999) |
| Selection | score 4.3218, in-pool citations 70, seed lists 1, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** What is the leading asymptotic of I_k(T)=\int_0^T|\zeta(1/2+it)|^{2k}dt for k=3,4, and what heuristic (approximate functional equation + mean values of long Dirichlet polynomials + conjectured additive divisor sums) predicts it?

**Historical motivation.** Prior to 1998 no plausible constant for moments beyond k=2; Conrey-Ghosh conjectured k=3; paper tests this independently and extends to k=4 in parallel to Keating-Snaith (1998).

### Main results

- **THM-PAPER-0093-1** (Conjecture 1, conjecture, scope: asymptotic; p.2 (Intro), derived at end of paper). As $T\to\infty$, $\int_0^T|\zeta(1/2+it)|^8dt\sim \frac{24024}{16!}\prod_p\Big(1-\frac1p\Big)^{9}\Big(1+\frac9p+\frac9{p^2}+\frac1{p^3}\Big)T\log^{16}T$. *Conditional on:* Conjectures 2, 3, 4 below (the derivation uses them).
- **THM-PAPER-0093-2** (Conjecture 2, conjecture, scope: asymptotic; p.3, eq.(6)-(7)). For each positive integer $k$, $\int_T^{2T}|\zeta(1/2+it)|^{2k}dt\sim\int_T^{2T}|D_{k,N}(1/2+it)|^2dt+\int_T^{2T}|D_{k,M}(1/2+it)|^2dt$ with $D_{k,N}(s)=\sum_{n\le N}d_k(n)n^{-s}$, $MN=(T/2\pi)^k$, $M,N\ge1/2$, or $N\gg (T/2\pi)^k$ if $M=0$. *Conditional on:* proved for k=1; for k=2 when max(M,N)<<T (classical).
- **THM-PAPER-0093-3** (Conjecture 3, conjecture, scope: asymptotic; p.6, eqs.(12)-(18)). $D_k(x,h)=\sum_{n\le x}d_k(n)d_k(n+h)=m_k(x,h)+O(x^{1/2+\epsilon})$ uniformly for $1\le h\le x^{1/2}$, with $m_k'(x,h)=\sum_{d|h}f_k(x,d)/d$, $f_k(x,d)=\sum_{q\ge1}\mu(q)q^{-2}P_k(x,qd)^2$, $P_k(x,q)=\frac1{2\pi i}\oint_{|s|=1/8}\zeta^k(s+1)G_k(s+1,q)(x/q)^sds$ (G_k, g_k explicit Euler-type sums, eqs. (14)-(17)). Also $f_k(x,d)\ll d_{2k-1}(d)\log^{2k-2}x$ for $d\le x$ (proved).
- **THM-PAPER-0093-4** (Conjecture 4, conjecture, scope: asymptotic; p.6-7). For $N=T^{1+\eta}$, $0\le\eta\le1$: $\int_T^{2T}|D_{k,N}(1/2+it)|^2dt\sim w_k(\eta)\frac{a_k}{\Gamma(k^2+1)}TL^{k^2}$, $L=\log T$, $a_k=\prod_p(1-1/p)^{k^2}\sum_{r\ge0}d_k(p^r)^2p^{-r}$, with $w_k(\eta)=(1+\eta)^{k^2}\big(1-\sum_{n=0}^{k^2-1}\binom{k^2}{n+1}^{-1}\gamma_k(n)^2... \big)$ as printed (explicit polynomial in $\eta$ with coefficients $\gamma_k(n)$; e.g. $w_2(\eta)=1+4\eta-6\eta^2+4\eta^3-\eta^4$). Exact formula for w_k should be taken from the paper, p.6-7 (OCR garbled). *Conditional on:* Conjecture 3.
- **THM-PAPER-0093-5** (Conclusion k=3, conditional derivation, scope: conditional; p.7). Given Conjectures 2 and 4, for any $T\ll N\ll T^2$, $\int_T^{2T}|\zeta|^6\sim 42\frac{a_3}{9!}T\log^9T$, hence $I_3(T)\sim 42\frac{a_3}{9!}T\log^9T$, reproducing the Conrey-Ghosh conjecture; independence from N in the whole range is the 'strong confirmation'. *Conditional on:* Conjectures 2,3,4.
- **THM-PAPER-0093-6** (Conjecture 3 failure remark, remark/negative observation, scope: conditional; p.6). For $k=2$, $w_2(\eta)>2$ when $\eta>1$, contradicting Ingham's $I_2$ asymptotic if (6),(7) and Conjecture 3 all held; the authors conclude Conjecture 3 must fail for $\eta>1$ (error terms in (12) accumulate into an additional main term). *Conditional on:* (6),(7) true.
- **THM-PAPER-0093-7** (Heuristic bounds on g_k, conjectural, scope: asymptotic; p.7-9). Writing $I_k(T)\sim g_k\frac{a_k}{\Gamma(1+k^2)}T\log^{k^2}T$: g_1=1, g_2=2, g_3=42, g_4=24024 (conjectured), and heuristically $2^{k^2}\lesssim g_k\lesssim 2(k/2)^{k^2}$ as $k\to\infty$ (integers); compared with Keating-Snaith $g_k=\Gamma(1+k^2)\lim_{N}N^{-k^2}\prod_{j=1}^N\Gamma(j)\Gamma(j+2k)/\Gamma(j+k)^2$. *Conditional on:* Conjecture 4.
- **THM-PAPER-0093-8** (Proposition, proposition (proved), scope: asymptotic; p.9, proof section 'Proof of the Proposition' (~line 1512 of text)). $\log a_k=-k^2\log(2e^\gamma\log k)+o(k^2)$ as $k\to\infty$, with $a_k$ as above. Under RH a more precise expansion with log log k terms is stated without proof.

### Key definitions

- I_k(T)=\int_0^T|\zeta(1/2+it)|^{2k}dt
- d_k divisor function; D_{k,N}
- a_k arithmetic factor
- g_k(T)=\Gamma(1+k^2)I_k(T)/(a_k T\log^{k^2}T); g_k=\lim g_k(T)

### Principal lemmas

- **THM-PAPER-0093-L1** (Montgomery-Vaughan mean value (8) (imported); p.4). $\int_T^{2T}|\sum_{n\le N}a(n)n^{it}|^2dt=\sum|a(n)|^2(T+O(n))$ — *Role:* gives $I_1,I_2$ from Conj. 2 for N<<T; fails for k>=3 since N or M must exceed T
- **THM-PAPER-0093-L2** (Goldston-Gonek long Dirichlet polynomial theorem [GG, Thm 1] (imported); p.4-5). Asymptotic for $\int_T^{2T}|\sum_{n\le N}a(n)n^{-1/2-it}|^2dt$ for $N\ll T^{\min(1/\theta,1/\phi,1/(1-\eta))-\epsilon}$ given $A(x)=m(x)+O(x^\theta)$ and $A(x,h)=m(x,h)+O(x^\phi)$ uniformly for $h\ll x^\eta$ — *Role:* converts additive-correlation conjecture into mean square for N up to T^2
- **THM-PAPER-0093-L3** (Approximate functional equation (4); p.2). $\zeta(s)^k=D_{k,N}(s)+\chi(s)^kD_{k,M}(1-s)+E_k(s)$, $MN=(t/2\pi)^k$ — *Role:* starting point; error term E_k not controlled for k>=3 (Good-type AFE suggested)
- **THM-PAPER-0093-L4** (Estimate (9)-(10); p.4). $\sum_{n\le N}d_k(n)^2/n\sim\frac{a_k}{\Gamma(k^2+1)}\log^{k^2}N$ — *Role:* diagonal term; source of the arithmetic factor a_k
- **THM-PAPER-0093-L5** (bound (18); p.6). $f_k(x,d)\ll d_{2k-1}(d)\log^{2k-2}x$ for $d\le x$ — *Role:* controls the conjectural main term of additive divisor sums

### Proof architecture

Heuristic, not a proof. (1) Approximate functional equation for zeta^k; assume Conjecture 2 that cross term is negligible and E_k small, reducing |zeta|^{2k} mean to two long Dirichlet-polynomial mean squares with MN=(T/2pi)^k. (2) For N<=T classical Montgomery-Vaughan gives the answer; for N~T^{1+eta} apply the Goldston-Gonek theorem, which needs the coefficient sum and the correlation sums sum d_k(n)d_k(n+h). (3) Conjecture 3 supplies a main term m_k(x,h) for the latter (delta method), yielding Conjecture 4 and weight w_k(eta). (4) Since max(M,N)<<T^2 is the range where Conj. 4 is available, only k=3,4 are reachable: k=3 works for any N in [T,T^2] (consistency check), k=4 forces N=M=T^2 giving constant 24024. (5) Separate proved Proposition on asymptotics of a_k as k->infty, and bounds heuristics for g_k.

Dependency edges: CAND-01366 → Goldston-Gonek mean values of long Dirichlet polynomials (imports); CAND-01366 → Keating-Snaith random matrix moments (agrees with (k=3,4)); CAND-01366 → Conrey-Ghosh sixth moment conjecture (supports)

**Imported results.** Hardy-Littlewood 1918 (I_1); Ingham 1926 (I_2); Montgomery-Vaughan mean value theorem (1974); Goldston-Gonek mean value of long Dirichlet polynomials, Thm 1 (1998); Heath-Brown additive divisor bound for k=2; Duke-Friedlander-Iwaniec delta method; Conrey-Ghosh lower bounds g_3(T)>=10.13 etc. and Soundararajan 20.26, 24.59 (quoted); Keating-Snaith random matrix conjecture (comparison)

**Techniques.** approximate functional equation; mean values of long Dirichlet polynomials (Goldston-Gonek); delta method for additive divisor problem (Duke-Friedlander-Iwaniec); Euler product asymptotics for a_k; consistency/independence-of-N test

## Context and interpretation

**Importance and obstacle overcome.** Gave first heuristic derivation matching the Conrey-Ghosh sixth moment constant 42 and predicted 24024 for the eighth moment, agreeing with Keating-Snaith random matrix prediction; an early hint of the arithmetic-times-random-matrix structure later formalized by the CFKRS recipe. Obstacle: long Dirichlet polynomials beyond T where diagonal MV fails, handled by conjectural additive divisor sums.

**Relation to prior work.** Builds on Conrey-Ghosh (k=3 conjecture and lower bounds), Goldston-Gonek long Dirichlet polynomials, Heath-Brown, Duke-Friedlander-Iwaniec, agrees with Keating-Snaith.

**Limitations and open questions.** Entirely conjectural for k>=3 (no unconditional asymptotic known). Conjectures 2 and 3 are unproved; Conj. 3 is explicitly stated to fail for eta>1, so method cannot reach k>=5 and the extrapolation eta in [1-eps,1] is unproved. Error term E_k and cross term uncontrolled. No access to later Duke version to check changes.

**Ideas in remarks/appendices/abandoned paths.** Remark that RH-conditional lower bound g_k>=1 (Conrey-Ghosh) and g_k>=2 (Soundararajan); remark that g_k considered as function of real k, meromorphic continuation idea (p.9); the 'mysterious main term' from accumulating additive divisor error terms (p.6) - potential heuristic for off-diagonal contributions.

## Research potential

- **Hypotheses that might be weakened.** Conjecture 3 error exponent x^{1/2+eps} uniform in h<=x^{1/2}; the paper itself says it fails past eta=1, so an exact characterisation of the 'mysterious' extra main term in D_k(x,h) for large h is a concrete target.
- **Generalizations.** Same scheme for twisted moments, L-function families (Dirichlet, cusp forms) via analogous additive correlation sums; shifted moments.
- **Candidate connections.** Compare with CFKRS recipe and Keating-Snaith constants (check g_k equals the RMT factor beyond k=4); links to d_3(n)d_3(n+1) additive problem.
- **Reusable lemmas.** Proposition on log a_k = -k^2 log(2 e^gamma log k)+o(k^2) for growth of the arithmetic factor; bound (18) for f_k.
- **Possible experiments.** Numerically evaluate w_k(eta) and verify independence of N at k=3 over eta in [0,1]; numerically test Conjecture 3 for k=3 with h up to x^{1/2} and beyond to locate the failure; numerically check I_4(T)/ (a_4 T log^16 T/16!) -> 24024 slowly.
- **Risks / barriers.** Does not bear on RH directly; moments for k>=3 unproved; conjectural inputs, and the method breaks at max(M,N)>T^2.

## Audit notes (Level 1 reader)

OCR of the formula for w_k(eta) and gamma_k(n) (p.6-7, text lines ~340-355) is garbled; the w_k statement above is not reliable and should be re-read from the PDF. Otherwise none noticed in inspected portion. Note the paper itself flags that Conjecture 3 contradicts Ingham for eta>1.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01366`; harvest queries: kw_moments_zeta, msc_11M06, msc_11M20, arxiv_moments_zeta.
- Triage decision: include — Conrey-Gonek landmark on high moments and conjectured formulas.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
