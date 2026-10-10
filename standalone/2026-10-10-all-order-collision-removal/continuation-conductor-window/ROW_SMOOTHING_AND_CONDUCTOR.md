# A power-saving part of the actual integrated sextic covariance

**Status:** proposed complete component proofs, not independently reviewed. The hard-conductor signed estimate, new fourth/sixth moment, 17/24 boundary and RH remain unproved.

**Frozen parent:** GettysburgResearch/riemann PR #916, `f5c089e33ccce4eae4307d4f6475b9977485cb78`, especially `continuation-integrated-window/INTEGRATED_CRITERION.md` (3.1), (6.2), (7.1)--(7.6). This is an add-only successor, not a promotion of an integrated result.

## 1. Result and exact scope

The parent bounds the whole diagonal but leaves the whole signed off-diagonal. We now bound an actual off-diagonal sector, not merely rename it. Positive smoothing of the *row measure*, followed by finite character Fourier expansion, gives a conductor-resolved estimate that is uniform in the scale horizon.

Fix an integer k>=2, 0<delta<1/2 and sigma=1/2+delta. Use the parent's fixed arithmetic data over K=Q(sqrt(-3)), with S containing primes over 6 and the conductor of a fixed finite-order character nu. Let W be any bounded measurable function supported in a fixed compact interval [a,b] in (0,infinity). The application uses the parent's single smooth window W_*; the arithmetic diagnostic uses a different, explicitly labeled box window. Neither the sector proof nor the diagnostic imports a quasi-RH theorem.

Write chi_r(u)=(u/r)_6, with original zeros at nonunits. Define the *same* squarefree balanced coefficients as in the parent:

    c_X(r)=mu_K(r) nu(r) w_X(r),
    w_X(r)=sum_(n_1...n_k=r) product_i W(Nn_i/X),
    B_u(X)=sum_(r squarefree,(r,S)=1) c_X(r) chi_r(u).       (1.1)

The factorizations are ordered and every ideal is nonzero, integral and prime to S. Since r is squarefree, the n_i are pairwise coprime. Units may occupy several positions. No divisor allocation is discarded.

For D,H>=2, change only the row weight to

    V(t)=(1-t/2)_+^8,
    K_H^V(r,s)=sum_(u in O, u!=0) V(Nu/H) chi_r(u) bar(chi_s(u)),
    I_B^V(D,H)=integral_0^D sum_(u!=0) V(Nu/H)|B_u(X)|^2
                          X^(-2k sigma) dX/X.              (1.2)

These sums are finite: Nu<2H and Nn_i<=bD. The weight is nonnegative. For Nu<=H it is at least 2^(-8), so

    I_B^sharp(D,H) <= 2^8 I_B^V(D,H).                       (1.3)

I_B^sharp is precisely the complete sharp row range used by the parent. This comparison is for the whole positive energy, NOT separately for its signed sectors.

For distinct squarefree r,s put

    c=gcd(r,s),  r=c a_0,  s=c b_0,
    q(r,s)=N(a_0 b_0).                                     (1.4)

The ideals c,a_0,b_0 are pairwise coprime. The character chi_(a_0) bar(chi_(b_0)) is primitive modulo a_0 b_0; in particular q>1. This is an exact finite additive-period conductor in the good-prime residue-symbol family, not an unspecified analytic conductor.

For Q>=1 let A_Q(D,H) be the absolute covariance mass in Q<q(r,s)<=2Q:

    A_Q(D,H)=integral_0^D X^(-2k sigma)
          sum_(r!=s, Q<q(r,s)<=2Q)
            |c_X(r) bar(c_X(s)) K_H^V(r,s)| dX/X.           (1.5)

### Theorem 1.1. Horizon-uniform conductor-band bound

For every epsilon>0,

    A_Q(D,H) <<_(k,delta,W,S,epsilon) (HQ)^epsilon F_delta(Q,H),

    F_delta(Q,H)=min{
          H^(-2delta) Q^(1+delta),
          Q^(1-delta),
          H Q^(1/2-delta)}.                                (1.6)

The constant is independent of D,H,Q and the moving ideals r,s,c. Dependence on a fixed nu may be allowed, though its modulus-one values cost nothing here. The hypotheses include all nonzero element rows and all their bad-prime factors. No squarefree-row restriction is imposed.

Equivalently, without the subpower factor, the three regimes are

    Q<=H:        H^(-2delta) Q^(1+delta),
    H<=Q<=H^2:  Q^(1-delta),
    Q>=H^2:     H Q^(1/2-delta).                            (1.7)

Two consequences are important:

    absolute contribution of 1<q<=H << H^(1-delta+epsilon);
    absolute contribution of 1<q<=H^(1/(1-delta))
                                            << H^(1+epsilon). (1.8)

Thus the first sector has a genuine power saving relative to H, at every fixed positive delta. The second removes conductors beyond H at the diagonal-scale budget. These are upper bounds for actual arithmetic terms, not assumptions about them. The constants and the positive exponent delta are fixed before H grows.

## 2. Elementary primitive character estimate on the Eisenstein lattice

Identify O=Z[omega] with its Euclidean lattice, covolume sqrt(3)/2. Every ideal is principal. Let q_0=(beta) be squarefree, prime to 6, of norm q>1; let psi modulo q_0 have a nonprincipal local component at every prime of q_0. For U>0 set

    S_psi(U)=sum_(v in O) psi(v) V(Nv/U).                   (2.1)

The term v=0 is zero. We prove, with an absolute constant depending only on the chosen V and the fixed field,

    |S_psi(U)| << min{U, sqrt(q) min(1,(q/U)^2)}.            (2.2)

No zero-free L-function region is used.

**Finite Gauss sums.** At a prime of norm p, finite Fourier transformation of a nonprincipal multiplicative character has value zero at frequency zero, modulus sqrt(p) at every nonzero frequency, and obeys the original zero convention. Indeed, for a nontrivial additive character e and nonprincipal chi, changing x to xy in the squared Gauss sum gives

    |sum_x chi(x)e(x)|^2
      =sum_(y!=0) chi(y) sum_(z!=0) e((y-1)z)
      =(p-1)-sum_(y!=0,1)chi(y)=p.

For any other nonzero additive frequency change x by a unit; a zero frequency has complete character sum zero. Chinese remaindering gives modulus at most sqrt(q) for every finite Fourier coefficient modulo q_0, and zero at the complete zero frequency. This proof also applies to the product of the +1 and -1 sextic local powers used in (1.4).

**Decay of the fixed radial weight.** The planar function f(z)=V(|z|^2) is compactly supported and C^7. Its derivatives through order six are integrable. Six integrations by parts in a coordinate with largest Fourier component show

    |hat f(xi)| <= C (1+|xi|)^(-6).                        (2.3)

The exponent eight in V is a convenient sufficient choice, not an optimized smoothness assertion. The sixth derivatives have no boundary distribution terms; they are continuous and vanish on the boundary. The Fourier series below is absolutely convergent in dimension two.

Periodize z -> f(z/sqrt(U)) over beta O, and expand that periodization in its ordinary Fourier series. Multiplying by psi on the residue classes gives the finite-character Poisson formula. The factor outside the dual sum is U/(covol(O)q). Its finite Fourier coefficients are bounded by sqrt(q); its zero coefficient vanishes. The dual lattice is a rotation of a fixed lattice scaled by q^(-1/2). Hence

    |S_psi(U)| <= C U/sqrt(q)
       sum_(m in O,m!=0) (1+sqrt(U/q)|m|)^(-6).             (2.4)

The elementary lattice count # {m:0<|m|<=R} << R^2 for R>=1 yields

    sum_(m!=0)(1+t|m|)^(-6) <<
           t^(-2)  (0<t<=1),
           t^(-6)  (t>=1).                                (2.5)

For the first estimate split into |m|<=1/t and successive doubled annuli; for the second use sum_(m!=0)|m|^(-6)<infinity. Substitution proves the second part of (2.2). Direct counting gives the first part: the support is Nv<2U, its coefficients have modulus at most one, and no nonzero point occurs when U<1/2. The bounded remaining range 1/2<=U<=1 is absorbed in the same absolute constant. This proves (2.2).

The argument is a standard finite Fourier/Poisson calculation, supplied here to fix its normalization and domain. It is not claimed as a new general character-sum theorem.

## 3. Keep the common-prime masks before bounding them

For (1.4), exactly

    chi_r(u) bar(chi_s(u))
       =psi(u) 1_((u,c)=1),
    psi=chi_(a_0) bar(chi_(b_0)).                            (3.1)

The extension by zero is essential. A prime common to r and s does NOT disappear at a row divisible by that prime. By ideal Mobius inversion,

    1_((u,c)=1)=sum_(d|c, d|u) mu_K(d).                    (3.2)

Choose the primary generator d_* of d. Since (d,q_0)=1, psi(d_*) is a unit phase. Substitute u=d_*v before applying (2.2):

    K_H^V(r,s)=sum_(d|c) mu_K(d) psi(d_*) S_psi(H/Nd).
                                                                    (3.3)

This is an exact finite identity. All original row zeros are retained. The u=0 issue causes no extra term because q>1 and psi(0)=0.

It follows that

    |K_H^V(r,s)| << tau_K(c) sqrt(q),                       (3.4)

and, more precisely,

    |K_H^V(r,s)| << tau_K(c) sqrt(q)
                  min{1,(q Nc/H)^2}.                       (3.5)

Independently the original positive row mass gives

    |K_H^V(r,s)| << H.                                     (3.6)

If c_X(r)c_X(s) is nonzero, every original factor lies between aX and bX. Consequently

    Nr,Ns are between a^k X^k and b^k X^k,
    Na_0/Nb_0 is between (a/b)^k and (b/a)^k.

When Q<q<=2Q this implies

    Na_0,Nb_0 asymp_(k,a,b) sqrt(Q),
    Nc <<_(k,a,b) X^k/sqrt(Q),
    X >= c_(k,a,b) Q^(1/(2k)).                             (3.7)

Thus (3.5) becomes

    |K_H^V(r,s)| << tau_K(c) sqrt(Q)
                   min{1,(X^k sqrt(Q)/H)^2},               (3.8)

with fixed constants absorbed in the inequality. There is no constant depending on a moving exclusion. The common-mask cost is explicitly tau_K(c), not silently put into S.

## 4. Count the actual balanced allocations, then integrate

For fixed k and each eta>0, the fixed-order ideal divisor estimate gives

    |w_X(r)w_X(s)| tau_K(c) <<_(k,W,eta) X^eta              (4.1)

on the support, after dividing eta among its finitely many uses. This is a size bound only. It does not assert Mobius cancellation at a fixed product. One elementary proof of the divisor estimate splits primes at a fixed threshold: for large norm, the local divisor coefficient is bounded by the requested norm power; the finitely many small primes are absorbed in a constant and an arbitrarily smaller power. Ideals in this fixed field have the usual unique prime factorization.

The number of triples (a_0,b_0,c) in (3.7) is at most

    C Q * (X^k/sqrt(Q)) = C X^k sqrt(Q),                   (4.2)

by the O(Y) ideal count, itself immediate from the primary Eisenstein lattice. If the c upper bound is below one there are no triples. Discarding coprimality and squarefreeness in this positive *count* only enlarges it. The original complex terms remain unchanged in (1.5).

Combining (3.6), (3.8), (4.1) and (4.2) proves the pointwise sector estimate

    sum_(Q<q<=2Q) |c_X(r)bar(c_X(s)) K_H^V(r,s)|
       << X^(k+eta) min{
             H sqrt(Q),
             Q min(1,(X^k sqrt(Q)/H)^2)}.                  (4.3)

This is an actual bound for the specified sector. It is not an arbitrary-coefficient sieve on the whole product length.

Multiply (4.3) by X^(-k-2kdelta) and integrate. Put z=X^k and choose eta so that

    alpha=2delta-eta/k is in (0,2).

The lower support in (3.7) says z>=c sqrt(Q). The constants c>0 below depend only on the fixed window and k. Extending the upper endpoint to infinity is legal after taking these nonnegative bounds. The first two needed integrals satisfy

    integral_(c sqrt(Q))^infinity z^(-alpha) dz/z
                                          <<_alpha Q^(-alpha/2),

    integral_0^infinity z^(-alpha)
          min(1,(z sqrt(Q)/H)^2) dz/z
       =(H/sqrt(Q))^(-alpha) [1/(2-alpha)+1/alpha].         (4.4)

The omitted change-of-variable factor 1/k is fixed. Use the first integral after either dropping the second minimum in (4.3) or using the H sqrt(Q) bound. Use the second integral after extending the lower endpoint to zero. The resulting three bounds are

    Q^(1-delta+eta/(2k)),
    H^(-2delta+eta/k) Q^(1+delta-eta/(2k)),
    H Q^(1/2-delta+eta/(2k)).                              (4.5)

Choose eta/k smaller than the requested epsilon and smaller than delta. All losses are bounded by (HQ)^epsilon. Taking their minimum proves (1.6), uniformly in D. Equation (1.7) follows by comparing the three explicit powers; their transition points are exactly Q=H and Q=H^2.

For completeness, keeping the finite upper endpoint in the part with the quadratic minimum gives the additional bound

    A_Q(D,H) << D^eta H^(-2) Q^2 D^(2k(1-delta)).          (4.6)

It is useful when D^k sqrt(Q) is much smaller than H. It is not needed for (1.8).

Every exponent in the piecewise function (1.7) is strictly positive as a function of Q when 0<delta<1/2. Summing the dyadic bands is a geometric sum, with constants depending on delta. This proves (1.8), allocating preliminary subpowers smaller than the final requested one. No finite numerical calculation is used in this proof.

## 5. An exact radial block cancellation

Let rho=1+omega, a unit of order six. Because V is radial, u -> rho u permutes its complete row set and preserves its weights. Multiplicativity gives

    K_H^V(r,s)=chi_r(rho) bar(chi_s(rho)) K_H^V(r,s).       (5.1)

Thus this kernel is exactly zero unless the two unit characters agree. All good prime norms are 1 modulo 6, and the defining finite-field power gives

    chi_p(rho)=rho^((Np-1)/6).

Multiplicativity and multiplication modulo 36 give, for squarefree r,

    chi_r(rho)=rho^((Nr-1)/6).

Therefore

    K_H^V(r,s)=0 unless Nr == Ns (mod 36).                 (5.2)

This is an exact six-block decomposition, including nonunit rows. It is ordinary finite unit orthogonality, not an asserted power saving or a new reciprocity theorem. The sharp radial row measure has the same property. Its value here is to remove these pairs from the remaining literal statistic and provide a stringent actual-arithmetic diagnostic.

## 6. The smaller signed frontier and its zero-free implication

The full diagonal with weight V remains O(H), by the same divisor-mass argument as the parent: K_H^V(r,r)<=C H and

    sum_r |c_X(r)|^2 << X^(k+eta),

so eta<2kdelta makes its weighted scale integral converge. No new premise is used for the diagonal.

Let Q_0=H^(1/(1-delta)), fixed after H is specified and unchanged at all inner scales. Define R_>(D,H) to be the signed integral of the EXACT terms

    r!=s, q(r,s)>Q_0, Nr==Ns (mod 36),                      (6.1)

in (1.2). The signed real value is obtained either by keeping both ordered pairs or by pairing each with its conjugate. No absolute values are introduced in R_>.

Equations (1.8) and (5.2) imply

    I_B^V(D,H) = D_diag^V(D,H) + O_low^V(D,H) + R_>(D,H),
    D_diag^V << H,
    |O_low^V| <<_epsilon H^(1+epsilon),
    R_>(D,H) >= -C_epsilon H^(1+epsilon).                  (6.2)

The last assertion follows from nonnegativity of the whole energy. In particular, for H=D^h and lambda>=0, the new arithmetic premise

    R_>(D,D^h) <= C_epsilon D^(h+lambda+epsilon)            (6.3)

implies the parent full positive-energy premise by (1.3). Its proved implication then gives

    L_K(s,nu)!=0 for Re(s)>1/2+delta+(lambda+5h/6)/(2k),    (6.4)

with poles of principal targets allowed. The parent's inverse-kernel absorption requires its explicitly enlarged but FIXED S; Theorem 1.1 works for that S as well. Constants need not be uniform as delta approaches zero or k grows. No moving-row-range replacement occurs.

The extraction can also be checked directly: each prime replica p^6 with Np<=H^(1/6) has V(N(p^6)/H)>=2^(-8). Thus none of the replica rows required by the exact prime-removal identity has been removed by the smoothing. The parent proof needs only a finite positive row measure, so all its row/scale Holder and dilation steps continue to apply. Alternatively (1.3) avoids redoing any of those steps.

### A defect-adapted cutoff

For 0<=lambda<=h(1-2delta), the larger cutoff

    Q_lambda=D^((h+lambda)/(1-delta))                      (6.5)

is at most H^2, and the same band estimates show that its entire lower sector costs at most D^(h+lambda+epsilon). In the complementary regime lambda>=h(1-2delta), the valid cutoff is

    Q_lambda=D^(lambda/(1/2-delta)).                       (6.6)

The formulas agree at the shared boundary. Using the corresponding cutoff in (6.1) leaves the SAME sufficient one-sided premise (6.3). This is a theorem about which portion is already bounded at a chosen loss budget. It is not a proof of (6.3).

For example, at k=2, h=1 and delta=1/16, the no-defect cutoff is H^(16/15) rather than H. Even after assuming the remaining no-defect estimate, (6.4) would give 37/48, not 17/24: the positive delta has its explicit cost. Arbitrarily small fixed delta is required for the limiting 17/24 deduction.

## 7. What the attack did not close

The unbounded high-conductor sector in (6.1) is still present. A size bound for its arbitrary coefficients would lose the Mobius/divisor source and encounters the replica obstruction audited in the parent. The present proof controls a specified part by finite character cancellation and scale damping; it does not manufacture a global signed saving from the smooth weight.

There is no claimed new numerical zero-free boundary. The full arithmetic fourth moment and the generalized cofinal hierarchy remain unproved. The smallest missing statement for this packet's deeper consequence is exactly (6.3), on the high-conductor, unit-matched pairs, with a useful lambda.

Adjacent PR #919 had already developed signed conductor frontiers in the original four-factor variables. Its current metadata were read; its complete proofs are not imported or independently re-audited here. The distinction of this calculation is the horizon-uniform, all-fixed-k bound for the parent's *balanced product columns*, its explicit three-regime function (1.7), and the integrated H^(-delta) saving in the low-conductor part. Elementary Poisson, divisor counting and unit orthogonality themselves are classical.
