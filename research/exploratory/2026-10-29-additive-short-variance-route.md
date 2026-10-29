# An additive short-interval route to a zeta half-plane

**Status.** This is a different, conditional arithmetic route, not a new zero-free region. Its missing input is a fixed-power bound for the additive short-interval variance of the actual Möbius function. The moment sources in the current tracker concern different multiplicative character averages; no transfer to the required additive variance is proved here.

Fix `0<λ<1`, set `H=X^λ`, and let `ψ∈C_c^∞((0,1))` satisfy `∫ψ=1`. Define

    S_{X,H}(x)=Σ_{n≥1} μ(n) ψ((n−x)/H),
    V(X,H)=∫_{X−H}^{2X+H} |S_{X,H}(x)|² dx.                 (1)

Suppose that for some fixed `0≤η≤2` and every ε>0 one can prove

    V(X,X^λ) ≪_ε X^(1+ε) X^(λη)                              (2)

uniformly as X→∞. Then ζ has no zeros in

    Re s > max{λ, 1−λ(1−η/2)}.                               (3)

For instance, a square-root variance `η=1` at `λ=3/10` would imply `Re s>17/20=0.85`, a substantial improvement over the separately staged θ≈0.8738694 boundary. The required estimate (2) is **not proved** here; in particular, taking η=1 is a strong additive correlation hypothesis, not a consequence of the present tracker bounds.

## Derivation

Choose a nonzero `V∈C_c^∞((1,2))` whose Mellin transform `V̂(s)=∫₀^∞V(u)u^s du/u` is zero-free for `Re s>0`. The fixed profile W in [the power-row note](2026-10-29-power-row-spectral-boundary/README.md) has such a transform. If its compact support lies in `[a,b]⊂(0,∞)`, choose L large and c>0 so that `V(x)=W(c x^L)` is supported strictly inside (1,2); then `V̂(s)=L^(−1)c^(−s/L)Ŵ(s/L)`, retaining zero-freeness. Integrate (1) against `V(x/X)`. Changing variables in each summand and using the smoothness of V gives

    ∫ S_{X,H}(x)V(x/X) dx
       = H Σ_n μ(n)V(n/X) + O(H²).                            (4)

The error is uniform for H≤X: only O(X) n occur, and each profile differs by `O(H/X)`. Cauchy–Schwarz and (2) bound the left side by `O_ε(X^(1+ε)H^(η/2))`. Therefore

    Σ_n μ(n)V(n/X)
       ≪_ε X^(1+ε) H^(η/2−1) + H.                            (5)

Initially for `Re s>1`, Mellin inversion gives

    ∫₀^∞ [Σ_n μ(n)V(n/X)] X^(−s) dX/X = V̂(s)/ζ(s).          (6)

The left side extends holomorphically to the **open** half-plane to the right of (3), by (5), arbitrary ε and the compact support at small X. Since `V̂` has no zeros there, (6) rules out every zero of ζ in that half-plane. The conclusion makes no assertion at the boundary. The pole of ζ at 1 produces a zero of its reciprocal and is harmless. No assumption on zeros or finite-height detector is used in this implication.

## The new input and a precise limitation

Expanding (1) gives a signed additive-correlation problem. In particular, its offdiagonal terms involve `μ(n)μ(m)` with `|n−m|≪H`, weighted by the overlap of two translates of ψ. The desired `X H^(1+ε)` bound for η=1 requires cancellation in that coupled sum. The quadratic and sextic large-sieve inputs used elsewhere in this repository instead bound multiplicative-character matrices against arbitrary coefficient vectors. Their abstract operator norms alone cannot imply (2): for a fixed large X and H, set coefficients `a_n=(−1)^floor(n/H)` on `[X−H,2X+H]`. Their cumulative sums on that interval are O(H), and all such arbitrary coefficients still obey those large-sieve inequalities, but for a positive proportion of x the corresponding smooth interval sum has magnitude ≫H; its variance is ≫XH². A proof for μ must use arithmetic structure beyond the coefficient-independent sieve norm. This finite-scale model is not asserted to be a multiplicative function or a counterexample for μ.

An explicit sufficient shifted-correlation input is as follows. Define

    K_{X,H}(n,m)=H^(−1) ∫_{X−H}^{2X+H}
       ψ((n−x)/H) overline(ψ((m−x)/H)) dx.                   (7)

It is uniformly bounded, vanishes unless `|n−m|≪H`, and forces n,m≪X for H≤X. The exact expansion is

    V(X,H)=H Σ_n μ(n)² K_{X,H}(n,n)
       + H Σ_{0<|h|≪H} Σ_n μ(n)μ(n+h) K_{X,H}(n,n+h).       (8)

The diagonal is `O(XH)`. Thus a uniform bound for every nonzero integer `|h|≪X^λ`,

    Σ_n μ(n)μ(n+h) K_{X,H}(n,n+h) ≪_ε X^(1−λ+ε),             (9)

would imply the η=1 estimate (2). For λ=3/10 this asks for `X^(7/10+ε)` cancellation uniformly in a growing family of shifts, with the specified smooth boundary weights. It is a sufficient but stronger condition: cancellation after summing h would also suffice. Neither (9) nor its aggregate form is established by the multiplicative source moments cited in this workspace.

The implication (3) also makes the difficulty concrete. At λ=3/10, any proof of square-root variance would itself establish the displayed `17/20` zero-free half-plane. The existing source-specific estimates have not been matched to the requisite additive shifted correlations, and no fixed-power saving for (2) is derived here.

## Comparison with short-interval sources

In a [targeted, nonexhaustive check](2026-10-29-additive-short-variance-prior-art.md), no unconditional integer-Möbius theorem was found that supplies the required `XH^(1+ε)` variance at `H=X^(3/10)`. Matomäki and Radziwiłł's [Theorem 1](https://arxiv.org/abs/1501.04585) gives powerful almost-all short-interval cancellation with explicit logarithmic/subpower errors, but those errors do not yield the square-root-scale variance here. Ng's [Theorem 1](https://www.cs.uleth.ca/~nathanng/RESEARCH/mobiusshort.pdf) gives a random-model sharp-interval variance under a strong uniform Möbius-tuple correlation hypothesis; its stated range at `H=X^(3/10)` requires the tuple error exponent strictly below 7/10. Results for the squarefree indicator μ² or Möbius over polynomial rings do not directly apply to signed integer Möbius sums. The cited sources have not been exhaustively searched for every possible later refinement.

**Independent review.** Literature checked the Mellin-profile rescaling, `O(H²)` error, Cauchy and open-half-plane exponents including endpoint η values, shifted-correlation sufficient condition, and the finite block model. The external variance estimate remains unproved here.
