# An unconditional all-rank lower bound for the parent's finite source Grams

Status: PROPOSED COMPLETE ELEMENTARY BOUND. It is exponentially small in rank;
it does not prove that the parent's projection errors tend to zero.

## 1. Statement

Retain d_b and R_1 from the parent, with 1/2<=b<=1. Let G_N be the original
L2 Gram of d_b,R_1 d_b,...,R_1^N d_b. Then for every integer N>=0,

    G_N >= gamma_N I,
    gamma_N=2^(-28N-21)/(N+1).                     (G1)

The numerical constants are deliberately conservative. This theorem supplies
an explicit finite inverse-stability bound without a zero census, a lower
bound for zeta on an entire vertical line, or RH. It is not a uniform-in-rank
positive floor. The parent already gives a synthetic example where even a
uniform floor coexists with a nonzero domain defect.

## 2. A literal source arc is enough

For 0<=t<=1/2 we have g(t)=1-t. Since b<=1 and exp(-1/2)>1/2,

    D_b(0)=integral d_b(t)dt >1/8.

Also

    integral t d_b(t)dt <=1/b^2+2/b^3<=20.

The elementary inequality |exp(-iyt)-1|<=|y|t yields

    |D_b(iy)|>1/16 for |y|<=delta:=1/320.           (G2)

Only this very short frequency interval is used. No line-wide reciprocal
zeta estimate is being assumed.

Set w(y)=(iy-1)/(iy+1). For y,y' in [0,delta],

    |w(y)-w(y')|=2|y-y'|/sqrt((1+y^2)(1+y'^2)) >=|y-y'|.

For a polynomial p(w)=sum_(j=0)^N c_j w^j, write n=N+1 and
ell=delta/(2n). Choose one y_j in each interval

    [j delta/n, j delta/n+ell], j=0,...,N,

at which |p(w(y_j))|^2 is at most its interval average. Then

    |w(y_j)-w(y_i)|>=ell |j-i|.

The Lagrange interpolation polynomial at node j has coefficient l2 norm at
most its coefficient l1 norm, hence at most

    2^N/(ell^N j!(N-j)!).

Cauchy--Schwarz applied to the interpolation formula, followed by
sum_j binom(N,j)^2=binom(2N,N)<=4^N, proves

    integral_0^delta |p(w(y))|^2dy
       >= ell^(2N+1)(N!)^2/16^N * sum_j |c_j|^2.   (G3)

No fixed sample is used as a lower bound for a continuous integral: the
sample points are selected separately for the particular polynomial by the
mean-value bound, and the separation estimate is uniform for every choice.

Plancherel, (G2), and pi<4 give the stronger exact bound

    c*G_N c >= [ell^(2N+1)(N!)^2/(2048*16^N)]||c||_2^2.          (G4)

For N>=1, N! >=(N/e)^N, e<3 and N/(N+1)>=1/2 give

    ell^(2N+1)(N!)^2/(2048*16^N)
      >= [delta/(4096(N+1))] [delta/(16e)]^(2N)
       > 2^(-28N-21)/(N+1).

Here 16e/delta<15360<2^14 and 4096/delta=1310720<2^21.
N=0 follows directly from (G4). This proves (G1).

## 3. A complete, but expensive, source-cutoff prescription

If d_b is truncated at time T before applying the all-pass filters, the
parent's norm calculation gives

    ||G_N-G_N^T||_op <=6(N+1)(T+3)exp(-T/2)        (G5)

uniformly for 1/2<=b<=1. For completeness, the source tail is at most
(T+3)exp(-T/2) in L2 and ||d_b||_2<3, so every entry error is at most six
times that tail. All filter output tails must be retained in G_N^T.

The explicit schedule

    T_N=128(N+1)                                    (G6)

makes (G5) smaller than gamma_N/2. To check this, put n=N+1, use e>2,
128n+3<=131n, n^3<=2^(3n), and 786<2^10. The ratio of the error to
gamma_N/2 is then at most 2^(4-33n)<1.

Thus G_N^T has minimum eigenvalue at least gamma_N/2, and

    ||(G_N^T)^(-1)-G_N^(-1)||_op
           <=2||G_N^T-G_N||_op/gamma_N^2.           (G7)

Increasing T explicitly makes this as small as any prescribed rational
tolerance. The associated integer cutoff is approximately exp(128(N+1));
this is NOT a practical polynomial-cost algorithm and was NOT run at large
rank. The advantage is a proved error/conditioning contract, not efficiency.

The finite projection formula still needs the actual value of its matrix
quadratic form. Neither (G1) nor (G7) forces that value to reach the target
limit 1. The all-rank cyclicity estimate remains unproved.
