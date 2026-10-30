# Conditional relative-zeta density for cyclic prime extensions

**Status.** A source-qualified class-field consequence of the [squarefree conductor-strip calculation](../2026-10-29-squarefree-conductor-strip/README.md). It additionally requires the powered-family compatibility and uniform fixed-order rectangular-sieve/detector replays described below; those inputs and the cited preprint are not independently established here. It is not an individual zero-free region or a statement about the full ζ_L, and no exhaustive priority claim is made.

Fix an odd prime p≥7, a field K containing μ_p and the source's good set S. For every good prime ideal B let χ_B be the source's primitive order-p character and let L_B/K be its cyclic degree-p class field. For

    σ_−=(3−sqrt(1−8(p−1)/p²))/4 < σ <
    σ_+=(3+sqrt(1−8(p−1)/p²))/4,
    δ=2σ−1,
    R_p(σ)=1/p+(1−δ)(1−3/p+δ/2)/(1−2/p),                  (1)

the following is conditional on the stated inputs: for each ε>0 there is τ>0 such that at most `O(X^(R_p(σ)+ε))` distinct L_B with `N f(χ_B)≤X` have a zero of their relative quotient in `Re s≥σ`, `|Im s|≤X^τ`. There are ≫X/log X such distinct fields, so a proportion tending to one has no quotient zero in that rectangle.

The quotient is the entire Artin product

    ζ_(L_B)(s)/ζ_K(s) = ∏_(j=1)^(p−1) L_K(s,χ_B^j).           (2)

Each factor is a nontrivial finite-order Hecke L-function. A zero of ζ_K persists in the full ζ_(L_B), so (2) is the controlled object; the conclusion does not assert full Dedekind-zeta zero-freeness.

## Why all powers have the same density bound

For every fixed `1≤j≤p−1`, the local power has exact order p, the same original zeros and the same primitive conductor as χ_B. On good ideals, `χ_B(q)^j=χ_(B^j)(q)`, including q meeting B. Applying the unbalanced conjugate-exponent moment and detector to the powered family `χ_B^j` gives the same R_p(σ) bound for B squarefree: the column family becomes `χ_q^j`, which is an order-p FHL family up to the fixed finite-ray phases and invertible root embedding. This is exactly the powered-family compatibility gate reviewed in the [full-order note](../2026-10-29-full-order-density/README.md); matching conductors alone would not justify it. The proof is repeated for each fixed j, with constants and admissible height powers depending on j; the finite union over j costs only a constant and the smallest positive height power may be chosen. The bound over all squarefree B dominates the prime-label subset. No permutation of prime ideals or assumption that a power is the identical original label family is needed.

Different B have different good conductor support, so their degree-p fields are distinct. Their bad conductors are uniformly bounded, and `N f(χ_B)≍NB`; the prime ideal theorem gives the denominator after a fixed rescaling. Since all j are coprime to p, the local characters χ_B^j have the same kernels as χ_B at every place and hence the same conductor, including at S. The conductor–discriminant formula therefore gives

    |D_(L_B)|=|D_K|^p [N f(χ_B)]^(p−1).                       (3)

Consequently the number of these fields with `|D_(L_B)|≤Y` and a relative-quotient zero in the analogous window at a sufficiently small power height Y^τ′ is

    O(Y^(R_p(σ)/(p−1)+ε)),                                     (4)

while the family has ≫Y^[1/(p−1)]/log Y distinct fields. For a common Y-height, split conductor scales X dyadically at X=Y^u with `0<u<R_p(σ)/(p−1)`; use the trivial label count below that threshold and choose τ′ below u times all p−1 available detector height powers above it. The fixed |D_K| factor and logarithmic dyads are absorbed in the constants and ε.

At p=7 and σ=3/4, `R_7=201/280`, so (4) has exponent `67/560` versus denominator exponent `1/6`. At p=31 and σ=4/5, `R_31=12288/22475`, so the exception exponent is `2048/112375≈0.018225`, versus family exponent `1/30`. The direct squarefree character comparison to de Faveri's stated natural-index bound is recorded in the linked squarefree note; it is not an exhaustive comparison for the relative-zeta family.

Two independent source-qualified reviews checked the powered-family root embedding and masks, the local conductor kernels, field count, quotient and discriminant/height conversion. They did not prove the imported analytical inputs.
