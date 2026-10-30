# A source-dependent density-one relative-zeta rectangle for cyclic quintic fields

**Status:** A class-field corollary of [the full order-five conductor-density proof](../2026-10-29-full-order-density/README.md), with its stated de Faveri generalized-sieve replay, powered-family normalization, fixed-field detector and source qualifications. Those inputs are not independently validated. This is not an individual zero-free region or a statement about the full ζ_L; no priority claim is made.

Fix K containing μ₅ and the source's fixed good-prime set S. For each nonunit good fifth-power-free ideal g, the finite-order character χ_g has exact order 5: any good p|g has exponent 1,2,3 or 4 and contributes a nontrivial local character of order 5. Class field theory gives a cyclic extension L_g/K of degree 5. For every fixed `3/4<σ<1` and ε>0, the full-order-five source-dependent bound supplies τ>0 with at most

    O_{K,S,σ,ε}(X^{7/4−σ+ε})                              (1)

fields L_g with `N f(χ_g)≤X` whose **relative quotient** ζ_(L_g)(s)/ζ_K(s) has a zero in `Re s≥σ`, `|Im s|≤X^τ`. For example σ=4/5 gives exponent 19/20. There are ≫X/log X distinct fields in the constructed family with that cutoff, so the exceptional proportion tends to zero.

Indeed, the four nontrivial characters of Gal(L_g/K) are χ_g^k, k=1,…,4, and Artin formalism gives

    ζ_(L_g)(s)/ζ_K(s)=∏_{k=1}^4 L_K(s,χ_g^k).                 (2)

All four factors are entire. If `g=∏_p p^{j_p}`, form the good fifth-power-free ideal g_k by replacing each j_p∈{1,…,4} with its least positive residue k j_p mod 5. The source's ideal-index multiplicativity and its n-th-power mask imply that, on every good ideal q,

    χ_g(q)^k=χ_(g_k)(q),

including the zero case `(q,g)≠1`. Equality of the primitive Hecke characters follows from equality at all good primes; equivalently, their quotient has trivial Euler factors outside finite S and is the trivial character. Thus each χ_g^k is represented by the same full source family, without assuming an extra independent density theorem for its powers. Since k is invertible mod 5, χ_g and χ_g^k have the same local kernels, hence exactly the same primitive conductor, including at bad primes. A relative-quotient zero in (2) is a zero of one of these four source characters, and the sum of their exceptional labels is bounded by (1). Each exceptional field has at least one exceptional character label; no injectivity is needed for this upper count.

For the denominator, choose good prime labels g=p with `Np≤X/C` for a fixed sufficiently large C. Their characters have good conductor support p and bounded fixed bad factors, so their fields have distinct conductor ideals and therefore are distinct. The prime ideal theorem supplies ≫X/log X such fields. More generally, a cyclic degree-five field has exactly four nontrivial characters, so the map from distinct primitive order-five characters to fields has fibers of size at most four.

The conductor–discriminant formula gives the exact identity

    D_(L_g)=D_K^5 [N f(χ_g)]^4.                                 (3)

Thus, ordering by absolute discriminant `D_(L_g)≤Y`, the exceptional-field exponent is `(7/4−σ)/4`; at σ=4/5 it is `19/80`. Prime labels give ≫Y^(1/4)/log Y distinct fields in this ordering. A slightly smaller fixed power of Y is used for the height so that it is within the source's `X^τ` window after the fixed discriminant factor in (3) is absorbed.

The quotient in (2) is the object controlled: zeros of the fixed base ζ_K persist in ζ_(L_g), so no corresponding assertion for the full Dedekind zeta functions follows. The full-order-five density input is a source-dependent theorem for a family; this corollary neither removes that dependency nor establishes a uniform half-plane for an individual field.
