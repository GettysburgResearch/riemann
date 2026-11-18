# Sharp derivative cost of regularizing a phase-image indicator

This is an exact Hilbert-space calculation using classical spectral filtering. No publication novelty or RH consequence is claimed. The director derived the filter and both integrals independently before requesting two separate reviews, then checked their parameter elimination and endpoint arguments.

On the complex Hilbert spaceL²((0,∞),dx), letU be any unitary Mellin multiplier, g=U1_(0,1], and D=x∂_x with maximal weak domain. Then||g||=1 andg∉DomD. Under f↦e^(v/2)f(e^v), D is∂_v−1/2 with domainH¹(R), hence is closed and densely defined. Its critical-line Mellin multiplier is−s, s=1/2+it, with measuredt/(2π). All assertions allow merely measurable unit-modulus phase symbols.

Forτ>0 the unique minimizer of||f−g||²+τ||Df||² is

    Mfτ(s)=u(s)/[s(1+τ|s|²)].

Completing the square pointwise gives, for everyf∈DomD, the exact excess objective

    ∫(1+τ|s|²)|Mf(s)−Mfτ(s)|²dt/(2π).

The minimizer is inDomD by its extra two inverse powers. PutA=1+τ/4. The elementary integrals of(A+τt²)^(-1) and its square give

    Bτ=||Dfτ||²=1/[4sqrtτ A^(3/2)],
    Eτ=||fτ−g||²=sqrtτ(1+τ/2)/[4A^(3/2)].

The phase disappears because its modulus is1. Eτ increases strictly from0 to1 andBτ decreases from∞ to0; strictness also follows by differentiating the positive spectral integrands. For each0<ε<1 there is exactly oneτ withEτ=ε². If||f−g||≤ε, the objective identity implies||Df||²≥Bτ, with equality only atfτ. Thus this is the actual constrained Pareto frontier, not just a family of example filters.

Eliminatingτ withz=sqrt(τ/(4+τ))∈(0,1) yields the especially simple exact result:

    z+z³=2ε²,
    inf_{f∈DomD, ||f−g||≤ε}||Df||²=(1−z²)²/(8z).

In particularε times the minimum derivative norm tends1/4 asε→0. The exact product on the frontier is(1−z²)sqrt(1+z²)/4. The tolerance0 is infeasible, sinceg is outside the domain; forε≥1 the unique zero-cost minimizer isf=0. A real-valued restriction gives the same result only when the targetg is real; a unitary phase need not preserve real functions.

Normalization matters. The centered skew-adjoint generatorD+1/2 has the same domain but a different finite Pareto curve, because its multiplier is−it. It shares the small-error constant1/4. The full graph norm also shares that asymptotic by squeezing between||Df|| andsqrt(||Df||²+(1+ε)²); its exact frontier is a different parametrization. The theorem above is expressly for||Df||.

Independent proofs and checks: proposals/independent_campaigns/latest62_phase_regularization.md; prefix_formula62_phase_regularization.md; their retained numerical/symbolic controls. Analytic minimization and elementary integrals establish the theorem. Numerical checks test the formulas even for a nonsmooth phase; they are not proofs of the operator statement. This quantifies the regularization cost behind OBS-MELLIN-PHASE-DERIVATIVE-BARRIER and does not exclude an RH operator with different domain or data.
