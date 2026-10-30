# The principal mode in a full-extension zeta detector

**Status:** A rigorous source-conditional obstruction to transferring the existing squarefree-column large sieve unchanged to full Dedekind-zeta inverse or plain coefficients. It does not rule out an alternative detector, cancellation among composite columns, or a stronger new arithmetic estimate. The cubic squarefree-column sieve is imported from De Faveri Proposition 8.1 and its fixed-ray reciprocity as in the [density proof packet](../2026-10-29-density-proof-packet/README.md).

Fix a number field K containing μ₃ and the source's fixed bad set S. Let X→∞ and let F_X be the family of cubic characters χ_p indexed by good prime ideals p with `cX/2≤Np≤cX`, where c>0 is fixed. Prime-ideal counting gives `N=#F_X ≍X/log X`. Every χ_p has finite conductor norm `≪X`, distinct p give distinct primitive characters by their good ramification support, and the corresponding cyclic cubic extensions L_p/K are distinct: a cyclic cubic field has only the two nontrivial characters χ and χ̄, both with the same good conductor support p.

In global L-functions below, χ_p denotes the primitive inducing character. Its values at good source primes agree with the original zero-extended presentation; at fixed bad primes the original presentation can delete extra Euler factors and must not be substituted into the global Artin factorization without restoring them.

Fix `0<r<1` and put D=X^r. Let P_D be the good prime ideals q in `[D,2D]`; `P=#P_D ≍D/log D`. For X large, every q∈P_D is distinct from every row prime p. Put `c_q=1/sqrt(P)`, so `Σ|c_q|²=1`. At such a q the prime coefficient of the relative-norm Dirichlet series of ζ_(L_p) is

    A_p(q) = 1+χ_p(q)+conjugate(χ_p(q)),

and the prime coefficient of its reciprocal is `−A_p(q)`. Indeed `ζ_(L_p)=ζ_K L(χ_p)L(χ̄_p)`, and q is unramified in all three factors. These are coefficients indexed by ideals q of K, not necessarily rational-prime coefficients.

Let 1 denote the constant vector on F_X. The prime response decomposes as

    (Σ_q c_q A_p(q))_(p∈F_X)
      = sqrt(P)·1 + (Σ_q c_q χ_p(q))_p
                     + (Σ_q c_q conjugate(χ_p(q)))_p.       (1)

For the two oscillating terms, finite-ray reciprocity changes `χ_p(q)` to `χ_q(p)` times a q-phase after splitting p into finitely many fixed ray classes. Both have the original zero masks, though in this disjoint prime setup the masks equal one. Proposition 8.1, or its global consequence in the density packet, gives for every fixed ε>0

    ||(Σ_q c_q χ_p(q))_p||₂²
      + ||(Σ_q c_q conjugate(χ_p(q)))_p||₂²
      ≪_ε X^ε [X+X^(1/2)D].                                (2)

The conjugate term follows by conjugating the coefficient vector. Because

    N P ≍ XD/(log X log D),
    (X+X^(1/2)D)/(NP) ≪ (log X)² (D^(−1)+X^(−1/2)),

we can choose ε<min(r,1/2)/2 in (2), so the sum of the two oscillating ℓ² norms is `o(sqrt(NP))`. The reverse triangle inequality in (1) gives

    Σ_(p∈F_X) |Σ_(q∈P_D) c_q A_p(q)|²
       ≫ N P ≫ XD/(log X log D).                              (3)

For every sufficiently small ε′>0 this is strictly larger, by a power of X, than `X^ε′[X+sqrt(X)D]`: the ratio is at least a constant times `X^(min(r,1/2)−ε′)/(log X)²`. Consequently the full-zeta prime-column operator cannot satisfy the quotient-character sieve bound `X^ε[X+sqrt(X)D]` uniformly for arbitrary coefficients. The rank-one principal mode is the obstruction. The same conclusion holds if P_D is restricted to a fixed positive-proportion smooth prime window.

This is not merely an artifact of unit normalization. On a smooth annulus, the actual centrally normalized prime-restricted full inverse block has coefficients `−D^(−1/2) W(Nq/D) A_p(q)`. Taking a nonnegative W bounded below on a fixed subinterval, the identical argument gives a second moment `≫N D/(log D)²`. It does **not** prove a lower bound for the complete annular inverse block: its composite-ideal terms may cancel the prime terms. Nor does it disprove an estimate exploiting the special Möbius convolution rather than an arbitrary-column operator norm.

## What principal-mode subtraction must preserve

For `F_p(s)=ζ_K(s)L(s,χ_p)L(s,χ̄_p)`, set

    B_p(s)=1/[L(s,χ_p)L(s,χ̄_p)],
    F_p(s)^(−1)=ζ_K(s)^(−1) B_p(s),
    F_p(s)^(−1)−ζ_K(s)^(−1)=ζ_K(s)^(−1)[B_p(s)−1].     (4)

The reciprocal identities are initially valid for Re s>1 and extend meromorphically. At a hypothetical zero ρ of ζ_K of multiplicity m, if the relative quotient is nonzero at ρ then B_p is holomorphic and nonzero there. The full reciprocal has a pole of order m, but the centered reciprocal in (4) has a pole only if `B_p−1` vanishes to order strictly less than m. Relative-family zero-density guarantees nonvanishing of the quotient for most p; it does not give the required nonvanishing or size of `B_p(ρ)−1`. In particular, subtracting the common `ζ_K^(−1)` contribution does not by itself retain a zero detector for ρ. An argument that bounds this mode using cancellation beyond Re s=σ also faces the possibility that the common reciprocal itself has a pole there. These facts identify a missing estimate, not a theorem that every centering approach must fail.

An idealized local calculation illustrates why the principal component persists in complete coefficient averages. For a good unramified q, write z=(Nq)^(−s) and average the inverse Euler polynomial over equally weighted cubic values χ(q)∈{1,ω,ω²}. One obtains

    (1/3) Σ_χ (1−z)(1−χ z)(1−χ̄ z) = (1−z)(1+z²).

If those local values were independently equidistributed for all primes, the formal averaged Euler product would be `ζ_K(2s)/[ζ_K(s)ζ_K(4s)]`. This is only a heuristic for a growing family and growing source lengths, not an asserted average or a proof of the failure of any actual full-annulus bound. It explains why a genuine common ζ_K reciprocal mode would remain problematic at a zero with real part >1/2.

## Further inputs for a full ζ_L detector

The full extension has `|D_(L_p)|=|D_K|³(Nf_p)²≪X²`, so its natural analytic-conductor base is `U=X²`, not X. A source-conditional full-family contradiction would require a detector valid for the full ζ_(L_p) and a bound for its actual inverse/plain witnesses whose Chebyshev count is `o(X/log X)` at the prescribed rectangle. An arbitrary-column quotient sieve cannot provide that bound in view of (3); a special cancellation estimate for the true composite coefficients or another mechanism would be needed.

There is also a pole issue. The truncated-inverse Gamma integral for ζ_L crosses its simple pole at 1, so the nonprincipal-entire detector cannot simply be applied unchanged. For a prescribed fixed zero ρ≠1, replacing Γ(z) by `Γ(z)(1−z/(1−ρ))` cancels the extra residue and has original-line kernel `e^(−x)(1−x/(1−ρ))`. For a row-varying selected zero ρ, controlling the factor `1/(1−ρ)` and the resulting uniform profiles is an additional requirement. No full-family detector estimate or individual zero-free region is proved here.

## The exact transfer that a full-family estimate would imply

Fix `1/2<σ<1`. Suppose one could prove, for some η,τ>0 and all sufficiently large X, that at most `O(X^(1−η))` distinct fields L_p from the above prime-label family with `Nf_p≪X` have a zero of ζ_(L_p) in `Re s≥σ`, `|Im s|≤X^τ`. Then ζ_K has no zero in `Re s≥σ` at any height. Indeed, if ζ_K(ρ)=0 at fixed ρ, both nonprincipal cubic factors in the product `ζ_(L_p)=ζ_K L(χ_p)L(χ̄_p)` are entire, so ζ_(L_p)(ρ)=0 for every p; for X large, ρ lies in the stated height window. This produces ≫X/log X distinct exceptional fields, a contradiction. For `K=Q(sqrt(−3))`, the identity `ζ_K=ζ·L(s,χ_(−3))` would consequently give the same zero-free half-plane for both the Riemann zeta function and this quadratic Dirichlet L-function. This is a conditional reduction; the stated full-family density hypothesis is not established by the quotient estimate, and (3) explains why an unchanged large-sieve proof is unavailable.
