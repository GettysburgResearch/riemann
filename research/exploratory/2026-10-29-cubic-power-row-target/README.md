# A cubic power-row target for a stronger zeta strip

**Status.** This is a conditional reduction and a comparison with existing source-qualified estimates. The proposed Möbius-specific moment is open and no new zero-free region is proved. The elementary power-row implication is already recorded more generally in [the n-th-power note](../2026-10-29-power-row-spectral-boundary/README.md).

Let K=Q(ω), fix the source good set S, and let χ_n(u) be a zero-extended cubic residue character, with the finite ray-sector conventions made explicit as in the cited n-th-power note. For D=Y^r define the normalized Möbius inverse polynomial and its all-natural-row energy

    M_u(D)=D^(−1/2) Σ_(n good) μ_K(n)ν(n)χ_n(u)W(Nn/D),
    I₃(Y,D)=Σ_(0<Nu≤Y) |M_u(D)|²,                            (1)

where ν is a fixed finite-order Hecke character supported at the fixed bad set and W=W₀ is the single fixed nonnegative smooth annular profile from the linked n-th-power note, whose Mellin transform is nonzero on Re s>0; retain the original zero masks. More generally one may assume the bound uniformly for all fixed admissible profiles, but an arbitrary one-profile bound need not detect a zero at which its Mellin transform vanishes. All row and column presentations must be compatible with a finite ray decomposition; the energy in (1) must count all natural rows, including cubes. A single primary element per good principal ideal provides the relevant rows, and bounded unit multiplicity is harmless in this fixed field.

On every cube row u=v³,

    χ_n(v³)=1_((n,v)=1).                                     (2)

Take good principal prime ideals v of norm ≍Y^(1/3); there are ≫Y^(1/3)/log Y. For each such v, the masked inverse differs from the corresponding unmasked fixed-field Möbius sum by `≪D^(1/2+ε)/(Nv)`, up to fixed-sector and endpoint factors. Consequently a bound

    I₃(Y,Y^r) ≪_ε Y^(1+ε),                                 (3)

for every ε>0, for this specified W₀ and `0<r≤4/3`, implies

    Θ_(L_K(s,ν)) ≤ 1/2 + 1/(3r),

more concretely that the primitive Hecke L-function `L_K(s,ν)` is zero-free in `Re s>1/2+1/(3r)`; for ν=1 it gives the same bound for ζ_K. This is the n=3, unmarked case of the power-row/Mellin implication in the linked note. The elementary prime-mask error is dominated by the moment-derived Y^(1/3+ε) normalized bound when r≤4/3, including r=9/10. For ν=1 and any r>0, the cited power-row note instead uses reciprocal-zeta bounds on fixed zero-free lines, giving (3a) below; no all-r extension to general ν is asserted here. As ζ_K=ζ·L(s,χ₋₃), the ζ_K conclusion implies the same boundary for the Riemann zeta function.


For ν=1, the full quantitative cube-row statement in the linked power-row note gives

    limsup_(Y→∞) log I₃,cube(Y,Y^r)/log Y
        = 1/3 + 2r(Θ_K−1/2),                               (3a)

where Θ_K is the supremum of real parts of nontrivial zeros of ζ_K and the fixed W₀ has a zero-free Mellin transform on Re s>0. It uses reciprocal-ζ estimates on fixed zero-free lines, the prime ideal theorem and all mask/unit conventions from that note. The endpoint Θ_K=1/2 uses existence of a critical-line zero, which follows from zero existence and functional-equation symmetry in that case.

At `r=9/10`, the hypothetical bound (3) would give

    Re s > 47/54 = 0.870370370… .                           (4)

This is a fixed improvement over the tracker candidate 0.8738694, if both source-dependent statements and all bridges were established. The requirement to beat the staged candidate 4369347/5000000 is `r>5000000/5608041≈0.891577`; beating 7/8 requires `r>8/9`. None of these inequalities proves (3).

## The actual source bounds and the obstacle

De Faveri's [arXiv:2610.04045v1, Theorem 1.1 and Lemma 6.1](https://arxiv.org/abs/2610.04045v1), together with the unrestricted-row n=3 decomposition described in [the general sieve note](../2026-10-29-conjugate-conductor-sieve/README.md), gives the coefficient-uniform bound

    I₃(Y,D) ≪ (YD)^ε [Y + Y^(1/3)D + (YD)^(2/3)].           (5)

For D=Y^(9/10), the last term is Y^(19/15), so this generic upper bound is `Y^(19/15+ε)`. It already uses the fact that the Möbius column is squarefree and has bounded normalized ℓ² mass; it does not exploit further cancellation in μ.

For the **principal finite twist**, the more specialized [rStation paper 52 v5, Corollary 3.10 (N1)](https://rstation.ai/problems/riemann_hypothesis/papers/52/v5) asserts the strictly stronger actual-Möbius estimate

    I₃(Y,D) ≪ (YD)^ε [Y+Y^(1/3)D],                           (5a)

including every good natural row and its original cube/deletion masks, for fixed common smooth profiles and polynomial-length data. This source and its cited Type I/II and sieve inputs have not been independently verified here. At D=Y^(9/10), (5a) gives `Y^(37/30+ε)`, leaving a Y^(7/30) saving to (3). For `r≥2/3`, its exponent is E=1/3+r; the cube-row extraction only forces `Θ_K≤1/2+(E−1/3)/(2r)=1`, so (5a) yields no nontrivial boundary through this route. Its principal-twist restriction must not be dropped when discussing general ν.

This loss cannot be removed by merely proving a better arbitrary-coefficient cubic sieve. De Faveri–Dunn–Hoffstein, [arXiv:2607.07911v2, Theorem 1.1](https://arxiv.org/abs/2607.07911v2), prove the cubic operator lower bound

    Ξ₃(A,B) ≫_ε (AB)^(−ε)[A+B+(AB)^(2/3)]                 (6)

for their squarefree primary Eisenstein row and column families. At A=Y, B=Y^(9/10) its last term is `Y^(19/15−ε)`. Its matrix orientation is transposed relative to (1), but transposition preserves the operator norm. These squarefree rows are a subset of the all-natural rows, so a coefficient-uniform Y-sized bound for the complete squarefree-column matrix is impossible after matching the fixed S/sector presentation. The paper states its norm for full cutoffs; a dyadic partition gives a corresponding obstruction to bounds uniform over all fixed annular profiles, up to logarithmic losses. The lower-bound vector is **not** shown to be the Möbius vector, so (6) does not disprove the target (3).

The recent OpenAI [September 30 manuscript, Lemma 17.1](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) asserts a Möbius-specific all-row bound for **sextic** twists when D<Y with fixed margin. It cannot simply be re-labelled cubic: writing a cubic twist as `χ₆,n(v²)` sends rows Nv≤Y to sextic rows of norm at most Y², and its Y²-sized bound is too large. Nor can the arbitrary cubic sieve be replaced by that coefficient-specific sextic statement without a separate proof. The cited manuscript and its analytic dependencies remain unverified here.

The cubic Poisson transform of the actual μ coefficient also does not match the coefficient in [rStation paper 5 v3, Theorem 1](https://rstation.ai/problems/riemann_hypothesis/papers/5/v3). On good squarefree n, the source's Gauss identity is `γ₂(n)^3=μ(n)α(n)` and cubic parity gives `γ₋₂(n)=overline(γ₂(n))`; hence

    μ(n)γ₋₂(n)=α(n)^(−1) γ₂(n)²=α(n)^(−1)G(n)^(−1)γ₁(n). (7)

The final equality uses the same source identity γ₁γ₂=μαG, with G a fixed ray phase: the coefficient is a single sextic Gauss sum, not a single cubic-theta coefficient. Paper 5 Theorem 1 treats `μ(n)α(n)^jγ₂(n)` with j=±2, not (7). This is not a harmless fixed ray phase: if their ratio were a fixed finite-ray character, then on good primes its cube would be `α(n)^(−2−3j)`, i.e. α⁻⁸ or α⁴, which varies with the prime's angle within a fixed ray sector. Its printed upper bound is Y-sized in particular once N≥B^(3/2); the direct Poisson scales here are N≈D²/Y=Y^(4/5), B≈D=Y^(9/10), well outside that range. Thus this source does not establish the missing cubic inverse moment.

The concrete open analytic target is an all-natural-row, Möbius-specific estimate (3), including cube rows, the exact nonunit masks and a common profile. It must save Y^(7/30) over the stated principal-twist Möbius-specific source bound, or Y^(4/15) over the sharp arbitrary-coefficient operator bound, at this scale. No unconditional claim is made that the target fails: its cube rows show only that proving it would itself establish the improved zeta boundary (4).

**Independent review:** Families checked the cube-row extraction, 47/54 boundary, fixed-profile/mask qualifications and the squarefree arbitrary-coefficient lower-bound scope. The imported source inequalities and the unproved target remain separate inputs.

## The squared cubic Gauss root and the sixfold cover

Patterson's cubic theta coefficient formula, in the conventions of [OpenAI October 5 §2.4](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex), says for good squarefree primary n and λ=1+2ω that

    c_θ(n)=3^(5/2) overline(χ_n(λ)^2) γ₂(n).               (8)

Combining (7)–(8) identifies the cubic-Poisson coefficient exactly as a fixed ray/angle multiple of a **pointwise square**:

    μ(n)γ₋₂(n)
      = 3^(−5) α(n)^(−1) χ_n(λ)^4 c_θ(n)²
      = α(n)^(−1) G(n)^(−1) γ₁(n).                         (9)

All nonunit zeros are retained. This is not automatically a Fourier coefficient of the pointwise automorphic product θ(z)²: the latter's Fourier coefficients are additive convolutions in the index, whereas (9) squares one coefficient at the same n. Nor does a bound for the usual Rankin–Selberg series of |c_θ(n)|² automatically bound the complex square with a moving character twist.

There is a precise sixfold-metaplectic connection. Chinta–Friedberg–Hoffstein, [*Multiple Dirichlet Series and Automorphic Forms*, §4.2.2–4.2.3](https://chinta.ccny.cuny.edu/publ/cfh2.pdf), explicitly connect squared cubic Gauss sums via Hasse–Davenport to conjugate sixth-order Gauss sums and to Fourier coefficients of a sixfold-cover Eisenstein series. Their discussed series arises from functional equations of GL₂ L-functions twisted by cubic characters, and includes additional Euler-correction polynomials and bad-prime factors. That connection supports using sixfold spectral methods, but the cited discussion does not state an all-natural-row mean square of (9) with the present moving cubic residue twist, fixed angular α⁻¹ and all masks.

At the schematic first-Poisson scales for D=Y^(9/10), the column length remains D while the dual row norm is `H≈D²/Y=Y^(4/5)`. The target primal Y-bound would require a corresponding signed dual correlation of size `≲D`, after retaining its physical prefactor Y/D, nonfactorized Fourier kernel, gcd/divisor expansions and diagonal cancellation. No result in the cited sixfold-Eisenstein or rStation estimates has been identified that supplies that exact estimate. The cubic Gauss-square/sixfold identity is an exact arithmetic match and a potential method, not an upper bound or an assertion that the metaplectic residual spectrum has been removed.

Equation (9) also places the missing coefficient one angular step from a printed structured theorem. The coefficient `α⁻¹γ₁` is, up to the fixed ray factor χ_n(−1), the complex conjugate of `αγ₋₁`. Paper 5 (1.6) rewrites `αγ₋₁` as `μγ₂` times a fixed ray factor. Thus, after conjugation and finite-ray decomposition, the missing cubic-twist polynomial has the `D_j=μα^jγ₂` form with **j=0**, whereas Theorem 1 states its bound for j=±2. Extending the coefficient theorem to j=0 would require a proof; it is not a parameter choice permitted by the printed theorem. Even if the same displayed upper bound `N+B³/N+N^(2/3)B^(1/2)` were established at j=0, its B³/N term is Y^(19/10) at `N=Y^(4/5), B=Y^(9/10)`, still much larger than the desired dual Y^(9/10) size. A meaningful improvement would need additional use of the signed kernel or stronger scale-specific arithmetic, not merely the same long-range upper bound.
