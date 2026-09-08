# Scientific review of post-integration work — first pass

**Disposition: substantive first-pass review completed; second pass required before integration preparation.** No change to main or any research source is authorized by this report. Recommendations below are review findings, not new canonical acceptances.

## 1. What was actually reviewed

The reference scientific integration is PR #800 at `4f461e5ad46e452b1eafa69eddff3b76cd0c12be`. The current main inspected is `c07aa6adcb1e8afa8bac4c5d6f921a822629b236`. Its intervening presentation, contribution, licensing and validation changes are not another research wave. Their newer cumulative organization should be retained during the eventual integration.

The identified research surface comprises PRs #803, #804, #805, #811, #812, #814, #817, #818, #819 and #823, plus the branch-only all-rank spectral classification. Their **39 distinct packet roots** are listed in [CENSUS.tsv](CENSUS.tsv), with exact heads in [SOURCE_FREEZE.json](SOURCE_FREEZE.json). Twelve packets received substantive paper review; the other 27 received inventory and triage only. Supporting code, artifacts, discussions and dependency files are not all covered merely because a main manuscript was read.

The discovery pass used recent PRs in all states, changed-file inventories, dated branch searches, parent comparisons and publication comments. Two recently updated old PRs, #396 and #440, still have heads already present in the previous review records; their update timestamps do not establish new mathematical deltas. The eleven original programme issues were not returned as newly updated issues in the recent issue query. This is not a claim to have discovered every arbitrary unadvertised or deleted branch.

Three immediate completeness findings matter. **First**, #804's opening description does not cover its later domain-cutoff and Möbius-work/resonance additions. **Second**, #811 contains a later-published prime-discrepancy packet as well as its endpoint-prime-discrepancy predecessor; their overlap must be reconciled rather than counted twice. **Third**, the all-rank classification is present on a research branch without a matching PR. A PR-number-only integration would miss it.

## 2. Overall mathematical assessment

There is substantial component progress. In particular, the new papers do more than rename the old open estimate: they prove an all-scale positive density, identify an operator domain and graph core, quantify approximation toward the actual source subspace, separate summable prime-detail error from cumulative discrepancy, and classify a full spectral intersection at every rank.

I found **no demonstrated fatal mathematical error in the inspected component arguments**. This is deliberately narrower than a clean bill of health for the entire corpus. Numerical signs, supporting producer implementations, several inherited analytic adapters and 27 packets remain unreviewed or partly reviewed. The two most consequential computer-assisted claims are held for actual independent certificate work, not accepted from their reported PASS markers.

The common unresolved distinction is now sharper: a positive source, a well-conditioned finite Gram matrix, a rapidly vanishing approximation excess, and a small upper bound for an intrinsic defect do not prove that the defect is zero. Several new papers correctly prove this limitation rather than concealing it. None of the inspected papers supplies an unconditional proof of RH.

## 3. Jordan positivity and the literal source domain

### 3.1 Global Jordan density, rather than a finite scale range

Source JG is the sharp-Jordan-Green packet on #804, including both `PROOF.md` and `REAL_AXIS.md`. For the source-defined Jordan coefficients, write

$$F_s(n)=\prod_{p\mid n}(1-p^{-s}),\qquad c_s=1/\zeta(1+s),$$

$$E_0(t)=\sum_{n\le e^t}F_s(n)/n-c_st,\qquad E_1(t)=\int_0^tE_0(u)\,du,$$

$$B_{s,\kappa}(t)=-c_s+\frac{\kappa s}{2}E_0(t)+s^2E_1(t).$$

The paper proves nonnegativity for all positive scales and all times precisely at the threshold class $\kappa\ge2$, with strict positivity at each fixed point for $\kappa=2$. It also supplies the stated strictly positive margin for the original coefficient $\sqrt{275/14}$. This is materially stronger than the older large-scale Green-density range.

The reconstruction checked the geometric-prime association argument, the native coefficient prefix, the factorial/von-Mangoldt lower bound and the local polynomial majorants. The reviewer code independently checks the rational endpoint identities and their connecting margins, including $47/1280$, $1/256$ and $203/3750$ in the source's respective scaled regimes. It does not replace the paper's all-parameter argument with a finite sample.

The Gamma factor must be grouped using its recurrence before positivity is inferred. The isolated rational factor $(q+1)/((q+s)(q+s+1))$ is not by itself a universally positive Laplace factor for all parameters. The manuscript's grouped expression avoids that inference. Likewise, its positive density is used in its declared convergent transform domain, not continued as a positivity theorem at the critical boundary.

The companion real-axis argument gives, for $0<s\le1$,

$$s^2\sum_p\frac{\log p}{p^s(p-1)}-c_s>\frac{13}{900}s^2c_s>\frac{13}{1800}s^3.$$

The Euler--Maclaurin derivative bound and the prime-two contribution leave exactly the positive rational margin $1/9-29/300=13/900$. This closes the named old scalar question; it does **not** construct the completed critical source-to-Hardy intertwiner. Recommendation: retain the density and scalar results as separate all-scale components after the remaining source/implementation reconciliation, and update that old obstacle without retiring the critical-domain obstacle.

### 3.2 Positive factorial source and a nontrivial closed range

The two CSM manuscripts construct

$$d_b(t)=e^{-bt}\{\lfloor e^t\rfloor(1-t)+\log(\lfloor e^t\rfloor!)\},\qquad
D_b(z)=\frac{(z+b-1)\zeta(z+b)}{(z+b)^2}.$$

The removable value is analytic. Positivity and elementary integrable envelopes do not make this transform outer. The closed cyclic source space is $B_bH^2$, with $B_b$ retaining the right-of-line zero divisor. The exclusion of a singular inner factor uses analytic continuation through finite boundary points and the radial asymptotic, rather than assuming zero-freeness.

The small-time contractive estimate, the isometry on the actual source range, and the maximal causal multiplier domain are different statements. In particular the maximal domain can cancel a common inner factor and be larger than the original source space. I checked that the papers do not silently replace one by the other. Finite positive-definite source Grams hold independently of RH and therefore cannot establish completeness. The reviewer code reconstructs the positive-source countercontrols and their nonzero limiting defect.

### 3.3 Compact inverse inputs and full tails

The compact-domain packet CD retains an ordinary compact $L^2$ input, not a Dirac input. With $X=N+1$ its terminal correction makes $P_N(1)=0$, and the convolution equals the desired ramp on the exact initial horizon. The reviewer code reconstructs the finite divisor identity and endpoint balance, plus the signed input-work formula through 512.

The paper distinguishes unconditional convergence on the absolutely convergent side from convergence under RH with a strict positive damping margin. Those estimates cannot simply be evaluated at their critical endpoint. A hypothetical zero gives a lower bound for the **whole delayed output error**; divergence of the input work alone is not divergence of that output. Recommendation: retain the construction and lower-bound interfaces at their stated parameters; leave the actual numerical campaign and the later cutoff/work packets for pass two.

## 4. Weil-window core, local positivity and residual growth

### 4.1 An operator-core theorem closes a genuine analytic omission

LC starts from the exact full arithmetic window kernel and the earlier positive finite-codimension sector. Its primitive derivative operator is an unbounded logarithmic Fourier multiplier plus a bounded compressed term, not the original compact positive block on $L^2$.

The domain argument is persuasive at the stated fixed-window scope. Exterior leakage is represented by a Carleman kernel, giving a bounded two-sided exterior map. The interior distribution is $L^2$ modulo the finite constraints. A residual supported at the interval endpoints is excluded in $H^{-1/4}$, so no unaccounted delta term survives. Shrinking, mollifying and correcting moments gives an **operator core**, not merely a form core.

That domain identification supports the fixed polynomial test family and dense strong-residual range. Ridge regularization permits dependent columns. Comparison with a fixed finite approximant proves that the residual Gram tends to zero. Consequently

$$U_m-C_\kappa R_m\preceq S_L\preceq U_m,\qquad R_m\longrightarrow0,$$

with $C_\kappa=3$, or $15/8$ in the specified length-one sector. Both enclosure sides converge; no monotonicity of this ridge sequence or rate uniform in window length is claimed. This is a useful improvement over having upper Galerkin approximations only.

The conditional strictness argument under RH also has a legitimate extra ingredient: uniqueness for compactly supported distributions with a superlinear set of distinct zero ordinates. It does not infer strictness merely from strict positivity on ordinary $L^2$ tests. Its Littlewood/Riemann--von Mangoldt input still requires exact literature/source confirmation in pass two. A universal family of finite strict certificates, one for every integer window, is not one finite certificate or a proof that the family exists.

Recommendation: retain the fixed-window core and strong-residual convergence as paper components. Keep their general analytic statement, their application to the exact arithmetic kernel, the strictness corollary and an implemented primitive matrix engine separately identified.

### 4.2 The proposed actual length-one certificate is important, but not yet replayed

WP proposes a strict lower bound for the actual complete form on every interval of length at most one, with arbitrary complex $L^2$ tests. It is not just positivity on a finite basis. A rational spectral extension agrees with the arithmetic kernel on the needed difference interval; positive Fourier coefficients then give an $H^{-1}$ lower norm. The companion dual construction gives a strictly positive lower matrix for the complete effective $S_1$ without assuming an $L^2$ minimizer.

I checked the proof architecture, the prime-two cusp, Fourier/Sobolev normalization, periodic extension, and distinction between global positivity of the extension and positivity of the prescribed arithmetic continuation. The periodic extension is not the actual kernel beyond the unit difference interval. Nor is the claimed lower norm an $L^2$ spectral gap for a compact operator.

**Hold:** I have not independently reconstructed all 2,049 finite coefficient inequalities, the 256 residue-class bounds, the positive gamma-tail contribution, or the accepting interval implementation. The DLMF digamma remainder contract is identifiable, but recognizing its formula is not validating the implementation. If that work passes, this is a meaningful new local theorem and the current `S1 sign not supplied` description can be updated. Until then, retain the analytic conditional certificate theorem and hold the asserted numerical sign.

### 4.3 Residual exponent: an exact characterization, not an evaluated edge

RG retains both safe constraints $p(1)=0$, $p'(1)=1$ for the actual Möbius-prefix completion. The complete residual norm and its minima over support at most $2Y$ or over arbitrary finite supports have limiting logarithmic exponent $2\Theta-1$, where $\Theta$ is the unknown zero abscissa. The explicit two-endpoint completion attains that power exponent without being claimed a finite optimizer.

I checked the two-jet normalization and the projected Hardy evaluation lower bound. The denominator $|1-\rho|^2$ belongs to the projected kernel with the extra safe constraint; it is not obtained by forgetting that constraint. The upper argument uses strict lines to the right of $\Theta$, a half-integer Perron cutoff, and the complete high-frequency tail. The endpoint case $\Theta=1$ and nonattainment of the supremum are separately handled.

Recommendation: retain the spectral growth classification after the predecessor and full code/source check. It does not give a known fixed power saving while $\Theta$ remains unevaluated, an effective stopping rule for the arbitrary-support infimum, or RH.

## 5. Quantitative capture and intrinsic entropy

### 5.1 The target rate is to the actual subspace, not an outer substitute

HC works with $A(w)=w\zeta(1/(1-w))=B(w)O(w)$, $A(0)=1$. Its main target theorem is

$$0\le U_K(q)-\operatorname{dist}(q,BH^2)^2
\le C(\|q\|_{H^{1/16}_{\rm Sob}}+\|q\|_\infty)^2
\exp[-c\sqrt{\log(K+2)}].$$

Here the fractional Sobolev space is not a Hardy space of exponent $1/16$. The paper uses the elementary convexity consequence of the approximate functional equation, a derivative estimate from Euler summation and Cauchy, small-value distribution rather than zero-freeness, clipped **outer** inversion, and a fractional regularity estimate for the possible Blaschke factor.

I reconstructed the small-value/Jensen mechanism, the exceptional-arc budget, the Fejer and Holder exponents, and the projection to $BH^2$. No unjustified low-regularity Sobolev algebra estimate or boundedness of the Hardy projection on $L^\infty$ is needed. For the exact horizon targets it gives an excess bound of the form

$$U_K(T)-C_B(T)\le C(1+T)^2e^T\exp[-c\sqrt{\log(K+2)}].$$

An enormous predetermined rank schedule removes the excess. It does not bound $C_B(T)$. An off-line zero forces exponential intrinsic cost. Recommendation: retain this as a quantitative approximation theorem with the source-space floor displayed, not as source completeness. The implementation and compact-input realization inherit distinct earlier packets still in the second-pass queue.

### 5.2 Entropy identifies the remaining floor; the small upper certificate is separate

IE connects the source-space defect to the classical Balazard--Saias--Yor logarithmic quantity

$$J=\frac1{2\pi}\int_{\mathbb R}\frac{\log|\zeta(1/2+it)|}{t^2+1/4}\,dt,\qquad
\delta=1-e^{-2J}.$$

The paper retains the full zero divisor and absolute logarithmic integrability. This is credited classical background, not a newly discovered RH criterion. The ramp target $1-w$ has cost $C_0=2-|b_0-b_1|^2-|b_0|^2$, with the genuine cubic sensitivity loss $\delta^3/4\le C_0\le4\delta$. The reviewer code checks the sharp lower factorization. The first logarithmic moment, strip-qualified lower refinement and Toeplitz determinant ratio are consistent with that normalization.

Finite entropy decreases to $J$, not automatically to zero. The proposed rate corollary inherits HC, while the basic entropy/target identities do not. The degree-six trial claiming full error below $13/250$ and $J<27/1000$ needs independent producer/interval-tail replay. It remains **held computational evidence** in this pass. A positive lower endpoint of its trial error is not a positive lower bound for the optimum or for $J$.

## 6. Ordinary-prime energy, tapering and square-grid localization

CCT correctly retains the sharp-cutoff endpoint state in the full norm. Its fixed logarithmic cutoff average preserves the exact initial source and controls the entire future memory. If the weighted prime-discrepancy energy $J_{\rm prime}$ is finite, the squared tapered error is at most six times its remaining state-energy tail. Bounded tapered norms on an unbounded sequence imply finiteness in the reverse direction.

The finite-energy-to-RH argument constructs an analytic exponential and identifies it first in the Euler half-plane. It does not assume a logarithm of zeta across unknown zeros. The converse uses the classical **RH-conditional** Cramer mean-square input. The Brent--Platt--Trudgian source explicitly states RH for its upper bound; its unconditional lower bound cannot replace that assumption. The resulting logarithmic convergence is not $L^2$ convergence after exponentiating. The higher-prime-power tail adapter inherited from PDS remains on the pass-two dependency list.

SSQ then proves a genuinely unconditional local approximation using only the coarse Brun--Titchmarsh interval bound. For $e(x)=\pi(x)-\operatorname{Li}_2(x)$ on the square cells, with $w_n=1/n^2-1/(n+1)^2$, the within-cell variances satisfy

$$\sum_{n\ge N}d_n<28/\log N,\qquad N\ge2.$$

The held-endpoint error has the corresponding bound $112/\log N$. I reconstructed the range-width estimate, weighted variance, constants and norm equivalence between the ordinary and square-root-weighted prime discrepancies. The global causal norm comparison is not asserted for arbitrary tail restrictions without memory terms.

All potentially infinite energy is left in the cumulative cell means, equivalently in the weighted square-endpoint samples. The prior cumulative level in the exact cell formula cannot be reset to zero. The code includes a shifted-level countercontrol with unchanged local detail. This is a clean integration candidate as an unconditional **local-detail theorem**, with the coarse-energy assertion visibly open and its RH-equivalence retaining the conditional converse input.

## 7. Late-tail perturbations: a useful rigorous obstruction

LT constructs sources arbitrarily close to the literal positive factorial source that preserve any fixed initial horizon, finitely many safe jets, crude norm bounds and finitely many strict certificates. A delayed rational filter inserts a conjugate interior zero pair near a classically existing boundary zero. The proof retains the original interior zeros with multiplicity, controls the whole perturbation relative to the positive source, and distinguishes ordinary output functions from compact inputs.

The changed cyclic domain is a proper subspace of the original one, and the projection operator-norm difference is exactly one, although the projections converge strongly on each fixed test. The entropy increases strictly but tends back to its original value. I checked the interpolation, complete Fourier-cancellation tail bound, jet-filter variation budget, entropy comparison and finite Gram perturbation implications.

Recommendation: retain the construction and topology/stability obstruction. The altered sources do **not** preserve the infinite factorial formula, Euler product or functional equation. They are not off-line zeros of zeta, nor a refutation of all arithmetic approaches. LT does not depend on HC's proposed quantitative-capture theorem; do not unnecessarily propagate that dependency into its standalone result.

## 8. The branch-only all-rank spectral classification

TSR compares the complete multisets for $\mathrm{Std}(u)\otimes\mathrm{Sym}^r(v)$ and $\mathrm{Sym}^{2r+1}(w)$, including multiplicities and the required raw scaling. Taking one adjacent eigenvalue ratio forces a monomial lift. If $w$ is noncyclotomic, the maximum-weight argument gives exactly the signed graph loci. Nongraph torsion has bounded order at each rank, so there are no further positive-dimensional reduced components.

For rational raw traces and positive rational $q$, algebraic integrality restricts torsion to four square-class alphabets in the 24th roots. The rank dependence is affine on each residue class modulo 24. The independent reviewer implementation solves **all 4,320 affine vector equations for every nonnegative rank quotient**, not merely a large finite range of ranks. It finds 560 admitted affine families, including 24 nongraph affine families, and no isolated additional nonnegative quotient.

The full raw exception is exactly

$$r\equiv3\pmod4,\qquad A=0,\qquad B^2=C^2=2q.$$

Thus it is unavailable for positive odd integer $q$ with integral raw traces. This restriction must not be generalized to every rational $q$. The reduced geometric statement is not a calculation of scheme multiplicities.

The nonabelian obstruction also survives paper review: squaring eigenvalues removes a pointwise square-root choice, and restriction to an $SL_2$ factor makes the highest weights on the two sides incompatible. Its reductive characteristic-zero, common-determinant and dense-set hypotheses are essential. It does not prove a statement on arbitrary positive-density Frobenius subsets or rule out every abelian realization.

Recommendation: include this previously unindexed deposit in the next integration plan as a standalone spectral/algebraic component. Do not infer global Euler-product equality, automorphy, a compatible family or RH from the local classification.

## 9. Integration implications, not integration actions

The likely cumulative additions are: all-scale Jordan positivity; a precise actual source-domain dictionary; a logarithmic core and vanishing residual enclosure width; quantitative target capture to the true floor; entropy/target sensitivity identities; square-grid local-detail summability; late-tail perturbation controls; and an all-rank spectral classification. The unit-window theorem and actual entropy trial need computational clearance first.

Keep the ordinary-prime energy, the factorial-source entropy and the floor-residual energy separately named. Several manuscripts use the letter J for different quantities. Equal RH relevance does not identify their finite values, target vectors, norms or rates. Likewise a later paper reconstructing one predecessor lemma does not review the predecessor's entire packet.

No public pages, registries, source manifests or original proofs are edited by this review. Pass two should finish the remaining packets and evidence rather than reopen the presentation or initiate an unrelated research campaign. Its explicit queue is [PASS2.md](PASS2.md).
