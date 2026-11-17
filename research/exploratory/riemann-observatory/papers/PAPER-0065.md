# PAPER-0065 — A note on the zeros of zeta and \(L\)-functions

| Field | Value |
|---|---|
| Authors | Carneiro, Emanuel; Chandee, Vorrapan; Milinovich, Micah B. |
| Year / stratum | 2015 / S5 |
| Venue | Math. Z. 281, No. 1-2, 315-332 (2015). |
| Identifiers | zbMATH [1332.11078](https://zbmath.org/?q=an:1332.11078) · DOI [10.1007/s00209-015-1485-9](https://doi.org/10.1007/s00209-015-1485-9) · arXiv [1503.00955](https://arxiv.org/abs/1503.00955) |
| MSC | 11M06, 11M26, 11M36, 11M41 |
| Families | A, E |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — https://arxiv.org/abs/1503.00955 |
| Selection | score 4.5136, in-pool citations 19, seed lists 0, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Give a simpler proof of the bound |S(t)|<=(1/4+o(1))log t/log log t under RH (Theorem 1 of CAND-01181) using only classical Beurling-Selberg majorants of the characteristic function of an interval, and extend it to L-functions of degree m (including cuspidal GL(m)), with applications to the order of vanishing at the central point and the height of the lowest zero.

**Historical motivation.** After CAND-01181 improved Goldston-Gonek by a factor 2 using specially built extremal functions, the authors observed that classical Beurling-Selberg functions for the symmetric interval [-t,t] already give the same constant. The L-function extension relates to bounds for order of vanishing at the central point (Brumer, Iwaniec-Kowalski Prop 5.21) and lowest zero height (Omar).

### Main results

- **THM-PAPER-0065-1** (Theorem 1, theorem, scope: asymptotic; Sec 1; proof Sec 3). Assume RH. For sufficiently large t, $|S(t)|\le\left(\frac14+o(1)\right)\frac{\log t}{\log\log t}$ with the $o(1)$ term $O(\log\log\log t/\log\log t)$. *Conditional on:* Riemann Hypothesis.
- **THM-PAPER-0065-2** (Theorem 5, theorem, scope: asymptotic; Sec 4, eqs (4.4)-(4.5); proof in Sec 4. NOTE: as extracted, the order-of-vanishing constant in (4.5) reads 1/2+vartheta (consistent with S(t,pi)+S(t,pi~) giving a factor of 2); I did not verify the printed constant beyond this reading.). Let $L(s,\pi)$ be an L-function of degree m with the stated analytic hypotheses (Euler product with $|\alpha_{j,\pi}(p)|\le p^\vartheta$, completed $\Lambda(s,\pi)=L(s,\pi_\infty)L(s,\pi)$ entire of order 1 up to poles at 0,1, functional equation $\Lambda(s,\pi)=\kappa\Lambda(1-s,\tilde\pi)$, $\Re\mu_j>-1$). Assume GRH for $\Lambda(s,\pi)$. Then for all $t>0$: $|S(t,\pi)|\le\left(\frac14+\frac\vartheta2\right)\frac{\log C(t,\pi)}{\log\log[C(t,\pi)^{3/m}]}+O\left(\frac{\log C(t,\pi)\log\log\log[C(t,\pi)^{3/m}]}{(\log\log[C(t,\pi)^{3/m}])^2}\right)$, and consequently $\mathrm{ord}_{s=1/2}\Lambda(s,\pi)\le\left(\frac12+\vartheta\right)\frac{\log C(\pi)}{\log\log[C(\pi)^{3/m}]}+O\left(\frac{\log C(\pi)\log\log\log[C(\pi)^{3/m}]}{(\log\log[C(\pi)^{3/m}])^2}\right)$, with universal implied constants, where $C(t,\pi)=C(\pi)(|t|+1)^m$, $C(\pi)=N\prod_j(|\mu_j|+3)$ is the analytic conductor. *Conditional on:* Generalized Riemann Hypothesis for Lambda(s,pi).
- **THM-PAPER-0065-3** (Theorem 6, theorem, scope: asymptotic; Sec 4, after proof of Theorem 5). Let $\pi$ be an irreducible unitary cuspidal representation of GL(m) over Q. Assuming GRH for $L(s,\pi)$, $|S(t,\pi)|\le\frac m4\frac{\log t}{\log\log t}+O\left(\frac{\log t\,\log\log\log t}{(\log\log t)^2}\right)$ for t sufficiently large, with the implied constant depending on m and on pi. *Conditional on:* GRH for L(s,pi), Rankin-Selberg: L(s,pi x pi~) has a simple pole at s=1 (imported).
- **THM-PAPER-0065-4** (Theorem 7, theorem, scope: asymptotic; Sec 5. NOTE: the printed form in the extracted text has pi/(loglog) with factor (1/2+vartheta); the exact placement of constants was read from a garbled extraction.). Assume GRH for $\Lambda(s,\pi)$. Then there is a zero $\rho_\pi=\frac12+i\gamma_\pi$ of $\Lambda(s,\pi)$ with $|\gamma_\pi|\le\left(\frac12+\vartheta\right)\frac{\pi}{\log\log[C(\pi)^{3/m}]}+O\left(\frac{\log\log\log C(\pi)^{3/m}}{(\log\log[C(\pi)^{3/m}])^2}\right)$ when $C(\pi)^{3/m}$ is sufficiently large, universal implied constant. *Conditional on:* GRH for Lambda(s,pi).
- **THM-PAPER-0065-5** (Examples 8-10, corollaries, scope: asymptotic; Sec 6, Examples 8, 9, 10 (the displayed constants for Example 9 are partly garbled in the extraction; see audit_notes)). Under GRH: Dirichlet L(s,chi) mod q: $|S(t,\chi)|\le(\frac14+o(1))\frac{\log q(|t|+1)}{\log\log q(|t|+1)}$ and $\mathrm{ord}_{1/2}\le(\frac12+o(1))\frac{\log q}{\log\log q}$. Weight k level q newform: bound with $\log q(k+3)^{?}$ factors and constants 1/2 for the S-bound (as printed: $\frac12+o(1)$) and 1 for ord. Dedekind zeta of K: $|S_K(t)|\le\frac{[K:Q]}{4}\frac{\log r_{d_K}(|t|+3)}{\log\log r_{d_K}(|t|+3)}$ and $\mathrm{ord}_{1/2}\zeta_K\le(\frac12+o(1))\frac{\log(|d_K|+3)}{\log\log(|d_K|+3)}$. *Conditional on:* GRH.

### Key definitions

- S(t,pi)=(1/pi) arg L(1/2+it,pi)
- N(t,pi) counts zeros with |gamma|<=t, weight 1/2 at endpoints (note N(t,zeta)=2N(t))
- analytic conductor C(pi)=N prod(|mu_j|+3), C(t,pi)=C(pi)(|t|+1)^m
- L-function axioms of degree m with parameter vartheta

### Principal lemmas

- **THM-PAPER-0065-L1** (Lemma 2; Sec 2). Beurling-Selberg: for the even real entire functions $R^\pm(z)=\frac12\{H^\pm(\Delta(t+z))+H^\pm(\Delta(t-z))\}$: (i) $R^-\le\chi_{[-t,t]}\le R^+$; (ii) $\int|R^\pm-\chi_{[-t,t]}|=1/\Delta$; (iii) $R^\pm(z)\ll e^{2\pi\Delta|\Im z|}$; (iv) $R^\pm(x)\ll\min(1,\Delta^{-2}(|x|-t)^{-2})$ for $|x|>t$; (v) $\hat R^\pm(\xi)=0$ for $|\xi|\ge\Delta$; (vi) $\hat R^\pm(\xi)=\frac{\sin2\pi t\xi}{\pi\xi}+O(1/\Delta)$ for $|\xi|\le\Delta$. — *Role:* The key point: the L^1 gap 1/Delta does not depend on the interval length, so the symmetric interval [-t,t] is as sharp as [0,t] and gives S(t)-S(-t)=2S(t), the factor 2 gain over Goldston-Gonek.
- **THM-PAPER-0065-L2** (Lemma 3; Sec 3). For all t>0, $N(t)=\frac1{2\pi}\int_{-t}^t\frac{\Gamma_R'}{\Gamma_R}(\frac12+iu)du+S(t)+1$ where $N(t)$ counts zeros with $0<\gamma\le t$ (weight 1/2 at endpoint) and $\Gamma_R(s)=\pi^{-s/2}\Gamma(s/2)$. — *Role:* Symmetric form of the zero-counting formula via functional equation.
- **THM-PAPER-0065-L3** (Lemma 4; Sec 3). Guinand-Weil explicit formula (same as Lemma 5 of CAND-01181 but with the argument normalized with $h((\rho-1/2)/i)$), imported from Goldston-Gonek Lemma 1. — *Role:* Connects zeros to prime sums.

### Proof architecture

Theorem 1: By RH and Lemma 2(i), 0<=sum_gamma (R^+(gamma)-chi_[-t,t](gamma)) = sum R^+(gamma) - 2N(t). Insert Lemma 3 and the explicit formula (Lemma 4): S(t) <= (1/2pi) int (R^+ - chi)(Gamma_R'/Gamma_R)(1/2+iu)du + O(e^{pi Delta}) after bounding the prime sum trivially via PNT and Lemma 2(v),(vi). Using Stirling (Gamma_R'/Gamma_R = log(u/2pi)/2 + O(1/u)), Lemma 2(ii),(iv) and splitting the integral at |u|=2t gives S(t)<= log t/(4 pi Delta)+O(e^{pi Delta}). Choose pi Delta = loglog t - 2 logloglog t. Lower bound via R^-. Theorem 5 self-dual case: same with GRH, with the conductor/gamma-factor integral producing m/4 terms and prime sum bounded using |Lambda_pi(n)|<=m Lambda(n) n^vartheta (this gives the vartheta term); non-self-dual case requires the S_1/extremal-function approach of CAND-01181 (Lemma 6 there rescaled, footnote 4), using separate majorants for S(t,pi)+S(t,pi~) etc. Theorem 6 improves the vartheta term for cuspidal GL(m) via Rankin-Selberg: sum_{n<=x} Lambda(n)|a_pi(n)|^2 log n / n ~ (log^2 x)/2 then Cauchy.

Dependency edges: CAND-01264 → CAND-01181 (gives simpler proof of its main S(t) bound); CAND-01264 → Goldston-Gonek 2007 (improves via symmetric interval); CAND-01264 → Brumer (rank of elliptic curve L-functions) (recovers the conductor bound for analytic rank)

**Imported results.** Beurling-Selberg majorant/minorant of sgn(x) and interval characteristic functions (Selberg, Vaaler survey); Goldston-Gonek explicit formula lemma [10, Lemmas 1-2]; Iwaniec-Kowalski Thm 5.12 (explicit formula) and Thm 14.1; Luo-Rudnick-Sarnak: vartheta<=1/2-1/(m^2+1); Kim-Sarnak vartheta<=7/64 for m=2; Blomer-Brumley for number fields; Brumer (analytic rank of elliptic curves); Rudnick-Sarnak Rankin-Selberg estimate for Theorem 6; Phragmen-Lindelof (used to verify growth condition for R^+)

**Techniques.** Beurling-Selberg majorants of interval characteristic functions; Guinand-Weil explicit formula; symmetrization trick (interval [-t,t] and symmetry of zeros); Stirling; Rankin-Selberg pole for improved prime sum in t-aspect

## Context and interpretation

**Importance and obstacle overcome.** Shows the 1/4 constant is attainable from the classical majorants by the symmetry trick, and generalizes it uniformly in conductor and t. The obstacle for non-self-dual L-functions is that the symmetry S(t,pi)=S(t,pi~) fails, so the explicit formula contains both Lambda_pi and Lambda_pi~ terms and S(t,pi)+S(t,pi~) rather than 2S(t) is controlled directly.

**Relation to prior work.** Simplifies CAND-01181's S(t) proof; for L-functions refines Iwaniec-Kowalski Prop 5.21 and Omar's result on lowest zero. In the non-self-dual case, uses the earlier extremal-function method. S_1(t,pi) analogue is deferred to Carneiro-Chirre-Milinovich [9].

**Limitations and open questions.** All conditional on GRH. The vartheta loss (Ramanujan parameter) enters via trivial prime sum bound; Ramanujan would give vartheta=0. For non-self-dual L-functions the new short proof does not apply. Constants in Examples 9-10 are only stated to o(1). The order-of-magnitude log/loglog is untouched.

**Ideas in remarks/appendices/abandoned paths.** Remark that bounding S(t)-S(-t)=2S(t) via the symmetric interval is the source of the factor 2. Remark that G(x)=F(x/2) so extremal functions of [4, Lemma 6] must be dilated (footnote 4). Pointer to [9] for S_1(t,pi).

## Research potential

- **Hypotheses that might be weakened.** The vartheta term could be removed or reduced by using Rankin-Selberg prime-sum estimates uniformly in the conductor (as done in t-aspect in Theorem 6) instead of the trivial bound |Lambda_pi(n)|<=m Lambda(n) n^vartheta. GRH could be replaced by a zero-density hypothesis with extra terms.
- **Generalizations.** Self-dual L-functions beyond GL(m) (Artin, Selberg class members with Ramanujan-type bound); non-self-dual via the extremal approach; function-field analogues.
- **Candidate connections.** Order of vanishing bounds for elliptic curves (Brumer) and lowest-zero bounds (Omar); family statistics (one-level density with extremal functions) cited in the introduction.
- **Reusable lemmas.** Lemma 2 (Beurling-Selberg R^+/-) with gap 1/Delta independent of t; the symmetrization identity N(t,zeta)=2N(t).
- **Possible experiments.** Evaluate S(t) and the right side numerically for t up to Odlyzko heights to see how conservative the 1/4 bound is, and compare 'sum_gamma R^+(t-gamma) - chi' for the optimal Delta. For Theorem 7, check lowest zero heights for elliptic curve L-functions against the bound.
- **Risks / barriers.** Conditional on GRH; trivial prime sum is the barrier to reaching the heuristic sqrt(log t loglog t) size.

## Audit notes (Level 1 reader)

Extracted text of constants in Theorems 5 and 7 and Example 9 is partly garbled, so I report them as read and flag them rather than assert exact values; in particular Example 9's displayed constants (1/2 and 1 in front of log q(k+3)...) differ from the 1/4+vartheta/2 shape of Theorem 5 only because vartheta=7/64 is not used there and the form of q(k+3) was not verified. In Theorem 5 the non-self-dual case proof was only partially read. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01264`; harvest queries: kw_RH_any, kw_weil_positivity, msc_11M06, msc_11M26, msc_11M36, arxiv_rh_abs.
- Triage decision: include — Simple proof of sharpest S(t) bound under RH, generalized to L-functions.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
