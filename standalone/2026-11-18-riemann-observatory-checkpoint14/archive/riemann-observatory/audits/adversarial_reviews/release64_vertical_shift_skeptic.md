# Independent check of the degree-one central-zero example

18 November 2026. Under its printed Selberg-class axioms, Nakamura–Suzuki arXiv:2307.02027v1 admits a degree-one function with a central zero. The example is a vertical translate of the primitive odd Dirichlet beta function by an actual critical-zero ordinate. The original degree-one classification explicitly includes this shift. The check concerns §3's degree and central-zero discussion. The central drift normalization has its own versioned audit. [Nakamura–Suzuki v1, §3 p. 5](https://arxiv.org/pdf/2307.02027v1#page=5) · [Version and drift audit](release64_central_extension_versions.md)

## The exact ordinate

Let χ₄ be the primitive character modulo 4, with values 0 on even integers, 1 at 1 mod 4 and −1 at 3 mod 4. The completed beta function

```text
Λ_χ(s) = (4/π)^((s+1)/2) Γ((s+1)/2) L(s,χ₄)
```

is real at s=1/2+it. The primitive functional equation has sign +1, since the Gauss sum is 2i and i√4=2i. Conjugation with real character coefficients then gives realness along this line.

I reran the archived 192-bit python-flint certificate. Its Hurwitz-zeta expression for beta gives a positive completed value approximately 3.4754220235×10⁻¹³ at the exact rational height 6.02094890469 and a negative value approximately −5.6744526729×10⁻¹³ at 6.02094890471. The interval radii were below 4×10⁻⁵⁸ and both signs were strict. Continuity gives an actual ordinate τ inside this interval with L(1/2+iτ,χ₄)=0. No simplicity or global zero-location premise is needed. The translated function uses this actual τ. [Archived implementation](../../scripts/chi4_phase_certificate_skeptic62.py) · [Original interval proof](../chi4_effective_phase_lower_skeptic62.md) · [Director replay](director_finite_lower_round8.md)

## All five printed axioms

Put F_τ(s)=L(s+iτ,χ₄) and Q=√(4/π). Up to its positive constant, the unshifted completion is X(s)=Q^s Γ((s+1)/2) L(s,χ₄), with X(s)=overline(X(1−bar s)).

1. **(S1)** Its Dirichlet coefficients are a_τ(n)=χ₄(n)n^(−iτ). Their absolute values are at most 1, giving absolute convergence for Re s>1.
2. **(S2)** The standard primitive nonprincipal Dirichlet L-function is entire of finite order. Translation preserves that property, so the minimum pole-clearing exponent is m_F=0. A nonzero translation of ζ would move its pole off s=1.
3. **(S3)** Use r=1, λ₁=1/2, μ₁=1/2+iτ/2 and the same positive Q. Then Re μ₁=1/2 and

   ```text
   ξ_(F_τ)(s) = Q^s Γ((s+1+iτ)/2) F_τ(s)
              = Q^(−iτ) X(s+iτ)
              = Q^(−2iτ) overline(ξ_(F_τ)(1−bar s)).
   ```

   The root number has modulus 1. With original unit root number ωχ, the translated root is ωχ Q^(−2iτ). The printed condition allows complex μ₁ and any unit root number. The degree is 2λ₁=1.
4. **(S4)** The estimate |a_τ(n)|≤1 gives every ε bound.
5. **(S5)** In the absolute half-plane the Euler logarithm uses b_τ(p^k)=χ₄(p)^k p^(−ikτ)/k and zero at all other positive integers, including b_τ(1)=0. Thus |b_τ(p^k)|≤1/k≤1, admissible with θ=0.

At the exact center F_τ(1/2)=0, while its gamma and Q factors are finite and nonzero. The central completion multiplicity is at least one. The translation preserves the real parts of every zero, so GRH for F_τ is equivalent to GRH for the original beta function. Under that common hypothesis, the corrected Gaussian covariance is the multiplicity of the original L-function at height τ. The unshifted β(1/2) is strictly positive by its decreasing alternating series, whose first two terms give 1−1/√3>0. The change from zero to positive central multiplicity is unconditional. [Printed axioms, pp. 2–3](https://arxiv.org/pdf/2307.02027v1#page=2)

## Classification and the meaning of normalization

Kaczorowski–Perelli, *On the structure of the Selberg class, I: 0≤d≤1*, Acta Math. 182 (1999), pp. 207–241, Theorem 3 on p. 211, gives ζ in the q=1 case and L(s+iθ,χ) for a primitive character in the q≥2 case. Perelli's survey Part II, which Nakamura–Suzuki cite as [7], gives the same shifted classification in its Theorem 6.3 on p. 94. Part II p. 107 explicitly distinguishes primitive functions from primitive-and-normalized functions, defining the latter by the vanishing of their shift invariants in that discussion. Nakamura–Suzuki §2.2 lists S1–S5 without a zero-shift condition. The argument satisfies all of those printed axioms. Imposing primitivity alone would not remove it either. For the ordinary Selberg class, degree is additive, the degree-zero part is the unit, and there are no functions with degree strictly between zero and one. A degree-one member therefore cannot split into two nonunit members. [Original classification, Theorem 3](https://doi.org/10.1007/BF02392574) · [Survey Part II, pp. 94 and 107](https://www.rivmat.unipr.it/fulltext/2004-3s/pdf/04.pdf)

For τ≠0, the translated Dirichlet series is distinct from any unshifted Dirichlet L-function. Uniqueness of absolutely convergent Dirichlet series would make its nonzero coefficients at 3 and 5 values of one Dirichlet character. Both would be roots of unity. Dividing out the original signs shows that exp(−iτ log 3) and exp(−iτ log 5) would be roots of unity as well. This would make the ratio of the two nonzero rational rotation numbers log 3/log 5 rational, contradicting unique factorization. The coefficients at even n also exclude ζ.

The example contradicts the lower-degree exclusion if read for all members of the paper's printed class. The conjectural nonvanishing question for the unshifted Dirichlet central values is a different statement. Restricting that sentence to appropriately normalized unshifted members would avoid this witness. The paper's separate weight-18 example still supplies a central zero under that narrower convention. No journal manifestation was available in the version audit. [Source §3](https://arxiv.org/pdf/2307.02027v1#page=5)

## Evidence pins and access

- The six-page arXiv v1 PDF SHA-256 is `d833f2af1f426c36f72cfb43df6b67bb3b3bf50ac9324c5069bc7442768a72d9`.
- The inspectable Parma PDF of Perelli Part II, 36 pages, SHA-256 `bcb884c906faa4a271116db5c9e67171e2d1f95a9c84dca2f8e3f66ad2589b8b`.
- The Acta paper publisher-page scan retrieved from the Tsinghua mirror, SHA-256 `4e33441a8ef5a7c6d8263e72deb75ea2551854ab6e0dd1ffbaa1e716c0ff38ea`. The printed classification is on p. 211.
- Perelli Part I, source [8], was identified via the Springer record. The tried publisher and mirror PDF routes did not yield its article text. The cited Part II and the original classification were directly accessible. [Part I publisher record](https://link.springer.com/article/10.1007/s00032-005-0037-x)
- The actual rerun used python-flint 0.9.0 at 192 bits and script SHA-256 `19404c978676f6e2cab399a9a57bdc89bbd90aa1393bddb6798757f7404506d4`. The sign test uses the exact rational endpoints and the real completed function. [Replay code](../../scripts/chi4_phase_certificate_skeptic62.py)
