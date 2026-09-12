# STAR26 — weight-adapted star companions and a full-law realization attack

Date: 2026-09-12. **PROPOSED component proofs and computer-assisted existence statements, pending independent mathematical and implementation review. RH and all-order theta realization are NOT proved.**

This is a new add-only packet on main `f99d9e3908dde4865377c75d9ca051c1f545bf4f`. It connects the failed native Brownian companion (#856), the Ising realization work (#842, #847, #854), and the gamma finite-defect work (#862). It does not treat a finite moment fit, an entire-function approximation rate, or a source-independent positivity principle as an RH proof. See SOURCES.json for exact versions and actual reading scope.

The constructive results are an exact 96-spin connected star matching SEVEN even theta moments (orders 2 through 14), an infinite-star completion matching the same moments and the leading theta MGF growth, and a no-go theorem for all homogeneous-coupling star sequences. The remaining all-order realization problem is stated with its complete consumer in Section 7. There is no priority claim for Lee–Yang, Hermite–Biehler, moment convergence, or normal-family methods.

## 1. Literal source and normalization

Use the entire completion, including removable values,

    xi(s)=s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)/2,
    Xi(z)=xi(1/2+iz).

For t>=0 put

    phi(t)=sum_(n>=1) [4 pi^2 n^4 exp(9t/2)-6 pi n^2 exp(5t/2)]
                                  exp[-pi n^2 exp(2t)],
    M_k=2 integral_0^infinity t^k phi(t)dt, k even.                 (1)

The unchanged classical source identity is

    Xi(z)=2 integral_0^infinity phi(t)cos(zt)dt.                    (2)

Here every summand of phi is positive on t>=0. All exponential moments exist. Let T have density phi(|t|)/M_0, let sigma^2=M_2/M_0, and set

    Z=T/sigma, nu_(2r)=E Z^(2r),
    Psi(z)=E exp(izZ)=Xi(z/sigma)/Xi(0).                            (3)

In particular nu_2=1. Physical weights are sigma times the standardized weights used below. No source rescaling is hidden in a comparison of cumulants.

For completeness, (2) follows from Jacobi inversion and the classical Mellin derivation, not from assumed zero geometry. Put psi(x)=sum_(n>=1)exp(-pi n^2 x), Q(t)=exp(t/2)psi(exp(2t)). Jacobi gives Q(-t)=Q(t)+sinh(t/2), hence Q'(0)=-1/4, and direct differentiation gives phi=Q''-Q/4. Splitting the Mellin integral at x=1 gives

    xi(s)=1/2 + s(s-1)/2 integral_1^infinity
                      psi(x)[x^(s/2)+x^((1-s)/2)] dx/x.

For s=1/2+iz substitute x=exp(2t) and integrate Q'' twice by parts. The boundary term is 1/2 and yields (2). Superexponential decay justifies both integrations and entire continuation. DLMF 20.7.32 (Jacobi theta transformation) and 25.4.3–4 fix the classical conventions.

The full primitive calculation in CERTIFICATE.md proves, among stronger retained enclosures,

    1/25 < sigma^2 < 1/20,
    5e-18 < Xi(l) < 6e-18,
   -9e-18 < Xi(r) <-8e-18,
   -3e-12 < Xi(q) <-2.9e-12,                                      (4)

where the exact rational arguments are

    l=14.13472514173469, r=14.13472514173470,
    q=3(l+r)/2=42.404175425204085.

It also proves M_0 M_2<1. Cauchy–Schwarz in (2) therefore gives |Xi'(x)|<1 on the ENTIRE real axis. Some real zero gamma lies between l and r, and every possible 3 gamma differs from q by less than 1.5e-14. The full interval enclosure remains negative:

    Xi(gamma)=0, Xi(3 gamma)<-2.9e-12.                             (5)

Neither uniqueness, simplicity, first-zero status, nor RH is used. The same zero/nonzero-triple property holds after standardization (3). This source obstruction was already used in #854; we independently regenerate it from (1), not from that packet's accepted numbers.

## 2. STAR26-1: a source-defined companion with a proved strict sign

Consider a finite zero-field Ising star with hub epsilon, leaf spins sigma_i, nonnegative observable weights b,a_i, and couplings J_i>=0. Write m_i=tanh J_i. An exact change of variables sigma_i=epsilon tau_i makes epsilon a fair sign independent of biased independent signs tau_i, with E tau_i=m_i. Its standardized observable is

    X=epsilon (b+sum_i a_i tau_i).                                (6)

The equality of Gibbs laws follows by substituting into sum_i J_i epsilon sigma_i and summing epsilon; no independent-spin approximation of the star is made.

Define entire functions

    F(z)=exp(ibz) product_i [cos(a_i z)+i m_i sin(a_i z)],
    E(z)=F#(z)=exp(-ibz) product_i [cos(a_i z)-i m_i sin(a_i z)],
    A=(E+F)/2, B_star=(E-F)/(2i).                                 (7)

Then A is exactly E exp(izX). Both A and B_star are real entire. For y>0,

    |cos(a(x+iy))-i m sin(a(x+iy))|^2
      -|cos(a(x+iy))+i m sin(a(x+iy))|^2
             =2m sinh(2ay).                                     (8)

The E factor has no zero in the upper half-plane: its exponential form has positive coefficients and a zero there would require an exponential modulus greater than one to equal (1-m)/(1+m)<=1. For b>0, (8) and the exponential give

    |E(z)|>|F(z)|,    Im(A(z) conjugate(B_star(z)))>0, Im z>0.     (9)

The same holds with b=0 when at least one a_i m_i>0. At an A zero, E=-F would contradict (9). Reflection gives NO nonreal zeros anywhere. This is a direct star-specific proof of the relevant Lee–Yang/Hermite–Biehler mechanism, supplied rather than imported as an unexplained positivity theorem.

Unlike BRN27's neutral B=-z Xi/4, this companion is not a multiple that hides all target zeros. But (9) concerns the STAR'S A, not Xi. Identifying A or a sequence of such A's with (3) is a separate mathematical task.

We now impose the weight-adapted rule

    m_i=k a_i, k=1/100, 0<=k a_i<1.                              (10)

It makes the model's finite moments polynomial in its weights. These are genuine nonuniform pair couplings, not an arbitrary mixture of cosine products.

## 3. STAR26-2: exact connected 96-spin realization through degree 14

There are nine leaf groups with multiplicities

    (1,1,1,1,1,1,1,24,64),                                      (11)

and one hub: 95 leaves, 96 spins, and 95 strictly positive edges. Let c denote the ten exact rational centers in parameters.json; the last is the hub. Their approximate standardized values are

    leaves: .3481476579175381, .2948607235631475,
            .2088900424985064, .21994570188028675,
            .19874795734917752, .2207528821573899,
            .17590620417053146, .09014008592946826 (24 copies),
            .04330368035257343 (64 copies);
    hub:    .5080669047415874.

The exact model is NOT these rounded decimals. Fix zero-based coordinates 3,4,6 at their terminating rational values in parameters.json. The seven active coordinates, in order, are (9,0,7,1,8,2,5). Each has radius 10^-24 about its exact rational center. Define a^(0),b^(0) as the unique root in this box of

    kappa_(2r)(X)=kappa_(2r)(Z), r=1,...,7.                        (12)

The certificate proves existence and uniqueness within this box. It makes no assertion of global uniqueness or minimal spin count. All weights lie strictly between zero and one; all 95 edge couplings satisfy

    .0004 < J_i < .004.                                          (13)

This is not a perturbative existence assertion requiring every edge to be below 10^-100. The literal formula is J_i=atanh(a_i/100), with a_i the standardized root coordinate; the physical observable weights are sigma a_i and sigma b.

To establish (12), let c_n(m) be the cumulants of a sign with mean m. Exactly,

    c_1(m)=m, c_(n+1)(m)=(1-m^2)c_n'(m).
    K_n=b 1_(n=1)+sum_j multiplicity_j a_j^n c_n(a_j/100).        (14)

K_n are conditional cumulants of Y=b+sum a_i tau_i. Convert them to moments with

    mu_0(Y)=1,
    mu_n(Y)=sum_(j=1)^n binom(n-1,j-1) K_j mu_(n-j)(Y).           (15)

Even moments of X=epsilon Y are those of Y; odd moments vanish. The inverse triangular recurrence yields the left side of (12). No sum over only selected configurations is used; (14)–(15) encode all 2^96 configurations exactly.

The full-source ball evaluation, exact rational inverse preconditioner R, and interval derivatives give

    delta_0=||R f(c)||_infinity <4.481e-61,
    q_0=sup_box ||I-R Df||_infinity <1.267e-11,
    delta_0+q_0*10^-24 <10^-24.                                  (16)

Norms are row-sum/infinity norms, not entry maxima. Banach's fixed-point theorem applied to x -> x-Rf(x) gives the true root. The exact inverse of the rational midpoint Jacobian is reconstructed and both inverse identities checked. Actual Jacobian intervals, including all polynomial dependency over the box, are then used in (16). The moment/cumulant triangular identities prove EXACT theta matching through order 14 for sigma X.

The SAME root enclosure proves

    -.115 < E X^16 - nu_16 < -.114.                              (17)

The center is approximately -.11438319548843916; this is a certified nonzero mismatch, not a stopping tolerance. X is not the full theta law.

## 4. STAR26-3: homogeneous-coupling stars cannot converge to theta

This theorem concerns stars with nonnegative observable weights, zero external fields, and ONE common leaf bias m_n in each finite star; m_n may vary arbitrarily with n. Suppose their variances are uniformly <=V and their laws converge weakly to Z in (3). We derive a contradiction.

Write A_n=sum a_i, S_n=sum a_i^2, and d_n=b_n+m_n A_n. Independence of the conditional signs gives

    Var(X_n)=d_n^2+(1-m_n^2)S_n
       =b_n^2+S_n+2 b_n m_n A_n+m_n^2(A_n^2-S_n).               (18)

Thus S_n<=V and d_n<=sqrt(V). If m_n>=m_0>0 on a subsequence, then

    m_n(b_n+A_n)<=d_n<=sqrt(V),

so that subsequence is supported on the fixed compact interval [-sqrt(V)/m_0,sqrt(V)/m_0]. Its weak limit cannot have the positive, everywhere-supported theta density. Consequently m_n ->0.

Couple a fair sign eta and a mean-m sign tau by leaving eta=+1 unchanged and flipping eta=-1 to +1 with probability m. Then

    E(tau-eta-m)=0,
    E(tau-eta-m)^2=2m-m^2.                                      (19)

Take independent such couplings, and use the same independent hub epsilon. The comparison variable

    Xtilde_n=epsilon (d_n+sum_i a_i eta_i)

is a sum of INDEPENDENT fair signs: the joint vector (epsilon,epsilon eta_1,...,epsilon eta_N) is uniform on its sign cube. The complete coupling gives

    W_2(X_n,Xtilde_n)^2 <=(2m_n-m_n^2)S_n <=2m_n V ->0,
    Var(Xtilde_n)=d_n^2+S_n<=2V.                                 (20)

The Fourier transform of any independent weighted-sign sum of variance U obeys

    |chi(3t)|<=exp(2Ut^2)|chi(t)|, ALL real t.                    (21)

Indeed cos(3u)=cos(u)(1-4sin^2 u), and |1-4sin^2 u|<=1+2u^2<=exp(2u^2). The elementary bound uses sin^2 u<=min(u^2,1)<=(u^2+1)/2 when the inner expression is negative. There is no division by a potentially zero cosine. Uniform U permits passage through weak convergence. Thus the limit's real zeros are closed under tripling. Equation (5) contradicts this. QED.

This strengthens the relevance of #854's independent-spin barrier to an interacting class. It does NOT exclude heterogeneous stars, general Ising graphs, or RH. It also does not confuse total coupling, a uniform rank-one coupling reserve, and the common star-edge parameter.

## 5. STAR26-4: whole-function limits of weight-adapted stars

Fix k>0. Consider (10) with Var(X_n)<=V and k sqrt(V)<1, allowing different finite leaf counts. Write S_n=sum_i a_(n,i)^2. From the pair correlations, or direct expansion of (6),

    Var(X_n)=S_n-k^2 sum_i a_(n,i)^4+(b_n+k S_n)^2 >=b_n^2+S_n. (22)

After sorting leaf weights, padding by zeros, and taking a subsequence, let

    b_n -> b>=0, a_(n,j)->a_j>=0,
    S_n->S, v=S-sum_j a_j^2>=0.                                 (23)

This is possible by boundedness and diagonal compactness; Fatou gives the last inequality. Uniformly on every fixed complex disk and for small a,

    log[cos(az)+i k a sin(az)]
           =a^2(ikz-z^2/2)+O_R(a^4).                            (24)

The logarithm here is only the branch near 1 for the small tail factors. Sorting gives a_(n,K+1)^2<=V/(K+1), hence the ENTIRE remaining log error is at most C_R V^2/(K+1). Finite head factors converge separately. Therefore, locally uniformly throughout C,

    F_n(z) -> F(z)=exp(i(b+k v)z-vz^2/2)
                   product_(j>=1)[cos(a_j z)+i k a_j sin(a_j z)],
    A_n -> A=(F+F#)/2.                                         (25)

The infinite product is locally uniformly convergent because each factor is 1+O_R(a_j^2) and sum a_j^2<infinity. No formal eigenfunction expansion or unspecified tail tightness is invoked. Equation (25) identifies the possible diffuse remainder as a Gaussian of variance v WITH its necessary mean shift k v. Omitting that shift changes the limit.

There is also a direct probability realization: the centered independent series sum a_j(tau_j-k a_j) converges almost surely and in L2, its means sum to k sum a_j^2, and one adds the indicated Gaussian and fair hub. Entire-transform convergence follows from the uniform MGF estimate in Section 7. This is an infinite-star probability limit, not a claim about an absolutely summable infinite-volume Ising Hamiltonian.

Hurwitz and A(0)=1 imply that A has only real zeros. In the nondegenerate case, the real zeros are in fact simple. The product F has no real zero, and its real-axis phase derivative is

    b+k v+sum_j k a_j^2/[cos^2(a_j x)+k^2 a_j^2 sin^2(a_j x)]>0. (26)

The sum and its local differentiation are justified by the same small-tail estimates. At Re F=0, differentiating Re F gives a nonzero derivative. In the nondegenerate case at least one positive term is present. The all-zero-parameters case gives A=1 and is not being used to infer simplicity.

If A=Psi, the diffuse variance MUST vanish. The native source, or the completed xi formula and Stirling, gives

    log Psi(iy)=(y/(2 sigma))log y+O(y), y -> infinity.            (27)

All factors in F#(iy) are >=1, so (25) gives A(iy)>=exp(v y^2/2)/2. Thus v>0 contradicts (27). Moreover sum a_j must diverge, since v=0 and sum a_j<infinity would imply bounded support, whereas Z has unbounded support. Hence a successful fixed-k construction would require

    sum a_j^2<infinity, sum a_j=infinity, k a_j->0, v=0.          (28)

This is how a multiscale heterogeneous construction can evade Section 4: small edges vanish with their weights, but each persistent weight retains a nonzero bias. These necessary conditions are not sufficient for theta realization.

## 6. STAR26-5: an actual infinite-star fourteen-moment completion

The conditions in (28) are not empty formal requirements. They can be incorporated into our certified finite root while keeping all seven exact moments.

Let

    c_tail=1/(2 sigma), J=10^40,
    a_j=c_tail/j, m_j=k a_j, j>=J, k=1/100.                     (29)

Append these independent conditional leaves to the nine finite groups. Their entire transform is defined by the normally convergent product, not by a finite cutoff. Adjust the same seven active finite-head coordinates; keep coordinates 3,4,6 fixed. Call this DIFFERENT root a^(infinity),b^(infinity). The finite root a^(0),b^(0) is not claimed to remain a root after the tail is added unchanged.

All tail conditional cumulants are enclosed WITHOUT evaluating a truncated zeta sum. Since c_tail<5/2 by (4), if L_n is the sum of absolute coefficients of c_n(m), then

    |tail K_1| <= k(25/4)/(J-1),
    |tail K_n| <= L_n (5/2)^n/[(n-1)(J-1)^(n-1)], 2<=n<=16.     (30)

This is the full integral-test bound on sum_(j>=J)j^-n. Each tail is constant with respect to the finite head coordinates. Add these outward intervals to (14) BEFORE computing moments, derivatives, the preconditioner and box residual. The result is

    delta_infinity <1.337e-29,
    q_infinity <1.267e-11,
    delta_infinity+q_infinity*10^-24 <10^-24.                    (31)

Banach therefore proves a unique head root for the ACTUAL tail (29), uniformly covered by (30). It matches the unchanged native moments through 14 exactly, has b>0 and all positive head/leaf couplings, and has only real zeros by (7)–(9) and the complete product limit. Its sixteenth-moment difference still lies in (-.115,-.114). It is NOT Psi.

Its entire MGF has exactly the native LEADING logarithmic growth:

    log A_infinity(iy)=c_tail y log y+O(y).                      (32)

Proof: for j<=c_tail y, log cosh(c_tail y/j)=c_tail y/j+O(1); summing produces c_tail y log y+O(y), with J fixed. For j>c_tail y, 0<=log cosh(c_tail y/j)<= (c_tail y/j)^2/2, whose complete sum is O(y). The bias correction log[1+k a_j tanh(a_j y)] is nonnegative and O(log y) on the first range, and O(1) on the second, using tanh u<=u. F#(iy) is the larger of the two positive summands, so log A differs from log F# by at most log 2. Finite head factors add only O(y). QED.

This model has unbounded support (otherwise its MGF logarithm would be O(y)), no Gaussian dust, square-summable but non-summable harmonic weights, and genuine nonzero interactions. The very large start J is a conservative perturbation device, not a useful numerical approximation scale. Equality of the leading coefficient in (32) does NOT match the linear subleading term, identify individual zeros, or establish whole-source convergence to theta.

## 7. Complete sufficient ending, and the actual unfinished step

Here is a precise all-order target, not an assumed lemma:

**OPEN-STAR.** For every integer m>=1, construct a finite star with b,a_i>=0, m_i=a_i/100<1, such that

    |E X_m^(2r)-nu_(2r)|<=2^-m, 1<=r<=m.                        (33)

It suffices to do this for an unbounded subsequence of m. No fixed graph size or fixed tail start is imposed. This ansatz may be stronger than RH; Section 5 shows its nondegenerate limits have simple real zeros. Neither necessity under RH nor (33) is proved.

**Conditional ending, fully supplied.** The variance bound in (33) gives V<=3/2 (or the looser V=2). For Y=b+sum a_i tau_i, put d=b+k S and S=sum a_i^2. The logarithm of the biased-sign MGF has second derivative at most one. Taylor's theorem therefore gives

    E exp(t(Y-d)) <= exp(S t^2/2), t real.

Average t and -t and use cosh u<=exp(u^2/2):

    E exp(tX) <= exp((S+d^2)t^2/2),
    S+d^2=Var(X)+k^2 sum a_i^4 <=V+k^2 V^2.                     (34)

Thus |A_m(z)|<=exp((V+k^2V^2)|z|^2/2) on every complex disk. Montel supplies subsequential locally uniform entire limits. Cauchy's formula and (33) identify every derivative at zero with that of Psi, including the zero odd derivatives. Entire uniqueness identifies every subsequential limit with Psi, so the FULL sequence converges locally uniformly. Each A_m has no off-real zeros by Section 2; Hurwitz excludes them for Psi, which is not identically zero. Scaling back proves RH. This uses no simplicity hypothesis about Xi.

**What failed in the attempted completion.** A selected-coordinate continuation from the fourteen-moment root toward the sixteenth theta cumulant failed at its first attempted 1/16 step. Earlier small-star, chain and dense-block searches also stalled. These are nondirected search outcomes, not impossibility theorems. The accepting calculation proves the mismatch (17) for the exhibited roots, not that every 96-spin star misses moment 16. No cofinal parameter continuation, positive-parameter degree argument, or uniform moment-lifting radius was obtained.

The infinite completion in Section 6 resolves real-zero geometry, infinite support, all transform tails, seven native moments, and the leading MGF growth for ONE model. It does not resolve (33). Matching many moments plus the correct growth class is demonstrably insufficient: the certified sixteenth moment remains wrong. The next load-bearing task is genuine target reachability at unbounded order, not another claim that a finite full-rank Jacobian can be iterated without hitting a boundary.

## 8. Review boundary

Theorem-sized components STAR26-1 through STAR26-5 have proofs above. STAR26-2 and STAR26-5 also depend on the executable arithmetic contract in CERTIFICATE.md. The code is not formal verification. Check the exact theta scaling, every omitted source term, the polynomial-to-Gibbs law, row-sum contraction, harmonic tail derivatives, compactness dust shift, and the separation between native Xi and the constructed model A.

Classical tools and the general Ising route are credited. The mathematical claim is the stated source-specific construction and the homogeneous-star obstruction, not a claim that their general mechanisms are unprecedented. No previous research, main, canonical status, formal files, or workflows are changed by this packet.
