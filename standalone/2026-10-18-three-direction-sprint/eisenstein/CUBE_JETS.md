# Complete cube jets and their growing-order cost

**PROPOSED component mathematics.** This is a consequence of the exact
all-prime deformation in CUBE_TILT.md. It does not improve the zero-free
boundary. In particular a derivative of the actual cube weight is not a
derivative of the whole quotient H/ zeta.

Write psi=vartheta^3 and let n be an exterior integral ideal. For n!=1,
the exact convolution coefficient of CUBE_TILT.md is

    c_v(n)=psi(n)/(Nn) sum_(d|rad n) mu_F(d)(Nn/Nd)^(-v).       (1)

Here rad n is the product of its distinct prime ideals. Formula (1)
follows prime by prime from the geometric local coefficient
`-(1-Q^(-v)) psi(P)^j Q^(-j-(j-1)v)`. No squarefree restriction on n
is imposed. For n=1, c_v(1)=1 for every v.

Define the generalized ideal von Mangoldt coefficient

    Lambda_j(n)=sum_(d|n)mu_F(d)(log(Nn/Nd))^j, j>=1.

Termwise differentiation is legal in the original complete Gaussian sum:
any fixed log power is absorbed by its lognormal tails, uniformly on
compact sets of v. Therefore

    d_v^j c_v(n)|_(v=0)=(-1)^j psi(n)Lambda_j(n)/(Nn), j>=1. (2)

The response is supported on omega(n)<=j, and

    0<=Lambda_j(n)<=(log Nn)^j.                              (3)

An explicit proof of both facts avoids any positivity hypothesis on the
Gauss vector. Factor n=product P_i^(a_i) and put u_i=log NP_i. Expand
`(sum_i a_i u_i)^j` as a sum of nonnegative ordered j-fold monomials on a
LABELLED alphabet with a_i copies of u_i. Designate one copy at each prime.
Subtracting log Nd deletes those designated copies. Inclusion-exclusion
therefore retains exactly the tuples using every designated copy at least
once. No tuple survives if omega(n)>j, and the surviving nonnegative
subcollection has total at most the unrestricted expansion. For j=1 this gives precisely the ordinary
ideal von Mangoldt function: only prime powers survive.

The j-th actual probe is consequently

    B_[j](m;Z)=(-1)^j sum_n psi(n)Lambda_j(n)/(Nn)
                     chi_n(m)^3 B_m(Z/(Nn)^3).             (4)

Its other exact description is to multiply the ORIGINAL cube variable by
`(-log Nn)^j`, leaving the squarefree c coefficient unchanged. All shared
primes and all nonunit character zeros in (4) remain present.

## Finite-order detection without a zero-multiplicity assumption

At a principal Mellin point s with Re s>1/2, the physical numerator is

    H_v(s)=L^S(6s-3+2v,vartheta^6) R_v(s).

The regular factor R_v(s) is holomorphic and nonzero near v=0. The angular
Hecke L-function is entire and is not identically zero, so v->H_v(s)
cannot vanish to infinite order. At every zero rho of ordinary zeta in
this half-plane there is therefore some FINITE j for which

    d_v^j H_v(rho)|_(v=0) !=0.                              (5)

The corresponding quotient `(d_v^j H_v|_0)/zeta` retains that zero as a
pole; the derivatives in (5) do not act on zeta. The required j can depend
on rho, and no uniform multiplicity bound is asserted. Statements about
all finite orders consequently need either bounds for every fixed j or
an explicit growing-order resource. A fixed positive deformation
v>=1/2 already supplies a single zero-safe numerator; (5) is an alternate
description of the detector family, not an analytic improvement.

## Uniform normalized jets have a visible scale price

For any fixed 0<r<1/2, normalize the j-th probe by r^j/j!. Equation (3)
and the exponential series give, SIMULTANEOUSLY for every j>=1,

    (r^j/j!) Lambda_j(n)/(Nn) <= (Nn)^(-1+r).               (6)

The bound is uniform in j. It explicitly pays for growing derivative
order rather than assuming that logarithmic derivatives have fixed norm.
On a filter dyad Nn approximately N, the two signed bounds proved in
HYBRID_MOMENT.md consequently acquire the factor N^(2r):

    Z^epsilon P^(1/2) [D N^(2r-1)+(D^2P/Z)N^(3+2r)],
    Z^epsilon P^(1/2) [DZ N^(2r-4)+Z N^(2r-3)].           (7)

No number of jets is hidden in (7): it bounds each normalized jet
uniformly in j. The coefficients differ by column phases, but the
collapsed quadratic-sieve lemma permits those phases. The complete
Gaussian filter tail is still uniform in j by (6), choosing its Gaussian
power after r and the desired tail order.

Balancing the first reflected term with each primal term gives

    Z^epsilon P^(1/2) [D
      +D^((11-2r)/7)P^((4-2r)/7)Z^((4r-1)/7)
      +D^(1-2r/3)P^(1/2-r/3)Z^(2r/3)].                  (8)

For example the first balance uses the power
`theta=(4-2r)/7` in `min(A N^(3+2r),B N^(2r-4))
 <=A^theta B^(1-theta)`, where A=D^2P/Z and B=DZ.
The second uses theta=(3-2r)/6 with B=Z. Since 2r<1,
the baseline D N^(2r-1) is bounded by D for N>=1.

On the actual compact-shape row box with PD<<Z^M, M>1, the resulting
uniform-j complete moment is

    sum_m |(r^j/j!)B_[j](m;Z)|^2
       <<_(r,epsilon) Z^(E_r(M)+epsilon),
    E_r(M)=min(((11-2r)M+4r-1)/7, M+1).                  (9)

The first balanced term in (8), after P^(1/2), equals
`(PD)^((11-2r)/7) P^(-1/2) Z^((4r-1)/7)` and is bounded as claimed.
The second has exponent at most `M+(2-M)r/3`, which is smaller: their
exponent difference is `((12+r)M-2r-3)/21>0` for M>1.
The envelope M+1 follows by summing the primal estimate alone; its
N-exponents remain summable for r<1/2. Every omitted tail is paid exactly
as in HYBRID_MOMENT.md with the coefficient majorant (6).

For 1<M<2 the additional uniform-order price in the first exponent is
`r(4-2M)/7>0`. It tends to zero as r decreases, while the normalization
r^j/j! becomes smaller. Thus one may state a uniform normalized-jet
result with an arbitrarily small exponent loss, but one may not discard
the j-dependent normalization or infer a stronger source estimate.
As with the positive cube deformation, the physical comparison still
gives no new critical-strip boundary.
