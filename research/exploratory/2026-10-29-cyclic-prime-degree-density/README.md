# Source-dependent relative-zeta rectangles in cyclic prime-degree families

**Status:** A class-field consequence of [the full fixed-order conductor-density proof](../2026-10-29-full-order-density/README.md), including its de Faveri general-order sieve replay, powered-family compatibility, Goldmakher–Louvel quadratic input where relevant, and fixed-field detector/profile proof. The cited preprints and proof replays have not been independently validated. This concerns a family of relative quotients, not an individual zero-free region or the full ζ_L. No priority claim is made.

Fix an odd prime p≥5, a number field K containing μ_p and the source's fixed good-prime set S. For each nonunit good p-th-power-free g, the finite-order source character χ_g has exact order p: at any good prime dividing g its valuation is in `{1,…,p−1}` and the local character has order p. Let L_g/K be the corresponding cyclic degree-p extension. Write

    R_p(σ)=2−1/(p−1)−σ.

For every fixed `1−1/(p−1)<σ<1` and ε>0, the cited source-dependent density bound gives τ>0 such that the number of distinct fields L_g with `N f(χ_g)≤X` and a zero of the relative quotient `ζ_(L_g)/ζ_K` in `Re s≥σ`, `|Im s|≤X^τ` is

    ≪_{K,S,p,σ,ε} X^{R_p(σ)+ε}.                               (1)

There are ≫X(log X)^{p−2} such distinct fields, so the exceptional proportion tends to zero.

Artin formalism gives

    ζ_(L_g)(s)/ζ_K(s)=∏_{k=1}^{p−1} L_K(s,χ_g^k).              (2)

All factors are entire. If `g=∏_𝔭 𝔭^{j_𝔭}` with `1≤j_𝔭≤p−1`, define g_k by replacing each exponent j_𝔭 with its least positive residue k j_𝔭 mod p. The source's multiplicativity, including original noncoprime zeros, and its trivial p-th-power factor give

    χ_g(q)^k=χ_(g_k)(q)      for every good ideal q.             (3)

Consequently their primitive inducing Hecke characters agree: their quotient is a finite-order character trivial at every prime outside S and hence trivial by Chebotarev. Since k is coprime to p, χ_g and χ_g^k have the same local kernels and the same primitive conductor at **every** place, including S. Each factor in (2) is therefore a member of the full source family at the same conductor cutoff. Apply the source density estimate to the finitely many factors; every exceptional field has at least one exceptional character label. Field-count injectivity is unnecessary for the upper bound.

For the denominator, the p-free label count with `N rad(g)≤X/C` is ≫X(log X)^{p−2}, because

    ∏_{𝔭∉S}[1+(p−1)(N𝔭)^(−s)] = ζ_(K,S)(s)^(p−1) H_p(s)

with H_p holomorphic near s=1 and H_p(1)>0; apply a positive-coefficient Tauberian theorem and absorb the fixed bad conductor in C. Each cyclic degree-p field has exactly p−1 nontrivial primitive characters. Distinct p-free g give distinct characters: at each good 𝔭, the tame local character detects both absence and the exponent `1,…,p−1`. Thus at most p−1 source labels produce any one field and the stated field lower bound follows. Good prime labels provide the weaker independent bound ≫X/log X.

All p−1 nontrivial characters have the same conductor, so the conductor–discriminant formula is

    |D_(L_g)|=|D_K|^p [N f(χ_g)]^(p−1).                         (4)

Consequently, for absolute discriminant at most Y, the exceptional-field exponent is `R_p(σ)/(p−1)`, and the family-size argument supplies ≫Y^{1/(p−1)}(log Y)^{p−2} distinct fields. A slightly smaller fixed power height in Y absorbs the constant `|D_K|^p` and the change from X to `Y^(1/(p−1))`.

For p=5 and σ=4/5, the conductor exponent is 19/20 and the discriminant exponent is 19/80, versus a family-size exponent 1/4 in discriminant ordering. The detailed quintic instance appears [here](../2026-10-29-cyclic-quintic-density/README.md). This is not a comparison with every prior cyclic-field density theorem; source and literature qualifications are essential. Zeros of the fixed base ζ_K remain in ζ_(L_g), so (1) gives no zero-free assertion for the full Dedekind zeta functions.
