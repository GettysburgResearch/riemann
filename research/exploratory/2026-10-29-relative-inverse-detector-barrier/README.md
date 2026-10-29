# The relative cubic inverse moment and detector-length barrier

**Status:** A source-qualified analysis of what the [short relative-inverse and prime-mark estimates](../2026-10-29-cubic-inverse-prime-mark/README.md) can presently imply. It does not posit that arbitrary zeros satisfy the physical prime-slot selection, and it does not prove an individual zero-free region.

Let K=Q(ω) and let χ_g be a nonprincipal cubic family character of conductor norm ≍Y, with its fixed bad factors deleted consistently. The relative product

    F_g(s)=L_S(s,χ_g)L_S(s,barχ_g)                              (1)

is entire. A zero of either factor is a zero of F_g, with no pole cancellation. Its inverse is the exact relative convolution

    F_g(s)^(−1)=Σ_{a,b good} μ(a)μ(b)χ_g(a)barχ_g(b)/(Na Nb)^s.

The analytic conductor of the product is comparable to Y² at bounded height. Applying the same buffered zero-detector construction to F_g is a standard-analytic proof obligation: use its product functional equation, both conjugate presentations in the finite buffer, original Euler masks and one cumulative frequency budget. Under that replay, if a is a bin endpoint, δ=2a−1>0, and lengths are measured in base Y, its individual pointwise bounds have the form

    |M_r|² ≪ Y^{δr+η},
    |S_m|² ≪ Y^{δ min(m,2−m)+η}.                              (2)

The reflected exponent contains 2 because both L-factors contribute a conductor of size Y. The truncated-inverse Gamma argument then supplies simultaneous witnesses

    r≤t+O(η),   r+m≥t−O(η),   m≤1+O(η),
    |M_r|²≥Y^{δr−η},  |S_m|²≥Y^{δm−η}.                        (3)

Indeed, comparing product lower and upper exponents gives `m≤1+O(η/δ)`. Thus r≥t−1−O(η), weaker than the single-character detector's `r≥t−1/2−O(η)`.

The independently checked short moment, using Wu's fixed-field GL(1) bound and the exact cubic exponent-vector diagonal, is

    Σ_g V(Ng/Y)|M_r(g)|²
       ≪ Y^{1+ε}+Y^{1/2+ε}Y^{(359/256)r}.                    (4)

It has Y-sized strength for `r<r₀=128/359≈0.356546`. With a fixed sextic prime slot of length P=Y^z, its marked version has an additional off-diagonal error `Y^{1/2+ε}Y^{(359/256)(r+z)}`, so the Y-sized marked range is even shorter: `r+z<r₀`. These are relative-inverse moments; they omit the common ζ_K factor and cannot be substituted for a full ζ_L inverse bound.

## A geometric obstruction to using (4) alone

The witness inequalities (3) do not force the inverse length into a useful positive part of (4)'s range for any choice of detector cutoff t:

* If `0<t≤r₀`, the relaxed pair `r=0,m=t` is admissible. The inverse unit block M₀=1 is consistent with the lower bound in (3), and its full-row second moment is of order Y. Chebyshev therefore gives no power saving for the number of rows.
* If `t>r₀` in the permitted bounded detector range, the relaxed pair `r=t,m=0` is admissible. It lies beyond the range where (4) gives a Y-sized inverse moment. The ordinary unit block is S₀=1, so the plain witness gives no additional selection.

Both pairs satisfy the pointwise bounds (2) as well. This is an obstruction to the **existing inequalities** and does not assert either endpoint actually occurs for a zero. It shows that a stronger inverse moment at longer lengths, a separate ordinary-product moment ruling out the short-r configuration, or an additional joint constraint on the witnesses would be needed for an unselected zero-density improvement.

A sextic slot with `|Q_P(g)|²≥P^σ_slot` can be imposed as an **extra hypothesis**. The prime-mark transfer then gives

    Σ_selected V|M_r|²
       ≤ P^(−σ_slot)[Λ(P)Σ_g V|M_r|²
                         +O(Y^{1/2+ε}(PD)^(359/256+ε))].      (5)

In the short marked range this saves P^σ_slot on selected rows. But (5) does not prove that a zero of F_g creates such a prime-slot spike. In fact, at the r=0 endpoint it reduces to the ordinary second-moment count for rows satisfying the imposed slot selection. Treating (5) as a zero detector without an independent mechanism connecting those zeros to the slot would be circular.

Nor is it enough to note that χ_g has conductor Y: the inverse in (4) is for the product F_g, whose reflection has conductor Y². Conversely, the known sharper single-character cubic conductor-density estimate already applies directly to zeros of χ_g and barχ_g; bounding their relative product does not automatically strengthen that estimate. The unresolved opportunities are a proven zero-to-slot transfer, a simultaneous longer relative-inverse/ordinary moment, or a new detector identity that excludes the two relaxed endpoint configurations.

## Numerical comparison at σ=4/5

The [source-qualified full cubic-family detector](../2026-10-29-short-cubic-conductor-detector/README.md) gives the exponent 11/14 ≈ 0.785714 for the number of rows with zeros to the right of 4/5, at a sufficiently small power of Y in height. Its independent analytic-input qualifications apply. For the squarefree-index subfamily considered here, the [unbalanced-family comparison](../2026-10-29-unbalanced-cubic-density/README.md) records the stronger existing Blomer–Goldmakher–Louvel exponent 8/11 ≈ 0.727273, with its own source and height qualifications. Union over χ and its conjugate changes only a constant.

As an illustrative comparison, even if one independently assumed a slot threshold σ_slot=223/500 and every zero row met it, (5) at the inverse unit block yields the selected-row exponent 1−(223/500)z, where the displayed Wu transfer requires z<128/359. Optimizing this **particular unit-block estimate** approaches 37739/44875 ≈ 0.840981, weaker than both preceding cubic exponents. This is not a bound on what a different prime moment or a genuinely joint zero-to-slot argument could establish. The threshold 223/500 belongs to a separate physical setup; it is not asserted here for zeros of F_g.
