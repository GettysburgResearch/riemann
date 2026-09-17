# Rational logarithmic-derivative comparators without integer multiplicities

MCE26, 2026-09-13. Proposed component arguments, requiring independent review.
No global native residual bound or RH proof is supplied.

Gaussian quadrature and its Pade connection are classical; see DLMF 3.5 and
18.40, and Allen--Chui--Madych--Narcowich--Smith, *Pade approximation and Gaussian
quadrature*. The construction below is given explicitly to make its hypotheses
and its permissible use in the repository unambiguous.

## 1. A finite positive comparator from two matrices

Let u_0,...,u_(2d-1) be real and suppose

    B0=(u_(i+j))_(i,j<d)>0, B1=(u_(i+j+1))_(i,j<d)>0.    (1)

Set T=B0^-1 B1, with inner product <x,y>_0=x^T B0 y. It is self-adjoint
and positive definite in that inner product. Let e0 be the first coordinate.
For j<d-1, B1 e_j=B0 e_(j+1), so T^j e0=e_j for j<d.
This proves cyclicity. Thus T has d distinct positive eigenvalues lambda_l
and positive spectral weights c_l=|projection_l e0|_0^2. Exactly,

    S(w)=e0^T B0 (I+wT)^-1 e0
        =sum_(l=1)^d c_l/(1+lambda_l w), c_l>0.         (2)

Its power series matches u_k through k=2d-1. For k<=2d-2, split k=i+j
with i,j<d and use self-adjointness and cyclicity:
<e0,T^k e0>=<T^i e0,T^j e0>=u_(i+j). For k=2d-1 use
<T^(d-1)e0,T T^(d-1)e0>=e_(d-1)^T B1 e_(d-1)=u_(2d-1).

For rational data no algebraic nodes need to be computed. Solve

    B0 (c0,...,c_(d-1))^T = -(u_d,...,u_(2d-1))^T,
    pi(x)=x^d+sum_(j<d)c_j x^j.

Then D(w)=(-w)^d pi(-1/w)=det(I+wT) and P is the degree-(d-1) truncation of
D(w) sum_(k<2d)(-1)^k u_k w^k. The coefficients of degrees d through 2d-1
in that product vanish EXACTLY, and S=P/D. All coefficients of D and P are
positive by (2). This gives a rational representation of the full comparator
with an algebraic proof of its pole and residue signs, not a floating eigensolve.

The delivered d=8 example uses u_k=200^(k+1)p_(k+1,Phi), rounded to rational
numbers with 60 decimal places. Both rational matrices are independently
checked positive. The variable in this example is t=w/200. Its numerator and
denominator and all exact moment identities are in result.json.

## 2. Why it is NOT automatically an NJT entire product

Formally integrating (2) produces

    G(z)=product_l (1-lambda_l z^2)^(c_l/lambda_l).      (3)

The exponents are positive, but need not be integers. Unless integrality or
other relevant structure is proved, (3) can have real-axis branch points.
For example S(w)=1/[2(1+w)] gives G(z)=sqrt(1-z^2). Positive moment matrices
do not turn that into an entire function. NJT's Newton-tail theorem must not
be applied to (3) as though it were a real-rooted polynomial.

Nevertheless, (3) is well-defined and holomorphic in the OPEN upper half-plane,
using the principal logarithm of every factor. For Im z>0, 1-lambda z^2
never lies on the nonpositive real logarithmic cut. The branches agree with
the positive values at z=iy and with G(0)=1 near the origin. This observation
allows a different, valid consumer.

## 3. A finite differential-residual zero exclusion test

Now use the unscaled convention in (2). Let F be even entire, F(0)=1, and set

    H(z)=D(-z^2)F'(z)+2z P(-z^2)F(z).                   (4)

H is entire even when the comparison G is not. Since G'/G=-2z S(-z^2),

    (F/G)'=H/[D(-z^2)G].                               (5)

For R>0 and 0<b<=R, take any z=x+iy with |z|<=R and y>=b. Join 0 to iR,
then x+iR, then z. This path has length <=3R and lies in |w|<=2R. Except for
the initial imaginary segment it has Im w>=b. On the imaginary segment,
|D(-w^2)|>=1 and |G(w)|>=1.

Write

    L=log G(4iR)=sum_l(c_l/lambda_l)log(1+16lambda_l R^2).

The quantity L also equals the real integral int_0^(16R^2) P(v)/D(v) dv.
The positive rational Stieltjes function P/D is decreasing there. Rational
left and right Riemann sums therefore give complete two-sided bounds for L
without computing a single algebraic node or a logarithm of one. An upper
bound for L may replace L everywhere in the sufficient inequality below.

The elementary factor estimate, including positive fractional weights, gives

    |G(w)|>=exp(-2L/3)(b/(2R))^(L/log2),
    |D(-w^2)|>=(b/(2R))^d.                              (6)

For the second bound, roots r_l=1/sqrt(lambda_l)<=4R give
|1-w^2/r_l^2|>=2b/r_l>=b/(2R); roots above 4R give at least3/4, which is
larger than b/(2R). For the first bound, split at r_l=4R. The near factors
have total exponent at most L/log2. For far factors use
-log(1-u/4)<=u/3 and log(1+u)>=u/2 with u=16R^2/r_l^2<1. Sum their weighted
costs. This is the same elementary growth-budget inequality as NJT, but its
use here is exclusively on the declared branch domain.

Consequently the completely explicit sufficient condition

    3R sup_(|w|<=2R)|H(w)| exp(2L/3)
                  (2R/b)^(d+L/log2) < 1               (7)

excludes every F zero with |z|<=R and |Im z|>=b. Integrate (5): it gives
|F/G-1|<1, hence F is nonzero. Reflection handles the lower half-plane.
There is no division by the UNKNOWN F, and no prior F zero-free hypothesis.
Pathwise estimates of the integral in (5) can replace the deliberately
conservative single supremum in (7).

### Pay the complete native Taylor tail in the residual

Suppose F(z)=sum (-1)^k f_k z^(2k) with f_k>=0. Let F_K be its truncation,
s=2R, M=F(2is)=F(4iR), and let U_K be the sum of the absolute coefficients
of D(-z^2)F_K'+2zP(-z^2)F_K, weighted by s to their full degrees. Then

    sup_(|z|<=s)|H(z)| <= U_K + M 4^(-K-1)
                        [2(K+1)D(s^2)/s+2sP(s^2)].     (8)

Indeed the omitted F tail is <=M4^(-K-1); the derivative tail is
<=2(K+1)M4^(-K-1)/s because k4^-k decreases for k>=1. The positive
coefficients of P,D bound their entire circular norms by their values at s^2.
All derivatives, polynomial degrees, and Taylor tails are retained.

Equations (1),(4),(7),(8) constitute a finite protocol with rational positive
comparators. They eliminate the integer-residue lifting problem but NOT the
native residual inequality. The current native d8 comparator is constructed;
no native successful (7) window is claimed. Synthetic exact product controls
verify (4) by two independent finite polynomial routes.

## 4. Relationship to the permanent moment test and the other routes

For global closure, MCE1 needs only cofinal native shift-two positivity, not
(7). The residual protocol is useful for a quantitative finite-window result,
or for studying how a native approximant deviates from its positive rational
comparator. Gaussian quadrature at one finite order cannot certify the next
native Hankel sign. Likewise #842's positive reciprocal subordinator supplies
factorial-weighted positivity, not the unweighted matrix required in (1).
No inference of the missing sign is made from either construction.

The Ising constructions remain valid, separate ways of obtaining entire
real-zero models. We have not replaced their exact finite moment results or
claimed that this rational comparator is an Ising magnetization. The original
arithmetic covariance upper bound remains unchanged and unproved.
