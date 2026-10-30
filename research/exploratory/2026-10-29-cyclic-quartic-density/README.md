# A controlled quadratic core in cyclic quartic relative zeta functions

**Status:** A source-dependent class-field application of [the full quartic conductor-density bound](../2026-10-29-full-quartic-density/README.md), the fixed-field quadratic Hecke large sieve and the [saturated detector replay](../2026-10-29-cubic-short-detector-proof/README.md). The general-order rectangular-sieve replay and source normalizations remain as qualified there. The classical/source inputs are not independently validated. The result concerns a constructed subfamily and a relative quotient, not an individual zero-free region; no priority claim is made.

Fix K=Q(i) and the source's good-prime set S. For a large X take distinct good prime ideals a,b in fixed norm intervals

    Na≈X^(3/10),     Nb≈X^(7/10),

with interval constants chosen so that `N f(χ_(a b²))≤X`; put g=a b². The quartic source character χ_g has exact order 4 because its local character at a does, and class field theory gives a cyclic quartic extension L_g/K. There are ≫X/(log X)² distinct such extensions: prime-pair counting gives that many labels, the tame local character at a has order four and at b has order two, so distinct pairs have distinct primitive characters, and an induced cyclic quartic field has only two order-four generators.

Subject to the listed inputs, for every ε>0 there is τ>0 such that at most

    O_ε(X^(13/15+ε))                                           (1)

of these fields have a zero of the relative quotient ζ_(L_g)/ζ_K in `Re s≥4/5`, `|Im s|≤X^τ`. Consequently their exceptional proportion tends to zero. The same argument works for any fixed κ∈(5/18,1) in place of 3/10, with `Na≈X^κ`, `Nb≈X^(1−κ)`.

## Separating the quadratic core

Artin formalism gives

    ζ_(L_g)(s)/ζ_K(s)=L(s,χ_g)L(s,χ_g²)L(s,χ_g³).              (2)

All factors are entire. The full quartic density bound counts exceptional χ_g and χ_g³ labels by `O(X^(13/15+ε))`: χ_g³ is the conjugate character and the symmetric height window reflects its zeros to those of χ_g. Alternatively it belongs to the same full fourth-free family after the residue-exponent permutation. This leaves the order-two factor.

Source multiplicativity, including original zero masks, gives on all good ideals q

    χ_(a b²)(q)² = χ_a(q)² · 1_((q,b)=1).

The extra mask only deletes the good Euler factor at b. Therefore the primitive inducing character of χ_g² equals that of χ_a²: equality on all good primes away from b determines the Hecke character. Its conductor has norm ≍Na, with fixed bad-prime factors. Distinct good prime a give distinct cores because each is ramified at its own good prime.

The fixed-field quadratic Hecke large sieve and the same saturated detector yield a core zero-density estimate at σ=4/5: for Q≥2 and sufficiently small power height,

    #{a good squarefree : N f(χ_a²)≤Q,
       L(s,χ_a²) has a zero in the window}
       ≪_ε Q^(13/25+ε).                                       (3)

For clarity, the detector arithmetic is the following: the quadratic squarefree inverse moment is `≪Q^ε(Q+D)` for source length D, and the qv² decomposition gives the plain moment `≪Q^(1+ε)` when its length is at most Q^(1/2+η). With δ=2(4/5)−1=3/5, choose detector cutoff `t=1+δ/2=13/10`. Its two witness branches give exponent `1−δ/2−δ²/2=13/25`. Binning, Sobolev and individual zero-count height losses are handled as in the detector note. This is a derivation from the fixed-field quadratic sieve and detector, not an independently claimed new source theorem.

Apply (3) with Q≈X^(3/10). If the core theorem permits height Q^τ₂, choose the final τ below `(3/10)τ₂`, with room for fixed constants. Each exceptional a can be paired with at most `O(X^(7/10+ε))` admissible b, so the number of labels whose χ_g² has a zero is

    ≪ X^[7/10+(3/10)(13/25)+ε] = X^(107/125+ε).                (4)

Since `107/125 < 13/15`, combining (2)–(4) proves (1). In a general box `Na≈X^κ`, the core exponent is `1−κ+κ·13/25`; it is smaller than 13/15 precisely when κ>5/18. The fixed finite conductor factors and norm twists only alter constants or the permitted height power.

The conductor–discriminant formula is `D_L=D_K^4 Nf(χ_g)^2 Nf(χ_g²)`. In these fixed boxes, `D_L≈X^(23/10)`. Thus, after the same fixed-factor and height adjustments, discriminant ordering gives exceptional exponent `(13/15)/(23/10)=26/69`, while the number of fields in this subfamily is ≫Y^(10/23)/(log Y)². This is a box-specific conclusion and does not count all cyclic quartic extensions.

Zeros of ζ_K remain in ζ_L, so (1) does not give a zero-free rectangle for the full Dedekind zeta function. The statement does not assert an individual zero-free half-plane or a comparison with all previous quartic-field results.
