# Director adjudication: what combined density bounds do and do not control

17 November 2026. I read the complete proponent proof density63_combined_frontier.md, its independent density63_independent_counting_review.md and the exact source theorem/branch statements, then independently checked the layer exponents, finite meshes and both all-height counting constructions. The cached Lean query formal63_palomar_fullcurve_query.json actually printed the two named full-curve declarations and their axiom lists, exactly propext, Classical.choice and Quot.sound, with exit0 and unchanged pinned module. Its quantifier scope is separate from the earlier smooth39/17 query. These are consequences of the specified inputs and positive-count countermodels, not new bounds on actual zeta zeros or counterexamples to its explicit formula.

## 1. The exact positive weighted bottleneck

Let L=log T, y=L(β−1/2), a=1/2, and let μ_T count right-hand zero copies with0<γ≤T and y≥a. Put D_T(y)=μ_T([y,L/2]), r_T(y)=e^(2y)D_T(y)/T and M_T=∫e^(2y)/(1+y²)dμ_T. The exact layer identity is

    M_T/T=(4/5)r_T(a)
       +∫_a^(L/2) [2−2y/(1+y²)]r_T(y)/(1+y²)dy.

The bracket is between1 and2. This controls the absolute majorant used to bound the BGSTB far pairs by O(L M_T); it is not a necessary condition for cancellation in the signed pair sum. Even D_T(a)=o(T) and local uniform convergence r_T→0 leave a tail-tightness question.

If a source exponent E(σ) has a strictly positive gap2(1−σ)−E(σ) on a fixed compact slab, a fixed finite horizontal mesh gives a power saving for its contribution to M_T. The mesh is chosen before T; no unjustified moving ε or continuum of implicit constants is used. Palomar's exact right branch is3(1−σ)/(2σ) for σ>3/4, giving a positive gap throughout that open range. Thus every fixed compact slab inside(3/4,1) is removed. Its value at exactly3/4 is9/16; this strict join must not be filled by taking a threshold from the right. Pintz's exponent is stronger than this branch above9/10 and weaker below, on its proof-valid range. A separate uniform near-one input, such as the stated no-power-loss upper estimate or the quoted Halász–Turán bound combined with Vinogradov–Korobov, is required to remove the entire range β≥3/4+δ rather than only compact slabs. The deeper proof of those external upper-tail inputs retains its separate source scope.

## 2. The precise short-window range

For Ye's Theorem1.2 and2/3≤b≤1, the relevant local count exponent is b times

    B(σ)=3(1−σ)/(2−σ)          through σ=7/10,
          15(1−σ)/(3+5σ)        from7/10 to a fixed v just above3/4.

The maximum weighted layer exponent below v is

    E_b(v)=max{2/5+9b/13,
               2v−1+15b(1−v)/(3+5v)}.

The first branch is increasing and the second is convex on the stated intervals. At v=3/4 the second value is1/2+5b/9, but the7/10 layer becomes critical first: b=13/15. Therefore, with a sufficiently small fixed v−3/4 and the separate upper-tail input, every single comparable-height interval of length O(T^b) has weighted o(T) for fixed0<b<13/15. For b<2/3 use positivity and containment in a2/3 window. Endpoint and strict-threshold shifts are controlled explicitly. Covering a full block costs T^(1−b) windows and supplies no saving over the lower strip from these estimates. A local o(T) is not summable by itself.

The earlier3/5-window fourth-moment corollary also improves quantitatively: below fixed v≥3/4 its weighted exponent is1−2(1−v)/3, with the small horizontal layer costing O(T^(4/5)/log T). This strengthens the earlier valid1−(1−v)/2 bound, but does not change the full-block obstruction.

## 3. Simultaneous all-height countermodels

These are one fixed positive multiset at all heights, not independently chosen finite-T arrays. At large t put right-hand points on

    β_c(t)=1/2+(log t)^(-3/4),
    β_j(t)=3/4+1/log t,

with counting rates

    λ_c(t)=(1+sqrt(log t))exp(−2(log t)^(1/4)),
    λ_j(t)=(e^(-2)/32)t^(-1/2)(log t)².

Mark the integral rate's integer crossings, then add same-height reflected points and negative-height conjugates. Both rates decrease below1, giving bounded local marks. Critical-line fillers can attain the Riemann–von Mangoldt main count with O(log T) error and the unit-height O(log T) bound. All points can be simple. The off-line count is o(T), so the model also satisfies the numerical lower proportions for critical and simple zeros.

The independent proof checks every inspected fixed and local count, including threshold dependence, all real starts and the exact Palomar join. The high-range counts vanish. Floor errors are bounded under integration by parts against the monotone weight. After t=uT, the two normalized weighted integrands tend respectively to1 and(1/2)u^(-1/2), with integrable domination; each contributes1. Thus

    D_T(1/2)=o(T),   r_T→0 locally uniformly,
    M_T/T→2 along all real heights T→∞.

Mass escapes both through scaled displacement(log T)^(1/4) near the critical line and through the moving right approach to3/4. A fixed zero-free cutoff well above these curves does not exclude the models. They do not impose the explicit formula, the signed pair-correlation identity or a large Dirichlet-sum trigger.

A separate lacunary block model at β=7/10 has about X^(3/5)(log X)²/25 right points in a window of length X^(13/15), with X=4^n. It meets the same count envelopes and local bounds, yet its single-window weighted mass divided by T tends to1 along those blocks. This proves sharpness of13/15 as an implication of the specified inequalities, not as a claimed sharp threshold for actual zeta.

## 4. An actionable sufficient missing lemma

After an accepted upper-tail input removes β≥3/4+δ, restrict μ_T accordingly. A sufficient new arithmetic estimate is D_T(a)=o(T) together with

    (1/Y)∫_Y^(2Y)r_T(y)dy≪Y^(1−κ)

for a fixed κ>0 and a constant uniform in Y,T. Each dyadic tail then contributes O(Y^(−κ)), giving uniform integrability and hence M_T=o(T). A genuinely signed far-pair estimate is another route. The inspected density inputs give neither. This precise limitation does not affect the separately verified actual-zeta simple-critical proportion route, whose proof does not assume the BGSTB absolute weighted-density premise.
