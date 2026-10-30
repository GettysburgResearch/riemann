# Common-probe closure for the first unitary stage

**Status:** A conditional implication; it is not a proved zero-free region. The assumptions include the remaining variable-geometry contour and tail gate. The continuation mechanism is Hu Lemma 8.1 with a different low exponent, and the final descent and unitary Brauer induction are Hu §§2 and 9. The analytic source preprints have not been fully audited here.

Fix K containing μ₁₂ and an infinity-type orbit as in Hu. Let 𝔽ω be Hu's family of finite-order twists, norm twists, and the three fixed types 0, ω∞, conjugate(ω∞). Let β be the supremum of the real parts of their nontrivial zeros. Assume Hu's claimed seven-eighths theorem for this family, so β≤7/8. Put

    B₀=69991/80000,   b=173/2000,   C_b(s)=s−(4+b)/6.

Assume that whenever β>B₀ one can choose a single finite slot system and a single ρ>0, independently of the later target in 𝔽ω, such that for each target ψ its same compensated probe Jψ and principal signal fψ satisfy, for every ε>0,

    Jψ(Z) ≪ψ,ε Z^(C_b(B₀)+ε),
    Jψ(Z)−fψ(Z) ≪ψ Z^(C_b(β)−ρ)                         (Z≥1),

where constants and thresholds may depend on ψ. Here

    fψ(Z) = (2πi)^(−1) ∫_(Re s=2)
              Z^C_b(s) exp((s−5/6)^2) Hψ^S(s)/L_K^S(s,ψ) ds,

with Hψ^S holomorphic and nonzero on Re s>B₀, after fixing the same finite excluded set S as in the physical probe. Assume also that the defining integral can be shifted arbitrarily far right, with sufficiently rapid decay as Z↓0. These are explicit hypotheses: in particular the high bound must include the same principal, moderate, small and distant physical rows and remove target-dependent height factors using a height exponent chosen only after the common ρ has been fixed.

Then β≤B₀. For if β>B₀, the two estimates give

    |fψ(Z)| ≪ψ,ε Z^(C_b(B₀)+ε)+Z^(C_b(β)−ρ).

For each fixed ψ, the Mellin transform ∫₀^∞ fψ(Z) Z^(−C_b(s)) dZ/Z is therefore holomorphic for Re s>max{B₀,β−ρ}; use an ε smaller than the distance from a compact set to B₀. The small-Z condition gives convergence at zero. On an absolute line Mellin inversion identifies this transform with exp((s−5/6)^2)Hψ^S(s)/L_K^S(s,ψ), and the identity theorem extends that equality. Its nonzero numerator rules out zeros of the denominator in the half-plane. A pole of the Hecke L-function instead makes its reciprocal vanish, so it is harmless. Because max{B₀,β−ρ}<β and ρ is common across the family, the definition of β gives a contradiction. □

If this implication is established for every K and fixed type orbit with the corresponding source inputs, Hu's abelian base-change argument descends the rank-one result to every number field. Hu's unitary Brauer induction and Frobenius reciprocity then transfer it to every finite-dimensional continuous unitary global Weil representation, with poles and orders prescribed by its norm-character constituents. Those last deductions are conditional here on the stated rank-one result and the cited classical induction inputs; they do not by themselves prove the needed probe estimates.

## Existing pieces and the outstanding gate

- The [variable low calculation](2026-10-28-hu-variable-low/README.md), [principal contour](2026-10-29-hu-principal-contour/README.md), and [moderate high contour](2026-10-29-unitary-high-contour/README.md) give reductions with their exact source assumptions. The latter has an independently checked rational endpoint certificate and a separate [audit](2026-10-29-unitary-high-contour/REVIEW.md).
- The [outer-row note](2026-10-29-unitary-outer-rows/README.md) derives the small- and distant-row powers and the relevant local-factor estimates from the displayed source table, subject to the explicit reciprocal and field-local inputs. An independent [review](2026-10-29-outer-rows-review.md) checks the accounting.
- The [dynamic-contour reconstruction](2026-10-29-unitary-dynamic-contour/README.md) and [first-region calculation](2026-10-29-unitary-first-euler-region/README.md) reduce the variable-scale contour to exact physical local identities, a fixed-type buffered detector, and the source's trace-tail and profile controls. They have separate internal reviews; the fixed-type detector is also isolated [here](2026-10-29-fixed-type-buffered-detector.md). These are conditional deductions from source assertions, not independent proofs of Hu's field-local Gauss table, common unit-sector calibration, theta reflection, or all moment/profile quantifiers.
- The two family-wide displays above must not be treated as established merely by substituting the new numbers into Hu's fixed-geometry theorem. In particular, one still needs an end-to-end source audit that every physical presentation, common mask and height order fits all of the separately reviewed estimates simultaneously.

Sources: [Hu, arXiv:2610.00216v1](https://hexagonmath.org/2610.00216v1), Lemmas 2.1 and 8.1 and §9; [Xu–Sang, arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291v2), §6 and Appendices C–E.
