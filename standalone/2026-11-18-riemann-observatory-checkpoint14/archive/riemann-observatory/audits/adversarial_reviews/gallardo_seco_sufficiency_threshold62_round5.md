# Independent review of sufficiency at the shifted threshold

2026-11-17. Reviewer threshold_review_62. Scope is the proposed sufficiency implication for the same parameter range, generators, and coefficient topology as Gallardo–Gutiérrez–Seco (2025), Theorem 5.5. I found a complete chain for this implication with the dependencies below. This is a scoped mathematical review, with novelty and wider adjudication pending.

## Source statements checked

The published Theorem 5.5, p. 26, uses `α∈[−3,−2]`, `1≤a<(1−α)/2`, and the source half-plane `Re s>−(α+1)/2`. Its Lemma 5.3 and equation (29) are on pp. 25–26, with the first-order operator introduced on p. 21 and the coefficient norm on p. 3. I read those passages in the local publisher text and regenerated the p. 26 text directly from the primary PDF. [Publisher PDF](../../sources/logarithmic_riesz_round3/gallardo_seco2025.pdf)

Báez-Duarte's actual arXiv:math/0202141v2 PDF, Lemma 2.1, p. 3, attributes its estimate to Balazard–Saias, *Notes sur la fonction ζ de Riemann, 1*, Lemme 2. Its quantifiers are `1/2≤β<1`, `δ>0`, `η>0`, `N≥2`, and `β+δ≤Re s≤1`, under zero-freeness for `Re s>β`. The error in the Möbius Dirichlet polynomial versus `1/ζ(s)` is `O_{β,δ,η}(N^{-δ/3}(1+|Im s|)^η)`. I checked the reproduced statement, which is the external estimate used below. The original 1998 proof was outside the review. The Mellin construction on pp. 4–5 of the same preprint uses the base `1/2`. Page 4 records the fractional-part Mellin identity immediately before (2.7). [Primary preprint](../../sources/equivalence_round2/baez_original.pdf) [Balazard–Saias DOI](https://doi.org/10.1006/aima.1998.1760)

Titchmarsh (1986) §2.12, equation (2.12.5), gives the genus-one completed-function product and the preceding paragraph gives reflection in the critical line. Section 5.1, equation (5.1.4), gives the classical convexity exponent `(1−σ)/2` for `0<σ<1`. Theorem 9.4 provides a zero count sufficient to obtain one nontrivial zero. These classical results are inputs. [Titchmarsh PDF](../../sources/equivalence_round2/titchmarsh1986.pdf)

## Arithmetic sufficiency for 1/2 ≤ b < 1

Set `t=−(α+1)/2`, `c=a−1`, `b=t−c`, so `0≤c<t` and `α+2c=−1−2b`. Let `H_b=L²((0,∞),x^{2b−1}dx)`. This exact Hilbert weight is determined by Mellin Plancherel. Substitution `x=e^v` identifies the norm with the Fourier-Plancherel norm of `e^{bv}f(e^v)`, with measure `dy/(2π)` on the transform side. A continuous-parameter `L^{1/b}` approximation theorem is unnecessary.

Assume no zeta zeros for `Re s>b`. Fix `0<e≤e₀<min(b/2,(1−b)/2,1/4)` and write `s₋=b−e+iy`, `s₊=b+e+iy`. For every completed-function zero `ρ`, put `β=Re ρ`. The difference of squared distances from the two lines is
`|s₊−ρ|²−|s₋−ρ|²=4e(b−β)≥0`.
The quotient of the exponential corrections in the canonical factors has modulus `exp(−2e Re(1/ρ))≤1` because the nontrivial zeros have nonnegative real part. Thus every finite product quotient is bounded by `exp(2e|Re B|)`, where `B` is the coefficient of `s` in the linear Hadamard exponential. The denominator converges to the nonzero `ξ(s₊)`. This bounds the quotient at each ordinate even if the numerator vanishes. There is no reflection step in this quotient argument. The right half-plane assumption puts every product zero on the required side.

From `ξ(s)=s(s−1)π^{−s/2}Γ(s/2)ζ(s)/2`, the gamma quotient in `ζ(s₋)/ζ(s₊)` is `Γ(s₊/2)/Γ(s₋/2)` and contributes `O((1+|y|)^e)` by uniform vertical Stirling. The other factors are bounded in this direction. Low heights are uniform because all real parts stay in a compact subinterval of `(0,1)`, including when a zero of `ζ` approaches the denominator line as `e→0`. The bound on the gamma and polynomial factors alone does not require a lower bound on `|ζ(s₊)|`. It follows that `|ζ(s₋)/(s₋ζ(s₊))| ≪_{b,e₀}(1+|y|)^{-1+e₀}`.

Let `ϱ_k(x)={1/(kx)}`, `F_{e,N}=Σ_{k≤N} μ(k)k^{-2e}ϱ_k`. For `0<Re s<1` the fractional-part Mellin integral is absolutely convergent and equals `−k^{-s}ζ(s)/s`. Each `x^{-e}ϱ_k` belongs to `H_b` from boundedness near zero and `O_k(1/x)` at infinity. The transform of `x^{-e}F_{e,N}` at ordinate `y` is
`−(ζ(s₋)/s₋)Σ_{k≤N} μ(k)k^{-s₊}`.
The reproduced Balazard–Saias lemma applies with base `b`, shift `e` and evaluation on the allowed lower boundary of its strip, with `b+e<1`. The transform error between this expression and `−ζ(s₋)/(s₋ζ(s₊))` is bounded by
`O_{b,e,η}(N^{-e/3}(1+|y|)^{−1+(1−b+e)/2+2η})`
by convexity on the fixed line `b−e`. Choose `4η<b−e`. The square of the ordinate factor is integrable. For each fixed `e`, the bound tends to zero in the transform norm as `N→∞`. Constants in this step may depend on `e`. No two-parameter uniformity is used.

For fixed `x>0` the floors `⌊1/(kx)⌋` are zero for `k>1/x` and the linear terms converge absolutely. Thus the pointwise limit is
`F_e(x)=x^{-1}/ζ(1+2e)−Σ_{k≤1/x}μ(k)k^{-2e}⌊1/(kx)⌋`.
An almost everywhere convergent subsequence of the norm-convergent sequence identifies the inverse Mellin limit with `x^{-e}F_e`. To remove `x^{-e}`, use the contraction by `x^e` on `(0,1)`, and on `(1,∞)` use convergence of the scalar coefficients of `1/x`, which has squared norm `1/(2−2b)` there. Hence `F_e` lies in the `H_b` closure of the finite `ϱ_k` span.

For almost every `y`, the boundary point `b+iy` is a nonzero regular point of `ζ`, and the transformed limit tends to `−1/(b+iy)` as `e↓0`. The exceptional ordinates of zeros form a discrete set. The uniform quotient bound gives domination in the squared transform norm. Mellin Plancherel yields `x^{-e}F_e→−1_{(0,1)}`. On `(0,1)`, contractive multiplication and `||(x^e−1)1_{(0,1)}||_{H_b}→0` give the same convergence for `F_e`. On the tail, the limiting coefficient `1/ζ(1+2e)→0` by the simple pole. It follows that `χ=1_{(0,1)}` belongs to the closed `H_b` span of the natural fractional-part functions.

Given a finite approximant `G=Σ d_kϱ_k`, its restriction to `(1,∞)` is `A/x` with `A=Σ d_k/k`. Along any approximating sequence to `χ`, `|A|≤(2−2b)^{1/2}||G−χ||_{H_b}→0`. Subtract `Aϱ_1`. The correction vanishes in norm, and the resulting approximant is exactly `Σ_{k≥2}(d_k/k)(kϱ_k−ϱ_1)`. This is the required constrained span. For `x∈(1/(n+1),1/n)`, `kϱ_k(x)−ϱ_1(x)=n−k⌊n/k⌋`. Labeling these intervals by coefficient index `n−1` takes `χ` to `f_0=1/(1−z)` and the generators to the remainder series `R_k`. Their exact interval weights are `(n^{-2b}−(n+1)^{-2b})/(2b)`. The derivative of `x^{-2b}` compares them above and below with `n^{-1−2b}`. Thus the step-function realization is isometric for the exact weights and a bounded isomorphism for the source coefficient norm, in which `f_0∈closure span{R_k}⊂D_{−1−2b}`.

## Shorter unshifted Mellin variant

The parent reviewer suggested estimating the quotient with numerator on the boundary line itself. This yields a shorter proof of the same arithmetic approximation. Take `s=b+iy` and `0<e≤e₀<(1−b)/2`. In the canonical product compare `s` with `s+e`. The squared-distance difference for a zero of real part `β≤b` is `e(2(b−β)+e)≥0`, the exponential correction has modulus `exp(−e Re(1/ρ))≤1`, and the gamma ratio is bounded by `C(1+|y|)^{e/2}`, uniformly as before. Thus `|ζ(s)/(sζ(s+e))|≪(1+|y|)^{-1+e₀/2}`.

Use `G_{e,N}=Σ_{k≤N}μ(k)k^{-e}ϱ_k` and its ordinary Mellin transform in `H_b`. This transform is `−(ζ(s)/s)Σ_{k≤N}μ(k)k^{-(s+e)}`. The same Balazard–Saias input with fixed shift `e` and convexity at the fixed real part `b` bounds its error from `−ζ(s)/(sζ(s+e))` by `O_{b,e,η}(N^{-e/3}(1+|y|)^{-1+(1−b)/2+2η})`. Here `4η<b` suffices for square integrability. Plancherel puts the inverse transform of the quotient in the closed natural span. Dominated convergence in the transform norm as `e↓0` places `−χ` there as well. This proof omits the `x^e` multipliers, the identification of a pointwise spatial limit, and the separate pole computation for the tail of that limit. The subsequent correction by `Aϱ_1` is still needed for the constrained remainder span. This is an internal simplification of the adaptation, with priority unassessed.

## Transfer to the original domain norm

For `c>0`, put `p=−α/2` and `m=p−c=b+1/2>0`. Write the matrix for multiplication by `u=(1−z)^{−c}` in the normalized source and target coefficient coordinates. The coefficients of `u` are bounded by `C_c(n+1)^{c−1}` by the gamma ratio, giving entrywise domination by
`C_c(n+1)^{-p}(n−j+1)^{c−1}(j+1)^m`, `j≤n`.
For `j+1≥(n+1)/2`, the bound is a constant times `(n+1)^{-c}(n−j+1)^{c−1}`. Row sums use `Σ_{l≤n+1}l^{c−1}≪(n+1)^c`. Column sums use `j≤n≤2j+1` and the same power sum, with `(n+1)^{-c}≤(j+1)^{-c}`. For `j+1<(n+1)/2`, the bound is a constant times `(n+1)^{-m−1}(j+1)^m`. Row bounds then use `Σ_{j≤n}(j+1)^m≪(n+1)^{m+1}` and column bounds use `Σ_{n≥j}(n+1)^{-m−1}≪(j+1)^{-m}`. This proves bounded multiplication `D_{−1−2b}→D_α` by the Schur test. For `c=0` it is the identity.

The target and generators belong to `D_{α+2}` before using any inverse. The coefficient formula `[z^n]h_k=H_n−H_{⌊n/k⌋}−log k` gives `O_k((n+1)^{-1})`. Splitting its convolution with the coefficients of `u` at `j=n/2` gives `[z^n](uh_k)=O_{c,k}((n+1)^{c−1}log(n+2))` for `c>0`. The exponent in the squared domain norm is `α+2c=−1−2b<−1`. For `c=0`, the constant and the direct `h_k` bound suffice. The analytic identities
`T_au=−uf_0` and `T_a(uh_k)=uR_k`
follow from `a=c+1` and `((1−z)h_k)'=(1−z)^{-1}−kz^{k−1}/(1−z^k)`.

For this case `a>t`. Indeed `a≥1≥t` with equality throughout only at `a=t=1`, which gives `b=1`. The strict inverse is valid. A direct check for `g=T_af` uses `F_n=Σ_{j≤n}f_j`, `H_n=(a+1)_n/n!`, `v_n=F_n/H_n`, and `d_n=g_n/((n+1)H_{n+1})`. The recurrence is `v_{n+1}−v_n=d_n`, and `f_n=(a)_n v_n/n!+g_{n−1}/(n+a)` for `n≥1`. With `δ=a−t>0`, the choice `v_n=−Σ_{j≥n}d_j` is well defined by Cauchy–Schwarz. In normalized coefficients its tail matrix is bounded by a constant times `(n+1)^{δ−1/2}(j+1)^{-δ−1/2}1_{j≥n}`, bounded by Schur weights `(n+1)^{-1/2}`. The shifted term is bounded directly. The analytic kernel is spanned by `(1−z)^{−a}`, whose domain norm diverges, establishing injectivity. Apply this inverse to `u` times the remainder approximants for `−f_0`. It gives approximants from the requested span converging to `u` in the original norm. [Strict operator audit](gallardo_seco_operator_impact_advocate_round4.md)

## Boundary cases and scope

If `0<b<1/2` the hypothesized zero-freeness fails by the Riemann–von Mangoldt count and symmetry. Sufficiency is then vacuous. Failure of the closure in that range is a separate necessity result.

If `b=1`, necessarily `(α,a)=(−3,1)`. The half-plane on the right is zero-free by the Euler product, the Mellin tail norm above diverges, and the inverse above is critical. The needed direct conclusion is `1∈closure span{h_k}⊂D_{−1}`. The independent Bergman proof uses `V_N=Σ_{k≤N}μ(k)h_k/k` with `h_1=0`. Its first `N+1` coefficients agree up to a central error controlled by `A_N=Σ μ(k)/k` and `B_N=Σ μ(k)log(k)/k`, with `A_N` and `B_N+1` smaller than every fixed reciprocal log power by classical unconditional estimates. For `n>N` the coefficients are `O(N/n)` by the exact `h_k` coefficients. The resulting bounded sequence converges coefficientwise to 1, hence weakly to 1. The norm-closed span is weakly closed. This verifies the endpoint reduction using the previously independently reviewed proof and its declared arithmetic dependency. [Bergman reconstruction](../../proposals/independent_campaigns/noor_critical_bergman_advocate_round4.md) [Independent Bergman review](noor_critical_bergman_skeptic_round4.md)

The main proof uses the original p. 3 version of Báez-Duarte's quoted estimate, classical zeta identities and convexity, and elementary Hilbert-space arguments. No source-wide audit, publication novelty judgment, or claim of acceptance is made.
