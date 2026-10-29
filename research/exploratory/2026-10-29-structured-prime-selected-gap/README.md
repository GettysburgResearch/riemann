# The structured-prime moment and the selected-row gap

**Status:** A source-qualified optimization of the structured prime component, not a full Möbius-inverse estimate or a zero-free region. It imports [Xu–Sang v2, §7](https://arxiv.org/abs/2610.17675v2) and, only in the explicitly conditional refinement below, a PR94 selected-row count. It does not independently validate those inputs or claim that an unproved joint moment fails.

Let Y be the sixth-power-free row scale. For a fixed smooth annular V, define the normalized long-prime component

    A_Y(u)=Y^(−1/2) Σ_{π good prime} V(Nπ/Y) χ_u(π).

Xu–Sang Theorem 1.2 gives for the squarefree sixth-order rows, with the source's fixed S, masks and smoothness assumptions,

    Σ_{u} |A_Y(u)|² ≪ Y^{κ₆−1+ε},
    κ₆=(37−10√6)/6=2.084183762028….                            (1)

The sum may be restricted to any row subset. This is an estimate for a **fixed structured prime coefficient vector**. It does not bound the entire normalized Möbius inverse, whose squarefree composite-ideal coefficients are also present. The ordinary unrestricted sixth-order sieve gives `Y^(7/6+ε)` at this normalization, so (1) saves `13/6−κ₆=0.082482904639…` in the exponent, but remains `κ₆−2=0.084183762028…` above the desired Y-sized selected bound.

## What a fixed smooth prime slot forces

For a fixed `0<w≤1`, put P=Y^w and let the physical slot be a fixed smooth annular normalized prime sum Q_P(u), with the source's fixed S/ray phases and a single permitted finite-height parameter. Suppose selected rows satisfy

    |Q_P(u)|² ≥ P^σ,      σ=223/500=0.446.                       (2)

Xu–Sang Lemma 7.1 is printed for a fixed untwisted profile at length Y; its proof, replayed at the fixed rough length P=Y^w as in Proposition 7.2, gives in a zero bin with endpoint a

    |Q_P(u)|² ≪ P^{2a−1+O(e)+η/w}.

For fixed w>0, after choosing the bin and detector losses arbitrarily small, (2) forces

    a ≥ (1+σ)/2−o(1)=0.723−o(1).                               (3)

This conclusion requires the actual slot's coefficients and height control to match the fixed smooth-profile source lemma; it is not a statement for arbitrary row-dependent or tailored coefficients. A polynomial-height norm twist is not covered verbatim by the printed untwisted Lemma 7.1 or by Proposition 7.2's log-seminorm hypothesis. Its use here is conditional on replaying the buffered contour with the twist placed in the L-argument, `|t|≤cH₁` for a sufficiently small fixed c, a single cumulative height budget and external tail orders chosen after the fixed height power. Without that transfer, restrict the assertion to the fixed untwisted profile.

The source bin count and long-prime pointwise bound yield, for `a≤11/12`,

    #bin ≪ Y^{R(a)+ε},       R(a)=(31−32a)/(21−12a),
    |A_Y(u)|² ≪ Y^{2a−1+ε}.

For `a≥11/12`, the source uses `R(a)=2(1−a)`. Thus the bin energy exponent is

    F(a)−1,     F(a)=R(a)+2a.                                  (4)

The first-branch F is strictly concave and maximized at

    a*=(21−5√6)/12=0.729379273840…,
    2a*−1=(15−5√6)/6=0.458758547681… .                         (5)

Because the actual selection threshold in (3) is 0.723<a*, this bin argument still permits the global maximizer and gives exactly the exponent κ₆−1 in (1). Raising σ above 2a*−1 excludes the maximizer and yields some improvement, but to get exponent 1 from this argument alone requires σ≥5/6. Indeed

    F(a)−2 = 24(a−1/2)(11/12−a)/(21−12a)>0

for `1/2<a<11/12`, while F(a)=2 on the final branch. These are upper-bound optimizations, not a construction of rows with zeros or large prime sums in any bin.

## Adding an independent selected-row count

Suppose, additionally and conditionally, that the exact selected family obeys the PR94 count input

    #F ≪ Y^{α+ε},
    α=137478360780643/225606975000000=0.609371056815… .         (6)

This requires verifying that the PR94 count and Xu–Sang's zero bins, source field, row masks, scale and fixed-profile slot all apply to the *same* family. On each bin the available count is at most `min(Y^α,Y^{R(a)})`. Since `α<R(a*)`, the crossing of the two exponents is

    a_α=(31−21α)/(32−12α)
        =1368923549535499/1856560956877428
        =0.737343713097… .                                     (7)

The selection threshold 0.723 is below a_α. On its left `α+2a−1` increases, and to its right `R(a)+2a−1` decreases until 11/12, after which it equals 1. Hence the best uniform upper exponent supplied by these two separate ingredients is

    α+2a_α−1 = 1.084058483009… ,
    α+2a_α−2 = 0.084058483009… .                               (8)

This is only about 0.000125279 smaller than κ₆−1 and still well above 1. In this particular bin optimization, a Y-sized bound would require the count exponent to be at most 1/6, or a substantially stronger slot threshold; neither follows from (6). The computation identifies a limitation of these upper bounds, not an assertion that the worst bin is nonempty.

## The missing joint input

A direct way to use selection would be a mixed estimate such as

    Σ_u |A_Y(u)|² |Q_P(u)|² ≪ Y^{1+ε} P^σ,                   (9)

with the actual common smooth profiles, source masks, bin/height losses and slot quantifiers. Then (2) and positivity would give `Σ_selected |A_Y(u)|²≪Y^{1+ε}`. Xu–Sang's (1) and the isolated slot moment do not imply (9). The trivial bound `|Q_P(u)|²≪P` gives only `Y^{κ₆−1+ε}P^(1−σ)` for the selected prime energy, which is weaker. Xu–Sang Proposition 7.2 treats a bounded product of rough fixed prime profiles whose **total** prime length is comparable to the row scale; the product of a long Y-prime block with a nontrivial P-slot has total length YP and lies outside that displayed hypothesis. No cited theorem here supplies the needed mixed estimate at this asymmetric scale.

Finally, even (9) would control only the prime component of the inverse. The [short-factor obstruction](../2026-10-29-short-factor-inverse-barrier/README.md) records other rough composite coefficients with logarithmic rather than power-small mass and explains why a full inverse still needs additional joint arithmetic control. None of these comparisons rules out a future genuinely mixed estimate or a proof exploiting the physical zero constraints.

**Independent review:** Families checked the source formulas, thresholds, intersection and arithmetic exponents, and the asymmetric-product limitation. The polynomial-height twist is explicitly a source-proof transfer rather than a verbatim Xu–Sang assertion, as noted above.
