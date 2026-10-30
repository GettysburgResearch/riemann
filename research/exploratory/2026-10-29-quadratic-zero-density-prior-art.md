# Quadratic Dirichlet zero-density comparison

**Conclusion:** The proposed small-power-height exponent `R(σ)=(1−σ)(2σ+1)` is weaker, at every fixed `1/2<σ<1` and sufficiently small positive height exponent, than a 2023 theorem of Corrigan and Zhao for the larger family of **all** primitive quadratic Dirichlet characters of conductor at most X. This is a source comparison, not an independent audit of the proof of that theorem. It does not rule out a different improvement in the height aspect, a different family, or a stronger exponent.

Write `N(σ,T,χ)` for zeros of `L(s,χ)` with `Re s≥σ` and `|Im s|≤T`, counted with the convention of the cited source. Every positive fundamental discriminant d>1 gives a distinct primitive quadratic character χ_d of conductor d, so a bound for all such characters with conductor at most X directly majorizes a sum over positive fundamental d≤X. Discarding the single d=1 principal presentation makes no difference to this containment.

Chandler C. Corrigan and Liangyi Zhao, [*Zero-density theorems for families of Dirichlet L-functions*](https://arxiv.org/abs/2211.00260), Bulletin of the Australian Mathematical Society 108 (2023), 224–235, Theorem 1.4, state for `T≫1` and `1/2<σ<1` that

    Σ_(χ∈C₂(X)) N(σ,T,χ)
      ≪_ε (XT)^ε min{ (X³T⁴)^((1−σ)/(2−σ)),
                          (XT)^(3(1−σ)/σ) },                  (1)

where C₂(X) is the collection of primitive characters of exact order 2 and conductor at most X. At T=X^τ the first term has exponent

    H(σ,τ)=3(1−σ)/(2−σ) + 4τ(1−σ)/(2−σ).

The proposed exponent is `R(σ)=2(1−σ)(σ+1/2)`. Exact algebra gives

    R(σ)−H(σ,0)=(1−σ)²(2σ−1)/(2−σ)>0,

and hence `H(σ,τ)<R(σ)` whenever

    0<τ<(1−σ)(2σ−1)/4.                                     (2)

Allow room for the source's ε-loss; at any fixed σ, choose τ strictly below this threshold and ε sufficiently small. For example, at `σ=4/5` the source gives `X^(1/2)T^(2/3)(XT)^ε`, whereas the proposed X exponent is `13/25=0.52`; the source is stronger for any fixed `τ<3/100`. If the proposed assertion holds for some unspecified τ₀>0, monotonicity in T permits comparing at any smaller τ, so (2) is a genuine comparison of its small-power-height scope.

The paper defines N using set-counting notation and does not explicitly state a multiplicity convention. For comparing merely the number of characters with at least one zero this distinction is irrelevant. If the proposed sum counts zeros with multiplicity while the source is read as counting distinct zeros, the standard local zero count bounds any individual multiplicity by `O(log(X(T+2)))`, which can be absorbed into `(XT)^ε` at polynomial T. This conversion uses that standard auxiliary zero-count estimate.

The original [Heath-Brown, *A mean value estimate for real character sums*, Theorem 3](https://doi.org/10.4064/aa-72-3-235-275), gives the same X exponent and height exponent `(3−2σ)/(2−σ)`. Corrigan–Zhao explicitly attribute this earlier result and state that their first term improves its T-aspect. Jutila's earlier bound, reported in Corrigan–Zhao's proof and Corrigan's [2022 thesis](https://web.maths.unsw.edu.au/~ccorrigan/honoursthesis.pdf), is `(XT)^((7−6σ)/(6−4σ)+ε)`; at σ=4/5 its X exponent is 11/14, so it is a much weaker comparator at small height.

For σ sufficiently close to 1, C. C. Corrigan, [*A note on the zeros of L-functions associated to fixed-order Dirichlet characters*](https://arxiv.org/html/2310.16518), Bulletin of the Australian Mathematical Society 110 (2024), 252–261, Theorem 2.1, states for `X,T≥2` the additional bound

    (XT)^ε min{ (XT)^(8(1−σ)/3), (X⁸T⁵)^((1−σ)/(6σ−3)) }.

Its first term improves the Corrigan–Zhao X exponent for `σ>7/8`; e.g. at σ=9/10 it has X exponent 4/15, compared with candidate 7/25. Both sources include the positive fundamental-discriminant subfamily, and both cover a positive power height when τ is sufficiently small. Other results and refinements may exist; no claim is made that these are the strongest possible bounds in every parameter range.
