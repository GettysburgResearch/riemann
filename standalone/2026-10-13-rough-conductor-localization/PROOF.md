# Mask-preserving rough-prime projection and log-square conductor sectors

Status: proposed standalone mathematics, with complete elementary upper-bound
proofs and an explicitly named classical input for the sharpness example.
No independent review, formal verification, full native moment, improved
zero-free boundary, or RH proof is asserted.

Scope: every fixed even order, all element rows, the original squarefree
columns, arbitrary bounded column coefficients, and literal nonunit zeros.
The small-prime set may grow with the column scale. The counting theorem
allows arbitrary further tuple selectors. Its random-phase interpretation
requires the complete selected union.

Sources and comparisons are in SOURCES.md. In particular, PR #931 already
proved a fully independent-prime benchmark; this note does not claim the
random-multiplicative moment method as new. The additional statement keeps
all physical divisibility masks and arbitrary small-prime phases, and gives
an absolute native tuple bound with a growing residual-conductor restriction.

## 1. Definitions and the exact projection

Let K=Q(omega), omega^2+omega+1=0. Index columns by integral ideals, using
the repository's fixed generators when a character requires them. Exclude
a fixed finite set S containing the primes over 2 and 3. Each remaining
prime ideal p has a sextic character chi_p(u) with values in mu_6 union {0};
its value is zero exactly when p divides the element row u. The symbol on a
squarefree ideal is the product of these local symbols. Unit ideal values
are one. No convention assigns a nonzero value at a nonunit.

Fix k>=1, X>=3, and complex coefficients a_n supported on squarefree ideals
prime to S with Nn<=X, and satisfying |a_n|<=1. Define

    F_u = sum_n a_n chi_n(u).                                      (1.1)

The native coefficients mu_K(n) nu(n) W(Nn/D) are covered after dividing by
max(1, ||W||_infinity), with X=max(3,bD) for a fixed support cap b. No
smoothness is needed for the present component estimate. Moving exclusions
can be imposed by setting the corresponding coefficients to zero. The proof
also permits coefficients depending on the fixed row, subject to the same
pointwise support and absolute bounds; this is not a license to import a
row-independent large sieve for such coefficients.

Let B be any subset of the prime ideals of norm at most X outside S. For
every prime outside B introduce an independent uniform sixth root Z_p.
Only the finitely many primes occurring in columns need randomization. Set

    F_u(Z) = sum_n a_n chi_n(u) product_{p|n, p not in B} Z_p,
    J_{k,B}(u) = E_Z |F_u(Z)|^(2k).                                (1.2)

Every original chi_p(u), including each zero, remains in this formula. In
particular no zero is redrawn with probability 1/Np. The small-prime phases
are neither averaged nor assumed independent.

For a Hermitian tuple t=(n_1,...,n_k;m_1,...,m_k), write

    r_p = #{i:p|n_i},  s_p = #{i:p|m_i},
    f(t) = product_{p: r_p-s_p is not 0 mod 6} p.                   (1.3)

This is the good-prime support of the actual nonprincipal residual
character, not the product of all primes in the tuple. Primes with
r_p=s_p mod 6 can still impose a principal nonunit mask.

**Proposition 1.** J_{k,B}(u) is exactly the sum of the original Hermitian
tuple contributions for which every prime dividing f(t) belongs to B.
It is a nonnegative real number.

Proof. Expand the finite 2k-th power. The average of
Z_p^(r_p) conjugate(Z_p)^(s_p) is one when r_p=s_p mod 6 and zero otherwise.
All remaining coefficient factors and nonunit zeros are unchanged. The
nonnegativity follows from (1.2). This proof does not replace congruence
modulo six by literal equality. At k=6 the distinction is already necessary.

Define the larger, positive accounting quantity

    T_{k,B}(u) = sum_{t: supp f(t) subset B}
                 product_i |a_{n_i} a_{m_i}|
                 product_i |chi_{n_i}(u) chi_{m_i}(u)|.            (1.4)

Then 0<=J<=T. Any further tuple selector bounded in absolute value by one
has selected signed sum bounded by T. Such a selector need not preserve
the random-phase representation or nonnegativity.

## 2. An explicit uniform activity bound

Write

    sigma_X = 1/2 + 1/(2 log X),
    S_B(u;X) = sum_{p in B, p does not divide u} (Np)^(-sigma_X).

**Theorem 2.** There is a constant C_k, depending on k and the fixed field
but not on X, u, B or the coefficient vector, such that

    T_{k,B}(u) <= C_k X^k (log X)^(k^2) exp(2k S_B(u;X)).           (2.1)

The stronger pre-optimization inequality, for every sigma>1/2, is

    T_{k,B}(u) <= C_k X^(2k sigma) zeta_K(2sigma)^(k^2)
                  product_{p in B, p does not divide u}
                           (1+(Np)^(-sigma))^(2k).               (2.2)

Here C_k can be chosen uniformly for all sigma>1/2. Neither statement
assumes a zero-free region, a theta transformation, a native second
moment, or a large sieve.

Proof. In each tuple with all column norms at most X, insert the upper
bound X^(2k sigma)/product_i (Nn_i Nm_i)^sigma. Drop the separate norm caps
and the coefficient absolute values, and sum the nonnegative majorant over
all squarefree ideals. This is Rankin's elementary bound. The resulting
sum factors into local polynomials.

If p divides u, every tuple term using p is zero, so its local factor is
exactly one. If p does not divide u and p is in B, put r=(Np)^(-sigma).
The local factor is (1+r)^(2k). At a prime outside B it is

    L_k(r) = sum_{0<=a,b<=k; a=b mod 6} binom(k,a) binom(k,b) r^(a+b).
                                                                    (2.3)

Its constant, linear and quadratic coefficients are 1, 0 and k^2. For
0<=r<=1, the remaining nonnegative terms total at most 4^k r^3. Hence

    log L_k(r) <= k^2 r^2 + 4^k r^3,
    L_k(r) <= (1-r^2)^(-k^2) exp(4^k r^3).                       (2.4)

The sum over prime ideals of (Np)^(-3sigma) is bounded by
zeta_K(3/2), uniformly for sigma>1/2. The product of the exponential
remainders is therefore an absolute constant depending only on k and K.
Enlarging the other Euler product to all prime ideals gives (2.2).
All exchanges are between nonnegative convergent series. They are not
analytic continuations of a physical Euler product.

For completeness, zeta_K(1+delta) is O_K(1/delta), for 0<delta<=1.
The Eisenstein lattice has O(t) elements of norm at most t; since this
ring is norm-Euclidean, each ideal has a generator and there are exactly
six generators up to unit multiplication. Thus the number I_K(t) of
ideals of norm at most t is O(t). Partial summation gives
zeta_K(1+delta)=(1+delta) integral_1^infinity I_K(t)t^(-2-delta)dt
=O(1/delta). Values with delta>1 are bounded directly.
At sigma=sigma_X, X^(2k sigma)=e^k X^k and
zeta_K(2sigma)=O(log X). Finally log(1+r)<=r. This proves (2.1).

The same proof works for a fixed cyclic order m>=3 by replacing the
congruence in (2.3) by modulo m: its quadratic coefficient is still k^2.
For order two that coefficient instead equals k(2k-1). This distinction
must not be hidden in a claimed universal logarithmic factor.

## 3. A native diagonal-size sector at every fixed order

Let B_y contain all good prime ideals with norm at most y. If f(t)=1,
interpret its largest prime norm as one.

**Corollary 3.1.** Suppose y(X)<= (log X)^(2+o(1)). For every fixed k and
every epsilon>0,

    T_{k,B_y}(u) <<_{k,epsilon} X^(k+epsilon),                    (3.1)

uniformly in every row u, with the threshold allowed to depend on the
specified function y. In particular the assertion holds for
y=(log X)^2. The native complete moment sector P^+(f(t))<=y has the
required diagonal order, including arbitrary further tuple restrictions.
There is no separate upper bound on Nf(t) other than its original tuple
support bound X^(2k).

Proof. Fix sigma=1/2+delta<1, where delta>0 will be sufficiently small
in terms of epsilon and k. Prime ideals in the quadratic field above a
rational prime have at most two factors, of norms p or p^2. Even summing
over all ordinary integers in place of rational primes gives

    sum_{Np<=y} (Np)^(-sigma) <<_sigma 1+y^(1-sigma).

For the asserted y, the right side is (log X)^(1-2delta+o(1)), which is
o(log X). In (2.2) the finite-prime product is therefore X^o(1), while
zeta_K(2sigma) is a fixed constant. Choose 2k delta<epsilon/2 and absorb
the remaining o(1). This proves (3.1) without needing a prime number theorem.

For the specific choice y=(log X)^2, a more explicit consequence of (2.1)
is

    T_{k,B_y}(u) <= C_k X^k (log X)^(k^2)
                      exp(O_k(log X/log log X)).                (3.2)

Indeed the elementary Chebyshev estimate pi(t)<<t/log(2t), together with
partial summation, gives sum_{Np<=y}(Np)^(-1/2)<<sqrt(y)/log(2y).
One elementary route to that estimate is to bound the product of primes
in (n,2n] by binom(2n,n)<=4^n, sum dyadically to obtain theta(t)=O(t),
and then split the prime count at sqrt(t). The inert-prime contribution
is at most a harmonic sum and satisfies the same displayed upper bound.

If w(u)>=0 has finite mass Z=sum_{u!=0}w(u), summing (3.1) yields

    sum_{u!=0} w(u) T_{k,B_y}(u) << Z X^(k+epsilon).              (3.3)

For the hard norm ball Nu<=H, the lattice count gives Z=O(H). Thus, with
X=bD for a fixed column support cap, the complete smooth-residual-
conductor sector is O(H D^(k+epsilon)) at every H>=1. All sixth-power,
imprimitive and nonunit rows remain. No row-distribution estimate is used.

**Corollary 3.2 (the whole logarithmic-power tradeoff).** For fixed A>0
and y<=(log X)^A, put beta(A)=max(1/2,1-1/A). Then

    T_{k,B_y}(u) <<_{k,A,epsilon} X^(2k beta(A)+epsilon).          (3.4)

Choose sigma>beta(A) with 2k(sigma-beta(A)) small. Since
A(1-sigma)<1, the same proof makes the finite-prime product X^o(1).
If A is very small, take any sigma just above 1/2. This proves (3.4).
The threshold A=2 is sharp for a bound uniform in arbitrary retained
small-prime phases, in the sense of the next section.

## 4. Sharpness above log-square: an actual but unrestricted-height row

Only this section uses a classical prime-distribution input: there are
>>z/log z split rational primes p=1 mod 3 in [z/2,z] for sufficiently
large z. This follows, for example, from the explicit unconditional
q=3 theta bound stated by Bennett--Martin--O'Bryant--Rechnitzer in
arXiv:1802.00085v3. Their result is an external input, not reproved here.
It is not used in Sections 1--3 or 5.

**Proposition 4.** Fix A>2, k>=1, and a nonnegative fixed compact smooth
W that is at least one on [1,2]. There are unbounded scales D and retained
local unit phases for which the native-coefficient hybrid with nu=1,
y=(log D)^A, and the original Moebius coefficients satisfies

    E_Z |F_u(Z;D,W)|^(2k) >= D^(2k(1-1/A)-o(1)).                (4.1)

These phases can be realized by an actual Eisenstein element row, but the
construction supplies no near-linear or polynomial upper bound on its
norm. In particular (4.1) is NOT a counterexample to the physical moment
at H=D^(1+theta), nor a limitation on methods using that height condition.

Proof. Choose a large parameter T and set

    z=(log T)^A/8,       m=floor(log T/(A log log T)).

There are M>>z/log z prime ideals with prime norms in [z/2,z]; it is
enough to choose one ideal above each such split rational prime. Products
of m distinct selected ideals are squarefree and have norms between
(z/2)^m and z^m, both T^(1-o(1)), and at most T. Their number is

    binom(M,m) >= (M/m)^m = T^(1-1/A-o(1)).                     (4.2)

Partition these products among dyadic norm intervals. There are O(log T)
intervals, so one [D,2D] contains D^(1-1/A-o(1)) such ideals, with
log D~log T. Consequently z< (log D)^A for all sufficiently large T.

Set chi_p(u)=-1 at every retained prime of norm at most y, and make every
prime appearing in the finitely many physical columns a unit at u. At
each good prime a nonzero residue with the specified sextic symbol exists.
The Chinese remainder theorem realizes all these finitely many choices
in an element u; exclude u=0 by choosing a nonzero representative.

Every y-smooth squarefree coefficient then has mu_K(n)chi_n(u)=1.
A coefficient with any prime above y has zero random-phase expectation.
Thus E F_u(Z;D,W) is the nonnegative sum of W(Nn/D) over all y-smooth
squarefree ideals, at least the count in (4.2). Jensen's inequality gives
(4.1). Notice that this uses the literal native Moebius coefficients,
not an unrelated coefficient vector, but only at an unrestricted-height
row. This proves the asserted optimality of the exponent in (3.4).

## 5. The remaining native estimate: rough Kummer-block interference

There is an exact block form of the new projection. For a k-tuple of
columns, retain the vector of prime exponents outside B modulo six,
denoted r. Put

    C_r(u) = sum_{(n_1,...,n_k) with rough charge r}
                      product_i a_{n_i} chi_{n_i}(u).

These are finite sums. All phases and masks stay inside their original
coefficients. Finite Fourier orthogonality and evaluation at Z_p=1 give

    J_{k,B}(u) = sum_r |C_r(u)|^2,
    |F_u|^(2k) = |sum_r C_r(u)|^2.                              (5.1)

For k<=5, equal rough charges mean equal rough ideal products. For k>=6
one must retain the additional sixth-power aliases. It is incorrect to
drop them. For example, E_{Z in mu_6}|1-Z|^12=926, whereas retaining only
literal equal powers gives binom(12,6)=924.

For an actual nonnegative row measure w, define

    R_{k,B}(X,w) = sum_u w(u) sum_{r!=s} C_r(u) conjugate(C_s(u)).
                                                                    (5.2)

This number is real and the exact moment is

    M_{2k}(X,w) = sum_u w(u) J_{k,B}(u) + R_{k,B}(X,w).          (5.3)

For B=B_y in Corollary 3.1, the first term is already O(Z X^(k+epsilon)).
Moreover R>=-sum_u w(u)J, so the negative side is already of diagonal
size. The only missing estimate is the one-sided upper bound

    R_{k,B_y}(X,w) << Z X^(k+epsilon).                          (5.4: OPEN)

At the native row height and test this is still unproved, even for k=2.
Equation (5.4) is equivalent to the full native upper moment at that
same height, because the projected term is bounded and nonnegative.
Unlike the earlier fully independent reference, this reference changes
no small-prime phase and no nonunit mask. It removes one possible
ambiguity in the comparison, not the central arithmetic difficulty.

### The attempted next step and its exact cost

For any fixed u, Cauchy gives

    |sum_r C_r(u)|^2 <= R_count(u) sum_r |C_r(u)|^2.             (5.5)

There are at most O_K(X)^k rough blocks, since there are O_K(X) columns.
Consequently this bound only returns O_k(X^(2k+epsilon)), not the desired
X^(k+epsilon). Even the improved pointwise theorem for the block diagonal
does not pay the native off-block cancellation. There is no asserted
improvement to the existing full-moment envelope.

In particular, conditioning the physical row measure on all residues at
primes up to y=(log X)^2 is not a free way to use a row-independent sieve:
the associated product modulus can be much larger than the physical row
range. The block coefficients also depend on the retained physical phases.
Neither obstacle is removed by the bound for their diagonal energy.

The finite arithmetic experiments in results/exact.json have both positive
and negative values of the rowwise remainder. At D=H=64, cutoff y=13,
the exact total native fourth moment is 153108, its projected contribution
is 155076, and the remainder is -1968. This is a bounded example showing
why positivity cannot be silently assigned to (5.2); it is not evidence
for an asymptotic estimate.
