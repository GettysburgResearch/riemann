# Local-exponent orthogonality for residue-character families

**Status.** This is a proposed fixed-field consequence of standard Kummer reciprocity, Hecke analytic continuation and the uniform subconvex theorem of Wu; the family-presentation and conductor hypotheses below are part of the statement and must be verified for each application. It does not give a new zero-free region. No priority claim is made.

Fix n≥2, a number field K containing μ_n, and a fixed finite bad-prime set S containing primes over n and supporting the finite ray/representative data. Let d range over squarefree good integral ideals in one specified fixed reciprocity sector, with a smooth weight W(Nd/X). Assume that the chosen n-th residue characters ρ_d form a genuine Hecke family on good ideals with the following standard presentation: every product of finitely many fixed-index values ρ_d(a)^b, as a function of d on the sector, is a fixed-sector Hecke character with zero extensions and conductor supported on S and the prime divisors of a; its local character at a good prime p has exact exponent b v_p(a) modulo n and full order n when b v_p(a)=1. This is automatic in the ordinary primary Eisenstein sextic convention, but a general number-field construction must explicitly provide its fixed ray/ideal representatives and unit phases. The implied conductor bounds below must be uniform in the varying indices.

Let p be a good prime, P=Np. For a mark exponent a and arbitrary inverse factors ρ_d(k_j)^{b_j}, set g=gcd(n,b_1,…,b_r). If

    g ∤ a,                                                   (1)

then for every choice of good k_j the local exponent at p of

    ρ_d(p)^a ∏_j ρ_d(k_j)^{b_j}

is nonzero modulo n: it is a+Σ_j b_j v_p(k_j), and condition (1) forbids its vanishing. Thus the corresponding Hecke character in d is nonprincipal, even when p divides one or more k_j. For negative exponents use the conjugate character with the same zero extension; no inverse of a zero is taken. Retain each original zero at a shared prime. Multiplying by a fixed ray character supported on S cannot undo nontrivial ramification at the good prime p. This is a sufficient criterion; if (1) fails, particular choices of indices can cancel the local exponent and no universal orthogonality follows.

In particular, for n=2m and m-order inverse factors ρ_d(k)^{±2}, g=2 and **every odd a works**. This includes products, conjugates and coefficient expansions of any number of such inverse polynomials. For n=6 and m=3 it recovers the sextic-mark/cubic-inverse parity mechanism.

## Uniform character sum and coefficient costs

Let α=103/512, or α=1/4 if only convexity is used. For a nonprincipal finite-order character ξ with conductor norm Q and fixed infinity type, [Wu, Theorem 1.1](https://doi.org/10.1112/S0010437X19007309), combined with θ=7/64, smooth Mellin inversion and finite-sector expansion, gives

    Σ_{d good sf} W(Nd/X) ξ(d)
       ≪_{K,S,W,ε} X^(1/2+ε) Q^(α+ε).                      (2)

Here the squarefree Dirichlet series is L_K(s,ξ)/L_K(2s,ξ²) times the finite fixed and moving mask factors. Shift to Re s=1/2+ε; the numerator is entire, the denominator is controlled by its absolutely convergent reciprocal Euler product, and the fixed smooth transform absorbs the polynomial height factor in Wu's hybrid estimate. Primitively induce imprimitive characters and retain the original zero masks. The claim uses Q bounded by a fixed S factor times the product of the good prime radicals of the displayed indices.

For example, take a common annular polynomial

    A_d = Σ_{k good sf} c_k ρ_d(k)^2,    Nk≈L,
    Σ_k |c_k| ≪ L^(1/2+ε),

as holds for a smooth normalized Möbius polynomial c_k=μ(k)U(Nk/L)/√Nk. For every odd a,

    |Σ_d W(Nd/X) ρ_d(p)^a |A_d|²|
       ≪ X^(1/2+ε) P^(α+ε) L^(1+2α+ε).                    (3)

All characters are zero-extended; the estimate remains valid for indices divisible by p. The absolute coefficient expansion is deliberately explicit: conductor norm is ≪_S P L², and the two ℓ¹ masses cost L. If P=X^p and L=X^ℓ in fixed polynomial ranges, (3) saves a fixed power against X when

    α p + (1+2α)ℓ < 1/2.                                    (4)

For fixed p, this permits ℓ<128/359≈0.356546 with Wu's exponent, or ℓ<1/3 via convexity. For a normalized prime block, summing its coefficients by ℓ¹ incurs an additional P^(1/2+ε); condition (4) must then be replaced by αp+(1+2α)ℓ+p/2<1/2. This elementary estimate is not a selected-row, coefficient-uniform large sieve.

## Frobenius-pair symmetry and an L-value consequence

Now suppose n=2m. Let ζ_n denote a primitive n-th root. For a good prime p and z∈μ_n, let W_d=V(Nd/X)Σ_j |A_{j,d}|², where V is a fixed nonnegative smooth row weight and the finite collection of m-order inverse polynomials satisfies the same coefficient conditions as in (3). Fourier inversion on μ_n expresses the difference of the weighted masses on ρ_d(p)=z and ρ_d(p)=−z using only **odd** Fourier exponents. Therefore in the regime (4),

    Σ_{ρ_d(p)=z} W_d − Σ_{ρ_d(p)=−z} W_d = O(X^(1−κ))       (5)

for some κ>0, subject to the displayed coefficient mass and the common smooth row weight. Rows with p|d have mark zero and lie in neither class. This is a difference estimate; a relative asymptotic additionally requires a lower bound for the relevant weighted mass. For m odd, the quadratic character ρ_d(p)^m is itself an odd harmonic, so its weighted mean is small. For m even, m is even and this quadratic harmonic is not controlled by the parity criterion; pair symmetry (5) still holds.

One actual L-value version avoids polynomial truncation. Fix s=σ+it with σ>1+α and t fixed. With ρ_d² regarded as its original zero-extended Hecke character, the Euler product gives

    L_K(s,ρ_d²)^(−1)=Σ_k μ_K(k)ρ_d(k)²/(Nk)^s

absolutely. Expanding its squared modulus and applying (2) termwise is justified because Σ_k (Nk)^(−σ+α+ε)<∞. It yields

    Σ_d W(Nd/X) ρ_d(p)^a |L_K(s,ρ_d²)|^(−2)
       ≪_{K,S,s,W,ε} X^(1/2+ε) P^(α+ε),    a odd.          (6)

Hence the reciprocal-L weighted masses at z and −z differ by the same bound. For P≤X^((1/2−κ)/α), this is a power saving compared with X. Absolute convergence also gives fixed upper and positive lower bounds on the reciprocal weight, so it is a meaningful weighted symmetry. This is a result in the elementary half-plane σ>1+α; it asserts no new zero-free strip, central-value estimate or novelty.

More generally, for inverse factor exponents b_j let g=gcd(n,b_j). If (1) applies to every frequency not divisible by g, the resulting weighted distribution on μ_n is invariant up to the correlation error under multiplication by ζ_n^(n/g), a subgroup of order g. Distinct roots or separate mark primes require their own local noncancellation checks and conductor factors; no multi-prime independence follows without them.

**Independent review:** Other_families checked the local gcd criterion, conductor and coefficient exponents, and reciprocal-L argument under the stated family-matching hypotheses. The review identified two presentation issues, now corrected: the ±z statement requires n even, and its weight includes the fixed smooth row cutoff.
