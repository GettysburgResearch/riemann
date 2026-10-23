# Low-frequency agreement and a quantitative ordinary sieve tail

Status: proved corollary of `NONCONSTANT_ORDINARY_SECTOR.md`. The scope is
the ordinary spherical nonconstant sector at the cusp infinity, with the
same explicit reciprocal-zeta factor. No metaplectic bridge or improved
zero-free boundary is asserted.

Use all notation and normalizations of that note. In particular k belongs
to Z[i], Nk=|k|^2, s=u+it with 0<u<=1, and the coefficient of E_(d^2)
at the nonzero frequency k vanishes unless d divides (k). Let

    V_R = sum_(d squarefree good, Nd<=R) mu(d) v_d,
    F_R = E[V_R]^nc,
    G_R = E[V_R^2]^nc.

The superscript nc removes both ordinary constant terms. G_R is induced
from the pointwise square of the finite section; it is not |E[V_R]|^2.

## 1. Exact agreement at every low frequency

Write the lcm coefficient of the squared section as

    lambda_R^(2)(l)
      = sum_(Nd,Ne<=R, lcm(d,e)=l) mu(d)mu(e).

If Nl<=R, every d,e dividing l is present. At each prime dividing l, the
three membership choices contribute -1,-1,+1. Consequently

    lambda_R^(2)(l)=mu(l)  whenever Nl<=R.                  (1)

At the unit ideal both sides equal one. The complete lcm convolution is
the same identity without a cutoff; it is the arithmetic form of the
idempotence of the full local product of (1-v_p).

For a nonzero frequency k with Nk<=R, every l contributing to its Fourier
coefficient divides (k), and therefore Nl<=R. Formula (1) proves

    Fourier_k(G_R-F_R)=0  for 0<Nk<=R.                     (2)

In fact it suffices that the product of the distinct good prime divisors
of (k) have norm at most R. Statement (2) is a convenient weaker version.
There has been no estimate or cancellation between different k in (2).

For the remaining frequencies, the difference array satisfies

    |lambda_R^(2)(l)-mu(l)1_(Nl<=R)|<=4^omega(l).            (3)

Indeed the first term is at most 3^omega(l), and 3^m+1<=4^m for m>=1;
the difference at l=1 is zero. Thus the same uniform divisor bound as in
Theorem 4 of the preceding note applies, with the fixed value A=4.

## 2. Arbitrarily high power decay, with all scale costs displayed

**Corollary.** For every epsilon>0 and real M>=0,

    ||G_R-F_R||_(L2(C/O))^2
       <<_(u,epsilon,M)
          R^(-M) (1+|t|)^(6-4u+2M+epsilon)
          y^(2u-2-2M-epsilon) / |zeta_K(u+it)|^2.           (4)

This is uniform in R>=1, real t and y>0. It has the same convention at
zeros and poles of zeta_K as Theorem 5 of the preceding note.

*Proof.* Parseval, (2) and (3) give the same sum as (11) in that note,
now restricted to Nk>R. On this set insert

    1 <= (Nk/R)^M = |k|^(2M) R^(-M).

The weighted lattice exponent in its proof changes from
L_0=4-2u+epsilon to L_0+2M. The logarithmic-annulus Sobolev inequality,
the exact Bessel product integral, and the derivative identity still apply:
their convergence conditions only improve. They contribute the additional
factor y^(-2M)(1+|t|)^(2M). The Gamma exponential cancellation is unchanged.
This proves (4). QED.

Relative to the complete nonconstant bound, the extra factor is

    [(1+|t|)^2/(R y^2)]^M.                                (5)

The gain is therefore effective when R y^2 is large compared with the
square of the spectral height. For fixed regular s and fixed y>0, the
difference tends to zero faster than any prescribed power of R. In a
moving-height or moving-spectral application, all factors in (4) must be
paid; an inverse scale saving does not follow automatically.

## 3. A common nonconstant Fourier limit

There is also a well-defined nonconstant Fourier series F_infinity whose
normalized kth arithmetic coefficient is the finite divisor sum

    b_infinity,s(k) = sum_(d|rad_good(k)) mu(d)b_(d,s)(k).

Theorem 4 bounds this by (Nk)^((1-u)/2+epsilon), and the Bessel decay
makes the Fourier series converge at every fixed regular s and y>0. It
also converges in L2(C/O), by the Parseval bound in Theorem 5.

For Nk<=R, both F_R and G_R have exactly this coefficient. The differences
of their arithmetic arrays from mu(l) are bounded respectively by
1 and 4^omega(l). The proof of (4) thus gives the same right-hand side
for each of

    ||F_R-F_infinity||_2^2,
    ||G_R-F_infinity||_2^2.                                 (6)

This defines a common limit only for the nonconstant Fourier sector.
The incoming coefficients of E[V_R] and E[V_R^2] are respectively the
summatory Mobius function M_K^S(R) and its square; no convergence or
cancellation of these terms is supplied here. Nor does
(6) identify the Fourier limit with an unproved metaplectic unfolding or
with a continuous cusp-evaluation map on the infinite finite-cover space.

## 4. Exact finite check and analytic scope

`verify_ordinary_fourier.py` checks the complete lcm Mobius identity, the
three-choice and four-choice coefficient bounds, and exact agreement of
the two cutoff series with the complete local divisor sum whenever the
good radical of k is inside the cutoff. These checks use exact rational
arithmetic. They do not certify the Bessel integral, contour continuation,
or a zero-free theorem; those analytic steps are the proofs stated above
and in the preceding note.
