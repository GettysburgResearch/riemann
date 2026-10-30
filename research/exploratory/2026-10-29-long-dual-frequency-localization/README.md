# Frequency localization in the second Poisson replay

**Status.** This is a source-qualified refinement of the [mask-preserving second-Poisson replay](../2026-10-29-mask-preserving-second-poisson.md), not an independent proof of its cited analytic inputs. It retains the original fixed ray sectors, zero masks, common Fourier-profile/height conditions, rapidly decreasing tails, and all-natural-row inverse estimate (10.2) specified there. It supplies a narrower sufficient target for the proposed 125/144 approach, not a zero-free region.

Let `P=Y^(6/5)`, localize the original good common gcd d, divisor k|d and auxiliary gcd g to norms `D₀=Y^d`, `K=Y^κ`, `G=Y^g` in the feasible source ranges, with `D₀≤Y^(7/10)` up to the source's small buffers. Let H=Y^h be one fixed original nonzero-dual annular frequency dyad satisfying

    H ≲ Y^ε P²K/(Y D₀²).                                       (1)

The phrase “nonprincipal dyadic contribution” below has the exact meaning of the cited replay: remove the artificial theta diagonal by summing the **complete signed auxiliary-g partition** first, before localizing g or applying triangle inequalities. Include all auxiliary ray classes in that cancellation; fix original source sectors throughout. Afterwards, the individual g dyads of the remaining offdiagonal can be bounded.

Subject to the cited replay's source inputs, each such frequency/g dyad, summed over d and k, is

    ≪ Y^ε [Y/K + Y (H/P)^(5/6) D₀^(5/6)/(K^(11/6)G^(5/6))]
       + O_ε(Y^ε YD₀/(P K)).                                   (2)

The last term is the separate artificial principal-restoration cost and is `O(Y^(1+ε))` in the indicated source range. In particular the entire displayed bound is within `Y^(21/20+ε)` when

    h ≤ 63/50 − d + g + (11/5)κ.                              (3)

Fixed dyadic constants and the enlargement by Y^ε are absorbed by choosing the source losses small compared with the final target loss. The number of dyads is logarithmic. There is no assertion that the signed diagonal cancels in a single g block.

## Ledger

Use the notation and inequalities (5)–(9) of the detailed source replay, including the ℓ mask divisor and the column scale

    D ≍ P/(D₀G),   T ≪ K D²G²/H ≍ K P²/(D₀²H).

For each ℓ dyad and fixed d′=d/k, the nonprincipal inner part is at most

    H/(L D) · [T + T^(1/6)D^(5/6)] Y^ε.                       (4)

As in the cited proof, the fixed t fibre absorbs the possible k,ℓ and second-Poisson divisor choices into a divisor-power loss; it is not replaced by an additional factor KL. After summing ℓ dyads with `L≥1`, multiplying by the physical outer factor `(Y/P)/(GK)` and the `≪D₀/K` possible d′, the two terms in (4) give respectively

    (Y/P)/(GK) · (D₀/K) · (H/D) · T = Y/K,
    (Y/P)/(GK) · (D₀/K) · (H/D) · T^(1/6)D^(5/6)
      = Y (H/P)^(5/6) D₀^(5/6)/(K^(11/6)G^(5/6)).          (5)

The principal restoration is bounded as in (9) of the cited replay, rather than inserted into the inverse norm. Source uniformity in H, its variable T, puncture `d′s`, ray factors and Fourier parameters remains an explicit hypothesis. Substituting the endpoint H in (1) recovers the older `Y/K+Y^(7/6)/(K D₀^(5/6)G^(5/6))`; (2) is its unspecialized frequency form.

At the fundamental `D₀=K=G=1` scale, (2) becomes

    ≪Y^ε [Y+Y(H/P)^(5/6)].                                    (6)

Thus the earlier first-Poisson theta mean controls `H≤Y^(5/4)` at `Y^(21/20)`, and the second-Poisson replay extends this to `H≤Y^(63/50)`. Relative to `Y^(21/20)`, at H=Y^(5/4) the exponent in (6) is `25/24`, a saving of `1/120`. The part of the natural dual band still requiring an improved source-qualified bound is

    Y^(63/50) < H ≲ Y^(7/5+ε).                               (7)

This is a reduction for the nonprincipal sector after the full signed g-diagonal cancellation, **not** a bound on the individual positive g=1 square. In fact the [physical frame note](../2026-10-29-gram-physical-dual-interface/README.md) records a source-conditional lower bound showing that individual square is too large at the endpoint.

In general the residual high-frequency interval is the part satisfying both

    h > 63/50−d+g+(11/5)κ,
    h ≤ 7/5+κ−2d+O(ε).                                        (8)

It can exist only when `d+g+(6/5)κ<7/50` up to small buffers. Thus frequency localization is consistent with, and refines, the already stated endpoint small-core criterion. It does not control the complementary ranges of the original physical decomposition or bypass any source/height assumption.

## A square-divisor sign check

The second-Poisson fibre contains the square of the auxiliary label. This makes the bare identity `Σ_(a²|t) μ(a)=1_(t squarefree)` tempting, but it cannot simply be inserted into the physical ledger: the original coprime projector carries the weight `μ(g)/Ng`, the ℓ and k masks and the source's smooth kernel also depend on the factorization, and the exact source phase and additional internal gcd restrictions remain. In particular the signed fibre is not established to be a unit-weight squarefree projector.

The following elementary model shows why a **weighted** square-divisor sign by itself need not have any power cancellation. For good ideals let

    c(t)=Σ_(a²|t) μ(a)/(Na) = ∏_(p²|t, p good)(1−1/Np).       (9)

Then c(t)>0 and `c(t)≳_ε (Nt)^−ε`; for example `c(p⁶)=1−1/Np`. For Re s>1 its Dirichlet series is

    Σ_(t good) c(t)/(Nt)^s = ζ_K^S(s)/ζ_K^S(2s+1).           (10)

The Euler product on the right has a simple pole, not a zero, at s=1. Thus its positive mean has a nonzero main term of order X by the ordinary ideal-counting theorem. This calculation does not claim that the physical transformed coefficient equals c(t); it isolates the exact missing arithmetic: proving a useful signed cancellation requires the actual kernel/phase/mask weights and cannot follow from the Möbius sign and square-divisor incidence alone.

**Independent review.** Literature checked that fixed-H localization commutes with complete signed diagonal cancellation, the polynomial range for the variable inverse row T, the d′ puncture, normalization, cutoff and residual wedge, conditional on the cited source uniformities. No cancellation in a single g dyad or new individual region is asserted.

Literature also checked (9)–(10), the local factors and nonzero positive mean; this does not identify the model coefficient with the physical fibre.

## Why a fixed smoothing zero does not remove the endpoint band

In the quasi-RH source's fixed radial convention, the physical row majorant is a fixed nonnegative nonzero `W∈C_c^∞((0,∞))`, and `w(z)=W(|z|²)` has self-dual Fourier transform `ŵ(y)=W̃(|y|²)`. Therefore

    W̃(0)=∫_C W(|z|²) dμ(z)>0.                                (11)

Continuity gives constants x₀,c₀>0 with `Re W̃(x)≥c₀` on `0≤x≤x₀`. If both original column norms lie in the source's fixed annulus `[aP,bP]`, choose a fixed c>0 sufficiently small in terms of a and x₀. The dual dyad `Nv≈cP²/Y` has `Nv Y/(Nr₁ Nr₂)≤x₀` throughout the physical kernel, and it lies inside (7) for all sufficiently large Y. The transform on this whole dyad is therefore bounded away from zero; Schwartz decay gives no Y-power saving there. The same conclusion holds for sufficiently small fixed perturbations of the common profiles.

This is a pointwise statement about the kernel only. The complete arithmetic expression remains signed and can cancel even when its scalar kernel is positive. A Mellin or transform zero at an isolated point does not remove this dyad, and choosing a Y-dependent highly oscillatory row profile would require a separate uniform-source and physical-detector proof.
