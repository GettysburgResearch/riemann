# Absorb all shared-prime collisions across a Hermitian moment

**Status:** proposed complete component proofs; independent review pending. The primitive high-conductor signed arithmetic estimate remains unproved. No new fourth/sixth moment, 17/24 boundary, improved zero-free half-plane or RH proof is claimed.

**Publication base:** PR #916, `e5d68883991b390798d993b0bafa7975ab801886`. This includes the saved Gaussian packet unchanged, on top of the compact radial checkpoint `1b55960ec9fb23425231dc281b70b640d8154104`. Nothing in either predecessor is overwritten.

## 1. The new comparison

The preceding reductions remove overlaps WITHIN each of two k-factor products. Their covariance still contains a changing common divisor between the products. Here the inverse kernel is applied to all 2k factors simultaneously, including the conjugate factors. This absorbs every shared-prime collision on both sides at a small RELATIVE cost.

Fix k>=1, put m=2k, fix sigma=1/2+delta with 0<delta<=1/2, and let W be real and bounded, supported in [a,b] subset (0,infinity). The zero-free application uses the parent's nonnegative smooth W_*. Work over K=Q(sqrt(-3)). Ideal indices are nonzero integral ideals. A fixed finite set S contains primes above 6 and the conductor of a fixed finite-order Hecke character nu. Enlarge S once as specified in Section 2, BEFORE choosing a horizon or a row range.

    theta_u(n)=nu(n) chi_n(u), (n,S)=1,
    A_u(X)=sum_(n,S)=1 mu_K(n) theta_u(n) W(Nn/X).

All original zero-on-nonunit values are retained. Let dmu(u) be any finite nonnegative row measure. Define

    I_M(D)=integral_0^D sum_u |A_u(X)|^m X^(-m sigma) dmu(u) dX/X.

For m squarefree ideals n_1,...,n_m, require them to be PAIRWISE COPRIME ACROSS ALL m POSITIONS, not just within each half. Put

    C_u(X)=sum_(all n_i pairwise coprime, all (n_i,S)=1)
       mu_K(product_i n_i)
       product_(i<=k) theta_u(n_i)
       product_(i>k) bar(theta_u(n_i))
       product_(i=1)^m W(Nn_i/X),
    I_C(D)=integral_0^D sum_u C_u(X) X^(-m sigma) dmu(u) dX/X.   (1.1)

Repeated unit ideals are permitted. Swapping the two halves conjugates a summand and permutes the tuple set, so C_u(X) is real. It need NOT be nonnegative pointwise.

### Theorem 1.1. Hermitian collision absorption

Let q=q_(m,S)(sigma) be the nonidentity absolute kernel mass defined below. If q<1, then, for every finite horizon and this SAME fixed row measure,

    |I_C(D)-I_M(D)| <= q I_M(D),
    (1-q) I_M(D) <= I_C(D) <= (1+q) I_M(D).                  (1.2)

Thus I_C(D)>=0, despite its signed summands. At q<=1/3,

    I_M(D) <= (3/2) I_C(D).                                 (1.3)

This is NOT a claim that the absolute sum of all collision terms is small. The absolute value in (1.2) is outside the completed signed row-and-scale expression. Nor does (1.2) imply pointwise positivity of C_u(X), or a pointwise estimate at a single X.

## 2. Exact mixed-colour inverse and its small mass

Use the same elementary kernel as the parent, now in m=2k variables:

    Q_m(z)=(1-sum_i z_i)/product_i(1-z_i),
    b_m(0)=1; b_m(e)=1-|supp(e)| for e!=0,
    D_m(d_1,...,d_m)=product_(p not in S) b_m(v_p(d_1),...,v_p(d_m)).

Set

    q_(m,S)(sigma)=sum_(d!=(1,...,1)) |D_m(d)|/(product_i Nd_i)^sigma. (2.1)

At each prime, take the colour characters to be theta_u in the first k positions and its conjugate in the last k. Multiplying Q_m by product_i(1-z_i) shows coefficientwise that

    C_u(X)=sum_d D_m(d)
       product_(i<=k) theta_u(d_i) product_(i>k) bar(theta_u(d_i))
       product_(i<=k) A_u(X/Nd_i) product_(i>k) bar(A_u(X/Nd_i)). (2.2)

For a finite horizon this identity is finite: a nonzero term has Nd_i<=bD. There is no division by theta_u(p), so it is valid when a row lies on a character zero. The conjugations on BOTH the dilation coefficients and the shifted factors are necessary.

For completeness, at t=(Np)^(-sigma) the one-prime absolute mass is

    F_m^-(t)=2-(1-mt)/(1-t)^m.

Its nonconstant terms have nonnegative coefficients. If mt<=1/2, counting a pair of occupied positions bounds

    F_m^-(t)-1 <= binom(m,2)t^2/(1-t)^m <= m^2 t^2.

The fixed-field ideal count # {n:Nn<=x}<=3x gives, for 0<delta<=1/2,

    sum_(Np>P) (Np)^(-1-2delta) <= (6/delta) P^(-2delta).

For example, the completely explicit fixed cutoff

    P >= max{(2m)^3, (24m^2/delta)^(1/(2delta))}              (2.3)

makes the sum of local nonconstant absolute masses at most 1/4. The product of (1+t_p) with sum t_p<=1/4 is at most 4/3, hence 1+q<=4/3. This restates the parent's elementary small-kernel proof at twice the previous colour count. The old cutoff is NOT assumed automatically sufficient.

Larger fixed cutoffs make q as small as any prescribed positive constant. No uniformity as delta tends to zero or k tends to infinity is asserted. At delta=0 this absorption argument is not available.

## 3. Proof of the Hermitian comparison

On the common measure space of rows times (0,D), with scale measure dX/X, generalized Holder gives for any fixed tuple d

    integral_0^D sum_u product_(i=1)^m |A_u(X/Nd_i)| X^(-m sigma)
    <= product_i [integral_0^D sum_u |A_u(X/Nd_i)|^m
                                      X^(-m sigma)]^(1/m)
    <= (product_i Nd_i)^(-sigma) I_M(D).                     (3.1)

The last step is the substitution Y=X/Nd_i: the upper endpoint becomes D/Nd_i<=D. Crucially the ROW MEASURE DOES NOT CHANGE after that substitution. The absolute values of all dilation characters in (2.2) are at most one.

The tuple d=(1,...,1) in (2.2) is exactly |A_u(X)|^m. Subtract it, integrate, and bound the other finitely many terms using (3.1). Their summed coefficient mass is at most (2.1). This proves (1.2). Every norm is finite before the comparison is made, so no conjectural moment estimate has been used. QED.

The proof applies to a Gaussian row measure exp(-Nu/H) on all nonzero elements. One may first truncate the rows; at fixed D there are finitely many column terms, so their bounded character values and the summable Gaussian give dominated convergence. Both I_M and I_C are finite. The comparison therefore holds for every D,H with the same constants.

### Fixed-prime reinsertion

The larger S is harmless for the final exponent, but it changes the literal polynomial. This is stated rather than hidden. If S_0 is a prior fixed set and T=S\S_0, exact squarefree splitting gives

    A_(S_0),u(X)=sum_(d squarefree supported on T)
                  mu_K(d)theta_u(d) A_S,u(X/Nd).

There are finitely many d. Minkowski in the weighted L^m norm shows that its reinsertion costs at most

    product_(p in T)(1+(Np)^(-sigma))

in norm, independently of D and the row measure. No moving prime is put into an implied constant. The corresponding finite Euler factors are nonzero on Re(s)>0.

## 4. What the new signed scalar actually is

Keep the parent's squarefree allocation weights

    w_X(r)=sum_(n_1...n_k=r) product_i W(Nn_i/X).

Grouping the first and second halves of (1.1) by their products gives EXACTLY

    C_u(X)=sum_(r,s squarefree, (r,s)=1, (rs,S)=1)
        mu_K(r)mu_K(s)nu(r)bar(nu(s))w_X(r)w_X(s)
        chi_r(u)bar(chi_s(u)).                              (4.1)

Thus this is the original balanced covariance restricted to gcd(r,s)=1, including r=s=1. No divisor allocation is dropped. All nonunit diagonal pairs r=s are absent, because a squarefree ideal coprime to itself is the unit ideal.

This removal is by the RELATIVE absorption (1.2), not by proving that each discarded gcd sector is absolutely O(H). The previously proved positive low-conductor bound and this new relative comparison are distinct statements.

For r!=s in (4.1), chi_r bar(chi_s) is primitive modulo rs: at every prime its exponent is +1 or -1, never zero. There is no shared-prime mask and no mask-dilation sum. Its conductor is exactly Q=Nr Ns. This is the structural gain of the Hermitian extension.

If W is nonnegative and S additionally contains every prime of norm <=b/a, a tuple with a unit factor and any nonunit factor cannot occur: the unit forces X<=1/a, hence every factor norm is <=b/a and any nonunit factor meets S. This optional enlargement isolates a single all-unit contribution, but is not needed for (1.2).

## 5. What the theorem does not prove

It does not bound I_C by O(H), and it does not prove a moment theorem by throwing away repeated primes. It proves a reversible exponent-level reduction, after an explicit larger fixed cutoff, to a REAL SIGNED sum whose two products are genuinely coprime.

The next file gives its primitive Gaussian Poisson representation and an unconditional bound for its low-conductor sector. The remaining one-sided high-conductor estimate still contains the full arithmetic difficulty. The new contribution is an extension of the already published inverse-kernel argument, not a claim that the kernel or Holder's inequality is newly discovered.
