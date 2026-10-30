# A quadratic Hecke-family density bound from the fourth witness

**Status.** This is a source-qualified fixed-field consequence of the quadratic large sieve and the buffered zero detector. It is a family-density result, not an individual zero-free region or a priority claim. For rational quadratic characters the same exponent already follows from Corrigan–Zhao, with an explicit height factor; see below. No exhaustive comparison for general number fields is claimed.

Fix a number field K, a finite bad-prime set S and a quadratic Hecke family satisfying the exact hypotheses of [Goldmakher–Louvel, Theorem 1.1](https://arxiv.org/abs/1112.1642), including its finite reciprocity classes, primitive-character and zero-extension conventions. Assume the associated good squarefree labels u satisfy `Nf(χ_u)≪Nu`, their deleted Euler radical has norm `≪Nu`, and all nonunit good labels give nonprincipal primitive characters. These properties hold for the source's Fisher–Friedberg presentation with its specified local data; the precise family match is an input. Fix `1/2<σ<1` and put `δ=2σ−1`, `h=1−δ=2(1−σ)`.

For each ε>0 there is τ>0 such that

    Σ_{u good squarefree; Nu≤X} N(σ,X^τ;χ_u)
      ≪_{K,S,σ,ε} X^[3h/(2+h)+ε].                             (1)

Here N counts zeros of the primitive inducing function with multiplicity, and τ is chosen after the fixed detector, profile and ε losses. Good squarefree labels have ≫X distinct primitive characters when the good conductor support is u, so this implies a density-one rectangle for that specified family. This is a natural-label bound, not a claim about all quadratic Hecke characters ordered by conductor.

## Moments and optimization

Goldmakher–Louvel's Theorem 1.1 gives the squarefree-row/squarefree-column quadratic operator bound `≪(XD)^ε(X+D)`. The theorem is printed with the two indices in the opposite orientation; transposition and adjoint duality give the same ℓ² operator norm in the row orientation used here, with fixed reciprocity-sector phases retained. It applies to the normalized squarefree Möbius inverse block. For the fourth moment of an ordinary block, square the block and write its column ideal uniquely as `a=a₁v²` with a₁ squarefree. At fixed v, χ_u(v²) is a row contraction, including all overlap zeros; the common a₁ coefficient vector has squared mass `≪X^ε/(Nv)²`, by divisor bounds. Minkowski and `Σ1/Nv≪log X` recover the same `X+D` bracket for the fourth moment at `D=N²`. The conjugate presentation is handled by conjugating the entire common coefficient vector.

For the detector, use the standard fixed-field Hecke assumptions and the [reviewed buffered long-cutoff proof](../2026-10-29-general-long-detector/README.md). In a fixed bin, simultaneous saturated inverse and ordinary witnesses obey `0≤r≤t`, `0≤m≤1/2`, and `r+m≥t`, up to arbitrarily small fixed losses. After the common-profile Sobolev step, the inverse second moment and ordinary fourth moment yield count exponents

    f(r), f(2m),   f(x)=max{1−δx,hx}.                            (2)

Take

    t=3/(2+h),       L=2t/3=2/(2+h),       R=3h/(2+h).         (3)

For `0<h<1`, `1<t<3/2` and `L<1`. On `[L,1]`, f is the decreasing face `1−δx`; on `[1,t]` it is the increasing face hx. Their values at L and t are equal to R. If r≥L use the inverse witness. If r<L then `2m≥2(t−r)>L` and `2m≤1`, so use the ordinary fourth moment. All dyadic, bin, height, endpoint and individual zero-count losses are absorbed by choosing them in the order specified above. This proves (1) subject to the named source and detector inputs.

The earlier quadratic detector calculation using only the ordinary second moment gives `Q=1−δ/2−δ²/2`; the strict gain is

    Q−R = h²(1−h)/[2(2+h)] > 0.                                (4)

At σ=4/5, R=1/2 versus Q=13/25. At `θ=4369347/5000000`, R=`1891959/5630653≈0.33601058` versus Q=`4332174293591/12500000000000≈0.346574`.

## Scope of higher generic mixed moments

Let `v=1/(2+h)`, so `1/3<v<1/2`, `t*=3v`, and `R=f(2v)=f(3v)`. A fixed mixed monomial `M^aS^b` has normalized product length `ar+bm`; after factoring square parts, fixed-power divisor bounds and the original row contractions, the same generic quadratic sieve gives scalar exponent `f(ar+bm)`. For every cutoff `t≥1`, an admissible relaxed witness makes all these exponents at least R:

* If `1≤t≤3v`, take `(r,m)=(2v,v)`. Every nonzero integer combination is kv with `k=2a+b≥1`. At k=1, `f₀(v)−R=(1−h)/(2+h)>0`; at k=2, f₀=R; for k≥3, the increasing face hx is at least `h·3v=R`.
* If `t≥3v`, take `(r,m)=(t,0)`. Every monomial with a≥1 has exponent at least `h at≥R`, and every ordinary-only monomial has exponent `f(0)=1≥R`.

Thus no fixed finite collection of **generic** mixed monomial estimates from the same large sieve improves the scalar minimax. These are feasible points in a relaxation, not actual rows or zeros; arithmetic cancellation, stronger moment inputs or detector constraints could still improve the result.

## Comparison and field-core consequences

For K=Q, [Corrigan–Zhao, Theorem 1.4](https://arxiv.org/abs/2211.00260) already bounds the full primitive quadratic Dirichlet family by

    (QT)^ε (Q³T⁴)^[(1−σ)/(2−σ)],

among other bounds. Its fixed-height conductor exponent is exactly (1), and it has explicit height dependence. Hence (1) is not a new rational quadratic density theorem. Their rational result does not by itself imply (1) over an arbitrary fixed K; no exhaustive general-K priority search has been completed.

For natural quartic labels `u=w c²`, the quadratic core is indexed by squarefree w and has at most `≪(X/Nw)^(1/2+ε)` presentations. A small-label/global-height split and partial summation therefore turn a core exponent R into `max{1/2,R}` for the full natural family. The same calculation applies to the quadratic power in the natural sextic family. At θ the improved core exponent R≈0.336 is below 1/2, so the natural-family multiplicity still costs X^(1/2+ε): the existing quartic and sextic full-field exponents do not improve merely from (1). On squarefree-label subfamilies the multiplicity is absent, but in the examples already analyzed the remaining higher-order factor still dominates. The full-zeta statements additionally require their own base-field nonvanishing input; (1) does not supply it.
