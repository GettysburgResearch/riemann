# Independent audit of directed integer Lagarias finite certificate

Reviewer: li_advocate. Date:2026-11-17. Inspected `experiments/code/lagarias_finite.py` in full and reran it. Status: independently checked with no issue found in the inspected code and mathematical certificate logic. This reproduces a known finite verification and asserts no new RH theorem.

Let S=2^80 and h_n=∑_(k≤n)floor(S/k). Then h_n/S≤H_n by summing exact inequalities. For nonnegative fixed-point inputs x,y, `mul_lower(x,y)/S=floor(xy/S)/S≤(x/S)(y/S)` and remains nonnegative. This directed rounding is essential.

For x≥0, `exp_lower(x)` starts with S and successively multiplies/floors by x/(Sk). By induction the kth stored term divided by S is at most (x/S)^k/k!. All omitted terms in exp's Taylor series are nonnegative; therefore the returned value/S is at most exp(x/S). No remainder upper bound is needed.

For x≥S, set y=(x/S−1)/(x/S+1)∈[0,1). The computed integer y_lower/S is at most y. Multiplying/flooring its square and odd powers preserves the lower bound. Each integer division by an odd positive integer lowers a term. The identity log(x/S)=2∑_(j≥0)y^(2j+1)/(2j+1) and the positivity of all omitted terms prove `log_lower(x)/S≤log(x/S)`. The n=1 case x=S gives exactly0.

Because h_n/S≥1, both function approximants are nonnegative. Monotonicity of exp and log on [1,∞), multiplication of nonnegative lower bounds, and the final directed floor prove that the recorded b_n/S is at most H_n+exp(H_n)log(H_n). The divisor sieve visits each positive divisor d of n exactly once, so sigma[n]=σ(n) exactly. Each positive recorded integer gap b_n−Sσ(n) is therefore a rigorous certificate for the strict desired inequality. At n=1, h=S, log=0 and σ=1, proving exact equality directly. Python arbitrary-precision integers avoid overflow.

The run checked all5039 strict cases n=2,…,5040 and equality at1. The smallest recorded directed lower gap occurred at n=2 and was383433241300091042769035/S>0. This minimum is a minimum of these particular lower-bound certificates, not asserted to be the exact minimum of the true transcendental gaps.

A second implementation `experiments/code/lagarias_independent_samples.py` uses Fraction arithmetic for the exact H_n and direct rational finite positive series at n=2,12,5040. It independently confirmed h_n/S≤H_n, that integer exp/log approximations lie below the corresponding rational series, and that their rational RHS and integer lower certificate exceed exact σ(n). Displayed sample gaps are approximately0.3171685434,0.3218372596,492.3187311, respectively. Decimal display does not enter any assertion. The sample code is a corroboration of three cases; the all-n certificate is supported by the preceding monotonicity proof and the full integer run.

Limitations: the finite check reaches5040 only. It provides no implication for n>5040 without a separately sourced and verified theorem. It does not evaluate a conditional theorem as though unconditional, and no floating-point inequalities are used.
