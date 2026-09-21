# CQT32: completion invariance, divisor-closed compensation, and rectangular microscopic covariance

**Proposed component proofs, 21 September 2026. Independent review required.**
**The complete native covariance estimate and RH are NOT proved.**

This continues the source-completion constructions preserved in PREVIOUS_PASS.md. The new upper estimate is a rectangular, mixed-source extension of MCB31. The exact identities also settle an important limitation of the proposed completion optimization: on the native bulk, changing completion cannot change the complete covariance at all. This is not a prohibition on finding a better proof using a different representation.

Read against #904 at aaea3f9605a430600bea0189397d93ca315b5f98, #905 at 98cf588261473724178231c667595fc09cc216fe, and the newer DCN26 on #903 at f80aa1346bbc457d5726977c0b720162c05bb70e. All three remain research packets, not independently accepted theorems here.

## 1. The exact bilinear observable

Convolution is ordinary Dirichlet convolution; 1 is the constant-one arithmetic function and delta is its convolution identity. Let c,d be finite real sources, separately reciprocal-balanced. Define

    m_c(k)=sum_(n<=k)c(n)/n,
    J(c)=sum_(k>=1)m_c(k)^2,
    Q_(c,d)(k)=sum_n (c*d)(n)/n H_floor(k/n), H_0=0.       (1)

The source supports are finite, but the observation argument k can be arbitrary. The reciprocal primitive of 1*c*d is exactly (1). The product c*d has zero reciprocal and logarithmic moments:

    sum_n(c*d)(n)/n=0,
    sum_n(c*d)(n)log(n)/n=0.                            (2)

For the second equation expand log(ab)=log a+log b and use both balances. Consequently (1) is also the COMPLETE sum of centered harmonic Fourier modes with amplitudes

    B_q(c,d)=sum_(q|n)(c*d)(n)/n.                       (3)

No partial centering constant may be dropped. The finite Fourier identity can be checked by first summing all j/n, reducing fractions only afterward, and using (2). This is the inherited Newton/Fourier adapter, extended bilinearly, not a new Fourier convention.

The reciprocal output of the rectangular Newton source is

    v=c+d-1*c*d,
    m_v=m_c+m_d-Q_(c,d).                               (4)

If c=mu through A and d=mu through B, then

    mu-v=mu*(delta-1*c)*(delta-1*d).                    (5)

Both factors on the right vanish below A+1 and B+1 respectively. Hence

    v(n)=mu(n) for n<(A+1)(B+1).                       (6)

There is no equality claim at the product endpoint. Formula (5) follows by expanding its right side and using mu*1=delta, so it does not need unproved cancellation. The symmetric short-prefix inverse is classical; Huxley--Watt arXiv:1807.05890 is an explicit antecedent, not a novelty claim for (5).

## 2. The complete output is affine and its covariance is quadratic in completion variables

Let c retain mu through Y, b=Y+1, and let h,g be finite reciprocal-balanced sources supported at indices >=b. Then, for every integer k<b^2,

    Q_(c,h)(k)=m_h(k),
    Q_(h,g)(k)=0.                                     (7)

For the first identity consider the coefficient of 1*c*h at n<b^2. Every nonzero h(j) has j>=b, so n/j<b. At that quotient 1*c equals delta. The coefficient is therefore h(n). Taking its reciprocal primitive proves the first identity. The second follows because every product of a support index of h and one of g is >=b^2. Balance is needed for the centered spectral interpretation; this coefficient proof itself is already finite.

It follows for every real t that

    Q_(c+t h,c+t h)(k)=Q_(c,c)(k)+2t m_h(k), k<b^2.    (8)

Thus for any set I of native observation integers and its counting norm,

    ||Q_(c+t h,c+t h)||_I^2
       =||Q_(c,c)||_I^2
        +4t <Q_(c,c),m_h>_I+4t^2||m_h||_I^2.           (9)

All cubic and quartic terms of the complete covariance cancel exactly. For several perturbations its Hessian is 8 times the Gram matrix of their primitives. In particular, if h has support at most L, the full output and energy on every I contained in [L,b^2) are INVARIANT under h.

This does not establish invariance for a chosen set of denominators, an angular or Mellin projection, or observations at and after b^2. It also does not forbid a new estimate exploiting a favorable representation. It does rule out treating numerical reduction of selected B_q as reduction of the full native covariance.

### Sharp endpoint control

Take h=b delta_b-(b+1)delta_(b+1). It is balanced and supported after Y. Then Q_(h,h)(k)=0 for k<b^2, but Q_(h,h)(b^2)=1. The strict endpoint in (7) is necessary. This is explicitly tested.

### Exact source-plus-output optimization

For Y<L<=B=b^2-1, lambda>0, allow all balanced c with c(n)=mu(n) through Y and support at most L, with NO coefficient cap. Then

    min_c sum_(k=Y+1)^B [Q_(c,c)(k)^2+lambda m_c(k)^2]
      =lambda/(lambda+4) sum_(Y<k<L)m(k)^2
       +sum_(L<=k<=B)m(k)^2.                           (10)

Indeed the free variables m_c(k), Y<k<L, can be prescribed independently: recover c(n)=n[m_c(n)-m_c(n-1)] and impose m_c(L)=0. On the native range Q_(c,c)=2m_c-m. Completing the square gives

    (2x-m)^2+lambda x^2
      =(lambda+4)(x-2m/(lambda+4))^2
        +lambda m^2/(lambda+4).

Thus the optimum has m_c(k)=2m(k)/(lambda+4) on those free coordinates. Beyond L the bulk energy is untouched. This is an exact DIAGNOSTIC optimum involving future native m-values, not a source-only upper estimate or an RH proof. Reconstructibility of those values from the known prefix does not bound their size.

## 3. Closing the transferred semiprime modes completely

Use the optimal three-point construction with

    P_Y={p prime: 3b/4<p<=Y}.

For each protected p, the modified source contains the balanced pair

    e_p=-delta_p+2delta_(2p).

The remainder of the source consists of all other indices, including the adjacent compensators; it is not discarded. For distinct protected p,r, the ORDERED cross product z_pr=2e_p*e_r has precisely

    z_pr(pr)=2, z_pr(2pr)=-8, z_pr(4pr)=8.              (11)

Its only nonzero divisibility amplitudes are

    B_(2d)(z_pr)=-2/(pr), B_(4d)(z_pr)=2/(pr), d|pr.   (12)

There are eight denominators: 2,4,2p,4p,2r,4r,2pr,4pr. The last two are the modes tracked in the preceding pass. The first six are their required SOURCE-ATTRIBUTED divisor closure. They are contributions to the actual B_q, not necessarily the whole B_q of the full source. Other source products contribute at the same small denominators.

Equation (11), substituted into (1), gives the complete closed contribution

    S_pr(k)=2/(pr) [H_floor(k/(pr))
                   -2H_floor(k/(2pr))+H_floor(k/(4pr))]. (13)

This vanishes EXACTLY for k<pr. In particular the nonzero early-window second-difference expression in PREVIOUS_PASS.md is canceled by the six other attributed divisor terms. One must not set the entire actual B_2,B_4,... to these attributed values.

On the whole native annulus k<b^2, however, 2pr>9b^2/8>b^2. Hence

    S_pr(k)=2/(pr) 1_(pr<=k),
    S_Y(k)=2 sum_(p<r in P_Y, pr<=k) 1/(pr).           (14)

So the closed packet is zero early and becomes a positive coherent packet near the square endpoint. Full divisor closure removes the early obstruction exactly; it does not remove the packet on the full annulus.

### An all-scale size calculation, using only the classical PNT

Let a=3/4, ell=log(4/3). Define

    A(t)=integral_a^1 integral_a^1 1_(uv<=t) du dv/(uv).

Changing to log coordinates evaluates this integral:

    A(t)=0,                               t<a^2,
         (1/2)log^2(t/a^2),                a^2<=t<=a,
         ell^2-(1/2)log^2(1/t),            a<=t<=1.    (15)

Then

    sum_(k=b)^(b^2-1) S_Y(k)^2
          ~ C_* b^2/(log b)^4,
    C_*=integral_(a^2)^1 A(t)^2 dt >0.                (16)

Proof: the classical PNT and partial summation give weak convergence of the finite positive measures

    (log b) sum_(p in P_Y) (1/p) delta_(p/b)
         -> 1_[a,1](u)du/u.

Their product measures converge; every boundary uv=t has zero limiting measure. The p=r diagonal has total rescaled weight O(log b/b), so (14) multiplied by (log b)^2 converges to A(t). The total masses stay bounded and the distribution functions are monotone with a continuous limit. One may therefore pass to the Riemann sum of their squares, proving (16). No RH-strength PNT error term is used.

This is NOT an obstruction to a bound for the complete signed native sum: the remaining source products are still present and may compensate it. It is an obstruction to declaring every completely closed source-product packet individually subpower. The observation interval in (16) has length of order Y^2, unlike the order-Y early window in the previous two-logarithm calculation. Those two energies must not be compared as if their intervals were identical.

## 4. A rectangular, mixed-source microscopic upper bound

This section extends MCB31 Section 2 from one source to two sources whose support lengths can be highly unequal. It retains the exact same smooth frequency mask and complete centered tails; it is NOT an estimate for the full frequency range.

Let c,d be finite real balanced sources supported through L_c,L_d, and let integers H>=1 and X satisfy

    X>=8H, L_c L_d<=8X.

For 0<alpha<1 write e(alpha)=exp(2pi i alpha) and

    Z_alpha(k)=sum_(n<=k)e(n alpha)/n+log(1-e(alpha)),

with the radial Abel logarithm. This equals the entire centered tail -sum_(n>k)e(n alpha)/n. Define the C^2 mask

    chi_H(t)=1 for 0<=t<=H;
             1-10u^3+15u^4-6u^5, u=(t-H)/H, H<t<2H;
             0 for t>=2H.

Set

    U_cd(k)=sum_(q=2)^(L_c L_d) B_q(c,d)
             sum_(1<=a<q,gcd(a,q)=1) chi_H(X||a/q||)Z_(a/q)(k).

Here ||alpha|| is distance to the nearest integer. All fractions of distance at most H/X are included at weight one. The smooth transition and all logarithmic constants are retained.

Define x_r=m_c(r), y_s=m_d(s), and

    a_c=max(0,floor(X/(2H L_d))-1),
    a_d=max(0,floor(X/(2H L_c))-1),
    E_c=sum_(a_c<r<L_c)x_r^2,
    E_d=sum_(a_d<s<L_d)y_s^2.                           (17)

**Rectangular microscopic theorem.** For X<=M<2X,

    sum_(k=X)^M |U_cd(k)|^2 <=2^21 H^4 E_c E_d.        (18)

There is NO coefficient-cap hypothesis. This includes the full covariance of all selected denominators and frequencies, but only on the displayed observation block. The values include infinite harmonic tails; the estimate is not a whole-future energy assertion.

### Proof with constants

For fixed k in [X,2X), let

    z_k(t)=2 Re Z_(t/X)(k)
          =2sum_(n<=k)cos(2pi n t/X)/n+2log(2sin(pi t/X)).

On 0<t<=2H<=X/4 the exact derivative is

    z_k'(t)=(2pi/X)cos((2k+1)pi t/X)/sin(pi t/X).

The finite sine-sum identity proves this, including the logarithmic derivative. Abel summation and sin(pi t/X)>=2t/X give, with deliberately loose constants,

    |z_k(t)|<=1/t,
    |t z_k'(t)|<=4,
    |t^2 z_k''(t)|<=64t+8.

Since |chi_H'|<=2/H and |chi_H''|<=6/H^2, g=chi_H z_k satisfies

    |t g'(t)+t^2 g''(t)|<=256H.

These are MCB31's derivative estimates, repeated to expose the dependency. For

    f(v)=sum_(j>=1)g(jX/v), f(0)=0,

only j<2Hv/X enter. Its smooth zero endpoint makes f C^2, including entry points. It vanishes for v<=X/(2H). Differentiation yields

    |f'(v)+v f''(v)|
       <=(1/v)sum_(j<2Hv/X)|t g'(t)+t^2g''(t)|
       <=512H^2/X.                                   (19)

The argument applies for every 0<v<=L_c L_d<=8X, so no square-support assumption has entered.

Unreduce all fractions before taking absolute values:

    U_cd(k)=sum_(r<=L_c,s<=L_d)c(r)d(s)/(rs) f(rs).

Both balances let us sum by parts separately, with no endpoint source term:

    U_cd(k)=sum_(r<L_c,s<L_d)x_r y_s D_k(r,s),
    D_k(r,s)=f(rs)-f((r+1)s)-f(r(s+1))+f((r+1)(s+1)).

Integrating the mixed derivative over a unit rectangle and using (19) gives |D_k|<=512H^2/X. If r<=a_c or s<=a_d, the entire rectangle is inside the zero range of f, so D_k=0. Therefore Cauchy--Schwarz gives

    |U_cd(k)|<=(512H^2/X) sqrt(L_c L_d E_c E_d).

There are at most X observation indices. Squaring and using L_c L_d<=8X proves (18). Every reduction, coalescence, and source sign was retained before this bound. QED.

### Native rectangular consequence and its limit

If c,d are cap-three completions of mu through A,B and M<(A+1)(B+1), (4)--(6) are native on the block. Their source budgets J(c)<=2F_A, J(d)<=2F_B give

    sum_(k=X)^M |U_cd(k)|^2 <=2^23 H^4 F_A F_B,         (20)

provided the support/product/block hypotheses of (18) hold. The localized product (18) is stronger when recent energies are small. If both completions have ended by X, the complete unprojected Q_(c,d)=-m on that block.

This permits asymmetric prefix lengths under a product constraint rather than forcing max(L_c,L_d)^2<=8X through naive polarization. Nevertheless F_A F_B has the same critical scaling as F_(sqrt(AB))^2 under a power-growth model F_N proportional to N^alpha. Asymmetry by itself is not a subcritical gain. No estimate for the complement of the microscopic mask is proved here.

## 5. Exact graph optimizers: finite evidence, not an all-scale spectral-gap theorem

PREVIOUS_PASS.md expresses protected-amplitude cancellation as Ar=-u, with A_(p,k)=1_(p|k)-1_(p|k+1), r=m_h. It yields the exact minimum u^T(AA^T)^+u when feasible. The fresh checker builds the full finite matrix for every prime R<p<=R^2, R=ceil(sqrt(2Y)), and solves it in rational arithmetic for Y=7,15,31,63. In these four panels the matrix is nonsingular; no general nonsingularity claim is inferred from these tests.

It verifies Ar=-u, reconstructs the optimizing source, and proves the finite minimum by an exact orthogonality/Pythagorean certificate against the feasible square-reservoir primitive. The report retains full-source energy and maximum coefficient as well as perturbation energy. Low perturbation energy does not alone prove a low total source energy, and no uniform coefficient cap for these optimizers is claimed.

At Y=63 the exact optimum has descriptive value 0.002562714247369316, versus 0.16646079003853273 for the square-reservoir perturbation. The maximum coefficient in this optimized panel is about 2.41242. These are bounded rational calculations, not a uniform graph-gap bound or evidence that the full covariance decreased on the invariant bulk.

## 6. What remains, stated without substituting another equivalence for a proof

The earlier completion constructions and the exact cancellation results here can improve representations. Equation (9) and the positive bulk packet (14) show precisely why those improvements alone do not supply the missing full bound. Equation (18) is an actual upper bound, but still microscopic and bilinear-critical.

MCB31 still leaves an intermediate angular-frequency loss and lacks a native subquadratic gain. DMC31 controls a high-Mellin projection but leaves low Mellin frequencies; this is a different projection and cannot be identified with MCB31's complement. DCN26's favorable divisor closures and near-ratio bounds still leave a signed far remainder. None of these distinct estimates is silently commuted, summed as orthogonal after restriction, or advertised as complete coverage here.

A conclusion-producing continuation must prove a bound for the full remaining signed native observable, with completion, projection interactions, and tails included. This packet does not establish such a bound. No RH or GRH resolution, new zero-free region, universal negative-covariance sign, or independently certified novelty is claimed.
