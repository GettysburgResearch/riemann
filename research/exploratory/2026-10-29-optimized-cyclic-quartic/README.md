# A cyclic-quartic relative-zeta family at the optimized 4/5 box

**Status.** Source-qualified conditional field-family consequence of [the optimized quartic conductor box](../2026-10-29-optimized-monomial-box/README.md), the fixed-field quadratic Hecke large sieve and its buffered detector replay, and classical class field theory. The generalized rectangular-sieve and detector/profile/height replays, and the cited source inputs, are not independently established here. This does not prove an individual zero-free region or a zero-free rectangle for the full ζ_L. No exhaustive priority claim is made.

Let K=Q(i), let S be the fixed good set for the source quartic FHL family, and choose good distinct prime ideals A,B with

    NA ≍ X^(1/30),     NB ≍ X^(29/30),     g=AB³.              (1)

Every χ_g has exact order 4; at both A and B its local character has exact order 4. By class field theory it cuts out a cyclic quartic extension L_g/K. Under the stated inputs, for every ε>0 there is τ>0 such that the number of **distinct** such fields with a zero of their relative quotient in

    Re s≥4/5,     |Im s|≤X^τ

is `O_ε(X^(17/25+ε))`. There are `≫X/(log X)²` distinct fields in fixed nonempty boxes of the form (1), so the proportion without a quotient zero in this rectangle tends to 1.

The quotient means the entire product of its nontrivial class-field L-functions,

    ζ_L(s)/ζ_K(s)=L_K(s,χ_g)L_K(s,χ_g²)L_K(s,χ_g³).          (2)

It is understood by this Artin factorization. No estimate here removes a zero of the fixed base ζ_K from ζ_L.

## The quadratic core and the field count

The source characters are multiplicative in their ideal label with their original good-prime zero masks. For every good ideal q,

    χ_(AB³)(q)² = χ_A(q)² χ_B(q)^6
                  = χ_(AB)(q)².                               (3)

Both sides vanish at q meeting AB. Their primitive inducing characters agree because they agree at every prime outside a fixed finite set. In particular χ_g² is a nontrivial quadratic Hecke character with good conductor exactly AB, and its bad conductor is supported in fixed S with uniformly bounded norm. Consequently

    N f(χ_g) ≍ X,    N f(χ_g²) ≍ X.                           (4)

The same quadratic character cannot arise from two different products AB: its good conductor records the radical AB. Because the two prime-norm scales in (1) are distinct, that product determines A and B in order. The source assigns one χ_g to each ideal label. Thus the map from the labels of (1) to quadratic cores is injective; no multiplicity from choosing B remains. Fixed ray sectors can be partitioned finitely, with no power loss.

The conditional long-detector quartic bound in the optimized-box note gives at most `X^(17/25+ε)` zeros (hence exceptional labels) for χ_g in a sufficiently short X-power height window. The factor χ_g³ is the complex conjugate character, so its zeros are reflected across the real axis; the symmetric height window makes its exceptional label set identical. For χ_g², Goldmakher–Louvel's quadratic Hecke large sieve and the fixed-field saturated detector give the core count `O(X^(13/25+ε))` at σ=4/5. Here the powered source family matches the quadratic family with the original masks, as reviewed in the [controlled-core quartic note](../2026-10-29-cyclic-quartic-density/README.md). The two analytic theorems may prescribe different height powers; take τ smaller than both and absorb fixed conductor factors. Injectivity just proved transfers the quadratic exceptional-core count to labels. A union bound in (2) gives the stated `17/25` field exception exponent.

The prime ideal theorem supplies ≫X/(log X)² ordered pairs in fixed positive-width boxes in (1). Different labels give distinct primitive quartic characters because their tame good-prime exponent vectors differ. A cyclic quartic field has exactly two order-four characters, so at most two of these distinct labels can define the same field. This proves the denominator without assuming a common quadratic core.

## Absolute discriminant ordering

The conductor–discriminant formula gives the exact identity

    |D_L|=|D_K|⁴ [N f(χ_g)]² N f(χ_g²) ≍ X³.                (5)

For the union of these boxes over scales, define the family by the fixed comparability in (1). For every ε>0 and a sufficiently small τ′>0, at most

    O_ε(Y^(17/75+ε))                                           (6)

such distinct fields of `|D_L|≤Y` have a quotient zero in `Re s≥4/5`, `|Im s|≤Y^τ′`. To see the uniform height carefully, split the conductor scale X dyadically. For X≤Y^u, bound exceptional fields simply by the number of labels, `≪Y^(u+ε)`, choosing fixed `u<17/75`. For `Y^u<X≪Y^(1/3)`, choose τ′ below u times both available detector height powers; then `Y^τ′≤X^τ` on every remaining dyad. Summing their `X^(17/25+ε)` bounds gives (6). Fixed scale factors and logarithmic dyads cost Y^ε. Conversely, take pairs in sufficiently small fixed boxes of scale X≈Y^(1/3); the uniform upper constants in (5) put all their fields under Y, giving `≫Y^(1/3)/(log Y)²` distinct fields. Thus the discriminant-ordered exceptional proportion also tends to zero.

This field statement inherits the two density replays, including their fixed-field source normalizations and arbitrary small losses. It is a source-dependent family consequence, not a claim that any individual Dedekind zeta function is zero-free.

A targeted literature review found no stronger result directly covering this entire two-prime Q(i) quartic quotient family. De Faveri's natural-index corollary gives the order-four factors `X^(8/11+ε)T^(9/7+ε)` after conjugating their labels; a separate quadratic bound is needed for χ². Cho–Kim's work on certain cyclic quartic fields over Q and near-1 rectangles has different scope. This is not an exhaustive priority review.

Two independent reviews checked the squared-character masks and primitive conductor, core injection, conjugate symmetry, field fibers, conductor–discriminant formula and cumulative height split, conditional on the named analytical inputs.
