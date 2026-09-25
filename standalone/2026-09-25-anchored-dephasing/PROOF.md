# ADP37: anchored dephasing, an independent mean-square bound, and the principal-phase obstruction

Date: 25 September 2026.
Status: PROPOSED component mathematics; independent mathematical review required.
Parent: CAP36, PR #907, `c5ee83dc5f2f5f7ffa2d89b45298923a04e6cf0b`.
Scope: the SAME smoothly selected microscopic centered-harmonic observable; exact product collisions and anchored-phase aliases; a finite, source-energy-independent phase-average estimate; an all-scale counterexample to generic mean-to-principal extraction for this ACTUAL harmonic observable.
Not claimed: an upper bound for the native principal phase, a subquadratic full Newton recurrence, control of the unmasked complement, or RH.

## 0. What this pass establishes

CAP36 bounds a difference between two phase-transformed quantities. This pass independently bounds an average of the original phase-twisted observable. For the native cap-three source, the finite anchored Fejer average is at most

    648 [1+(L^2 log(Y)/K)^2] h_(16H)^2 (2 h_L-1),        (0.1)

under the explicit separation hypotheses below. Here h_j=sum_(a=1)^j 1/a, L is the source length, and K determines the phase averaging weights. The bound contains NO native input energy F_Y. For K>=2L^2 log Y it is logarithmic in L at fixed bandwidth H. All product collisions remain in the diagonal before the bound is applied.

This is not a new general mean-value theorem for Dirichlet polynomials. Finite Fourier orthogonality, Fejer kernels, separation/Schur bounds, and the gcd parametrization of ab=cd are classical. They are proved here with the normalization, exact product support, and anchors of CAP36 retained.

A second result prevents a false closure: there are real reciprocal-balanced sources with |c(n)|<=1, using the SAME harmonic mask, for which the principal observation energy is at least 2^(-72)L^2 whereas its limiting anchored mean is O(log L). These sources are NOT native Mobius prefixes. Thus generic balance, coefficient caps, mask smoothness and phase averaging cannot by themselves extract the principal native member with a subpower loss. A genuinely native arithmetic concentration theorem is still needed.

## 1. Literal observable and product coefficients

Take integers L>=2, H>=1, X>=8H, and X<=M<2X, with B=L^2<=8X. Let c be any finite complex source supported through L. No reciprocal balance is needed in Sections 1--4. Put

    z(n)=(c*c)(n),  n<=B,
    Z_alpha(k)=sum_(a=1)^k exp(2 pi i a alpha)/a
                         +log(1-exp(2 pi i alpha)).

The logarithm is the radial Abel value, so Z is the complete centered harmonic tail. Define eta_H(t)=1 for 0<=t<=H, zero for t>=2H, and

    eta_H(t)=1-10v^3+15v^4-6v^5, v=(t-H)/H

on the intervening interval. Set

    g_k(t)=eta_H(t) [2 sum_(a<=k) cos(2 pi a t/X)/a
                                     +2 log(2 sin(pi t/X))],
    Phi_k(n)=(1/n) sum_(j>=1) g_k(jX/n),
    b_n(k)=z(n) Phi_k(n).                              (1.1)

Each j sum is finite and Phi_k(n)=0 when n<=A=X/(2H). The original reduced-frequency observable of CAP36 is exactly

    U_tau(k)=U(c_chi,c_chi;k)
            =sum_(A<n<=B) b_n(k) exp(i tau log n),
    chi(n)=n^(i tau).                                 (1.2)

This is a bilinear source square, not an absolute square. Only its subsequent observation energy is Hermitian. Formula (1.2) follows by unreducing fractions and using complete multiplicativity; it includes every factorization r s=n through L. No transformed compressed kernel Psi from CAP36 is substituted for Phi.

Write vectors b_n=(b_n(k))_(k=X)^M and use the ordinary Euclidean observation norm. Define the exact product diagonal

    D(c;X,H,M)=sum_n ||b_n||^2.                        (1.3)

It is |sum_(rs=n)c(r)c(s)|^2 in this expression, NOT sum_(rs=n)|c(r)c(s)|^2. Those are generally different.

## 2. The exact anchored average and its aliases

Fix an integer anchor Y>=2, and let

    tau_j=2 pi j/log Y,
    w_(K,j)=(K-|j|)/K^2 for |j|<K, zero otherwise,
    A_K=sum_j w_(K,j) ||U_(tau_j)||^2,   K>=1.         (2.1)

The weights are nonnegative and sum to 1. Expanding the finite Hermitian square gives

    A_K=sum_(n,m) <b_m,b_n> F_K(log(n/m)/log Y),        (2.2)
    F_K(theta)=|K^(-1) sum_(r=0)^(K-1)e^(2 pi i r theta)|^2
              =[sin(pi K theta)/(K sin(pi theta))]^2. (2.3)

At integer theta the value is exactly 1. Formula (2.3) is the normalized classical Fejer kernel, including its normalization 1/K^2. It is real, nonnegative, and at most 1. The source inner products may have either sign or complex phase; positivity of F_K does not authorize making those inner products positive.

### Theorem 1: exact alias-sensitive limiting mean

Let n~m mean n/m=Y^r for an integer r. Then

    lim_(K->infinity) A_K
        =sum_(alias classes C) ||sum_(n in C)b_n||^2.  (2.4)

Proof. In (2.2), F_K(theta)->0 at every noninteger theta and equals 1 at integers. The sums are finite. Group the surviving pairs. QED.

An integer representative for a class is obtained by repeatedly dividing n by Y while Y divides n. This remains true when Y is composite or a perfect power: the permitted ratios are integer powers of Y, not arbitrary powers of rad(Y) or of its perfect-power base.

Aliases matter. At anchor Y=4, coefficients 1 and -1 at indices 3 and 12 give U_(tau_j)=0 at EVERY j, although the ungrouped diagonal is 2. The checker rejects dropping this cross term. This is a scalar control for the general averaging identity, not a claimed native harmonic counterexample.

## 3. Finite dephasing with a complete remainder bound

Assume in addition

    Y X >= 4 H B.                                    (3.1)

Since B<=8X, Y>=32H is a simpler sufficient condition; (3.1) is the sharper condition used by the checker. If the active set is empty all statements are trivial. Otherwise B/A<=Y/2, so no two active indices are aliased.

For distinct active n,m, their circular frequencies theta_n=log n/log Y modulo 1 have separation at least

    delta=1/(B log Y).                               (3.2)

Indeed, suppose n>m. If log(n/m)/log Y<=1/2, then log(n/m)>= (n-m)/n>=1/B. Otherwise the distance around the other side of the circle is log(Ym/n)/log Y>=log 2/log Y>=1/(B log Y). Here B>=4. The same argument gives pairwise circular separation for every pair.

### Theorem 2: finite anchored mean-square comparison

For every K>=1,

    |A_K-D| <= (B log Y/K)^2 D.                       (3.3)

Proof. For noninteger theta, |sin(pi theta)|>=2||theta||. Therefore

    0<=F_K(theta)<=1/[4K^2||theta||^2].

Order other frequencies clockwise and counterclockwise from a fixed one. The r-th point in each half-circle has distance at least r delta. The complete off-diagonal row sum is at most

    2 sum_(r>=1) 1/[4K^2 r^2 delta^2]
        <1/(K^2 delta^2),

using sum r^(-2)<2. The Hermitian Schur bound, applied for each observation coordinate and then summed, proves (3.3). No off-diagonal term was discarded or assigned a favorable sign. QED.

In particular, K>=2B log Y yields

    (3/4)D <= A_K <= (5/4)D.                          (3.4)

The number of sampled phases is 2K-1. Their largest absolute frequency is 2pi(K-1)/log Y. Thus this guaranteed dephasing scale is of order B=L^2 in tau, NOT the bounded-tau regime of CAP36's simpler small-defect estimate. This is a sufficient scale from our proof, not a lower bound on the scale needed for a particular native source.

## 4. An independent logarithmic upper bound

### Lemma 3: complete product-collision count

For integers L_1,L_2>=1, let

    M(L_1,L_2)=#{a,c<=L_1; b,d<=L_2: ab=cd}.

Then, writing ell=min(L_1,L_2),

    M(L_1,L_2)=L_1 L_2
        +2 sum_(r=2)^ell varphi(r) floor(L_1/r)floor(L_2/r)
      <=L_1 L_2 (2h_ell-1).                           (4.1)

Proof. Write a=g u,c=g v with (u,v)=1. The equality forces b=h v,d=h u. For r=max(u,v), the allowed g and h have the displayed floor counts. There is one coprime pair at r=1 and 2varphi(r) pairs at r>=2. For the upper bound use varphi(r)<=r and the two floor bounds. QED.

This is a classical gcd parametrization, rederived rather than claimed as a new multiplicative-energy theorem. For complex c with |c(n)|<=C, expansion and absolute values AFTER grouping give

    sum_n |z(n)|^2 <= C^4 M(L,L)
                       <=C^4 L^2(2h_L-1).            (4.2)

This logarithmic bound is sharper here than estimating each z(n) by C^2 d(n) and summing d(n)^2 through L^2, which loses three logarithms.

### Lemma 4: exact harmonic kernel envelope

For every retained t and every k>=X,

    |2 Re Z_(t/X)(k)| <=1/t.

For example, partial sums of exp(2pi i a alpha) have magnitude at most 1/|sin(pi alpha)|. Abel summation of the ENTIRE tail gives |Z_alpha(k)|<=1/[(k+1)|sin(pi alpha)|]. On alpha=t/X<=1/4, sin(pi alpha)>=2alpha, proving the stated paired bound. Centering is essential; the finite uncentered harmonic sum does not obey it.

Hence, using 0<=eta_H<=1 and j<2Hn/X<=16H,

    |Phi_k(n)| <= h_(16H)/X.                          (4.3)

Combine (4.2)--(4.3), M-X+1<=X, and B<=8X:

    D <= C^4 (L^2/X) h_(16H)^2 (2h_L-1)
      <=8C^4 h_(16H)^2(2h_L-1).                       (4.4)

### Theorem 5: native, source-energy-independent averaged bound

Let c be the actual cap-three completion of mu through Y, with L<=2Y, and impose the observation hypotheses in Section 1 and (3.1). Then

    A_K <=648[1+(L^2 log Y/K)^2] h_(16H)^2(2h_L-1).   (4.5)

For K>=2L^2 log Y, the right side is at most

    810 h_(16H)^2(2h_L-1).                            (4.6)

These estimates are independent of F_Y and E_Y. They in fact hold for every coefficient-capped source, so they do not exploit a uniquely Mobius cancellation. All output frequencies inside the same mask and every phase-average cross term are included. There is no statement about the unmasked complement.

For any R>0, the total Fejer weight of sampled phases with ||U_tau||^2>R is at most A_K/R. In particular some sampled phase has energy no larger than the displayed upper bound. This is an average/existence result, NOT principal-member extraction.

## 5. The principal-phase obstruction for the ACTUAL harmonic observable

The following uses the very same centered harmonic g_k and eta_H, not the rational bump controls in earlier packets.

### Theorem 6: no generic subpower mean-to-principal transfer

For every integer L>=8192, take Y=L, H=1, X=L^2, epsilon=1/4096, and M=floor((1+epsilon)X). There is a real reciprocal-balanced source c supported through L, with |c(n)|<=1, such that

    ||U_0||_[X,M]^2 >=2^(-72)L^2,                     (5.1)
    0<D=lim A_K <=h_16^2(2h_L-1).                     (5.2)

Consequently any inequality ||U_0||^2<=C_L lim A_K valid for ALL these bounded balanced sources requires

    C_L >= 2^(-72)L^2/[h_16^2(2h_L-1)].               (5.3)

In particular C_L cannot be bounded, polylogarithmic, or L^(o(1)). This is NOT a native Mobius source and does not refute a source-specific estimate.

**Construction.** Let I={floor((1-epsilon)L)+1,...,L}. Set c(n)=1 on I,

    c(1)=-sum_(n in I)1/n,

and set all other coefficients to zero. There are at least epsilon L indices in I. Since L>=8192, |c(1)|<=1, and the source is reciprocally balanced. Every product involving coordinate 1 is at most L<=X/2, so it is invisible to Phi. Thus only positive pairs from I x I contribute.

For r,s in I and X<=k<=M, put t=X/(rs). Then

    1<=t<=(1-epsilon)^(-2)<5/4,
    2pi<=2pi t k/X <=2pi(1+epsilon)/(1-epsilon)^2.     (5.4)

Only j=1 occurs in Phi(rs), since j>=2 would give jt>=2 where eta_1=0.

**A rigorous negative rectangle for the harmonic kernel.** For x>0 use the classical cosine integral Ci(x)=-integral_x^infinity cos v/v dv. The elementary/standard Laplace representation gives

    -Ci(2pi)=integral_0^infinity e^(-2pi v) v/(1+v^2) dv
             >=1/(4pi^2)-6/(16pi^4)>1/50.             (5.5)

The first inequality follows from v/(1+v^2)>=v-v^3. For the final strict inequality it suffices to use 3<pi<22/7: 49/1936-1/216>1/50. The Laplace identity and Ci definitions are credited to DLMF 6.7.14 and 6.2; no asymptotic series is truncated without its sign justification.

For X>=8, X<=k<2X and 0<t<=2, the complete finite expression satisfies

    |z_(X,k)(t)-2Ci(2pi t k/X)| <=200/X,              (5.6)
    z_(X,k)(t)=2sum_(a<=k)cos(2pi a t/X)/a
                                     +2log(2sin(pi t/X)).

Here is a proof with room in the constant. Put a=2pi t and
f(v)=(cos(av)-1)/v, continuously f(0)=0. Since
f(v)=-a integral_0^1 sin(a v s) ds, |f'(v)|<=a^2/2. The right-endpoint Riemann sum with mesh 1/X differs from integral_0^(k/X) f by at most k a^2/(4X^2). The identity
Ci(x)=gamma+log x+integral_0^x (cos v-1)/v dv
and 0<h_k-log k-gamma<1/k then account for all but the sine correction. For u=pi t/X<=pi/4<1,
0<=-log(sin u/u)<=u^2/3,
using sin u/u>=1-u^2/6 and -log(1-w)<=w/(1-w). After multiplication by 2 the three errors are at most

    2/X + a^2/X + (2/3)(2pi/X)^2 <200/X.

The harmonic/gamma bound follows directly from integral comparison of 1/x. Thus (5.6) is uniform, not a numerical approximation claim.

Since Ci'(x)=cos x/x, (5.4)--(5.6) give

    z_(X,k)(t) <=-1/25+8epsilon+200/X <-1/32,         (5.7)

using log((1+epsilon)/(1-epsilon)^2)<=4epsilon and X>=8192^2. Every last inequality is checked rationally in the replay. The polynomial eta_1 decreases on [1,2] and eta_1(5/4)=459/512>1/2. Consequently

    g_k(t)<=-1/64,
    Phi_k(rs)<=-1/(64L^2).                           (5.8)

Therefore U_0(k)<=-|I|^2/(64L^2)<=-epsilon^2/64. There are at least epsilon X observations. Squaring gives epsilon^5 L^2/4096=2^(-72)L^2, proving (5.1). Alias separation holds, and (4.4) with C=1, L^2/X=1 proves (5.2). Positivity of D follows because there is at least one nonzero product coefficient and every relevant Phi is strictly negative. QED.

The constants are deliberately small; their purpose is an unbounded, rigorously signed counterexample, not a useful finite numerical ratio at L=8192. The construction is not evidence of a bad native Mobius phase.

## 6. What this says about CAP36 and the next target

The Fejer estimate independently bounds the original phase family U_tau. It does NOT bound the compressed arithmetic side A_tau of CAP36; that notation is distinct from the Fejer average A_K here. No compression projection has been commuted with Phi.

At K of order L^2 log Y, phase magnitudes reach order L^2. CAP36's convenient estimate for |tau|<=1 cannot be applied to them. Its full formula remains valid for anchored real tau, but its kappa(tau) and tau-dependent defect factors must be paid. Nothing in this packet proves that those costs are small at the dephasing scale.

Also, the positivity of Fejer weights gives only the generic extraction

    ||U_0||^2 <= K A_K,

because w_(K,0)=1/K. Theorem 6 proves that the polynomial loss in a generic extraction cannot simply be wished away. Small averaged output plus invertible source modulation is NOT coercivity for the quadratic observable.

A precise native quantity worth attacking is

    R_native(Y,X,H,M)=||U_0(c_native,c_native)||^2 / D(c_native;X,H,M),

when D>0; define it as 0 when D=0 (then all b_n and U_0 vanish). A polylogarithmic or subpower bound on this ratio for the literal native caps would transfer (4.4) to the principal microscopic sector. It would still leave the complementary frequency sectors and the full recurrence to be assembled with their exact existing hypotheses. We do NOT assert that this ratio estimate is proved, easier than the previous problem, or by itself equivalent to RH.

This formulation isolates an actual distinction: multiplicative product collisions have been bounded independently; coherent addition ACROSS distinct products at the principal phase is still uncontrolled. The nonnative counterexample shows exactly why a proof must use the arithmetic signs beyond balance and coefficient caps.

## 7. Attribution and validation boundary

The Fejer identity, separated-frequency Schur method, Dirichlet-polynomial mean-square perspective and gcd collision parametrization are classical. Montgomery--Vaughan, "Hilbert's Inequality" (1974), is prior art for stronger mean-value/separation machinery; we do not import a sharp constant from it. All estimates used here are proved above. Cosine-integral definitions and the Laplace representation are standard NIST DLMF inputs. CAP36 supplies the literal observable and its source-qualified transport setting; the centered-tail bound is rederived.

No external or repository-wide novelty claim is made. The contribution is the exact anchored/alias-sensitive assembly for this observable, its independent logarithmic averaged bound, and the same-harmonic-kernel obstruction to generic principal extraction.

The checker has separate exact arithmetic, rational structural-kernel, and directed actual centered-harmonic/anchored-phase panels. Its finite numerical enclosures test normalization; the universal analytic statements rely on these written proofs. No independent mathematical review, proof-assistant build, repository-wide validator, remote CI verdict, or complete rerun of historical campaigns is claimed. See VALIDATION.md for executed ranges and limitations.
