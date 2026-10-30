# Möbius-specific sextic and metaplectic estimates at long columns

The requested target is the all-natural-row bound

    Σ_{0<Nu≤U} |D^(−1/2) Σ_n μ_K(n)χ_n(u)W(Nn/D)|² ≪ U^(1+ε)

at D=U^(6/5), with original nonunit zeros and fixed good-prime data. No source located in this search establishes it. The [power-row identity](2026-10-29-sextic-inverse-target/README.md) explains why it is a difficult target: the bound would force ζ_K(s) nonzero for Re s>61/72. This is an implication, not a lower bound contradicting the target.

## Closest coefficient-specific inputs

1. The OpenAI [October 5 quasi-Riemann manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex), Step 3–5 and Proposition 2, uses the actual Möbius coefficient: after sextic Poisson and Gauss–Jacobi identities, the dual coefficient becomes a cubic theta coefficient. Its stated main family mean has U=D^(1+ϑ)>D. Its schematic dual scale is ℋ=D²/U and the normalized dual mean target is D. The completed-theta estimate is ℋ+ℋ²/D; the displayed cube cutoff requires ℋ≤D. At D=U^(6/5), ℋ=D^(7/6)>D and the printed cutoff is D^(−1/9)<1. The displayed completed estimate is D^(4/3), so the existing proof does not transfer directly. This is a limitation of a sufficient bound, not a lower bound for the true mean.

2. [rStation paper 5 v3](https://rstation.ai/problems/riemann_hypothesis/papers/5), Theorem 5, claims for fixed nonzero integer ℓ the all-row mean

       Σ_{0<Nz≤K} |Σ_{n squarefree} α(n)^ℓ γ₂(n)ν(n)χ_n(z)W(Nn/D)/√Nn|²
          ≪ K(KD)^ε,

for all K,D≥1, in its fixed-ray setup. It imports the October 5/September 30 theta-reflection and inverse-moment framework and has not been independently verified here. This is strong but it is a Gauss-weighted coefficient, not the original μ polynomial. The paper explicitly excludes ℓ=0 and states that the zero theta mode and its residues remain outside the sextic theorem. Its equation (10.2) gives the ordinary Möbius inverse bound K+K^(1/6)D^(5/6), exactly the present source-qualified benchmark.

   The comparison is nevertheless informative: Oct. 5 Step 3 writes its simplified dual B_h(D)/√D with coefficient α(n)^(−1)γ₂(n) times a fixed ray twist, apparently matching paper 5's ℓ=−1 family. Even if the relevant sector, gcd and smoothing transfer is granted, the theorem supplies a normalized dual bound ℋ, while the simplified target is D. At D=U^(6/5) the loss is ℋ/D=D^(1/6). Inserting this only into the schematic Poisson comparison gives normalized original size U+D=U^(6/5), worse than the baseline U^(7/6). This is an exponent and scope calculation, not a proof that the paper 5 theorem applies to every suppressed component.

3. [rStation paper 62 v1](https://rstation.ai/problems/riemann_hypothesis/papers/62/v1), Theorem 1, claims a natural-row mean for the **cubic** Gauss-weighted coefficient μ(n)G(n), with diagonal A·D_{Y,w,E} and error O((AY)^(2/3) exp(−c√log Y)) in Y^(1−θ)≤A≤Y². It allows fixed common deletions and specified bounded modifications at small primes. Its source is a near-equal cubic inverse estimate with a fixed saving, and its conclusion includes only a subpower saving over the mixed error scale; it does not state an all-row sextic μ estimate or a fixed-power gain at our target. Its own abstract excludes the shorter physical rows. It is a non-peer-reviewed, source-dependent manuscript, and the result is not independently verified here.

4. Dunn–Radziwiłł, [*Bias in cubic Gauss sums*](https://arxiv.org/abs/2109.07463v3), Propositions 9.1–9.2, subtract cubic polar terms in a structured dispersion estimate under roughness and character-cancellation restrictions, with GRH in that argument. The statements do not supply a uniform full-row sextic inverse estimate with the actual μ coefficients.

5. [rStation paper 10](https://rstation.ai/problems/riemann_hypothesis/papers/10), Theorem 1 and §8, treats a contour remainder for actual adjoint Gauss images and, under an additional Gram hypothesis, an approximation to a specified growing theta-mode correction. It expressly leaves the complementary operator acting on the Möbius/plain vector uncontrolled. The presence of many large twisted modes is consistent with the independently reviewed [source-qualified growing-rank calculation](2026-10-29-gauss-growing-rank/README.md).

## Concrete missing ingredient

The independently reviewed, source-conditional [diagonal calculation](2026-10-29-sextic-dual-diagonal-obstruction.md) now rules out a normalized `≪D` bound for the **complete positive unmarked dual family** at `ℋ=D^(7/6)`: its mean is `cℋ+o(ℋ)` by paper 5's stated off-diagonal estimate. Therefore a positive term-by-term bound at the schematic Oct. 5 dual stage cannot prove this long-inverse target.

A possible route is a joint **signed** estimate retaining the physical correlation between the two primal columns, gcd and dual variable, as in the [61/72 signed-correlation note](2026-10-29-61-72-dual-correlation/README.md). Another is a direct primal improvement of the source amplification bound. Either route must retain sixth-power rows: deleting them would remove the mechanism by which the proposed all-row estimate detects base-field zeros. The diagonal obstruction does not rule out either route and no new zero-free region follows from the sources or comparisons above.
