# Sharp heavy tails and all fixed moments of the original ramified correction

Status: PROPOSED complete component arguments. Independent mathematical review is required.
No RH, new zeta zero-free region, native inverse-L moment estimate, or full theta/additive pairing bound is claimed.

## 1. Source, quantifiers, and the change from the preceding work

Fix a number field F containing mu_12 and the admissible finite exterior exclusions S. Use the ORIGINAL correction H_u(xi,w,z) in the Poisson source, not its inverse and not a replacement independent-prime model. Here H_u means the exterior Euler correction product; no lower estimate is asserted after multiplication by an arbitrary vanishing finite-S test factor. A fixed nonzero bounded normalization only changes constants. The exact five ramified factors and unramified factor are those of #971, RAMIFIED_FACTORS.md, at commit 3f1d2a07631eb6cca1f2716be01f64e874667639. They are reproduced below at the level needed for the proof. Their identification with the original CT source is a declared imported local-source contract. This pass checks the deduction from that contract, not the full metaplectic construction.

The indices u are the actual sixth-power-free exterior IDEALS a, with a fixed finite list of S-unit labels. Count full ideal norm Na, not the radical or conductor. One fixed label suffices for every lower bound; a fixed finite number only changes constants. All local unit phases can depend arbitrarily on u and on the spectral ordinates, subject to the source relations and Gauss norms. No statistical independence of those phases is used.

Fix real parts (x,y,z0), with 0<x<1/2, in the ORIGINAL enlarged Poisson domain

    x,y,z0>0;
    6z0+y>1, x+6z0>1, x+y>1,
    x+y+6z0>2, 6x+6z0>5.                               (1)

Put delta=1/2-x and alpha=1/(3 delta). Every assertion is uniform in the imaginary parts and permitted phases. Constants may depend on F, S, the fixed real parts (or a compact real-part subdomain with positive margins), and any fixed moment order p. In particular, NO uniform growing-p assertion and NO uniformity as x tends to 0 or 1/2 are made.

For the upper bounds S can be any fixed admissible set. For phase-UNIFORM LOWER bounds enlarge S once to contain all exterior prime ideals of norm at most Q0(x,y,z0), for a sufficiently large fixed Q0. This removes the possibility of an isolated small-prime local zero destroying a lower estimate. This qualification is essential. After this enlargement the source remains fixed as U grows.

Write

    N_U(T)=#{u: Na<=U, |H_u|>T},
    M_p(U)=sum_(Na<=U) |H_u|^p.

### Theorem 1 (a uniform weak-tail bound, with no epsilon loss)

For U>=2 and T>0,

    N_U(T) <= C U T^(-alpha).                            (2)

For every fixed epsilon in (0,1/4), under the lower-bound exclusion above, there are constants c0,c1>0 such that, for all sufficiently large U,

    N_U(c0 R^(3 delta)) >= c1 U/R
    whenever U^epsilon <= R <= U^(1/2-epsilon).          (3)

Thus the exponent alpha is realized by actual ideal indices, not just by a prime-by-prime upper envelope. No limiting distribution or phase-independent asymptotic constant is asserted; the displayed bounds themselves are uniform in each permitted phase profile.

### Theorem 2 (sharp order of every fixed positive moment)

For each fixed real p>0, put A=3p delta. Under the lower-bound exclusions,

    M_p(U) asymp
       U,                          A<1;
       U log(2U),                  A=1;
       U^((A+1)/2),                A>1.                 (4)

The corresponding upper estimates hold for any fixed admissible S. The constants are uniform over ALL the phase profiles allowed in Section 1. These are two-sided orders, NOT leading-constant asymptotics. The endpoint A=1 is included.

For example at x=1/4,

    M_1(U) asymp U,
    M_(4/3)(U) asymp U log U,
    M_2(U) asymp U^(5/4),
    M_4(U) asymp U^2.                                   (5)

The preceding #971 bound states U^(1+epsilon) in the strict range x>1/2-1/(3p). Equation (4) gives the endpoint and the complete complementary range, and removes the arbitrary power loss throughout the stated fixed-margin domain. The p=2, x=1/4 upper bound improves a direct full-norm pointwise majorization from U^(7/4+epsilon) to U^(5/4). It is a bound for H, NOT L, 1/L, B_m, or the original Mobius polynomial.

### Corollary 3 (arbitrary selected sets, with dependence retained)

For ANY subset E of R indices, and 0<p<alpha,

    sum_(u in E)|H_u|^p
       <= C_p U^(p/alpha) R^(1-p/alpha).             (6)

The set can be selected using denominator zeros, numerator values, or the correction itself. This inequality assumes no independence. For x>1/6, p=1 gives

    sum_E |H_u| <= C U^(3 delta) R^(1-3 delta).          (7)

For any complex row array L_u and q>1 with q'=q/(q-1)<alpha, the same estimate and Holder give the explicitly correlated bound

    sum_E |H_u L_u|
       <= C (sum_all |L_u|^q)^(1/q)
                U^(1/alpha) R^(1/q'-1/alpha).           (7a)

No independence from E is needed. This can replace a uniform pointwise correction bound in an appropriately justified future contour calculation. It grants neither a zero-free denominator contour nor an estimate for its reciprocal.

## 2. Exact local input and phase-uniform envelopes

Use q=Np and the notation of #971:

    a=g h theta^(-1) q^(-1/2-xi),
    b=h^3 theta^(-3) q^(-1-3xi),
    r=theta q^(-w), v=q^(-6z), d=-a tau_1,
    e=q^6 b^2 v.

Here |g|=|h|=|theta|=1, |tau_j|=sqrt(q) for j=1,...,5, tau_1 tau_5=q, and the source relation gives |d|=q^-x. The theta at a ramified prime is the UNIT PART of u; it is not the zero-valued extracted L-character. The latter character's Euler factor is absent at that prime. This distinction preserves the original nonunit convention.

For j=v_p(a) in {1,...,5}, the exact source identity is H_j=N_j/(1-e), where

    N1=1-e/q+d r(1-qv),
    N2=1-e/q-(q-1)d r+(1-v)q^2 b tau_3,
    N3=1-e/q-(q-1)d r+(1-v)(q^2 b tau_1 tau_2 r+q^3 a b tau_4),
    N4=1-e/q-(q-1)d r+(1-v)q^3 a b tau_1 tau_3 r,
    N5=1-e/q-(q-1)d r-(1-v)q^5 b^2.                     (8)

For j=0, with W=theta q^-w and D=d,

    F0=1/(1-v)+W/(1-W)
       +e/(1-e)[(1-q^-1)/(1-v)+W]
       -D/(1-e)[1+(q-1)Wv/(1-v)],
    H0=(1-v)(1-W)F0/(1-D).                             (9)

On (1), |v|=q^(-6z0), |e|=q^(4-6x-6z0), and |dr|=q^(-x-y). Each denominator in (8)-(9) is bounded away from zero for large q; all remaining finitely many denominators have modulus bounded below by a positive constant. Define

    eta0=min(6z0+y-1, x+6z0-1, x+y-1,
              x+y+6z0-2, 6x+6z0-5)>0,
    kappa=min(3 delta,6z0,1)>0.

Equations (8)-(9), with their actual correlated phases retained, imply

    H0=1+O(q^(-1-eta0)),
    H1=1+O(q^(-1-eta0)),
    |H2|=q^(3 delta)(1+O(q^-kappa)),
    |H3|<=C q^(4 delta),
    |H4|<=C q^(3 delta),
    |H5|<=C q^(6 delta).                               (10)

For H0 use the five errors of #971 (9), including their actual denominators. H1-1 has the terms e(1-1/q)/(1-e) and dr(1-qv)/(1-e); (1) makes all three resulting magnitudes O(q^(-1-eta0)). For H2 the unique dominant summand is (1-v)q^2 b tau_3, of modulus q^(3 delta)(1+O(q^(-6z0))); all other numerator summands are O(1). Division by 1-e contributes O(q^(-1-eta0)). This proves its relative bound with the stated kappa.

For H3 the two extra magnitudes are q^(2-3x-y) and q^(2-4x). Since x+y>1, the first is at most q^(2 delta), while the second equals q^(4 delta). For H4 its extra magnitude q^(5/2-4x-y) is at most q^(3 delta). For H5 it is q^(3-6x)=q^(6 delta). These estimates show that the valuation-two branch controls the heavy-tail threshold throughout the full domain, not just on a special right-hand slice.

Finite excluded norms and finitely many remaining small primes change upper constants only. Under the extra lower-bound exclusions, choose Q0 so that the H0/H1 errors have modulus <1/2 and the relative H2 error has modulus <1/2. Since sum_p q^(-1-eta0)<infinity, products of all H0 and H1 factors are bounded above and away from zero, uniformly in u and phases.

Write uniquely

    a=b0 c^2 d0^3 e0^4 f0^5,                            (11)

where the five ideals are squarefree and PAIRWISE COPRIME. Unlike the earlier decomposition n=c d^6, (11) DOES require coprimality: each prime goes into its unique exact-valuation slot. This is not an additional restriction on the original family.

With the positive kappa just defined, put

    g(c)=product_(p|c)(1+C q^-kappa),
    K(d0,e0,f0)=C^(omega(d0)+omega(e0)+omega(f0))
                  (Nd0)^(4 delta)(Ne0)^(3 delta)(Nf0)^(6 delta).

Then (10) yields, uniformly,

    |H_u| <= C g(c) (Nc)^(3 delta) K(d0,e0,f0).          (12)

For indices a=b0 c^2 only, under the lower-bound exclusions,

    |H_u| >= c (Nc)^(3 delta)
                exp(-C sum_(p|c) q^-kappa).             (13)

No factor in (12) or (13) is replaced by an independent random variable.

## 3. Proof of the weak upper tail

We need an elementary ideal-counting fact. For every FIXED r>0,

    sum_(Nc<=L) g(c)^r <= C_r L, L>=1.                  (14)

Extend g to all ideals by its radical. Its nonnegative divisor expansion has local coefficient h(p)=g(p)^r-1=O_r(q^-kappa), h(p^j)=0 for j>1. Thus g(c)^r=sum_(d|c)h(d), and

    sum_d h(d)/Nd=product_p(1+O_r(q^(-1-kappa)))<infinity.

Fixed-field ideal counting I_F(L)<=C_F L proves (14). This argument also bounds the squarefree subfamily.

For V>0 choose r>alpha. Dyadically summing (14) and Markov's inequality gives

    sum_(c: g(c)(Nc)^(3 delta)>V) 1/(Nc)^2 <= C V^-alpha. (15)

Indeed let R=V^alpha. A dyad Nc~C has mass at most

    C^-1 min(1,(C/R)^(3 delta r))

up to fixed constants. Sum below and above R; 3 delta r>1 makes both sums O(1/R). If R<1, the whole ideal zeta sum at 2 is O(1)<=O(1/R). Thus (15) covers every V>0; no hidden cutoff or logarithm remains.

For fixed c,d0,e0,f0 in (11), the number of possible b0 is at most

    C U / [(Nc)^2(Nd0)^3(Ne0)^4(Nf0)^5].

Dropping its coprimality and squarefree restrictions is legal ONLY in this positive count. Use (12), apply (15) at V=T/(C K), and sum the remaining three ideals. At alpha=1/(3 delta) their weighted denominators have exponents

    3-4/3=5/3,   4-1=3,   5-2=3.

Consequently

    sum_(d0,e0,f0) K^alpha/[(Nd0)^3(Ne0)^4(Nf0)^5]<infinity.

All constants C^omega are summable at these exponents. This proves (2), for the complete family and all original label choices. Layer-cake integration of min(R,C U T^-alpha) proves (6): its integral against p T^(p-1)dT is finite precisely when p<alpha.

## 4. Complete moment upper bounds, including the sharp endpoint

A weak-tail bound alone is not used to invent a pointwise maximum. We instead prove the moment estimates directly, keeping the full prime-power support.

Set A=3p delta and sigma0=max(1,(A+1)/2). By (10), after one global constant covering H0/H1, a multiplicative positive majorant for |H_u|^p has local series

    P_q(s)=1+q^-s+q^(A-2s)(1+C q^-kappa)^p
             +C_p[q^(4A/3-3s)+q^(A-4s)+q^(2A-5s)].      (16)

Outside S divide its formal ideal Dirichlet series by

    zeta_F^S(s) zeta_F^S(2s-A).                          (17)

At s=sigma0, the absolute coefficient mass of the local quotient minus 1 is O(q^(-1-eta0)) for some eta0>0. To check this WITHOUT an analytic continuation hypothesis: the two first-order terms q^-s and q^(A-2s) cancel against (1-q^-s)(1-q^(A-2s)). Each has critical magnitude <=q^-1. The H2 error is O(q^(-1-kappa)). The remaining three exponents are at most -5/3,-3,-3, respectively, for every A>=0. All products of two first-order terms are O(q^-2). Thus one may take eta0=min(kappa,2/3), with a constant depending on p,x. The finitely many local exceptions have finite mass.

If h is the resulting SIGNED coefficient sequence, this proves

    sum_a |h(a)|/(Na)^sigma0<infinity.                  (18)

The coefficients of (17) are nonnegative and its prefix is exactly

    V_A(U)=sum_(Nb<=sqrt U) (Nb)^A I_S(U/(Nb)^2).

Ideal counting and partial summation give

    V_A(U) << U (A<1),
    V_1(U) << U log(2U),
    V_A(U) << U^((A+1)/2) (A>1).                        (19)

Convolution with |h| and (18) preserves each bound; at A=1 use log(2U/Nd)<=log(2U). All coefficient identities are formal finite divisor identities before any summation. Equations (16)-(19) prove every upper estimate in (4), without an epsilon exponent. No unknown zeta zero is crossed and no claim of nonvanishing of the quotient is needed.

## 5. Lower bounds on actual full-norm rows

We record the elementary counting fact used here. For fixed S, sufficiently large B,C have at least c B C pairs of squarefree S-coprime ideals b,c in B<Nb<=2B, C<Nc<=2C with (b,c)=1. The same statement with b=1 has at least c C admissible c. Moreover a positive fraction can be required to satisfy

    sum_(p|c) q^-kappa <= M                             (20)

for a sufficiently large fixed M.

Proof: impose S-coprimality and the squarefree/pairwise-coprime conditions first at the finitely many primes of norm <=L. Fixed-field ideal counting and finite inclusion-exclusion give a dyadic pair density equal to a fixed positive S-factor times product_(p notin S, Np<=L)(1-3/q^2+2/q^3), times the square of the ideal-count residue. This product stays bounded away from zero as L grows. The pairs spoiled by a square p^2 dividing either variable or a shared p outside that finite set are at most C_F B C sum_(Np>L)(Np)^-2. Choose a fixed L making this tail smaller than half the positive limiting density. Ideal counting bounds the tail by O_F(1/L). The one-variable squarefree argument instead uses product(1-q^-2). Finally the total of the nonnegative quantity in (20) over all pairs is <=C_F B C sum_p q^(-1-kappa). Markov, with M sufficiently large relative to the preceding positive density, removes less than half the clean pairs. This proof uses only fixed-field counting (including its usual pole-at-one asymptotic) and convergent ideal sums; it is uniform once both dyadic lengths tend to infinity, with no relation between their rates required. The finite-sieve density claim can equivalently be obtained by its finite inclusion-exclusion expansion. No short-interval prime theorem is used.

For (3), choose c in a fixed-factor dyad around R and b in a dyad around U/(K R^2), with K a sufficiently large absolute scale constant so Nb (Nc)^2<=U. In the stated R-range both lengths tend to infinity. Clean pairs give c U/R distinct ideals a=b c^2. Equation (13) and (20) put |H_u| above c0 R^(3 delta). Uniqueness of (11) prevents duplicate counting. This proves (3).

If A<1, squarefree a alone give M_p(U)>>U: all its ramified factors are H1 and their product is bounded away from zero. If A>1, take a=c^2 with Nc in a fixed dyad below sqrt U and impose (20). There are >>sqrt U such indices, each contributing >>U^(A/2). Hence M_p(U)>>U^((A+1)/2).

At A=1, take disjoint dyadic c ranges from U^(1/16) to U^(1/4), and corresponding b ranges around U/(K (Nc)^2) as above. Each range has >>U/R clean pairs and each contributes >>R to |H_u|^p, hence >>U per range. There are a positive constant times log U disjoint exact-valuation ranges, proving M_p(U)>>U log U. This completes (4).

## 6. What the attack achieved and what failed

The bound is for the complete original correction family throughout the stated fixed-margin subcritical part of its Poisson domain. Its heavy tail is caused by the valuation-TWO term, not by a hypothetical zeta zero. It explains exactly why arbitrarily high correction moments cannot be treated as uniformly diagonal-sized below Re xi=1/2. Replacing this tail by an epsilon loss would be false. The selected-set bound (6) gives a rigorously priced substitute, even for adaptively selected zero classes.

I also tested the latest #976 theta hierarchy against the missing additive factor. Its published complete moments are source-qualified estimates for B_m, not for Mobius sums. The only supplied additive norm is l^2. Converting it to the conjugate of l^(2k) costs N^(1/2-1/(2k)); its multiplication with [N+(N^2/Z)^k]^(1/(2k)) gives no power improvement over the old second-moment pairing. That failure is already established in #976 and is NOT claimed as new.

A direct character-orthogonality attempt at the joint pairing must also retain the exact reflected row coefficient rho(d). The freshly read OpenAI 04-reflection.tex, equations reflection-row-factor and reflection-column-factor, show that rho contains local omega_p and the factors chi_p((d/p)^(-2)), not merely a fixed Dirichlet character. Replacing it by 1 would permit a tempting short-conductor cancellation argument but would change the source. This pass does NOT claim that argument for the original theta pairing.

The remaining full-proof target is still the signed principal inverse-L moment/energy or a proved zero-sensitive physical projection. Theorem 2 is an all-fixed-moment theorem for a different factor in that calculation. It supplies no missing denominator estimate, no contour through zeros, and no full RH resolution. No worldwide literature-priority claim is made for ideal counting, Euler comparison, layer-cake, or weak-Lp methods.
