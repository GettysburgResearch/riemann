# Director adjudication: finite phase lower certificates

Date: 2026-11-17. Accepted scope: finite nonasymptotic projection inequalities, their computable fixed-zero-set error, and the interval certificates below. No RH, GRH, zero enumeration, uniform increasing-set estimate, or priority assertion is needed for the finite inequalities. These are scoped reconstructions, not whole-paper audits.

I read the full [zeta proof](prefix_formula62_effective_lower.md), the independent [beta-function construction](../chi4_effective_phase_lower_skeptic62.md), the scripts, and the previous source-phase repair. I independently checked the Mellin normalization, the cutoff orthogonality, the conjugation in the two-vector projection, cancellation of the diagonal singularity, and the error constants. I actually reran both scripts with the retained python-flint 0.9.0 environment; the outputs agreed. The arguments and analytic truncation estimates establish the bounds; numerical agreement alone would not.

## 1. Exact finite projection

Write L=log N and use the norm integral |1-F(1/2+it)A(1/2+it)|² dt/[2π(1/4+t²)], with arbitrary complex ordinary length-N coefficients. Let Δ_N denote its optimized distance. For a finite set R of actual critical-line zeros, choose derivative indices strictly below their actual multiplicities. The repaired phase construction gives vectors Y_i orthogonal to every allowed dilation α≥1/N, hence to the integer polynomial space. If G_ij=<Y_j,Y_i> and b_i=<target,Y_i>, with the inner product linear in its first argument, then for every trial column a,

    Δ_N² ≥ 2 Re(a* b) − a* G a.

No invertibility hypothesis is needed for this trial inequality. Positive definite G permits the optimized value b*G^(-1)b. A genuine zero is essential; replacing it by a nearby interior Hardy kernel destroys annihilation unless an additional coefficient estimate is paid for.

For ζ the pole is removed by the Hardy factor before applying the phase. With Hf(x)=x^(-1)∫_0^x f, P(s)=(s−1)/s, V=(1−H)²U, the target in phase coordinates is (1−H)U 1_(0,1), not the unmodified indicator. The published continuous-dilation distance Dζ(1/N) is at most Δ_N, which is at most the anchored distance d_N. These inclusions give the displayed lower bounds for both ordinary distances.

For any fixed finite R of critical zeros, the independently computed entrywise bounds in the proponent proof give

    L Δ_N² ≥ S_R − C_R/L,    L≥1,
    S_R = Σ_(ρ∈R) m_ρ²/|ρ|².

Here full multiplicity jets are used for S_R; a subset of jets remains a valid, weaker projection. C_R is explicitly given there by finite rational Hilbert-matrix inverses, gamma derivatives and certified zero separations. It need not have controlled growth as R grows. The normalized leading Gram is a direct sum of Hilbert blocks, and the trial vector G0^(-1)b0 gives the bound without asserting that the actual finite-cutoff Gram is invertible. Distinct-root oscillatory integrals are bounded by 2L^j/|γ−γ'| after integration by parts. This is a fixed-set estimate.

## 2. Small-interval cancellation and actual certificates

For a phase jet h(w,x)=V(w)x^(−w)+E(w,x), first subtract the interval (0,λ), λ=1/N, from the uncut Gram in the region Re w, Re v<1/2. The singular term is

    [1−V(w)V#(v) λ^(1−w−v)]/(1−w−v).

It is removable since V(w)V#(1−w)=1. The diagonal value is L+V'(w)/V(w), with the plus sign. The remaining integrals involve only the convergent local series on (0,λ). Taking boundary limits after this cancellation identifies the actual cutoff vectors and avoids infinite oscillatory quadrature.

For ζ, the certified zero near ordinate 111.029535543169674524656 lies between 111 and 112 in modulus. Its existence and nonzero derivative were certified in the earlier Conrey–Li replay. Only one zeroth jet is needed here. The explicit local envelopes |g(x)|≤18x² and |E(ρ,x)|≤20x² give Gram correction ≤16λ^(5/2)+80λ^5 and target correction ≤(36/5)λ^(5/2)+72λ^5. Interval gamma differentiation gives 0<V'(ρ)/V(ρ)<3. For L≥10, the resulting trial constant is <1/4000. Thus the concrete unconditional bound is

    (log N) Δ_N² ≥ 1/112² − 1/(4000 log N),    log N≥10.

The weaker C_R<0.027 bound for L≥1 is also valid. This is a small one-zero certificate, not an optimized lower estimate or a complete list of low zeros. Code: experiments/code/prefix_formula62_effective_lower_example.py.

For χ4 the elementary phase-image kernel is φ(x)=(1−cos(πx/2))/(πx/2). The interval [6.02094890469,6.02094890471] has opposite strict signs of the real completed beta function, so it contains a genuine critical zero; conjugation supplies its partner. Each vector uses derivative index zero: “two jets” in a script message means two zero vectors, not two derivatives at one zero. No simplicity or GRH is required. Here switch explicitly to the row convention G_row,ij=<Y_i,Y_j> (the transpose of the column-convention G in §1). With G_row=[[g,h],[conj(h),g]] and target row (b,conj(b)), the exact projection is

    2[g|b|²−Re(h b²)]/[g²−|h|²].

The 12-term local series, full ordinate interval, analytic factorial tails and 192-bit ball arithmetic enclose every entry and certify positive definiteness. Downward-rounded unconditional lower bounds for Δ_(N,χ4)² are 0.01463, 0.00903, 0.00665, 0.00362 at N=10,100,1000,1000000 respectively. The script scripts/chi4_phase_certificate_skeptic62.py implements the exact conjugation just stated. Root reproduced all four. A positive sign of a point evaluation or a numerical zero approximation alone would not suffice.

## 3. Effective upper/lower interface

Under RH, and only after the separate numerical global majorants and complete finite-cluster certificates of EFFECTIVE-CLUSTER62-UPPER are supplied, take R to be those clusters. If the multiplicity tail is certified by Cζ−S_R≤Θ_Y, then

    L Δ_N² ≥ Cζ−Θ_Y−C_R/L,

while the existing effective upper certificate bounds L d_N². Choose fixed Y first and N second. This closes the former missing effective-lower interface; it does not instantiate the global constants or a practical two-sided threshold. The earlier director note correctly described the then-missing lower input and is retained as historical evidence. A uniform growing-height algorithm or a universal convergence rate still needs new estimates.
