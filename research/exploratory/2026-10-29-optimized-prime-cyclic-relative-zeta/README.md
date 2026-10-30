# Optimized cyclic prime-degree relative-zeta families

**Status.** This is a source-qualified family consequence of the [optimized-box theorem](../2026-10-29-optimized-monomial-box/README.md), conditional on its generalized rectangular-sieve and fixed-field long-detector/profile/height replays. It does not independently establish those analytical inputs, assert an individual zero-free region, or claim a complete priority comparison. The detailed p=5 case is [here](../2026-10-29-optimized-quintic-relative-zeta/README.md).

Fix an odd prime p≥5 and K=Q(ζ_p). Fix the finite good set S and the order-p FHL family `{χ_a}` of [De Faveri v1](https://arxiv.org/abs/2610.04045v1). Define

    a_p = (3p−10)/[5(p+2)(p−2)]                 for p=5,7,
          0                                      for p≥11;
    R_p = (13p+50)/[25(p+2)]                    for p=5,7,
          (13p²−5p−50)/[25p(p−2)]                for p≥11.       (1)

For p=5 or 7 choose good prime ideals A,B in fixed annuli `NA≈X^a_p`, `NB≈X^(1−a_p)`; for p≥11 take A=(1) and choose the good prime ideal B in `NB≈X`. In both cases let `χ=χ_(AB^(p−1))` and replace it by its primitive inducing character. De Faveri §2.5.1 gives good conductor support AB and bounded bad part, so its conductor f has norm ≍X and χ has exact order p. Class field theory associates to its kernel a cyclic degree-p extension L/K.

For every j=1,…,p−1, consider the entire powered family `χ_a^(j)=χ_a^j`. De Faveri Remark 2.1 says a new complex embedding raises all pth-power residue symbols to any unit exponent j modulo p, and §2.3.4 builds the FHL characters directly from those symbols. Therefore the powered family is another instance of the same source construction, with the same n=p, conductor identities, and fixed bad set; the finite ray reciprocity phases are simply raised to j and remain in finitely many sectors. Exactly, with all good zero masks,

    χ_(AB^(p−1))(q)^j = χ_A^(j)(q) overline(χ_B^(j)(q)).       (2)

The right side is again the conjugate-pair box in the powered source family. It is not an application of the original ±1 box result to the potentially much larger natural index A^j B^(p−j). Applying the cited optimized-box bound with this source family yields, for each j and each ε>0, a τ_j>0 such that

    Σ_(A,B in the specified prime boxes)
       N(4/5, X^τ_j; χ^j) ≪ X^(R_p+ε).                        (3)

Choose τ>0 below all finitely many τ_j. All constants may depend on fixed p,K,S and ε; no uniformity as p varies is asserted. The background twist is trivial here, and primitive characters are used in the zero counts.

Since j is coprime to p, χ and χ^j have the same local kernels and hence the same primitive conductor f at every place, including the fixed bad primes. Therefore

    ζ_L(s)/ζ_K(s) = ∏_(j=1)^(p−1) L_K(s,χ^j),
    |D_L| = |D_K|^p (Nf)^(p−1) ≍ X^(p−1).                  (4)

All relative factors are entire. The sum of the p−1 instances of (3) bounds the number of fields whose relative-zeta quotient has a zero in the rectangle. Distinct prescribed pairs give distinct characters: the good conductor support identifies the distinct-scale primes, and at those primes the exponents 1 and −1 are nonzero and different modulo p. For A=(1) the good support B identifies the label. A cyclic field has exactly p−1 nontrivial generating characters, so the field map has fibers of size at most p−1.

The prime ideal theorem gives ≫X/(log X)² pairs when p=5 or 7, and ≫X/log X labels when p≥11. Fixed rescaling of the annuli ensures the corresponding fields satisfy `|D_L|≤Y` for X a fixed multiple of `Y^(1/(p−1))`. For every fixed ε>0 there exists τ′>0 such that in this specified family at most

    O_(p,ε,S)(Y^(R_p/(p−1)+ε))                              (5)

fields have a zero of `ζ_L/ζ_K` in `Re s≥4/5` and `|Im s|≤Y^τ′`. One can take τ′ strictly less than τ/(p−1), accounting for the fixed discriminant constant. The family has at least ≫`Y^(1/(p−1))/(log Y)²` fields for p=5,7, and ≫`Y^(1/(p−1))/log Y` fields for p≥11. Since R_p<1, the relative-zeta rectangle is density-one within each specified family, assuming the cited inputs. The fixed ζ_K factor is excluded; no conclusion about zeros of ζ_L itself follows.

Examples are p=5, R₅=23/35 and discriminant exception exponent 23/140; p=7, R₇=47/75 and exponent 47/450; and p=11, R₁₁=1468/2475 and exponent 734/12375. The Chen An field-count asymptotic issue documented in the [source audit](../2026-10-29-cyclic-field-count-source-audit/README.md) is avoided: only the elementary prime-ideal lower bound and fixed character-to-field multiplicity are used. No statement is made that these families exhaust cyclic p-extensions.

**Independent review:** Families and High_match checked powered FHL compatibility and zero masks, finite ray data, all-place conductor equality, label/field fibers, one-box height accounting and the three explicit exponents, conditional on the cited analytical replays.
