# An inverse-moment target for the 125/144 boundary

**Status.** This is a precise research reduction, not a proof of the target estimate or of a new zero-free region. The partial dyad control below is conditional on the cited physical Poisson identities, paper 5's all-row inverse estimate and the signed mask-preserving replay. The small-divisor core is open. No detector or arbitrary-number-field claim is used.

Let `E=ℚ(ω)`, let S be the fixed finite good-prime set in the source, and select the fixed smooth annular profile `W(x)=sqrt(x) W₀(x)`, where W₀ is the nonnegative compact-annular profile with Mellin transform zero-free on `Re s>0` constructed in the [sixth-power sector note](../2026-10-29-mobius-marked-boundary/README.md). If desired, shrink and translate its compact logarithmic support to lie in `(1,2)`; its Mellin transform remains zero-free in `Re s>0`. This choice ensures that `W(Na/P)/sqrt(Na)=P^(−1/2)W₀(Na/P)`, exactly matching the sector identity; zero-freeness of an arbitrary Mellin transform for W would not by itself establish the needed shifted zero-freeness. Fix one nonnegative `V∈C_c^∞((0,∞))` that is strictly positive on a nonempty open interval. For `P=Y^(6/5)` define the all-row **smooth-shell** moment

    M(Y)= Σ_(u good) V(Nu/Y)
      | Σ_(a good) μ_E(a) χ_a(u) W(Na/P)/sqrt(Na) |².       (1)

Rows use the source's zero masks and the primary representative of each good principal ideal. For every good ideal `(v)`, the sixth power `v⁶` is independent of the choice of generator and is its primary representative, so every allowed sixth-power row is included. The empty prime-slot convention is in force. Unit/ray multiplicities are fixed, and a finite sector partition is permitted when applying the cited reciprocity formulas.

The following estimate would suffice:

    M(Y) ≪_ε Y^(21/20+ε)   for every fixed ε>0.             (2)

Write Θ_E for the supremum of the real parts of nontrivial zeros of ζ_E. The reviewed sixth-power-row identity gives the exact growth exponent

    limsup_(Y→∞) log M_sixth(Y)/log Y
       = 1/6 + (12/5)(Θ_E−1/2).                            (3)

Here `M_sixth` is the nonnegative sub-sum of (1) over `u=v⁶`, including the original good-prime masks. The sector note proves this exponent for rows below Y; its same upper bound applies to this shell, and its lower Ω proof applies by choosing v in a fixed prime annulus whose sixth powers land in an interval where V is bounded below. This uses only a constant rescaling of the v annulus. Thus (2), applied to that sub-sum, would force

    Θ_E ≤ 1/2 + (5/12)(21/20−1/6)
        = 125/144 = 0.8680555555….                        (4)

Equivalently ζ_E would have no nontrivial zero with real part greater than `125/144`. The factorization `ζ_E=ζ·L(s,χ_{−3})` gives the same boundary for both ζ and the Dirichlet L-function `L(s,χ_{−3})`. This extraction does not require a detector, any other character family, or a claim that the source benchmark is attained. The exact limsup uses the nonvanishing Mellin profile and the standard reciprocal-ζ analytic input stated in the sector note.

The sharper isolated Lean candidate currently has bound `4369347/5000000=0.8738694`, subject to the separate tracker admission and semantic status described in its [packet](../2026-10-29-return-retune-8738694/README.md). The numerical improvement in (4) would be

    4369347/5000000 − 125/144
       = 261623/45000000 = 0.0058138444….                 (5)

Even a smaller improvement needs less than a `Y^(1+ε)` moment: the current boundary corresponds via (3) to the exponent `19949123/18750000 = 1.0639532266…`. Any valid bound for (1) with exponent strictly below that number would already improve the ζ_E boundary. The source sixth-free inverse estimate, extended to all rows with the original moving masks, currently gives only `M(Y)≪Y^(7/6+ε)`; it does not prove (2).

## The remaining dyadic core

In the fixed-sector signed dual expansion, write `Nd=Y^d` for the original column gcd, `Nk=Y^κ` for its mask divisor, and `Ng=Y^g` for the auxiliary projector divisor. The reviewed [mask-preserving second-Poisson reduction](../2026-10-29-mask-preserving-second-poisson.md) conditionally bounds each relevant offdiagonal dyad by

    Y^ε [Y^(1−κ)+Y^(7/6−5d/6−5g/6−κ)]

plus the separately controlled principal-restoration error. The physical theta diagonal cancels only after recombining the signed auxiliary projector over all auxiliary g-ray classes and norm dyads; it must not be removed from separate positive g-majorants. The cited deduction uses source identities, inverse means and uniform smooth-profile calculus, and remains source qualified.

Therefore all dyads outside

    d+g+(6/5)κ < 7/50                                     (6)

are bounded by `Y^(21/20+ε)`; equality is harmless with the usual ε losses. Their logarithmic number is absorbed by ε, and source tails and the larger-gcd range have their separate bounds. To establish (2) by this route it remains to control, **for each fixed original column ray sector**, the signed sum over the small-divisor core (6), with its original coupled masks, profiles and phases, by `Y^(21/20+ε)`. Equivalently one may bound the sum of absolute values of these finitely many sector contributions. Cancellation across different original column sectors is insufficient for the sector-by-sector Cauchy argument. For comparison, merely beating the candidate boundary by this route would require addressing the smaller core `d+g+(6/5)κ<1925877/15625000=0.123256128`, with a strict exponent margin. The special point `d=g=κ=0` still yields `Y^(7/6)` from the existing inverse input. A suitable signed aggregate bound for the core would suffice; no such bound is claimed here. The proof of the partial reduction must preserve the cancellation ordering and all cited source hypotheses.

**Independent review.** Families and High_match checked the zero-free-Mellin profile normalization, primary sixth-power row inclusion, exact sixth-power extraction, fractions, `7/50` core and the use of the unsplit full inverse moment. The source-qualified partial dyad bound and the unproved core retain their stated limitations.
