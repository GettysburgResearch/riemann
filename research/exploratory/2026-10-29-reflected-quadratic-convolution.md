# Reflected theta times the quadratic Möbius prefix

**Status.** Source-qualified investigation of a constructive route; no mixed estimate or individual zero-free theorem is proved. The reflection, local tables, masks and fixed-sector/profile uniformity are imported from the cited October 5 source, not independently re-established here.

At the earlier active dual dyad, put

    B=Y^(10283/11000), H=Y^(579/5500), Z=Y^(4093/5500).

The object to bound is a mixed second moment over the *same* good sixth-free b rows of the quadratic Möbius prefix `A_b(H)` and the completed theta `T_b(Z)`; see [the mixed-moment search](2026-10-29-quadratic-theta-mixed-prior-art.md).

## A constructive reflection route

The [OpenAI October 5 source, §6, equations (residual-quadratic-factor) and (theta-separated-columns)](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex) reflects the **completed** theta sum. After fixing a finite ray/cusp sector, its active moving squarefree row contributes a quadratic factor. More explicitly, a transformed constituent has a sum over squarefree n and cube index q whose common coefficient is

    A_{u,m}(n,q) / [sqrt(Nn) Nq],

with `|A_{u,m}(n,q)|≤27` in the source normalization, finite fixed local factors and a smooth cutoff at effective `Nn (Nq)^3≲B²/Z`. The row-dependence is a bounded sector scalar, a quadratic `χ_b(nq)^3`, and a norm-weight that requires source-uniform Fourier/Mellin separation. The paper then applies a quadratic sieve after fixing q and separating the norm profile. Relevant bad primes, original zero masks, finitely many cusps and local active-prime reindexings remain part of that process.

Now insert the prefix. Its row character is also quadratic, so

    χ_b(c)^3 χ_b(nq)^3 = χ_b(cnq)^3

including zeros. Thus, **after** a valid common-profile separation, both pieces can be combined into a single quadratic column indexed by cnq. This is a concrete way to avoid treating the shared b-dependence as an arbitrary coefficient. It does not itself show cancellation: the resulting coefficient is a convolution of the actual `μ(c) ᾱ(c)^3 ξ(c)^3` prefix with the actual reflected cusp coefficient and the q-weights.

For a scale check only, suppose that after squarepart extraction and the source's finite-index summations the combined column has effective length `L H`, with `L=B²/Z`, and squared coefficient mass `≪H Y^ε`. Applying only the quadratic large sieve would lead schematically to

    H (B+LH) = H B + H² B²/Z.                                  (1)

At the displayed dyad, the two exponent faces of (1) are `11441/11000≈1.040091` and `167/125=1.336`. The existing A8/A10 plus source-theta Hölder comparison has exponent `28373/22000≈1.289682`, so (1) would need an extra saving of `1019/22000≈0.0463182` in its dominant face. This is an **optimistic scale comparison**, not a source theorem for the full mixed product: deriving its common coefficient, dealing with gcd/extracted square masks, bounding cusp coefficients, and retaining all finite profile and local factors remain necessary. In particular (1) does not prove a new bound and its comparison does not rule out a structured improvement.

## Why an ordinary Euler product is not immediate

The *original*, unreflected squarefree cubic-theta coefficient `a_ξ(n)=ᾱ(n) γ₂(n) ξ(n)` has source identity (crt-a)

    a_ξ(pq)=a_ξ(p) a_ξ(q) χ_q(p)^4

for coprime good primes, with the fixed source conventions. Let `u(c)=ᾱ(c)^3 ξ(c)^3`, and formally convolve `f=(μu)*a_ξ` on squarefree ideals. Then

    f(pq)−f(p)f(q)
       =a_ξ(p)a_ξ(q)[χ_q(p)^4−1].                              (2)

For suitable good primes the cubic residue factor is nontrivial and the Gauss coefficients are nonzero. Hence the actual coefficient is not an ordinary multiplicative Euler-product coefficient, even before truncation, smoothing and the q³ completion. This calculation is for the original cusp/squarefree subpiece, **not** an assertion that every reflected cusp coefficient has exactly the same formula. A metaplectic or twisted multiple Dirichlet series may still encode (2); that possibility requires its own analysis.

At the actual norm scales the prefix cut at H and the reflected smooth profile also prevent replacing the finite convolution by the value of a global reciprocal L-function. No source found in the targeted search bounds this μ–reflected-cusp convolution with the saving required above. The result does not exclude nontrivial cancellation: possible directions are a twisted Rankin–Selberg or metaplectic spectral estimate with moving quadratic conductors, or control of the norm-synchronised cross-correlations before absolute values, while retaining the original q,c square and deletion masks.
