# The common zeta factor in a cyclic-cubic inverse detector

**Status:** Exact local identities and a conditional obstruction to a triangle-inequality proof. The argument does not assert a base-field zeta zero, does not rule out cancellation in the *full* inverse polynomial, and does not prove a zero-free region. No priority claim is made.

Let K contain μ₃ and let χ be the **primitive** nontrivial cubic Hecke character corresponding by class field theory to a cyclic cubic extension L/K. Its Euler factors are zero-extended exactly at its conductor. Then

    ζ_L(s)=ζ_K(s)L(s,χ)L(s,barχ).                         (1)

A De Faveri presentation can additionally delete fixed primes in S outside the conductor; applying (1) to that presentation requires the corresponding finite Euler correction factors. All identities below involving S-good indices are unchanged by those fixed deletions.

For a prime ideal p of K and z=Np^(−s), put `c_p=χ(p)+barχ(p)` and `e_p=χ(p)barχ(p)`, so e_p is 1 if p is unramified for χ and 0 otherwise. The exact local factor of the reciprocal is

    1/ζ_(L,p)(s)=(1−z)(1−χ(p)z)(1−barχ(p)z)
       = 1−(1+c_p)z+(c_p+e_p)z²−e_p z³.                 (2)

Thus at unramified p its coefficients at powers 1,2,3 are `−(1+c_p),1+c_p,−1`; they are respectively `−3,3,−1` at a split prime and `0,0,−1` at an inert prime. At a ramified p they are `−1,0,0`. This is the exact zero-mask convention, not an average over characters.

Let μ_K be the ideal Möbius function. At the Dirichlet-series level,

    1/ζ_L(s) = (Σ_d μ_K(d)/(Nd)^s)
               (Σ_a μ_K(a)χ(a)/(Na)^s)
               (Σ_b μ_K(b)barχ(b)/(Nb)^s).               (3)

All products converge absolutely for Re s>1. Equivalently the coefficient c_χ(j) is the convolution

    c_χ(j)= Σ_{d a b=j} μ_K(d)μ_K(a)μ_K(b)χ(a)barχ(b).   (4)

The term `a=b=1` is exactly μ_K(j), independently of χ. Other terms must be retained jointly if one hopes to exploit cancellation. For example, writing `a=h a₀,b=h b₀` with a₀,b₀,h squarefree and pairwise coprime gives

    χ(a)barχ(b)=1_(h,fχ)=1 χ(a₀)barχ(b₀).

The equal-index diagonal contributes the Euler factor `∏_p(1+e_p Np^(−2s))`; at p|fχ it is absent. This is a useful decomposition, but neither it nor the common μ_K term is an individually harmless error.

## Exact principal-mode limitation

Fix a finite S and write the S-good principal inverse block

    P_K(D)=D^(−1/2) Σ_{(j,S)=1} μ_K(j) W(Nj/D),           (5)

with a fixed smooth annular W. Suppose, conditionally, that ζ_K has a zero `ρ=β+iγ` with β>1/2. One can choose W≥0, smooth and supported in a sufficiently narrow fixed annulus, with its Mellin transform `Ŵ(ρ)≠0`. Then for every `0<η<β−1/2` there is an unbounded sequence D_j for which

    |P_K(D_j)| ≥ D_j^(β−1/2−η).                         (6)

To prove this, first remove D^(−1/2). For Re s>1, Mellin integration gives

    ∫₀^∞ [Σ_{(j,S)=1} μ_K(j) W(Nj/x)] x^(−s−1) dx
      = Ŵ(s) ζ_K(s)^(−1) ∏_{p∈S}(1−Np^(−s))^(−1).   (7)

The finite Euler factors are nonzero at ρ. The right side has a pole there. If the bracket were `O(x^(β−η))`, its Mellin integral would be analytic in `Re s>β−η`, contradicting that pole. Thus it is not O of that power, giving (6) on an unbounded sequence. This argument uses no zero-location assumption for any χ.

Now let a fixed cubic family contain `N(X)≫X/log X` distinct labels or fields of conductor at most X, as for the good prime labels in the [conductor-density note](../2026-10-29-cubic-conductor-density/README.md). Fix any r>0 and set `D=X^r`. Along `X_j=D_j^(1/r)`, the squared norm of the isolated common mode is

    Σ_{χ∈F(X_j)} |P_K(X_j^r)|²
      ≫ X_j^{1+r(2β−1−2η)}/log X_j.                     (8)

In particular, conditional on such a base zero, no argument can prove an `O(X^{1+ε})` bound for this isolated mode for every ε>0. A proof of that isolated bound would itself exclude ζ_K zeros with β>1/2. Consequently, applying triangle inequality or a positive majorant that separately demands this bound for the μ_K term already contains a base-field zero-free input at least as strong as that conclusion. This is the exact obstruction to simply summing independent character-family norm estimates after expanding (3).

Equation (8) is **not** a lower bound for the full cubic inverse polynomial: writing its normalized smoothed sum as `P_K(D)+R_χ(D)`, the cross terms may cancel in finite polynomial ranges. At a fixed common base zero the full reciprocal has a pole as well, but the pole coefficients and onset scales depend on χ, so (6) alone does not provide a uniform Ω-sequence simultaneously for X-dependent families. Any successful full-ζ detector must estimate the correlations of the exact convolution in (4), without assuming that the principal block is small or discarding its cancellation with the other blocks.

## Logical lifting and its missing input

If, for a fixed σ and all large X, one proves an actual sublinear count `o(#F(X))` for fields L whose **full** ζ_L has a zero with `Re s≥σ` and `|Im s|≤X^τ`, then ζ_K has no zero in `Re s≥σ`: any fixed base zero would occur in every ζ_L, and eventually lie inside the growing height window. The relative quotient `ζ_L/ζ_K` does not have this replication property. The conditional family-density theorems in the adjacent notes count nontrivial Hecke factors and hence do not supply the full-ζ count. The unproved input is a detector/moment estimate for the full regular representation and its exact coefficients (4), with common height, deleted Euler masks and conductor uniformity; assuming this input is not a proof of the lifted zero-free region.

## Why the available rectangular sieve does not immediately bound the full inverse

Already on the squarefree K-ideal indices j, (4) becomes the exact identity

    c_χ(j)=μ_K(j) Σ_{d a b=j} χ(a)barχ(b)
          =μ_K(j) Σ_{d a b=j} χ(a b²),                  (9)

where d,a,b are pairwise coprime and squarefree. The d=j,a=b=1 summand is the common μ_K mode. The other summands are coupled to that same signed mode through the common weight W(Nj/D); treating them separately loses precisely the cancellation discussed above.

For the conductor-ordered family `χ=χ_{u v²}`, reciprocity turns the inner term into a fixed ray-class phase times `χ_{a b²}(u v²)`. When b is nontrivial, its character index `a b²` is cube-free but **not squarefree**. The available conductor sieve in the adjacent note is uniform only for squarefree character indices q; it does not cover these coupled indices. The weights in (9) are also highly structured divisor convolutions, so a direct arbitrary-coefficient bound would be stronger than what the detector actually needs. A viable new input could be a mixed correlation bound for these explicit signed triples, retaining the d=j principal summand and all coprimality masks; the known rectangular sieve alone cannot simply be invoked on the collapsed index. This identifies a source-specific missing estimate, not a proof that such an estimate is impossible.

## The pole in a full-zeta detector

The source saturated detector is stated for an entire nonprincipal Hecke function. Applying its Gamma-integral verbatim to ζ_L (or its S-deleted version) crosses, in addition to z=0, the pole at `z=1−ρ`. In the S-deleted version the residue below is multiplied by the corresponding nonzero finite Euler factor at 1. Its residue is

    Y^(1−ρ) Γ(1−ρ) Res_(s=1)ζ_L(s) · C(1),

where C is the truncated full inverse. This term cannot simply be discarded. It is distinct from the coefficient-moment problem.

For the logical lifting argument, however, one may focus on one fixed putative base zero ρ≠1. Then `|ρ−1|` is a fixed positive constant. Replace Γ(z) by

    Γ(z)(z+ρ−1)/(ρ−1).

The factor kills the ζ_L pole, while the z=0 residue still vanishes at the zero ρ. The associated inverse-Mellin weight at x is `e^(−x)[1+x/(ρ−1)]`, so the unit convolution term is `1+o(1)` for a sufficiently large terminal scale. The extra factor changes only the fixed zero-dependent constants and polynomial vertical decay. For a detector that is uniform over arbitrary zeros ρ moving near 1, the factor `1/(ρ−1)` would instead need an explicit uniform bound. The fixed-zero observation addresses this pole issue only; it does not supply the missing full-inverse moments or their correlations.

**Independent review:** Two researchers checked the primitive-character convention, ramified local coefficients, Mellin pole argument, fixed S factors, signed-triple identity and distinction between the isolated mode and full inverse. The source presentation may have additional finite Euler deletions as stated above.
