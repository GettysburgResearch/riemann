# PAPER-0089 — Decoupling, exponential sums and the Riemann zeta function

| Field | Value |
|---|---|
| Authors | Bourgain, J. |
| Year / stratum | 2017 / S6 |
| Venue | J. Am. Math. Soc. 30, No. 1, 205-224 (2017). |
| Identifiers | zbMATH [1352.11065](https://zbmath.org/?q=an:1352.11065) · DOI [10.1090/jams/860](https://doi.org/10.1090/jams/860) · arXiv [1408.5794](https://arxiv.org/abs/1408.5794) |
| MSC | 11M06, 11L07, 42B37 |
| Families | A |
| Work type | original_paper |
| Evidence level of this record | **L1-partial** |
| Full text | partial_fulltext — https://arxiv.org/abs/1408.5794 |
| Selection | score 4.3286, in-pool citations 75, seed lists 3, triage relevance 5 |

## Mathematical content (Level 1: full text read)

**Research question.** Prove a sharp mean-value estimate (A_6 bound) for the exponential sums $\sum_{n\le N}e(nx_1+n^2x_2+N^{1/2}n^{3/2}x_3+N^{1/2}n^{1/2}x_4)$ that arise in the Bombieri-Iwaniec / Huxley method, via a new l^2-type decoupling inequality for non-degenerate curves in R^d (d even), and use it to improve the subconvexity exponent for zeta(1/2+it) from 32/205 to 13/84.

**Historical motivation.** Bombieri-Iwaniec (1986) proved zeta(1/2+it)<<t^{9/56+eps}; Huxley improved to 89/570 and 32/205; Huxley's refinements required better mean values for these exponential sums (A_5 by Huxley-Kolesnik, noted in [H] that bounds on A_6 would give further gains). Bourgain-Demeter decoupling (2014-15) made a sharp A_6 bound reachable.

### Main results

- **THM-PAPER-0089-1** (Theorem 1 (decoupling for curves), theorem, scope: asymptotic; Section 1, eq. (1.2)). Let $\Phi=(\phi_1,\dots,\phi_d):[0,1]\to\Gamma\subset\mathbb R^d$ be smooth with non-vanishing Wronskian $\det[\phi_j^{(s)}(t_s)]\ne0$ for all $t_1,\dots,t_d$, d even. Let $I_1,\dots,I_{d/2}\subset[0,1]$ be O(1)-separated intervals, N large, $\{I_\tau\}$ a partition of [0,1] into $N^{-1/2}$-intervals. Then for coefficient functions $a_j$: $\Big\|\prod_{j=1}^{d/2}\big|\int_{I_j}a_j(t)e(x\cdot\Phi(t))dt\big|^{2/d}\Big\|_{L^{3d}_\#(B_N)}\ll N^{\frac16+\varepsilon}\prod_{j=1}^{d/2}\Big[\sum_{\tau:I_\tau\subset I_j}\Big\|\int_{I_\tau}a_j(t)e(x\cdot\Phi(t))dt\Big\|_{L^6_\#(B_N)}^6\Big]^{\frac{1}{3d}}$, for every eps>0 (weighted L^p technicality ignored in the paper).
- **THM-PAPER-0089-2** (Theorem 2 (A_6 bound), theorem, scope: asymptotic; Section 2, eq. (2.12)). $\int_0^1\!\int_0^1\!\int_{-1}^1\!\int_{-1}^1\Big|\sum_{n\le N}e\big(nx_1+n^2x_2+N^{1/2}n^{3/2}x_3+N^{1/2}n^{1/2}x_4\big)\Big|^{12}dx\ll N^{6+\varepsilon}$, essentially sharp; equivalently the number of solutions of the system (2.14)-(2.17) (sums and sums of squares of 6+6 integers, plus the 3/2 and 1/2 power equations up to O(N^{-1/2})) is $\ll N^{6+\varepsilon}$.
- **THM-PAPER-0089-3** (Corollary 3, corollary, scope: asymptotic; Section 2, eq. (2.28)). For $N^{-1/2}\le\delta\le1$, $N^{-1}\le\Delta\le1$: $A_6(N,\delta,\Delta)=\int\!\!\int\!\!\int\!\!\int\Big|\sum_{n\le N}e\big(nx_1+n^2x_2+\tfrac1\delta(\tfrac nN)^{3/2}x_3+\tfrac1\Delta(\tfrac nN)^{1/2}x_4\big)\Big|^{12}dx\ll\delta\Delta N^{9+\varepsilon}$, essentially best possible by the major arc contribution (first-spacing optimal result).
- **THM-PAPER-0089-4** (Theorem 4, theorem, scope: asymptotic; Section 3, (3.19)). Let $F$ be smooth on $[\tfrac12,1]$ with $\min\{|F''|,|F'''|,|F''''|\}>c$, $f(u)=TF(u/M)$, $S=\sum_{m\sim M}e(f(m))$. Then $|S|\ll M^{1/2}T^{\varepsilon+13/84}$ for $\tfrac12\ge\alpha=\frac{\log M}{\log T}\ge\tfrac{17}{42}$.
- **THM-PAPER-0089-5** (Theorem 5, theorem, scope: asymptotic; Section 0 eq. (0.5), proved in Section 4). $\zeta(\tfrac12+it)\ll|t|^{13/84+\varepsilon}$ (13/84=0.15476...), improving Huxley's 32/205=0.15609 and Bombieri-Iwaniec's 9/56=0.16071.
- **THM-PAPER-0089-6** (Theorem 6, theorem, scope: asymptotic; Section 5). $(\tfrac{13}{84}+\varepsilon,\tfrac{55}{84}+\varepsilon)$ is an exponent pair, giving $|S|\ll(T/M)^{13/84+\varepsilon}M^{55/84+\varepsilon}=M^{1/2}T^{13/84+\varepsilon}$ under the stated conditions.

### Key definitions

- A_r(N,delta,Delta): 2r-th moment of the sum with phase (n x_1 + n^2 x_2 + (1/delta)(n/N)^{3/2}x_3 + (1/Delta)(n/N)^{1/2}x_4)
- Non-degenerate curve: non-vanishing Wronskian of derivatives at distinct parameters
- Averaged L^p norm L^p_#
- Exponent pair (k,l)
- First and second spacing problems (Huxley): distribution of (h,h^2,h^{3/2},h^{1/2}) and of the vector x(I)

### Principal lemmas

- **THM-PAPER-0089-L1** (Remark (1.4), eq (1.5); Section 1). The d=2 case of Theorem 1 follows from the L^6 decoupling for planar curves with non-vanishing curvature (Bourgain-Demeter): $\|\int_0^1a(t)e(x\cdot\Phi(t))dt\|_{L^6(B_N)}\ll N^\varepsilon\big(\sum_\tau\|\int_{I_\tau}\cdots\|^2_{L^6(B_N)}\big)^{1/2}$ (discrete: $\ll N^\varepsilon\|a_n\|_{\ell^2}$). — *Role:* Main analytic input, imported from Bourgain-Demeter [B-D1]
- **THM-PAPER-0089-L2** (Section 2 reduction; Section 2, eq. (2.18)-(2.28)). Theorem 1 gives, via discretization, an L^12 bilinear average over each ball B_{N^2}; ball-average to Omega~=[0,N]x[0,N^2]x[0,N^2]x[0,N] is handled by two further 2D decouplings and periodicity; bilinear to linear is handled by induction on scales (Bourgain-Guth) with partitions I_0,...,I_K, using (2.24)-(2.26) and the recursion b(N)<=2^{12}100^6K^{-6}b(100N/K)+C_eps N^eps. — *Role:* Passage from the decoupling inequality to Theorem 2; recursion implies b(N)<<N^eps
- **THM-PAPER-0089-L3** (Section 3 / Theorem 4 derivation; Section 3). Combining Corollary 3 with known estimates for the 'second spacing' parameter B (a referee's treatment; Huxley-Watt double large sieve) in the Bombieri-Iwaniec-Huxley scheme gives |S|<<M^{1/2}T^{13/84+eps} for log M/log T in [17/42,1/2]. — *Role:* Application: new exponential sum bound
- **THM-PAPER-0089-L4** (Section 4 (zeta); Section 4, eq. (4.1)-(4.2)). For 13/42<alpha<17/42 use Huxley's bound $|S|\ll T^{\frac1{128}(4+103\alpha)+\varepsilon}$ ([H1] Thm 3, valid for 12/31<alpha<=1) together with the exponent pair $|S|\ll(T^{1/9})M^{13/18}$ (0<=alpha<=1) to verify (3.19) on the remaining interval; alpha<=13/42 trivial (|S|<=M). — *Role:* Completes the range needed for zeta(1/2+it) via the approximate functional equation

### Proof architecture

Step 1: Prove a bilinear d-dimensional decoupling (Theorem 1) for curves in R^d, d even, by reducing to the planar L^6 decoupling of Bourgain-Demeter (1.5) (cases d=2 direct; general via the Bourgain-Demeter machinery). Step 2: Specialize to Phi(t)=(t,t^2,t^{3/2},t^{1/2}) (d=4) to obtain the bilinear L^12 estimate on balls B_{N^2}. Step 3: pass to the actual domain Omega~ by two further 2D decouplings and periodicity, and from bilinear to linear by induction on scales (Bourgain-Guth), yielding Theorem 2 (A_6<<N^{6+eps}). Step 4: Theorem 2 gives Corollary 3 for A_6(N,delta,Delta), which feeds the Huxley/Bombieri-Iwaniec method's first spacing problem; combined with prior estimates for the second spacing parameter B, gives Theorem 4. Step 5: add exponent-pair/Huxley bounds on the remaining alpha-range and apply the classical approximate functional equation to get Theorem 5. Imported: Bourgain-Demeter L^6 decoupling for the parabola/planar curves; Huxley's Theorem 3; exponent pair theory (Graham-Kolesnik); Bombieri-Iwaniec double large sieve; Huxley-Kolesnik A_5 bound.

**Imported results.** Bourgain-Demeter L^6 decoupling for planar curves with non-vanishing curvature [B-D1]; Bourgain-Demeter l^2 decoupling for the moment curve / curves [B-D2]; Bourgain-Guth bilinear-to-linear induction on scales [B-G]; Huxley, Theorem 3 of [H1] (|S|<<T^{(4+103 alpha)/128+eps}, 12/31<alpha<=1); Exponent pair (1/9, 13/18); Huxley-Kolesnik A_5 bound; Bombieri-Iwaniec double large sieve ([B-I1], [H-W] Lemma 3.6); Approximate functional equation for zeta (Titchmarsh)

**Techniques.** l^2 decoupling for non-degenerate curves (Bourgain-Demeter); Bilinear-to-linear induction on scales (Bourgain-Guth); Discretization to exponential sums and counting of solutions to Vinogradov-type systems with fractional powers; Bombieri-Iwaniec / Huxley method and double large sieve; Exponent pair theory (van der Corput processes); Taylor expansion of (N_0+m)^{3/2}, (N_0+m)^{1/2} to expose cubic/quartic phases (2.18)-(2.19)

## Context and interpretation

**Importance and obstacle overcome.** First use of decoupling in the Bombieri-Iwaniec method and the first improvement of the zeta subconvexity exponent via it; doubling the saving over 1/6 of Bombieri-Iwaniec (9/56 -> 13/84) and improving Huxley's 32/205. Obstacle: obtaining an optimal mean value for the first spacing problem (A_6), previously only A_5 bound (Huxley-Kolesnik), via a new decoupling for the 4-dimensional curve (t,t^2,t^{3/2},t^{1/2}) that is not a moment curve.

**Relation to prior work.** Builds on Bourgain-Demeter decoupling [B-D1,B-D2], Bourgain's earlier recovery of the Huxley-Kolesnik A_5 result [B], Huxley's treatise [H], and Bombieri-Iwaniec [B-I1,B-I2]; supersedes Huxley's 32/205.

**Limitations and open questions.** Only improves the subconvexity exponent from 32/205 to 13/84; the Lindelof exponent 0 and the exponent 1/6 barrier were not the target. The A_6 bound is essentially sharp, so further gains must come from the second spacing problem (the parameter B) which remains sub-optimal; the author notes this is non-trivial and not resolved. The decoupling is stated with an L^p weight technicality ignored in the text.

## Research potential

- **Hypotheses that might be weakened.** Theorem 1 requires d even and O(1)-separated intervals; an extension to odd d or to non-separated intervals would give higher-moment bounds A_r for r>6. The bound is already sharp for A_6; improving 13/84 now requires attacking the second spacing problem or extending to A_7, A_8.
- **Generalizations.** Extend to Dirichlet L-functions (subconvexity in t-aspect for L(1/2+it,chi)), to Hecke L-functions, and to other exponential sums (e.g. Weyl sums with fractional powers). Combine with larger iterates of the Bombieri-Iwaniec method.
- **Candidate connections.** Lindelof/density-hypothesis programme: improved subconvexity feeds directly into explicit zero-density exponents (e.g. Kadiri-Lumley-Ng uses an explicit van der Corput constant; an explicit version of 13/84 would improve their constants), and into short-interval prime estimates via Ingham's argument. Signed native/Mobius cancellation: no direct route, but the zero-density exponent 2(1+2c)(1-sigma) is tied to c=13/84.
- **Reusable lemmas.** Theorem 1 (decoupling for curves with non-vanishing Wronskian, d even) and the bilinear-to-linear induction argument (2.24)-(2.26) are reusable; Theorem 6 gives a new exponent pair (13/84+eps,55/84+eps) usable in any exponent-pair computation.
- **Possible experiments.** Numerically count solutions of the system (2.14)-(2.17) (with the O(N^{-1/2}) tolerance) for N up to 200-500 to test N^{6+eps} behavior; compute constants in an explicit version of Theorem 2 for use in explicit zero-density work.
- **Risks / barriers.** The result is not explicit (no numerical constant for implied constants or eps); making Theorem 5 explicit would require tracking constants through decoupling (Bourgain-Demeter constants are not explicit). The 1/6 barrier of van der Corput type is only moved, and the second-spacing bottleneck remains. No implication for RH beyond via Lindelof-type exponents.

## Audit notes (Level 1 reader)

In the published version the author acknowledges a referee who supplied an alternative treatment of Section 3 leading to the improved 13/84 (the original manuscript gave a weaker exponent). Reading arXiv v2, the abstract's 'improved bound 13/84' agrees with Theorem 5. The range of delta in Corollary 3 as extracted reads N^{-1/2}<=delta<=1; compare with the introduction's statement that A_5 holds for N^{-1/2}<=delta<=N^{-1}, so check the exact ranges in the PDF. The weighted L^6 technicality is explicitly ignored in the exposition. Otherwise none noticed in inspected portion.

*These notes are a reader's observations, not verified findings; see `audits/` for adjudicated findings.*

## Provenance

- Candidate `CAND-01954`; harvest queries: kw_moments_zeta, msc_11M06, arxiv_critical_line.
- Triage decision: include — Bourgain's decoupling bound improving zeta growth on critical line.
- Record generated by `tools/make_records.py`; search cutoff 2026-11-17.
