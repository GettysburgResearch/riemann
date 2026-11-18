# Independent review of the critical fractional leading constant

Reviewer: semantic_skeptic. Date: 17 November 2026. Independently reconstructed the extension proposed in `proposals/independent_campaigns/fractional_scalar_critical_constant_round3.md`. This supplements the separately challenged threshold theorem; no computation or formal build is used.

**Conclusion:** for every fixed integer m>=1, p=m-1/2 and Q=(1-qz)^m with |q|=1, the claimed expansion is correct:

E_(M,p)=kappa_m² logM/M+O_m(1/M),

kappa_m=(p)_m/(m-1)!=m binom(2m,m)/4^m.

There is no extra hidden condition on how the common phase varies with M: coefficient rotation makes the error exactly phase-independent. Constants depend on fixed m, and no growing-m uniformity is established.

## Uniformity of the derivative expansion

Take M>=4m and1<=j<=floor(M/2). All finite-difference integration points have t=j+sum s_i in[1,3M/4], hence u=M-t>=M/4. A lower bound M/2 for u would be incorrect at the far edge of this block, but M/4 suffices and is what the proposal uses.

For the fixed polynomial P(u)=product_(l=1..m-1)(u+l)/(m-1)!, finite product expansion gives

P(M-t)=M^(m-1)/(m-1)![1+O_m((t+1)/M)],

P^(r)(M-t)=O_m(M^(m-1-r)),0<=r<=m-1,

uniformly throughout that block. The first error need not tend to0 when t is a fixed fraction of M; it is a valid uniform bound, which is enough.

In a_M(u)=M^(-p)P(u)(M-u)^p, the k=m Leibniz term is

(-1)^m kappa_m M^(-1/2)t^(-1/2)
 +O_m(M^(-3/2)t^(1/2)).

The factor(t+1)t^(-1/2) is O(t^(1/2)) because t>=1. Every lower term k<=m-1 is also O_m(M^(-3/2)t^(1/2)), since its additional factor is(t/M)^(m-k-1)<=1. The k=0 term vanishes because P has degree m-1. This verifies the derivative error uniformly in j and every cube variable.

## Coefficient errors are summable at the required scale

The finite-difference integral and the mean-value theorem on[j,j+m] give

r_(M-j)=(-1)^(m+1)kappa_m M^(-1/2)j^(-1/2)+e_j,

|e_j|<=C_m[M^(-1/2)j^(-3/2)+M^(-3/2)j^(1/2)].

All indices in this block satisfy n-m>=0, so the actual reciprocal coefficients agree with the positive-index formula; no continuation through a singular endpoint is used.

The main/error cross sums are bounded by

C_m[M^(-1)sum j^(-2)+M^(-2)sum1]=O_m(1/M).

Using(a+b)^2<=2a²+2b², the squared-error sum is bounded by

C_m[M^(-1)sum j^(-3)+M^(-3)sum j]=O_m(1/M).

Thus the near-endpoint energy is kappa_m² times the harmonic sum divided by M, with O_m(1/M) error. Since H_floor(M/2)=logM+O(1), its leading term is exactly the one claimed.

## Remaining coefficients

The already proved critical upper coefficient estimate is

|r_(M-j)|<=H_m/M *[(j+1)/M]^(-1/2).

For j>floor(M/2), its square sums to O_m(1/M), because the bracket is bounded and there are at most M terms. At j=0 the square is O_m(1/M). The finite terminal block has the same total order, and the constant residual coefficient is0. Therefore there is no omitted logarithmic contribution or larger endpoint error.

Finally,(p)_m=(2m)!/(4^m m!) gives the stated kappa identity. The first squared constants are1/4 and9/16 for m=1,2, respectively. This agrees with the exact one-root radical identity in the threshold proposal.

Classification: **Independently checked with no issue found in the inspected portion.** This is a fixed finite-polynomial asymptotic consequence. No historical novelty, RH implication or uniformity for growing multiplicity is asserted.
