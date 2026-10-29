# The full cubic inverse retains the base pole on average

**Status:** Proposed elementary conditional implication; independent review requested. This is not a proof that a full-inverse moment bound holds and not a zero-free theorem. It uses standard cubic reciprocity and finite-order Hecke analytic estimates in the Eisenstein field, with the original zero masks. No priority claim is made.

Let K=Q(√−3), O=Z[ω], and fix a finite set S containing primes above 6 and all fixed reciprocity moduli. For each good squarefree ideal g, let χ_g be the primary cubic character with its original zero extension. Write

    1/[ζ_(K,S)(s)L_S(s,χ_g)L_S(s,barχ_g)]
        = Σ_{j good} c_g(j)/(Nj)^s,                   Re s>1,
    M_g(D)=D^(−1/2) Σ_{j good} c_g(j) W(Nj/D),

where W is a fixed smooth annular function. The product is the S-deleted ζ-function of the cyclic cubic extension for nontrivial χ_g; the finitely many trivial presentations can be removed at no relevant cost. Fix a nonnegative smooth annular V with `∫V(x)dx>0`, and average over all good squarefree g with weights V(Ng/X). Denote this normalized average by E_X.

Define the fixed multiplicative factor

    h(h₀)=∏_{p|h₀} Np/(Np+1),
    H_S(s)=∏_{p∉S} [1+(Np/(Np+1)) (Np)^(−2s)].

Then H_S converges absolutely and is nonzero for Re s>1/2. For every ε>0 and D,X≥2,

    E_X M_g(D)
      = D^(−1/2) Σ_{d,h good} μ_K(d) μ_K(h)² h(h)
            W(N(d h²)/D)
        + O_{S,V,W,ε}(X^(−1/2+ε) D^(1+ε)).          (1)

The main term has Mellin transform

    Ŵ(s) ζ_(K,S)(s)^(−1) H_S(s).                       (2)

This is the **full inverse**, not just the isolated μ_K summand. The H_S factor is nonzero throughout Re s>1/2, so it cannot remove a base ζ_K zero there.

Consequently, suppose ζ_K has a zero `ρ=β+iγ` with β>1/2. Choose once a nonnegative annular W with Ŵ(ρ)≠0. For any fixed `0<r<1/2` and `0<η<β−1/2`, there are arbitrarily large X such that, with D=X^r,

    Σ_{g squarefree good} V(Ng/X)|M_g(D)|²
       ≫ X^{1+r(2β−1−2η)}.                            (3)

Thus any uniform full-inverse moment bound `≪X^(1+ε)` for all ε>0, even only at one fixed inverse-length exponent `0<r<1/2` and all such fixed W, would itself imply the Riemann hypothesis for ζ_K. In particular, an argument proving such a bound without excluding the putative base zeros would be genuinely decisive; applying a general character-family bound to separate nonprincipal terms cannot make the common pole disappear. This is a conditional no-go theorem for the *proposed norm*, not a proof that RH is false, and not a full ζ_L zero-density estimate.

## Proof of the average

By Artin factorization and the primitive convention, for good indices

    c_g(j)=Σ_{d a b=j} μ(d)μ(a)μ(b)χ_g(a)barχ_g(b).   (4)

Take a,b squarefree (otherwise μ vanishes), set h=(a,b), a=h a₀, b=h b₀; h,a₀,b₀ are pairwise coprime. Then

    χ_g(a)barχ_g(b)=1_(g,h)=1 χ_g(a₀ b₀²).            (5)

This includes every original noncoprime zero. The term a₀=b₀=1 has row weight `1_(g,h)=1`; all other terms have a nontrivial cubic character in g after finite-ray reciprocity. The product index `a₀b₀²` has a good prime with exponent 1 or 2, so even after multiplying by a fixed S-ray character its primitive conductor has a nontrivial good-prime factor; its conductor norm is `≪N(a₀b₀)≤C D`. A common fixed ray sector determines the reciprocity phase and costs only finitely many cases.

The following two standard fixed-field estimates, detailed below, hold uniformly for good h,q with `N(hq)≤D^O(1)`:

    Σ_{g good, squarefree, (g,h)=1} V(Ng/X)
       = C_{S,V} X h(h) + O_ε(X^(1/2+ε)(Nh)^ε);     (6)
    Σ_{g good, squarefree, (g,h)=1} V(Ng/X)χ_q(g)
       ≪_ε X^(1/2+ε) (N rad(q))^(1/2+ε)(Nh)^ε     (7)

for each nonprincipal finite-order character produced in a fixed reciprocity sector. The main density C_{S,V}>0 is the same for every h. The finite S-part of the character, common ray sectors, and all original zero masks are included in the constants or the displayed h-loss.

For (6), the Dirichlet series is

    ζ_(K,S)(s)/ζ_(K,S)(2s) · ∏_{p|h}(1+Np^(−s))^(−1).

Mellin inversion and a shift to `Re s=1/2+ε` yield the pole at s=1 with factor h(h); ζ_(K,S)(2s) has an absolutely convergent reciprocal on the shifted line. The h-local factor is `≪_ε (Nh)^ε` there. For (7), expand squarefreeness by `Σ_{k²|g}μ(k)` and the h-mask by divisor inclusion–exclusion. A nonprincipal primitive finite-order Hecke character of conductor Q has a smooth ideal sum `≪_ε Q^(1/2+ε)` uniformly in its scale: shift the compactly supported Mellin transform to Re s=−ε and use the functional equation and absolute convergence at 1+ε. Additional finite Euler deletions cost a divisor bound and small powers. There are `O(X^(1/2))` k ideals; the primitive conductor is `≪N rad(q)` and stays nonprincipal because q has a good ramified prime. Fixed ray-sector characters have bounded conductor. This proves (7), including the row masks.

Applying (6)–(7) to (4), the unnormalized denominator is `C_{S,V}X+O(X^(1/2+ε))`. The diagonal a₀=b₀=1 gives the displayed main term in (1); the denominator correction costs at most `X^(−1/2+ε)D^(1/2+ε)`, already covered by the displayed error. For the off-diagonal, each character sum is `≪X^(1/2+ε)D^(1/2+ε)`, and the number of triples with `N(dab)≪D` is `≪D^(1+ε)` by the ideal divisor bound. Dividing by the family mass ≍X and the `D^(1/2)` normalization gives `O(X^(−1/2+ε)D^(1+ε))`. This proves (1).

## From a base zero to the lower bound

The Euler product in (2) is obtained by summing independently over d and squarefree h. Every factor `1+c_p Np^(−2s)` has `|c_p Np^(−2s)|<1` for Re s>1/2, and the product converges absolutely there, hence H_S is holomorphic and nonzero. If ζ_K(ρ)=0 and Ŵ(ρ)≠0, the Mellin transform of the unnormalized main sum has a pole at ρ. As in [the common-factor note](../2026-10-29-common-factor-lifting/README.md), it cannot be O(D^(β−η)), so the main term in (1) has size at least D^(β−1/2−η) along an unbounded sequence.

For any fixed r<1/2, choose ε small enough that the error in (1), with X=D^(1/r), tends to zero. Set X along this sequence. Since the main term grows by a positive fixed power of D, the average has the same lower order. Weighted Cauchy–Schwarz, `Σ_g V(Ng/X)≍X`, yields (3). □

The desired full-ζ lifting route therefore cannot obtain an `X^(1+ε)` full inverse mean-square estimate from the stated arithmetic inputs alone **unless it proves the base zero-free claim as part of that argument**. Stronger but genuinely structured estimates or a different zero-detection strategy may still be possible; no restriction on their existence is asserted.

**Independent review:** Two researchers checked the finite-ray nonprincipal character reduction, squarefree and h-mask averages, normalized error, H_S nonvanishing and Mellin/Jensen implication. The review remains conditional on the stated fixed-field reciprocity and uniform smooth Hecke estimates; it does not assert the desired full-inverse upper bound.
