# Quartic box density using a powered ordinary witness

**Status.** Proposed source-qualified density improvement, conditional on the fixed-order conjugate-pair sieve replay, powered-family and fixed-field detector/common-profile replays, and the stated classical large-sieve/class-field inputs. The imported preprints and replays are not independently established here. This is not an individual zero-free region or a priority claim; prior-art comparison is targeted, not exhaustive.

Let K=Q(i), let A,B be good distinct prime ideals with `NA≈X^(1/30)`, `NB≈X^(29/30)`, and use the source quartic character `χ_(AB³)`. Under the cited inputs, for each ε>0 there is τ>0 such that the total number of zeros with multiplicity in `Re s≥4/5`, `|Im s|≤X^τ` over these labels is

    ≪_ε X^(2/3+ε).                                             (1)

The same bound holds over the full squarefree A,B box. This improves the previously derived 17/25=0.68 upper exponent for this box. The two-prime cyclic-quartic class-field family therefore has at most X^(2/3+ε) exceptional **relative quotients** ζ_L/ζ_K, against ≫X/(log X)² fields. The quadratic factor is bounded separately by the source-qualified quadratic Hecke sieve/detector exponent 13/25, as in the [quartic quotient note](../2026-10-29-optimized-cyclic-quartic/README.md); the two order-four factors are conjugates and have identical symmetric zero counts. Their conductors and the quadratic core are ≍X, so `|D_L|≈X³`: the corresponding discriminant-order exception exponent is 2/9 against a family-size exponent 1/3. The same small-conductor/height split in that note supplies one common Y-power height. This does not control zeros of the base ζ_K in the full ζ_L.

## Powered ordinary block, with masks

Write `Q=X^m`, `S_m(g)=Q^(−1/2)Σ_a c(a)χ_g(a)` for a source ordinary dyad with `Na≈Q`, bounded common smooth/ray coefficients and their fixed polynomial height costs. Squaring and using multiplicativity including zeros gives

    S_m(g)²=Q^(−1) Σ_n χ_g(n) C(n),
    C(n)=Σ_(ab=n) c(a)c(b),      |C(n)|≪_ε (Nn)^ε,           (2)

with `Nn≪Q²`. Decompose every good n uniquely as `n=q v²`, q squarefree. For each fixed v, the row factor χ_g(v²) has modulus ≤1 and may be dropped **after** forming the row L² norm. The remaining coefficient vector on q is common across rows, has squared mass `≪X^ε/(Nv)²`, and retains the original χ_g(q) zero mask and finite ray phases. Reciprocity and the source-conditional quartic conjugate-pair sieve then apply to each q dyad. Minkowski over v costs only `Σ_(Nv≪Q)1/Nv≪log X`; the fixed S part and divisor bounds are absorbed into ε. Therefore

    Σ_g |S_m(g)|⁴ ≪ X^[E(2m)+ε],                             (3)
    E(x)=max{1, 4/15+x, 11/15+x/2}.

The same calculation applies after a common Mellin/Fourier separation of the two profiles. For row-dependent detector heights and real parts, the fixed-dimensional Sobolev replay must be applied before the sieve, with its derivative order and polynomial height budget fixed before choosing τ. Equation (3) is not an assertion that arbitrary row-dependent coefficient vectors can be inserted into one sieve application.

## Saturated detector at t=1

The fixed-field detector replay supplies simultaneous witnesses with

    r≤1+O(η),  0≤m≤1/2+O(η),  r+m≥1−O(η),
    |M_r|²≥X^[(3/5)r−η],   |S_m|²≥X^[(3/5)m−η].             (4)

For the inverse second moment the Markov exponent is

    f(r)=E(r)−(3/5)r
        =max{1−3r/5, 4/15+2r/5, 11/15−r/10}.              (5)

For the ordinary fourth moment (3), the corresponding exponent is `f(2m)=E(2m)−6m/5`; there is no extra division by two in Markov's inequality. If `r≤2/3`, the **actual** constraints give `m∈[1/3,1/2]` up to losses; throughout this whole interval `2m∈[2/3,1]` and all three faces of f are ≤2/3. If `r≥2/3`, all three faces of f(r) are ≤2/3 for `r≤1`. Thus one of the two witness counts has exponent at most 2/3 for every feasible pair. In particular this proof does not assume the false equality `m=1−r`. The rowwise-bin and t-endpoint deviations contribute O(η), absorbed after choosing losses. The source's standard individual zero-count factor and bounded polynomial height loss are handled by choosing τ sufficiently small.

For comparison, de Faveri's stated quartic natural-index exponent is 15/22 at σ=4/5. The conjugate label `A³B` has index norm `≈X^(16/15)`, leading to `X^(8/11+ε)` before height losses. The earlier inverse/plain second-moment minimax gives 17/25 for this box. The targeted comparator does not rule out other stronger density results, and this note relies essentially on the detector and generalized rectangular-sieve replays.
