# The signed dual correlation behind the 61/72 long-inverse target

**Status:** An exact source-qualified reduction to a signed arithmetic sum; the required bound is not proved here. The source Poisson formula, ray-class reciprocity, primitive conductor and root-number identities are de Faveri [§§2–3 and Proposition 8.1](https://arxiv.org/abs/2610.04045v1), with the sextic source normalization as in the tracker. This is not an individual zero-free result.

Let K be the Eisenstein field, S the fixed good set and c its fixed reciprocity modulus. Fix one column ray class C. Let W be a fixed smooth annular column profile, V a fixed nonnegative smooth row profile, and set

    P=Y^(6/5),
    a_q=P^(−1/2) μ_K(q) W(Nq/P)

on good squarefree q in C. Allow a fixed ray twist or norm-twist phase in W; these are common coefficients. Define the fixed-sector all-row energy

    E_C(Y)=Σ_{u good} V(Nu/Y) |Σ_{q good sf, [q]=C} a_q χ_q(u)|².

The source characters keep their zero masks. The desired 61/72-type estimate for this sector is `E_C(Y)≪Y^(1+ε)` uniformly in the stated profiles and heights. Splitting finitely many sectors by Cauchy–Schwarz makes such bounds sufficient for the unsplit inverse; a bound for the unsplit sum alone need not imply the separate sector bounds.

## Exact gcd and Poisson expansion

Expand the square and write `q₁=d r₁`, `q₂=d r₂`, with d,r₁,r₂ squarefree and pairwise coprime except that r₁,r₂ are only required mutually coprime and coprime to d. The two original q columns share C, so r₁,r₂ have the same class `C[d]^(−1)`. The common d character is the mask `1_((u,d)=1)`. Let ξ_(r₁,r₂) be the primitive Hecke character inducing `χ_(r₁) overline(χ_(r₂))`. For r₁≠r₂ the source's same-ray conductor lemma gives

    f(ξ)=r₁r₂,     ξ nonprincipal.                              (1)

The equal-column case has r₁=r₂=1 and contributes a nonnegative diagonal `D_C(Y)≪Y∑_q|a_q|²≪Y`. Here and below all sums are finite after the column cutoffs and all fixed S-modulus factors are retained. For r₁≠r₂, remove the original `(u,c d)=1` mask by

    1_((u,cd)=1)=Σ_{k|cd, k|u} μ_K(k).

The same Hecke functional-equation Poisson formula used in de Faveri Lemma 3.1 then gives

    E_C(Y)=D_C(Y)+B_C(Y),                                     (2)

where, with `f=r₁r₂` and ζ_ξ its unit root number,

    B_C(Y)= (Y/P) Σ_d Σ_{r₁≠r₂}
      μ(dr₁)μ(dr₂) W(Ndr₁/P) overline(W(Ndr₂/P))
      · Σ_{k|cd} [μ(k) ξ(k)/(Nk sqrt(Nf))] ζ_ξ
      · Σ_{v≠0} overline(ξ(v)) Ṽ( Nv Y/(Nf Nk) ).            (3)

The r-sums carry the squarefree, mutual-coprimality and ray-class conditions described above. In fact `(k,f)=1` follows from k|cd, the good-column condition and `(d,r₁r₂)=1`; retaining ξ(k) also covers the zero convention in any enlarged sum. The nonzero dual ideal v is essential because ξ is nonprincipal. Ṽ is **exactly** the rapidly decaying transform in de Faveri (3.1), including its fixed field and discriminant normalization; changes of complex-conjugation convention replace ξ by its conjugate throughout but do not affect the equality. No row-dependent zero mask is deleted before its divisor expansion.

Equation (3) is a **signed complex sum**; B_C itself is real because the (r₁,r₂) and (r₂,r₁) terms are conjugate. Since `E_C≥0` and `0≤D_C≪Y`, the fixed-sector all-row target `E_C≪Y^(1+ε)` is equivalent, up to the same small losses, to the concrete signed estimate

    |B_C(Y)| ≪ Y^(1+ε).                                       (4)

The inequality `B_C≥−D_C` is what makes an absolute bound equivalent here; bounding absolute values term by term is not justified.

## Scale and root-number structure

On a dyadic portion with `Nd≈D₀` and `Nk≈K₀`, both residual columns have norm `≈P/D₀`, and the nonnegligible dual scale is

    Nv ≲ Y^ε P² K₀/(Y D₀²)
       = Y^{7/5+ε} K₀/D₀².                                   (5)

This is the source Poisson tail cutoff, not an assertion of a sharp dual cutoff. For squarefree r₁,r₂ the source's general root-number lemma splits

    ζ_ξ = η_{C[d]^(−1)} β(r₁) overline(β(r₂)),                  (6)

where η depends only on the residual ray class `C[d]^(−1)` and β is the source's one-column root-number phase. The d-class can be fixed in finitely many sectors. Thus (3) is a bilinear correlation in the two residual columns, coupled by the *same* dual ideal v and divisor k. Its coefficients include `μ(dr₁)μ(dr₂)`, the two root-number phases, reciprocity, and the original coprimality restrictions. In a sextic normalization where β is explicitly identified with the normalized γ₁ Gauss phase up to fixed ray factors, source (4.7) replaces the Möbius/Gauss product by a cubic-Gauss coefficient. That final calibration must be checked for the exact β convention before labeling every term in (3) as a specific γ₂ coefficient; (3) and (4) themselves do not require that extra identification.

At P=Y^(6/5), the unrestricted-row sixth-order L₂ bound obtained from de Faveri's general sieve gives `E_C≪Y^(41/30+ε)` for an arbitrary unit-mass column vector. Thus (4) asks for a saving of `Y^(11/30)` beyond that general estimate for this specific signed Möbius vector. The source's structured-prime moment concerns a different coefficient class and row/column scale; the marked-moment/prime-slot bounds likewise do not state (4) for the coupled d,r₁,r₂,k,v sum.

The source-qualified [moving Gauss-profile projection](../2026-10-29-gauss-profile-low-rank/moving-twist-overlap.md) gives `||T Π_H a||²≪Y^(29/30+ε)` for its explicit low-conductor profile space at `H=P^(1/3−δ)`, for any fixed δ>0, with the stated profile and height qualifications. It does **not** identify that finite profile space with the full theta component of (3), nor does it bound the cross term or `T(1−Π_H)a`. The exact identity is

    E_C=||TΠ_H a||² + ||T(1−Π_H)a||²
          +2 Re⟨TΠ_H a,T(1−Π_H)a⟩.

Consequently (4), or an independent complement/joint-correlation bound strong enough to imply it, remains the concrete missing analytic lemma. No full-space cancellation, moving-row mask uniformity or selected-row gain follows solely from the known finite-profile overlap.

**Independent review:** Families checked the gcd splitting, same-ray primitive conductor, original masks, Poisson normalization, residual-class root phase, dual scale and 41/30-to-1 gap against the source. The β-to-γ₁ calibration and the signed bound (4) remain open.

## Test against the available Gauss estimates

The present source estimates do not by themselves prove (4). One concrete range mismatch already appears in the d=k=1 dyad. Its dual norm may reach `Nv≲Y^(7/5+ε)`, whereas each residual column has length `P=Y^(6/5)`. Even after the β-to-γ₁ normalization is established, treating a dual v as a moving Kummer twist h leads to the independently checked overlap bound

    |⟨m_P,v_(P,h)⟩| ≪ P^(−1/2+ε) [N rad(h)]^(1/2+ε).

For squarefree h of norm ≍Y^(7/5), this is only `Y^(1/10+ε)`, worse than the trivial O(1) Cauchy bound; it becomes power-saving only for radical `o(P)` on a fixed-power scale. The conditioned profile span extends to radical `≤P^(128/359−δ)` using Wu's subconvex bound; the projected source energy is below `Y` for `H=P^(25/72−δ)`. These observations do not show that the high-dual portion is large; they show that the available one-column moving-profile estimate does not bound it nontrivially at the edge of the permitted Poisson range.

The [first-moment cubic-Gauss draft](https://github.com/openai/math/blob/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf), Proposition 3.1, treats Type-I sums with total product scale X₀, an outer variable of length `R≪X₀^0.51` carrying arbitrary divisor-bounded coefficients, and a smooth **unrestricted** inner variable. Its Proposition 5.1 treats a Type-II range with shorter length between `X₀^0.32` and `X₀^1/2`; for lengths above `X₀^0.40` its coefficients must have the specified bounded prime-convolution form, and the strongest comparison also requires the stated roughness and Siegel–Walfisz conditions. In (3), after freezing the other variables, the column coefficient contains a moving character depending on the same dual v and k, as well as the signed Möbius and gcd masks; simply splitting r₂ into factors does not produce the source's unrestricted inner variable or establish its roughness/Siegel–Walfisz hypotheses. The two columns are also coupled through the common v,k and root-number phases. Thus neither cited Type-I nor Type-II statement can be inserted directly as a uniform bound for the entire sum (3). A detailed decomposition proving all their hypotheses, or a new joint signed estimate, is an additional task; no claim of impossibility is made.

## A rigorously controlled high-gcd regime

The ordinary source recursion already controls a genuine portion of (3), although it does not use the Möbius signs. Write `Nd≈Y^d`, `Nk≈Y^k` for a localized nonempty dyad; fixed S factors and losses are suppressed. Equation (9.8) of the [OpenAI September 30 draft](https://wcook04.github.io/plectis-atlas/papers/The-Quasi-Riemann-Hypothesis-September-30-2026.html), followed by the de Faveri unrestricted-row sixth-order L₂ bound, gives an upper bound by the following five monomials (including the row-diagonal term):

    Y^(1−k),   Y^(6/5−d),   Y^(37/30−d/3−5k/6),
    Y^(41/30−d−k/6),        Y^(19/15−d/2−2k/3).            (7)

For reproducibility, the dual row scale is `H=P² Nk/(Y(Nd)²)=Y^(7/5+k−2d)` and the remaining column scale is `P/Nd=Y^(6/5−d)`. The source prefactor is `Y Nd/(P Nk)=Y^(−1/5+d−k)`. Inserting the four terms

    H,  H^(1/6)(P/Nd),  H^(5/6)(P/Nd)^(1/3),
    H^(1/3)(P/Nd)^(5/6)

produces the last four powers in (7). The fixed-class, divisor, masks and coefficient mass are handled in the source recursion; O(log²Y) localizations cost only small powers.

Consequently each localized block is `≪Y^(1+ε)` whenever

    d≥1/5,  2d+5k≥7/5,  d+k/6≥11/30,  3d+4k≥8/5.          (8)

In particular **all** gcd ranges `Nd≥Y^(7/10)` are controlled, since k≥0; the short/empty dual ranges are discarded exactly as in the source. This is a real source-qualified partial bound for the signed dual expansion, not merely a formal rearrangement. It does not establish cancellation of the dominant small-gcd range d<7/10, and it holds even for arbitrary unit-mass column coefficients, so it is not a Möbius-specific gain. The relevant source recursion and general L₂ inputs remain imported rather than independently proved.

### Exact controlled polytope and a gcd sparsity check

Ignoring arbitrarily small fixed-power losses and fixed S constants, the source dyads satisfy

    0≤d≤6/5,  0≤k≤d,  2d−7/5≤k,

where the last condition is the nonempty dual-scale condition `H=Y^(7/5+k−2d)≥1`. Within that admissible region, the four inequalities in (8) are equivalent to the following complete generic-sieve controlled set:

    11/35≤d≤12/35:   k≥11/5−6d;
    12/35≤d≤7/10:    k≥7/25−(2/5)d;
    7/10≤d≤6/5:      every admissible k.                      (9)

At d=12/35 all three nontrivial lower lines meet; d=11/35 is where `11/5−6d` first meets k=d. The condition `k≥2d−7/5` remains in force throughout. Thus for d<11/35 there is no nonempty dyad in which these generic monomial inequalities prove a Y-sized bound. In the particularly important k=0 slice the source bound exponent is

    41/30−d          for 0≤d≤1/5,
    37/30−d/3        for 1/5≤d≤7/10,
    1                for d≥7/10.                              (10)

At d=k=0 the dual scale reaches Y^(7/5) and the exponent is 41/30. These are bounds for the localized absolute values produced by the source recursion, not lower bounds or statements that the corresponding arithmetic sums attain them.

There is also a direct gcd-counting bound, independent of the source recursion. For `Nd≈D₀`, there are `≪Y^ε D₀(P/D₀)²` admissible ordered column pairs. The smooth row correlation is at most Y trivially, and at most `(P/D₀)Y^ε` by the fixed-field Hecke functional equation for its nonprincipal conductor `Nr₁Nr₂≈(P/D₀)²`, including deleted factors. The two column normalizations contribute P^−1. Therefore

    |B_[d≈D₀]| ≪ Y^ε (P/D₀) min{Y,P/D₀}.                    (11)

This independently reaches O(Y^(1+ε)) for `D₀≥P/sqrt(Y)=Y^(7/10)`, but is weaker than the source bound in the intermediate range. Moreover, for squarefree columns `(d,r₁r₂)=1` gives `μ(dr₁)μ(dr₂)=μ(r₁)μ(r₂)`: the common gcd d carries **no Möbius sign** after opening the square. Thus simple cancellation in d is unavailable; a Möbius-specific improvement must use the residual pair, the k-divisor sum, their coupling to v, or another actual source structure.

**A positive-dual-family obstruction:** The independently reviewed, source-conditional [theta-family diagonal calculation](../2026-10-29-sextic-dual-diagonal-obstruction.md) gives mean `≫ℋ` for the complete unmarked angular Gauss family when `ℋ=D^(7/6)`. Therefore the schematic extension that bounds that entire positive family by `D^(1+ε)` cannot hold. This does not bound or preclude the signed correlation (3): its gcd, divisors, masks, smoothing and common dual variable are coupled, and the October 5 manuscript itself uses the different regime `ℋ<D`.
