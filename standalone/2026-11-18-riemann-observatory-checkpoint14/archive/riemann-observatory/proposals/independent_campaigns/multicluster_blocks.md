# Explicit decoupling of finitely many bounded clusters

Round2 continuation, equivalences agent,2026-11-17. Status: elementary continuous-Gram estimate, independent review pending. No novelty claim; the stable-basis mechanism has substantial prior literature, notably Avdonin–Ivanov math/0103160v1. This statement does not provide an infinite-zero bound.

## Lemma E-BLOCK-001

Consider p>=1 groups with sizes1<=m_a<=q and total size m=sum m_a. Group a has real frequencies mu_a+nu_(a,j), where |nu_(a,j)|<=R, repetitions within a group are permitted, and distinct group centers satisfy |mu_a-mu_b|>=S>0. Use within each group the normalized exponential Hermite divided-difference basis from multicluster_uniform.md, with the center factor separated:

phi_(a,j)(x)=exp(i mu_a x) h_j(x;nu_a), 0<=j<m_a.

Let G be the continuous Gram matrix of all these functions on[0,1], G_a its diagonal blocks, G_diag=diag(G_a), and b have entry1 for each order-zero basis vector and0 for the others. Define kappa_total=b*G^(-1)b and kappa_a=e_0*G_a^(-1)e_0 whenever inverses exist.

Let delta_* be the minimum of the explicit local delta(m_a,R) bounds established in the multicluster theorem. Put

epsilon=2m(q+R)/S.

If epsilon<=delta_*/2, then G>=delta_* I/2 and

|kappa_total-sum_a kappa_a| <=4pm(q+R)/(delta_*² S).

For p=1 the cross-block error is zero and no separation condition is needed.

## Proof

For entries joining two different groups, pull out the phase exp(i(mu_a-mu_b)x). Its amplitude f=h_j(nu_a) conjugate(h_k(nu_b)) satisfies |f|<=1 and |f'|<=j+k+2R<=2(q-1+R). Integration by parts gives

|integral_0^1 exp(i(mu_a-mu_b)x)f(x)dx|
 <=[|f(1)|+|f(0)|+integral|f'|]/|mu_a-mu_b|
 <=2(q+R)/S.

The Hermitian cross-block perturbation therefore has operator norm at most its maximum absolute row sum, bounded by epsilon. Local theorem gives G_diag>=delta_*I, so Weyl's inequality (or the quadratic-form triangle inequality) gives G>=delta_*I/2. Resolvent identity yields

||G^(-1)-G_diag^(-1)||<=2epsilon/delta_*².

Since ||b||²=p, sandwiching the inverse difference by b gives the claimed estimate.

The groupwise Hermite constraints are precisely the same value/jet constraints as a single global divided-difference basis, provided distinct groups do not represent the same frequency. The separation threshold implies S>2R unless R=0 (where nonzero centers are already distinct): delta_*<=1/4 and m,q>=1 make its requiredS more than sufficient. Thus kappa_total equals the global constant of the fixed-total-size theorem. Repeated frequencies inside a group are handled by confluent derivatives.

## Interpretation and limits

This makes the fixed-cluster additive limit quantitative: for finitely many bounded clusters moving far apart, the leading optimal approximation constant tends to the sum of their own collision-stable constants. Complete coalescence inside each group gives sum m_a², consistent with Burnol's fixed-root multiplicity mechanism.

The result does not assert uniform quadrature as the group centers grow with L. At large centers the finite grid can alias phases; transferring the continuous block estimate to a joint finite-L limit requires a nonaliasing condition and discrete oscillatory-sum bounds. Nor does it allow infinitely many groups, growing totalm, or omission of global Riesz-basis hypotheses. These are precisely the missing assumptions that an arithmetic application would need to address.

A next concrete step is a discrete summation-by-parts version with the denominator(L+1)|1-exp(i(mu_a-mu_b)/L)|, making the alias obstruction explicit. Even that would remain a finite polynomial theorem; it would not bound zeta residue coefficients.

## Discrete continuation E-BLOCK-002: phase separation replaces a diameter bound

The missing finite-grid step can itself be proved by summation by parts. Retain the group notation, fix a common residual degree L>=m, and let G_(a,L) be each local normalized endpoint Gram matrix. Write

D_*=max_a 2m_a(R+m_a), delta_*=min_a delta(m_a,R),

sigma_L=min_(a!=b)(L+1)|1-exp(i(mu_a-mu_b)/L)|,

epsilon_L=2m(q+R)/sigma_L.

For p=1 set epsilon_L=0 and omit sigma_L. Assume L>=2D_*/delta_* and epsilon_L<=delta_*/4. Then the complete empirical Gram matrix is at least delta_*I/4, and the actual polynomial optimum satisfies

|L E_total-sum_a L E_a^(L)| <=8p epsilon_L/delta_*².       (D)

Here E_total has all m roots and approximant degree<=L-m; E_a^(L) has group a's m_a roots and approximant degree<=L-m_a. The **same residual degree L**, not the same approximant degree, is essential for this exact common-grid comparison.

Combining(D) with the local uniform theorem gives

|L E_total-sum_a kappa_a|
 <=p(2D_*/delta_*²+2/delta_*)/L
   +16pm(q+R)/(delta_*² sigma_L).                         (E)

These bounds concern actual finite polynomials. They do not infer discrete decoupling from continuous oscillatory integrals.

### Proof

For z=exp(i(mu_a-mu_b)/L) and f_k=h_j(k/L;nu_a)conjugate(h_k(k/L;nu_b)), the exact Abel identity is

(1-z)sum_(r=0)^L z^r f_r
 =f_0-z^(L+1)f_L+sum_(r=1)^L z^r(f_r-f_(r-1)).

Its right side has modulus at most2+2(q-1+R)=2(q+R): endpoint moduli are at most1 and the total sampled variation is at most the continuous Lipschitz bound2(q-1+R). Thus every cross empirical-Gram entry is at most2(q+R)/sigma_L. Maximum absolute row sums bound the cross-block operator norm by epsilon_L.

The local quadrature theorem gives G_(a,L)>=delta_*I/2. Therefore the complete empirical Gram matrix is at least delta_*I/4. The inverse difference from the block diagonal matrix is at most

(4/delta_*)epsilon_L(2/delta_*)=8epsilon_L/delta_*².

The target vector b has squared normp. The exact coefficient optimum is b*G_L^(-1)b/(L+1), and the analogous block expression is the sum of E_a^(L). Multiplying by L and using L/(L+1)<=1 proves(D). The local uniform theorem, applied separately to each radius-R group with its common residual degreeL, proves(E).

Within each group the large-L threshold excludes internal aliases. Across groups, a hidden collision modulo2pi L would make the union of evaluation/derivative rows linearly dependent: identical circle roots have the same derivative-evaluation span, with maximum rather than summed multiplicity. The strictly positive complete empirical Gram matrix therefore rules out such a hidden alias under the stated assumptions. This justifies its use for the actual global polynomial constraints.

### Joint limits and the explicit alias obstruction

Let S_L=min_(a!=b)|mu_a-mu_b|. If all pairwise center differences have modulus at most pi L, then the elementary sine inequality gives

sigma_L>=2S_L/pi.

Thus(E) gives a genuine joint O(1/L+1/S_L) estimate with fixed local group parameters. It applies even when S_L is comparable toL, provided phase separation and the stated small-cross-block condition hold. The global compact-diameter theorem could not alone justify this regime.

For centers differing by nearly2pi times an integer timesL, sigma_L can be small even when their ordinary separation is enormous. This is the precise finite-grid alias obstruction. No replacement of sigma_L by S_L is valid without a nonaliasing restriction. The result is still finite and carries explicit dependence on p,m,q,R; it supplies no separation, multiplicity, summability or residue estimates for zeta zeros.
