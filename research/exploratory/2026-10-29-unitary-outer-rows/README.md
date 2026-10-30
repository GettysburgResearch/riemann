# Outer rows for the first variable-geometry unitary stage

**Status:** Conditional on Hu's physical high identity, quotient-free local factors and fixed-field Hecke bounds; it supplies the outer-range exponent calculation, not a standalone zero-free region. The numerical inequalities are Xu–Sang Appendix E. The original source preprints and the field-local Gauss table have not been fully audited here.

Use the field, family, probe and parameters of [the high-contour note](../2026-10-29-unitary-high-contour/README.md), in particular β>B₀=69991/80000, dmin=1/100, ζ=10^(−7), z₀=17/50 and h=31757/40000. Assume the physical high identity and original row masks, the quotient-free correction on the contours below, at most O(U^(1+ε)) physical rows in Nu≍U, a fixed-field convexity-type upper bound U^(3/5+ε)(1+height)^A for the nonprincipal numerator at Re w=1/2, and Hu's source tails. On the global line Re s=β+e, assume in addition the fixed-type reciprocal and deletion estimate |1/L_K^S(s,ψ conjugate(χᵤ))|≪_(ψ,e,ε) U^ε(1+|Im s|)^A, including all primitive/imprimitive presentations used on these nonprincipal-numerator rows. This estimate requires the uniform source disk and deleted-factor bounds; being to the right of β alone is not the quantitative estimate. Assume the source selected/unselected local factors give

    |H_(ψ,u,Z)(β+e+it, 1/2+iv, z₀+iw)|
          ≪ Z^(ℓ z₀+ε) U^(1/2+ε) (1+|t|+|v|+|w|)^A,       (1)
    |H_(ψ,u,Z)(2+it, 2+iv, z∞+iw)|
          ≪ Z^(ℓ z∞+ε) U^ε (1+|t|+|v|+|w|)^A,              (2)

for a fixed sufficiently large z∞>2, with finite height exponents. These are upper bounds for the **full** correction and do not divide at its local zeros. Fixed-prime exclusions, finite sectors, bounded nonprincipal rows and the same principal normalization are included in the hypotheses. Then the contributions from U≤Z^dmin and from U>Z^(h+ζ) are each Oψ(Z^(C_b(β)−c)) after the usual choice of small losses and the late height cutoff, for some c>0 common to the later finite-order twists in the fixed type orbit.

## Small rows

Put s on β+e, w on 1/2 and z on z₀. Since β>B₀>87/100, this contour is inside the first Euler region with a fixed margin; the reciprocal uses the global family boundary. The outside Mellin scales together with the slot factor in (1) are

    C_b(β) + e + h(z₀−1/6) − lᵧ/2.

The row count, numerator, correction and Poisson row weight contribute at most U^(1+3/5+1/2−z₀+ε)=U^(44/25+ε), which is at most U^(2+ε). For the stated geometry exact rational calculation gives

    h(z₀−1/6) − lᵧ/2 + 2dmin = −433393/6000000 < −1/20.

Thus summing logarithmically many dyads with U≤Z^dmin leaves a fixed saving after choosing e and ε small. This includes any bounded exceptional rows with nonprincipal numerator; the separate principal Kummer class is not included.

## Distant rows

Choose absolute lines Re s=Re w=2 and Re z=z∞. The scalar L-factors are bounded on these lines after the fixed excluded factors are handled. Inserting (2), ideal row counting and the Poisson row weight into Hu's physical Mellin factor gives for U≍Z^d

    ≪ Z^(B_abs+h z∞+ε) U^(1−z∞+ε),
    B_abs=lₓ/2+1+lᵧ.

Summing geometrically over U>Z^(h+ζ) yields

    ≪ Z^[B_abs+(h+ζ)(1+ε)−ζ z∞+ε].

All real parameters other than z∞ are fixed. Since z∞ may be any fixed sufficiently large positive number, choose it so that the last exponent is less than C_b(B₀)−1, for instance by taking z∞>(B_abs+h+ζ−C_b(B₀)+2)/ζ. This choice is made before the external decay order. The vertical Mellin bounds at that fixed line, the absolute row convergence and the source trace tails justify the shift and summation. A fixed finite number of sector components and logarithmic normalization cost only Z^ε. □

## Source-table reduction of the correction bounds

Assume the full local formulas and ramified table stated in [the first-region calculation](../2026-10-29-unitary-first-euler-region/README.md). At an unramified selected prime on either contour, the explicit cancellation in [the numerator interface](../2026-10-28-hu-numerator-interface/README.md) gives G_p/H_p=−conjugate(χᵤ(p))+O(Q^(−c)) for some c>0; here |W|≪Q^(−1/2), so its proof applies. After the fixed cutoff |H_p| is bounded on both contours, hence |G_p|≪1. At a ramified selected prime, the same table gives

    |G_p| ≪ Q^(−ω)+Q^σ[|R|+1_(j=1)Q^(1−σ−ω−6ξ)
                                 +1_(j≥2)Q^(1−σ−ω)+T_j],

with T_j as in the first-region note. On the small-row contour, σ≥B₀ and ω=1/2: the one potentially growing term is Q^(1−ω)=Q^(1/2), while every T_j term after Q^σ is O(1). On the absolute contour σ=ω=2 and ξ=z∞>2, all terms are O(1). Thus selected factors are bounded by Q^(1/2) at row primes on the first contour and by O(1) at every prime on the second.

The first-region argument bounds the unselected product by U^ε after enlarging S; the same estimate applies to the absolute contour. For each selected prime tuple, the distinct row-prime factors contribute at most ∏_(p|u)Q^(1/2)≤U^(1/2). Ideal counting and the original annular windows give, for each slot, Σ_(p in slot)Q^(ξ−1)≪Z^(ℓᵢξ); a fixed finite number of slots contributes Z^(ℓξ), with a small loss for fixed support constants. The quotient-free tuple sum therefore gives (1) and (2). These deductions retain the complete table, including the j≥2 term omitted in an earlier draft; they remain conditional on the field/sector realization of that table.

The tail order must remain independent of the internal profile orders, and the normalizing prime-window mass must be common to the same probe. The physical identity, local field matching and target-family uniformity remain source inputs.
