# Power lifting and density-bootstrap limits for fourth- and fifth-order inverses

**Status.** The lifting identity and scalar calculation are elementary. The strong all-row inverse bound below is an explicit additional hypothesis; no theorem establishing it for n=4 or n=5 is claimed. The existing direct density theorem and Θ_n sieve are source-qualified by their stated inputs. No new zero-free region follows.

Fix n≥3, a fixed number field containing μ_n, and FHL data and good set S. Let

    M_u(D)=D^(−1/2) Σ_(a good) μ_K(a)χ_u(a)W(Na/D)

for a common smooth annular W and original zero masks. Suppose a Liu-type **all-natural-row inverse input** is proved: for every fixed c,ε>0, uniformly in fixed smooth-profile seminorms, bounded norm-twist heights and the required scale supremum,

    Σ_(Nk≤H) sup_(1≤T≤D) |M_k(T)|² ≪ H(HD)^ε,
    H≥D^(1+c).                                                  (1)

This is an extra hypothesis for n=4 and n=5. A version for sixth-order rows is claimed in Liu's Theorem 10.4 under its own cyclotomic, theta and source hypotheses; it does not automatically transfer to fourth or fifth order.

For n-free u and good a, χ_(u a^n)(b)=χ_u(b)1_((a,b)=1), including all zeros. Expanding the deleted Euler factors expresses M_u(D) as a divisor-weighted sum of `M_(u a^n)(D/Nd)` for d|rad(a), up to the standard annular profile split. The divisor weight and its smooth-profile seminorms cost `(HD)^ε`; the scale supremum is needed here, and bounded subunit scales are included by the usual unit-annulus convention. The map `(u,a)↦u a^n` is injective on n-free u, with prime exponents split uniquely. Averaging over `Na≲(H/U)^(1/n)` gives, for U≤Nu≤2U,

    Σ_u |M_u(D)|² ≪ U^(1/n) H^(1−1/n)(HD)^ε.                  (2)

Choose `H≈max(U,D^(1+c))`, then let c>0 be arbitrarily small relative to ε. At D=U^r, the resulting normalized inverse exponent is

    e_n(r)=max{1,[1+(n−1)r]/n}.                                (3)

For comparison, applying de Faveri's arbitrary-coefficient **all-row** Θ_n bound to the same lifting and optimizing H does not prove (3): all its terms are nondecreasing in H after multiplication by `(U/H)^(1/n)`, so the best choice is H=U and one recovers the original generic sieve. The extra content is exactly the Möbius-specific all-row hypothesis (1).

The strong hypothesis is itself constrained by its nth-power rows. At `u=a^n`, χ_u is principal with the original coprimality mask; the fixed-profile Mellin Ω argument from [the power-row note](../2026-10-29-power-row-spectral-boundary/README.md) shows that (1) for every fixed c>0 would imply

    ζ_K(s)≠0 for Re s>1−1/(2n).                                 (4)

This is 7/8 for n=4 and 9/10 for n=5. It is not an impossibility theorem, but it shows (1) includes a genuine fixed-field zeta input and cannot be inferred from a generic coefficient norm estimate.

## Why an unstructured density bootstrap cannot beat the generic inverse face

There is a precise obstacle to obtaining an actual improvement just by feeding the existing direct-density exponent back into pointwise reciprocal estimates. For the [direct n-free density](../2026-10-29-direct-nfree-density/README.md), write δ=2σ−1 and

    R_n(δ)=2/n+3(n−3)(1−1/n−δ)/[n(3−δ)−7],
    E₃(r)=2/n+(1−1/n)r.                                         (5)

For every `1<r<3/2`, define

    δ_r=3−7/n−3(n−3)/(nr).                                     (6)

Then `2/n<δ_r<1−1/n`, and the detector cutoff corresponding to δ_r is exactly r. Direct substitution gives

    R_n(δ_r)+δ_r r = E₃(r).                                    (7)

On `1≤r≤3/2` the term E₃ is the dominant generic Θ_n inverse-moment face. Thus a conventional layer-cake estimate that separately bounds each zero-height layer by `X^[R_n(δ)+ε]` and each normalized inverse by its pointwise `X^[δr+ε]` upper bound cannot, from these exponents alone, certify an exponent strictly below E₃: its supremum includes equality (7). This holds for n=4 and n=5. It is a limitation of that particular use of the known density bound, not a lower bound on true inverse moments or a prohibition on using stronger density inputs or arithmetic cancellation.

## What (3) would buy

At every fixed `2/n<δ<1−1/n`, let t and L=2t/3 be the direct theorem's four-face optimizer and R its density exponent. Its generic inverse/ordinary-fourth relaxation reaches R only at `(r,m)=(L,L/2)` and on `r=t, 0≤m≤L/2`. The inverse exponent (3) is strictly smaller than the generic inverse exponent at both locations: at L<1 the generic inverse exponent exceeds 1 by `(2L−1)/n>0`, and at t>1 it exceeds e_n(t) by 1/n. Continuity and compactness then give a fixed positive improvement in the density exponent if (1) and the direct theorem's ordinary fourth and detector inputs all hold. This is a conditional reduction only; it does not assert that (1) is known in orders four or five.
