# Independent skeptic review of the first-window finite search

Reviewer: search_skeptic subagent. Date:2026-11-17. Starting point: the original C++ source and frozen input data, without reading the parent agent's reconstruction notes. Artifact: [kristianmk/839, commit0e961ea199b425010843bc8044676d4ad29fe031](https://github.com/kristianmk/839/tree/0e961ea199b425010843bc8044676d4ad29fe031), `verifier/verify.cpp` and `certificate/inputs.json`.

**Finding classification:** independently checked with no issue found in the inspected finite-search argument. No mathematical error witness was found. This is a scoped reconstruction of the reference checker's soundness for the frozen first-window data, not a whole-paper Level3 audit and not a local Lean-kernel replay.

## Exact mathematical target and units

There are seven ordered points and six gaps. In grid coordinates let G=16384, S=2^28 and R=209009. All weights, rewards, knot ordinates and α=6219 use the common factor10^-6; the code cancels that common denominator. Multiplying a local inequality by S leaves pressure per grid step αS/G=101892096, kernel contributions W·(S K²), potential contributions S B and rewards S h.

The checker proves the inequality on the larger gap domain g≥13926 grid steps. The paper's separation17/20 corresponds to69632/5=13926.4 grid steps, so this rounding enlarges the verified domain. It cannot lose a permitted configuration.

This review treats valid lower bounds for every kernel-table cell as an input. The parent reports an independently implemented full table validation; that result was not re-derived here. The search code does not pretend to prove table soundness.

## Continuum coverage and span pruning

The root box covers [13926,R]^6. Outside it, any gap greater than R makes the total span greater than R. Nonnegative weights make all kernel contributions nonnegative. Each gap potential, over all labels and all real arguments, is bounded below by its smallest knot value or0; continuity at its zero endpoint knots makes this true also outside its tabulated support. Summing these independent lower bounds yields the code's `potentialBudget`=9902. The largest reward is the sum of all double rewards, since each double reward is at least its simple reward.

The exact frozen data satisfy

αR−G(sum double rewards+potentialBudget)=2331>0.

Consequently the span term pays every reward and potential loss whenever total span≥R, for every labelling. This justifies both the initial restriction and later pruning, without a table value for large distances.

At each remaining box let l_r≤g_r≤u_r and L=Σl_r. The span test uses L; when it does not accept, L<R. Capping an upper bound at R−L+l_r removes only points whose total span exceeds R, already covered by the universal span argument. For a pair crossing several gaps, its distance has lower bound a=Σl_r and upper bound b=min(Σu_r,R−L+a). This follows by retaining all remaining gaps at their lower bounds. It is a constraint on the feasible span≤R part, even if the rectangular box also contains some already-covered points with larger span.

Splitting [l,u] at integer floor((l+u)/2) into closed subintervals [l,m] and[m,u] covers every real point. The shared boundary causes duplication, not a gap. The conservative stack guard and the width≤1 failure branch return an error; neither silently accepts an unverified box. A success occurs only after every pending box was soundly accepted.

## Closed-cell endpoint convention and range minima

Table entry k bounds K(t)² on the **closed** cell[k/G,(k+1)/G]. An integer-grid distance q∈[a,b], b>a, therefore lies in at least one cell with index a,…,b−1, including q=b through the last cell[b−1,b]. The code's last index `max(a,b−1)` is valid. When b=a it uses cell a, which contains that single distance. It is unnecessary to include cell b when b>a. This resolves a plausible off-by-one objection.

After the span test fails, pair lower bounds are at most L<R and capped upper bounds at most R. Thus all queried indices lie in0,…,R. Sparse-table range minima use two overlapping blocks of length2^floor(log2(length)); their union covers the full interval and both blocks were populated. No unpopulated zero slot is reached by a valid query. The binary reader decodes unsigned bytes explicitly and rejects size mismatches and entries greater than S.

## Reconstruction of the label-share inequality

Fix a pair and let d_i,d_j∈{0,1} indicate double labels. Let κ be the range lower bound on S K². Relative to the all-simple pair, define D1=(W1−W0)κ plus the minimum of B1−B0 if adjacent, and D2=(W2−W0)κ plus the minimum of B2−B0 if adjacent. These are lower bounds for the corresponding actual gains because W1,W2≥W0, a condition checked in the input.

Set g=min(2D1,D2), exactly as in `basicBound`. The doubled gain is at least g(d_i+d_j):

- no double endpoints: both sides0;
- one double endpoint: doubled gain≥2D1≥g;
- two double endpoints: doubled gain≥2D2≥2g.

This remains valid for **negative** D1,D2 or g. Requiring W2≥W1 would be unnecessary; only W1,W2≥W0 is used. Assign g to each endpoint's share. After subtracting the doubled reward increases, every labelling contributes at least

Σ_i d_i[share_i−2S(h_double,i−h_simple,i)] ≥ Σ_i min(0,share_i−2SΔh_i).

The right side is exactly the code's `penalty`. Combining it with the all-simple base lower bound proves the basic acceptance test for every labelling.

The penalty is a **pointwise lower bound relative to the actual all-simple expression**, not merely relative to one particular numerical base bound. It can therefore also be added to the affine all-simple lower bound in the shortcut of `affineTest`. This resolves another plausible objection to reusing the basic-test penalty in an affine test.

## Affine tests

The kernel slope can be arbitrary; using a finite difference near the interval midpoint affects efficiency, not soundness. For slope m, the code sets c=min_k[2 table(k)−m e_k], where e_k=k+1 for m≥0 and e_k=k otherwise. For every real q in cell[k,k+1], mq+c≤2 table(k)≤2S K(q/G)². Thus its affine line is a valid lower bound throughout every covered cell.

For a potential, subtracting any proposed affine slope leaves a continuous piecewise-linear function. Its minimum on a closed interval occurs at an interval endpoint or a knot. The source evaluates exactly those points; endpoint-knot values0 are explicitly validated. Integer positions have exactly representable scaled values because S is divisible by the knot step2048. The actual continuum statement follows from linearity between those integer breakpoints, rather than an assumption that all gaps are integral.

Nonnegative pair weights preserve all lower bounds. After summation the lower expression is affine in the six gaps, and its minimum over the full rectangle is attained coordinatewise at the lower or upper endpoint according to coefficient sign. Some rectangle points may violate the span≤R constraint. Minimizing over this larger set only lowers the result, so it remains a safe bound on feasible points. Each of the128 labellings is checked unless the earlier uniform label-share shortcut already proves them all.

## Frozen-data integer bounds

This review checks the actual seven-point data, without claiming a general overflow proof for every input the parser might accept. All coordinate sums and midpoint additions are below6R or2R, far below signed32-bit limits. Before ordinary64-bit bound calculations, magnitudes are restricted to10^9; the actual maxima are substantially smaller.

An independent coarse bound for ordinary basic-test intermediates is

2·pressure·R+S[3n(n−1)Wmax+(4n+2)(n−1)Bmax+4n hmax]

=270954247700185088 <9223372036854775807.

The source's larger frozen `searchBound` is1105300692241743872 and `supportBound`459328498696192, also below that limit. These cover the source's ordinary64-bit arithmetic; potential interpolation and affine-offset calculations are much smaller. The code switches to signed128-bit before the large affine and span products.

For the seven-point affine value, |kernel slope|≤S and |kernel offset|≤S(R+3). A potential slope is at most2Bmax S (using knotStep≥1), and its offset at most Bmax S(1+2R). Summing21 pairs and6 gaps gives the independent bound

S[12Bmax+63Wmax+R(48Bmax+147Wmax+12α)]

=65990023632844486606848, vastly below2^127−1. Reward subtraction and the basic penalty remain far below the same128-bit margin. Overflow is not inferred solely from the author's guard returning true.

## Independent exact supplementary checks

`experiments/code/839_search_skeptic_checks.py` and `839_search_skeptic_harness.cpp` are separate reviewer code. The harness includes the unchanged reference source and calls its public potential and range-minimum APIs; it does not run its search.

The Python checker independently interprets potentials as exact Fraction-valued piecewise-linear functions, checks frozen conditions and the span margin, exercises all128 labels at50 sampled boxes (6400 pointwise comparisons), and includes negative gain cases. It compares204 author API queries with independent Fraction semantics, including support endpoints, degenerate ranges, the final table cell and full range minima. All checks passed. Random exact tests supplement the general derivations above; they are not used as a proof that untested boxes are sound. The machine-readable result records the actual counts and bounds.

## Limits and next steps

No full search was rerun in this reviewer track, and no zeta value, analytic second moment, local-to-global transfer or formal proof artifact was audited here. The parent independently executed the author's full finite search; that is distinct evidence. This review reconstructs the mathematical acceptance rules and their continuum coverage for the frozen data and found no issue. The next stronger step is an independent certificate-producing implementation that emits accepted leaf boxes with compact lower-bound witnesses, checked by a small independently implemented or kernel-verified replay tool.
