# PAPER-0110 — The sixth moment of the Riemann zeta function and ternary additive divisor sums

| Field | Value |
|---|---|
| Authors | Ng, Nathan |
| Year / stratum | 2021 / S6 |
| Venue | Discrete Anal. 2021, Paper No. 6, 60 p. (2021). |
| Identifiers | zbMATH [1486.11102](https://zbmath.org/?q=an:1486.11102) · DOI [10.19086/da.22057](https://doi.org/10.19086/da.22057) · arXiv [1610.04977](https://arxiv.org/abs/1610.04977) |
| MSC | 11M06 |
| Families | A, B |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/1610.04977 |
| Selection | score 4.2222, in-pool citations 10, seed lists 0, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Show that a conjectured asymptotic formula (with power-saving error AD(theta,C)) for smoothed shifted ternary additive divisor sums sum_{m-n=r} sigma_I(m)sigma_J(n) f(m,n) implies an asymptotic with power saving for the sixth moment of zeta on the critical line, rigorously realizing the Conrey-Gonek heuristic and the CFKRS shifted-moment conjecture for k=3.

**Historical motivation.** Only I_1 (Hardy-Littlewood 1918) and I_2 (Ingham 1926) are asymptotically known; Keating-Snaith/CFKRS conjecture all I_k with explicit constants (1.4)-(1.7). Conrey-Gonek (1998) derived heuristically I_3 from D_3 additive divisor conjecture; Ivic showed such a conjecture implies I_3<<T^{1+eps}.

### Main results

- **THM-PAPER-0110-1** (Conjecture 2 (AD(theta,C)), conjecture, scope: conditional; Sec 1, Conjecture 2). There exists (theta,C) in [1/2,3/2) x [0,infty) such that for I={a_1,a_2,a_3}, J={b_1,b_2,b_3} distinct shifts with |a_i|,|b_i|<<(log X)^{-1}, f smooth supported in [X,2X]x[Y,2Y], Y<<X, x^m y^n f^{(m,n)}<<P^{m+n}: $D_{f;I,J}(r)=\sum_{i_1,i_2=1}^3\prod_{j_1\ne i_1}\zeta(1-a_{i_1}+a_{j_1})\prod_{j_2\ne i_2}\zeta(1-b_{i_2}+b_{j_2})\sum_{\ell\ge1}\frac{c_\ell(r)G_I(1-a_{i_1},\ell)G_J(1-b_{i_2},\ell)}{\ell^{2-a_{i_1}-b_{i_2}}}\int_{\max(0,r)}^\infty f(x,x-r)x^{-a_{i_1}}(x-r)^{-b_{i_2}}dx+O(P^CX^{\theta+\epsilon})$ uniformly for 1<=|r|<<X^{1/2-eps_2}.
- **THM-PAPER-0110-2** (Theorem 1.1, theorem, scope: conditional; Sec 1, Thm 1.1, eq (1.22) (exponent printed as T^{3theta/2+eps}(T^{1+C}/T_0))). Assume AD(theta,C) with theta in [1/2,3/2), C>0 (as in Conj 2); I,J of size 3 with |a_i|,|b_i|<<1/log T; omega smooth, supported in [c_1T,c_2T], omega^{(j)}<<T_0^{-j} for some T_0>=T^{3/4+eps_0}, T_0<<T^b with b>(C+3theta)/2/(C+1), int|omega|<<T. Then $I_{I,J}(\omega)=\int_{-\infty}^{\infty}\sum_{S\subset I,T\subset J,|S|=|T|}Z_{I_S,J_T}(0)(t/2\pi)^{-\sum_{S}-\sum_T}\omega(t)dt+O\bigl(T^{\frac{3\theta}2+\epsilon}(T^{1+C}/T_0)\bigr)$, where $I_{I,J}(\omega)=\int\prod_{j=1}^3\zeta(\frac12+a_j+it)\zeta(\frac12+b_j-it)\omega(t)dt$. *Conditional on:* Conjecture 2 (AD(theta,C)).
- **THM-PAPER-0110-3** (Corollary 1.2, corollary, scope: conditional; Sec 1, Cor 1.2; proof by smooth majorant/minorant of 1_[T,2T], dyadic summation, P_9 from CFKRS contour integral). If AD(theta,C) holds for some theta in [1/2,3/2), C>=0, there exists a degree-9 polynomial P_9 with, for every eps>0, $\int_0^T|\zeta(\tfrac12+it)|^6dt=TP_9(\log T)+O(T^{\frac{3\theta+1+C}{2+C}+\epsilon})$. *Conditional on:* Conjecture 2.
- **THM-PAPER-0110-4** (Remark 6 after Thm 1.1, remark, scope: conditional; Sec 1, remarks). If AD(1/2,C) holds then error in (1.22) is O(T^{3/4+eps}) for T_0=T^{1-eps} (matching Ivic/Motohashi speculation), and the exponent in Cor 1.2 becomes 1-1/(8+4C)+eps (which exceeds 7/8+eps).
- **THM-PAPER-0110-5** (Remark 2 after Cor 1.2, remark, scope: conditional; Sec 1). Under a strengthened Conjecture 2 with |a_i|,|b_i|<=delta_0 (small constant) in place of <<1/log X, Thm 1.1 holds with (1.16) replaced by (1.15).

### Principal lemmas

- **THM-PAPER-0110-L1** (Lemma 2.2; Sec 2). Approximate functional equation for the product of three zeta values with shifts (A>0, delta in (0,1/6), t>=2A+3), used to write the shifted sixth moment as sums of divisor-type sums. — *Role:* Starting point: express I_{I,J}(omega) as diagonal plus off-diagonal (shifted convolution) sums.
- **THM-PAPER-0110-L2** (Proposition 4.1; Sec 4). Decomposition of I_{I,J}(omega) for |a_i|,|b_i|<=delta<1/2 into main terms and off-diagonal sums under conditions (3.1),(3.3). — *Role:* Reduction to diagonal contribution plus additive divisor sums D_{f;I,J}(r).
- **THM-PAPER-0110-L3** (Proposition 5.1 / Lemma 5.3 / Lemma 5.4 / Proposition 5.5; Sec 5). Off-diagonal terms: after separating variables (support of f_{r;M,N} in [M,2M]x[N,2N]) and applying AD(theta,C) with error P^C X^{theta+eps} summed over r, the off-diagonal contributes main terms matching the 'swap' terms plus O(T^{3theta/2+eps}...) error; Lemma 5.4 bounds an auxiliary sum for 0<theta<1. — *Role:* Evaluation of off-diagonal via the conjectured additive divisor formula.
- **THM-PAPER-0110-L4** (Proposition 6.1 / 6.2 / 6.4 / 6.5, Lemma 6.3; Sec 6). Evaluation of the resulting main terms as sums of residues; Prop 6.2 gives identities identifying them with Z_{I_S,J_T}(0) (j-swap terms); Lemma 6.3 (delta in (0,1/7)) handles analytic properties; Prop 6.5 finishes with residue at poles s=p_j. — *Role:* Match arithmetic main terms to the CFKRS recipe.
- **THM-PAPER-0110-L5** (Lemma 2.3 / Definitions 1-4; Sec 1-2). Euler factors: Z_{X,Y}(s)=prod_{x,y} zeta(1+s+x+y) A_{X,Y}(s) with explicit A for |X|=|Y|=3; multiplicative functions g_X(s,n), G_X(s,n). — *Role:* Arithmetic factor of the conjectured main term; matches Conrey-Gonek singular series.

### Proof architecture

Follow Hughes-Young twisted fourth moment strategy. (1) Approximate functional equation for product of three shifted zetas (Lemma 2.2) gives I_{I,J}(omega) = diagonal (m=n) + off-diagonal sums over m-n=r of sigma_I(m)sigma_J(n) weighted by smooth functions (Prop 4.1). (2) Smooth dyadic partition and separation of variables; apply AD(theta,C) to evaluate sum over m-n=r for r up to X^{1/2-eps}; larger r bounded trivially/analytically (Prop 5.1, 5.5; Lemma 5.3, 5.4). (3) Main terms combine, via contour integration and residue calculus (Prop 6.1-6.5), to the CFKRS recipe sum over j-swaps of Z_{I_S,J_T}(0); this is the first rigorous derivation of the Conrey-Gonek heuristic. (4) Holomorphy in shifts (a_i,b_i): F=f-g holomorphic for small shifts, so evaluation at 0 follows from Cauchy estimates; Corollary 1.2 passes to shift 0 using P_9 as CFKRS contour integral of degree 9 [Conrey-Farmer-Keating-Rubinstein-Snaith] and smooth majorant/minorant of [T,2T] with T_0 optimized: error T^{(3theta+1+C)/(2+C)+eps}. Imported: CFKRS recipe/holomorphy (Lemma 2.5.1), degree-9 polynomial P_9, Hughes-Young method, Duke-Friedlander-Iwaniec delta-method heuristics for the main term.

Dependency edges: CAND-02046 → Conrey-Farmer-Keating-Rubinstein-Snaith shifted moments conjecture (gives_conditional_evidence_for); CAND-02046 → Conrey-Gonek 1998 heuristic (makes_rigorous_conditionally); CAND-02046 → Ivic (sixth moment << T^{1+eps} conditional) (improves); CAND-02046 → Hughes-Young twisted fourth moment (uses_method_of)

**Imported results.** Conrey-Farmer-Keating-Rubinstein-Snaith recipe and Lemma 2.5.1 (holomorphy of main term in shifts); [9, Thm 1.2] P_9 has degree 9; Hughes-Young (twisted fourth moment) method; Duke-Friedlander-Iwaniec for the d(n) additive divisor main-term shape; Goldston-Gonek theorem (for the Conrey-Gonek heuristic comparison)

**Techniques.** shifted moments and CFKRS recipe; additive divisor sums / delta method; approximate functional equation; smooth weight and dyadic partitioning; contour integration and residues; Hughes-Young twisted moment technique; analytic continuation in shifts and Cauchy estimates

## Context and interpretation

**Importance and obstacle overcome.** Turns a heuristic into a rigorous conditional theorem: AD(theta,C) for ternary additive divisor sums implies the sixth moment asymptotic with power saving, and gives evidence (not proof) for the CFKRS shifted-moment conjecture. Obstacle: unlike k<=2, the off-diagonal needs asymptotics for sums of d_3-type divisors in shifts with power-saving error uniform in r<<X^{1/2-eps}, and Ng organizes the argument so that only smoothed, shifted versions are needed.

**Relation to prior work.** 

**Limitations and open questions.** Entirely conditional: AD(theta,C) is open for k=3 (only proven for d(n), theta=3/4, C=5/4 by Duke-Friedlander-Iwaniec). The result needs theta<3/2, and the exponent beating T^{7/8} requires strong C. The condition on shifts |a_i|,|b_i|<<1/log T limits the shifted-moment evidence; extension to larger shifts is Remark 2. Does not imply Lindelof beyond what is known conditional on the same hypothesis (Ivic) and says nothing about RH.

## Research potential

- **Hypotheses that might be weakened.** AD(theta,C) uniformity range |r|<<X^{1/2-eps_2}; the requirement that shifts be distinct and <<1/log X; theta<3/2 could be tested numerically for k=3 divisor correlations (Ng-Thom, Henriot).
- **Generalizations.** Eighth moment/k=4 from additive divisor sums with 4-fold divisor functions (Conrey-Gonek) needs a different framework; analogous implication for quadratic Dirichlet L-function cubic moment or moments in other families.
- **Candidate connections.** Matomaki-Radziwill-Tao almost-all-r asymptotics for D_k(x,r) might give partial (almost-all-shift) results; connection to Harper's upper bound and Soundararajan under RH for sharp I_k bounds; conditional route to the Lindelof-on-average hypothesis I_3<<T^{1+eps} (Ivic).
- **Reusable lemmas.** Proposition 6.2 identities and Lemma 2.3 explicit A_{X,Y}(s) for |X|=|Y|=3 are reusable arithmetic-factor computations for the CFKRS recipe at k=3.
- **Possible experiments.** Numerically compute smoothed D_{f;I,J}(r) for k=3 shifts to estimate theta, C in AD(theta,C); compare the predicted main term to the numerical sixth moment for T up to ~1e6-1e8; verify P_9 coefficients against Conrey-Ghosh a_3.
- **Risks / barriers.** Proving AD(theta,C) for k=3 is as hard as any current ternary divisor problem (open); this paper does not reduce difficulty of sixth moment unconditionally.

## Audit notes (Level 1 reader)

Exponent in the extracted text for (1.22) and Cor 1.2 is partially garbled; reported as T^{3theta/2+eps}(T^{1+C}/T_0) and T^{(3theta+1+C)/(2+C)+eps} per source. Remark 4 reads 'I_3(T)<<T^{1+eps}' (Ivic). The condition T_0<<T^b with b>(C+3theta)/2/(C+1) appears slightly garbled in extraction. Main body of proof (Sec 4-6) not read in detail.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02046`; harvest queries: kw_moments_zeta, msc_11M06, arxiv_critical_line, arxiv_moments_zeta.
- Triage decision: include — Sixth moment of zeta (conditional on divisor-sum conjecture); frontier moments.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
