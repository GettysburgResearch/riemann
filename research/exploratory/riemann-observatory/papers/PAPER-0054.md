# PAPER-0054 — New large value estimates for Dirichlet polynomials

| Field | Value |
|---|---|
| Authors | Guth, Larry; Maynard, James |
| Year / stratum | 2026 / S7 |
| Venue | Ann. Math. (2) 203, No. 2, 623-675 (2026) |
| Identifiers | DOI [10.4007/annals.2026.203.2.6](https://doi.org/10.4007/annals.2026.203.2.6) · arXiv [2405.20552](https://arxiv.org/abs/2405.20552) |
| MSC | 11M26, 11N05 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1** |
| Full text | fulltext_read — arxiv.org/abs/2405.20552 |
| Selection | score 4.5591, in-pool citations 3, seed lists 3, triage relevance 4 |

## Mathematical content (Level 1: full text read)

**Research question.** Improve the large-values estimate for Dirichlet polynomials with |b_n|<=1 near the critical size V=N^{3/4}, and deduce a better zero-density exponent and primes in short intervals, without assuming RH.

**Historical motivation.** Zero-density estimates (Carlson, Ingham, Huxley 1972, Montgomery-Halasz), where sigma=3/4 with N=T^{4/5} is the critical case where both classical methods give R<=T^{3/5}; goal: density hypothesis and Montgomery's large value conjecture.

### Main results

- **THM-PAPER-0054-1** (Theorem 1.1, theorem, scope: asymptotic; Sec. 1, p. 1). Let $|b_n|\le1$ and $(t_r)_{r\le R}$ be 1-separated points in $[0,T]$ with $|\sum_{n=N}^{2N} b_n n^{it_r}|\ge V$ for all r. Then $R\le T^{o(1)}\left(N^2V^{-2}+N^{18/5}V^{-4}+TN^{12/5}V^{-4}\right)$.
- **THM-PAPER-0054-2** (Theorem 1.2, theorem, scope: asymptotic; Sec. 1, p. 2, eq. (1.4)). Unconditionally $N(\sigma,T)\le T^{15(1-\sigma)/(3+5\sigma)+o(1)}$; combined with Ingham for $\sigma\le 7/10$, $N(\sigma,T)\le T^{30(1-\sigma)/13+o(1)}$ uniformly in $\sigma\in[1/2,1]$. Here N(sigma,T) = #{rho: Re rho>=sigma, |Im rho|<=T}.
- **THM-PAPER-0054-3** (Corollary 1.3, corollary, scope: asymptotic; Sec. 1, p. 2-3 (improves Huxley's 7/12)). For $y\in[x^{17/30+\epsilon},x^{0.99}]$: $\pi(x+y)-\pi(x)=\frac{y}{\log x}+O_\epsilon\!\left(y\exp(-\sqrt[4]{\log x})\right)$.
- **THM-PAPER-0054-4** (Corollary 1.4, corollary, scope: asymptotic; Sec. 1, p. 3 (improves Huxley's 1/6)). For $y\in[X^{2/15+\epsilon},X^{0.99}]$, for all but $O(X\exp(-\sqrt[4]{\log X}))$ integers $x\in[X,2X]$: $\pi(x+y)-\pi(x)=\frac y{\log x}+O_\epsilon(y\exp(-\sqrt[4]{\log x}))$.
- **THM-PAPER-0054-5** (Proposition 3.1, proposition, scope: asymptotic; Sec. 3, p. 9). Let $\sigma\in[7/10,8/10]$, $|b_n|\le1$, W a $T^\epsilon$-separated set in an interval of length $T=N^{6/5}$ with $|\sum_n w(n/N)b_nn^{it}|\ge N^\sigma$ for t in W. Then $|W|\le TN^{(12-20\sigma)/5+o_\epsilon(1)}$.
- **THM-PAPER-0054-6** (Proposition 12.1, proposition, scope: asymptotic; Sec. 12, p. ~70). If $T^{5/6}\le N\le T$, $V=N^\sigma$, $\sigma\ge7/10$, then $R\lesssim N^{2-2\sigma}+T^{1/2}N^{3-4\sigma}+T^{(30\sigma-21)/5}N^{(46-60\sigma)/5}$ (with an inf-over-k form). At sigma=3/4 improves (1.1) by a factor (T/N)^{1/2}.
- **THM-PAPER-0054-7** (Proposition 8.1 / 10.1, proposition, scope: asymptotic; Secs. 8 and 10). For a $T^\epsilon$-separated W in an interval of length T: $S_3\lessapprox T^2|W|^{1/2}E(W)^{1/2}$ (Prop 8.1) and refined $S_3\lessapprox T^2|W|^{3/2}+TN|W|^{1/2}E(W)^{1/2}$ (Prop 10.1), where $E(W)=\#\{w_1+w_2-w_3-w_4\in[-1,1]\}$ is additive energy.

### Key definitions

- Large values set W={t in [0,T]: |D(t)|>N^sigma}, 1-separated
- Additive energy E(W)=#{w1,w2,w3,w4: |w1+w2-w3-w4|<=1}
- M_{t,n}=n^{it}, s_1(M) largest singular value
- R(x)=sum_{t in W}|x|^{it}

### Principal lemmas

- **THM-PAPER-0054-L1** (Prop 4.6 / Lemma 4.5; Sec. 4). For W T^epsilon-separated with |D_N(t)|>N^sigma: $|W|\ll N^{2-2\sigma}+N^{1-2\sigma}\left(\sum_{m\in\mathbb Z^3\setminus0}I_m\right)^{1/3}$ where I_m comes from the expansion of the cubic trace tr((M^*M)^3), M=(n^{it}). — *Role:* Reduces large values to a cubic-trace bound (s_1(M)^6 <= tr((M^*M)^3) after removing near-diagonal terms).
- **THM-PAPER-0054-L2** (Prop 6.1; Sec. 6). For any k: $S_2\lessapprox_{\epsilon,k}N^2|W|^2+TN|W|^{2-1/k}+N^2|W|^{2}\,(T^{1/2}/|W|^{3/4})^{1/k}$. — *Role:* Controls one error term (S2) via approximate functional equation.
- **THM-PAPER-0054-L3** (Prop 7.1; Sec. 7). $|I_m|\ll N^3\left|\int\!\!\int R(v_1)R(v_2/v_1)R(v_2)\,dv_1dv_2\right|+O(T^{-200})$ where $R(x)=\sum_{t\in W}|x|^{it}$. — *Role:* Cancellation inside the u-integrals avoiding stationary phase; moves to the 2-dim subvariety z1 z2 z3=1.
- **THM-PAPER-0054-L4** (Lemma 8.2/8.3 (L2, L4 bounds); Sec. 8). $\|R\|_{L^2[1/2,2]}^2\lessapprox|W|$ and $\|R\|_{L^4[1/2,2]}^4\lessapprox E(W)$. — *Role:* Gives Prop 8.1 (energy-controlled S_3).
- **THM-PAPER-0054-L5** (Prop 9.1; Sec. 9). Equidistribution over affine transformations: for f>=0 supported on u~1 with Fourier decay $|\hat f(\xi)|\lessapprox_j (T/|\xi|)^j\sup f$, $J(f)\lessapprox M^6(\int f)^2+M^4\int f^2$. — *Role:* Key new input: a small set U cannot be approximately closed under many affine maps u->(m1 u+m3)/m2; yields the T N |W|^{1/2}E^{1/2} refinement.
- **THM-PAPER-0054-L6** (Prop 11.1; Sec. 11). For $T^{3/4}\le N\le T$, $|D|\ge N^\sigma$ on W: $E(W)\lessapprox|W|N^{4-4\sigma}+|W|^{21/8}T^{1/4}N^{1-2\sigma}+|W|^3N^{1-2\sigma}$. — *Role:* Energy bound using Heath-Brown's Thm 1.6 (imported) to cover the large-energy case.
- **THM-PAPER-0054-L7** (Lemma 1.7; Sec. 1, proved Sec. 11). For $N\in[T^{2/3},T]$, sigma>1/2, $|b_n|\le1$: $E(W)\le|W|^3N^{1-2\sigma+o(1)}+|W|^2N^{2-2\sigma+o(1)}$. — *Role:* Large additive energy forces Montgomery's conjecture bound.
- **THM-PAPER-0054-L8** (Theorem 1.6 (Heath-Brown, imported); Sec. 1, p. 4). For 1-separated set T in an interval of length T and |a_n|<=T^{o(1)}: $\sum_{t_1,t_2}|\sum a_n n^{i(t_1-t_2)}|^2\le T^{o(1)}(|T|^2N+|T|N^2+|T|^{5/4}T^{1/2}N)$. — *Role:* Imported difference-set mean-value bound.

### Proof architecture

Reduce Theorem 1.1 to Prop 3.1 (smooth weight, N=T^{4/5}, T=N^{6/5} after subdivision, the critical point where the last two terms coincide). Bound |W| via Hilbert-Schmidt/operator norm of M_{t,n}=n^{it}: |W|<=N^{-1/2} s_1(M)^2 and s_1(M)^6<=cubic trace after removing near-diagonal t-terms (Lemmas 4.1-4.5, Prop 4.6). Expand the cubic trace by Poisson summation WITHOUT stationary phase, keep the oscillatory u-integrals, change variables to the subvariety z1z2z3=1 and gain a factor T from the u3 integral (Prop 7.1). Bound the remaining sums by L2 and L4 norms of R(x)=sum |x|^{it}: ||R||_4^4 ~ additive energy E(W) (Prop 8.1, giving S3 << T^2 |W|^{1/2}E^{1/2}). To handle intermediate E(W), exploit averaging over m via a new equidistribution estimate for affine transformations (Props 9.1, 10.1, giving T N |W|^{1/2} E^{1/2}). For large E(W) use Heath-Brown's difference-set theorem (Lemma 1.7, Prop 11.1). Combine to get Prop 3.1; then Theorem 1.1, then insert into the Huxley/Ingham zero-density machinery to get Theorem 1.2 and short-interval corollaries.

Dependency edges: CAND-02366 → Heath-Brown 1979 Thm 1.6 (imports); CAND-02366 → Huxley 1972 zero-density (improves); CAND-02366 → Montgomery large value conjecture (partial progress toward)

**Imported results.** Heath-Brown 1979 difference-set mean value theorem (Thm 1.6); Montgomery-Halasz-Huxley large values estimate and Mean Value Theorem for Dirichlet polynomials (bound (1.1)); Ingham zero-density N(sigma,T)<=T^{3(1-sigma)/(2-sigma)+o(1)}; Huxley zero-density machinery and short-interval transfer (Huxley 1972); Zero-free region of Vinogradov-Korobov type for the exp(-(log x)^{1/4}) saving

**Techniques.** singular-value / high-trace method for Dirichlet polynomial matrices; Poisson summation without stationary phase; change of variables to z1z2z3=1; additive energy dichotomy; sum-product/affine equidistribution (Prop 9.1); Heath-Brown difference-set mean values; dyadic subdivision and smoothing

## Context and interpretation

**Importance and obstacle overcome.** First improvement in 50+ years of the zero-density exponent 12/5 (Huxley 1972) in the critical range sigma~3/4, and first substantive improvement of the large-values estimate for N^{7/10}<V<N^{3/4}. Obstacle: the classical trace method fails because stationary phase links the t_i variables; they avoid stationary phase and exploit the affine structure of the arguments of R.

**Relation to prior work.** Improves Huxley 12/5 -> 30/13; Corollary 1.3 improves 7/12 -> 17/30; Corollary 1.4 improves 1/6 -> 2/15. Uses Heath-Brown's difference-set theorem.

**Limitations and open questions.** Only improves the exponent for V in (N^{7/10+eps}, N^{8/10-eps}) and N<=T^{5/6-eps}; the weaker bound near sigma~3/4 persists in the density hypothesis range. Montgomery's large value conjecture (R <= T^{o(1)}N^{2-2sigma}) and the Density Hypothesis N(sigma,T)<=T^{2(1-sigma)+o(1)} remain open; the new exponent 30/13 is still above 2. The proof genuinely uses the l^infty bound |b_n|<=1 (remark after Lemma 11.4), and cannot be run with only l^2 coefficient control.

**Ideas in remarks/appendices/abandoned paths.** Remark after Prop 12.1: a simpler/stronger version for N>=T^{5/6}, with the term N^{18/5}V^{-4} replaceable by T^{1/2}N^{3-4sigma}+T^{(30sigma-21)/5}N^{(46-60sigma)/5} (Sec. 12). Footnote 1 gives an explicit near-extremal Dirichlet polynomial supporting Montgomery's conjecture (p.3).

## Research potential

- **Hypotheses that might be weakened.** Prop 3.1 fixes T=N^{6/5}; the exponent 18/5 and 12/5 come from optimising at N=T^{4/5}. Replacing |b_n|<=1 by a structured class (e.g. b_n multiplicative/ Euler-product) could weaken the |W|<=... energy bound. The dependence on Heath-Brown's Thm 1.6 for large energy is the weakest link for pushing past 30/13.
- **Generalizations.** Higher traces (r>3) replacing the cubic trace; the same method for Dirichlet L-function large values (character version), for N(sigma,T) with Dirichlet characters, and for large values of exponential sums sum e(f(n)) with f non-power phases.
- **Candidate connections.** Density-hypothesis programme: connecting the new bound to Pintz's/Bourgain's refinements; Prop 9.1 resembles Bourgain's sum-product/Fourier-decay (Szemeredi-Trotter/Furstenberg-type) estimates; Lindelof-on-average (Ivic Ch. 11) large-values bounds near sigma=3/4.
- **Reusable lemmas.** Prop 9.1 (equidistribution over affine transformations) and Lemma 8.4 (Fourier decay of smoothings of R) are general harmonic-analysis lemmas; Prop 12.1 for N>=T^{5/6}.
- **Possible experiments.** Numerically compute additive energy E(W) for t-sets from actual large values of random Dirichlet polynomials (|b_n|<=1) at N~10^4, T~N^{6/5}, and check the E(W)<=|W|^{19/8} regime predicted by Prop 11.1; evaluate the resulting zero-density exponent 15(1-s)/(3+5s) against known N(sigma,T) counts.
- **Risks / barriers.** Does not touch the critical line; RH-relevant only through zero-density input to explicit formula and Linnik/Bombieri-Vinogradov range improvements. Barrier: reaching the density hypothesis needs a bound R<<T N^{2-2sigma}-type at sigma~3/4, beyond this method (needs removing both T^{o(1)} energy loss and the 18/5 term).

## Audit notes (Level 1 reader)

none noticed in inspected portion. Remark: the paper itself notes the improvement is limited to N<T^{10/11} at the critical point V=N^{3/4}.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-02366`; harvest queries: kw_zero_density, msc_11M26, msc_11N05, arxiv_large_values_dirichlet, arxiv_zero_density.
- Triage decision: include — Large value estimates for Dirichlet polynomials, extending Guth-Maynard zero density.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
