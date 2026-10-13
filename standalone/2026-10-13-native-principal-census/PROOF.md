# The complete principal sector: physical masks, densities and sixth-power aliases

**Status: PROPOSED component mathematics.** The proof below estimates the entire
principal sector, not the nonprincipal covariance. No new full fourth-moment
bound, higher-moment hierarchy, zero-free boundary or RH proof is asserted.
The proof and software have the same author and await independent review.

This is a return from the coefficient classifications of #935/#939 to the
actual physical moment. Orthogonal independent-prime benchmarks, principal
kernels and squarefull-product counting are established tools in the earlier
packets. The contribution here is the explicit all-order physical-density
error, including unrestricted Liouville columns, and a complete finite census
which evaluates the true principal reference rather than an unmasked surrogate.
No broad novelty claim is made for Poisson summation or the counting method.

## 1. Exact object and quantifiers

Let K=Q(omega), omega^2+omega+1=0, embedded in C. Its integer lattice has
covolume v_K=sqrt(3)/2. All column indices are integral IDEALS. The fixed bad
set contains the primes over 2 and 3. At every other prime ideal p, chi_p(u)
is the sextic residue symbol, zero exactly when p divides the element u.
Extend to ALL ideals by chi_n(u)=product_{p^e || n} chi_p(u)^e, with the
literal rule 0^e=0 for e>0 and unit-ideal value one.

Fix k>=1 and X>=2. Let c_n be complex coefficients, independent of u, with
|c_n|<=1 and support Nn<=X outside the excluded primes. Arbitrary further
column exclusions are allowed. Define

    F(u)=sum_n c_n chi_n(u),
    M_(2k)(w)=sum_{u!=0} w(u)|F(u)|^(2k).

The coefficients may depend on X and on fixed auxiliary data. They may NOT
depend arbitrarily on the physical row in the density approximation below.
The original Mobius coefficients and the extended Liouville coefficients
are both included, after division by a fixed test's supremum norm.

For a Hermitian tuple t=(n_1,...,n_k;m_1,...,m_k), set

    a(t)=product_i c_(n_i) conjugate(c_(m_i)),
    E_p(t)=sum_i v_p(n_i),    F_p(t)=sum_i v_p(m_i),
    Q(t)=rad(product_i n_i m_i).

Call t principal if E_p(t)-F_p(t)=0 modulo 6 at EVERY good prime. On such a
tuple its exact row character is 1_{(u,Q(t))=1}, not identically one. Put

    P_(2k)(w)=sum_(t principal) a(t) sum_{u!=0,(u,Q(t))=1} w(u),       (1)
    delta(Q)=product_{p|Q}(1-1/Np),
    B_(2k)=sum_(t principal) a(t) delta(Q(t)).                        (2)

Both quantities are real and nonnegative when w>=0. For (1), keep every
physical zero fixed and multiply each good-prime phase by an independent
uniform sixth root; the conditional moment is exactly the selected sum.
For (2), independently at each prime choose zero with probability 1/Np,
and otherwise a uniform sixth root. Expansion of the moment gives (2).
These interpretations establish positivity of the COMPLETE selected sums,
not of every tuple for arbitrary complex coefficients.

The full physical moment is exactly

    M_(2k)(w)=P_(2k)(w)+R_(2k)(w),                                (3)

where R contains every nonprincipal tuple and is real. There is no asserted
sign for R. A physical moment theorem requires its one-sided upper bound;
the identity is not an estimate for that remainder.

## 2. The all-order counting input, also for nonsquarefree columns

**Lemma 1.** For each fixed k and epsilon>0,

    sum_(t principal) |a(t)| <<_(K,k,epsilon) X^(k+epsilon).        (4)

The same upper bound holds if the sole restriction is that the total product
of the 2k columns is squarefull (each occurring prime has total exponent >=2).

**Proof.** A prime of total exponent one would have charge +1 or -1, so no
principal tuple has such a prime. The total product N has norm at most X^(2k).
Every squarefull ideal has a unique representation N=A^2 B^3 with B squarefree:
an even prime exponent is put in A^2; an odd exponent, necessarily >=3, has
one exponent in B and its remaining even part in A. Thus the number of such
ideals of norm <=Y is at most

    C_K Y^(1/2) sum_B (NB)^(-3/2) <<_K Y^(1/2).

Here the elementary lattice bound for the number of ideals of norm <=T is
O_K(T). Each total product has at most d_(2k)(N) ordered ideal factorizations.
For fixed k and any eta>0, d_(2k)(N)<<_(k,eta)(NN)^eta. One elementary proof
uses d_r(p^e)=binom(e+r-1,r-1): for sufficiently large prime norms this is
bounded by (Np)^(eta e), uniformly in e; the finitely many small primes
are bounded separately, since their exponential denominator dominates the
polynomial in e. Take Y=X^(2k) and reduce eta. Individual norm caps and
coefficient absolute values can only decrease the count. This proves (4).

The argument is not restricted to squarefree columns. It therefore covers
the Liouville completion without discarding its higher prime powers. QED.

Also tau(Q(t)) << X^eta for any fixed eta>0, after adjusting the implied
constant, since NQ(t)<=X^(2k). Consequently inserting tau(Q(t)) into (4)
costs only an arbitrarily small further power of X.

## 3. Uniform physical-density theorem

Let Phi be a fixed nonnegative Schwartz function on C and write

    w_H(u)=Phi(u/sqrt(H)),
    c_Phi=(1/v_K) integral_C Phi(z) dx dy.

**Theorem 2 (smooth physical rows).** For every fixed k, epsilon>0 and Phi,
uniformly for X>=2, H>=1, the coefficient arrays above and their exclusions,

    P_(2k)(w_H)=c_Phi H B_(2k)+O_(K,k,epsilon,Phi)(X^(k+epsilon)). (5)

In particular P_(2k)(w_H)<< H X^(k+epsilon). The error in (5) has no factor
H^(1/2). This is an ABSOLUTE error, not a uniform relative error when B is
small. Constants may depend on k; no growing-order uniformity is claimed.

**Theorem 3 (sharp norm ball).** For w_H(u)=1_{0<Nu<=H},

    P_(2k)(w_H)=(2pi/sqrt(3)) H B_(2k)
                     +O_(K,k,epsilon)(sqrt(H) X^(k+epsilon)).    (6)

The sharper smooth error (5) is not substituted for the sharp error (6).

### Proof of the row-counting statements

For a squarefree ideal Q, inclusion-exclusion is exact:

    C_Q^Phi(H)=sum_{d|Q} mu_K(d)
                    sum_{v!=0} Phi(d v/sqrt(H)).                (7)

Choose any generator of each d. Its norm is Nd and its phase only rotates
Phi. Thus the inner sum is a rotated-lattice sum at t=H/Nd. The rotation
has no effect on its area integral or on uniform Schwartz seminorm bounds.

The classical Poisson summation formula on the fixed lattice gives, for t>=1,

    sum_{v!=0} Phi_rot(v/sqrt(t))=c_Phi t+O_Phi(1).               (8)

For completeness, the zero dual frequency is c_Phi t; the nonzero dual
sum is bounded by C_M t sum_{xi!=0}(1+sqrt(t)|xi|)^(-M), which is bounded
uniformly when M>4. Removing the original zero row subtracts Phi(0), also
bounded. For 0<t<=1, Schwartz decay bounds the original nonzero lattice
sum by C_M t^(M/2) sum_{v!=0}|v|^(-M)=O_Phi(1), and c_Phi t is bounded.
Therefore (8) holds for EVERY t>0, uniformly in the rotation.

Insert (8) in (7):

    C_Q^Phi(H)=c_Phi H delta(Q)+O_Phi(tau(Q)).                    (9)

This step retains divisors d with Nd>H: their small-t contributions are
handled by the uniform estimate, not dropped from the density product.

For the sharp ball, elementary lattice geometry gives

    R_K(t):=#{v!=0:Nv<=t}=(2pi/sqrt(3))t+O_K(sqrt(t)+1)          (10)

for every t>0. Covering the disk by fundamental cells leaves only O(sqrt(t)+1)
boundary cells, which proves (10) without a circle-problem estimate. Exact
scaling of the ideal lattice gives

    C_Q(H)=sum_{d|Q} mu_K(d) R_K(H/Nd)
          =(2pi/sqrt(3)) H delta(Q)+O_K(sqrt(H) tau(Q)), H>=1.   (11)

Sum (9) or (11) over principal tuples. Lemma 1 and its divisor-weighted
version bound the total error, proving (5)-(6). Nonnegativity and (4) also
bound B. The only analytic transform used is standard Poisson summation;
no zero-free theorem, theta foundation, large sieve, or RH premise enters.

## 4. Exact finite formula: charge AND support

Form the actual ordered product coefficients

    v_m=sum_(n_1 ... n_k=m) product_i c_(n_i).

For each product ideal m keep BOTH

    r(m)=product_p p^(v_p(m) mod 6),      S(m)=rad(m).

Character equality away from zeros is classified by r; literal nonunit
zeros still depend on S. The exact principal reference over the sharp ball is

    P_(2k)(H)=sum_(m,n:r(m)=r(n)) v_m conjugate(v_n)
                             C_(lcm(S(m),S(n)))(H),             (12)
    C_Q(H)=sum_{d|Q} mu_K(d) R_K(floor(H/Nd)).                   (13)

The floor in (13) is legitimate because ideal norms are integers. A divisor
with Nd>H has R_K=0. Distinct ideals with the same norm remain distinct in
(12); only AFTER a divisor ideal has been selected may its norm be used in
(13). Two different divisors of equal norm contribute with their multiplicity.

**Proof.** Expand F(u)^k by product ideals. A pair m,n has principal residue
character exactly when its charges agree. At that pair the surviving zero
mask is the union of their supports. Apply (13), which is (7) for the sharp
ball; multiplication by a generator of d bijects nonzero lattice elements
and nonzero elements of the ideal d. This proves the formulas.

**Corollary 4 (exact prime-phase invariance of the reference).** Let rho be
completely multiplicative with rho(p) a sixth root of unity at every retained
prime. Replacing c_n by rho(n)c_n leaves BOTH principal references (1) and (2)
unchanged, at every fixed order. Indeed each retained pair in (12) has equal
sixth charge, so rho(m) conjugate(rho(n))=1. In particular multiplication by
Liouville leaves the complete principal sector unchanged. The Mobius and
unsigned-squarefree censuses therefore have exactly the same principal
reference, even beyond the orders where equal product is sufficient. This is
an invariance of the reference, not of the physical moment. It pinpoints why
principal-sector estimates alone cannot exploit the special Mobius signs.

For native Mobius or Liouville coefficients with trivial fixed twist and a
nonnegative column window, v_m has sign (-1)^(Omega(m)). Products with equal
sixth charge have the same sign. Hence every term in (12) is nonnegative
for those particular coefficients. This permits the unsigned factorization
profiles in census.py. Arbitrary complex coefficient arrays would instead
require their actual complex v_m; the numerical implementation does not
pretend to cover arbitrary twists.

For squarefree columns and k<=5, v_p(m),v_p(n)<=5, so r(m)=r(n) forces m=n.
At k=6, this implication fails. For unrestricted Liouville columns it can
already fail at the fourth moment: columns p^3 and q^3, for the two distinct
ideals over 7, lie in the D=512 window. The pair products p^6 and q^6 have
zero charge but DIFFERENT nonunit masks. In the complete D=H=512 census,
these aliases add exactly 2748 to the Liouville fourth reference.

The memory-bounded fourth-order implementation assigns each ideal prime its
own distinct symbolic rational prime label. The resulting integer code is
injective by ordinary unique factorization. These labels are not ideal norms.
A representative factor pair recovers the true ideal support. Only products
containing an exponent at least six can create a nontrivial charge collision;
the remaining canonical product, when present, is then joined explicitly.
This is an algorithmic compression, not an additional arithmetic hypothesis.

## 5. What the estimate does NOT prove

For the original smooth-column Mobius polynomial, Theorem 2 pays the complete
principal part at H D^(k+epsilon), with its exact source masks. The missing
estimate is still

    R_(2k)(D,H) <= C_(k,epsilon) H D^(k+epsilon),                 (OPEN)

at the required near-linear heights, twists and test uniformity. Absolute
values on R are unnecessary for this upper implication, but no one-sided
bound is proved here. Replacing R by zero, by a single sign, or by a generic
independent-prime comparison is invalid. Exact hard-window examples give
R_4=36 at D=H=16 and R_4=-15252 at D=H=128.

The finite data use the HARD window D/2<Nn<=D, not a C-infinity test. They do
not establish a smooth-test asymptotic, a rate of decay, or any new zero-free
exponent. Even accurate agreement at all recorded finite scales is not an
argument that (OPEN) holds at unbounded scales. The purpose of the census is
to measure the unpaid signed term without confusing it with zeros or aliases.
