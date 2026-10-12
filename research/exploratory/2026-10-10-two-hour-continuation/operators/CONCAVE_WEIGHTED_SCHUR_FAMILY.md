# The same-source weighted finite gate is a concave family

Status: exact analytic mechanism, conditional only on the complete native
source and Parseval identities already reviewed in the physical packet.
Finite native signs remain dependent on the completed directed residual.
No ordinary matrix output is used in the proof.

Fix one physical L<=log3, one exact finite trial frame, its complete protected
residual R, and its protected cosine moments a_n. Let m=7 and N>=8. In the
notation of SUPPORTING_LINE_INTERPOLATION.md, put

lambda_n(theta)=4/5+theta/2-(244+466theta)L²/(n pi)².

Restrict theta to any closed interval in[0,1] on which lambda8 is positive.
Since lambda_n increases with n, every weight in the entire tail is also
positive. The protected mean and first seven cosine moments vanish exactly.
Complete physical Parseval therefore gives the positive semidefinite tail
Gram

T_N=R-(2/L)sum_(n=8)^N a_n^*a_n >=0.

This is a continuum identity for the exact source. An interval subtraction
with a negative lower endpoint does not contradict it and is not needed
to prove it. The same-source finite dual bound can now be written

B_N(theta)=(2b/L)sum_(n=8)^N a_n^*a_n/lambda_n(theta)
             +b T_N/lambda_(N+1)(theta).

Every coefficient matrix in this expression is positive semidefinite and
independent of theta. Each lambda is affine in theta. Hence

B_N''(theta)=(4b/L)sum_(n=8)^N
                 (lambda_n')² a_n^*a_n/lambda_n³
             +2b (lambda_(N+1)')² T_N/lambda_(N+1)³ >=0.

Thus B_N is convex in Loewner order and S_N(theta)=U-B_N(theta) is concave
in Loewner order. In particular, its smallest eigenvalue is a concave real
function: it is the infimum over unit coefficient vectors of concave
quadratic forms. This explains why selecting the source line is a one
dimensional concave maximization problem rather than a search over unrelated
continuum integrals. The statement does not assert strict concavity or a
unique maximizer.

Two complete directed endpoint gates imply a whole parameter interval.
If S(theta0)>=epsilon0 I and S(theta1)>=epsilon1 I, then for0<=s<=1,

S((1-s)theta0+s theta1)>=[(1-s)epsilon0+s epsilon1]I.

No additional R integration or theta sampling is needed for this exact
consequence. It applies to the SAME fixed physical length and SAME trials;
it does not join different physical lengths. The source weights remain
positive throughout the segment by their affinity and the endpoint guards.

The tradeoff can be located exactly. Its derivative is

lambda_n'=1/2-466 L²/(n pi)².

For every21/20<=L<=log3, the bounds pi<3.1416, pi>3.1415 and
log3<1.0987 give lambda_n'<0 for n8,9,10 and lambda_n'>0 for every n>=11.
For n10, using L>=21/20 and the upper pi bound yields
2*466*(21/20)²>100*(3.1416)². For n11, using L<=1.0987 and the lower
pi bound yields2*466*(1.0987)²<121*(3.1415)². Monotonicity in n pays all
other modes. Increasing theta therefore enlarges the inverse weight of
the first three surviving modes while reducing that of every higher mode.
Their exact complete Gram balance determines the finite optimum.

The same reasoning works for any finite collection of pointwise supporting
lines for the same complete source: convex combinations produce affine
weights on a simplex, and the finite dual bound is jointly convex wherever
all weights are positive. This offers a source-specific finite optimization
mechanism with the protected coupling and full continuum tail retained.
It supplies neither an actual positive gate nor all-window positivity by
itself.
