# First-window transfer: proposer reconstruction

2026-11-17. Read original arXiv2610.08965v1 Lemma2.5 pp11–12 and pinned source `Distinct839/Transfer/Main.lean`. This proof was reconstructed before reading the separately tasked transfer skeptic's notes. Local seven-point inequality is an input; this is not a claim about the zeta analytic bridge.

Let y1<...<ym be θ-separated, with labels d_i∈{1,2}. Let x_d=Σ_{r=0}^6 κ_{r,d}; assume 0≤κ_{r,1}≤κ_{r,2}, α≥0, pair weights nonnegative with Σ_{r=0}^{6−s}W_{r,r+s}^{dd'}≤2dd' for1≤s≤6. Suppose each Br^{dd'} is bounded, common-type sum Σ_{r=0}^5 Br^{dd'}(g)=0 for every real g, and the seven-point inequality holds for all permitted gaps/labels. Define prefix B≤r=Σ_{j≤r}Bj and Φ=Σ_{r=0}^4 B≤r^{d_r d_{r+1}}(g_r); let Ω bound its oscillation.

For ε≥0 and symmetric e_ij≥0 with e_ij≥K(yi−yj)²−ε on0<|i−j|≤6, the conclusion is

Σ_{0<|i−j|≤6} d_i d_j e_ij ≥ x1 n1+x2 n2−6α spread(Y)−6x2−Ω−48εm.

Empty and small m≤6 cases: rewards≤mx2≤6x2, spread≥0, Ω≥0 and ε≥0, so the asserted lower bound is nonpositive; energy is nonnegative. This includes m=0 and6, not only asymptotically long chains.

For m≥7, sum the local inequality over the m−6 contiguous frames. Four uniform bounds suffice:

1. A pair at ordered-chain distance s≤6 has the same endpoint labels wherever it appears. Its total coefficient is a subset of the nonnegative offset-s weights, hence≤2d_i d_j. Replace K² by e+ε, which is nonnegative, before applying the budget. Thus all local pair terms≤the ordered near-pair energy plus8ε times at most6m unordered pairs, giving48εm. The factor2 in the budget pays the two ordered directions; it must not be counted again.
2. Each gap is charged by at most six spans, so total pressure≤6α spread(Y).
3. For each local position r, exactly six global points fail to appear in that position across the frames. Each missed κ_{r,d}≤κ_{r,2}. Summing positions yields loss≤6Σ_rκ_{r,2}=6x2, independent of m.
4. For each frame, Σ_rBr^{d_r d_{r+1}}(g_r)=Φ(current5gapstate)−Φ(next5gapstate). The identity at the final gap uses B5=−Σ_{r≤4}Br. Adjacent labels shift with the gaps, so every interior state cancels exactly. The total correction is one endpoint difference≤Ω, not (m−6)Ω.

Subtract these three costs and the ε loss from the accumulated reward. No limit interchange occurs; all sums are finite. The constants are independent of m and the positions. The formal source allows nonsymmetric e by using(e_ij+e_ji)/2; under the source's symmetric hypothesis it gives precisely this argument, then safely adds nonnegative far pairs to state a bound with the full off-diagonal sum.

For the frozen first window, a common-knot exact check yields prefix oscillation bounds(4038,3903,0,3903,4038)/10^6, whose sum is Ω=15882/10^6. Extrema of each prefix potential occur at the14 knots or the zero exterior; summing their individual oscillations is conservative even though adjacent label choices in Φ are coupled. The typewise sum of the six Br functions vanishes because it vanishes at every common knot, interpolation is linear, and all endpoint values are zero. Code/result: `839_transfer_oscillation.py` / `.json`.

At any later use on a selected subset of points, chain distance means distance in that subset's sorted order. Reusing original indices after deleting close pairs would be a different assertion. Likewise the εm term is negligible only after proving a uniform ε→0 and an appropriate count bound; the finite transfer theorem itself does not supply those analytic facts.

Finding: no issue in this inspected finite implication. The infinite-height zeta moment/approximation steps remain outside the review.
