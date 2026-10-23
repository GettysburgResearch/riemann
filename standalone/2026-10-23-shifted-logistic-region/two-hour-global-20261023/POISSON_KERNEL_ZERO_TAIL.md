# A sharper outside-disc zero sum from the Hadamard identity

2026-10-23. New analytic lemma, proposed for independent review.
This replaces the Rosser-count input in the weighted Ford detector;
it does not alter any earlier frozen theorem packet.

## 1. A pointwise comparison preserving the local subtraction

Let rho=beta+i gamma be a nontrivial zero, 0<beta<1, and put
d=1-beta, y=q-gamma, r^2=d^2+y^2. Define the positive kernel

    P_rho(q)=(d+1/2)/[(d+1/2)^2+y^2]
            =Re[1/(3/2+iq-rho)].

If r^2>=1/4, then

    1/r^2 <=4P_rho(q),                              (Z1)

because this is equivalent to (4d+1)r^2>=d+1/4. If r^2<1/4,
then P_rho(q)>1, since its denominator is r^2+d+1/4<d+1/2.
At r^2=1/4 the kernel is exactly1. Assign the boundary to the
local disc, which is closed throughout this note.
Summing the two cases, with multiplicities, gives

    sum_(|1+iq-rho|>1/2) |1+iq-rho|^-2
       <=4 sum_rho P_rho(q)-4N(q,1/2),                (Z2)

where N counts zeros in the closed disc. In particular the count
term remains exactly the -4N needed to cancel the local-detector
loss. The local bound (G2) holds on the boundary, and the outside
bound also holds on the open complement, so this convention is
permitted in the decomposition. A boundary zero is never counted
both in the outside sum and in N.

## 2. Explicit control of the positive kernel sum

The logarithmic derivative of the completed zeta product gives, for
s=3/2+iq,

    sum_rho Re[1/(s-rho)]
      =Re[zeta'(s)/zeta(s)]+Re[1/(s-1)]
        +(1/2)Re psi(1+s/2)-(1/2)log pi.              (Z3)

This is the usual symmetric Hadamard identity. The real parts converge
absolutely here; the constant in the canonical product cancels by the
functional equation. It assumes no zero-free strip beyond Re s>1.

The absolutely convergent Euler product bounds
|zeta'(3/2+iq)/zeta(3/2+iq)|<=-zeta'(3/2)/zeta(3/2)<1.506.
The last numerical bound is the same explicit input used in Ford v5,
Lemma 3.2, page7; it is not a new numerical evaluation in this note.

For Re z=x>0, Euler summation for the digamma function gives

    psi(z)=log z-1/(2z)+E(z),
    |E(z)|<=(1/2) integral_0^infinity |t+z|^-2 dt.

For z=7/4+iq/2 and q>0, the integral is at most pi/q. Since
Re[-1/(2z)]<0, this yields

    Re psi(z)<=log|z|+pi/(2q).

Also

    (1/2)log|z|
       <=(1/2)log(q/2)+49/(16q^2),
    Re[1/(s-1)]<=1/(2q^2).

Consequently, for q>=10000, (Z3) is at most

    (1/2)log q+1.506-(1/2)log(2pi)
                 +pi/(4q)+57/(16q^2)
       <(1/2)log q+3/4.                             (Z4)

For example, the elementary bounds pi<4 and log(2pi)>8/5 give
an additive constant below .706101<.75. The bound log(2pi)>8/5
follows from pi>3 and exp(8/5)<6. This leaves substantial slack.

Combining (Z2) and (Z4), we obtain the explicit lemma

    sum_(|1+iq-rho|>1/2) |1+iq-rho|^-2
       <=2log(q+1)+3-4N(q,1/2),  q>=10000.           (Z5)

The use of log(q+1) makes (Z5) slightly weaker and matches the
frequencywise h_j in the weighted detector. Unlike the previous
bound, (Z5) has no loglog term.

## 3. Substitution and compatible kernel constant

Replace only (G6) in GENERAL_WEIGHTED_FORD_DETECTOR.md by (Z5).
Its gamma/remainder contribution is unchanged at 1.8+h_j/3.
Therefore (G8) remains valid after replacing

    3.5691*h_j+5.316*log(h_j)+17.934

by

    (7/3)*h_j+4.8.                                  (Z6)

The coefficient of the local count is still pi^2*c5-4*c4=-4/R0,
so that term can still be discarded. No zero-density estimate or
assumption about the horizontal locations of the zeros is used.

For theta=23/20, K=12, l>=60, and B<=.22, we may take R0=139:

    lambda=B/log(12t+1)<=.22/(60+log12)<1/280.

Thus eta=1/2>=(R0+1)lambda as required in (7.5). The resulting
c4 from (G1) is approximately1.07998041488, with its exact upper
bound delegated to the rational checker. The same local maximum-
principle proof (7.8) remains compatible with this sharper c4.

The monotonicity proof for the infinite tail is simpler after (Z6):
it only needs s_j/h0^2 and h0^-2 to decrease, already proved in
Section4 of the weighted detector. Any retained prime contribution
must be handled separately when deriving the endpoint reduction.

## 4. Kernel inputs for the separate retained-prime bound

For the cosine bump g above, g is continuous and compactly supported,
and g' belongs to L2. Hence w''=g'*g' is continuous and Cauchy--Schwarz
gives |w''(u)|<=||g'||_2^2=-w''(0) everywhere, including across the
support boundary. Direct integration (or differentiation of w) gives

    -w''(0)=sec(theta)^2*tan(theta)^2
                         [sec(theta)^2*theta*cot(theta)-1].

The exact checker at theta=23/20 proves

    w0>6, ||w''||_infinity<70, c4(R0=139)<1.08.        (Z7)

These are precisely the kernel inputs of the separate parent-derived
`../two-hour-root-20261023/FORD_COMBINED_PRIME_GAIN.md`. Its exact
four-prime Bernstein certificate supplies a gain
.255lambda-18lambda^3 in the left side of (G8). The two gains arise
from different original expressions: the present note bounds the
zero sum; the prime note retains terms in the Dirichlet sum and the
right-line Euler smoothing.

Let lambda_plus=A/h0. At the minimizing zero lambda=B/log(Kt+1),
and the positive prime gain must not be replaced blindly by its value
at lambda_plus. Instead first combine all linear terms at the actual
B. For the endpoint enclosure, with A replacing B in the adverse
terms, use

    .255*B/(h0+epsilon)>=.254999*B/h0,

because .254999*(60+epsilon)<.255*60. The cubic prime error is
bounded by18(B/h0)^3. Thus a sufficient endpoint margin is

    M_P(A,l)=b1*W(eplus)/w0-W(-1)/w0
      -.3334*pi^2*b1*A^2/(l*h0)
      -(A/h0){sum b_j[q(s_j)+10^-7]+.596001}
      -c4*(A/h0)^2{sum b_j[(7/3)*s_j+4.8]+1.8}
      -18*(A/h0)^3.                                (Z8)

Every adverse term is nonnegative and increasing in A, so B<=A
permits this endpoint substitution. Every adverse term decreases
with l>=60, by the monotonicities proved for (G11); the added cubic
term also decreases. Therefore M_P(A,60)>0 excludes every minimizing
zero at log-height>=60, not merely those at the sampled endpoint.

The exact-rational endpoint replay in `verify_general_ford.py`
checks, among other candidates, A=4/19 (R=19/4), l=60. The
complementary logistic rectangle remains a separate requirement.
The global zero-free theorem is not supplied by this component.
