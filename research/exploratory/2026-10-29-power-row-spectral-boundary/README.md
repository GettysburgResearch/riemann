# Prime-marked inverse growth on n-th-power rows

**Status:** A proposed exact special-family identity, conditional only on the fixed-field prime ideal theorem, standard reciprocal-zeta bounds on fixed zero-free lines, and the stated character convention. It does not establish the stronger inverse moment needed for a new zero-free region. The logarithmic growth is sensitive to the base-field zeta zeros; no priority claim is made.

Let K be a fixed number field, `n≥2` a fixed integer, S a fixed finite bad-prime set, and Θ_K the supremum of real parts of its nontrivial Dedekind zeta zeros. Suppose a family of zero-extended characters satisfies, for every principal ideal v and every good inverse or prime-slot ideal a,

    χ_a(v^n)=1 if (a,v)=1, and 0 otherwise.                   (1)

This includes the usual quadratic symbol over ℚ with S containing 2, and the standard n-th residue symbol in fields containing the n-th roots of unity, after the usual finite bad-prime exclusions. Choose exactly one generator of each principal ideal v; the existence of one per ideal supplies the lower bound, while bounded multiplicity is essential when K has infinitely many units. Let W be the fixed compact-annular smooth profile with Mellin transform nonzero on `Re s>0` constructed in the [cubic note](../2026-10-29-cubic-full-inverse-mean/README.md). For m,r>0, z>0 use an annular prime slot of scale `Z^z`, uniformly bounded coefficients, and one fixed nonnegative smooth profile positive on a subannulus; when z=0 take the empty slot `Q=1`. Define

    M_u(Z^r)=Z^(−r/2) Σ_(a,S)=1 μ_K(a) χ_a(u) W(Na/Z^r),
    Q_u(Z^z)=Z^(−z/2) Σ_(p,S)=1 a_p χ_p(u) U(Np/Z^z).

Let H(Z) be the supremum over `|a_p|≤1` of the sum of `|M_(v^n) Q_(v^n)|²` over the chosen principal ideal labels with `Nv≪Z^(m/n)`. For z=0 the supremum is unnecessary. Then

    limsup_(Z→∞) log H(Z)/log Z
       = m/n + z + 2r(Θ_K−1/2).                              (2)

The proof is identical to the [sextic result](../2026-10-29-mobius-marked-boundary/README.md). For the lower bound use principal prime ideals v of norm `≈Z^(m/n)` with annulus disjoint from the slot annulus; the fixed class group's prime-ideal theorem supplies `≫Z^(m/n)/log Z` such primes. The masked inverse is exactly `S_W(X)+Σ_{j≥1}S_W(X/(Nv)^j)`, and a near-supremum zero plus the uniform zero-free-line bound makes the tail smaller than a Mellin Ω value of S_W(X). For the upper bound, shift the masked inverse Mellin transform to `Re s>a>Θ_K`; its variable deletion factor `∏_(p|v)(1−Np^(−s))^(−1)` is `≪(Nv)^ε` uniformly in height. If Θ_K=1, use trivial ideal counting instead. The number of v labels is `≪Z^(m/n)` and `|Q|²≪Z^z`. The fixed W ensures no base zero is hidden by its Mellin transform. The endpoint Θ_K=1/2 needs a critical-line zero: standard zero counting gives nontrivial zeros, and functional-equation symmetry implies that when Θ_K=1/2 all such zeros lie on the critical line.

Consequently a hypothetical all-row estimate `≪_ε Z^(m+ε)` at the same parameters forces

    Θ_K ≤ 1/2 + [m(1−1/n)−z]/(2r).                          (3)

This is a conditional implication. The equality (2) concerns only the n-th-power rows; it does not bound other rows, prove the all-row estimate, or supply a new zero-free region.

## A concrete quadratic threshold for Riemann ζ

For K=ℚ, n=2, S={2}, consider all positive integers u≤Y, with χ_a(u) the zero-extended quadratic residue symbol and no prime slot. An estimate

    Σ_(1≤u≤Y) |X^(−1/2) Σ_(a odd) μ(a)χ_a(u)W(a/X)|²
        ≪_ε Y^(1+ε),   X=Y^(671/1000),                       (4)

would imply, by (3), that ζ has no zeros in

    Re s > 1/2 + 250/671 = 1171/1342 ≈ 0.8725782414.         (5)

That would improve on the tracker's candidate `0.8738702` if both inputs were established. Estimate (4) is **not proved** here, and (2) shows directly that it already contains the zero-free information (5). For any target `θ>1/2`, this route requires an exponent `r/m > 1/[4(θ−1/2)]`; beating 7/8 requires `r/m>2/3`, while beating 0.8738702 requires `r/m>1250000/1869351≈0.66868127`.

The existing quadratic large sieve alone does not reach that range. Factor u uniquely as `u=a v²` with a squarefree, retain the source mask `(v,n)=1`, apply Heath-Brown's quadratic large sieve to a for each v, and sum `v≤sqrt(Y)`. The source coefficients have squared mass `≪(YX)^ε`, giving the familiar bound

    Σ_(u≤Y)|M_u(X)|² ≪_ε (Y+X sqrt(Y))(YX)^ε.                (6)

Thus this direct route gives O(Y) only for `X≤sqrt(Y)` up to losses, where (3) extracts no nontrivial ζ zero-free boundary. The gap between exponents 1/2 and 0.66868 is the new analytic work, not a parameter optimization.

**Independent review:** Families checked the zero masks, the fixed representative convention and the quadratic large-sieve split. They noted that the lower bound requires one representative for every principal ideal (or a positive-density supply of principal primes), not merely at most one; the statement above includes that requirement.
