# Prior work on the quadratic full-inverse moment criterion

**Scope:** Targeted source search, not a priority determination or an independent verification of every estimate in the [quadratic growth note](2026-10-29-riemann-quadratic-inverse-growth/README.md). The familiar Mellin-to-zero-free and family second-moment ingredients have substantial prior literature; the exact single-test, full-Dedekind-inverse growth identity may already be implicit elsewhere.

## Quadratic-family Möbius moments

Peng Gao and Liangyi Zhao, [*Mean squares of quadratic twists of the Möbius function*](https://doi.org/10.1016/j.jnt.2022.12.007), Journal of Number Theory 247 (2023), 1–14, study moments of `Σ_n μ(n)χ_(8d)(n)`, the coefficient sum for an **individual reciprocal quadratic Dirichlet L-function**. For smooth compactly supported profiles in d and n, their Theorem 1.1, as reproduced in [Yuichiro Toma's 2024 preprint, §1](https://arxiv.org/html/2405.18778), assumes GRH and gives a main term of order XY with error `O(X^(1/2+ε)Y^(3/2+ε))+O(XY^(1/2+ε))` in the range `Y≪X^(1−ε)`.

Toma, [*On the moments of averages of quadratic twists of the Möbius function*](https://arxiv.org/abs/2405.18778v1), Theorem 1.2, proves an unconditional sharp-cutoff asymptotic of size `CXY` for that same one-factor χ_(8d) family when `Y≪X^(1/3−ε)`. Its explicit error is `O(XY^(7/12))+O(X^(1/2+ε)Y^(2+ε))+O(X^(1/2)Y^(5/2)(log Y)^2)`. Theorem 1.3 considers higher moments. These are close prior results on short inverse sums in families and should be cited. They do not assert the growth identity in the companion note: the family is χ_(8d) with odd squarefree d, and the inner coefficients are μ(n)χ_(8d)(n), without the additional ζ(s)^−1 factor present in a quadratic field's full Dedekind inverse. Adding that common factor changes the coefficients to a convolution and introduces the base-zeta zero obstruction.

## Classical Mertens and RH comparisons

The equivalence `RH ⇔ M(x)≪_ε x^(1/2+ε)` is classical and explicitly recalled by Gao–Zhao and Toma. The Mellin pole/Ω argument and reciprocal-zeta contour shift in the proposed criterion are instances of that longstanding mechanism, not novel methods.

There is also established **mean-square** literature, but its averaging variable differs. The weak Mertens conjecture asks `∫_1^X (M(x)/x)^2 dx≪log X`; it implies RH and simple ζ zeros, as recorded for example in [Bui, *Negative discrete moments of the derivative of the Riemann zeta-function*](https://doi.org/10.1112/blms.13092), citing Titchmarsh, Chapter 14. Nathan Ng, [*The distribution of the summatory function of the Möbius function*](https://arxiv.org/abs/math/0310381), proves a strong form of weak Mertens under RH and an additional Gonek–Hejhal reciprocal-derivative moment hypothesis. This is not the same as the companion's all-ε, family average over real quadratic discriminants, and the sharp `log X` formulation should not be equated with RH alone.

For ideal Möbius functions of fixed number fields, Hu, Kaneko, Martin and Schildkraut, [*On a Mertens-type conjecture for number fields*](https://arxiv.org/abs/2109.06665), Propositions 2.6–2.8 and Theorem 2.10, analyze zeros and Ω-results for the individual field's Mertens function. Their source also discusses the special base field Q(√−3), but not the proposed average of full inverses over real quadratic fields.

The [OpenAI October 5 manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex) §3 explicitly derives a fixed-Hecke-zero-free implication from bounds for smoothed twisted Möbius sums by choosing a test with nonzero Mellin transform at a putative zero. It is a source for the analytic reduction, not an independent verification of that manuscript's deeper analytic claims, and not a statement of the quadratic full-inverse moment equivalence.

## Candidate criterion and caveats

The companion proposes a single smooth compact-annular W with Mellin transform nonzero on Re s>0 and a fixed nonnegative discriminant weight V. For squarefree d>0, d≡1 mod 4, it uses the odd-prime-deleted inverse of `ζ(s)L(s,χ_d)`, not merely `1/L(s,χ_d)`. Its stated limsup identity ties the logarithmic growth exponent of a normalized second moment to the abscissa Θ_ζ of ζ zeros and, if correct, yields a two-way RH criterion for one short exponent r and this fixed W. It is an equivalence to RH, not a proof of RH, and its exact allowable range must follow the version and estimates in the companion.

Searches for quadratic-field reciprocal Dedekind-zeta moments, family Mertens functions, and short Möbius-twist moments located the above nearby sources, but no direct matching theorem in the sources inspected. This is insufficient to establish novelty. In particular, none of the comparisons substitutes an isolated inverse L-factor for the full quadratic Dedekind inverse or silently replaces the stated fixed-field family by χ_(8d).
