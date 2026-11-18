# First-window kernel table: independent exact-rational reconstruction

2026-11-17. Claim scope: every one of209010 binary entries in `kristianmk/839` arXiv-v1 tag's first-window `certificate/kernel_lower.bin` is a valid lower bound for K(t)² across its entire designated cell. Exact table SHA256: `b80e5a8c70e4beb3b872dada426016bc97b0954c1a8a5eabaeb40fba49cded36`. This is a separately implemented interval reconstruction after inspecting source construction, not a blind independent discovery. It does not prove the full RH-related proportion theorem or execute Lean.

## Analytic justification

Set a=(193305,−23105,29166,13952,−21009,41052)/10^6 and

f(u)=[1+Σ_{j=1}^6 a_j cos(2πju)] 1_{[-1/2,1/2]}(u).

Since Σ|a_j|=321589/10^6<1, f≥678411/10^6 on its support. Integral f=1 because the integer cosine modes integrate to0. K(t)=∫f(u)exp(−2πiut)du is real/even on real t. Differentiation under the compact integral gives |K'|≤2π∫|u|f≤π and |K''|≤4π²∫u²f≤π². The cutoff discontinuity does not obstruct differentiating with respect to t: u and u² remain bounded on the integration support.

At a noninteger midpoint t=(2k+1)/(2H), H=16384,

r(t)=1/t+Σ_j a_j(−1)^j t/(t²−j²),

K(t)=sin(πt)r(t)/π,

K'(t)=cos(πt)r(t)+(sin(πt)/π)r'(t).

This follows directly by integrating each cosine mode (or adding its two shifted sinc functions); differentiating the rational expression gives r' as implemented. Midpoints are never integers, so no removable singularity is evaluated.

Let h=1/(2H). Certified midpoint enclosures imply |K(t)|≥A and |K'(t)|≤D. Throughout the cell |s−t|≤h, the derivative bound yields

|K'(s)|≤min(π,D+π²h).

A second application of the mean-value inequality gives

|K(s)|≥max(0,A−h min(π,D+π²h)).

In the code π is replaced by a rational upper bound, A by a rational lower bound and D by an interval upper bound, preserving the inequality. Squaring this nonnegative lower bound and multiplying by2^28 yields an exact rational; its integer floor is compared with the binary entry. No floating-point comparison is used.

## Trigonometric enclosures

Machin's identity π=16atan(1/5)−4atan(1/239) plus100 and40 alternating arctangent terms gives rigorous lower/upper rationals, then outward rounding at10^-55. The identity can be checked by tangent addition and quadrant bounds. Sine/cosine at reduced arguments in(0,π/2) use18-term lower and19-term upper Taylor sums. Alternating tails have the required signs and decrease from the truncation point; monotonicity on this reduced interval propagates the π uncertainty. Bounds are outward rounded to denominator2^100 for computational efficiency. Reducing k mod H determines the sign of cos relative to the positive sine; the shared integer-period sign cancels from the absolute values of K and K'.

## Observed result and limits

`experiments/code/independent_kernel_cells.py` ran in89.11s and certified all209010 entries, zero mismatches. `experiments/results/independent_kernel_cells.json` records the result. This provides independent exact arithmetic for **table soundness** with the analytic justification above. It is independent of the author's Python/numpy table-builder implementation and uses stronger truncations and different rounding. It does share the same mathematical cell-bound strategy, so a reviewer must check the analytic argument rather than treating implementation agreement as enough.

Separate questions remain: correctness of the local branch-and-bound search, transfer from local inequalities to all zeros, the analytic second-moment theorem, exact formal statements and Lean/compiler trust boundaries. Parent mathematical adjudication requested.

## Independent energy and final rational constant check

For any finite real cosine coefficients with ∫f=1,

C(f)=∫f²+∬|x−y|f(x)f(y)dxdy

=4/3+Σ a_j²/2+π^{-2}Σ[(-1)^j a_j/j²−a_j²/(4j²)].

To verify, set h(x)=∫|x−y|f(y)dy. On the interval h''=2f and h'(0)=0, while h(1/2)=1/2. Thus h(x)=x²+1/4+Σa_j[(-1)^j−cos(2πjx)]/(2π²j²). Integrate f·h and use cosine orthogonality, ∫x²=1/12 and ∫x²cos(2πjx)=(-1)^j/(2π²j²). This checks the entire nontrivial double integral analytically.

Exact rational Machin bounds in `cosine_window_energy_check.py` prove C(f)<266541/200000. Combining this upper bound with the stated local rewards x=54350/10^6, y=69433/10^6 and span cost b=6·6219/10^6 gives

(3−C_upper+y−x−b)/(2−2x+y)=1645064/1960733

exactly. This validates arithmetic in the first-window final proportion **conditional on** the local inequality and analytic transfer. It does not establish either premise.

A useful optimization distinction emerges directly from this formula: minimizing energy alone is a separable quadratic problem in the coefficients; the local-interaction certificate rewards also vary with the window. Therefore the best bare moment window need not maximize a bound that uses additional local interaction inequalities. The source's six-mode window has larger energy than Montgomery–Taylor but compensates through those extra inequalities. This is explanatory reconstruction, not a new discovery.

## Extension to the two other source windows

The analytic proof above depends only on a finite real cosine density on[-1/2,1/2], integral1 and positivity, not on having six modes. The second coefficient vector(122290,−45012,16241,1887,2711,3731,−5307,2982,−5153,5358)/10^6 has absolute sum0.210672; the third(200566,19,−9358,9283,−6746,8170)/10^6 has sum0.234142. Both satisfy the same derivative bounds, and their sinc/rational midpoint formulas follow term by term with ten or six terms.

The separately saved checker verified262,144 cells for each, with zero mismatches; hashes and exact positive margins are in independent_kernel_cells_second_third.json. The energy identity proved above also certifies the two source caps. The generic program checks every dimension, coefficient array and expected binary hash before using a table. No first-window computation was rerun. Full second/third branch searches remain outside these conclusions.
