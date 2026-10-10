# Remove the low product-conductor covariance at every fixed order

**Status:** proposed complete component proofs, awaiting independent mathematical review. The high-conductor signed upper bound is still unproved. No new full fourth/sixth moment, 17/24 half-plane, improved zero-free boundary or RH proof is claimed.

**Source:** add-only continuation of PR #916, frozen head `f5c089e33ccce4eae4307d4f6475b9977485cb78`. The predecessor `continuation-integrated-window/INTEGRATED_CRITERION.md` has Git blob `34928b0d8531e8cbe8764edbabb188bcb72d5ff1`. Its balanced polynomial, scale weight and complete element-row convention are retained. The Gaussian row weight introduced here is not silently identified with the predecessor's sharp cutoff.

## 1. Arithmetic object and the new theorem

Work over K=Q(sqrt(-3)), O=Z[omega], omega=exp(2 pi i/3). Put N(z)=|z|^2. All ideal variables are nonzero integral ideals. Choose the unique generator congruent to 1 modulo 3 whenever a generator is needed. Fix a finite set S containing the primes over 6 and the conductor of a finite-order Hecke character nu. All column ideals avoid S. All nonzero element rows u in O are retained, including units and sixth powers.

Let k>=2 be fixed. Let W be a fixed real, nonnegative, bounded function supported in [a,b], 0<a<b<infinity. The component bounds do not require smoothness; the zero-free implication in HORIZON_TRANSFER.md uses the predecessor's particular smooth window W_*.

For a squarefree ideal r define

    w_X(r) = sum_(n_1...n_k=r) product_i W(Nn_i/X),
    c_X(r) = mu_K(r) nu(r) w_X(r),
    B_u(X) = sum_(r squarefree) c_X(r) chi_r(u),
    chi_r(u) = (u/r)_6.                                      (1.1)

The factorizations in w_X are ordered. Their factors are automatically squarefree and pairwise coprime; repeated unit factors are allowed. Characters are extended by zero on nonunits, with chi_1(u)=1 even at u=0.

Fix 0<delta<1/2 and sigma=1/2+delta. For D,H>=2 set

    I_G(D;H) = integral_0^D X^(-2k sigma)
                  sum_(u != 0) exp(-Nu/H) |B_u(X)|^2 dX/X,
    K_H^G(r,s) = sum_(u != 0) exp(-Nu/H) chi_r(u) bar(chi_s(u)),
    J_D(r,s) = integral_0^D w_X(r) w_X(s) X^(-2k sigma) dX/X.   (1.2)

At fixed D the column set is finite; the row Gaussian is summable. All expansions and interchanges at this stage are absolutely justified by these facts and by the lower support threshold X>=1/b.

For r!=s write

    g=gcd(r,s),  r=g a_0,  s=g b_0,
    Q(r,s) = N(a_0 b_0) = Nr Ns/(Ng)^2.                       (1.3)

The ideals g,a_0,b_0 are squarefree and pairwise coprime. Q is the EXACT conductor norm of the nonprincipal finite residue character

    psi_(a_0,b_0)(u)=chi_(a_0)(u) bar(chi_(b_0)(u)).            (1.4)

Here 'conductor' refers to this product-column residue character. It is not the physical row norm, nor an unspecified conductor from another PR. A nontrivial restriction to units causes the radial sum to vanish; it does not invalidate the primitive finite residue character statement.

Define the absolute low-conductor covariance mass

    A_leQ(D;H) = sum_(r!=s, Q(r,s)<=Q)
                          J_D(r,s) |K_H^G(r,s)|.              (1.5)

It bounds the absolute value of the corresponding signed covariance. It is stronger than a bound on that signed part alone.

### Theorem 1.1. Uniform all-order low-conductor bound

For every fixed k,W,delta, every epsilon>0, and all D,H,Q>=2,

    A_leQ(D;H) << D^epsilon * {
         H^(-2delta) Q^(1+delta),  if Q<=H;
         Q^(1-delta),             if Q>=H.
    }                                                        (1.6)

Constants may depend on k,W,delta,epsilon and the fixed field. They do not depend on D,H,Q, any moving common divisor, or the individual row. Restricting columns by any fixed S only reduces the positive majorants used in the proof. The estimate uses no quasi-RH input and no new moment assumption.

In particular,

    A_leH(D;H) << D^epsilon H^(1-delta),                       (1.7)

and, at

    Q_* = H^(1/(1-delta)),

    A_leQ_*(D;H) << D^epsilon H.                              (1.8)

Thus an increasing range of actual off-diagonal arithmetic terms is now bounded completely. Equation (1.8) does not bound the remaining Q>Q_* terms.

## 2. Exact primitive character and unit-sector facts

At every prime p|a_0, the local character in (1.4) is the nontrivial primitive sextic character modulo p. At every prime p|b_0 it is its conjugate. Since (a_0,b_0)=1, the Chinese remainder theorem proves primitivity at the squarefree modulus m=a_0 b_0. The modulus is nonunit because r!=s. No reciprocity assumption is needed here: the numerator-variable residue characters are already defined on O/(m).

Let zeta_6=1+omega. For a squarefree ideal r put

    j(r) = sum_(p|r) (Np-1)/6 modulo 6.                       (2.1)

The reduction of zeta_6 has exact order six at every prime outside 6, so

    chi_r(zeta_6)=zeta_6^j(r).

### Proposition 2.1. Six exact orthogonal unit sectors

For every radial summable row weight, including the Gaussian and any finite norm ball,

    K(r,s)=0 if j(r)!=j(s) modulo 6.                          (2.2)

**Proof.** Multiplication u->zeta_6 u permutes the nonzero row lattice, preserves Nu, and preserves every coprimality zero. It multiplies the summand by zeta_6^(j(r)-j(s)). Consequently K equals that scalar times itself. QED.

This is a six-block decomposition, not a power saving in D. In the notation (1.3), j(r)-j(s)=j(a_0)-j(b_0). Shared primes cannot change the surviving unit-sector condition.

## 3. Gaussian Poisson bound, with normalization and conductor exposed

Use the additive character

    e_K(z) = exp(4 pi i Im(z)/sqrt(3)).

It is one on O. The lattice O is self-dual for the real bilinear pairing e_K(vz), and its Euclidean covolume is v_K=sqrt(3)/2. These assertions follow directly by testing the generators 1 and omega.

For a primitive nonprincipal character psi modulo the chosen generator m, Nm=Q, define

    G(psi)=sum_(x mod m) psi(x) e_K(x/m),
    S_psi(L)=sum_(u in O) psi(u) exp(-Nu/L), L>0.              (3.1)

The zero term is zero. Finite Fourier orthogonality gives

    sum_(x mod m) psi(x)e_K(vx/m)=bar(psi(v)) G(psi),
    |G(psi)|=sqrt(Q).                                        (3.2)

For nonunit v the first sum vanishes by primitivity. For unit v it follows by substitution. The norm identity follows from Parseval: both sides of the finite Fourier identity have phi(m) nonzero entries, so Q phi(m)=|G(psi)|^2 phi(m). This argument retains the zeros and applies to the product character (1.4), not just a single prime character.

With Fourier convention integral f(z)e_K(-vz) dx dy,

    Fourier[exp(-Nz/L)](v)=pi L exp(-4 pi^2 L Nv/3).

Poisson summation on mO gives the exact identity

    S_psi(L) = (2 pi/sqrt(3)) (L/Q) G(psi)
        sum_(v!=0) bar(psi(v)) exp(-4 pi^2 L Nv/(3Q)).         (3.3)

There is no zero-frequency main term. This is the usual Eisenstein-lattice Gaussian Poisson formula; the normalization is derived here. Compare Gao--Zhao, arXiv:2201.01885v2, Sections 2.2 and 2.10 for the residue/Gauss and Poisson setting.

Counting lattice points in norm balls gives, for every A>0,

    |S_psi(L)| <= C_A sqrt(Q) min(1,(Q/L)^A).                 (3.4)

**Details.** Put t=L/Q. For t<=1 the nonzero Gaussian lattice sum is O(1/t), so (3.3) is O(sqrt(Q)). For t>=1 that sum is O(exp(-c t)); hence (3.3) is O(sqrt(Q) t exp(-c t)), bounded by C_A sqrt(Q)t^(-A). Constants are independent of the conductor and primitive character. QED.

## 4. Shared-prime masks are not free: sum their exact dilation cost

From (1.3), for every row u,

    chi_r(u) bar(chi_s(u)) = 1_((u,g)=1) psi_(a_0,b_0)(u).

Inclusion-exclusion and u=dv, using the fixed primary generator of d, give

    K_H^G(g a_0,g b_0)
       = sum_(d|g) mu_K(d) psi_(a_0,b_0)(d)
                              S_psi(H/Nd).                  (4.1)

The phase psi(d) is essential. Its modulus is one because (g,a_0 b_0)=1. Equation (4.1) neither drops nor divides by a row-character zero.

### Lemma 4.1. Weighted complete common-divisor estimate

For fixed coprime squarefree a_0,b_0, not both units, Q=N(a_0 b_0),

    sum_(g squarefree,(g,a_0 b_0)=1) (Ng)^(-1-2delta)
                                   |K_H^G(g a_0,g b_0)|
       << sqrt(Q) min(1,(Q/H)^(2delta)).                      (4.2)

**Proof.** Take absolute values after the exact identity (4.1). Enlarge the resulting positive sums to all ideals g=de. The left side is at most

    zeta_K(1+2delta)
       sum_d (Nd)^(-1-2delta) |S_psi(H/Nd)|.                 (4.3)

If R=H/Q<=1, use |S|<<sqrt(Q) and convergence of the ideal zeta series. If R>=1, choose A>2delta in (3.4). After removing sqrt(Q), the remaining sum is

    <= C_A [ R^(-A) sum_(Nd<=R) (Nd)^(A-1-2delta)
                        + sum_(Nd>R) (Nd)^(-1-2delta) ]
    << R^(-2delta).                                         (4.4)

Both estimates follow by partial summation from # {d:Nd<=x}=O_K(x). This proves (4.2). In particular, an arbitrarily large changing gcd is handled without changing a fixed-data constant. QED.

This step is why exponential cancellation at fixed primitive conductor is not, by itself, enough: a large divisor d reduces the physical row length from H to H/Nd. Summing that effect costs a power (Q/H)^(2delta), rather than retaining exponential decay after the common-divisor sum.

## 5. Complete proof of Theorem 1.1

The ordered allocation weight satisfies

    w_X(r)<=||W||_infinity^k k^omega(r),
    Nr<=(bD)^k whenever it contributes below D.

For each eta>0, k^omega(r)<<_(k,eta)(Nr)^eta. To see this without a hidden coefficient theorem, put the finitely many primes with Np<k^(1/eta) into the constant; at every other prime use k<=(Np)^eta. Thus arbitrary D^epsilon losses may cover both divisor weights.

If w_X(r)w_X(s)!=0, then X>=max(Nr,Ns)^(1/k)/b. Extending the positive integral to infinity gives

    J_D(r,s) << D^epsilon max(Nr,Ns)^(-2sigma).

For r=g a_0, s=g b_0 and Q=N(a_0 b_0), max(Nr,Ns)>=Ng sqrt(Q). Consequently,

    J_D(g a_0,g b_0)
       << D^epsilon (Ng)^(-1-2delta) Q^(-1/2-delta).          (5.1)

No pointwise domination of a signed character sum was made. Equation (5.1) is only a positive bound for the integrated coefficient weight.

Apply Lemma 4.1 to sum all common divisors in the absolute covariance. Up to a suitably small D^epsilon, it remains to bound

    sum_(a_0,b_0 squarefree,coprime; 1<N(a_0 b_0)<=Q_0)
       N(a_0 b_0)^(-delta)
                    min(1,(N(a_0 b_0)/H)^(2delta)).           (5.2)

The number of ideal pairs with N(a_0 b_0)<=R is O(R log(2R)):

    sum_(Na_0<=R) # {b_0:Nb_0<=R/Na_0}
       <= C R sum_(Na_0<=R) 1/Na_0 << R log(2R).              (5.3)

Discarding coprimality and squarefreeness is legitimate in this positive count. Only R<= (bD)^(2k) can actually occur. Its logarithms and the finite dyadic decomposition can be absorbed into D^epsilon by initially assigning smaller losses in (5.1).

On a dyadic conductor interval [R,2R), (5.2) is therefore at most a small D-power times

    R^(1-delta) min(1,(R/H)^(2delta)).                        (5.4)

For Q_0<=H, summing the increasing powers gives

    << H^(-2delta) Q_0^(1+delta).

For Q_0>=H, the part below H is O(H^(1-delta)), and the rest is O(Q_0^(1-delta)). Here 1-delta>0. This proves (1.6), after assigning the small losses to the originally requested epsilon. Taking Q_0=H and Q_0=H^(1/(1-delta)) proves (1.7)--(1.8). QED.

### Corollary 5.1. The critical scale weight also permits low-conductor removal

At delta=0, sigma=1/2, and finite D,H,Q>=2,

    A_leQ(D;H) <<_(k,W,epsilon) D^epsilon Q.                  (5.5)

In particular Q<=H costs at most H D^epsilon.

**Proof.** Do not substitute delta=0 into the infinite sum (4.2). Keep the actual cutoff Ng<=G=(bD)^k. In place of (4.3) use

    sum_(Nd<=G) (Nd)^(-1)|S_psi(H/Nd)|
                       sum_(Ne<=G/Nd)(Ne)^(-1)
       << sqrt(Q) (log(2G))^2.

At sigma=1/2, (5.1) has Q^(-1/2)(Ng)^(-1). Equations (5.3)--(5.4) then give (5.5), after logarithms are absorbed. The critical integrated diagonal is likewise O(H D^epsilon), by the same finite-horizon allocation count.

This critical component bound is not an assertion that the predecessor's inverse-kernel absorption works at delta=0. Its q<1 proof still uses a fixed positive delta. QED.

## 6. Diagonal, high-conductor remainder, and the precise open statement

The Gaussian diagonal is

    D_G(D;H)=sum_r J_D(r,r) sum_(u!=0) exp(-Nu/H)|chi_r(u)|^2.

It satisfies D_G<<H for fixed delta>0. Indeed the row Gaussian mass is O(H), and the same allocation argument as in the predecessor gives sum_r w_X(r)^2<<X^(k+eta), with eta<2k delta. Integrating X^(eta-2k delta) dX/X is bounded. The bounded initial X range is harmless.

With Q_*=H^(1/(1-delta)), let R_high(D;H) be exactly the ordered signed covariance terms with

    Q(r,s)>Q_* AND j(r)=j(s) modulo 6.                        (6.1)

All other off-diagonal terms either vanish by Proposition 2.1 or have absolute total O(H D^epsilon) by Theorem 1.1. Therefore

    I_G(D;H) = R_high(D;H) + E_low(D;H),
    |E_low(D;H)| << H D^epsilon.                              (6.2)

The error includes the nonnegative diagonal and signed low covariance; it is not asserted to be nonnegative. Since I_G>=0,

    R_high(D;H) >= -C_epsilon H D^epsilon.                    (6.3)

For H=D^h and lambda>=0, the following two all-horizon upper bounds are equivalent up to constants and arbitrarily small exponent losses:

    I_G(D;D^h) << D^(h+lambda+epsilon),
    R_high(D;D^h) <= C_epsilon D^(h+lambda+epsilon).           (6.4)

The second inequality is the NEW REMAINING ARITHMETIC PREMISE. It has NOT been proved. HORIZON_TRANSFER.md proves why Gaussian smoothing is admissible and how the same conditional zero-free exponent follows.

## 7. Why this does not yet force a zero-free improvement

The product support only gives Q(r,s)<=(bD)^(2k). To delete the entire range using (1.8) on the exponent level would require h>=2k(1-delta). At that threshold the inherited conditional exponent is

    1/2+delta+5h/(12k) >= 4/3+delta/6 > 1.                    (7.1)

So simply making the row average long enough to remove every conductor gives no nontrivial zero-free statement. Near-linear rows still leave a large high-conductor interval. Its coefficient-sensitive signed cancellation is the missing breakthrough.

No assertion that random phases predict a theorem, no transfer of an absolute bound to an uncontrolled signed subfamily, and no promotion of finite checks into an infinite estimate is used in this packet.
