# A cyclic-cubic full-zeta family over Q(ζ₁₂)

**Status.** This is a source-qualified consequence for a specified family, conditional on the analytic interfaces below and on the conventional interpretation of the separately staged Dirichlet candidate. It is not a new individual zero-free region, an unconditional theorem independent of those inputs, or an exhaustive novelty claim.

Let `K=Q(ζ₁₂)` and `θ=4369347/5000000`. Assume the cubic `n`-free row sieve of [de Faveri, arXiv:2610.04045](https://arxiv.org/abs/2610.04045), the fixed-field long-cutoff detector and common-profile eighth-moment transfer described in [the direct density calculation](2026-10-29-direct-nfree-density/README.md) and [its detector proof](2026-10-29-direct-nfree-density/UNIFORM-DETECTOR-PROOF.md), including the original FHL zero masks and uniformity in the finite ray sectors. Assume also that the separately staged Dirichlet candidate gives the conventional primitive Dirichlet zero-free strip `Re s>θ`. These are named inputs, not proofs of the cited recent sources.

Under those inputs, for every ε>0 there are τ,c>0 and a specified family of at least `cY^(1/2)` distinct cyclic cubic extensions `L/K` with `|D_L|≤Y`, such that at most

    O(Y^(3153265/11891959+ε))                                 (1)

of these fields have a zero of `ζ_L(s)` in `Re s>θ`, `|Im s|≤Y^τ`. The pole at s=1 is excluded. All constants may depend on ε and K. The family need not exhaust cyclic cubic extensions of K ordered by discriminant.

## Density and field correspondence

Fix the good finite set S of the FHL cubic presentation. For good cube-free ideals u, write χ_u for the inducing primitive Hecke character and choose its allowed cubic embedding. The source-qualified density estimate gives, for every η>0 and a sufficiently small height power τ₀>0,

    #{Nu≤X : χ_u has a zero with Re s≥θ, |Im s|≤X^τ₀}
       ≪ X^(6306530/11891959+η).                              (2)

The exact scalar parameters are `h=2(1−θ)=630653/2500000`, `t=10/(4+3h)=25000000/11891959`, and `R=10h/(4+3h)=6306530/11891959`. The bound uses the inverse second moment or the ordinary eighth moment according to the actual detector witness; its `t>2` extension, fixed-power Sobolev orders and masks are part of the stated input. If a source is only dyadic, split `Nu≤X^a` trivially, including the standard polynomial-height zero-count loss, and choose τ₀ below a times the local height allowance; summing the remaining dyads supplies (2), with a and τ₀ chosen after η.

Every nontrivial χ_u has exact order three and cuts out a cyclic cubic field L_u/K. The two nontrivial characters of `Gal(L_u/K)` are χ_u and χ_u². The conjugate/powered FHL embedding uses the **same** label u and its original good-prime zero mask; its primitive inducing character is χ_u². Since the finite-order unitary L-function has the usual conjugation symmetry, either apply (2) to this second embedding or use symmetry in the two-sided height rectangle. The primitive all-place Artin factorization is

    ζ_{L_u}(s) = ζ_K(s) L_K(s,χ_u) L_K(s,χ_u²).              (3)

If the S-good source presentation deletes further Euler factors, they have no zeros in `Re s>0`, so it has the same zeros there as the primitive L-function. The field K is abelian over Q, and its primitive Dirichlet factorization is

    ζ_K(s)=ζ(s)L(s,χ_{−3})L(s,χ_{−4})L(s,χ_{12}).           (4)

Thus the assumed Dirichlet strip controls ζ_K in `Re s>θ`; (2) and (3) yield at most `O(X^(R+η))` exceptional labels for full ζ_{L_u} in that open rectangle. No nonvanishing on the boundary line is claimed.

## Counting and discriminants

The good squarefree ideals with norm ≤X number ≫X. Their good local conductors equal u, so different squarefree labels have different primitive character conductors; consequently a cyclic cubic field has at most its two nontrivial characters among these labels. This gives ≫X distinct fields, and excludes the trivial label without affecting the count. More generally, any required finite ray-sector split has only finitely many classes; the source matching and local conductor assertion are assumed uniformly in these fixed classes.

The conductor–discriminant identity and equality of the conductors of χ_u and χ_u² give

    |D_{L_u}|=|D_K|³ (N f_{χ_u})² ≪ (Nu)²,                  (5)

where the fixed S-part is uniformly bounded in the named presentation. Choose X a fixed small multiple of `Y^(1/2)`. Then all fields in this X-truncated family satisfy `|D_{L_u}|≤Y`, and (2) gives the exponent in (1) after replacing η by a sufficiently small value. Shrink the Y-height power to account for `X≈Y^(1/2)`. On the squarefree subfamily, good conductor `u` also gives `|D_{L_u}|≍(Nu)²`, although the one-sided estimate suffices for (1).

The order-three theorem used in (2) is conditional on the cited source/replay interfaces. For K=Q(ω), paper 52 v5 claims a stronger field-specific cubic exponent, but that Eisenstein result does not automatically apply to K=Q(ζ₁₂).

**Independent review.** Families checked the same-label conjugate, primitive base factorization, squarefree field count, discriminant exponent and common-height conversion, treating the named analytic and candidate inputs as assumptions.
