# Exact hyperbola completion does not give a power saving in coefficient energy

**PROPOSED, unconditional estimate-class obstruction.** This does not
lower-bound the full mixed character mean. It rules out the proposed
shortcut of combining the detector's dyads, invoking `mu*1=delta`, and
obtaining a polynomially smaller coefficient square mass before applying
a generic large sieve. Genuine signed row correlations remain available
and are not disproved here.

## 1. The actual corner has isolated semiprime coefficients

Take the complete synchronized coefficient of the inverse/plain corner

    c_A=L^(-1/2) nu(A)
          sum_(dn=A) mu(d) W_M(Nd/U)W_S(Nn/U^(1/2)),
    L=U^(3/2).                                         (1)

All original good ideals and nonunit zeros are retained. Suppose the
fixed annular profiles are nonzero: there are compact intervals
I,J inside their respective supports on which
`|W_M(x)|>=c_M>0`, `|W_S(y)|>=c_S>0`.
Their actual common norm twist does not change this assumption: its
modulus is uniformly bounded above and below on a fixed annulus for
the prescribed compact sigma range. If an inverse cutoff is included
in W_M, the interval I must lie in its nonempty support as well.

Let P,Q be good prime ideals with

    NP in U*I,    NQ in U^(1/2)*J.

For all sufficiently large U their norm ranges are disjoint. The only
divisor of PQ in the inverse U annulus is P. The other divisors are
1, Q, and PQ, whose norms respectively are bounded, of order U^(1/2),
and of order U^(3/2). Hence the COMPLETE coefficient is exactly

    c_(PQ)=-L^(-1/2)nu(PQ)W_M(NP/U)W_S(NQ/U^(1/2)).    (2)

It is not a coefficient of a selected contraction. No other term of
the same product is omitted. Unique factorization of ideals and the
disjoint prime ranges make all these products distinct.

There are `>>U/log U` such P and `>>U^(1/2)/log U` such Q. Therefore

    sum_A |c_A|^2 >= sum_(P,Q) |c_(PQ)|^2
                           >> 1/(log U)^2.             (3)

This lower bound is uniform in the common height. Fixed good-prime
exclusions remove only finitely many of the counted primes. Fixed
finite character values nu(PQ) have modulus one on this support.

The prime ideal interval input here follows directly from the ordinary
prime-number theorem in the progression `p=1 mod 3`: every such rational
prime splits into two distinct degree-one prime ideals of Z[omega].
Its asymptotic in each fixed relative interval supplies the stated
counts. One primary official reference is
[NIST DLMF 27.12.8](https://dlmf.nist.gov/27.12.E8), with fixed modulus 3;
the primary page was read directly. No short-interval or varying-ray
prime theorem is needed. We do not claim the same lower bound after an
arbitrary additional moving prime mask.

## 2. Combining every plain dyad still leaves the same coefficient

Let V be the actual smooth inverse cutoff: `V(x)=1` for 0<=x<=1,
`V(x)=0` for x>=2. Define the COMPLETED prefix-convolution coefficient

    b_V(A)=sum_(d|A) mu(d)V(Nd/U).                     (4)

It comes from the full inverse polynomial multiplied by the full plain
Dirichlet series, before any dyadic separation. The sum over every
dyad is an exact partition of (4), so changing the order in which those
dyads are estimated cannot change its coefficients.

Choose P with NP in [U/2,3U/4] and Q in a fixed relative interval at
U^(1/2). Then, for all sufficiently large U,

    b_V(PQ)=V(1/U)-V(NP/U)-V(NQ/U)+V(NPQ/U)
            =1-1-1+0=-1.                              (5)

Thus the literal `mu*1=delta` identity has not annihilated this entire
product range. It annihilates 1<NA<=U because every divisor there sees
V=1. At NA≈U^(3/2), the inverse divisor d=PQ is unavailable, and its
missing +1 is exactly what prevents the semiprime cancellation.
The two middle divisors both have sign -1; interchanging d and n
does not provide an opposite sign.

Multiplying (4) by a fixed nonzero product-annular profile and central
normalization L^(-1/2) gives the same lower bound (3), after choosing
fixed prime intervals whose products lie in a nonzero portion of that
profile. This is a lower bound for the complete coefficient vector,
not merely for one dyad before recombination.

For a fixed smooth product profile there can also be prime products
A of norm about L, with b_V(A)=1; those belong to the long-plain,
unit-inverse sector introduced by full completion. They provide a
separate coefficient lower bound of order 1/log U. That extra sector
is not present in the original corner (1), so it must not be used as
an alleged lower bound for the corner mean.

## 3. The precise class of estimates this prevents

Suppose an argument proposes to use only a generic large-sieve bound

    mean <= C_epsilon U^epsilon Xi(U,L) sum_A |c_A|^2,
    Xi(U,L)>=c L,

and seeks a bound `U^(q+epsilon)`, q<3/2, by deriving a power saving
for the coefficient square mass from hyperbola completion alone.
Equations (3) and (5) show why this cannot work: the right-side resource
is at least a constant times `U^(3/2)/(log U)^2` before any positive
small-power loss. The actual coefficient energy is not
`O(U^(-eta))` for any eta>0.

This is an obstruction to that NONNEGATIVE RESOURCE strategy. The
displayed large-sieve expression is an upper-bound resource; its size
does not lower-bound the true mean. Oscillation among the primitive
large-conductor correlations can still make that mean much smaller.
Such cancellation, rather than the literal low-product divisor identity,
is exactly what a successful improving mixed estimate must establish.

## 4. A sparse inverse cannot preserve the detector gate for free

There is an exact companion obstruction to replacing the full cutoff
inverse by a sparse finite Euler product. Let a(1)=1, and require

    sum_(d|A) a(d)=0 for every 1<NA<=T.                (6)

Then necessarily `a(A)=mu(A)` for every NA<=T. Induct on the integer
norm: each proper divisor has smaller norm, so

    a(A)=-sum_(d|A,d!=A) a(d)
         =-sum_(d|A,d!=A) mu(d)=mu(A).

The unit ideal starts the induction. Thus preserving the source's
exact low-product annihilation through T uniquely fixes all inverse
coefficients through that range. A finite Euler inverse supported on
small-prime products omits some prime P<=T; its convolution coefficient
at P is then 1, not zero. Such a sparse inverse can have a cheaper
moment, but the zero detector no longer forces its nontrivial witness
product to have norm at least T. This is a failure of the required
exact detector gate, not merely a weak estimate for the sparse inverse.
