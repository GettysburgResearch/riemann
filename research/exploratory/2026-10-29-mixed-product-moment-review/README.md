# Independent review of a mixed inverse/plain second moment

**Status:** The proposed upper bound follows from the stated cubic squarefree-column sieve and the usual fixed-parameter Sobolev interface. It does not itself establish a detector, a zero-free region, or novelty. The proof applies to the exact original row characters and masks; it relies on both polynomials being evaluated at the same row presentation.

Let D,E≥1 have fixed polynomial bounds in X. For a row g and one of the finitely many allowed presentations write

    M_g=D^(−1/2) Σ_a μ_K(a) ψ_g(a) W₁(Na/D),
    S_g=E^(−1/2) Σ_b ψ_g(b) W₂(Nb/E).

The W_i are bounded annular profiles. Multiplicativity, including zero extensions, gives the exact convolution

    M_g S_g=(DE)^(−1/2) Σ_q ψ_g(q) C(q),
    C(q)=Σ_{ab=q} μ_K(a)W₁(Na/D)W₂(Nb/E).                (1)

Its q-support has norm `≍DE` with fixed endpoint constants, and `|C(q)|≪τ_K(q)≪_ε (Nq)^ε`. The profiles need not make C(q) a function only of Nq: the source squarefree sieve accepts arbitrary common coefficient vectors.

Factor q uniquely as `q=q₁v²`, q₁ squarefree, with no coprimality assumption between q₁ and v. For each v the row factor ψ_g(v²) is outside the inner q₁ sum and has modulus ≤1. The squared norm of the inner coefficient vector is

    (DE)^(−1) Σ_{Nq₁≪DE/(Nv)²} |C(q₁v²)|²
       ≪_ε (XDE)^ε/(Nv)².                                  (2)

This follows from ideal counting and the divisor bound. The nonempty unit-end case `DE/(Nv)²≈1` is covered by an O(1) endpoint box. De Faveri's squarefree-column sieve, reciprocity and row dyadic summation then bound the ℓ² row norm for that fixed v by

    ≪_ε (XDE)^ε [X+X^(1/2)DE]^(1/2)/(Nv).

The source scale is `Q_v≈DE/(Nv)²≤C DE`, so replacing it by DE only enlarges the bound. Minkowski over v and `Σ_{Nv≤C sqrt(DE)}1/Nv≪log(2DE)` yield

    Σ_g |M_g S_g|² ≪_ε (XDE)^ε [X+X^(1/2)DE].             (3)

If ψ_g contains a fixed background ν, its v² factor also has modulus ≤1. Fixed bad-prime source factors can be omitted consistently or split into their fixed-prime exponent tuples and summed; their geometric weights are convergent. Finite ray-class partitions absorb reciprocity phases into a common q₁ vector, and finitely many row presentations can be grouped separately.

For detector witnesses the zero's real part and the common norm-twist height vary across rows. Apply the finite-dimensional Sobolev reduction to the row-indexed products before Chebyshev. For each common parameter value, (1)–(3) use a single coefficient vector across all rows. Differentiating in those parameters replaces W₁,W₂ by a finite sum of profiles with fixed logarithmic factors; each coefficient remains bounded by `τ_K(q)` times a fixed power of log X, and the v² phase contributes at most the same type of factor. Thus each differentiated common-parameter moment satisfies (3) with subpower losses, and the bounded interval for the height adds the already stipulated polynomial `X^{O(τ)}` cost. This step is essential: applying the sieve separately to an independently chosen vector for each row would be invalid. A source framework allowing an arbitrary independent smooth function for each row, rather than the detector's specified finite-dimensional profile family, would require a stronger hypothesis.

With `D=X^r,E=X^m`, equation (3) is `≪X^ε[X+X^(1/2+r+m)]` after absorbing fixed logarithmic and Sobolev costs. Combining it with a saturated product lower bound would count witness rows by

    X^{max(1,1/2+r+m)−δ(r+m)+ε},

with the standard detector losses, bin and height qualifications. The numerical minimax consequences depend on the full allowed r,m region and must be optimized separately; (3) alone is not an individual zero-free estimate.

## Scalar limitation when combined with the two separate moments

The extra mixed estimate alone does not improve the previously obtained joint density exponent using only the current witness inequalities. Fix δ∈(0,1), put `t₀=1/(2−δ)` and `R=1−δt₀/2`. Ignore arbitrarily small losses and write the three exponents as

    f=max(1,1/2+r)−δr,
    g=1−δm,
    h=max(1,1/2+r+m)−δ(r+m).

For any detector parameter `t∈[1/2,t₀]`, the admissible point `r=m=t₀/2` satisfies `r≤t`, `m≤1/2` and `r+m≥t`; all three exponents equal R there. For `t∈[t₀,1]`, the admissible point `r=t,m=0` gives `f=h=1/2+(1−δ)t≥R` and `g=1≥R`. Thus every t leaves some configuration on which the best of the three bounds is at least R. The existing choice t=t₀ achieves the upper bound R from the separate moments. This is a limitation of the displayed estimates and witness region, not a claim that the actual witnesses occur at either test point.
