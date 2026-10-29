# Independent check of the variable-geometry outer rows

**Status:** Review of a conditional calculation in [the outer-row note](../2026-10-29-unitary-outer-rows/README.md), not an independent proof of its imported local table or an L-function zero-free region. The review found one missing quantitative reciprocal hypothesis, which was added to that note.

**What was checked:** Hu's exterior norm and finite-sector counting convention, the local upper-bound exponents from the cited table, the exact outside and row powers on both contours, the small-row rational margin, and the ordering needed to make the distant-row estimate and later height losses uniform in their real exponents. The full theta-to-Euler identity, finite ramified Gauss table, zero-free log-control theorem and trace-tail proof were not replayed.

## Local factor check

For an unramified selected prime, the source-conditional rational calculation gives `G_p/H_p = -conjugate(chi_u(p)) + O(Q^(-c))` after a fixed cutoff, for some `c>0`; it applies at `(sigma,omega,xi)=(beta+e,1/2,17/50)` and at `(2,2,z_infty)`. The unselected local factor `H_p` is bounded there, hence `G_p=O(1)`. Its bounds use only the modulus-one target and unit phases, so a finite-order twist does not change the local exponents.

For a selected prime with row valuation `j=1,...,5`, use the full source-table bound reproduced in the outer-row note. On the first contour its extra `j>=2` term gives the only potentially positive power `Q^(1-omega)=Q^(1/2)`. To check the remaining displayed `Q^sigma T_j` terms, their exponents are respectively

    -omega;  3/2-2sigma;
    2-2sigma-omega and 2-3sigma;
    5/2-3sigma-omega;  3-5sigma.

All are nonpositive at `omega=1/2`, `sigma>=B0=69991/80000`; the source's baseline and `j=1` extra terms are also nonpositive. On `(2,2,z_infty)` all displayed exponents are nonpositive. The constants may depend on the fixed real contours and local data, but not on the imaginary parts. These estimates rely on the source table, especially the extra term with no `V` saving when `j>=2`.

Because slot prime supports are disjoint, distinct selected row primes contribute at most

    product_(p selected, p|u) Q^(1/2) <= (N(uR))^(1/2).

The unselected product costs `N(uR)^epsilon` by the first-region bound, and fixed-field ideal counting gives `sum_(p in slot i) Q^(xi-1) << P_i^xi` for either stated positive `xi`. This reproduces the claimed `Z^(ell xi)` factors without dividing at zeros of the full correction. Fixed `S` and finitely many unit sectors are retained; the row norm is the **exterior ideal norm**, not the absolute norm of an arbitrary S-unit representative.

## Small and distant powers

The small-row power is `1 + 3/5 + 1/2 - 17/50 = 44/25`; replacing it by 2 is a valid enlargement for `U>=1`. Direct rational substitution gives

    h(z0-1/6) - ly/2 + 2/100 = -433393/6000000 < -1/20.

The scalar zero-free statement to the right of the family supremum alone is insufficient for this exponent. The revised note explicitly imports a reciprocal/deleted-factor bound `U^epsilon(1+|t|)^A` on the common line, including principal-denominator cases; it also imports a fixed-field numerator bound `U^(3/5+epsilon)` and trace tails. Constants and polynomial height orders may depend on the fixed target. The real margin stays common to later finite twists only if the real losses are fixed first, the target-dependent height degree is fixed next, and the height exponent is chosen last.

On `(2,2,z_infty)` the quotient of scalar L-functions is absolutely bounded, with fixed excluded factors treated consistently. The Mellin kernel and slot factor have exponent `B_abs + h z_infty`, where `B_abs=lx/2+1+ly`; ideal row counting and the row weight contribute `U^(1-z_infty+epsilon)`. For fixed `z_infty>2` that dyadic tail converges and begins beyond `U=Z^(h+zeta)`, giving

    B_abs + (h+zeta)(1+epsilon) - zeta z_infty + epsilon.

Choose the fixed `z_infty` first and then choose small real losses; a later external test order can be taken sufficiently large to integrate the finite height degree. The resulting strict margin is independent of any later fixed target twist, though thresholds and implicit constants need not be. These are estimates for the same physical probe only under the identity, normalization and source-tail hypotheses of the outer-row note.
