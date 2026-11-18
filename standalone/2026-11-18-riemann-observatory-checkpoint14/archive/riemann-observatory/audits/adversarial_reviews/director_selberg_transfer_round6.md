# Fixed Selberg-class optimal approximation under its GRH

The director read the complete proponent and independent adversarial proofs and independently reconstructed the analytic log, degree budget and distributional Mellin steps below. The conclusion is conditional on the stated fixed function's GRH. It combines the source adaptive construction with a published generalized lower theorem. No publication priority, uniformity across the class or proof of GRH is claimed.

## Exact scope and result

LetF be one fixed member of the Selberg class, with its ordinary Dirichlet-series normalization, finite gamma data, Ramanujan coefficient axiom, Euler-log prime-power bound exponent<1/2, and at most a pole of actual finite orderp at1. Assume the zero-free-half-plane formulation of its GRH: F has no zeros in Re s>1/2, with its pole at1 permitted. This includes the necessary boundary convention. Define

    Δ_(N,F)²=inf_{A(s)=Σ_{n≤N}a_n n^(-s)}
       (2π)^(-1)∫_R |1−F(1/2+it)A(1/2+it)|²/(1/4+t²)dt,

where all coefficients are arbitrary complex numbers. Then

    lim_N (logN)Δ_(N,F)²
       =Σ_{distinct nontrivialρ ofF} mρ²/|ρ|².       (A)

All signed ordinates and a possible central zero are included. The sum converges. Every parameter ofF, including degree and pole order, stays fixed whileN→∞. The distance is the full boundary norm; it imposes no vanishing jets onA at1. This result does not assert an optimal rate for prescribed reciprocal coefficients. It applies in particular to each fixedζ^k under RH, predicting k² times the correspondingζ multiplicity constant.

## 1. The adaptive analytic interface at arbitrary fixed degree

Write d=2Σ_jλ_j for the degree. The completionΛ=Q^sΠΓ(λ_js+μ_j)F(s) has poles only at0 and1 of exact orderp: gamma poles lie in Re s≤0, and the conjugate functional equation reflects any such completed pole to Re s≥1, where only the allowed pole at1 can occur. The productX=s^p(s−1)^pΛ removes those poles exactly. It adds no artificial endpoint zeros. Standard gamma growth, absolute convergence on the far right, the functional equation on the far left and finite-order strip Phragmén–Lindelöf give |X(s)|≤exp(O_F(|s|log(2+|s|))). Thus X is entire of order≤1. Under the stated GRH all its zeros lie on Re s=1/2.

For the reciprocal series, Selberg Euler-log prime coefficients equal the ordinarya_p. Their absolute sum converges for eachσ>1 by Ramanujan with a smaller positive epsilon. The higher prime powers converge absolutely because their log-coefficient exponentθ<1/2 gives2(σ−θ)>1. Exponentiating the negative log in the absolutely convergent Dirichlet-series algebra proves1/F has an ordinary absolutely convergent series onσ>1. No pointwise reciprocal coefficient estimate is needed by the construction.

The pole-canceled functionH(s)=F(s)((s−1)/(s+2))^p is holomorphic and nonzero on Re s>1/2, including1. Its analytic logarithm agrees with the Euler branch plus bounded rational logarithms on a far-right strip. Borel–Carathéodory gives O_F,η(log(2+|t|)) on a smaller disk; a fixed inner Euler disk and three circles improve this to a power<1 of that logarithm. Cauchy then gives F′/F=o(log|t|) at every fixed right offset. Functional equation and interpolation give F's subpower critical-line bound and fixed-strip bound T^(d max(1/2−σ,0)+ε), while the inverse has subpower growth on fixed lines on either side. Compact-height constants are handled separately on the selected nonzero contours.

The same-character horizontal modulus symmetry ofX centers its real Hadamard derivative as a positive Poisson sum. Stirling and the log derivative give leading term(d/2)log|t|. Integrating a fixed Poisson kernel across a slightly enlarged fixed interval, then sending its fixed offset and enlargement down after the height limit, gives the count(dh/π+o(1))log|t| for |γ−t|≤h. Averaging the logarithmic defect kernel gives good horizontal heights at either sign on every arbitrarily small fixed mesh. The possible central zero is a finite cell, not an exception to the formula.

Choose e=c0=10^-4,D=10^-4/(1+d),δ=D/100. Then k_C≤c0logT_C eventually, dD≤10^-4, and the near-cluster squared exponent loss is

    2dD+5e+2c0log1200 <0.0022<0.01.

The far loss is2(2e+c0log200)+2e<0.0017<0.01. Thus decreasing the fixed mesh with the degree retains the summable delayed tail. Constants depending onD and finite exceptional multiplicities are permitted to depend onF. There is no estimate uniform in increasing degree.

Use the retained left edge from RST048(94)–(97) rather than a far-left expansion. Poles ofF are zeros of1/F and produce no reciprocal residue. Its derivative identity and Perron identity therefore combine with the same grouped rational formula. The retained edge costsO_F(1/logN) in norm. Independently chosen signed high strips have the same complete indicator and connector estimates. Delayed collective quadrature withH=N^(1/20),K=N^(3/20) has squared powers at most−0.1499595 and−0.049958; the high-strip slowest power is at most−0.049978 becauseδ≤10^-6.

All fixed-profile, local and far proofs now apply toF. Cauchy's factorial still cancels the Hermite–Genocchi volume; the analytic prefactor is not raised to the cell multiplicity. The fixed-singleton Laurent qualification covers gaps inside hulls. Fixed optimal profiles yield mρ²/|ρ|², while the uniform tail permitsN→∞ at fixed repaired cells and then exhaustion. This proves the upper limsup in(A). These are uses of previously reconstructed complete lemmas with their hypotheses verified, rather than a presumed analogy based on terminology.

## 2. Arbitrary pole order and the exact lower model

The essential lower-model identity must retain its residue term on the *whole* positive axis. Put

    S(x)=Σ_{n≤x}a_n,
    R(x)=Res_{s=1}F(s)x^s/s,
    ψ_F(t)=R(1/t)−S(1/t),  t>0.

For t>1, S(1/t)=0 butR(1/t) generally does not vanish. Setv=logx. Forc>1, absolute Dirichlet convergence makes e^(-cv)S(e^v) an L1 function with Fourier transformF(c+it)/(c+it). Test its inverse againstφ∈C_c^∞(R). The tested integral has the factor B(s)=∫φ(v)e^(sv)dv, rapidly decaying in height uniformly on the closed strip1/2≤Re s≤c. Polynomial strip growth permits a contour shift across exactlys=1, with residue∫R(e^v)φ(v)dv. Therefore e^(-v/2)[S(e^v)−R(e^v)] is the distributional inverse Fourier transform ofF(1/2+it)/(1/2+it).

The GRH-derived subpower bound puts that multiplier inL²(dt). Plancherel and local distributional uniqueness identify it almost everywhere with the displayed locally integrable function. Consequently

    ∫_0^∞|ψ_F(t)|²dt
       =∫_R e^(-v)|S(e^v)−R(e^v)|²dv<∞,
    Mψ_F(s)=−F(s)/s

on the critical line in the L² Mellin sense. No pointwise Perron convergence, absolute boundary integral or unconditional all-degree square-integrability claim is used. De Roton's published Theorem2 requires precisely this L² membership and has no degree restriction. Its adjacent degree<4 remark is an unconditional sufficient route to membership, not a restriction of the lower theorem.

The residual1_(0,1](t)+Σ_{n≤N}a_nψ_F(nt) has transform(1−FA)/s. Continuous dilationsα∈[1/N,1] containα=1/n, so D_F(1/N)≤Δ_(N,F) in exactlydt/(2π). Apply and square the nonnegative published lower bound to obtain the reverse liminf in(A). This proves the full result in the specified coefficient space.

As a sharp pole-control test,F=ζ² hasR(x)=x(logx+2γ_E−1). Thusψ_F(t)=(2γ_E−1−logt)/t for t>1, with Mellin contribution(2γ_E−1)/(1−s)−1/(1−s)², precisely the pole part of−ζ²/s. Deleting that tail or imposing artificialA(1)=A′(1)=0 would change the model. For a pole of any order, ifF(s)/s has principal partΣ_jd_j(s−1)^(-j), the tail contributes exactly−Σ_jd_j(s−1)^(-j).

## Evidence and remaining research

Complete proponent: effective_cluster62_selberg_transfer.md. Independent adversarial reviews: witness62_selberg_adaptive.md and ../general_l_priority_and_transfer_skeptic62.md. The director independently checked the entire completion, actual pole cancellation, reciprocal absolute convergence, log branch, degree budgets, integer support and tested Mellin signs. The generalized lower result is credited to de Roton2006; the adaptive upper method to the versioned RST048 source. The full-source readings and the local displayed-identity repair in de Roton's phase proof retain separate scopes.

Next precise questions: establish publication priority against inaccessible general sequential-criterion sources; make the phase and adaptive constants effective for a selectedF; investigate when degree/conductor dependence can be controlled; formalize the explicit analytic interface and test which weaker Dirichlet-series classes satisfy it. None of these follows merely from the qualitative fixed-function theorem.
