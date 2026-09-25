# CAP36: completion-anchored, source-compressed phase transport

Date: 25 September 2026.
Status: PROPOSED component mathematics; independent mathematical review required.
Parent: RLC35, PR #907, `0e4be03a59c266ec54b3a3862b7d4eba2e08ba28`.
Scope: exact finite identities and an all-cutoff quantitative comparison for the SAME smoothly masked microscopic observable. The transformed kernel has two separate source cutoffs; it is not the uncompressed Hankel adapter of RLC35.
Not claimed: a new asymptotic bound for native energy, a subquadratic full Newton recurrence, control of the uncompressed adapter leakage, or RH.

## 0. Result and limitation

Two obstructions in RLC35 can be dealt with together, for a specified microscopic observable. Reciprocal balance can be repaired at coefficient 1 because that coefficient is invisible to this observable in the stated parameter range. Unlike a late repair, this early repair has a cutoff-uniform phase norm. Separately, compressing the arithmetic action BEFORE forming the tensor square confines its defect to the short completion interval. Anchoring the phase at the native cutoff makes that defect small.

The result is a bound for the difference between a compressed arithmetic transform of the microscopic target and a phase twist of that same target. It is not an absolute bound for either unknown target. In particular, the new comparison must not be used as a bounded inversion theorem.

Let c be the cap-three reciprocal-balanced completion of mu through Y>=2, let L=Y+J be its declared support cutoff, and set

    m(k)=sum_(n<=k)mu(n)/n,  F_Y=sum_(k=1)^Y |m(k)|^2,
    rho=J/Y.

For a real phase tau satisfying exp(i tau log Y)=1, set chi(n)=n^(i tau),

    a_chi=1*mu_chi,   q=P_L(a_chi*c),
    U_tau(k)=U(c_chi,c_chi;k),  A_tau(k)=U(q,q;k).

U is precisely the smoothly masked centered-harmonic observable in Section 1. Under

    H>=1, X>=8H, X>=2HL, L^2<=8X, X<=M<2X,

we prove

    ||A_tau-U_tau||_[X,M]^2
      <=2^21 H^4 [2 kappa(tau) sqrt(J(c) D)+D]^2,          (0.1)
    kappa(tau)=sqrt(1+tau^2)+|tau|,
    D=32 tau^2 J^4/Y^3.

Here J(c), with an argument, is the reciprocal-primitive energy, not the integer completion width J. In particular D<=192 tau^2 rho F_Y. For |tau|<=1,

    ||A_tau-U_tau||_[X,M]^2 <=2^39 H^4 tau^2 rho F_Y^2    (0.2)
      <=2^41 H^4 tau^2 Y^(-1/3) F_Y^(7/3).              (0.3)

The F exponent in (0.3) is 7/3, NOT subquadratic. The saving is in the comparison error, not in the size of U_tau. No smallness relative to U_tau itself is asserted; that observable can be zero.

The phase set is tau_j=2 pi j/log Y. Finite linear combinations with sum of absolute coefficients at most one have the same worst-parameter norm bound. There is no factor equal to the number of phases. This is a family of explicit finite comparisons, not principal-member extraction from a family average.

## 1. Exact observable and a coordinate that it cannot see

For finite complex sources u,v supported through L, define

    Z_alpha(k)=sum_(n=1)^k exp(2 pi i n alpha)/n
                         +log(1-exp(2 pi i alpha)),

where the logarithm is the radial Abel value. Keep its entire centered tail. For integers H>=1, use eta_H(t)=1 on [0,H], zero on [2H,infinity), and

    eta_H(t)=1-10w^3+15w^4-6w^5,
    w=(t-H)/H,  H<t<2H.

It is C^2 and has its first two derivatives zero at each endpoint. Define

    B_d(u,v)=sum_(d|n)(u*v)(n)/n,
    U(u,v;k)=sum_(d=2)^(L^2) B_d(u,v)
       sum_(1<=a<d,(a,d)=1) eta_H(X||a/d||) Z_(a/d)(k).  (1.1)

All denominators and all reduced fractions admitted by this one mask occur. The source pairing is BILINEAR, not Hermitian; absolute values enter only in norm estimates.

Pair the two conjugate frequency locations, and put

    g_k(t)=eta_H(t)[2 sum_(n<=k)cos(2 pi n t/X)/n
                                  +2 log(2 sin(pi t/X))],
    f_k(z)=sum_(j>=1)g_k(jX/z),   Phi_k(n)=f_k(n)/n.      (1.2)

Use g_k(t)=0 for t>=2H. Since X>=8H, no retained location is a half-turn or an integer. Unreducing fractions in (1.1) gives, without any balance assumption,

    U(u,v;k)=sum_(r,s<=L)u(r)v(s)Phi_k(rs).              (1.3)

Every sum defining f_k(z) is finite. Crucially,

    Phi_k(n)=0 for n<=X/(2H).                          (1.4)

Let ell(u)=sum_(n<=L)u(n)/n, and let

    Pi u=u-ell(u)delta_1.                              (1.5)

This is a projection onto the reciprocal-balanced sources. If X>=2HL, every product involving coordinate 1 and any other source coordinate is in (1.4). Consequently

    U(u,v;k)=U(Pi u,Pi v;k).                           (1.6)

This is an exact observable identity. Pi changes the literal coefficient at 1. We do NOT claim that the changed vector is a native Mobius prefix for other criteria or for the complete unmasked Newton output. The change is authorized here by (1.4), not by permission to substitute arbitrary mollifiers. This does not contradict RLC35's counterexample to a late, source-preserving balance repair.

## 2. A bounded, balance-preserving phase action

For a balanced source c, set

    J(c)=sum_(j=1)^(L-1) |sum_(n<=j)c(n)/n|^2,
    B_tau c=Pi(c_chi),  chi(n)=n^(i tau).               (2.1)

Theorem 1. For every such finite complex source and every real tau,

    kappa(tau)^(-2) J(c)<=J(B_tau c)<=kappa(tau)^2 J(c). (2.2)

There is no L, Y or prime-count factor. Moreover B_tau B_sigma=B_(tau+sigma) on the balanced subspace, with inverse B_(-tau).

Proof. Set x(t)=sum_(n<=t)c(n)/n for 1<=t<=L. Then x(L)=0 and J(c)=integral_1^L |x(t)|^2 dt. Finite tail Abel summation gives the primitive of B_tau c:

    y(t)=-sum_(t<n<=L)c(n)n^(i tau)/n
        =t^(i tau)x(t)+integral_t^L i tau v^(i tau-1)x(v)dv. (2.3)

Put h(w)=exp(w/2)x(exp w), on 0<w<log L. Its image is

    (I+i tau R*) M_tau h,
    (R*h)(w)=integral_w^(log L)exp(-(v-w)/2)h(v)dv,
    M_tau h(w)=exp(i tau w)h(w).                        (2.4)

Zero extension turns R* into the full-line anticausal convolution, followed by restriction. Its Fourier multiplier is 1/(1/2-i xi). Thus the square of the multiplier modulus of I+i tau R* is

    [1/4+(xi-tau)^2]/[1/4+xi^2].                       (2.5)

Its supremum is kappa(tau)^2, by elementary maximization. Plancherel, restriction and the unitarity of M_tau prove the upper bound. Since chi(1)=1, the projection correction at 1 gives Pi M_tau Pi M_sigma=Pi M_(tau+sigma) on balanced sources. This proves the group law and then the lower bound by applying the upper bound at -tau. QED.

The continuous extremal multiplier calculation is classical Fourier operator theory; no new Hilbert-space spectral theorem is being claimed. Section 2 adapts it to the reciprocal metric and the explicit early repair needed by (1.6). It is a different metric/interface from RLC35's uncentered late repair.

## 3. Compress first: the exact defect has only J coefficients

Let c agree with mu through Y, let L<2(Y+1), and let chi be any completely multiplicative function with chi(1)=1. Define

    a_chi=1*mu_chi,
    q=P_L(a_chi*c),
    r=q-c_chi.                                        (3.1)

Theorem 2. Coefficientwise through L,

    r(n)=0 for n<=Y,
    r(n)=(1-chi(n))(c(n)-mu(n)) for Y<n<=L.             (3.2)

Proof. Write e=c-mu through L. Mobius inversion gives a_chi*mu=mu_chi. Every nonzero coefficient of e has index at least b=Y+1. A term a_chi(d)e(n/d) with d>=2 therefore has index n>=2b. It is absent at all n<=L. Thus P_L(a_chi*e)=e, and (3.2) follows. QED.

This is not a claim that the uncompressed r_chi of RLC35 has only J coefficients. P_L is taken on EACH source factor before the tensor square. It changes the transformed kernel, as Section 6 records exactly.

For phases chi(n)=n^(i tau), a_chi(n)=product_(p|n)(1-p^(i tau)), with a_chi(1)=1. The divisor product and Mobius inversion are classical (DLMF 27.5 and 27.6.2). The source and all product collisions are literal; there are no independent replacement amplitudes.

## 4. Anchor at Y: an explicit small-width bound

Assume now the native cap-three source, |c(n)|<=3, L=Y+J<=2Y. Choose

    exp(i tau log Y)=1.                               (4.1)

For Y<n<=L,

    |1-chi(n)|=|1-exp(i tau log(n/Y))|
              <=|tau|log(n/Y)<=|tau|(n-Y)/Y,
    |r(n)|<=4|tau|(n-Y)/Y.                            (4.2)

Let d=Pi r. Its reciprocal primitive is the exact negative tail of r. For every 1<=j<L,

    |sum_(n<=j)d(n)/n|=|sum_(j<n<=L)r(n)/n|
       <=4|tau| sum_(h=1)^J h/[Y(Y+h)]
       <=2|tau| J(J+1)/Y^2.                           (4.3)

There are at most 2Y primitive cells. Therefore

    J(d)<=8 tau^2 J^2(J+1)^2/Y^3
         <=32 tau^2 J^4/Y^3 = D.                     (4.4)

For J=0, r=d=0 and all these conclusions hold with D=0. Note that Pi r may have a nonzero coefficient at 1; its WHOLE primitive energy, including the long constant portion before Y, has been paid in (4.3)-(4.4). The saving is due to the anchored phase, not a deletion of that portion.

### Native completion estimates, with their costs retained

For completeness we reproduce the needed estimates from NCG28. Write a=|m(Y)|. The finite divisor identity sum_(n<=k)mu(n)floor(k/n)=1 gives

    |m(k)|<=1,   F_Y>=1.                              (4.5)

Indeed k m(k)=1+sum mu(n){k/n}; the absolute value is at most 1+k-H_k<=k. For 0<=j<=floor(aY/4),

    |m(Y)-m(Y-j)|<=j/(Y-j+1)<=a/3.

There are at least aY/4 such indices, so F_Y>=Ya^3/9. Hence

    Ya^3<=9F_Y.                                      (4.6)

The cap subtracts reciprocal mass of the same sign with each next coefficient of magnitude at most 3, using only the necessary amount in its final coefficient. Its first j full coefficients have capacity at least 3j/(Y+j). Thus, if a>0,

    J<=ceil(Ya/(3-a))<=ceil(Ya/2)<=Ya/2+1,
    J<=ceil(Y/2),  L<=2Y.                            (4.7)

If a=0, set J=0. For each relevant correction index i<=ceil(Y/2), 3/(Y+i)>=1/(Y-i+1). Comparing the remaining residual after j corrections with |m(Y-j)|, by the reverse triangle inequality, pays the entire completion primitive:

    J(c)<=2F_Y.                                      (4.8)

In (4.7), use (x+1)^3<=4(x^3+1), (4.6), Y>=2 and F_Y>=1. This gives

    J^3/Y^2<=Ya^3/2+4/Y^2<=6F_Y,
    D<=192 tau^2 (J/Y) F_Y.                          (4.9)

Also rho=J/Y<=a/2+1/Y<=3(F_Y/Y)^(1/3). All these are all-cutoff finite inequalities. No PNT, zero-free region, or conjectural sign cancellation enters them.

Without (4.1), the leading defect includes (1-chi(Y))(c-mu). It cannot be bounded by the logarithmic width alone. Section 4 is not an estimate for arbitrary phase parameters, arbitrary character twists, or arbitrary balanced completions of length comparable to Y with many more correction coefficients.

## 5. Full masked covariance comparison

We state and rederive the needed bilinear estimate so that the complex phase extension has no implicit real-to-complex gap. It is the rectangular microscopic estimate from CQT32, with the same constants and mask.

Lemma 3. For any two complex balanced sources u,v supported through L, if X>=8H and L^2<=8X, then

    sum_(k=X)^M |U(u,v;k)|^2<=2^21 H^4 J(u)J(v).      (5.1)

Proof. With the g_k of (1.2), finite trigonometric summation including the logarithmic constant gives

    z_k'(t)=(2pi/X)cos((2k+1)pi t/X)/sin(pi t/X),
    z_k(t)=2sum_(n<=k)cos(2pi n t/X)/n+2log(2sin(pi t/X)).

Abel summation of the entire harmonic tail and sin(pi t/X)>=2t/X give, on 0<t<=2H,

    |z_k(t)|<=1/t, |t z_k'(t)|<=4,
    |t^2 z_k''(t)|<=64t+8.

Also |eta_H'|<=2/H and |eta_H''|<=6/H^2. Expanding derivatives shows

    |t g_k'(t)+t^2 g_k''(t)|<=256H.

For f_k(v)=sum_j g_k(jX/v), only j<2Hv/X enter, so

    |f_k'(v)+v f_k''(v)|<=512H^2/X.                   (5.2)

The flat C^2 zero endpoint justifies differentiation through each entry point. Separate finite summation by parts in (1.3), using both balances, gives

    U(u,v;k)=sum_(r,s<L)x_r y_s
       [f_k(rs)-f_k((r+1)s)-f_k(r(s+1))+f_k((r+1)(s+1))],

where x_r and y_s are the two reciprocal primitives. The bracket is the integral of f_k'(ab)+ab f_k''(ab) over a unit rectangle. Equation (5.2) and Cauchy--Schwarz bound each |U| by (512H^2/X)L sqrt(J(u)J(v)). There are at most X observations; L^2<=8X gives (5.1). This proof uses absolute values after the exact bilinear identity and therefore applies unchanged to complex sources. QED.

Set p=B_tau c=Pi c_chi and d=Pi r. The invisibility identity (1.6) implies, for EACH k,

    A_tau(k)-U_tau(k)=2U(p,d;k)+U(d,d;k).              (5.3)

Equations (2.2), (4.4), (5.1), and the triangle inequality in the observation norm prove (0.1). This includes every cross term of the masked covariance.

For |tau|<=1, kappa(tau)<5/2 and rho<=1. Substituting J(c)<=2F_Y and D<=192 tau^2 rho F_Y into (0.1) yields

    ||A_tau-U_tau||^2
      <=2^21 H^4 F_Y^2 tau^2 rho
              [16sqrt(6) kappa(tau)+192|tau|sqrt(rho)]^2.

The bracket is less than 512. This proves (0.2), and rho<=3(F_Y/Y)^(1/3) gives (0.3). Constants are intentionally conservative, not fitted to finite tests.

For tau_1=2pi/log Y<=1 the comparison has the additional explicit factor 4pi^2/log^2 Y. It remains a comparison against the generic F_Y^2 scale, NOT a relative bound against the actual unknown U_tau.

For weights lambda_j with sum |lambda_j|<=1 and anchored |tau_j|<=T<=1, apply the norm triangle inequality to (5.3) and use (0.2). The combined comparison has bound 2^39 H^4 T^2 rho F_Y^2, independently of the number of phases. No orthogonality or random phases are assumed.

## 6. What compression changes: the precise new kernel and the remaining obstacle

The compressed arithmetic side is explicitly

    A_tau(k)=sum_(r,s<=L)c(r)c(s)Psi_tau,k(r,s),
    Psi_tau,k(r,s)=sum_(d<=L/r,e<=L/s)
                        a_chi(d)a_chi(e)Phi_k(r s d e). (6.1)

It generally depends on r and s separately, not just their product. The two source cutoffs in (6.1) are part of the theorem. They cannot be replaced by the single product cutoff de<=L^2/(rs). This is an exact finite source-compressed adapter, not a claim that source projection commutes with a Mellin/Hankel operation.

An exact countercontrol uses the actual cap source at Y=2:

    c=delta_1-delta_2-(3/2)delta_3,  L=3, chi(n)=1/n.

For a_chi=1*mu_chi, the full q=a_chi*c has q(1)=1, q(3)=-5/6, q(9)=-1/3. Hence

    (q*q)(9)-(P_3 q*P_3 q)(9)=-2/3.                   (6.2)

With the structural test kernel g(t)=(1-t)^4 on (0,1), zero thereafter, and X=8, Phi(9)=1/9^5. The omitted leakage pairing is -2/(3*9^5), not zero. This is an exact rational control in the same unreduced-product construction, NOT a numerical evaluation of the actual harmonic g_k or an anchored phase-norm test.

Thus CAP36 does not bound the entire residual of RLC35's UNCOMPRESSED kernel identity. It constructs and bounds a different, explicitly compressed transport relation for the same original observable. The uncompressed leakage is still a separate problem.

The substantive remaining obligation is to exploit (6.1) and (0.1) to bound an unknown target independently, for example by controlling the transformed kernels or establishing an appropriate source-specific coercivity statement. Merely showing that two unknown quantities nearly agree is not an absolute covariance estimate. No inversion, contraction under prime insertion, all-frequency estimate, or native asymptotic gain follows from this packet alone.

## 7. Attribution and validation scope

Mobius inversion and the divisor product are classical. The cap estimates are NCG28's source-qualified estimates, rederived above. The harmonic derivative estimate and the microscopic bilinear bound are MCB31/CQT32, also rederived with complex sources. The Fourier multiplier method is the classical method used by RLC35, here applied to the anticausal reciprocal-primitive action. No external or repository-wide priority claim is made.

The contribution is the combination of exact observable-invisible balance repair, factorwise compression, cutoff-anchored phases, and a quantitative short-completion defect bound. Its proof is finite arithmetic, Abel summation, and Fourier/elementary norm estimates. No RH-bearing input is assumed.

The checker verifies exact primitive cap data, native and nonnative controls, Gaussian-rational and rational character identities, factorwise compressed kernels, all product terms in its declared panels, balance projection/group algebra, the rational defect envelope, and deliberately failed shortcuts. Analytic statements for actual real phases and the centered harmonic kernel rely on the written proof, not on finite rational examples. See VALIDATION.md for the exact executed ranges, commands, and remaining review boundaries.
