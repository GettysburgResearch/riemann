# Smooth singleton support, growing orders, and the exact native remainder

**Status: proposed component mathematics with complete written proofs.** No full
fourth moment, improved zero-free boundary, generalized native hierarchy, or RH
proof is claimed. These proofs and their checker have the same author; an
independent mathematical review is still needed.

## 1. Object, conventions, and what is different

Work over the fixed field K=Q(sqrt(-3)). Prime indices always mean PRIME IDEALS;
two split ideals of the same norm remain distinct. Let S contain the fixed bad
primes. For squarefree ideals n coprime to S, the character chi_n(u) is the
product of its sextic local symbols, with its actual value zero when (n,u)>1.

Take X>=3 and coefficients a_n(u), supported on squarefree ideals Nn<=X, with
|a_n(u)|<=1. The coefficients may depend on the fixed physical row u; no large
sieve for row-independent arrays is invoked. For the native source one can take

    a_n(u)=mu_K(n) nu(n) chi_n(u) W(Nn/D) / max(1,||W||_infinity),

with X=max(3,bD) when the fixed window is supported in (0,b]. Masks and moving
exclusions are implemented by zero coefficients. Below, using a_n(u) to include
the character is convenient. Let A(u)=sum_n a_n(u).

For a Hermitian 2k-tuple t=(n_1,...,n_k;m_1,...,m_k), define

    c_p(t)=sum_i 1_{p|n_i}+sum_i 1_{p|m_i}.

A prime is a **singleton** if c_p(t)=1. This refers to TOTAL occurrence, not to
its left-minus-right charge, its parity, or its residual character conductor.
Let E_{k,y}(u) be the actual signed tuple sum in |A(u)|^(2k) restricted by

    every singleton prime has norm at most y.                 (1.1)

Let T_{k,y}(u) be the same selected sum with absolute values on all coefficient
products. Thus |E|<=T, and any further selector of modulus at most one is also
bounded by T. No positivity or probabilistic-projection assertion for E is used.

This strictly enlarges several earlier sectors. Smooth residual sextic
conductor (#936) and the moment with all small prime signs frozen and all large
signs randomized (#937) both satisfy (1.1). So does the old no-singleton sector.
However (1.1) also permits a large prime appearing three times and a small prime
appearing once. For k=2 the tuple (p q,p; p,1), with Np>y, Nq<=y and N(pq)<=X,
has this property. It is outside each of those three sectors. This witness
establishes strictness for the stated norm-cap theorem, not for every individual
fixed annular window. All prime exponents from 2 through 2k are permitted here.

The fixed-order mechanism is the classical squareful-product / Rankin count,
not a new general method in random multiplicative functions. What this packet
adds relative to the inspected sources is the larger complete native union,
explicit growing-order bounds without an unspecified C_k, and its exact
largest-singleton remainder with the original coefficients and physical rows.

## 2. The finite local factor and a uniform bound

Write L=log X. All logarithms are natural. For sigma>1/2 put r_p=(Np)^(-sigma).
Dropping the individual norm caps AFTER inserting their positive Rankin factors
proves

    T_{k,y}(u) <= X^(2k sigma)
       product_{Np<=y}(1+r_p)^(2k)
       product_{Np>y}[(1+r_p)^(2k)-2k r_p].                   (2.1)

It is harmless to enlarge the products to all prime ideals, including the fixed
bad primes or primes that divide u. Originally such a prime has local factor
one when its use has been masked out; adding it increases the positive bound.

Proof of (2.1). Each of the 2k squarefree columns either uses p once or does not
use p. At a small prime every subset of columns is allowed. At a large prime
all subsets except those of size one are allowed. Thus its exact local count is

    V_k(r)=1+sum_{j=2}^{2k} binom(2k,j) r^j
          =(1+r)^(2k)-2k r.                                (2.2)

The original tuple norm product is at most X^(2k), so its contribution to the
positive majorant is at most X^(2k sigma) times the product norm to -sigma.
The local products converge for sigma>1/2: V_k(r)=1+binom(2k,2)r^2+O_k(r^3).
All rearrangements are of nonnegative convergent series. No unfiltered signed
Euler product is substituted for the native finite polynomial. QED.

The following elementary estimate avoids constants exponential in 2^k. If
2k r<=1, then

    0<=log V_k(r)<=2 e k^2 r^2.                              (2.3)

Indeed binom(2k,j)<= (2k)^j/j!, and
sum_{j>=2}(2k r)^j/j! <= (2k r)^2 exp(2k r)/2.
Use log(1+z)<=z.

Consequently, whenever 2k y^(-sigma)<=1,

    log T_{k,y}(u) <= 2k sigma log X
       +2k sum_{Np<=y}(Np)^(-sigma)
       +2 e k^2 sum_{Np>y}(Np)^(-2sigma).                    (2.4)

The right side contains only field-dependent absolute constants in the estimates
below. In particular there is no suppressed factor C_k.

## 3. Elementary prime/ideal estimates used here

There are constants depending only on K such that, for z>=3,

    # {ideals a: Na<=z} <= C_K z,
    sum_{Np<=z}(Np)^(-1/2) <= C_K sqrt(z)/log z,               (3.1)
    sum_{Np>z}(Np)^(-1-a) <= C_K z^(-a)/a  (0<a<=1).         (3.2)

The first estimate follows from lattice counting and the class-number-one
Eisenstein norm. Each ideal has six generators differing by units. The last
estimate follows by enlarging primes to all ideals and partial summation; the
boundary at infinity vanishes and the lower-end subtraction can be dropped.

For the middle estimate, a rational prime has at most two ideals of norm p,
or one ideal of norm p^2. The elementary Chebyshev bound pi(t)<=C t/log t
therefore bounds the prime-ideal count the same way. Partial summation gives
(3.1). One can obtain Chebyshev by bounding the product of primes in (n,2n]
by binom(2n,n)<=4^n, summing dyadically, then separating primes below sqrt(t).
Neither the prime ideal theorem nor any zero-free assumption is needed.

## 4. Fixed-order diagonal scale for a larger native sector

**Theorem 4.1.** Set y=(log X)^2. For every fixed k and epsilon>0,

    T_{k,y}(u) <= C_{K,k,epsilon} X^(k+epsilon),              (4.1)

uniformly in u, all permitted coefficients and masks, and additional tuple
selectors. For any nonnegative row weights of finite mass Z,

    |sum_u w(u) E_{k,y}(u)| <= C_{K,k,epsilon} Z X^(k+epsilon).
                                                                    (4.2)

In particular Z=O(H) for every Eisenstein element norm ball Nu<=H. All element
rows, including imprimitive and sixth-power rows, are retained.

Proof. Take sigma=1/2+delta with fixed 0<delta<min(1/4,epsilon/(4k)). The finite
small-prime contribution in (2.1) has logarithm at most
C_{k,delta} y^(1/2-delta)=C_{k,delta}(log X)^(1-2delta)=o(log X),
even by the ideal counting bound instead of Chebyshev. The large-prime product
is bounded by a constant depending on k,delta: enlarge to all primes, separate
the finitely many for which 2k r>1, and use (2.3). Finally 2k sigma=k+2k delta.
Absorb the subpower term into the remaining epsilon. Summation over w is purely
positive accounting, not a row-distribution argument. QED.

## 5. Uniform growing moments through k<=log X

**Theorem 5.1.** There is an absolute field-dependent C such that, for all
sufficiently large X and every integer 1<=k<=log X,

    T_{k,(log X)^2}(u)^(1/(2k))
      <= X^[1/2 + (log log log X)/(2 log log X) + C/(log log X)].
                                                                    (5.1)

Every constant is independent of k, X, u and the coefficient vector. A zero
left side is allowed. Equivalently, the exponent in T itself is k+o(k), with
the o(k)/k tending to zero uniformly throughout the stated growing-order range.
For row averages replace T by Z^(-1) sum_u w(u) T whenever Z>0.

Proof. Let L=log X, v=log L, and suppose v>=2. Put

    delta=(log v)/(2v),   sigma=1/2+delta,   y=L^2.

Here 0<2delta<1. If Np>y and k<=L,

    2k (Np)^(-sigma) <= 2k/(L v) <= 2/v <=1.

Thus (2.4) applies. By (3.1) its small-prime contribution is at most C k L/v.
By (3.2), since y^(-2delta)=v^(-2), its last contribution is at most

    C k^2 /(v log v).

It follows that

    log T <= kL+2k delta L+C kL/v+C k^2/(v log v).            (5.2)

Divide by 2k. Since k<=L and log v>=log 2, absorb the last two terms into
C L/v. Exponentiating proves (5.1). QED.

This is a component upper bound, not the full moment premise required by the
zero detector. It also does not by itself identify X with a zeta zero's height.
For fixed k, Theorem 4.1 is the standard all-epsilon assertion; (5.1) additionally
prices the constants when k grows. No uniformity is asserted for the inherited
moment-to-zero theorem merely because this component has uniform constants.

## 6. A singleton-norm budget (another complete selected union)

Let U_y(t) be the product of all singleton prime ideals with norm greater than y.
For fixed k, impose N U_y(t)<=Z, with 1<=Z<=X^(2k). Then, for every epsilon>0,

    sum_{t: N U_y(t)<=Z} product_i |a_{n_i}(u) a_{m_i}(u)|
      <= C_{K,k,epsilon} X^(k+epsilon) Z^(1/2),               (6.1)

when y=(log X)^2. Additional selectors and nonnegative row weights are allowed.

Proof. Insert the extra positive Rankin factor (Z/N U_y(t))^tau, with tau=1/2,
and take sigma=1/2+delta as in Theorem 4.1. At a large prime the local factor is

    V_k(q^(-sigma)) + 2k q^(-sigma-tau).

The new linear series converges, because sigma+tau=1+delta>1. Its local logarithm
is bounded by 2k q^(-1-delta)+O_k(q^(-1-2delta)), apart from finitely many primes.
The small-prime factor is unchanged and is subpower. The prefactor is
X^(2k sigma) Z^(1/2), proving (6.1) after reducing delta. QED.

For Z=X^z the excess is z/2. Hence a cofinal singleton-norm budget z_k=o(k)
costs only o(k) at each fixed order. This does not show that the remaining
larger-singleton-norm tuples have small signed sum. It is an additional
quantitative way of delimiting the part that still needs arithmetic cancellation.

## 7. Exact largest-singleton rooting for the actual native source

Return to the unnormalized source

    A_u(D)=sum_{(n,S)=1} mu_K(n) nu(n) chi_n(u) W(Nn/D),

with squarefree columns and a real fixed W supported in (0,b]. All sums below
are finite. Give prime ideals a fixed total order refining norm; split primes
with equal norms have distinct positions. Let B be the initial segment Np<=y.
For each p outside B, define C_{p,u}(D) by summing over a 2k-tuple
(m,n_2,...,n_k;m_1,...,m_k) with ALL entries coprime to p and S:

- the first coefficient is mu_K(m) nu(m) chi_m(u) W(Nm/(D/Np));
- the other k-1 left coefficients and k conjugate coefficients are the original
  coefficients at scale D;
- among all these cofactor entries, no prime strictly AFTER p in the fixed order
  occurs exactly once.

There is no condition forbidding singleton primes before p. All original
composite cofactors remain. The physical row u is unchanged, and when p|u the
outside factor chi_p(u) is zero. A common moving exclusion q is retained by
requiring every cofactor to be coprime to q and omitting primes p dividing q;
no bound depending on q is used in this finite identity.

Let E_{k,y}(D,H) be the true signed moment sector of Section 1, now with native
coefficients and nonnegative row weights w_H. Then

    M_{2k}(D,H)
      = E_{k,y}(D,H)
        -2k Re sum_{p outside B} nu(p)
                      sum_u w_H(u) chi_p(u) C_{p,u}(D).       (7.1)

Proof. A tuple outside the selected sector has a unique largest singleton prime
p. It appears on exactly one of its 2k columns. If that column is on the left,
write it p m. Squarefreeness and unique occurrence require p to divide none of
the cofactor entries. Complete multiplicativity of nu and of the squarefree
symbol, and mu_K(p m)=-mu_K(m), give the displayed factor -nu(p)chi_p(u).
The cutoff is exactly W(Nm/(D/Np)), not W(Nm/D). The remaining selector is
precisely the one in the definition of C. There are k symmetric left positions.
Tuples rooted on the right give their complex conjugates. Adding proves (7.1).
No estimate, independence, limit or change of physical row measure is used. QED.

Theorem 4.1 has already paid |E| at H D^(k+epsilon). Therefore the one-sided
bound

    Re sum_p nu(p) sum_u w_H(u) chi_p(u) C_{p,u}(D)
                 >= -C_{k,epsilon} H D^(k+epsilon)           (OPEN-k)

would imply the full native diagonal moment. Conversely that moment bound and
the proved |E| bound imply (OPEN-k), with a changed constant. This is an exact
arithmetic target, not a weaker hypothesis masquerading as a proof.

At k=2 the factor in (7.1) is -4. No sign is asserted for an individual rooted
prime, and absolute values must not be moved inside the prime or row sums.
Complete-residue cancellation does not bound this short physical-row sum.

Compared with #937's exact sign-freezing flux, (7.1) uses the largest SINGLETON
rather than the largest odd-occurrence prime. All tuples with no large singleton
are already paid, including large primes occurring three or five times. This
removes a larger, absolutely bounded collection before the remaining signed
prime/cofactor estimate. It is not a proof of that estimate.

## 8. What would actually move 17/24

The existing extraction, with its own test and fixed-twist hypotheses, gives a
boundary 1/2+5h/(12k)+lambda/(2k) from a full moment excess lambda at H=D^h.
At k=2, the open target (OPEN-2) for arbitrarily small fixed h-1 would supply
lambda=0 and the strict half-plane Re(s)>17/24. It has NOT been proved here.

The growing-order result closes the bookkeeping of one larger sector, and the
root identity preserves exactly the prime/composite cancellation the earlier
prime-face obstruction requires. Neither randomization of that root sum nor
replacing its coefficient by an arbitrary bounded array supplies the missing
saving. The previous replica packet's unknown coherent source remains unknown.

## Sources and boundaries

- #932, c63b5aaa5d53dd183abb20299cea4628f0ab57b7: ordinary-zeta bridge and physical
  density warning; this is the publication base, not an analytic input here.
- #936, eb8d23decc003d36ded287dc98868308192cc889,
  standalone/2026-10-13-rough-conductor-localization/PROOF.md: Sections 1--3,
  the strictness example and Section 5 through (5.2) were read, together with
  the PR description. It already proves smooth residual
  conductor sectors by a Rankin local product. The fixed-k strategy is credited.
- #937, 9f3250198a9b0551f42eb73dfd74a265c2a66854,
  standalone/2026-10-13-prime-freezing-and-noise/PRIME_FREEZING.md: read in full.
  It supplies growing frozen signs and the exact odd-binomial return. Its
  (OPEN) lower bound is not assumed, and no priority for prime-rooting is claimed.
- Earlier no-singleton estimates and source-compatible rooting appear in
  #913/#918/#929/#930/#933. Their PR descriptions and the live cross-references
  above were inspected; this is not a complete historical file-by-file audit.
- Adam J. Harper, "Moments of random multiplicative functions, II: High moments",
  arXiv:1804.04114, is prior literature on uniform high-order random moments and
  hypercontractive methods. Its sharper model theorems are not invoked here.
  This packet does not claim to improve that theorem or establish global novelty.

All analytic estimates actually used in Sections 2--7 are proved here. Hashes
and finite tests authenticate bytes and finite algebra, not these asymptotic
inequalities, the imported extraction theorem, or RH.
