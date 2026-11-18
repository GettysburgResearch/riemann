# Independent advocate audit: double unit-circle root

Reviewer: li_advocate, 2026-11-17. The equivalence agent's proof and code were not read before this reconstruction. The parent supplied only the proposed formulas. I independently checked the primary-source convention in Bettin–Conrey–Farmer, arXiv:1211.5191v1, p.3, equation(3) and Theorem2. That theorem explicitly assumes simple zeros. This example violates that hypothesis and is not an error in that theorem.

Let N≥0, L=N+2, P(z)=(1−z)^2. By Parseval the squared circle norm of R=1−PA is ∑_(k=0)^L |c_k|², where A has degree≤N and R(z)=∑c_k z^k. The residual constraints are exactly R(1)=1 and R'(1)=0, or ∑c_k=1 and ∑k c_k=0. Conversely these constraints ensure 1−R is divisible by (1−z)^2 and the quotient has degree≤N.

The minimum Euclidean norm solution of these two linear constraints lies in the span of their conjugate row vectors, i.e. c_k=α+βk with real α,β. Solving using ∑k=L(L+1)/2 and ∑k²=L(L+1)(2L+1)/6 gives

α=2(2L+1)/[(L+1)(L+2)], β=−6/[(L+1)(L+2)].

Its norm² is ∑c_k(α+βk)=α, since the constraints are1 and0. The optimal quotient is

a_n=(n+1)(L−n)(L−n−1)/[(L+1)(L+2)], 0≤n≤N.

This follows either by discrete double integration c_k=δ_(k0)−a_k+2a_(k−1)−a_(k−2), taking a outside[0,N] to be zero, or by direct substitution. Strict convexity gives uniqueness, including complex coefficients. Thus the optimum squared norm is 2(2L+1)/[(L+1)(L+2)]~4/N. This agrees with the multiplicity-squared constant quoted in BCF p.3 before Theorem2.

BCF's W_N is precisely ∑_(n=0)^N(1−n/N)a_n z^n with a_n the reciprocal Taylor coefficient. For P=(1−z)^2, a_n=n+1; the n=N coefficient is zero. For N≥1 the residual coefficients of W_N are c_0=0, c_k=2/N for 1≤k≤N, c_(N+1)=−1, and c_(N+2)=0. Therefore its squared norm is **exactly 1+4/N**, rather than tending to zero. This independently confirms the proposed obstruction.

Terminology caution: the optimal **coefficient** a_n above is cubic in n, but relative to reciprocal coefficient n+1 the **window** (L−n)(L−n−1)/[(L+1)(L+2)] is quadratic. Calling it a 'cubic taper' without specifying which quantity can mislead. There is an N vs L=N+2 boundary correction and the optimal constant coefficient is not1; both are essential to the exact formula.

Independent code `experiments/code/toy_advocate_exact.py` verifies for N=0,…,100 using Fraction arithmetic: all residual coefficients, both constraints, the claimed norm, and orthogonality c_j−2c_(j+1)+c_(j+2)=0 to every multiplication column. It verifies the triangular formula for N=1,…,100. These computations supplement the all-N proof above.

Classification: independently checked with no issue in inspected claim. This is an elementary finite-dimensional model and no novelty is asserted. Transferring the observation to ζ requires controlling infinite zero sums, their multiplicities and clusters, and arithmetic approximation spaces; the polynomial example itself supplies none of those estimates.
