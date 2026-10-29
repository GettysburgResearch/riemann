# Averaged Möbius overlaps for an inverse-oriented Gauss family

**Status:** A source-qualified positive estimate checked by two independent researchers. It imports the October 5 quasi-RH manuscript's completed-theta mean and cube inversion, and the [moving-profile Gram bound](../2026-10-29-gauss-profile-low-rank/moving-twist-overlap.md). It controls a particular projection of the Möbius coefficient vector, not its complementary part, and proves no zero-free region. The conjugate orientation and full-norm restriction below are essential.

Fix K=Q(ω), the fixed good-prime set S and a fixed finite-ray sector C. Let W,V be fixed smooth compact-annular functions, V nonzero, and ν a fixed finite ray character. On good squarefree ideals s in C define

    m_P(s)=P^(−1/2) μ(s)ν(s)W(Ns/P)(Ns/P)^(−it),
    v⁻_(P,h)(s)=P^(−1/2) γ₁(s) overline(χ_s(h)) V(Ns/P)(Ns/P)^(−1/2).

The original zero masks at `(s,h)>1` are retained. This is the inverse-oriented family; replacing `overline(χ_s(h))` by `χ_s(h)` does not give the same average estimate from the cited theorem without additional work. Choose one primary generator per good sixth-free principal ideal h with `Nh≤H`. In particular, prime h=p supplies exactly the earlier profile `v_(P,p⁵)`, because `χ_s(p)^5=overline(χ_s(p))` with zeros retained. The result covers this prime family but not the entire prior family indexed by `N rad(h)≤H`, whose full norms can be H⁵.

For every ε>0 and `1≤H≤P²`, the claimed estimate is

    Σ_(h sixth-free, Nh≤H) |⟨m_P,v⁻_(P,h)⟩|²
       ≪_ε (PH)^ε P^(−1)(H+H^(3/2))(1+|t|)^A.             (1)

Here A is a fixed profile-seminorm order after the losses and polynomial scale bounds are chosen; it is independent of h,P,t. The summation may be restricted to primes or to any subset. Unit/sector choices cost fixed constants. This improves the previously available sum of individual reflection bounds `≪P^(−1+ε)H²` for H growing by a power.

## Source matching and proof

Conjugating the moving profile in the inner product produces `μ(s) overline(γ₁(s)) χ_s(h)`. The source's Gauss identity converts the first two factors into `overline(α(s))γ₂(s)` times a unit-modulus character of a fixed finite ray group. Expand that fixed phase and the C-sector indicator into finitely many ray characters ξ. The common radial test becomes a fixed smooth annular profile, with norm twist t absorbed in its derivatives. Thus each overlap is a fixed finite linear combination of `P^(−1/2) P_h(P)` in the October 5 notation, where

    P_h(X)=X^(−1/2) Σ_(n good squarefree)
       overline(α(n)) γ₂(n) ξ(n) χ_n(h) W₀(Nn/X).           (2)

The sign of the h-character in (2) matches exactly because v⁻ contains the conjugate character. The source's `χ_n(h)` includes the same zero at common primes. Finite ray classes are handled before applying the mean, and the number of them is fixed.

The October 5 manuscript's Proposition `prop:R` and cube inversion `eq:cube-inverse`, with its auxiliary f=1, state for all polynomially bounded `H,X≥1`

    Σ_(0<Nh≪H)|T_h(X)|² ≪_ε (HX)^ε [H+H²/X],               (3)
    P_h(P)=Σ_(d good) μ(d) w_h(d)/(Nd) · T_h(P/(Nd)^3),       (4)

where `w_h(d)=overline(α(d))³ ξ(d)³ χ_d(h)³` is completely multiplicative with all zeros retained and `|w_h(d)|≤1`. Formula (4) is an exact cube-index Möbius inversion, not a triangle inequality or an assumption of pointwise orthogonality.

For `1≤C≤P^(1/3)`, split (4) at `Nd=C`. Weighted Cauchy and (3) give

    Σ_(Nh≤H)|Σ_(Nd≤C) ...|²
       ≪_ε (PH)^ε [H+H² C³/P].                              (5)

For the complementary sum, the source's explicit cubic theta coefficients and ideal counting give the uniform elementary bound

    |T_h(X)| ≪_ε X^(1/2+ε),                                  (6)

with T_h(X)=0 for X below a fixed positive constant. Indeed `|γ₂|,|Ψ_h|≤1`, and for fixed cube index b, `Σ_(Nn≈X/Nb³)(Nn)^(−1/2)≪(X/Nb³)^(1/2+ε)`; summing the extra factor `(Nb)^(−1)` uses `Σ_b (Nb)^(−5/2)<∞`. Hence, uniformly in h,

    |Σ_(Nd>C) μ(d)w_h(d)/(Nd) · T_h(P/(Nd)^3)|
       ≪_ε P^(1/2+ε) C^(−3/2).                             (7)

Summing its square over O(H) rows gives `≪(PH)^ε H P C^(−3)`. Take `C³=P/sqrt(H)`, admissible for `1≤H≤P²`. The two nontrivial terms both become H^(3/2), so (3)–(7) give `Σ_h|P_h(P)|²≪(PH)^ε(H+H^(3/2))`. With the normalization in (2) this is (1). The finite source derivative order controls the displayed t factor; the ε absorbs fixed divisor, log and dyadic losses. □

## Projection and the remaining Gram/complement questions

The preceding [Gram argument](../2026-10-29-gauss-profile-low-rank/moving-twist-overlap.md) also applies to the inverse-oriented vectors: conjugating the sextic twist leaves the tame conductor, deleted masks and diagonal mass bounds unchanged. Under its Wu/Hecke inputs, their normalized Gram matrix is uniformly conditioned for `H≤P^(128/359−η)`, for any fixed η>0. The inverse of this Gram matrix and (1) yield

    ||Proj_(span{v⁻_(P,h): Nh≤H}) m_P||²
       ≪_ε P^(−1+ε)(H+H^(3/2))(1+|t|)^A.                 (8)

At `P=Y^(6/5)`, the unrestricted source operator bound `||T_(Y,P)||²≪Y^(41/30+ε)` gives projected energy ≪Y^(1−c) throughout this Gram range; at its limiting exponent the displayed power is `Y^(8707/10770+ε)≈Y^0.8084494`. The overlap estimate itself would permit projected O(Y) up to `H≤P^(25/54)`, but the existing Gram conditioning is only proved up to `P^(128/359)`. In particular the earlier prime profiles `v_(P,p⁵)` are covered for `Np≤H` in that range. Source positivity allows any subset of these labels.

Neither (8) nor the prime-mode statement shows that these modes are the dominant or exceptional eigenspace, controls the component orthogonal to their span, or permits discarding its cross term in the full energy. The estimate is a strict improvement for this explicit inverse-oriented low-radical family, not a proof of the 61/72 moment target or a zero-free region.

**Independent reviews:** Families and High_match checked the exact Oct5 source formulas, finite ray factors and masks, coefficient orientation, full-norm restriction, short/tail split and projection exponents. They did not verify the imported theta theorem or the complementary spectral contribution.

A complementary [partial-frame argument](../2026-10-29-theta-partial-frame/README.md) combines this averaged overlap with the large-sieve upper bound and a trace count. It controls the projection onto a large selected well-conditioned spectral subspace for full-norm h up to P^(1/2), but does not control the whole profile span or its complement.

A subsequent [full Gram estimate](../2026-10-29-theta-partial-frame/full-gram.md) conditions every profile in the full-norm family Nh≤P^(1/2−δ), source-conditionally. Combined with the overlap above, it controls the **entire indexed span** at H=P^(25/54−δ), extending the prior Gershgorin/partial-frame range. This is a full-norm cutoff, not the much larger radical-only cutoff, and does not control the orthogonal complement.
