# Director adjudication: an explicit tapered prime array for the factorial target

17 November 2026. I independently derived the proposed array and its residue/tail mechanism, then read both complete proofs: jump_factorial_prime_array63_proponent.md and generator63_tapered_prime_array_skeptic.md. The upper proofs use independently organized Hadamard estimates. The lower proofs use two different previously checked constructions, Burnol's cutoff vectors and the discrete compact tests. I checked their full-line estimates, pole multiplicities, coefficient and anchor normalizations and order of limits. The source comparison mangoldt_taper63_priority.md credits Selberg's derivative formula for the Riesz residue mechanism, Balazard for the general closure obstruction and earlier approximation papers for related norm methods. A bounded search found no exact matching statement in the inspected sources; publication priority remains open.

## 1. The theorem and its target

Fix an integer k≥2. In the unit-step space S⊂L²([1,∞),dx/x²), define R_k on cell [n,n+1) by

    R_k(n)=k log(q!)+kq log k−log(n!),    q=floor(n/k), 0!=1.

Put h(s)=k^(1−s)−1, F_k(s)=ζ(s)h(s), T_k(s)=M R_k(s)=−F'_k(s)/s. The norm in Mellin coordinates is L²(dt/(2π)) on Re s=1/2. The function R_k is O_k(log(2+x)); it is the first jump generator of the bounded periodic Nyman vector, divided by i.

Let Λ be von Mangoldt, Λ(1)=0, and set

    w_k(d)=k 1_(k|d)Λ(d/k)−Λ(d)+k log k 1_(d=k),
    A_(N,k)(s)=Σ_(d≤N)w_k(d)(1−log d/log N)d^(−s),
    B_(N,k)=A_(N,k)−A_(N,k)(1).

Every B has length at most N and B(1)=0. For each fixed k, RH implies

    lim_N (log N)‖T_k−ζ B_(N,k)/s‖²=C_k,
    C_k=Σ_(distinct simple critical ρ)
          |ζ'(ρ)(k^(1−ρ)−1)|²/|ρ|².

Both ordinate signs are included. The same constant is the limit of log N times the best squared error over anchored length-N polynomials, and also over all ordinary length-N polynomials in the full boundary norm. No simplicity or reciprocal-zeta-derivative moment hypothesis is required. Multiple zeros contribute zero to this leading constant. The sum is finite and positive; a certified simple critical zero suffices for positivity.

Convergence of this particular prescribed anchored array to T_k is equivalent to RH for each fixed k. This is a different approximation target from the constant target in the classical Möbius problem. It does not remove the latter prescribed array's multiple-zero obstruction.

## 2. Coefficients, poles and exact smoothing

The divisor identity Σ_(d|n)Λ(d)=log n gives

    Σ_(d|n) w_k(d)=(k 1_(k|n)−1)log n,

which is exactly the jump of R_k. Thus the meromorphic quotient to taper is

    Z(s)=−F'_k(s)/ζ(s)=−h(s)ζ'(s)/ζ(s)−h'(s)
         =Σ w_k(d)d^(−s)   (Re s>1).

F_k cancels the zeta pole at1, Z(1)=0, and every zero pole of Z is simple, with residue r_ρ=−mρ h(ρ). This simple log-derivative pole is the reason no inverse ζ'(ρ) enters.

For L=log N use the exact double Perron integral on Re z=2, then shift to Re z=−1. It crosses only the kernel point and nontrivial zero poles; the apparent pole at1 is removable and trivial zeros start at−2. Good horizontal heights at distance ≫1/log|t| from zero ordinates give Z=O_k(log²|t|), enough to remove the horizontal integrals at fixed N,s. The left line has Z=O_k(log(2+|t|)). Under RH,

    Z−A_N=−Z'/L−(1/L)Σ_ρ r_ρ N^(ρ−s)/(s−ρ)²−I_N,
    |I_N(σ+it)|≪_k N^(−1−σ)log(2+|t|)/L.

The sum is absolutely convergent away from its removable boundary locations. In particular

    A_N(1)=[γ_E log k−(log k)²/2]/L+O_k(N^(−1/2)/L).

The anchor therefore changes the residual by O_k(1/L) in norm.

## 3. A uniform infinite-tail proof

A local Hadamard expansion on a fixed disk about1/2+it, with a fixed local zero list, gives

    Z'(s)=−Σ_(|γ−t|≤1)r_ρ/(s−ρ)²+O_k(log(2+|t|)).

The pole-free part is analytic before differentiation. This avoids differentiating a moving truncation. Classical convexity and Cauchy's estimate give |ζ|+|ζ'|≪(2+|t|)^θ for some θ<1/2; the stronger RH Lindelöf consequence is unnecessary for this step.

Except for O_k(1/L) in full norm, the residual is

    Σ_(|γ−t|≤1) r_ρ ζ(s)/[s(s−ρ)] E_L(t−γ),
    E_L(v)=(1−e^(−iLv))/(iLv).

Plancherel gives ∫|E_L|²dt/(2π)=1/L. For a nearby zero, |ζ(s)/(s−ρ)| is bounded by the supremum of |ζ'| along the critical-line segment. Multiplicity-weighted Cauchy–Schwarz and the unit-height count imply

    L‖near-tail_(|γ|>Y)‖²
       ≪_k Σ_(|γ|>Y)mρ log(2+|γ|)(2+|γ|)^(−2+2θ) →0,

uniformly in N. The distant zero sum is O_k(1/L) in norm by its inverse-square denominator. These estimates handle arbitrarily close distinct zeros and all multiplicities.

For a fixed finite set, take disjoint fixed neighborhoods and apply the mass-one approximate identity L|E_L|²/(2π). The value at a zero is r_ρ ζ'(ρ)/ρ. It is zero for a multiple zero; at a simple zero it gives the stated term. Take N→∞ first, then exhaust the zeros using the uniform tail bound. The local limit alone would not prove the upper result.

## 4. Matching lower bounds and the converse

For any bounded sequence of anchored candidates the source-independent compact zeroth Mellin tests at finitely many simple critical zeros have Gram matrix L times the identity plus o(L), and annihilate candidates up to o(1). The target pairing tends to T_k(ρ), since its cell growth is logarithmic and the gamma bump has vanishing pairing. Projection gives the finite sum lower bound; exhaustion gives C_k. The advocate's independent Burnol proof uses the inner multiplier(s−1)/s and a tested left-strip Mellin shift to justify the target pairings with exact cutoff witnesses. This is not numerical agreement.

For fully unrestricted ordinary polynomials, the exact outside-Hardy tail forces A(1)=O(L^(−1/2)) for candidates with bounded scaled error. Its fixed compact-test pairings are bounded, so this scalar changes each limiting pairing by o(1), even though its norm need only be O(L^(−1/2)). The same lower constant follows; the anchored array supplies the upper. One must not assert that the scalar's norm contribution is already o(L^(−1/2)).

If RH fails, a right-hand zero ρ of order m gives a bounded(m−1)-st Mellin evaluation annihilating every anchored approximant but taking value

    −ζ^(m)(ρ)(k^(1−ρ)−1)/ρ≠0

on T_k. It gives a fixed positive distance for every N. This proves necessity, including multiple and real hypothetical off-line zeros, without a zero-density estimate.

## 5. Scope and immediate work

The coefficients and target are fully explicit and use no zero labels. The proof is conditional on RH in its upper asymptotic. It gives no new bound on zero locations. The classical Selberg kernel, general membership criterion and lower-witness machinery are credited; the norm result is independently established here without a settled publication-priority claim.

The immediate effective task is to instantiate a global bound E_(N,k)≤K_k/log N under RH using explicit classical derivative and unit-zero-count bounds. This needs no growing inverse Gram or reciprocal-derivative estimate. A numerical modulus for convergence to the exact leading constant additionally needs quantitative fixed-zero localization and tail control. Limits in k or combinations of targets require fixed targets before N→∞ unless new uniform estimates are proved. Finite certified errors are recorded separately and do not prove the infinite conditional statement.
