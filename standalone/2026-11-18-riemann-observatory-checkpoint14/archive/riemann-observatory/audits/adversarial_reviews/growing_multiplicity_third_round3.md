# Third independent review: growing multiplicity in the polynomial model

Reviewer: semantic_skeptic. Date: 17 November 2026. Reviewed `proposals/independent_campaigns/growing_multiplicity_transition_round3.md` from its stated hypotheses. No formal build was launched. This review establishes the asymptotic deductions **from the exact finite-model formula**; it does not independently reprove that formula for all dimensions or make an arithmetic/zeta claim.

**Conclusion:** the proposed two-sided bounds, transition at m of order sqrt(N), saturation regime, and exact criterion for E~m²/N are correct. All displayed constants are explicit in N,m; no fixed-m remainder is being applied outside its range. There is one minor wording correction in the necessity discussion: an unbounded subsequence need not itself tend to infinity, but one can extract a further subsequence that does. An independent global bound below gives an even shorter necessity proof and sharpens the proposed simple absolute remainder.

## Independent verification of the uniform artanh bound

Let N,m be integers at least1, L=N+m, C=L+1/2, x_j=j+1/2 and r=(m-1/2)/C. Then0<x_j/C<=r<1 since C-(m-1/2)=N+1>0. All product factors are strictly between0 and1, so E is strictly between0 and1 and its logarithm is legitimate.

Write S=-log(1-E). The exact product gives

S=2 sum_{j=0}^{m-1}artanh(x_j/C).

For0<=u<=r<1, the convergent positive power series gives

artanh(u)-u=sum_{k>=1}u^(2k+1)/(2k+1)
 <=u³/[3(1-u²)]<=u³/[3(1-r²)].

The exact half-integer sums are

sum x_j=m²/2,

sum x_j³=m²(2m²-1)/8.

Consequently A<=S<=A+B with exactly

A=m²/C,

B=m²(2m²-1)/[12 C³(1-r²)].

There is no hidden dependence on a fixed multiplicity. Even when r approaches1 the explicit denominator records the deterioration rather than hiding it in an O constant.

Exponentiation, preserving the signs, gives

1-exp(-A)<=E<=1-exp(-A-B),

0<=E-[1-exp(-A)]<=exp(-A)(1-exp(-B))<=exp(-A)B.

These prove the proposal's(1) for every admitted N,m, not just asymptotically.

## Transition and saturation, with the quantifiers checked

Set t=m²/N and let N tend to infinity along any integer sequence, with m=m(N)>=1.

If t tends to a finite lambda>=0, then m=O(sqrt(N)), m/N tends to0, C/N tends to1, r tends to0, and A tends to lambda. Also B=O(1/N) along every bounded-t family, so B tends to0. Therefore E tends to1-exp(-lambda). The argument includes lambda=0 and fixed m.

If t tends to infinity, split the indices according to m<=N or m>N. In the first class, C<=3N, so A>=t/3 tends to infinity. In the second class, C<=3m and m>N tends to infinity, so A>=m/3 tends to infinity. These estimates apply to all indices in their respective classes and therefore handle an arbitrarily interlaced sequence. The lower bound E>=1-exp(-A) and E<1 imply E tends to1.

For t tending to0, A/t=N/C tends to1, A tends to0, and B/A tends to0. Thus E/t tends to1. Conversely, if t does not tend to0, select indices with t>=epsilon>0. A bounded such subsequence has a convergent further subsequence with positive finite limit; an unbounded one has a further subsequence tending to infinity. On those respective sequences the limiting ratio is(1-exp(-lambda))/lambda<1 or0. Hence E/t cannot tend to1. The proposal's conclusion is correct; replace the phrase "an unbounded subsequence has ... tending to0" by "from an unbounded subsequence, choose a further subsequence tending to infinity."

The saturation wording should likewise be understood in the precise sense m/sqrt(N) tending to infinity, not merely m greater than some fixed multiple of sqrt(N).

## A separate global bracket and direct necessity proof

There is a useful independent bound that does not require the cubic remainder. Since L-j>=N+1,

S=sum_{j=0}^{m-1}log[1+(2j+1)/(L-j)]
 <sum_{j=0}^{m-1}(2j+1)/(L-j)
 <=m²/(N+1)<t.

Together with S>=A, this gives the global bracket

1-exp(-A)<=E<1-exp[-m²/(N+1)]<1-exp(-t).

Define g(t)=(1-exp(-t))/t for t>0. Its derivative is

[e^(-t)(t+1)-1]/t²<0,

because exp(t)>1+t. Therefore, if t>=epsilon, then E/t<=g(epsilon)<1. This proves necessity of t tending to0 directly, with no subsequence argument or boundedness assumption. Sufficiency follows by squeezing E/t between[1-exp(-A)]/t and g(t).

The exact product also equals

1-E=binom(N+m,m)/binom(N+2m,m).

Thus E is exactly the probability that a sample of m objects without replacement from N+2m objects hits a specified set of m marked objects. This is an exact algebraic identity, not a vocabulary analogy; no probabilistic limit theorem is needed for the analytic proof above.

## Explicit compact uniformity and stronger simple remainder

For any fixed K>0, simultaneously for every integer N,m>=1 with t=m²/N<=K, the preceding bracket yields

0< [1-exp(-t)]-E
 <=t-A
 =m²(m+1/2)/(NC)
 <=K^(3/2)/sqrt(N)+K/(2N).

This proves uniform convergence to the transition profile on bounded t ranges, including all m up to sqrt(KN), with an explicit bound and no implicit m-dependent constants. A sharper intermediate bound is exp(-A)(t-A).

The proposal's stated absolute remainder is valid, but its +B term can be omitted. Since E<1-exp(-t)<t and E>=1-exp(-A),

0<t-E
 <=(t-A)+[A-(1-exp(-A))]
 <=m²(m+1/2)/(NC)+A²/2.

The last step follows from A-(1-exp(-A))=integral_0^A(1-exp(-u))du<=A²/2. This is another globally valid explicit inequality.

## Optional first correction in the transition window

The verified estimates also determine the first correction relative to the profile evaluated at the actual t=m²/N. If m/sqrt(N) tends to a finite c>=0, then

sqrt(N){E-[1-exp(-m²/N)]} tends to -c³ exp(-c²).

Indeed B=O(1/N), so E=[1-exp(-A)]+O(1/N). Also

sqrt(N)(t-A)
 =t[(m+1/2)/sqrt(N)]/[1+(m+1/2)/N]
 tends to c³.

The mean-value theorem applied to1-exp(-x) then gives the displayed limit. This statement does not require m-c sqrt(N) to be bounded: using the actual t in the comparison removes that rounding issue. It is a derived consequence of the exact model, with no novelty or zeta claim.

## Independent finite verification of the projection indexing

`experiments/code/growing_multiplicity_third_round3.py` constructed the actual coefficient vectors of(1-z)^m z^j, j=0,...,N, and solved their Gram projection system exactly over Python Fraction. It did not evaluate the optimal error by the proposed product. Across96 cases, N=1,...,8 and m=1,...,12, including m>N, its independently obtained squared H2 error agreed with both the product and binomial-ratio expressions. The result is `experiments/results/growing_multiplicity_third_round3.json`.

The linear-algebra rationale is that the Gram right side for projecting1 is the first standard basis vector, so the squared residual is1-(G^(-1))_00. The polynomial basis is linearly independent and gives the same real solution even when complex approximation coefficients are allowed. These finite checks corroborate indexing and parameter conventions; they are not a proof for all N,m or a numerical substitute for the asymptotic argument.

Classification: **Independently checked with no issue found in the inspected portion**, with the minor subsequence wording clarification above and valid stronger consequences recorded separately. The result concerns polynomial degree N and multiplicity m only. It establishes no map from N to a Dirichlet-polynomial cutoff and no extension to several independently moving confluent clusters.
