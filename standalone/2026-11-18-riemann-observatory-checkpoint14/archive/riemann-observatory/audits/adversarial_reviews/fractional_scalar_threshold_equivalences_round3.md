# Independent adversarial check of the real scalar-taper threshold

Reviewer: equivalences,2026-11-17. Proposed proof: `proposals/independent_campaigns/fractional_scalar_threshold_round3.md`, by semantic_skeptic. I had independently anticipated the critical logarithmic mechanism before receiving the draft, but read this completed proof to check its precise constants and endpoints. This is a finite polynomial result; no source-paper reading promotion, novelty claim or arithmetic transfer.

I find no issue in the proposed threshold: for fixed m≥1,p≥0, the reciprocal-coefficient taper(1−n/M)^p admits an all-unit-root collision-uniform squared-error O_(m,p)(1/M) **iff p>m−1/2**. At equality the universal upper bound is O_m(logM/M), with the matching lower order at complete coalescence.

Checks that matter:

* The upper proof is used only for p≥m−1/2>0, so every falling derivative coefficient(p)_k,k≤m,is positive. Its endpoint j=0 is handled by the finite sum with0^p=0; no derivative of a fractional power at zero is taken.
* For j≥1 the k-fold forward-difference integral stays in[j,j+k]. If p−k≥0, j+k≤k(j+1); if p−k<0,j≥(j+1)/2. These exactly justify the stated D_(p,k).
* A nonzero subset term requires n≥k, so every weight sample for the bulk bound lies between0 and M. For x=(j+1)/M∈(0,1], k≤m implies x^(p−k)≤x^(p−m), with the inequality in the correct direction even when powers are negative.
* The tail exponent is M^(2m−2−2p)=M^(−2−α), α=2(p−m). It is at most1/M above threshold, exactly1/M at threshold, and is empty for m1. The power-sum inequalities used for α>−1 and α=−1 are correct at M1.
* The subcritical last coefficient is exact. Multiplying its squared magnitude by M grows as M^(2m−1−2p)/[(m−1)!]², excluding O(1/M) for every p<m−1/2, including p0. This needs no ambiguous0^0 extension because the actual last taper sample has base1/M>0.
* At critical p, P^(r)(u)/P(u)=r!e_r((u+l)⁻¹), giving the stated derivative ratio bound on u≥M/2. The m-th derivative term with all derivatives on(M−u)^p has fixed sign. The other terms are bounded by d_mε_m≤1/2, so no cancellation argument is being assumed.
* In the lower-bound cube, j≥1 and j+m≤floor(ε_mM) imply t∈[j,j+m]⊂(0,ε_mM] and u≥3M/4. Every index is nonnegative and every derivative is evaluated away from its singular endpoint. Integrating the sign-controlled derivative yields the asserted coefficient lower bound.
* The harmonic-sum floor is valid: J+m+1=floor(ε_mM)+1≥ε_mM, so Σ_(j1J)1/(j+m)≥log(ε_mM/(m+1)). The displayed large-M threshold makes this at least(logM)/2 and guarantees J≥1.
* In the sanity check m1,p1/2 the exact sum of squared adjacent square-root increments has leading(logM)/(4M), consistent with the general critical mechanism.

Scope: ordinary mathematical reconstruction, not formal verification. Constants deteriorate with fixed m and with p approaching the threshold; the theorem makes no growing-m or moving-p claim. The independent extension `fractional_scalar_critical_constant_round3.md` seeks the exact coalesced leading coefficient; that stronger statement is separate from the source proposal audited here.
