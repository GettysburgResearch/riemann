# Printed Hardy-iteration identity: exact witness and local repair

Source: Anne de Roton, BSMF134(2006),417–445, DOI10.24033/bsmf.2516. Inspected29-page primary PDF SHA256 `6b379ceeead2c10e614bd4be268c9672f0b364fa95799a5474a9479a82f9e445`. The director inspected printedpp440–441 and reconstructed the operator calculation. Two independent reviewers inspected the typeset formula and supplied the same necessary correction. This is a counterexample to one exact displayed identity, not to Theorem2 or the paper's generalized multiplicity lower bound.

## The printed assertion and an interior witness

For Hf(t)=t^(-1)∫_0^tf(v)dv, Proposition6.4 prints the small-t term

    H^j φ_(w,k)(t)=(1−w)^(-j)∂_w^k[U_F(w)t^(-w)]+O(t^(-ε)).

The multiplier is explicitly outside the derivative, including in the last induction line. Take the actual allowed Selberg functionF=ζ, j=k=1,w=1/4,ε=1/8. These are strictly inside the printed domain ε<Re w<(1+1/d)/2 with d=1. Its phase multiplier is

    Uζ(s)=π^(1/2−s)Γ(s/2)/Γ((1−s)/2) × s/(1−s),
    Uζ(1/4)=π^(1/4)Γ(1/8)/(3Γ(3/8))>0.

Commuting the locally dominated Hardy integral with the w derivative gives the actual leading term

    ∂_w[(1−w)^(-1)Uζ(w)t^(-w)].

Its difference from the printed leading term atw=1/4 is

    (16/9)Uζ(1/4)t^(-1/4).

This cannot be O(t^(-1/8)) as t→0: the quotient is a nonzero positive constant times t^(-1/8)→∞. No RH, numerical zero location or numerical gamma evaluation is used.

## Independent Mellin-residue check

This check does not assume the source's preceding small-t asymptotic. For ψ_(w,1)(t)=1_(0,1)(t)t^(-w)log(1/t), Re w<1/2, its Mellin transform is(s−w)^(-2). The source phase operator is multiplication by Uζ(s) on the critical-line Mellin transform, and H is multiplication by(1−s)^(-1). Therefore the two inverse transforms are exactly the integrals with integrands

    Uζ(s)t^(-s)/(s−w)²,
    Uζ(s)t^(-s)/[(1−s)(s−w)²].

They are absolutely integrable on Re s=1/2. Shift each line to Re s=ε=1/8, crossing only the double pole atw=1/4. Stirling gives Uζ(σ+iy)=O((1+|y|)^(σ−1/2)) uniformly on this fixed strip. The denominators supply two or three additional inverse powers, so the horizontal connectors vanish and both shifted integrals are O(t^(-ε)). The residues are respectively∂_w[Uζ(w)t^(-w)] and∂_w[Uζ(w)t^(-w)/(1−w)]. Thus the omitted term occurs for the actual source operator and function, not merely a formal model. Endpoint values of step functions do not affect these L² identities.

## Correct formula and downstream scope

The corrected leading term is

    H^j φ_(w,k)(t)=∂_w^k[(1−w)^(-j)U_F(w)t^(-w)]+O(t^(-ε)).

For each fixed compact w-neighborhood in the stated strip, domination by v^(-Re w) times fixed log powers justifies commuting derivatives. The error under H^j retains its stated exponent because ε<1. Iterating and expanding(1−H)^(2m_F) produces∂_w^k[V_F(w)t^(-w)], exactly the expression printed in Proposition6.5. The omitted terms have lower logarithmic degree, although the same t power. After normalized fixed zero jets they contribute O(1/log(1/λ)) to the Gram limit, so the Hilbert blocks and published lower constant survive this explicit repair. This finding does not assert a gap in the resulting main theorem.

Independent evidence: [full-source reconstruction](../prefix_formula62_deroton2006_full_reading.md), [skeptic audit](../deroton2006_hardy_skeptic62.md), [second visual/operator audit](witness62_deroton2006_prop64.md). The full derivative and its Mellin check are concrete repairs. No correction-history claim beyond the pinned inspected version is made.
