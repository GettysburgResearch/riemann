# Independent review of the all-order finite cover

This is an exact scalar and witness-domain review, conditional on the moving-twist moment, common-profile/height interface and short-cutoff detector stated in [README](README.md). It does not prove those analytic inputs or a new individual zero-free region.

The certificate checks the maximum f of the three moment faces at the corners of each b-interval, each chosen x-interval and, for n≥21, h=1/n∈[0,1/21]. Each individual face is separately affine in b,h,x, so its maximum over such a box is attained at a corner. The fact that f is a maximum causes no difficulty: f≤R is equivalent to all three face inequalities. The 100 b-intervals cover [0,1/2], including their common endpoints.

For a fixed certificate cutoff t∈[1/2,3/2], the modes cover the full feasible witness set r≤t, m≤1/2, r+m≥t as follows.

* `inverse`: r≥t−1/2, so the inverse second-moment argument lies in the certified interval [t−1/2,t].
* `second`: either r≥t/2 or m≥t/2. In the latter case m≤1/2≤t. Thus the full inverse or ordinary **second-moment** exponent f lies in [t/2,t]. The ordinary estimate is the general squarefree-kernel/Minkowski bound f(m); the orthogonal face f₀(m) alone need not apply when b>0.
* `fourth`: either r≥2t/3 or 2m≥2t/3. Because 2m≤1, both the inverse exponent f(r) and fourth-witness exponent f(2m) are tested inside [2t/3,max(t,1)]. No equality m=t−r is assumed.
* `trivial`: the source labels in the b-dyad number ≪X^(1−b+ε), which is ≤X^(R+ε) when 1−b_left≤R; choose the common height loss afterward.

The script selects t=1/2 in multiple `second` cells, while the short detector requires t>1/2. Fix any κ>0, replace these cutoffs by 1/2+κ, and absorb the O(κ) changes in the Lipschitz face bounds and witness overflows into the prescribed ε. Select κ and the detector losses first, then τ. For each fixed n and field there are finitely many cells and profile degrees, so a single sufficiently small τ works for all cells; no uniformity of τ in n or K follows. In the formal n≥21 limiting check h=0 is used only as an endpoint for the affine inequality, not as a character family or a uniform-in-n analytic estimate.

The latest exact cover was run successfully for h∈[1/20,1/11] at R=29/50 and h∈[0,1/21] at R=14/25. These cover n=11,…,20 and n≥21 respectively; all 100 b-cells pass in each block. The limiting t=1/2 occurs in 20 and 19 cells respectively and is handled by the perturbation above. The named de Faveri comparison is also positive in each range: D_n=(12n²−38n+5)/(21n²−80n+50) is decreasing for n≥4, with derivative `−6(3n−10)(9n−25)/(21n²−80n+50)²`; `D₂₀−29/50=36/3425`, and `D_n>4/7`, whose limiting gap above 14/25 is 2/175. These comparisons have a positive fixed gap after which the polynomial-height loss can be chosen small.
