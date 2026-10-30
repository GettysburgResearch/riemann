# Full-zeta family rectangles at 87387/100000

**Status.** These are conditional family-density consequences, not a new individual zero-free region. They combine the source-qualified [quartic continuum](../2026-10-29-quartic-relative-continuum/README.md) and [prime-degree fourth-witness calculation](../2026-10-29-fourth-moment-cyclic-box/README.md) with the separately staged [Dirichlet candidate](../2026-10-29-return-retune-8738694/README.md). The generalized sieve, detector/profile/height bridges and source preprints have not been independently established; the candidate also requires admission and its conventional analytic interpretation. Comparisons are with named sources, not an exhaustive literature claim.

Put

    σ=87387/100000,  δ=2σ−1=37387/50000,
    θ=4369347/5000000,  σ−θ=3/5000000>0.                      (1)

The strict positive margin in (1) is essential: the candidate only gives an open half-plane Re s>θ. Its asserted all-Dirichlet nonvanishing gives zero-freeness at every height of ζ_Q(i)=ζL(χ₋₄) and ζ_Q(ζ₅)=ζ∏_{χ mod 5, χ≠1}L(s,χ), away from their poles at 1. Both factorizations are exact, using primitive nonprincipal characters and ζ itself for the principal factor.

For K=Q(i), take good coprime squarefree ideals A,B in fixed boxes `NA≈X^a`, `NB≈X^(1−a)` and the cyclic quartic L/K from χ_(AB³). For K=Q(ζ₅), use the analogous χ_(AB⁴) and cyclic degree-five field. The source-qualified t=1 inverse-second/ordinary-fourth detector gives

    family          a                  R                 R/(degree−1)
    quartic         4129/50000         10871/20000       10871/60000
    quintic         17387/180000       30613/60000       30613/240000.  (2)

For each fixed ε>0, there is a sufficiently small fixed τ>0 such that at most `O(X^(R+ε))` fields in the corresponding box have a zero of the relative quotient ζ_L/ζ_K in `Re s≥σ`, `|Im s|≤X^τ`. In the quartic case the quadratic core is counted separately: its exponent is `1732862231/5000000000<R`, and the possible factorization multiplicity of its squarefree radical is only X^ε. The conjugate quartic factor has the same zero count. In the quintic case the four nontrivial powers are covered by the finite list of compatible powered FHL embeddings on the same labels. The [squarefree-box count](../2026-10-29-squarefree-box-count/README.md) supplies ≫X distinct fields after the bounded character-to-field fibers.

On the conditional base-field input above, the same exception counts apply to the **full** ζ_L, with its pole at s=1 excluded. All nontrivial relative factors are entire, so multiplication by the base ζ_K cannot hide a zero. In either family every nontrivial power has conductor norm ≍X; consequently |D_L|≍X^(degree−1). Choosing one top-scale X-box with constants putting its fields below Y, and choosing τ′<τ/(degree−1), gives the discriminant exponents in the last column of (2), against ≫Y^(1/3) quartic or ≫Y^(1/4) quintic fields. This is a one-box Y-family; a cumulative union of all smaller boxes needs the separate small-height/dyad argument.

For the same boxes, conjugation changes the natural-label norm to `X^[1+(n−2)a]`. At σ in (1), de Faveri Corollary 1.5 gives the fixed-height X-exponents and positive gaps

    n=4:  5502460264299/9374744620000,   gap 203408913049/4687372310000;
    n=5:  148430248422779/237951669300000, gap 6755835221191/59487917325000.  (3)

The fixed-height Khale–O'Kuhn–Panidapu–Sun–Zhang conductor comparator, under its hypotheses, is `50452/87387` for both fields and also exceeds each R in (2). The displayed inequalities remain strict at sufficiently small polynomial heights after their source-specific height losses are accounted for. These comparisons do not verify the cited sources or establish priority. Hu's claimed open Re s>7/8 strip and Liu's claimed 0.874886647… boundary both lie strictly to the right of σ in (1).

## Open rectangles at the candidate boundary itself

There is a stronger, still conditional formulation which does not require a positive gap σ−θ. Apply the relative-quotient density estimates at **σ=θ**, counting zeros with `Re s≥θ`. Their inequalities are valid at this fixed value because `δ=1869347/2500000` lies strictly inside the relevant parameter intervals. The assumed base Dirichlet theorem is used only for `Re s>θ`. Therefore every field outside the relative-exception set has full ζ_L zero-free in the **open** rectangle `Re s>θ`, `|Im s|≤X^τ`, apart from its pole at 1. No base nonvanishing on Re s=θ is asserted.

The exact parameters at this boundary are

    family          a                  R                 R/(degree−1)
    quartic         206449/2500000     543551/1000000     543551/3000000
    quintic         869347/9000000     1530653/3000000    1530653/12000000. (4)

The quartic quadratic-core exponent is `4332174293591/12500000000000`, strictly smaller than its order-four R. The same squarefree-pair count gives ≫X fields in each family; the one-box discriminant lower counts are ≫Y^(1/3) and ≫Y^(1/4), respectively, with exception exponents in (4) and suitably shortened height powers.

For the same boxes the de Faveri natural-index comparators are `687809742243193359/1171843043591000000` (quartic) and `18553826691430685539/29743946903865000000` (quintic). The Khale et al. fixed-height conductor comparator is `2522612/4369347` for each. Each is strictly larger than the corresponding R in (4), with sufficient room for a small fixed height power. These are named-source comparisons only, and all source, detector and candidate qualifications above remain in force.

**Independent review.** Families checked both near-boundary and exact-θ fractions, the quadratic core and named-source comparators, squarefree-pair counts and top-box height. The reviewer confirmed that the exact-boundary argument yields the open full-ζ rectangle only; it does not establish the analytic inputs.
