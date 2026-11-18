# Director adjudication: what the prefix profile determines

Date: 2026-11-17. Accepted after independent full proofs by prefix_formula_62 and effective_cluster_62, exact coefficient checks, finite-data counterexamples, and my reconstruction below. Evidence: audits/adversarial_reviews/prefix_formula62_multiplicity_moments.md and effective_cluster62_prefix_inverse_moments.md. These are ordinary scoped proofs with classical moment-determinacy methods. No publication-priority claim is made.

## 1. Algebra and positive measure

Let W_m=Σ |ρ|^(−2) over distinct actual critical-line ζ zeros of multiplicity exactly m, counting both ordinate signs, and μ_m=m(m−1). Define the zero-sum function C(b)=Σ W_m c_m(b), where the finite cost c_m was independently proved earlier. This definition and its local analysis do not require RH. Identifying C(b) with the optimal arithmetic prefix limit does require RH and the reconstructed RST048 Theorem 5.

Put s=b/(1−b). The exact identity is

    c_m(b)=m²+4∫_0^s [P'_(m−1)(1+2u)]² du.

The integrand polynomial has nonnegative coefficients. Since

    2P'_(m−1)(1+2s)
      =μ_m Σ_(j≥0) [Π_(l=1)^j(μ_m−l(l+1))]s^j/[j!(j+1)!],

with termination at j=m−2, the b^k coefficient of c_m−m² is μ_m² p_(k−1)(μ_m). The polynomial p_(k−1) has degree k−1 and strictly positive leading coefficient binom(2k,k)/[k!(k+1)!]. In particular the first two coefficients are μ² and μ³/2. Hence the Taylor coefficients of C−C(0) determine recursively all moments of the positive measure

    ν=Σ_(m≥2) W_m μ_m² δ_(μ_m).

The source proofs give an exact finite coefficient formula, not only leading asymptotics. Root checked the normalization against m=2, for which c_2(b)=4/(1−b).

## 2. Actual zeros give enough determinacy

The unconditional unit-height zero count O(log T) implies m≤K log(2+|γ|). For some a>0 this gives Σ W_m(1+μ_m²)e^(a√μ_m)<∞. The bound |c_m−m²|≤|s| μ_m² exp(4√(μ_m|s|)) proves a locally normally convergent analytic germ at b=0 and legitimizes the triangular coefficient extraction.

The moments determine ν among all positive competitors, even if a competitor is not initially assumed to have an exponential moment. Symmetrically push ν to ±√μ. Its even moments are the moments just recovered and its odd moments vanish. Monotone convergence of the cosh series transfers a smaller finite exponential moment to any positive competitor with the same moments. The moment generating functions are analytic on a common strip, their Taylor series agree, and uniqueness of Fourier transforms gives equality of the measures. Therefore the analytic germ determines every W_m for m≥2. Finally W_1=C(0)−Σ_(m≥2)m²W_m. It does not determine individual ordinates or their allocation within a multiplicity class.

Under RH the fixed-small-window zero count, with arbitrarily small leading coefficient, strengthens this to m=o(log|γ|). Every square-root exponential moment is then finite and C is holomorphic on C\{1}. With only simple support C is constant. With bounded positive multiple support and largest index M≥2, b=1 is a pole of order 2M−3. With unbounded multiple support it is an essential singularity: in the s variable the normally convergent series is entire with nonnegative coefficients of unbounded degree, so it cannot be a polynomial. These statements concern C, not the finite-N staircase functions.

## 3. Sharp tail and finite-data limitations

For arbitrary nonnegative weights with Σm²W_m<∞ and some multiple mass, let λ=limsup W_m^(1/m)∈[0,1]. The exact Taylor radius at zero is

    r*=((1−√λ)/(1+√λ))².

It follows by the fixed-b root growth c_m(b)^(1/m)→((1+√b)/(1−√b))² and positivity of the Taylor coefficients; Tonelli converts the root test into the Taylor radius. The cases λ=0 and λ=1 are included. All-simple weights instead give a constant function with infinite radius. Synthetic height/multiplicity models with γ_m=exp(αm/2) and W_m=(1/4+exp(αm))^(−1) satisfy a weak logarithmic count yet have r*<1. They are not proposed actual zeta zeros.

Without an appropriate tail condition, even all formal moments can be indeterminate on the exact triangular lattice μ_m. The two independent proofs construct a real rapidly decreasing signed sequence from the Taylor coefficients of z² exp(−(1−z)^(−β)), 0<β<1. Smooth flatness at z=1 gives vanishing polynomial moments. Splitting signs yields distinct positive measures with equal moments; simple weights can balance C(0). These profiles need not have any analytic germ and do not contradict the actual-zero determinacy theorem.

At every finite Taylor order K there exist two finite positive profiles with the same C(0) and first K coefficients but different maximum multiplicity. Barycentric null weights on K+1 distinct triangular nodes annihilate degrees below K; split signs and adjust W_1 to balance C(0). This is an existence obstruction, not ambiguity for every datum. Positivity gives the important exception C'(0)=Σ W_m μ_m²=0 if and only if all multiple weights vanish. Arbitrarily high multiplicity with sufficiently small weight is invisible at any specified positive error tolerance on a compact range 0≤b≤r<1, even with C(0) fixed.

Finite-N prefix distances are step functions in b, with breakpoints log n/log N. Their almost-everywhere derivative is zero. Even uniform convergence on compact b intervals would not justify differentiating them to obtain the derivative of C. This is a concrete limit-order barrier to a naive computational simplicity test.

## 4. Exact arithmetic research target

Under RH and the separately adjudicated fixed-prefix theorem,

    all ζ zeros simple  ⇔  C(b)=o((1−b)^(−1)) as b↑1.

Indeed c_2 has a first-order pole, and every m≥2 term has a positive pole of order 2m−3; positivity forbids cancellation. Simple support is constant. More general polynomial endpoint bounds constrain the maximum multiplicity. This is an exact reformulation and potential quantitative target, not a proof of simplicity or an endpoint estimate furnished by the present fixed-b construction. The next publishable step would require new arithmetic control uniform near b=1, with the N→∞ limit taken first or with a proved joint regime. The observed finite costs and inverse moments do not supply that control.
