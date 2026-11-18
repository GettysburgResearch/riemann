# Third independent review: a collision-uniform scalar polynomial window

Reviewer: semantic_skeptic. Date: 17 November 2026. Inspected `proposals/independent_campaigns/unit_circle_scalar_window_round3.md` after first reconstructing the claim independently. No formal build was launched. This is a finite polynomial/H2 theorem, not an arithmetic transfer or a novelty claim.

**Conclusion:** the universal estimate with the stated K_m and the fixed-m complete-coalescence asymptotic are correct. I found no endpoint, indexing, collision or normalization gap. The proof genuinely has no root-separation denominator. The asymptotic constant m² is for fixed m, whereas the finite bound has an explicit rapidly growing m-dependent constant.

## Exact hypotheses and normalizations

Take an integer m>=1, arbitrary complex q_j with |q_j|=1, and every integer M>=1, equivalently degree cutoff N=M-1>=0. Let Q=product(1-q_j z), Q(0)=1, and let b_n be its reciprocal Taylor/formal-series coefficients. There is no assumption that1/Q belongs to H2, and none is needed: the approximant and residual are finite polynomials. The H2 norm is the coefficient square sum, corresponding to normalized circle measure dtheta/(2pi).

The q_j are indexed factors, so repeated values remain separate indices in subset sums. This correctly treats collisions without requiring distinct roots. A common nonzero scalar normalization of Q can be absorbed in b_n, leaving QA unchanged.

The statement excludes m=0. If desired, that case is trivial separately: Q=1, A=1 and the error is0; the closed binomial expression for C_m need not be used at m=0. M=0 is not admitted, since the window contains division by M.

## Twisted product rule independently checked

Let S denote the backward shift and D_q=1-qS. Direct expansion gives

D_q(cw)_n=w_n(D_qc)_n+q c_(n-1)(w_n-w_(n-1)).

All D_q commute with each other and with S. Induction therefore gives one term for each indexed subset J: every index placed in J contributes q_j and one shift of the coefficient sequence and one backward difference of w. The factors outside J act on the reciprocal coefficient sequence. Formal cancellation reduces that sequence exactly to the reciprocal product over J, giving

(QA)_n=w_n delta_(n0)+sum_(nonempty J)q_J h_(n-|J|)(q_j:j in J) Delta^|J| w_n.

For k=|J|, h_(n-k)=0 when n<k. This vanishing is essential: the derivative estimate is used only when n>=k, where every point sampled by the finite difference lies in[0,M]. No estimate at a negative continuous argument is being silently applied to the bulk bound.

The coefficient sequence uses w_n=(1-n/M)^m through n=M and0 thereafter. Because m>=1, w_M=0. Thus this is exactly the stated truncation at degree M-1. The coefficient n=M nevertheless belongs to the bulk estimate; discarding it would leave a missing term.

## Bulk, terminal coefficients and all small endpoints

For1<=n<=M and n>=k,

|h_(n-k)|<=binom(n-1,k-1)<=M^(k-1)/(k-1)!,

while the repeated finite-difference integral gives

|Delta^k w_n|<=m_falling_k/M^k.

Summing over binom(m,k) subsets gives |(QA)_n|<=C_m/M, with

C_m=sum_(k=1..m)binom(m,k)m_falling_k/(k-1)!
 =sum_(k=1..m)k binom(m,k)^2
 =m binom(2m-1,m-1).

The residual has r0=0 and r_n=-(QA)_n for n>=1. There are exactly M bulk coefficients n=1,...,M.

The remaining degrees are n=M+r,1<=r<=m-1. Only convolution indices j>=r+1 can contribute; indices giving a negative reciprocal coefficient are omitted. The bound

|b_l|<=binom(l+m-1,m-1)<=binom(M+m-2,m-1)<=M^(m-1)

holds for0<=l<=M-1. For m>=2 the last inequality follows factorwise from M+j<=(j+1)M; for m=1 it is1<=1. Consequently the terminal bound is exactly T_(m,r)/M, with the T from the claim. The degree of QA is at most M+m-1, so there is no further tail.

It follows that

E_M<=C_m²/M+sum_(r=1..m-1)T_(m,r)²/M²<=K_m/M.

All inequalities include M=1. Negative indices are zero, rather than values of an analytic continuation of b_n. This distinction is explicitly respected in both parts of the proof. For m=1 the error is exactly1/M. For m=2, C2=6 and T_(2,1)=1, yielding K2=37. These are bounds for a prescribed polynomial, whose finite error need not be<=1.

## Complete coalescence and endpoint cancellation

When every factor equals1-qz, the nth coefficient of the residual is q^n times the q=1 residual. Hence the norm is exactly independent of the common phase, even if that phase varies with M. It suffices to take q=1.

The binomial polynomial P_m(n)=product_(j=1..m-1)(n+j)/(m-1)! equals b_n for n>=0 and vanishes at the integers -1,...,-(m-1). A backward m-th difference at n>=1 never reaches below1-m, so its polynomial extension agrees with the actual zero extension at every negative index used. At n=0 it would not agree in general; the proof correctly treats r0 separately.

Set

f_M(x)=product_(j=1..m-1)(x+j/M)(1-x)^m/(m-1)!,

f(x)=x^(m-1)(1-x)^m/(m-1)!.

For fixed m, f_M-f and all needed derivatives are O_m(1/M) on a fixed bounded interval. Applying the finite-difference integral at n/M yields, uniformly1<=n<=M,

r_n=-f^(m)(n/M)/M+O_m(M^-2).

The m-1 terminal coefficients have total squared norm O_m(M^-2). Squaring the bulk expression and using the polynomial Riemann sum gives

E_M=M^-1 integral_0^1[f^(m)(x)]²dx+O_m(M^-2).

I independently checked the integration-by-parts identity. For every polynomial p of degree at most m-1, m integrations by parts leave only the first lower-endpoint term: f has a zero of order m at1 and of order m-1 at0, with f^(m-1)(0)=1. Thus

integral_0^1 f^(m)(x)p(x)dx=-p(0).

Taking p=f^(m), whose degree is m-1, is valid. The x^m coefficient of f is -m/(m-1)!, so f^(m)(0)=-m², and the integral is m². Therefore E_M=m²/M+O_m(M^-2).

The differentiation/Riemann-sum constants here depend on fixed m. This does not prove the same asymptotic when m grows, nor uniformity in such a growth regime. It does prove uniformity in the common phase and the stated collision-uniform upper estimate for each m.

## Independent exact checks and a closed double-root example

`experiments/code/polynomial_window_third_round3.py` obtained reciprocal coefficients through the Qb=1 recurrence, then formed QA by direct convolution over exact rational Gaussian pairs. It did not use the subset formula to generate the residual.204 cases passed, using17 root patterns, degrees1 through4, M=1,...,12, complete/partial collisions, and rational nonreal unit phases. The checks validate both individual coefficient bounds and the total-energy bound. Result: `experiments/results/polynomial_window_third_round3.json`. They support the analytic proof rather than substitute for it.

A separate exact coalesced m=2 calculation gives

r_n=(4M+4-6n)/M²,1<=n<=M,

r_(M+1)=-1/M,

E_M=4/M+3/M²-2/M³.

It confirms the limit M E_M->4 and includes E1=5. At M=1 the optimal constant polynomial approximation instead has squared error5/6; thus "optimal leading constant" must not be confused with finite-M optimality. The proposal makes that distinction correctly.

## Lower powers and scope

For repeated roots, the last residual coefficient under a nonnegative integer taper power p<m has modulus binom(M+m-2,m-1)/M^p. Its squared value stays bounded away from0 at p=m-1 and diverges for smaller integer p. This independently confirms the stated negative result. It does not prove a sharp threshold among noninteger powers; that requires a separate endpoint-layer argument.

Classification: **Independently checked with no issue found in the inspected portion.** No zeta analogue follows without specifying coefficient arithmetic, norm weights and the growing/infinite-zero regime. No historical-priority claim was checked or made.

## Additional independent review: sharp m=2 constant5

After completing the general review, I independently checked the sharper m=2 autocorrelation argument supplied by equivalences in §6 of the proposal. By a common rotation write Q=(1-z)(1-qz), |q|=1. Put a_n=2M+1-2n. Direct convolution, or the checked product rule, gives

M² r_n=a_n(1+q^n)-2 sum_(j=1..n-1)q^j,1<=n<=M,

M² r_(M+1)=-sum_(j=1..M)q^j.

For lag k=1,...,M in M^4 E_M, the row n=k contributes a_k². A row n>k has two endpoint/interior products -2a_n each and n-k-1 interior/interior products4. The terminal row contributes M-k. Hence its total real Laurent coefficient is

R_k=a_k²+sum_(n=k+1..M)[-4a_n+4(n-k-1)]+(M-k).

Setting d=M-k, the summation is -2d²-2d and a_k=2d+1; therefore

R_k=(2d+1)²-2d²-d=(d+1)(2d+1)>0.

It follows exactly that

E_M(1)-E_M(q)=(2/M^4)sum_(k=1..M)R_k[1-Re(q^k)]>=0.

This verifies all lag endpoints, including k=M and M=1. The coalesced value already computed is

E_M(1)=4/M+3/M²-2/M³.

The inequality E_M(1)<=5/M is equivalent to(M-1)(M-2)>=0, valid for integer M>=1 with equality M=1,2. Thus5 is the sharp constant in a uniform bound E_M<=K/M for m=2;37 remains a valid generic-argument bound. The maximum over relative phases is attained only at q=1 because R1>0. The updated exact checker independently verifies this Laurent-gap identity and sharp bound in72 rational-complex cases, within its204 total cases.
