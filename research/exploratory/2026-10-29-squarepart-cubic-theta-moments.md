# Cubic theta moments after fixing the squarefree part

**Status.** These are source-qualified moment bounds for a fixed dyadic square-part slice, not a full inverse-moment estimate or an individual zero-free region. They use de Faveri's [cubic FHL large sieve](https://arxiv.org/abs/2610.04045) and the completed-theta expansion, original zero masks, finite ray sectors and uniform profiles in [the square-part stratification](2026-10-29-squarepart-stratified-tail/README.md). Their exact physical/source calibration is an imported input.

Write each good sixth-free ideal uniquely as `b=w v²`, where w is squarefree and v is cube-free. The two may share primes. Fix `Nb≈B`, `Nv≈V`; then `Nw≪B/V²` and the sum over possible w has `O((B/V²)Y^ε)` terms in a fixed polynomial range. For fixed source k, f and profile, the completed theta sums obey

    Σ_(b in slice) |T_{bk}(X;f)|²
       ≪ Y^ε (B/V²) Θ₃(V,X),                                 (1)
    Σ_(b in slice) |T_{bk}(X;f)|⁴
       ≪ Y^ε (B/V²) Θ₃(V,X²),                                (2)

where

    Θ₃(V,D) ≪ (VD)^ε [V+D+(VD)^(2/3)].                       (3)

The same bounds apply to the fixed log-scale derivative profile. All small powers depend on fixed seminorm orders, the field and the finite sector data. These bounds can be combined by a pointwise minimum with the pre-existing unstratified and fixed-v bounds; (1)–(2) themselves do not assert an improved final cutoff.

## Proof and local factors

Fix w before averaging v. On good indices, sextic-symbol multiplicativity gives

    χ_n(bk)=χ_n(wk) χ_n(v)²,                                 (4)

including zeros. Since `χ_n(v)²` is the cubic residue symbol, its matrix is the cubic FHL matrix of de Faveri after the fixed finite-ray normalization and, where necessary, transposition/conjugation. Both the n-index and v-index are cube-free in the applications. Their shared-prime zero masks are precisely the original zeros in (4); no `(w,v)=1` assumption is needed. The factor `χ_n(wk)` and the source f-mask are common column multipliers after fixing w and k.

In the completed-theta expansion fix its cube index q. Its v-dependent row factor is

    χ_q(bk)³ = χ_q(wk)³ χ_q(v)^6,
    χ_q(v)^6 = 1_{(q,v)=1}.                                  (5)

This is a bounded row contraction. Apply it before enlarging the v set, never as a v-dependent column coefficient. The remaining squarefree n-polynomial has length `≪X/(Nq)³` and coefficient squared mass `≪Y^ε`; Θ₃ therefore gives its v-row ℓ² norm squared `≪Y^ε Θ₃(V,X)`.

For the fourth moment, square this fixed-q n-polynomial. Its new column index `m=n₁n₂` has prime exponents at most two and is cube-free, its norm is `≪X²/(Nq)^6`, and fixed-divisor bounds give total squared coefficient mass `≪Y^ε`. The cubic character factor is exactly `χ_m(v)²`, including all overlap zeros. Apply Θ₃ with column length X², taking the square root after the row ℓ² estimate. This bounds the fourth power of the fixed-q row ℓ⁴ norm by `Y^ε Θ₃(V,X²)`.

Finally use row-space ℓ² or ℓ⁴ Minkowski over q. The source coefficient carries `1/Nq`, whose sum over `Nq≪X^(1/3)` is logarithmic; its other q phases and the fixed f,k zeros have modulus at most one. Sum the resulting nonnegative estimates over the `≪B/V²` possible w ideals. The annular, Fourier-separated profiles and their log derivatives are fixed uniformly in w,v,q before this enlargement, as required by the source interface. This proves (1)–(2) subject to the cited analytic and matching inputs.
