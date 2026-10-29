# A conditional natural-label quartic field consequence at θ

**Status.** This is a source-qualified family-density deduction, not an independent zero-free theorem. It assumes de Faveri's fixed-order FHL family and large sieve, the direct full-row detector and common-profile/height replay, the quadratic Hecke large sieve and detector, and the admitted conventional interpretation of the separately staged [Dirichlet candidate](../2026-10-29-return-retune-8738694/README.md). The analytic inputs and candidate admission are not established here. No exhaustive priority claim is made.

Put K=Q(i), θ=4369347/5000000, and δ=2θ−1=1869347/2500000. Let u range over good fourth-power-free ideals Nu≤X, and retain the labels for which the source FHL character χ_u has exact order four. Its cyclic quartic class field is L_u/K. Under the stated inputs, for each ε>0 there is τ>0 such that at most

    O_ε(X^(842755/1674204+ε))                                (1)

of these distinct fields have a zero of the full ζ_(L_u) in `Re s>θ`, `|Im s|≤X^τ`. The pole at s=1 is not a zero. There are ≫X distinct fields already among squarefree good labels. All have |D_(L_u)|≪X³, so choosing X a fixed small multiple of Y^(1/3) gives a specified family of ≫Y^(1/3) fields below Y with at most `O(Y^(842755/5022612+ε))` exceptions at a sufficiently small Y-power height. This is an X-truncated natural-label family, not a claim about all cyclic quartic fields below a discriminant bound.

## The order-four factors

The source's Θ₄(X,D) applies directly to **all** fourth-free row labels and fourth-free columns, including the squarefree inverse columns. For unrestricted ordinary columns, write a=a₁v² with a₁ squarefree; retain χ_u(v²) as a row contraction for each fixed v and use Minkowski. Squaring first gives the ordinary fourth moment with divisor-bounded convolution coefficients. The t≥1 saturated detector, common β/height profile and finite Sobolev controls are the source-qualified inputs; no growing auxiliary twist or t<1 detector is used here.

For x=log_X D, the source moment exponent is

    E(x)=max{1,x,3/4+x/2,1/2+3x/4}.

The corresponding witness count exponent is f(x)=E(x)−δx. Choose

    t=3/[4(3−δ)−7],   L=2t/3,   R=842755/1674204.            (2)

The exact δ makes 1<t<3/2 and 2/3<L<1. On [L,1], the face `3/4+(1/2−δ)x` dominates and decreases; on [1,t], the face `1/2+(3/4−δ)x` dominates and increases. Their values at L and t are equal to R. For a detected zero, if r≥L use the inverse second moment. Otherwise the actual simultaneous constraint r+m≥t and m≤1/2 gives `2m≥L` and `2m≤1`, so use the ordinary fourth moment. Thus the summed zero count for χ_u is `O(X^(R+ε))` at a sufficiently small global X-power height, subject to the stated detector and profile replay. The χ_u³ factor is its complex conjugate and has the same zero count in symmetric height windows.

## The quadratic core and small scales

Every fourth-free u has a unique decomposition u=w c² with w,c squarefree, possibly sharing primes. Source multiplicativity and zero extensions give

    χ_u²(a)=χ_w²(a)·1_((a,c)=1)                               (3)

on good ideals. The additional mask only deletes Euler factors, which have no zero for Re s>0; the primitive core is χ_w². If w=1 then χ_u has order at most two, so it is excluded from this quartic field family. Otherwise the core is nonprincipal and its good conductor is w. Distinct good squarefree w give distinct cores.

At σ=θ the source-qualified fixed-field quadratic sieve/detector gives a core exception exponent

    Q=1−δ/2−δ²/2 = 4332174293591/12500000000000 < 1/2.       (4)

To use the **global X-height** with all w, choose a fixed η>0 satisfying `1/2+η<R`, and split at Nw=X^η. For Nw≤X^η, count w trivially and c by `Nc≤(X/Nw)^(1/2)`; including the individual zero-count height factor costs at most `X^(1/2+η+ε)` after choosing τ small. For Nw>X^η, the quadratic detector with cutoff W≈X is valid at height X^τ after choosing τ below η times its allowed W-power (or dyadically at W≈Nw). Partial summation of its `O(W^(Q+ε))` exceptional-core estimate yields

    Σ_{bad w; X^η<Nw≤X} (Nw)^(−1/2) ≪ X^ε,

because Q<1/2. The number of c choices per w is `≪X^(1/2+ε)(Nw)^(−1/2)`, hence the large-core contribution is `≪X^(1/2+ε)`. This counting retains shared primes w,c and does not require uniqueness of the quadratic character's natural presentation beyond the good conductor support. Take the common τ below the order-four and quadratic allowances. Both core ranges are o(X^R) after fixing η and ε sufficiently small.

## Full zeta, labels and comparison

Artin factorization uses primitive all-place factors: `ζ_L/ζ_K=L_K((χ_u)^*)L_K((χ_u²)^*)L_K((χ_u³)^*)`. These have the same zeros in Re s>0 as the original S-deleted presentations. Outside the three-factor exception set it has no zeros for Re s≥θ within the height window. The Dirichlet candidate, if admitted with its conventional semantics, makes `ζ_K=ζ·L(s,χ₋₄)` nonzero only in the **open** half-plane Re s>θ. Their product therefore gives (1) on that open rectangle; no base nonvanishing on Re s=θ is claimed.

Distinct fourth-free labels have distinct local inertia exponents at good primes and hence distinct primitive source characters. Each cyclic quartic field has two order-four generators. Squarefree good u alone supply ≫X labels and ≫X fields. The fixed S factors give `Nf(χ_u),Nf(χ_u²)≪rad(u)≤Nu`, so the conductor–discriminant formula gives |D_L|≪X³, with no need to assert a matching lower bound for nonsquarefree labels.

At fixed height de Faveri's natural-label exponent at θ is `D₄=2361255842955/4687372174364`, and its strict gap over R is

    D₄−R = 182352530781250/490476077738056641 > 0.

The positive gap remains after choosing sufficiently small height powers; it compares one named source under its stated hypotheses, not all prior work. The finite-width scalar checks and the source-to-detector matching are not a substitute for independently proving the cited analytical inputs.

**Independent review.** Families checked the direct Θ₄ moment and exact R, the quadratic core identity with shared primes, the small/large-core split and common-height order, the field fibers and discriminant upper bound, and the closed-relative/open-full-zeta deduction. The review treats the stated analytic and candidate inputs as assumptions.

## Full real-part interval

The same source-qualified argument works for every fixed `3/4<σ<7/8`. Put `δ=2σ−1∈(1/2,3/4)` and choose

    t=3/(5−4δ),  L=2t/3,
    R(δ)=(19−20δ)/[4(5−4δ)],
    Q(δ)=1−δ/2−δ²/2.                                        (5)

Here `1<t<3/2`. On `[L,1]` the exact quartic Θ₄ count exponent is `3/4+(1/2−δ)x`, which decreases; on `[1,t]` it is `1/2+(3/4−δ)x`, which increases. Their endpoint values are R(δ). The actual detector constraints give the same inverse/ordinary-fourth witness split as above, without using t<1 or imposing m=t−r.

The quadratic core of `u=w c²` is counted at exponent `max{1/2,Q(δ)}` up to an arbitrarily small loss. To see this at a global X-power height, fix η>0, handle Nw≤X^η trivially at cost `X^(1/2+η+ε)`, and choose the final height exponent below η times the quadratic detector's allowance on each larger w-dyad. For Nw>X^η, partial summation gives

    X^(1/2+ε) Σ_{bad w≤X}(Nw)^(−1/2)
       ≪ X^[max{1/2,Q(δ)}+ε],

with a logarithm absorbed when Q(δ)=1/2. The relevant margins are strictly positive throughout the interval:

    R−1/2 = 3(3−4δ)/[4(5−4δ)] > 0,
    R−Q = −[8δ³−2δ²−6δ+1]/[4(5−4δ)] > 0.            (6)

For the second inequality, δ≤3/4 gives the numerator bound `8δ³−2δ²−6δ+1≤4δ²−6δ+1<0` throughout `[1/2,3/4]`. Choose η and ε below the fixed margin, then τ below both detector allowances. Thus each fixed σ in the interval has a relative-quotient exception count `O(X^(R(δ)+ε))` for all exact-order-four natural labels Nu≤X, with ≫X fields and the same |D_L|≪X³ family scaling.

De Faveri Corollary 1.5 gives, on the same natural-label family and at fixed height,

    D₄(δ)−R(δ)
      = −(2δ−1)(4δ−3)/[4(4δ−5)(8δ²−12δ+3)] > 0.     (7)

All three factors in its denominator have the signs needed for (7) throughout the open interval. The strict gap permits a sufficiently small positive height power for comparison. This is a comparison with that named source, not a priority or unconditional claim.

If σ>θ, the assumed Dirichlet candidate makes ζ_K nonzero on the **closed** half-plane Re s≥σ, so outside the relative-exception set the full ζ_L is zero-free on that closed rectangle, with its pole at 1 excluded. At σ=θ, the base input is open and the resulting full-ζ rectangle is only `Re s>θ`, as stated above. For σ<θ, the candidate gives no base-field conclusion at σ. The complete continuum remains conditional on the source large sieve, quadratic and fourth-witness detector/profile transfers, and the candidate interpretation whenever the full-zeta conclusion is used.

**Continuum review.** Families independently verified the scalar faces and three factored gaps, quadratic-core split and height choices, and the open/closed boundary distinction. In particular R−1/2 tends to zero as σ approaches 7/8, so the losses and height are chosen separately for each fixed σ; no uniformity over the interval is asserted.
